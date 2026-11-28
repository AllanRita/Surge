#!/usr/bin/env python3
"""Sync the complete Surge rule-set tree from blackmatrix7 and remove only exact, dual-feed confirmed threat hosts."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlsplit
import argparse, hashlib, json, re, shutil, subprocess, tempfile

ROOT = Path("Rule/Upstream")
QUARANTINE = ROOT / "ThreatQuarantine"
ALLOWED_TYPES = {"DOMAIN","DOMAIN-SUFFIX","DOMAIN-KEYWORD","DOMAIN-WILDCARD","DOMAIN-REGEX","IP-CIDR","IP-CIDR6","IP-ASN","GEOIP","USER-AGENT","URL-REGEX","PROCESS-NAME","DEST-PORT","SRC-PORT","SRC-IP","IN-PORT","PROTOCOL","AND","OR","NOT","RULE-SET","DOMAIN-SET","SUBNET","DEVICE-NAME","HOST","HOST-SUFFIX","HOST-KEYWORD"}

def sha(b): return hashlib.sha256(b).hexdigest()

def host_from_url(value):
    try: return (urlsplit(value if "://" in value else "http://" + value).hostname or "").lower().rstrip(".")
    except ValueError: return ""

def openphish_hosts(path):
    out=set()
    for line in Path(path).read_text(encoding="utf-8",errors="replace").splitlines():
        s=line.strip()
        if s and not s.startswith(("#",";")):
            h=host_from_url(s)
            if h: out.add(h)
    return out

def urlhaus_hosts(path):
    out=set()
    for line in Path(path).read_text(encoding="utf-8",errors="replace").splitlines():
        s=line.strip()
        if not s or s.startswith(("#",";")): continue
        body=s.split(";",1)[0].split("#",1)[0]
        for token in body.split():
            h=host_from_url(token)
            if h and "." in h: out.add(h)
    return out

def validate_tree():
    files=sorted(ROOT.rglob("*.list"))
    folders=sorted({p.parent for p in files})
    errors=[]
    for p in files:
        if p.is_symlink(): errors.append({"path":str(p),"error":"symlink"}); continue
        b=p.read_bytes()
        if not b: errors.append({"path":str(p),"error":"empty file"})
        if b"\x00" in b: errors.append({"path":str(p),"error":"NUL byte"})
        try: text=b.decode("utf-8-sig")
        except UnicodeDecodeError:
            errors.append({"path":str(p),"error":"invalid UTF-8"}); continue
        for n,line in enumerate(text.splitlines(),1):
            s=line.strip()
            if not s or s.startswith(("#",";","//")): continue
            kind=s.split(",",1)[0].strip().upper()
            if "," in s and kind not in ALLOWED_TYPES:
                errors.append({"path":str(p),"line":n,"error":"unknown rule type","value":kind})
    return {"rule_files":len(files),"rule_folders":len(folders),"errors":errors}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--openphish")
    ap.add_argument("--urlhaus")
    ap.add_argument("--output",default="Rule/Upstream/SECURITY-SYNC-REPORT.json")
    a=ap.parse_args()
    if ROOT.is_symlink() or not ROOT.is_dir(): raise SystemExit("Unsafe or missing Rule/Upstream")
    if Path("Rule/Personal").is_symlink(): raise SystemExit("Rule/Personal symlink")
    personal_before={str(p.relative_to("Rule/Personal")):sha(p.read_bytes()) for p in Path("Rule/Personal").rglob("*") if p.is_file()}
    source_commit=""
    with tempfile.TemporaryDirectory() as td:
        clone=Path(td)/"source"
        subprocess.run(["git","clone","--depth","1","--branch","master","https://github.com/blackmatrix7/ios_rule_script.git",str(clone)],check=True)
        source_commit=subprocess.check_output(["git","-C",str(clone),"rev-parse","HEAD"],text=True).strip()
        source=clone/"rule"/"Surge"
        if not source.is_dir(): raise SystemExit("Upstream rule/Surge directory missing")
        source_files=sorted(source.rglob("*.list"))
        if not source_files: raise SystemExit("No upstream Surge .list files")
        # Remove old rule files and stale per-App README files, preserving root reports and non-rule assets.
        for p in ROOT.rglob("*.list"):
            if p.is_file() and not p.is_symlink(): p.unlink()
        for p in list(ROOT.rglob("README.md")):
            if p.parent != ROOT and p.is_file() and not p.is_symlink(): p.unlink()
        for folder in sorted((p for p in ROOT.rglob("*") if p.is_dir()),key=lambda x:len(x.parts),reverse=True):
            try: folder.rmdir()
            except OSError: pass
        imported=[]
        for src in source_files:
            rel=src.relative_to(source)
            dst=ROOT/rel
            dst.parent.mkdir(parents=True,exist_ok=True)
            data=src.read_bytes()
            dst.write_bytes(data)
            imported.append({"path":str(dst),"sha256":sha(data),"bytes":len(data)})
    openphish=set(); urlhaus=set()
    if a.openphish and Path(a.openphish).is_file(): openphish=openphish_hosts(a.openphish)
    if a.urlhaus and Path(a.urlhaus).is_file(): urlhaus=urlhaus_hosts(a.urlhaus)
    corroborated=openphish & urlhaus
    removals=[]
    if openphish and urlhaus:
        for p in sorted(ROOT.rglob("*.list")):
            original=p.read_text(encoding="utf-8-sig")
            kept=[]
            for n,line in enumerate(original.splitlines(),1):
                s=line.strip()
                parts=[x.strip() for x in s.split(",")]
                if len(parts)>=2 and parts[0].upper()=="DOMAIN":
                    host=parts[1].lower().rstrip(".")
                    if host in corroborated:
                        removals.append({"path":str(p),"line":n,"rule":s,"host":host,"feeds":["OpenPhish","URLhaus"],"removed_utc":datetime.now(timezone.utc).isoformat(),"sha256":sha(line.encode())})
                        continue
                kept.append(line)
            if len(kept)!=len(original.splitlines()):
                p.write_text("\n".join(kept)+("\n" if original.endswith("\n") else ""),encoding="utf-8")
    QUARANTINE.mkdir(parents=True,exist_ok=True)
    log=QUARANTINE/"removed-indicators.jsonl"
    if removals:
        with log.open("a",encoding="utf-8") as f:
            for item in removals: f.write(json.dumps(item,ensure_ascii=False)+"\n")
    validation=validate_tree()
    personal_after={str(p.relative_to("Rule/Personal")):sha(p.read_bytes()) for p in Path("Rule/Personal").rglob("*") if p.is_file()}
    if personal_before!=personal_after: raise SystemExit("Rule/Personal changed unexpectedly")
    report={"generated_utc":datetime.now(timezone.utc).isoformat(),"source":"blackmatrix7/ios_rule_script","source_branch":"master","source_commit":source_commit,"upstream_rule_files":len(imported),"upstream_file_manifest":imported,"openphish_hosts":len(openphish),"urlhaus_hosts":len(urlhaus),"automatic_deletion_enabled":bool(openphish and urlhaus),"corroborated_hosts":len(corroborated),"removed_exact_domain_rules":removals,"coverage_note":"OpenPhish phishing URLs and URLhaus malware URLs only; not comprehensive fraud/scam coverage. Missing either feed disables automatic deletion.","validation":{k:v for k,v in validation.items() if k!="errors"},"validation_errors":validation["errors"],"rule_personal_unchanged":True}
    Path(a.output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"imported":len(imported),"folders":validation["rule_folders"],"removed":len(removals),"validation_errors":len(validation["errors"]),"auto_delete":report["automatic_deletion_enabled"]}))
    if validation["errors"]: raise SystemExit("Full-tree validation failed")
if __name__=="__main__": main()
