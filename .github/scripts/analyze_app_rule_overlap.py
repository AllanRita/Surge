#!/usr/bin/env python3
"""Build non-destructive app-overlap and additional-source coverage reports."""
from pathlib import Path
from collections import defaultdict
from itertools import combinations
import json
import re
from datetime import datetime, timezone

ROOT = Path("Rule/Upstream")
META = ROOT / "SourceMetadata"
SCENARIO_SUFFIXES = (
    ("_All_No_Resolve", "all_no_resolve"),
    ("_All_NoResolve", "all_no_resolve"),
    ("_No_Resolve", "no_resolve"),
    ("_No_IPv6", "no_ipv6"),
    ("_NoIPv6", "no_ipv6"),
    ("_Resolve", "resolve"),
    ("_Domain", "domain_only"),
    ("_All", "all"),
)
ALIASES = {"pchometw": "pchome", "scholar": "globalscholar", "bardai": "gemini", "abematv": "abema"}
AGGREGATE_APPS = {
    "adguarddnsfilter", "advertising", "advertisinglite", "advertisingtest",
    "advertisingmitv", "china", "chinamax", "chinamaxnoip", "chinamaxnomedia",
    "chinanomedia", "chinatest", "chinaips", "chinaipstest", "chinaasn",
    "global", "globalmedia", "cloud", "game", "block", "process", "proxy",
    "proxylite", "direct", "privacy", "asianmedia", "usmedia", "iptvmainland",
    "iptvother", "lan", "mail", "systemota", "download", "classic",
    "developer", "marketing", "privatetracker", "stun", "hijacking",
}

def norm(value):
    return re.sub(r"[^a-z0-9]+", "", value.lower())

def split_variant(stem):
    for suffix, scenario in SCENARIO_SUFFIXES:
        if stem.endswith(suffix):
            return stem[:-len(suffix)], scenario
    return stem, "standard"

def read_rules(path):
    rules = set()
    domains = set()
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError):
        return rules, domains
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith(("#", ";", "//")):
            continue
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 2:
            continue
        kind, value = parts[0].upper(), parts[1].lower()
        rules.add(line)
        if kind in {"DOMAIN", "DOMAIN-SUFFIX", "HOST", "HOST-SUFFIX"}:
            domains.add((kind, value))
    return rules, domains

files = sorted(ROOT.rglob("*.list"))
records = []
for path in files:
    rel = path.relative_to(ROOT)
    stem = path.stem
    base, scenario = split_variant(stem)
    category = rel.parts[0] if rel.parts else "unknown"
    app_folder = rel.parts[-2] if len(rel.parts) >= 3 else base
    app_key = ALIASES.get(norm(app_folder), norm(app_folder))
    all_rules, domain_rules = read_rules(path)
    records.append({
        "path": str(path),
        "category": category,
        "app": app_key,
        "display_app": app_folder,
        "scenario": scenario,
        "base": base,
        "all_rules": all_rules,
        "domains": domain_rules,
    })

# Same App name in different top-level categories, keeping resolution modes apart.
app_groups = defaultdict(list)
for rec in records:
    if rec["scenario"] in {"standard", "resolve"}:
        app_groups[(rec["app"], rec["scenario"])].append(rec)

same_app_candidates = []
for (app, scenario), group in sorted(app_groups.items()):
    categories = sorted({x["category"] for x in group})
    if len(categories) < 2:
        continue
    group = sorted(group, key=lambda x: x["path"])
    common = set.intersection(*(x["domains"] for x in group)) if group else set()
    union = set.union(*(x["domains"] for x in group)) if group else set()
    common_rules = set.intersection(*(x["all_rules"] for x in group)) if group else set()
    union_rules = set.union(*(x["all_rules"] for x in group)) if group else set()
    exact_same = bool(group) and all(x["all_rules"] == group[0]["all_rules"] for x in group[1:])
    differences = []
    for item in group:
        other = set.union(*(x["all_rules"] for x in group if x is not item)) if len(group) > 1 else set()
        only = sorted(item["all_rules"] - other)
        if only:
            differences.append((item["path"], only))
    same_app_candidates.append({
        "app": app, "scenario": scenario, "categories": categories,
        "files": group, "common_count": len(common), "union_count": len(union),
        "common_rule_count": len(common_rules), "union_rule_count": len(union_rules),
        "identical": exact_same, "differences": differences,
    })

# Cross-app overlap uses exact domain-rule tokens only. These are review candidates.
standard_records = [
    x for x in records
    if x["scenario"] == "standard"
    and x["app"] not in AGGREGATE_APPS
    and len(x["domains"]) >= 5
]
inverted = defaultdict(list)
for i, rec in enumerate(standard_records):
    for token in rec["domains"]:
        inverted[token].append(i)
pair_counts = defaultdict(int)
for indexes in inverted.values():
    unique_indexes = sorted(set(indexes))
    for i, j in combinations(unique_indexes, 2):
        if standard_records[i]["app"] != standard_records[j]["app"]:
            pair_counts[(i, j)] += 1
overlap_candidates = []
for (i, j), shared in pair_counts.items():
    a, b = standard_records[i], standard_records[j]
    smaller = min(len(a["domains"]), len(b["domains"]))
    union_size = len(a["domains"] | b["domains"])
    jaccard = shared / union_size if union_size else 0
    containment = shared / smaller if smaller else 0
    if shared >= 5 and (jaccard >= 0.55 or (smaller >= 5 and containment >= 0.85)):
        overlap_candidates.append({
            "a": a, "b": b, "shared": shared, "jaccard": jaccard,
            "containment": containment, "examples": sorted(a["domains"] & b["domains"])[:8],
        })
overlap_candidates.sort(key=lambda x: (x["jaccard"], x["shared"]), reverse=True)

# Cross-author source contribution coverage against the final target list.
SOURCE_TARGETS = {
    "Aoang-Apple": "Apple/Apple.list",
    "Aoang-DNS": "Block/DNS/DNS.list",
    "Aoang-OneDrive": "Microsoft/Microsoft.list",
    "Aoang-Other": "Block/Other/Other.list",
    "Aoang-Parallels": "Block/Parallels/Parallels.list",
    "Aoang-Process": "Process/Process/Process.list",
    "Aoang-Teams": "Microsoft/Microsoft.list",
    "Aoang-Unavailable": "Process/Unavailable/Unavailable.list",
    "Aoang-YouTube": "Block/YouTube/YouTube.list",
    "Apple": "Apple/Apple.list",
    "BiliBiliIntl": "BiliBiliIntl/BiliBiliIntl.list",
    "GitLab": "GitLab/GitLab.list",
    "Microsoft": "Microsoft/Microsoft.list",
    "NetEaseMusic": "NetEaseMusic/NetEaseMusic.list",
    "Telegram": "Telegram/Telegram.list",
}

def source_rule_coverage(rule, target_rules):
    if rule in target_rules:
        return "exact"
    parts = rule.split(",")
    if len(parts) < 2:
        return "missing"
    kind, value = parts[0].upper(), parts[1].strip().lower()
    if kind in {"DOMAIN", "DOMAIN-SUFFIX", "HOST", "HOST-SUFFIX"}:
        for existing in target_rules:
            ep = existing.split(",")
            if len(ep) < 2 or ep[0].upper() not in {"DOMAIN-SUFFIX", "HOST-SUFFIX"}:
                continue
            suffix = ep[1].strip().lower()
            if value == suffix or value.endswith("." + suffix):
                if len(suffix.split(".")) == 1:
                    return "covered_by_single_label_suffix"
                return "covered_by_parent_suffix"
    return "missing"

source_rows = []
for name, target_rel in sorted(SOURCE_TARGETS.items()):
    meta_path = META / (name + ".json")
    if not meta_path.is_file():
        source_rows.append({"name": name, "target": target_rel, "error": "metadata missing"})
        continue
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        source_rows.append({"name": name, "target": target_rel, "error": "invalid metadata: " + str(exc)})
        continue
    target = ROOT / target_rel
    if not target.is_file():
        source_rows.append({"name": name, "target": target_rel, "error": "target missing"})
        continue
    target_rules, _ = read_rules(target)
    rules = meta.get("rules", [])
    counts = defaultdict(int)
    missing = []
    for rule in rules:
        result = source_rule_coverage(rule, target_rules)
        counts[result] += 1
        if result == "missing":
            missing.append(rule)
    source_rows.append({
        "name": name, "source": meta.get("source", "unknown"),
        "license": meta.get("license", "unknown"),
        "commit": meta.get("commit", "unknown"),
        "source_path": meta.get("path", "unknown"), "target": target_rel,
        "source_count": len(rules), "exact": counts["exact"],
        "parent_suffix_covered": counts["covered_by_parent_suffix"],
        "single_label_suffix_covered": counts["covered_by_single_label_suffix"],
        "missing": missing,
    })

stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
app_lines = [
    "# App-level rule overlap report", "",
    f"Generated: {stamp}", "",
    f"- Rule files scanned: {len(files)}",
    f"- App/scenario candidate groups across categories: {len(same_app_candidates)}",
    f"- High-overlap cross-App pairs for manual review: {len(overlap_candidates)}",
    "",
    "## Same App candidates across categories", "",
    "Grouped by normalized app-folder name and scenario. A match is a review candidate, not permission to merge. Standard and Resolve are analyzed separately.",
]
if not same_app_candidates:
    app_lines.append("- None")
for item in same_app_candidates:
    app_lines += [
        "", f"### {item['app']} ({item['scenario']})",
        f"- Categories: {', '.join(item['categories'])}",
        f"- Exact shared rule lines: {item['common_rule_count']}; union: {item['union_rule_count']}",
        f"- Same full rule set: {'yes' if item['identical'] else 'no'}",
        f"- Exact shared domain rules: {item['common_count']}; domain union: {item['union_count']}",
    ]
    for rec in item["files"]:
        app_lines.append(f"- File: {rec['path']} ({len(rec['all_rules'])} total rules; {len(rec['domains'])} domain rules)")
    for path, only in item["differences"]:
        app_lines.append(f"- Only in {path}: {len(only)}")
        for rule in only[:12]:
            app_lines.append(f"  - {rule}")
if not overlap_candidates:
    app_lines += ["", "## High-overlap cross-App candidates", "",
                  "- None met the conservative threshold (at least 5 exact domain-rule overlaps and high Jaccard/containment)."]
else:
    app_lines += ["", "## High-overlap cross-App candidates", "",
                  "Shared domains may be CDNs, identity providers, analytics, or other common infrastructure. Do not merge these lists solely because of overlap."]
    for item in overlap_candidates[:100]:
        a, b = item["a"], item["b"]
        app_lines += [
            "", f"### {a['display_app']} vs {b['display_app']}",
            f"- Files: {a['path']} and {b['path']}",
            f"- Shared exact domain rules: {item['shared']}; Jaccard: {item['jaccard']:.2f}; smaller-set coverage: {item['containment']:.2f}",
            "- Examples: " + ", ".join(f"{kind},{value}" for kind, value in item["examples"]),
        ]
app_lines += [
    "", "## Safety and scope",
    "- No rule files are deleted, rewritten, or merged by this report generator.",
    "- Aggregate, All, Domain-only, and No-Resolve variants are not collapsed into standard app lists.",
    "- Domain overlap is not proof that two apps are the same; shared infrastructure can produce false positives.",
    "- Personal rules are outside this scan and must remain separate.", "",
]
(ROOT / "APP-OVERLAP-REPORT.md").write_text("\n".join(app_lines), encoding="utf-8")

source_lines = [
    "# Additional-source merge coverage report", "",
    f"Generated: {stamp}", "",
    "Coverage is measured against the final target rule list. Exact matches and matches covered by a parent DOMAIN-SUFFIX are distinguished. This is a static coverage check, not proof of routing correctness.",
    "",
    "| Source contribution | License | Source rules | Exact | Parent suffix | Single-label suffix | Missing | Target |",
    "|---|---:|---:|---:|---:|---:|---:|---|",
]
for row in source_rows:
    if "error" in row:
        source_lines.append(f"| {row['name']} | — | — | — | — | — | — | {row['error']} |")
    else:
        source_lines.append(
            f"| {row['name']} | {row['license']} | {row['source_count']} | {row['exact']} | "
            f"{row['parent_suffix_covered']} | {row['single_label_suffix_covered']} | "
            f"{len(row['missing'])} | {row['target']} |"
        )
for row in source_rows:
    if row.get("missing"):
        source_lines += ["", f"## Missing rules: {row['name']}", ""]
        source_lines += [f"- {rule}" for rule in row["missing"]]
source_lines += [
    "", "## Interpretation",
    "- A source rule covered by a parent suffix is already matched by the target list; it is not appended again.",
    "- A source rule missing from the target is a supplementation candidate, not an automatic insertion. Confirm that it belongs to the same app and routing scenario first.",
    "- Source licenses and provenance remain recorded in SourceMetadata.",
    "- No personal rules are imported or merged.", "",
]
(ROOT / "SOURCE-MERGE-REPORT.md").write_text("\n".join(source_lines), encoding="utf-8")

# Verify every explicitly approved canonical/legacy pair has identical ordered rule payloads.
plan_path = Path("Rule/CONSOLIDATION-PLAN.json")
merge_groups = json.loads(plan_path.read_text(encoding="utf-8")).get("merge_groups", [])

def ordered_rule_lines(path):
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.lstrip().startswith(("#", ";", "//"))
    ]

for group in merge_groups:
    paths = [group["canonical_path"]] + group.get("legacy_paths", [])
    payloads = [ordered_rule_lines(Path(path)) for path in paths]
    if not payloads or any(payload != payloads[0] for payload in payloads[1:]):
        raise SystemExit("Canonical/legacy rule payload mismatch: " + group.get("app", "unknown"))

audit = ROOT / "AUDIT-REPORT.md"
if audit.is_file():
    audit_text = audit.read_text(encoding="utf-8")
    audit_text = re.sub(
        r"- Identical rule-set groups \(review only\): \d+",
        f"- Canonical same-app merge groups: {len(merge_groups)} (legacy paths retained and mirror-verified)",
        audit_text,
    )
    audit_text = audit_text.replace(
        "- Exact duplicate rows are removed only within each individual file; cross-file semantic deduplication is not claimed. Identical rule-set groups are reported for review and are not automatically merged.",
        "- Exact duplicate rows are removed within each file. Explicitly approved same-app groups are unioned and mirrored; similarity-only overlaps remain review candidates and are never merged automatically."
    )
    audit.write_text(audit_text, encoding="utf-8")
    with audit.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n## Further app-level analysis\n"
            f"- Canonical/legacy ordered rule payloads verified for {len(merge_groups)} approved groups.\n"
            "- See CANONICAL-MERGE-REPORT.md for approved same-App unions and legacy URL mirrors.\n"
            "- See APP-OVERLAP-REPORT.md for cross-category App candidates and conservative domain-overlap review.\n"
            "- See SOURCE-MERGE-REPORT.md for cross-author source-rule coverage against final target lists.\n"
        )
print("App overlap report: same-app groups", len(same_app_candidates),
      "cross-app overlap candidates", len(overlap_candidates),
      "source contributions", len(source_rows))
