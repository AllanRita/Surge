#!/usr/bin/env python3
"""Read-only App/folder completeness evidence matrix.

This audit distinguishes structural inventory from author-source coverage.
A folder with no mapped cached author source is NOT marked complete; it is
explicitly reported as NOT_VERIFIABLE_FROM_CACHED_SOURCES.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse, json, re

ROOT = Path("Rule/Upstream")
SOURCE_ROOT = ROOT / "SourceMetadata"
FORMAT_SUFFIXES = (
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

def classify_format(path):
    for suffix, label in FORMAT_SUFFIXES:
        if path.stem.endswith(suffix):
            return label
    return "standard"

def classify_entry(line):
    value = line.strip()
    if not value or value.startswith(("#", ";", "//")):
        return None
    if value.startswith(("||", "@@||")) or (value.startswith("/") and value.endswith("/") and len(value) > 2):
        return "native_filter"
    if "," in value:
        return "surge_rule"
    if re.fullmatch(r"(?i)[a-z0-9_-]+(?:\.[a-z0-9_-]+)+", value.lstrip(".")):
        return "native_domain"
    return "unclassified"

def inventory(root, source_root, source_map):
    mapped = {}
    for source_file, targets in source_map.items():
        for target in targets:
            mapped.setdefault(target, []).append(source_file)

    folders = {}
    for path in sorted(root.rglob("*.list")):
        if path.is_symlink() or not path.is_file():
            raise RuntimeError("Unsafe rule file: " + str(path))
        if source_root.name in path.parts:
            continue
        rel = path.relative_to(root)
        folder = rel.parent
        row = folders.setdefault(folder, {
            "folder": str(folder),
            "rule_files": 0,
            "rule_entries": 0,
            "surge_rule_entries": 0,
            "native_filter_entries": 0,
            "native_domain_entries": 0,
            "unclassified_entries": 0,
            "formats": [],
            "files": [],
            "cached_author_sources": set(),
            "mapped_target_files": 0,
        })
        lines = path.read_text(encoding="utf-8-sig").splitlines()
        classes = [kind for line in lines if (kind := classify_entry(line))]
        row["rule_files"] += 1
        row["rule_entries"] += len(classes)
        row["surge_rule_entries"] += classes.count("surge_rule")
        row["native_filter_entries"] += classes.count("native_filter")
        row["native_domain_entries"] += classes.count("native_domain")
        row["unclassified_entries"] += classes.count("unclassified")
        row["formats"].append(classify_format(path))
        row["files"].append(str(rel))
        rel_posix = rel.as_posix()
        sources = mapped.get(rel_posix, [])
        if sources:
            row["mapped_target_files"] += 1
            row["cached_author_sources"].update(sources)
        output_readme = root / folder / "README.md"
        row["readme_present"] = output_readme.is_file() and not output_readme.is_symlink()

    output = []
    for folder, row in sorted(folders.items(), key=lambda x: str(x[0]).casefold()):
        row["formats"] = sorted(set(row["formats"]))
        row["files"] = sorted(row["files"])
        row["cached_author_sources"] = sorted(row["cached_author_sources"])
        row["author_source_coverage"] = (
            "CACHED_SOURCE_COMPARISON_CONFIGURED"
            if row["cached_author_sources"]
            else "NOT_VERIFIABLE_FROM_CACHED_SOURCES"
        )
        row["author_source_note"] = (
            "Only the listed existing snapshots and explicitly mapped target file(s) were compared; this does not prove completeness against every author."
            if row["cached_author_sources"]
            else "No existing cached author snapshot is mapped to this folder; do not infer completeness."
        )
        output.append(row)

    summary = Counter(row["author_source_coverage"] for row in output)
    return {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "READ_ONLY_APP_COMPLETENESS_EVIDENCE_MATRIX",
        "scope": "Existing Rule/Upstream rule files and the 15 existing cached author snapshots only; no network fetches and no rule modifications.",
        "folder_count": len(output),
        "rule_file_count": sum(x["rule_files"] for x in output),
        "rule_entry_count": sum(x["rule_entries"] for x in output),
        "surge_rule_entry_count": sum(x["surge_rule_entries"] for x in output),
        "native_filter_entry_count": sum(x["native_filter_entries"] for x in output),
        "native_domain_entry_count": sum(x["native_domain_entries"] for x in output),
        "unclassified_entry_count": sum(x["unclassified_entries"] for x in output),
        "folders_with_readme": sum(1 for x in output if x["readme_present"]),
        "folders_with_cached_source_mapping": summary["CACHED_SOURCE_COMPARISON_CONFIGURED"],
        "folders_not_verifiable_from_cached_sources": summary["NOT_VERIFIABLE_FROM_CACHED_SOURCES"],
        "cached_source_snapshot_count": len([p for p in source_root.glob("*.json") if p.is_file() and not p.is_symlink()]),
        "folders": output,
        "limitations": [
            "A mapped cached source comparison covers only that source snapshot and its explicitly configured target file(s), not every author or every App.",
            "A folder without a mapped cached source is not author-completeness verified.",
            "README presence is structural evidence only; it does not establish that the rule list is current or complete.",
            "No files are added, removed, renamed, merged, or rewritten by this audit."
        ]
    }

def render_markdown(report):
    lines = [
        "# App-by-App completeness evidence matrix",
        "",
        f"Generated: {report['generated_utc']}",
        "",
        "Read-only report. No new author sources were fetched and no rule files were modified.",
        "",
        "## Summary",
        "",
        f"- Rule-set folders containing .list files: **{report['folder_count']}**",
        f"- Rule files: **{report['rule_file_count']}**",
        f"- Rule entries (all non-comment entries): **{report['rule_entry_count']}**",
        f"- Surge rule entries: **{report['surge_rule_entry_count']}**",
        f"- Native filter entries: **{report['native_filter_entry_count']}**",
        f"- Native domain entries: **{report['native_domain_entry_count']}**",
        f"- Unclassified entries: **{report['unclassified_entry_count']}**",
        f"- Folders with README: **{report['folders_with_readme']}**",
        f"- Folders with an explicitly mapped cached-author comparison: **{report['folders_with_cached_source_mapping']}**",
        f"- Folders not verifiable from existing cached author snapshots: **{report['folders_not_verifiable_from_cached_sources']}**",
        f"- Existing cached author snapshots: **{report['cached_source_snapshot_count']}**",
        "",
        "## Per-folder evidence",
        "",
        "| Rule-set folder | Files | Entries | Surge | Native filters | Native domains | Unclassified | Formats | README | Cached author sources | Evidence status |",
        "|---|---:|---:|---:|---:|---:|---:|---|---|---|---|",
    ]
    for row in report["folders"]:
        sources = ", ".join(row["cached_author_sources"]) if row["cached_author_sources"] else "None mapped"
        status = "Mapped cache only" if row["cached_author_sources"] else "Not verifiable"
        lines.append(
            f"| {row['folder']} | {row['rule_files']} | {row['rule_entries']} | "
            f"{row['surge_rule_entries']} | {row['native_filter_entries']} | {row['native_domain_entries']} | "
            f"{row['unclassified_entries']} | {', '.join(row['formats'])} | "
            f"{'Yes' if row['readme_present'] else 'No'} | "
            f"{sources} | {status} |"
        )
    lines.extend(["", "## Interpretation", ""])
    lines.extend("- " + item for item in report["limitations"])
    lines.append("")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--source-root", default=str(SOURCE_ROOT))
    ap.add_argument("--output-dir", default="batch-output")
    args = ap.parse_args()
    root = Path(args.root)
    source_root = Path(args.source_root)
    if root.is_symlink() or not root.is_dir() or source_root.is_symlink() or not source_root.is_dir():
        raise SystemExit("Missing or unsafe upstream/source metadata directory")
    from merge_cached_sources import SOURCES
    report = inventory(root, source_root, SOURCES)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "app-completeness-matrix.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "app-completeness-matrix.md").write_text(render_markdown(report) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in (
        "folder_count", "rule_file_count", "rule_entry_count", "folders_with_readme",
        "folders_with_cached_source_mapping", "folders_not_verifiable_from_cached_sources",
        "cached_source_snapshot_count"
    )}, ensure_ascii=False))

if __name__ == "__main__":
    main()
