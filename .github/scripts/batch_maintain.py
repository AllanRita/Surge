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

BLOCK_FILTER_SEGMENTS = {
    "block", "reject", "rejects", "filter", "filters",
    "adguardsdnsfilter", "easyprivacy",
    "advertising", "advertisinglite", "advertisingmitv", "advertisingtest",
    "privacy", "hijacking",
}
BLOCK_FILTER_README_MARKERS = (
    "去广告", "广告过滤", "广告拦截", "隐私保护", "反劫持",
    "adblock plus", "adguard dns filter", "easyprivacy",
)

def is_blocklist_path(path):
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        relative = path
    if any(part.casefold() in BLOCK_FILTER_SEGMENTS for part in relative.parts[:-1]):
        return True
    readme = path.parent / "README.md"
    if readme.is_file() and not readme.is_symlink():
        content = readme.read_text(encoding="utf-8", errors="replace").casefold()
        if any(marker in content for marker in BLOCK_FILTER_README_MARKERS):
            return True
    return False

def feed_hosts(path):
    """Parse URL feeds and URLhaus hostfiles, including IP-prefixed host rows."""
    if not path or not Path(path).is_file():
        return set()
    domain_pattern = re.compile(r"(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\\.)+[a-z]{2,63}")

    def candidate_host(token):
        value = token.strip().lower().strip("[](){}<>,;\\\"'")
        if "://" in value:
            value = value.split("://", 1)[1]
        value = value.split("/", 1)[0].split("?", 1)[0].split("#", 1)[0]
        if "@" in value:
            value = value.rsplit("@", 1)[1]
        if value.count(":") == 1:
            value = value.split(":", 1)[0]
        value = value.strip(".")
        try:
            ipaddress.ip_address(value)
            return None
        except ValueError:
            pass
        return value if domain_pattern.fullmatch(value) else None

    out = set()
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        value = line.strip()
        if not value or value.startswith(("#", ";")):
            continue
        # URLhaus hostfile rows may be "host CNAME ." or "IP host".
        # Ignore the trailing semicolon-delimited description.
        body = value.split(";", 1)[0].split("#", 1)[0]
        for token in body.split():
            host = candidate_host(token)
            if host:
                out.add(host)
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
   is_blocklist = is_blocklist_path(path)
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
    # Exact-host deletion requires independent corroboration and is excluded
    # from known block/filter lists. Parent suffixes are review-only.
    if "," in stripped and kind == "DOMAIN":
     host = value.lower().rstrip(".")
     if not is_blocklist:
      if host in corroborated:
       changes.append({"action":"REMOVE_CONFIRMED_THREAT","path":str(path),"line":no,"rule":stripped,"reason":"Exact hostname independently present in both OpenPhish and URLhaus"})
       totals["threats_removed"] += 1; changed = True; continue
      matched_feeds = [name for name, feed in (("OpenPhish", openphish), ("URLhaus", urlhaus)) if host in feed]
      if matched_feeds:
       findings.append({"severity":"REVIEW","path":str(path),"line":no,"rule":stripped,"reason":"Exact host found in only one available threat feed: " + ", ".join(matched_feeds)})
    elif "," in stripped and kind in {"DOMAIN-SUFFIX", "HOST-SUFFIX"}:
     suffix = value.lower().rstrip(".")
     matched = {}
     for feed_name, feed in (("OpenPhish", openphish), ("URLhaus", urlhaus)):
      hits = sorted(host for host in feed if host == suffix or host.endswith("." + suffix))
      if hits:
       matched[feed_name] = hits[:5]
     if matched:
      findings.append({"severity":"REVIEW","path":str(path),"line":no,"rule":stripped,"reason":"Threat host found beneath parent suffix; suffix is review-only and is never automatically deleted","matched_feeds":matched})
    kept.append(line)
   if changed:
    backup=Path(a.backup_dir)/("batch-"+str(a.batch).zfill(3))/str(path.relative_to(ROOT))
    backup.parent.mkdir(parents=True,exist_ok=True)
    backup.write_bytes(path.read_bytes())
    ending="\n" if raw.endswith("\n") else ""
    path.write_text("\n".join(kept)+ending,encoding="utf-8")
    totals["files_changed"]+=1
 if sha(PERSONAL)!=personal_before: raise SystemExit("Rule/Personal changed unexpectedly")
 out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True)
 report={"generated_utc":datetime.now(timezone.utc).isoformat(),"mode":"AUTO_REMEDIATE_CONSERVATIVE","batch":a.batch,"batch_size":100,"selected_folders":[p.name for p in selected],"summary":dict(totals),"openphish_loaded":len(openphish),"urlhaus_loaded":len(urlhaus),"corroborated_hosts":len(corroborated),"security_coverage_complete":bool(openphish and urlhaus),"personal_unchanged":True,"changes":changes,"review_findings":findings}
 (out/f"batch-{a.batch:03d}-maintenance.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"batch":a.batch,"folders":len(selected),"changes":dict(totals),"review_findings":len(findings),"security_coverage_complete":report["security_coverage_complete"]},ensure_ascii=False))

if __name__=="__main__": main()
