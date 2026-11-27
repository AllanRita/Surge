#!/usr/bin/env python3
"""Remove only the verified non-IANA public root suffix xihuan from public rule files."""
from pathlib import Path
from collections import Counter
import argparse, json, re

ROOT=Path("Rule/Upstream")
TARGET="DOMAIN-SUFFIX,xihuan"

def read_lines(path):
    return path.read_text(encoding="utf-8-sig").splitlines()

def rule_lines(lines):
    return [x.strip() for x in lines if x.strip() and not x.strip().startswith(("#",";","//"))]

def update_file(path):
    rows=read_lines(path)
    removed=[x for x in rows if x.strip().lower()==TARGET.lower()]
    if not removed:
        return 0
    if len(removed)>1:
        raise SystemExit("More than one xihuan entry in "+str(path))
    first=next((i for i,x in enumerate(rows) if x.strip() and not x.strip().startswith(("#",";","//"))),None)
    if first is None:
        raise SystemExit("No rule body in "+str(path))
    header=rows[:first]
    body=rows[first:]
    body=[x for x in body if x.strip().lower()!=TARGET.lower()]
    rules=rule_lines(body)
    clean=[]
    for line in header:
        s=line.strip()
        if not s:
            continue
        if re.match(r"^# [A-Z0-9_-]+:\s*\d+\s*$",s):
            continue
        clean.append(line)
    counts=Counter(x.split(",",1)[0].strip().upper() for x in rules)
    for kind in sorted(counts):
        clean.append(f"# {kind}: {counts[kind]}")
    clean.append(f"# TOTAL: {len(rules)}")
    path.write_text("\n".join(clean)+"\n\n"+"\n".join(body).rstrip()+"\n",encoding="utf-8")
    return 1

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--iana-tlds",required=True)
    args=ap.parse_args()
    tld_file=Path(args.iana_tlds)
    if not tld_file.is_file():
        raise SystemExit("IANA TLD reference unavailable; refusing to remove any rule")
    tlds={x.strip().lower() for x in tld_file.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")}
    if "xihuan" in tlds:
        raise SystemExit("xihuan is present in IANA root zone; refusing removal")
    changed=[]
    for path in sorted(ROOT.rglob("*.list")):
        if path.is_symlink():
            raise SystemExit("Symlink encountered: "+str(path))
        if update_file(path):
            changed.append(str(path.relative_to(ROOT)))
    report=[
        "# Security remediation report","",
        "## Removed rule",
        "- Rule: DOMAIN-SUFFIX,xihuan",
        "- Reason: xihuan is not present in the IANA root-zone TLD list. This public root-suffix rule cannot match a normal public DNS suffix; it was repeated in ChinaMax-family variants.",
        f"- Occurrences removed: {len(changed)}",
        "- Files changed:",
    ]
    report += [f"  - {x}" for x in changed] if changed else ["  - none"]
    report += [
        "",
        "## Safety boundaries",
        "- Only the exact DOMAIN-SUFFIX,xihuan rule was removed.",
        "- No other domain, App folder, file format, cached source metadata, or personal rule was changed by this remediation.",
        "- Other single-label suffixes were retained; their IANA/private status requires separate review.",
        "",
    ]
    (ROOT/"SECURITY-REMEDIATION-REPORT.md").write_text("\n".join(report),encoding="utf-8")
    print(json.dumps({"removed_occurrences":len(changed),"files_changed":changed},ensure_ascii=False))

if __name__=="__main__":
    main()
