#!/usr/bin/env python3
"""Conservative automatic remediation for one 100-folder Surge batch."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse, hashlib, ipaddress, json, re

ROOT = Path("Rule/Upstream")
PERSONAL = Path("Rule/Personal")
MANIFEST = Path(".github/explicit-rule-exclusions.json")
DOMAIN_TYPES = {"DOMAIN", "DOMAIN-SUFFIX", "HOST", "HOST-SUFFIX"}
KNOWN_TYPES = {
 "DOMAIN","DOMAIN-SUFFIX","DOMAIN-KEYWORD","DOMAIN-WILDCARD","DOMAIN-REGEX",
 "IP-CIDR","IP-CIDR6","IP-ASN","GEOIP","USER-AGENT","URL-REGEX",
 "PROCESS-NAME","DEST-PORT","SRC-PORT","SRC-IP","IN-PORT","PROTOCOL",
 "AND","OR","NOT","RULE-SET","DOMAIN-SET","SUBNET","DEVICE-NAME",
 "HOST","HOST-SUFFIX","HOST-KEYWORD"
}

def sha(path):
 h=hashlib.sha256()
 if path.exists():
  for p in sorted(path.rglob("*")):
   if p.is_file() and not p.is_symlink():
    h.update(str(p.relative_to(path)).encode()); h.update(p.read_bytes())
 return h.hexdigest()

def tombstones():
 data=json.loads(MANIFEST.read_text(encoding="utf-8"))
 entries=data.get("exclusions")
 if not isinstance(entries,list): raise RuntimeError("Invalid tombstone manifest")
 out=set()
 for e in entries:
  n=e.get("folder","")
  if not n or n in {".",".."} or "/" in n or "\\" in n or e.get("path")!="Rule/Upstream/"+n:
   raise RuntimeError("Unsafe tombstone entry")
  out.add(n.casefold())
 return out

def feed_hosts(path):
 if not path or not Path(path).is_file(): return set()
 out=set()
 for line in Path(path).read_text(encoding="utf-8",errors="replace").splitlines():
  s=line.strip().lower()
  if not s or s.startswith(("#",";")): continue
  if "://" in s:
   s=s.split("://",1)[1].split("/",1)[0].split(":",1)[0]
  else:
   parts=s.split()
   s=parts[0].split("#",1)[0] if parts else ""
  s=s.strip(".")
  if re.fullmatch(r"(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}",s):
   out.add(s)
 return out

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--batch",type=int,required=True)
 ap.add_argument("--batch-size",type=int,default=100)
 ap.add_argument("--openphish")
 ap.add_argument("--urlhaus")
 ap.add_argument("--output-dir",default="batch-output")
 ap.add_argument("--backup-dir",default="batch-output/backups")
 a=ap.parse_args()
 if a.batch<1 or a.batch_size!=100: raise SystemExit("Batch size must be 100")
 if ROOT.is_symlink() or not ROOT.is_dir(): raise SystemExit("Unsafe or missing upstream root")
 denied=tombstones()
 folders=sorted((p for p in ROOT.iterdir() if p.is_dir() and not p.is_symlink() and p.name!="SourceMetadata"),key=lambda p:(p.name.casefold(),p.name))
 if any(p.name.casefold() in denied for p in folders): raise SystemExit("A tombstoned folder is present; stop before modifying files")
 start=(a.batch-1)*100
 selected=folders[start:start+100]
 if not selected: raise SystemExit("No folders for requested batch")
 personal_before=sha(PERSONAL)
 openphish=feed_hosts(a.openphish); urlhaus=feed_hosts(a.urlhaus)
 corroborated=openphish & urlhaus
 findings=[]; changes=[]; totals=Counter()
 for folder in selected:
  if folder.is_symlink(): raise SystemExit("Folder symlink")
  for path in sorted(folder.rglob("*.list")):
   if path.is_symlink(): raise SystemExit("Rule-file symlink: "+str(path))
   raw=path.read_text(encoding="utf-8-sig")
   lines=raw.splitlines()
   seen=set(); kept=[]; changed=False
   is_blocklist=any(x in str(path).lower() for x in ("reject","block","filter","adguard","easyprivacy"))
   for no,line in enumerate(lines,1):
    stripped=line.strip()
    if not stripped or stripped.startswith(("#",";","//")):
     kept.append(line); continue
    normalized=stripped
    if normalized in seen:
     changes.append({"action":"REMOVE_DUPLICATE","path":str(path),"line":no,"rule":stripped,"reason":"Exact duplicate rule line"})
     totals["duplicates_removed"]+=1; changed=True; continue
    seen.add(normalized)
    parts=[x.strip() for x in stripped.split(",")]
    kind=parts[0].upper()
    value=parts[1] if len(parts)>1 else ""
    invalid_reason=None
    if "," in stripped and kind in DOMAIN_TYPES:
     d=value.lower().rstrip(".")
     if not re.fullmatch(r"[a-z0-9_-]+(?:\.[a-z0-9_-]+)*",d):
      invalid_reason="Invalid domain operand"
    elif "," in stripped and kind in {"IP-CIDR","IP-CIDR6"}:
     try:
      net=ipaddress.ip_network(value,strict=False)
      if (kind=="IP-CIDR" and net.version!=4) or (kind=="IP-CIDR6" and net.version!=6):
       invalid_reason="IP version does not match rule type"
     except ValueError:
      invalid_reason="Invalid IP network"
    if invalid_reason:
     changes.append({"action":"REMOVE_INVALID","path":str(path),"line":no,"rule":stripped,"reason":invalid_reason})
     totals["invalid_removed"]+=1; changed=True; continue
    # Automatic threat removal is deliberately narrow: exact DOMAIN rows only,
    # exact host corroborated by both feeds, and never block/filter lists.
    if not is_blocklist and "," in stripped and kind=="DOMAIN":
     host=value.lower().rstrip(".")
     if host in corroborated:
      changes.append({"action":"REMOVE_CONFIRMED_THREAT","path":str(path),"line":no,"rule":stripped,"reason":"Exact hostname independently present in OpenPhish and URLhaus"})
      totals["threats_removed"]+=1; changed=True; continue
     if host in openphish or host in urlhaus:
      findings.append({"severity":"REVIEW","path":str(path),"line":no,"rule":stripped,"reason":"Exact host found in only one threat feed"})
    elif not is_blocklist and "," in stripped and kind=="DOMAIN-SUFFIX":
     host=value.lower().rstrip(".")
     if any(x==host or x.endswith("."+host) for x in corroborated):
      findings.append({"severity":"REVIEW","path":str(path),"line":no,"rule":stripped,"reason":"Threat host beneath parent suffix; parent suffix is not automatically deleted"})
    kept.append(line)
   if changed:
    ending="\n" if raw.endswith("\n") else ""
    path.write_text("\n".join(kept)+ending,encoding="utf-8")
    totals["files_changed"]+=1
 if sha(PERSONAL)!=personal_before: raise SystemExit("Rule/Personal changed unexpectedly")
 out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True)
 report={"generated_utc":datetime.now(timezone.utc).isoformat(),"mode":"AUTO_REMEDIATE_CONSERVATIVE","batch":a.batch,"batch_size":100,"selected_folders":[p.name for p in selected],"summary":dict(totals),"openphish_loaded":len(openphish),"urlhaus_loaded":len(urlhaus),"corroborated_hosts":len(corroborated),"security_coverage_complete":bool(openphish and urlhaus),"personal_unchanged":True,"changes":changes,"review_findings":findings}
 (out/f"batch-{a.batch:03d}-maintenance.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"batch":a.batch,"folders":len(selected),"changes":dict(totals),"review_findings":len(findings),"security_coverage_complete":report["security_coverage_complete"]},ensure_ascii=False))

if __name__=="__main__": main()
