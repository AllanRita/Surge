#!/usr/bin/env python3
"""Fail-closed verification of each maintenance batch and its final reports."""
from pathlib import Path
import argparse
import json
import math
import subprocess

PREFIX = "Rule/Upstream/"

def read_json(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise RuntimeError("Required report missing or unsafe: " + str(path))
    return json.loads(path.read_text(encoding="utf-8"))

def git_bytes(args):
    result = subprocess.run(["git", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    return result.stdout

def parse_name_status(raw):
    records = []
    for line in raw.decode("utf-8").splitlines():
        if not line:
            continue
        parts = line.split("\\t")
        if len(parts) < 2:
            raise RuntimeError("Unrecognized git diff --name-status row: " + line)
        records.append((parts[0], parts[-1]))
    return records

def validate_change_records(records, selected_folders):
    selected = set(selected_folders)
    for status, path in records:
        if status != "M":
            raise ValueError("Only modifications to existing .list files are allowed; found " + status + " " + path)
        if not path.startswith(PREFIX):
            raise ValueError("Changed path is outside Rule/Upstream: " + path)
        relative = path[len(PREFIX):]
        parts = Path(relative).parts
        if not parts or parts[0] == "SourceMetadata" or parts[0] not in selected:
            raise ValueError("Change is outside the current 100-folder batch: " + path)
        if not relative.endswith(".list"):
            raise ValueError("Automatic maintenance may only modify existing .list files: " + path)
    return True

def verify_batch(batch, output_dir, backup_dir):
    out = Path(output_dir)
    backup_root = Path(backup_dir)
    stem = "batch-" + str(batch).zfill(3)
    preflight = read_json(out / (stem + ".json"))
    maintenance = read_json(out / (stem + "-maintenance.json"))
    cached = read_json(out / (stem + "-cached-sources.json"))
    for report in (preflight, maintenance, cached):
        if report.get("batch") != batch or report.get("batch_size") != 100:
            raise RuntimeError("Batch identity mismatch in " + stem)
    selected = cached.get("selected_folders", [])
    if not selected or selected != preflight.get("selected_folders") or selected != maintenance.get("selected_folders"):
        raise RuntimeError("Selected folder lists disagree in " + stem)
    total = preflight.get("total_eligible_top_level_folders")
    expected_count = min(100, total - (batch - 1) * 100)
    if len(selected) != expected_count or preflight.get("selected_folder_count") != expected_count:
        raise RuntimeError("Unexpected selected-folder count in " + stem)
    if preflight.get("summary", {}).get("blockers") != 0:
        raise RuntimeError("Preflight blockers present in " + stem)
    if not preflight.get("personal_tree_unchanged") or not maintenance.get("personal_unchanged") or not cached.get("personal_unchanged"):
        raise RuntimeError("Rule/Personal protection check failed in " + stem)
    if cached.get("cached_sources_expected") != 15:
        raise RuntimeError("Cached-source inventory expectation changed in " + stem)

    diff_records = parse_name_status(git_bytes(["diff", "--name-status", "HEAD", "--", "Rule/Upstream"]))
    validate_change_records(diff_records, selected)
    for status, path in diff_records:
        relative = path[len(PREFIX):]
        backup = backup_root / stem / relative
        if backup.is_symlink() or not backup.is_file():
            raise RuntimeError("Missing pre-change backup for " + path)
        original = git_bytes(["show", "HEAD:" + path])
        if backup.read_bytes() != original:
            raise RuntimeError("Pre-change backup does not match HEAD for " + path)

    personal_diff = git_bytes(["diff", "--name-status", "HEAD", "--", "Rule/Personal"]).strip()
    personal_untracked = git_bytes(["ls-files", "--others", "--exclude-standard", "Rule/Personal"]).strip()
    if personal_diff or personal_untracked:
        raise RuntimeError("Rule/Personal has tracked or untracked changes")
    upstream_untracked = git_bytes(["ls-files", "--others", "--exclude-standard", "Rule/Upstream"]).strip()
    if upstream_untracked:
        raise RuntimeError("Unexpected untracked files under Rule/Upstream")
    return {"batch": batch, "folders": len(selected), "changed_files": len(diff_records), "cached_sources_processed": cached.get("cached_sources_processed", 0)}

def verify_final(total, output_dir):
    out = Path(output_dir)
    if total < 1:
        raise RuntimeError("Total folder count must be positive")
    batches = math.ceil(total / 100)
    aggregate = {"folders": 0, "cached_sources_processed": 0, "source_rules": 0, "added": 0, "format_pairs": 0}
    for batch in range(1, batches + 1):
        stem = "batch-" + str(batch).zfill(3)
        preflight = read_json(out / (stem + ".json"))
        maintenance = read_json(out / (stem + "-maintenance.json"))
        cached = read_json(out / (stem + "-cached-sources.json"))
        expected = min(100, total - (batch - 1) * 100)
        if preflight.get("batch") != batch or preflight.get("total_eligible_top_level_folders") != total:
            raise RuntimeError("Missing or mismatched preflight batch " + str(batch))
        if preflight.get("selected_folder_count") != expected or len(preflight.get("selected_folders", [])) != expected:
            raise RuntimeError("Incomplete preflight folder coverage in batch " + str(batch))
        if maintenance.get("batch") != batch or cached.get("batch") != batch:
            raise RuntimeError("Missing maintenance or cached-source report in batch " + str(batch))
        if not preflight.get("personal_tree_unchanged") or not maintenance.get("personal_unchanged") or not cached.get("personal_unchanged"):
            raise RuntimeError("Rule/Personal protection failed in batch " + str(batch))
        if preflight.get("summary", {}).get("blockers") != 0:
            raise RuntimeError("Preflight blockers present in batch " + str(batch))
        aggregate["folders"] += expected
        aggregate["cached_sources_processed"] += cached.get("cached_sources_processed", 0)
        summary = cached.get("summary", {})
        aggregate["source_rules"] += summary.get("source_rules", 0)
        aggregate["added"] += summary.get("added", 0)
    if aggregate["folders"] != total:
        raise RuntimeError("Final report folder count does not match eligible folder total")
    if aggregate["cached_sources_processed"] != 15:
        raise RuntimeError("Expected all 15 cached author snapshots to be processed; found " + str(aggregate["cached_sources_processed"]))
    format_audit = read_json(out / "format-parity-audit.json")
    format_summary = format_audit.get("summary", {})
    if format_summary.get("pairs_needing_review", 0) != 0:
        raise RuntimeError("Paired-format audit has unresolved differences")
    matrix = read_json(out / "app-completeness-matrix.json")
    if matrix.get("cached_source_snapshot_count") != 15:
        raise RuntimeError("App completeness matrix did not inspect all 15 cached snapshots")
    if not (out / "app-completeness-matrix.md").is_file() or not (out / "format-parity-audit.md").is_file():
        raise RuntimeError("Required Markdown audit report missing")
    if not (out / "BATCH-STATUS.txt").is_file():
        raise RuntimeError("Final batch status file missing")
    aggregate["format_pairs"] = format_summary.get("pairs_compared", 0)
    aggregate["app_folders"] = matrix.get("folder_count", 0)
    aggregate["cached_source_mapped_folders"] = matrix.get("folders_with_cached_source_mapping", 0)
    aggregate["not_verifiable_folders"] = matrix.get("folders_not_verifiable_from_cached_sources", 0)
    return aggregate

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int)
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--total", type=int)
    ap.add_argument("--output-dir", default="batch-output")
    ap.add_argument("--backup-dir", default="batch-output/backups")
    args = ap.parse_args()
    if args.final:
        if args.total is None:
            raise SystemExit("--final requires --total")
        result = verify_final(args.total, args.output_dir)
    else:
        if args.batch is None or args.batch < 1:
            raise SystemExit("--batch must be a positive integer")
        result = verify_batch(args.batch, args.output_dir, args.backup_dir)
    print(json.dumps({"status": "PASS", **result}, ensure_ascii=False))

if __name__ == "__main__":
    main()
