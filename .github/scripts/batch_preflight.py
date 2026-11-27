#!/usr/bin/env python3
"""Read-only, deterministic 100-folder Surge rule-set batch preflight.

This tool never edits, deletes, renames, merges, or restores rule files.
It validates one alphabetical batch and emits JSON/Markdown reports for review.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse, hashlib, ipaddress, json, re, sys

ROOT = Path("Rule/Upstream")
PERSONAL = Path("Rule/Personal")
MANIFEST = Path(".github/explicit-rule-exclusions.json")
ALLOWED = {
    "DOMAIN","DOMAIN-SUFFIX","DOMAIN-KEYWORD","DOMAIN-WILDCARD","DOMAIN-REGEX",
    "IP-CIDR","IP-CIDR6","IP-ASN","GEOIP","USER-AGENT","URL-REGEX",
    "PROCESS-NAME","DEST-PORT","SRC-PORT","SRC-IP","IN-PORT","PROTOCOL",
    "AND","OR","NOT","RULE-SET","DOMAIN-SET","SUBNET","DEVICE-NAME",
    "HOST","HOST-SUFFIX","HOST-KEYWORD"
}
DOMAIN_TYPES = {"DOMAIN","DOMAIN-SUFFIX","HOST","HOST-SUFFIX"}

def digest_tree(root):
    h = hashlib.sha256()
    if not root.exists():
        return "MISSING"
    for p in sorted(root.rglob("*")):
        if p.is_symlink():
            h.update(("SYMLINK:"+str(p)).encode())
        elif p.is_file():
            h.update(str(p.relative_to(root)).encode())
            h.update(p.read_bytes())
    return h.hexdigest()

def load_tombstones():
    if not MANIFEST.is_file() or MANIFEST.is_symlink():
        raise RuntimeError("Explicit exclusion manifest missing or unsafe")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = data.get("exclusions")
    if not isinstance(entries, list):
        raise RuntimeError("Manifest exclusions must be a list (empty is valid)")
    names = set()
    for e in entries:
        if not isinstance(e, dict):
            raise RuntimeError("Malformed tombstone entry")
        name = e.get("folder")
        if (not isinstance(name, str) or not name or name in {".",".."}
                or "/" in name or "\\\\" in name
                or e.get("path") != "Rule/Upstream/" + name):
            raise RuntimeError("Unsafe tombstone entry: " + repr(e))
        if name.casefold() in names:
            raise RuntimeError("Duplicate tombstone: " + name)
        names.add(name.casefold())
    return names

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--batch-size", type=int, default=100)
    ap.add_argument("--output-dir", default="batch-output")
    a = ap.parse_args()
    if a.batch < 1 or a.batch_size != 100:
        raise SystemExit("Batch number must be >=1 and batch size must be exactly 100")
    if ROOT.is_symlink() or not ROOT.is_dir():
        raise SystemExit("Rule/Upstream missing or unsafe")

    personal_before = digest_tree(PERSONAL)
    tombstones = load_tombstones()
    top = sorted(
        (p for p in ROOT.iterdir() if p.is_dir() and not p.is_symlink()
         and p.name != "SourceMetadata"),
        key=lambda p: (p.name.casefold(), p.name)
    )
    present = {p.name.casefold() for p in top}
    conflict = sorted(x for x in tombstones if x in present)
    if conflict:
        raise SystemExit("Tombstoned folders reintroduced: " + ", ".join(conflict))

    start = (a.batch - 1) * 100
    selected = top[start:start + 100]
    if not selected:
        raise SystemExit(f"Batch {a.batch} has no folders; total eligible folders: {len(top)}")

    totals = Counter()
    findings = []
    folder_rows = []
    for folder in selected:
        folder_files = sorted(folder.rglob("*.list"))
        if folder.is_symlink():
            findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(folder),"issue":"folder symlink"})
            continue
        for f in folder.rglob("*"):
            if f.is_symlink():
                findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(f),"issue":"symlink inside rule folder"})
        if not folder_files:
            findings.append({"severity":"REVIEW","folder":folder.name,"path":str(folder),"issue":"no .list files"})
        fr = Counter()
        seen_files = set()
        for path in folder_files:
            totals["files"] += 1
            fr["files"] += 1
            if path.is_symlink():
                findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(path),"issue":"rule file symlink"})
                continue
            try:
                raw = path.read_text(encoding="utf-8-sig")
            except UnicodeError as e:
                findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(path),"issue":"not valid UTF-8: "+str(e)})
                continue
            except OSError as e:
                findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(path),"issue":"cannot read: "+str(e)})
                continue
            rows = [x.strip() for x in raw.splitlines() if x.strip() and not x.strip().startswith(("#",";","//"))]
            totals["rules"] += len(rows)
            fr["rules"] += len(rows)
            dup = Counter(rows)
            dups = sum(n-1 for n in dup.values() if n > 1)
            if dups:
                fr["duplicate_lines"] += dups
                totals["duplicate_lines"] += dups
                findings.append({"severity":"REVIEW","folder":folder.name,"path":str(path),"issue":f"{dups} duplicate rule lines"})
            for line_no, raw_line in enumerate(raw.splitlines(), 1):
                if any(ord(c) < 32 and c not in "\t" for c in raw_line):
                    fr["control_chars"] += 1
                    totals["control_chars"] += 1
                    findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(path),"line":line_no,"issue":"hidden control character"})
                line = raw_line.strip()
                if not line or line.startswith(("#",";","//")):
                    continue
                if line.startswith(("||","@@||")) or (line.startswith("/") and line.endswith("/") and len(line)>2):
                    fr["native_filters"] += 1
                    totals["native_filters"] += 1
                    continue
                if "," not in line:
                    if re.fullmatch(r"(?i)[a-z0-9_-]+(?:\.[a-z0-9_-]+)+", line.lstrip(".")):
                        fr["native_domains"] += 1
                        totals["native_domains"] += 1
                    else:
                        findings.append({"severity":"REVIEW","folder":folder.name,"path":str(path),"line":line_no,"issue":"unclassified non-comment line"})
                    continue
                parts = line.split(",")
                kind = parts[0].strip().upper()
                value = parts[1].strip() if len(parts)>1 else ""
                if kind not in ALLOWED or not value:
                    fr["unsupported"] += 1
                    totals["unsupported"] += 1
                    findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(path),"line":line_no,"issue":f"unsupported rule type or missing operand: {kind}"})
                    continue
                if kind in {"IP-CIDR","IP-CIDR6"}:
                    try:
                        net = ipaddress.ip_network(value, strict=False)
                        if (kind=="IP-CIDR" and net.version!=4) or (kind=="IP-CIDR6" and net.version!=6):
                            raise ValueError("address family does not match rule type")
                        if net.prefixlen == 0:
                            findings.append({"severity":"REVIEW","folder":folder.name,"path":str(path),"line":line_no,"issue":"catch-all network requires manual review"})
                    except ValueError as e:
                        fr["invalid_network"] += 1
                        totals["invalid_network"] += 1
                        findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(path),"line":line_no,"issue":"invalid IP network: "+str(e)})
                if kind in DOMAIN_TYPES:
                    domain = value.lower().rstrip(".")
                    if not re.fullmatch(r"[a-z0-9_-]+(?:\.[a-z0-9_-]+)*", domain):
                        fr["invalid_domain"] += 1
                        totals["invalid_domain"] += 1
                        findings.append({"severity":"BLOCKER","folder":folder.name,"path":str(path),"line":line_no,"issue":"invalid domain operand"})
                    elif kind in {"DOMAIN-SUFFIX","HOST-SUFFIX"} and "." not in domain:
                        findings.append({"severity":"REVIEW","folder":folder.name,"path":str(path),"line":line_no,"issue":"single-label suffix is broad or special-use; review only"})
        folder_rows.append({"folder":folder.name,**dict(fr)})

    personal_after = digest_tree(PERSONAL)
    if personal_before != personal_after:
        findings.append({"severity":"BLOCKER","folder":"Rule/Personal","issue":"personal rules changed during read-only batch"})
    blockers = sum(1 for x in findings if x["severity"]=="BLOCKER")
    reviews = sum(1 for x in findings if x["severity"]=="REVIEW")
    report = {
        "schema_version":1,
        "generated_utc":datetime.now(timezone.utc).isoformat(),
        "mode":"READ_ONLY_PREFLIGHT",
        "batch":a.batch,
        "batch_size":100,
        "total_eligible_top_level_folders":len(top),
        "range_start_1based":start+1,
        "range_end_1based":start+len(selected),
        "selected_folders":[p.name for p in selected],
        "selected_folder_count":len(selected),
        "summary":{"files":totals["files"],"rules":totals["rules"],"blockers":blockers,"review_items":reviews,"duplicate_lines":totals["duplicate_lines"],"unsupported":totals["unsupported"],"invalid_network":totals["invalid_network"],"invalid_domain":totals["invalid_domain"],"native_filters":totals["native_filters"],"native_domains":totals["native_domains"]},
        "tombstone_count":len(tombstones),
        "personal_tree_unchanged":personal_before==personal_after,
        "folders":folder_rows,
        "findings":findings
    }
    out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True)
    stem=f"batch-{a.batch:03d}"
    (out/(stem+".json")).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    md=["# Surge rule-set batch preflight", "",f"- Batch: {a.batch}",f"- Mode: {report['mode']}",f"- Eligible top-level folders: {len(top)}",f"- Selected folders: {len(selected)}",f"- Rule files: {totals['files']}",f"- Rule entries: {totals['rules']}",f"- Blockers: {blockers}",f"- Review items: {reviews}",f"- Tombstones: {len(tombstones)}",f"- Rule/Personal unchanged: {personal_before==personal_after}","","## Selected folders",""]
    md += [f"- {x['folder']}: {x.get('files',0)} files, {x.get('rules',0)} rules" for x in folder_rows]
    md += ["","## Findings",""]
    md += [f"- **{x['severity']}** {x.get('path',x.get('folder',''))}{(':'+str(x['line'])) if x.get('line') else ''}: {x['issue']}" for x in findings] or ["- None"]
    md += ["","## Safety","- No rule file was modified, deleted, renamed, merged, or restored.","- This is a preflight only. No batch is approved for remediation automatically.",""]
    (out/(stem+".md")).write_text("\n".join(md),encoding="utf-8")
    summary = f"Surge batch {a.batch}: {len(selected)} folders, {totals['files']} files, {totals['rules']} rules, {blockers} blockers, {reviews} review items."
    print(json.dumps({"status":"PASS" if blockers==0 else "BLOCKED","summary":summary,"report_json":str(out/(stem+".json")),"report_markdown":str(out/(stem+".md"))},ensure_ascii=False))
    if blockers:
        raise SystemExit(2)

if __name__=="__main__":
    main()
