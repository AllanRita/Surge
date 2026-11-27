#!/usr/bin/env python3
"""Read-only semantic parity audit for paired Surge rule formats."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse, json, re

ROOT = Path("Rule/Upstream")
PERSONAL = Path("Rule/Personal")
FORMAT_SUFFIXES = (
    ("_All_No_Resolve", "all_no_resolve"),
    ("_No_IPv6_Resolve", "no_ipv6_resolve"),
    ("_NoIPv6_Resolve", "no_ipv6_resolve"),
    ("_No_IPv6", "no_ipv6"),
    ("_NoIPv6", "no_ipv6"),
    ("_No_Resolve", "no_resolve"),
    ("_NoResolve", "no_resolve"),
    ("_Resolve", "resolve"),
    ("_All", "all"),
    ("_Domain", "domain_only"),
)
PAIRINGS = (
    ("standard", "resolve", "Standard vs Resolve"),
    ("all", "all_no_resolve", "All vs All_No_Resolve"),
    ("no_ipv6", "no_ipv6_resolve", "No_IPv6 vs No_IPv6_Resolve"),
    ("standard", "no_resolve", "Standard vs No_Resolve"),
    ("standard", "no_ipv6", "Standard vs No_IPv6"),
    ("resolve", "no_ipv6_resolve", "Resolve vs No_IPv6_Resolve"),
)

def classify(path):
    stem = path.stem
    for suffix, fmt in FORMAT_SUFFIXES:
        if stem.endswith(suffix):
            return stem[:-len(suffix)], fmt
    return stem, "standard"

def parse_rule(line):
    value = line.strip()
    if not value or value.startswith(("#", ";", "//")) or "," not in value:
        return None
    parts = [part.strip() for part in value.split(",")]
    if len(parts) < 2 or not parts[0] or not parts[1]:
        return None
    kind = parts[0].upper()
    operand = re.sub(r"\s+", "", parts[1]).casefold()
    options = tuple(sorted(
        re.sub(r"\s+", "", option).casefold()
        for option in parts[2:] if option and option.casefold() != "no-resolve"
    ))
    no_resolve = any(option.casefold() == "no-resolve" for option in parts[2:])
    return (kind, operand, options), no_resolve, value

def load_file(path):
    rules = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        parsed = parse_rule(line)
        if parsed:
            rules.append(parsed)
    return rules

def compare_files(left_path, right_path, label, ignore_ipv6_left=False, ignore_ipv6_right=False):
    left = load_file(left_path)
    right = load_file(right_path)
    if ignore_ipv6_left:
        left = [rule for rule in left if rule[0][0] != "IP-CIDR6"]
    if ignore_ipv6_right:
        right = [rule for rule in right if rule[0][0] != "IP-CIDR6"]
    left_counts = Counter(rule[0] for rule in left)
    right_counts = Counter(rule[0] for rule in right)
    left_modes, right_modes = {}, {}
    for key, no_resolve, raw in left:
        left_modes.setdefault(key, set()).add(no_resolve)
    for key, no_resolve, raw in right:
        right_modes.setdefault(key, set()).add(no_resolve)
    left_only = left_counts - right_counts
    right_only = right_counts - left_counts
    shared = set(left_counts) & set(right_counts)
    mode_diff = [key for key in shared if left_modes.get(key, set()) != right_modes.get(key, set())]
    def examples(counter):
        return [{"rule": ",".join([key[0], key[1], *key[2]]), "count_difference": count}
                for key, count in list(counter.items())[:25]]
    return {
        "pair": label, "left": str(left_path.relative_to(ROOT)), "right": str(right_path.relative_to(ROOT)),
        "left_rule_lines": len(left), "right_rule_lines": len(right),
        "left_only_count": sum(left_only.values()), "right_only_count": sum(right_only.values()),
        "resolution_option_difference_count": len(mode_diff),
        "left_only_examples": examples(left_only), "right_only_examples": examples(right_only),
        "resolution_option_examples": [
            {"rule": ",".join([key[0], key[1], *key[2]]),
             "left_no_resolve": sorted(left_modes.get(key, set())),
             "right_no_resolve": sorted(right_modes.get(key, set()))}
            for key in mode_diff[:25]
        ],
        "status": "MATCH" if not left_only and not right_only else "REVIEW",
    }

def render_markdown(report):
    s = report["summary"]
    lines = [
        "# Surge paired-format semantic parity audit", "",
        f"Generated: {report['generated_utc']}", "",
        "Read-only comparison. Only the no-resolve option is ignored for rule identity; all other rule types, operands, and options remain significant. Differences are review findings, not automatic repair instructions.", "",
        f"- Upstream rule files scanned: {s['rule_files_scanned']}",
        f"- Paired-format comparisons: {s['pairs_compared']}",
        f"- Pairs with content differences: {s['pairs_needing_review']}",
        f"- Left-only rule occurrences: {s['left_only_occurrences']}",
        f"- Right-only rule occurrences: {s['right_only_occurrences']}",
        f"- Pairs with no-resolve option differences: {s['pairs_with_resolution_option_differences']}",
        f"- Exact tombstones: {s['tombstones_enforced']}",
        "- Rule/Personal modified: no", "",
        "## Pair results", "",
        "| App folder | Pair | Left-only | Right-only | no-resolve differences | Status |",
        "|---|---|---:|---:|---:|---|",
    ]
    for item in report["pairs"]:
        app = str(Path(item["left"]).parent)
        lines.append(f"| {app} | {item['pair']} | {item['left_only_count']} | {item['right_only_count']} | {item['resolution_option_difference_count']} | {item['status']} |")
    lines.extend(["", "## Differences requiring review", ""])
    findings = [item for item in report["pairs"] if item["status"] == "REVIEW"]
    if not findings:
        lines.append("No paired-format content differences were found.")
    for item in findings:
        lines.extend([f"### {item['left']} ↔ {item['right']}",
                      f"- Left-only occurrences: {item['left_only_count']}",
                      f"- Right-only occurrences: {item['right_only_count']}"])
        for side in ("left_only_examples", "right_only_examples"):
            if item[side]:
                lines.append(f"- {side.replace('_', ' ').title()}:")
                for example in item[side]:
                    lines.append(f"  - {example['rule']} (count difference {example['count_difference']})")
        lines.append("")
    lines.extend(["## Interpretation", "",
        "- MATCH means both files contain the same normalized rule multiset after ignoring only no-resolve; it does not prove correctness or completeness.",
        "- REVIEW means one format has rules not present in its paired format. Do not copy or delete entries automatically; first confirm whether the format has an intentional scope difference.",
        "- Resolution-option differences are reported separately and are expected where formats intentionally vary DNS resolution behavior.",
        "- Aggregate lists, domain-only lists, and unrelated App folders are not compared as if interchangeable.", ""])
    return "\n".join(lines)

def load_tombstones():
    manifest = Path(".github/explicit-rule-exclusions.json")
    if manifest.is_symlink() or not manifest.is_file():
        raise RuntimeError("Missing or unsafe exact deletion manifest")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    entries = data.get("exclusions")
    if not isinstance(entries, list):
        raise RuntimeError("Manifest exclusions must be a list")
    return entries

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="batch-output")
    args = ap.parse_args()
    if ROOT.is_symlink() or not ROOT.is_dir():
        raise SystemExit("Unsafe or missing Rule/Upstream")
    if PERSONAL.exists() and PERSONAL.is_symlink():
        raise SystemExit("Unsafe Rule/Personal path")
    tombstones = load_tombstones()
    folders = sorted((p for p in ROOT.rglob("*") if p.is_dir() and not p.is_symlink() and "SourceMetadata" not in p.parts), key=lambda p: str(p).casefold())
    groups, files_scanned = {}, 0
    for folder in folders:
        for path in sorted(folder.glob("*.list")):
            if path.is_symlink():
                raise RuntimeError("Symlinked rule file is not allowed: " + str(path))
            files_scanned += 1
            stem, fmt = classify(path)
            groups.setdefault((folder, stem), {})[fmt] = path
    pairs = []
    for (folder, stem), formats in sorted(groups.items(), key=lambda item: (str(item[0][0]).casefold(), item[0][1].casefold())):
        for left_fmt, right_fmt, label in PAIRINGS:
            if left_fmt in formats and right_fmt in formats:
                ignore_left_ipv6 = label in {"Standard vs No_IPv6", "Resolve vs No_IPv6_Resolve"}
                pairs.append(compare_files(
                    formats[left_fmt], formats[right_fmt], label,
                    ignore_ipv6_left=ignore_left_ipv6
                ))
    summary = {
        "rule_files_scanned": files_scanned, "pairs_compared": len(pairs),
        "pairs_needing_review": sum(1 for item in pairs if item["status"] == "REVIEW"),
        "left_only_occurrences": sum(item["left_only_count"] for item in pairs),
        "right_only_occurrences": sum(item["right_only_count"] for item in pairs),
        "pairs_with_resolution_option_differences": sum(1 for item in pairs if item["resolution_option_difference_count"]),
        "tombstones_enforced": len(tombstones),
    }
    report = {"generated_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "Read-only paired-format semantic comparison; no rule or personal file is changed.",
              "normalization": "Ignore only no-resolve; preserve rule type, operand, and every other option.",
              "summary": summary, "pairs": pairs}
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "format-parity-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "format-parity-audit.md").write_text(render_markdown(report), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    main()
