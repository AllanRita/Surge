#!/usr/bin/env python3
"""Remove rule-set folders that the user explicitly excluded.

This is a narrow tombstone enforcer: it only operates on direct child folders
of Rule/Upstream named in .github/explicit-rule-exclusions.json. It never
touches domains in other rule sets or anything under Rule/Personal.
"""
from pathlib import Path
import json
import shutil

MANIFEST = Path(".github/explicit-rule-exclusions.json")
ROOT = Path("Rule/Upstream")


def load_exclusions():
    if not MANIFEST.is_file() or MANIFEST.is_symlink():
        raise SystemExit("Explicit exclusion manifest is missing or unsafe")
    if ROOT.is_symlink() or not ROOT.is_dir():
        raise SystemExit("Rule/Upstream is missing or unsafe")
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit("Cannot read explicit exclusion manifest: " + str(exc))
    entries = data.get("exclusions")
    if not isinstance(entries, list):
        raise SystemExit("Explicit exclusion manifest exclusions must be a list")
    seen = set()
    names = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise SystemExit("Invalid exclusion entry")
        name = entry.get("folder")
        expected_path = "Rule/Upstream/" + str(name)
        if (not isinstance(name, str) or not name or name in {".", ".."}
                or "/" in name or "\\" in name
                or entry.get("path") != expected_path):
            raise SystemExit("Unsafe or inconsistent exclusion entry: " + repr(entry))
        key = name.casefold()
        if key in seen:
            raise SystemExit("Duplicate exclusion entry: " + name)
        seen.add(key)
        names.append(name)
    return names


def enforce_explicit_exclusions():
    names = load_exclusions()
    removed = []
    for name in names:
        matches = [p for p in ROOT.iterdir() if p.name.casefold() == name.casefold()]
        for target in matches:
            if target.is_symlink() or not target.is_dir():
                raise SystemExit("Excluded path is not a safe directory: " + str(target))
            for child in target.rglob("*"):
                if child.is_symlink():
                    raise SystemExit("Symlink found inside excluded folder; refusing unsafe removal: " + str(child))
            shutil.rmtree(target)
            removed.append(str(target))
    remaining = {
        p.name.casefold()
        for p in ROOT.iterdir()
    }
    still_present = [name for name in names if name.casefold() in remaining]
    if still_present:
        raise SystemExit("Explicitly excluded folders remain: " + ", ".join(still_present))
    if removed:
        print("Removed reintroduced user-excluded folders: " + ", ".join(removed))
    else:
        print("Explicit exclusion check passed; no user-excluded folders were present.")
    print("Protected exclusions enforced: " + str(len(names)))


if __name__ == "__main__":
    enforce_explicit_exclusions()
