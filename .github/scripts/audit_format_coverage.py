#!/usr/bin/env python3
"""Read-only cross-format coverage audit for Surge rule files.

No rule files are modified. Only documented format pairs are compared:
standard/Resolve, All/All_No_Resolve, No_IPv6/No_IPv6_Resolve, and
standard/No_IPv6. Domain-only exports are recorded but not inferred to be
equivalent to RULE-SET files.
"""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import argparse, json

ROOT = Path("Rule/Upstream")
SUFFIXES = (
    ("_All_No_Resolve", "all_no_resolve"),
    ("_No_IPv6_Resolve", "no_ipv6_resolve"),
    ("_NoIPv6_Resolve", "no_ipv6_resolve"),
    ("_All_NoResolve", "all_no_resolve"),
    ("_No_Resolve", "no_resolve"),
    ("_NoResolve", "no_resolve"),
    ("_No_IPv6", "no_ipv6"),
    ("_NoIPv6", "no_ipv6"),
    ("_Resolve", "resolve"),
    ("_Domain", "domain_only"),
    ("_All", "all"),
)

def identify_format(path):
    stem = path.stem
    for suffix, fmt in SUFFIXES:
        if stem.endswith(suffix):
            return stem[:-len(suffix)], fmt
    return stem, "standard"

def load_rules(path):
    rules = set()
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", ";", "//")):
            continue
        rules.add(line)
    return rules

def normalize_rule(rule, strip_no_resolve=False, remove_ipv6=False):
    parts = [x.strip() for x in rule.split(",")]
    if len(parts) < 2:
        return rule.strip().casefold()
    kind = parts[0].upper()
    if remove_ipv6 and kind == "IP-CIDR6":
        return None
    if strip_no_resolve and kind in {"IP-CIDR", "IP-CIDR6"}:
        parts = [parts[0], parts[1]] + [x for x in parts[2:] if x.casefold() != "no-resolve"]
    return ",".join(parts).casefold()

def normalized_set(rules, strip_no_resolve=False, remove_ipv6=False):
    result = set()
    for rule in rules:
        value = normalize_rule(rule, strip_no_resolve, remove_ipv6)
        if value is not None:
            result.add(value)
    return result

def compare_pair(directory, base, left_fmt, right_fmt, files, strip_no_resolve=False, remove_ipv6_left=False, remove_ipv6_right=False):
    left_path = files[left_fmt]
    right_path = files[right_fmt]
    left_raw = load_rules(left_path)
    right_raw = load_rules(right_path)
    left = normalized_set(left_raw, strip_no_resolve, remove_ipv6_left)
    right = normalized_set(right_raw, strip_no_resolve, remove_ipv6_right)
    left_only = sorted(left - right)
    right_only = sorted(right - left)
    return {
        "directory": str(directory),
        "app": base,
        "left_format": left_fmt,
        "left_file": str(left_path),
        "right_format": right_fmt,
        "right_file": str(right_path),
        "left_rules": len(left_raw),
        "right_rules": len(right_raw),
        "left_only_count": len(left_only),
        "right_only_count": len(right_only),
        "left_only_examples": left_only[:20],
        "right_only_examples": right_only[:20],
        "status": "MATCH" if not left_only and not right_only else "DIFFERENCE_REVIEW_ONLY",
    }

def audit(root):
    grouped = defaultdict(dict)
    for path in sorted(root.rglob("*.list")):
        if path.is_symlink():
            raise RuntimeError("Symlink encountered during format audit: " + str(path))
        base, fmt = identify_format(path)
        if fmt in grouped[(path.parent, base)]:
            raise RuntimeError("Duplicate format in one App directory: " + str(path.parent / base) + " [" + fmt + "]")
        grouped[(path.parent, base)][fmt] = path

    pairs = []
    skipped = []
    for (directory, base), files in sorted(grouped.items(), key=lambda x: (str(x[0][0]).casefold(), x[0][1].casefold())):
        pair_specs = [
            ("standard", "resolve", True, False, False, "standard_vs_resolve"),
            ("all", "all_no_resolve", True, False, False, "all_vs_all_no_resolve"),
            ("no_ipv6", "no_ipv6_resolve", True, False, False, "no_ipv6_vs_no_ipv6_resolve"),
            ("standard", "no_ipv6", False, True, False, "standard_vs_no_ipv6"),
            ("resolve", "no_ipv6_resolve", False, True, False, "resolve_vs_no_ipv6_resolve"),
        ]
        found = False
        for left, right, strip_nr, rm_left6, rm_right6, label in pair_specs:
            if left in files and right in files:
                row = compare_pair(directory, base, left, right, files, strip_nr, rm_left6, rm_right6)
                row["comparison"] = label
                pairs.append(row)
                found = True
        if "domain_only" in files:
            skipped.append({
                "directory": str(directory),
                "app": base,
                "format": "domain_only",
                "file": str(files["domain_only"]),
                "reason": "DOMAIN-SET export has distinct parser/consumer semantics; not compared as a RULE-SET twin."
            })

    summary = Counter(x["status"] for x in pairs)
    return {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "READ_ONLY_FORMAT_COVERAGE_AUDIT",
        "root": str(root),
        "format_pairs_checked": len(pairs),
        "matching_pairs": summary["MATCH"],
        "pairs_with_differences": summary["DIFFERENCE_REVIEW_ONLY"],
        "domain_only_exports_skipped": len(skipped),
        "pairs": pairs,
        "domain_only_skipped": skipped,
        "safety": "Report only. No rule file is modified, deleted, merged, renamed, or restored. Differences are review findings, not automatic merge instructions."
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--output", default="batch-output/format-coverage.json")
    args = ap.parse_args()
    root = Path(args.root)
    if root.is_symlink() or not root.is_dir():
        raise SystemExit("Rule/Upstream root missing or unsafe")
    report = audit(root)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "format_pairs_checked": report["format_pairs_checked"],
        "matching_pairs": report["matching_pairs"],
        "pairs_with_differences": report["pairs_with_differences"],
        "domain_only_exports_skipped": report["domain_only_exports_skipped"],
        "report": str(out)
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
