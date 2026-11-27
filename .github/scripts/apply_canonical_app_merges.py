#!/usr/bin/env python3
"""Apply only explicitly approved same-app canonical unions; never delete legacy paths."""
from pathlib import Path
from collections import Counter
import json
import re
import sys

PLAN = Path("Rule/CONSOLIDATION-PLAN.json")
ROOT = Path("Rule/Upstream")
REPORT = ROOT / "CANONICAL-MERGE-REPORT.md"

if not PLAN.is_file() or PLAN.is_symlink():
    raise SystemExit("Canonical merge plan is missing or unsafe")
if ROOT.is_symlink() or not ROOT.is_dir():
    raise SystemExit("Upstream rule root is missing or unsafe")

plan = json.loads(PLAN.read_text(encoding="utf-8"))
groups = plan.get("merge_groups", [])
if not isinstance(groups, list):
    raise SystemExit("Invalid merge_groups in canonical plan")

def safe_path(value):
    p = Path(value)
    if not value.startswith("Rule/Upstream/") or ".." in p.parts:
        raise SystemExit("Canonical merge path outside Rule/Upstream: " + value)
    if p.is_symlink():
        raise SystemExit("Symlink not allowed in canonical merge: " + value)
    parent = p.parent
    while parent != Path("."):
        if parent.is_symlink():
            raise SystemExit("Symlink parent not allowed in canonical merge: " + str(parent))
        parent = parent.parent
    if not p.is_file():
        raise SystemExit("Canonical merge file missing: " + value)
    return p

def parse_file(path):
    header = []
    rules = []
    trailing_comments = []
    started = False
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw.rstrip()
        if not line.strip():
            if not started:
                header.append("")
            else:
                trailing_comments.append("")
            continue
        if line.lstrip().startswith(("#", ";", "//")):
            if not started:
                header.append(line)
            else:
                trailing_comments.append(line)
            continue
        started = True
        rules.append(line.strip())
    if not rules:
        raise SystemExit("Empty canonical merge input: " + str(path))
    return header, rules, trailing_comments

def render(header, rules, trailing_comments, canonical, aliases):
    # Refresh numeric rule counts while retaining source/license/name metadata.
    clean = []
    for line in header:
        if re.match(r"^# [A-Z0-9_-]+: \d+$", line):
            continue
        if line.startswith("# CANONICAL-RULESET:") or line.startswith("# MERGED-ALIASES:"):
            continue
        clean.append(line)
    clean = [line for line in clean if line.strip()]
    clean.append("# CANONICAL-RULESET: " + canonical)
    if aliases:
        clean.append("# MERGED-ALIASES: " + ", ".join(aliases))
    counts = Counter()
    for rule in rules:
        counts[rule.split(",", 1)[0].strip().upper()] += 1
    for kind in sorted(counts):
        clean.append(f"# {kind}: {counts[kind]}")
    clean.append(f"# TOTAL: {len(rules)}")
    body = clean + [""] + rules
    if trailing_comments:
        body += [""] + [x for x in trailing_comments if x.strip()]
    return "\n".join(body) + "\n"

report_lines = [
    "# Canonical same-app merge report", "",
    "Generated during the validated upstream sync. Rule lines are unioned exactly; no legacy path is deleted.", "",
    "| App | Scenario | Source rule occurrences | Unique merged rules | Exact duplicates collapsed | Canonical path | Legacy mirrors |",
    "|---|---|---:|---:|---:|---|---|",
]
changed_files = 0
for group in groups:
    canonical_value = group.get("canonical_path", "")
    legacy_values = group.get("legacy_paths", [])
    if not canonical_value or not isinstance(legacy_values, list):
        raise SystemExit("Malformed canonical merge group")
    if canonical_value in legacy_values or len(set(legacy_values)) != len(legacy_values):
        raise SystemExit("Duplicate or self-referential path in canonical merge group")
    paths = [safe_path(canonical_value)] + [safe_path(x) for x in legacy_values]
    parsed = [parse_file(path) for path in paths]
    headers = [x[0] for x in parsed]
    source_rules = [x[1] for x in parsed]
    trailing = []
    for _, _, comments in parsed:
        trailing.extend(comments)
    # Keep canonical ordering, then append new exact lines from legacy sources.
    merged = list(dict.fromkeys(rule for rows in source_rules for rule in rows))
    occurrences = sum(len(rows) for rows in source_rules)
    duplicates = occurrences - len(merged)
    aliases = legacy_values
    for path, header in zip(paths, headers):
        new_content = render(header, merged, trailing, canonical_value, aliases)
        old_content = path.read_text(encoding="utf-8-sig")
        if old_content != new_content:
            path.write_text(new_content, encoding="utf-8")
            changed_files += 1
    report_lines.append(
        f"| {group.get('app','unknown')} | {group.get('scenario','standard')} | "
        f"{occurrences} | {len(merged)} | {duplicates} | {canonical_value} | "
        f"{'; '.join(legacy_values) if legacy_values else '—'} |"
    )
    report_lines += [
        "",
        f"## {group.get('app','unknown')} ({group.get('scenario','standard')})",
        f"- Canonical path: {canonical_value}",
        f"- Legacy paths mirrored: {', '.join(legacy_values) if legacy_values else 'none'}",
        f"- Rule lines before merge: {occurrences}; after exact deduplication: {len(merged)}",
        f"- Exact duplicate lines collapsed across inputs: {duplicates}",
        f"- Reason: {group.get('reason','approved same-app merge')}",
    ]

report_lines += [
    "",
    "## Safety",
    "- All inputs are required to exist; missing or unsafe files block publication.",
    "- Only paths explicitly listed in Rule/CONSOLIDATION-PLAN.json are merged.",
    "- Standard, Resolve, No-Resolve, No-IPv6, region, block, and routing scenarios remain distinct unless a group is explicitly approved.",
    "- Each legacy file keeps its own NAME/header identity and receives the same merged rule payload as the canonical file.",
    "- Personal rules are never read or modified.",
    "- No legacy file is deleted.",
    "",
]
REPORT.write_text("\n".join(report_lines), encoding="utf-8")
print("Canonical app merge groups:", len(groups), "files changed:", changed_files)
