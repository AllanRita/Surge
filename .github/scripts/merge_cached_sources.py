#!/usr/bin/env python3
"""Idempotent, format-aware union of the 15 already-cached author snapshots."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse, hashlib, ipaddress, json, re

ROOT = Path("Rule/Upstream")
PERSONAL = Path("Rule/Personal")
MANIFEST = Path(".github/explicit-rule-exclusions.json")
SOURCES = {
    "Aoang-Apple.json": ["Apple/Apple.list", "Apple/Apple_Resolve.list", "Apple/Apple_All.list", "Apple/Apple_All_No_Resolve.list"],
    "Aoang-DNS.json": ["Block/DNS/DNS.list"],
    "Aoang-OneDrive.json": ["OneDrive/OneDrive.list"],
    "Aoang-Other.json": ["Block/Other/Other.list"],
    "Aoang-Parallels.json": ["Block/Parallels/Parallels.list"],
    "Aoang-Process.json": ["Process/Process/Process.list"],
    "Aoang-Teams.json": ["Teams/Teams.list"],
    "Aoang-Unavailable.json": ["Process/Unavailable/Unavailable.list"],
    "Aoang-YouTube.json": ["Block/YouTube/YouTube.list"],
    "Apple.json": ["Apple/Apple.list", "Apple/Apple_Resolve.list", "Apple/Apple_All.list", "Apple/Apple_All_No_Resolve.list"],
    "BiliBiliIntl.json": ["BiliBili/BiliBili.list", "BiliBili/BiliBili_Resolve.list"],
    "GitLab.json": ["GitLab/GitLab.list"],
    "Microsoft.json": ["Microsoft/Microsoft.list"],
    "NetEaseMusic.json": ["NetEaseMusic/NetEaseMusic.list", "NetEaseMusic/NetEaseMusic_Resolve.list"],
    "Telegram.json": ["Telegram/Telegram.list", "Telegram/Telegram_Resolve.list"],
}
DOMAIN_TYPES = {"DOMAIN", "DOMAIN-SUFFIX", "HOST", "HOST-SUFFIX"}
IP_TYPES = {"IP-CIDR", "IP-CIDR6"}

def digest(root):
    h = hashlib.sha256()
    if root.exists():
        for p in sorted(root.rglob("*")):
            if p.is_symlink():
                h.update(("SYMLINK:" + str(p)).encode())
            elif p.is_file():
                h.update(str(p.relative_to(root)).encode())
                h.update(p.read_bytes())
    return h.hexdigest()

def write_backup_once(backup_path, source_path):
    backup_path = Path(backup_path)
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    if not backup_path.exists():
        backup_path.write_bytes(Path(source_path).read_bytes())

def load_tombstones():
    if MANIFEST.is_symlink() or not MANIFEST.is_file():
        raise RuntimeError("Missing or unsafe exact deletion manifest")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = data.get("exclusions")
    if not isinstance(entries, list):
        raise RuntimeError("Manifest exclusions must be a list")
    out = set()
    for item in entries:
        name = item.get("folder", "")
        if not name or name in {".", ".."} or "/" in name or "\\" in name or item.get("path") != "Rule/Upstream/" + name:
            raise RuntimeError("Unsafe tombstone entry")
        out.add(name.casefold())
    return out

def parse_rule(line):
    s = line.strip()
    if not s or s.startswith(("#", ";", "//")) or "," not in s:
        return None
    parts = [x.strip() for x in s.split(",")]
    kind = parts[0].upper()
    if len(parts) < 2 or not parts[1]:
        return None
    return kind, parts[1], parts[2:]

def normalized(line):
    return re.sub(r"\s+", "", line.strip()).casefold()

def is_covered(source_rule, existing_rules):
    sk, sv, so = source_rule
    sv = sv.casefold().rstrip(".")
    for ek, ev, eo in existing_rules:
        ev = ev.casefold().rstrip(".")
        if sk in DOMAIN_TYPES and ek in DOMAIN_TYPES:
            if sk in {"DOMAIN", "HOST"}:
                if ek in {"DOMAIN", "HOST"} and sv == ev:
                    return True
                if ek in {"DOMAIN-SUFFIX", "HOST-SUFFIX"} and (sv == ev or sv.endswith("." + ev)):
                    return True
            elif sk in {"DOMAIN-SUFFIX", "HOST-SUFFIX"}:
                if ek in {"DOMAIN-SUFFIX", "HOST-SUFFIX"} and (sv == ev or sv.endswith("." + ev)):
                    return True
        elif sk in IP_TYPES and ek == sk:
            # no-resolve changes routing semantics; only treat a containing
            # network as coverage when both rules use the same resolution mode.
            source_no_resolve = any(x.casefold() == "no-resolve" for x in so)
            existing_no_resolve = any(x.casefold() == "no-resolve" for x in eo)
            if source_no_resolve != existing_no_resolve:
                continue
            try:
                src_net = ipaddress.ip_network(sv, strict=False)
                dst_net = ipaddress.ip_network(ev, strict=False)
                if src_net.version == dst_net.version and src_net.subnet_of(dst_net):
                    return True
            except ValueError:
                pass
        elif sk == ek and normalized(",".join([sk, sv] + so)) == normalized(",".join([ek, ev] + eo)):
            return True
    return False

def adapt_for_target(rule, target, existing_text):
    parsed = parse_rule(rule)
    if not parsed:
        return rule.strip()
    kind, value, options = parsed
    opts = list(options)
    resolve_variant = "_Resolve" in Path(target).stem or "_No_Resolve" in Path(target).stem
    if kind in IP_TYPES:
        opts = [x for x in opts if x.casefold() != "no-resolve"]
        if not resolve_variant:
            has_no_resolve = any(
                (p := parse_rule(line)) and p[0] == kind and any(o.casefold() == "no-resolve" for o in p[2])
                for line in existing_text.splitlines()
            )
            if has_no_resolve:
                opts.append("no-resolve")
    return ",".join([kind, value] + opts)

def valid_for_auto_add(rule):
    p = parse_rule(rule)
    if not p:
        return False, "unparsed or non-rule source line"
    kind, value, _ = p
    if kind in DOMAIN_TYPES:
        if not re.fullmatch(r"[a-z0-9_-]+(?:\.[a-z0-9_-]+)*", value.casefold().rstrip(".")):
            return False, "invalid domain operand"
        if kind in {"DOMAIN-SUFFIX", "HOST-SUFFIX"} and "." not in value:
            return False, "single-label suffix requires review"
    if kind in IP_TYPES:
        try:
            net = ipaddress.ip_network(value, strict=False)
            if (kind == "IP-CIDR" and net.version != 4) or (kind == "IP-CIDR6" and net.version != 6):
                return False, "IP address family mismatch"
        except ValueError:
            return False, "invalid IP network"
    return True, ""

def update_header_counts(text):
    lines = text.splitlines()
    rule_lines = [line for line in lines if parse_rule(line)]
    counts = Counter(parse_rule(line)[0] for line in rule_lines)
    total = len(rule_lines)
    out = []
    for line in lines:
        m = re.match(r"^#\s*([A-Z0-9-]+):\s*\d+\s*$", line)
        if m and m.group(1) in counts:
            out.append("# " + m.group(1) + ": " + str(counts[m.group(1)]))
        elif re.match(r"^#\s*TOTAL:\s*\d+\s*$", line):
            out.append("# TOTAL: " + str(total))
        else:
            out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, required=True)
    ap.add_argument("--batch-size", type=int, default=100)
    ap.add_argument("--output-dir", default="batch-output")
    ap.add_argument("--backup-dir", default="batch-output/backups")
    a = ap.parse_args()
    if a.batch < 1 or a.batch_size != 100:
        raise SystemExit("Batch size must be exactly 100")
    if ROOT.is_symlink() or not ROOT.is_dir():
        raise SystemExit("Unsafe or missing Rule/Upstream")
    tombstones = load_tombstones()
    folders = sorted((p for p in ROOT.iterdir() if p.is_dir() and not p.is_symlink() and p.name != "SourceMetadata"), key=lambda p: (p.name.casefold(), p.name))
    if any(p.name.casefold() in tombstones for p in folders):
        raise SystemExit("Tombstoned folder reintroduced; refusing cached-source merge")
    start = (a.batch - 1) * 100
    selected = folders[start:start + 100]
    if not selected:
        raise SystemExit("No folders in requested batch")
    selected_names = {p.name for p in selected}
    personal_before = digest(PERSONAL)
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "CACHED_SOURCE_FORMAT_AWARE_UNION",
        "batch": a.batch,
        "batch_size": 100,
        "selected_folder_count": len(selected),
        "selected_folders": [p.name for p in selected],
        "cached_sources_expected": 15,
        "cached_sources_processed": 0,
        "source_results": [],
        "summary": {"source_rules": 0, "exact_present": 0, "semantically_covered": 0, "added": 0, "review_only": 0, "files_changed": 0},
        "changes": [],
        "review_findings": [],
    }
    backup_root = Path(a.backup_dir) / ("batch-" + str(a.batch).zfill(3))
    for source_file, targets in SOURCES.items():
        source_path = ROOT / "SourceMetadata" / source_file
        if not source_path.is_file() or source_path.is_symlink():
            raise RuntimeError("Cached source snapshot missing or unsafe: " + str(source_path))
        source_data = json.loads(source_path.read_text(encoding="utf-8"))
        source_rules = source_data.get("rules")
        if not isinstance(source_rules, list):
            raise RuntimeError("Cached source rules must be a list: " + source_file)
        source_targets = [t for t in targets if t.split("/")[0] in selected_names]
        if not source_targets:
            continue
        report["cached_sources_processed"] += 1
        for target in source_targets:
            target_path = ROOT / target
            if target_path.is_symlink() or not target_path.is_file():
                raise RuntimeError("Cached source target missing or unsafe: " + str(target_path))
            original = target_path.read_text(encoding="utf-8-sig")
            parsed_existing = [p for line in original.splitlines() if (p := parse_rule(line))]
            exact_set = {normalized(line) for line in original.splitlines() if parse_rule(line)}
            additions = []
            exact = 0
            covered = 0
            review = []
            for source_rule in source_rules:
                report["summary"]["source_rules"] += 1
                ok, reason = valid_for_auto_add(source_rule)
                if not ok:
                    review.append({"rule": source_rule, "reason": reason})
                    report["summary"]["review_only"] += 1
                    continue
                candidate = adapt_for_target(source_rule, target, original)
                n = normalized(candidate)
                if n in exact_set:
                    exact += 1
                    report["summary"]["exact_present"] += 1
                    continue
                parsed_candidate = parse_rule(candidate)
                if is_covered(parsed_candidate, parsed_existing):
                    covered += 1
                    report["summary"]["semantically_covered"] += 1
                    continue
                additions.append(candidate)
                exact_set.add(n)
                parsed_existing.append(parsed_candidate)
            if additions:
                backup_path = backup_root / target
                write_backup_once(backup_path, target_path)
                marker = "# CACHED SOURCE SUPPLEMENT: " + source_file
                if marker not in original:
                    block = [
                        "",
                        marker,
                        "# Source: " + str(source_data.get("source", "")),
                        "# Snapshot commit: " + str(source_data.get("commit", "")),
                        "# License: " + str(source_data.get("license", "unspecified")),
                    ]
                else:
                    block = []
                block.extend(additions)
                updated = original.rstrip("\n") + "\n" + "\n".join(block) + "\n"
                updated = update_header_counts(updated)
                target_path.write_text(updated, encoding="utf-8")
                report["summary"]["added"] += len(additions)
                report["summary"]["files_changed"] += 1
                for rule in additions:
                    report["changes"].append({"action": "ADD_CACHED_SOURCE_RULE", "source_file": source_file, "source": source_data.get("source"), "source_commit": source_data.get("commit"), "target": target, "rule": rule})
            report["source_results"].append({
                "source_file": source_file,
                "source": source_data.get("source"),
                "source_commit": source_data.get("commit"),
                "source_path": source_data.get("path"),
                "license": source_data.get("license"),
                "source_rule_count": len(source_rules),
                "target": target,
                "exact_present": exact,
                "semantically_covered": covered,
                "added": len(additions),
                "review_only": review,
            })
            report["review_findings"].extend({"source_file": source_file, "target": target, **item} for item in review)
    report["personal_unchanged"] = digest(PERSONAL) == personal_before
    if not report["personal_unchanged"]:
        raise RuntimeError("Rule/Personal changed during cached-source merge")
    out = Path(a.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / ("batch-" + str(a.batch).zfill(3) + "-cached-sources.json")).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"batch": a.batch, "sources": report["cached_sources_processed"], "summary": report["summary"], "personal_unchanged": report["personal_unchanged"]}, ensure_ascii=False))

if __name__ == "__main__":
    main()
