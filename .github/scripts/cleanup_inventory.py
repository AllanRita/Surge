#!/usr/bin/env python3
"""Read-only inventory, source-coverage, and reputation audit for the frozen Surge rules."""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
from urllib.parse import urlsplit
import argparse, hashlib, ipaddress, json, re

ROOT=Path("Rule/Upstream"); PERSONAL=Path("Rule/Personal"); META=ROOT/"SourceMetadata"
FORMAT_SUFFIXES=(("_All_No_Resolve","all_no_resolve"),("_No_IPv6_Resolve","no_ipv6_resolve"),("_NoIPv6_Resolve","no_ipv6_resolve"),("_All_NoResolve","all_no_resolve"),("_No_Resolve","no_resolve"),("_NoResolve","no_resolve"),("_No_IPv6","no_ipv6"),("_NoIPv6","no_ipv6"),("_Resolve","resolve"),("_Domain","domain_only"),("_All","all"))
ALIAS_GROUPS=[
 {"canonical":"Abema","aliases":["AbemaTV"],"reason":"Same service under former/alternate name; prior union verified."},
 {"canonical":"Gemini","aliases":["BardAI"],"reason":"Same Google assistant service after renaming; prior union verified."},
 {"canonical":"PChome","aliases":["PChomeTW"],"reason":"Same PChome Online service; prior union verified."},
 {"canonical":"GlobalScholar","aliases":["Scholar"],"reason":"GlobalScholar README explicitly says Scholar is included; prior union adds cnki.net."},
 {"canonical":"BiliBili","aliases":["BiliBiliIntl"],"reason":"Same Bilibili service family with international variant."},
 {"canonical":"iQIYI","aliases":["iQIYIIntl"],"reason":"Same iQIYI service family with international variant."},
 {"canonical":"Hulu","aliases":["HuluUSA","HuluJP"],"reason":"Same Hulu app/service with US and Japan regional domains."},
 {"canonical":"Telegram","aliases":["TelegramNL","TelegramSG","TelegramUS"],"reason":"Same Telegram app; regional files are IP-range subsets."},
 {"canonical":"Amazon","aliases":["AmazonCN"],"reason":"Same Amazon service family with China-region domains."},
 {"canonical":"HBO","aliases":["HBOAsia","HBOHK","HBOUSA"],"reason":"Same HBO/Max service family with regional rules."},
 {"canonical":"Cloudflare","aliases":["Cloudflarecn"],"reason":"Same Cloudflare service with China-specific domain subset."},
 {"canonical":"Steam","aliases":["SteamCN"],"reason":"Same Steam service family with China-region domains."},
 {"canonical":"Assassin'sCreed/Assassin'sCreed-Odyssey","aliases":["Game/Assassin'sCreed-Odyssey"],"reason":"Same game duplicated under two categories; Standard and Resolve stay separate."},
 {"canonical":"Assassin'sCreed/Assassin'sCreed-Origins","aliases":["Game/Assassin'sCreed-Origins"],"reason":"Same game duplicated under two categories; Standard and Resolve stay separate."},
]
SOURCE_TARGETS={
 "Aoang-Apple":"Apple/Apple.list","Aoang-DNS":"Block/DNS/DNS.list",
 "Aoang-OneDrive":"OneDrive/OneDrive.list","Aoang-Other":"Block/Other/Other.list",
 "Aoang-Parallels":"Block/Parallels/Parallels.list","Aoang-Process":"Process/Process/Process.list",
 "Aoang-Teams":"Teams/Teams.list","Aoang-Unavailable":"Process/Unavailable/Unavailable.list",
 "Aoang-YouTube":"Block/YouTube/YouTube.list","Apple":"Apple/Apple.list",
 "BiliBiliIntl":"BiliBili/BiliBili.list","GitLab":"GitLab/GitLab.list",
 "Microsoft":"Microsoft/Microsoft.list","NetEaseMusic":"NetEaseMusic/NetEaseMusic.list",
 "Telegram":"Telegram/Telegram.list",
}
KNOWN_FINANCIAL={"alipay","boc","bocom","ccb","ceb","cgb","cmb","icbc","psbc","paypal","stripe","unionpay","visa","pingan","paypay","wechatpay","applepay","googlepay","samsungpay","mastercard","amex","americanexpress","discover","jcb","paytm","phonepe","cashapp","venmo","payoneer","revolut","wise","adyen","worldpay","klarna","afterpay","affirm","square","paddle","checkout","wallet"}
FINANCIAL_RE=re.compile(r"(?i)(?:[a-z0-9_-]+\.)*(?:paypal\.com|alipay\.com|stripe\.com|unionpay\.com|visa\.com|icbc\.com\.cn|boc\.cn|paypay\.ne\.jp)$")
FINANCIAL_APP_REVIEW_CANDIDATES={
 "Binance":"crypto exchange",
 "OKX":"crypto exchange",
 "EastMoney":"securities brokerage / investment platform",
 "TigerFintech":"securities brokerage / investment platform",
 "Crypto":"cryptocurrency category list (not a single App)",
 "Cryptocurrency":"cryptocurrency category list (not a single App)",
}
SHARED_HOSTING_SUFFIXES={
 "cloudfront.net":"shared CDN / Amazon CloudFront",
 "amazonaws.com":"shared cloud infrastructure / AWS",
 "pages.dev":"Cloudflare Pages shared hosting",
 "workers.dev":"Cloudflare Workers shared hosting",
 "trycloudflare.com":"Cloudflare temporary tunnel",
 "gitbook.io":"shared documentation hosting",
 "github.io":"GitHub Pages shared hosting",
 "gitlab.io":"GitLab Pages shared hosting",
 "bitbucket.io":"Bitbucket Pages hosting",
 "blogspot.com":"Blogger shared hosting",
 "web.app":"Firebase Hosting",
 "firebaseapp.com":"Firebase Hosting",
 "appspot.com":"Google App Engine hosting",
 "vercel.app":"Vercel shared hosting",
 "netlify.app":"Netlify shared hosting",
 "herokuapp.com":"Heroku shared hosting",
 "onrender.com":"Render shared hosting",
 "fly.dev":"Fly.io shared hosting",
 "railway.app":"Railway shared hosting",
 "replit.app":"Replit shared hosting",
 "replit.dev":"Replit shared hosting",
 "glitch.me":"Glitch shared hosting",
 "surge.sh":"Surge.sh shared hosting",
 "azurewebsites.net":"Azure App Service hosting",
 "azurestaticapps.net":"Azure Static Web Apps",
 "cloudapp.net":"Azure Cloud Services",
 "azureedge.net":"Azure CDN",
 "azurefd.net":"Azure Front Door shared CDN",
 "weebly.com":"Weebly shared website hosting",
 "duckdns.org":"dynamic DNS",
 "no-ip.org":"dynamic DNS",
 "ddns.net":"dynamic DNS",
 "dynu.net":"Dynu dynamic DNS",
 "eu.org":"subdomain hosting",
 "is.gd":"URL shortener",
 "bit.ly":"URL shortener",
 "tinyurl.com":"URL shortener",
 "t.co":"URL shortener",
 "cutt.ly":"URL shortener",
 "rebrand.ly":"URL shortener",
 "shorturl.at":"URL shortener",
 "linktr.ee":"link-in-bio / redirect platform",
}
ALLOWED={"DOMAIN","DOMAIN-SUFFIX","DOMAIN-KEYWORD","DOMAIN-WILDCARD","DOMAIN-REGEX","IP-CIDR","IP-CIDR6","IP-ASN","GEOIP","USER-AGENT","URL-REGEX","PROCESS-NAME","DEST-PORT","SRC-PORT","SRC-IP","IN-PORT","PROTOCOL","AND","OR","NOT","RULE-SET","DOMAIN-SET","SUBNET","DEVICE-NAME","HOST","HOST-SUFFIX","HOST-KEYWORD"}
DOMAIN_TYPES={"DOMAIN","DOMAIN-SUFFIX","HOST","HOST-SUFFIX"}; IP_TYPES={"IP-CIDR","IP-CIDR6"}

def lines(path):
 try: return path.read_text(encoding="utf-8-sig").splitlines()
 except (OSError,UnicodeError): return []
def rules(path): return [x.strip() for x in lines(path) if x.strip() and not x.strip().startswith(("#",";","//"))]
def fmt(stem):
 for suffix,label in FORMAT_SUFFIXES:
  if stem.endswith(suffix): return stem[:-len(suffix)],label
 return stem,"standard"
def feed_domains(path,kind):
 out=set()
 if not path or not Path(path).is_file(): return out
 for raw in lines(Path(path)):
  x=raw.strip()
  if not x or x.startswith(("#",";","!")): continue
  if kind=="url":
   try: host=urlsplit(x if "://" in x else "http://"+x).hostname
   except ValueError: host=None
   if host: out.add(host.lower().rstrip("."))
  else:
   for token in x.split():
    token=token.lower().rstrip(".")
    if not token or token in {"0.0.0.0","127.0.0.1","::1","localhost"}: continue
    try: ipaddress.ip_address(token); continue
    except ValueError: pass
    if re.fullmatch(r"(?i)[a-z0-9-]+(?:\.[a-z0-9-]+)+",token): out.add(token)
 return out
def domain_covered(rule,target_rules):
 p=rule.split(",")
 if len(p)<2 or p[0].upper() not in DOMAIN_TYPES: return False
 value=p[1].strip().lower().rstrip(".")
 for target in target_rules:
  q=target.split(",")
  if len(q)<2: continue
  if target.lower()==rule.lower(): return True
  if q[0].upper() in {"DOMAIN-SUFFIX","HOST-SUFFIX"}:
   d=q[1].strip().lower().rstrip(".")
   if value==d or value.endswith("."+d): return True
 return False
def ip_covered(rule,target_rules):
 p=rule.split(",")
 if len(p)<2 or p[0].upper() not in IP_TYPES: return False
 try: src=ipaddress.ip_network(p[1].strip(),strict=False)
 except ValueError: return False
 for target in target_rules:
  q=target.split(",")
  if len(q)<2 or q[0].upper() not in IP_TYPES: continue
  try:
   net=ipaddress.ip_network(q[1].strip(),strict=False)
   if src.version==net.version and src.subnet_of(net): return True
  except ValueError: pass
 return False
def rule_covered(rule,target_rules):
 if rule.lower() in {x.lower() for x in target_rules}: return True
 return domain_covered(rule,target_rules) or ip_covered(rule,target_rules)

def source_coverage():
 out=[]
 for name,target_rel in sorted(SOURCE_TARGETS.items()):
  mp=META/(name+".json"); tp=ROOT/target_rel
  if not mp.is_file(): out.append({"source":name,"target":target_rel,"error":"cached metadata missing"}); continue
  if not tp.is_file(): out.append({"source":name,"target":target_rel,"error":"mapped target missing"}); continue
  try: meta=json.loads(mp.read_text(encoding="utf-8"))
  except (OSError,ValueError) as e: out.append({"source":name,"target":target_rel,"error":str(e)}); continue
  target_rules=rules(tp); counts=Counter(); missing=[]
  for rule in meta.get("rules",[]):
   if rule.lower() in {x.lower() for x in target_rules}: counts["exact"]+=1
   elif domain_covered(rule,target_rules): counts["parent_suffix"]+=1
   elif ip_covered(rule,target_rules): counts["ip_range"]+=1
   else:
    counts["missing"]+=1
    if len(missing)<100: missing.append(rule)
  out.append({"source":name,"source_url":meta.get("source"),"license":meta.get("license"),"source_commit":meta.get("commit"),"source_path":meta.get("path"),"source_rules":len(meta.get("rules",[])),"target":target_rel,"target_rules":len(target_rules),"exact":counts["exact"],"parent_suffix":counts["parent_suffix"],"ip_range":counts["ip_range"],"missing_count":counts["missing"],"missing_examples":missing})
 return out
def alias_report():
 out=[]
 for g in ALIAS_GROUPS:
  by_fmt=defaultdict(list)
  for folder in [g["canonical"]]+g["aliases"]:
   p=ROOT/folder
   if p.is_dir():
    for f in sorted(p.rglob("*.list")):
     by_fmt[fmt(f.stem)[1]].append({"path":str(f.relative_to(ROOT)),"folder":folder,"rules":rules(f)})
  comps=[]
  for label,items in sorted(by_fmt.items()):
   canon=[x for x in items if x["folder"]==g["canonical"]]
   alias=[x for x in items if x["folder"]!=g["canonical"]]
   if not canon or not alias: continue
   base=set(canon[0]["rules"]); union=set(base); missing=set()
   for item in alias:
    union.update(item["rules"])
    for rule in item["rules"]:
     if not rule_covered(rule,canon[0]["rules"]): missing.add(rule)
   missing=sorted(missing)
   comps.append({"format":label,"canonical_file":canon[0]["path"],"alias_files":[x["path"] for x in alias],"canonical_lines":len(base),"alias_lines":sum(len(x["rules"]) for x in alias),"union_unique_lines":len(union),"new_semantic_lines":len(missing),"new_examples":missing[:30]})
  out.append({"canonical":g["canonical"],"aliases":g["aliases"],"reason":g["reason"],"canonical_exists":(ROOT/g["canonical"]).is_dir(),"existing_aliases":[x for x in g["aliases"] if (ROOT/x).is_dir()],"comparisons":comps})
 return out

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--iana-tlds"); ap.add_argument("--urlhaus"); ap.add_argument("--openphish"); a=ap.parse_args()
 tlds={x.strip().lower() for x in lines(Path(a.iana_tlds)) if x.strip() and not x.startswith("#")} if a.iana_tlds and Path(a.iana_tlds).is_file() else set()
 urlhaus=feed_domains(a.urlhaus,"hosts"); openphish=feed_domains(a.openphish,"url")
 def suffix_index(domains):
  out={}
  for bad in domains:
   parts=bad.split(".")
   for i in range(len(parts)):
    out.setdefault(".".join(parts[i:]),bad)
  return out
 urlhaus_suffix=suffix_index(urlhaus); openphish_suffix=suffix_index(openphish)
 files=sorted(p for p in ROOT.rglob("*.list") if p.is_file()); folders=defaultdict(list); rawhash=defaultdict(list); payloadhash=defaultdict(list)
 file_rows=[]; findings=Counter(); examples=defaultdict(list); financial=[]; threat=[]; threat_scope=Counter(); domain_count=0; shared_hosting_hits=defaultdict(lambda:{"count":0,"paths":set(),"folders":set(),"examples":[]})
 for path in files:
  rel=path.relative_to(ROOT); folder=str(rel.parent); folders[folder].append(path)
  raw=path.read_bytes(); row_rules=rules(path); payload="\n".join(row_rules).encode()
  rawhash[hashlib.sha256(raw).hexdigest()].append(str(rel)); payloadhash[hashlib.sha256(payload).hexdigest()].append(str(rel))
  dup=Counter(row_rules); findings["duplicate_rule_lines"]+=sum(n-1 for n in dup.values() if n>1); types=Counter()
  for num,line in enumerate(lines(path),1):
   if any(ord(c)<32 and c not in "\t" for c in line):
    findings["hidden_control"]+=1
    if len(examples["hidden_control"])<30: examples["hidden_control"].append(f"{rel}:{num}")
   s=line.strip()
   if not s or s.startswith(("#",";","//")): continue
   # Recognize AdGuard-native filters and bare domain-only lines without
   # incorrectly counting them as malformed Surge rules.
   native=s
   adguard=native[4:] if native.startswith("@@||") else (native[2:] if native.startswith("||") else "")
   if adguard:
    host=re.split(r"[\^/$:*]",adguard,1)[0].strip(".")
    if re.fullmatch(r"(?i)[a-z0-9_-]+(?:\.[a-z0-9_-]+)+",host):
     findings["recognized_native_filter"]+=1
     if FINANCIAL_RE.fullmatch(host): financial.append(f"{rel}:{num}: {s}")
    else:
     findings["invalid_native_filter"]+=1
     if len(examples["invalid_native_filter"])<30: examples["invalid_native_filter"].append(f"{rel}:{num}: {s[:140]}")
    continue
   if native.startswith("/") and native.endswith("/") and len(native)>2:
    findings["recognized_native_regex"]+=1
    continue
   bare=native[1:] if native.startswith(".") else native
   if "," not in native and re.fullmatch(r"(?i)[a-z0-9_-]+(?:\.[a-z0-9_-]+)+",bare):
    findings["recognized_native_domain"]+=1
    if FINANCIAL_RE.fullmatch(bare): financial.append(f"{rel}:{num}: {s}")
    continue
   p=s.split(","); kind=p[0].strip().upper(); value=p[1].strip() if len(p)>1 else ""; types[kind]+=1
   if kind not in ALLOWED or not value:
    findings["unsupported_or_missing_operand"]+=1
    if len(examples["unsupported_or_missing_operand"])<30: examples["unsupported_or_missing_operand"].append(f"{rel}:{num}: {s[:140]}")
    continue
   if kind in IP_TYPES:
    try:
     net=ipaddress.ip_network(value,strict=False)
     if (kind=="IP-CIDR" and net.version!=4) or (kind=="IP-CIDR6" and net.version!=6):
      findings["ip_family_mismatch"]+=1
      if len(examples["ip_family_mismatch"])<30: examples["ip_family_mismatch"].append(f"{rel}:{num}: {s}")
     if net.prefixlen==0:
      findings["catch_all_network"]+=1
      if len(examples["catch_all_network"])<30: examples["catch_all_network"].append(f"{rel}:{num}: {s}")
    except ValueError:
     findings["invalid_network"]+=1
     if len(examples["invalid_network"])<30: examples["invalid_network"].append(f"{rel}:{num}: {s[:140]}")
   if kind in DOMAIN_TYPES:
    domain=value.lower().rstrip("."); domain_count+=1
    if kind in {"DOMAIN-SUFFIX","HOST-SUFFIX"} and domain in SHARED_HOSTING_SUFFIXES:
     hit=shared_hosting_hits[domain]
     hit["count"]+=1
     hit["paths"].add(str(rel))
     hit["folders"].add(str(rel.parent))
     if len(hit["examples"])<20: hit["examples"].append(f"{rel}:{num}: {s}")
    if not re.fullmatch(r"[a-z0-9_-]+(?:\.[a-z0-9_-]+)*",domain):
     findings["invalid_domain"]+=1
     if len(examples["invalid_domain"])<30: examples["invalid_domain"].append(f"{rel}:{num}: {s[:140]}")
    if len(domain.split("."))<2:
     findings["single_label_suffix"]+=1
     if len(examples["single_label_suffix"])<50: examples["single_label_suffix"].append(f"{rel}:{num}: {s}")
     if tlds and domain not in tlds:
      findings["stale_or_private_root_suffix"]+=1
      if len(examples["stale_or_private_root_suffix"])<50: examples["stale_or_private_root_suffix"].append(f"{rel}:{num}: {s}")
    if FINANCIAL_RE.fullmatch(domain): financial.append(f"{rel}:{num}: {s}")
    if len(domain.split("."))>=2 and domain not in tlds:
     for feed_name,feed,suffixes in (("URLhaus",urlhaus,urlhaus_suffix),("OpenPhish",openphish,openphish_suffix)):
      if kind in {"DOMAIN-SUFFIX","HOST-SUFFIX"}: match=suffixes.get(domain)
      else: match=domain if domain in feed else None
      if match:
       scope="block_or_filter" if any(x in rel.parts for x in ("Block","Advertising","AdvertisingLite","AdvertisingTest","AdGuardSDNSFilter","Privacy","Hijacking")) else "app_or_routing"
       threat_scope[scope]+=1
       if len(threat)<500: threat.append({"feed":feed_name,"scope":scope,"path":str(rel),"line":num,"rule":s,"matched_domain":match})
 financial_folders=[]
 for folder in folders:
  norm=re.sub(r"[^a-z0-9]+","",folder.split("/")[-1].lower())
  if norm in KNOWN_FINANCIAL or any(x in norm for x in ("alipay","paypal","stripe","unionpay","visa","mastercard","paypay","wechatpay","applepay","googlepay","samsungpay","bank","paytm","phonepe","cashapp","venmo","payoneer","revolut","klarna","afterpay","affirm","adyen","worldpay","americanexpress","jcb")):
   financial_folders.append(folder)
 finance_review=[]
 for folder,members in sorted(folders.items()):
  name=folder.split("/")[-1]
  if name in FINANCIAL_APP_REVIEW_CANDIDATES:
   finance_review.append({"folder":folder,"classification":FINANCIAL_APP_REVIEW_CANDIDATES[name],"rule_file_count":len(members),"rule_occurrences":sum(len(rules(p)) for p in members),"files":[str(p.relative_to(ROOT)) for p in sorted(members)],"status":"review_only_not_removed"})
 rawdups=[x for x in rawhash.values() if len(x)>1]; payloaddups=[x for x in payloadhash.values() if len(x)>1]
 multi=[]
 for folder,members in sorted(folders.items()):
  if len(members)>1: multi.append({"folder":folder,"file_count":len(members),"formats":sorted({fmt(x.stem)[1] for x in members}),"files":[str(x.relative_to(ROOT)) for x in members]})
 aliases=alias_report(); coverage=source_coverage(); personal=sorted(str(p) for p in PERSONAL.rglob("*") if p.is_file()) if PERSONAL.exists() else []
 data={
  "generated_utc":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
  "scope":"Existing Rule/Upstream and cached SourceMetadata only. No rule authors fetched. This audit does not edit rules.",
  "summary":{"rule_files":len(files),"app_or_category_folders":len(folders),"top_level_folders":len({p.relative_to(ROOT).parts[0] for p in files}),"total_rule_bytes":sum(p.stat().st_size for p in files),"multi_file_folders":len(multi),"exact_raw_duplicate_file_groups":len(rawdups),"same_rule_payload_file_groups":len(payloaddups),"duplicate_rule_lines":findings["duplicate_rule_lines"],"domain_rule_count":domain_count,"personal_files_seen_not_modified":len(personal),"bank_payment_app_folders_found":len(financial_folders),"finance_app_review_candidates":len(finance_review),"cached_author_source_count":len(coverage),"cached_author_source_rule_count":sum(x.get("source_rules",0) for x in coverage),"cached_author_source_missing_count":sum(x.get("missing_count",0) for x in coverage),"shared_hosting_suffixes_found":len(shared_hosting_hits),"shared_hosting_suffix_rule_occurrences":sum(x["count"] for x in shared_hosting_hits.values())},
  "bank_payment_app_folders":financial_folders,"finance_app_review_candidates":finance_review,"personal_files_seen_not_modified":personal,"multi_format_folders":multi,
  "exact_raw_duplicate_file_groups":rawdups,"same_rule_payload_file_groups":payloaddups,"alias_candidates":aliases,
  "cached_source_coverage":coverage,"static_security_findings":dict(findings),"static_security_examples":{k:v[:50] for k,v in examples.items()},"financial_domain_matches_not_deleted":financial[:500],
  "shared_hosting_suffix_matches":[{"suffix":suffix,"classification":SHARED_HOSTING_SUFFIXES[suffix],"rule_occurrences":hit["count"],"folders":sorted(hit["folders"]),"files":sorted(hit["paths"]),"examples":hit["examples"]} for suffix,hit in sorted(shared_hosting_hits.items())],
  "reputation_feed_status":{"urlhaus_domains":len(urlhaus),"openphish_domains":len(openphish),"feeds_available":bool(urlhaus or openphish),"urlhaus_file_present":bool(a.urlhaus and Path(a.urlhaus).is_file()),"openphish_file_present":bool(a.openphish and Path(a.openphish).is_file()),"urlhaus_status":"loaded" if urlhaus else "not loaded; authenticated hostfile export requires the URLHAUS_AUTH_KEY repository secret","note":"Reputation matches are review flags, not automatic deletions. Matches in block/filter lists may be expected."},
  "reputation_matches":threat,"reputation_match_counts_by_scope":dict(threat_scope),"files":file_rows,
 }
 (ROOT/"CLEANUP-INVENTORY.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 md=["# Surge rule cleanup inventory and security audit","",f"Generated: {data['generated_utc']}","","Scope: existing rule files and cached source metadata only. No new rule authors or rule lists were fetched. This report is read-only and does not alter rule files.","","## Inventory","",f"- Rule files: **{len(files)}**",f"- App/category folders: **{len(folders)}**",f"- Top-level folders: **{data['summary']['top_level_folders']}**",f"- Rule data size: **{data['summary']['total_rule_bytes']:,} bytes**",f"- Folders with multiple files/formats: **{len(multi)}**",f"- Exact byte-identical file groups: **{len(rawdups)}**",f"- Identical rule-payload groups (headers ignored): **{len(payloaddups)}**",f"- Duplicate rule lines inside files: **{findings['duplicate_rule_lines']}**",f"- Personal files inspected but not modified: **{len(personal)}**","","## Bank/payment App folders","","This classifies dedicated App folders by folder name only. Financial-service domains inside other App or aggregate lists are not removed."]
 md += [f"- {x}" for x in financial_folders] if financial_folders else ["- No dedicated bank/payment App folders found under Rule/Upstream. Rule/Personal/PayPay.list remains untouched."]
 md += ["","## Other finance/trading/crypto folders — review only","","These folders are not automatically classified as bank/payment Apps. They are listed for manual classification only; no rule files are deleted or modified.","","| Folder | Classification | Rule files | Rule entries | Status |","|---|---|---:|---:|---|"]
 for x in finance_review: md.append(f"| {x['folder']} | {x['classification']} | {x['rule_file_count']} | {x['rule_occurrences']} | Review only |")
 if not finance_review: md.append("| — | No additional finance candidates | 0 | 0 | — |")
 md += ["","## Same-App / regional alias candidates",""]
 for g in aliases:
  md += [f"### {g['canonical']}",f"- Candidate folders: {', '.join(g['aliases'])}",f"- Present aliases: {', '.join(g['existing_aliases']) if g['existing_aliases'] else 'none'}",f"- Rationale: {g['reason']}"]
  for c in g["comparisons"]:
   md.append(f"- {c['format']}: canonical {c['canonical_lines']} lines; aliases {c['alias_lines']} lines; union {c['union_unique_lines']} unique; new semantic lines {c['new_semantic_lines']}")
   for x in c["new_examples"][:10]: md.append(f"  - {x}")
 md += ["","## Known shared-hosting, dynamic-DNS, and URL-shortener suffixes","","This curated scan checks exact DOMAIN-SUFFIX / HOST-SUFFIX rules across all upstream lists. It is a review inventory, not an automatic deletion list; a platform suffix may be intentional in a particular scenario.","","| Suffix | Classification | Rule occurrences | Folders |","|---|---|---:|---|"]
 for x in data["shared_hosting_suffix_matches"]:
  md.append(f"| {x['suffix']} | {x['classification']} | {x['rule_occurrences']} | {', '.join(x['folders'])} |")
 if not data["shared_hosting_suffix_matches"]: md.append("| — | No curated suffix matches | 0 | — |")
 md += ["","## Cached author-source coverage","","- Cached source snapshots compared: **"+str(len(coverage))+"**","- Source rule entries checked: **"+str(sum(x.get('source_rules',0) for x in coverage))+"**","- Missing source rules: **"+str(sum(x.get('missing_count',0) for x in coverage))+"**","- Scope limitation: only cached author snapshots are compared. This does not establish that every App has been compared against every author. No new authors or rule lists were fetched.","","| Cached source | Target | Source rules | Exact | Parent suffix | IP covered | Missing |","|---|---|---:|---:|---:|---:|---:|"]
 for r in coverage:
  if r.get("error"): md.append(f"| {r['source']} | {r['target']} | — | — | — | — | {r['error']} |")
  else:
   md.append(f"| {r['source']} | {r['target']} | {r['source_rules']} | {r['exact']} | {r['parent_suffix']} | {r['ip_range']} | {r['missing_count']} |")
   for x in r["missing_examples"][:15]: md.append(f"  - Missing candidate for {r['source']}: {x}")
 md += ["","## Static security checks",""]
 for k,v in sorted(findings.items()): md.append(f"- {k}: {v}")
 for x in examples.get("unsupported_or_missing_operand",[])[:30]: md.append(f"  - {x}")
 for x in examples.get("invalid_domain",[])[:30]: md.append(f"  - {x}")
 for x in examples.get("invalid_network",[])[:30]: md.append(f"  - {x}")
 md += ["","- Detailed threat-feed and broad shared-hosting review: see SECURITY-REVIEW.md.",f"- Financial-domain matches: {len(financial)} (review only; not deleted)",f"- URLhaus domains loaded: {len(urlhaus)}",("- URLhaus status: authenticated hostfile not loaded; configure the GitHub Actions secret URLHAUS_AUTH_KEY to enable it" if not urlhaus else "- URLhaus status: authenticated hostfile loaded"),f"- OpenPhish domains loaded: {len(openphish)}",f"- Reputation matches shown: {len(threat)} (max 500); scope counts: {dict(threat_scope)}","- Reputation-feed matches are review flags, not automatic deletions. Matches in block/filter lists may be intentional; app/routing matches need manual review.","","## Exact duplicate files",""]
 md += [", ".join(x) for x in rawdups] if rawdups else ["- None"]
 md += ["","## Identical rule payloads with headers ignored",""]
 md += [", ".join(x) for x in payloaddups] if payloaddups else ["- None"]
 md += ["","## Multi-format folders","","Format labels are inferred from filename suffixes; distinct formats are preserved unless explicitly approved after content comparison.",""]
 for x in multi: md.append(f"- {x['folder']}: {', '.join(x['formats'])} ({x['file_count']} files)")
 md += ["","## Safety boundaries","- No rule files or personal files are deleted, renamed, or rewritten by this audit.","- Bank/payment classification applies to dedicated App folders only; domains embedded in other Apps remain untouched.","- Regional variants are candidates for consolidation into one App policy group; country selection belongs in the Surge policy group, not separate rule folders.","- Resolve / non-Resolve and other distinct formats are compared and preserved separately.","- Similarity, shared CDN domains, or parent-company ownership alone never authorizes cross-App merging.",""]
 (ROOT/"CLEANUP-INVENTORY.md").write_text("\n".join(md),encoding="utf-8")

 # Separate review of threat-feed matches. A parent suffix match means a known
 # phishing/malware host exists beneath the suffix; it does not mean the suffix
 # itself is malicious or should be deleted.
 shared_hosting=SHARED_HOSTING_SUFFIXES
 grouped=defaultdict(lambda:{"matched_domains":set(),"paths":set(),"feeds":set(),"scopes":set()})
 for item in threat:
  key=item["rule"]
  grouped[key]["matched_domains"].add(item["matched_domain"])
  grouped[key]["paths"].add(item["path"])
  grouped[key]["feeds"].add(item["feed"])
  grouped[key]["scopes"].add(item["scope"])
 sec=[
  "# Security reputation review","",
  f"Generated: {data['generated_utc']}","",
  "This report compares current domain rules against public threat-intelligence feeds. A feed match is a review signal, not proof that the rule's parent domain is malicious. No rules are automatically removed.","",
  f"- URLhaus domains loaded: {len(urlhaus)}",
  f"- OpenPhish domains loaded: {len(openphish)}",
  f"- Rule-to-feed matches: {len(threat)} (up to 500 retained in the JSON report)",
  f"- Scope counts: {dict(threat_scope)}","",
 ]
 if not urlhaus:
  sec.append("- URLhaus hostfile not loaded: the current export requires an Auth-Key. Configure the GitHub Actions secret URLHAUS_AUTH_KEY to enable authenticated checks; OpenPhish was used for this run.")
 sec += ["","## Matched rules",""]
 if not grouped:
  sec.append("- No rule-to-feed matches.")
 for rule,info in sorted(grouped.items()):
  suffix=rule.split(",",1)[1].strip().lower() if "," in rule else ""
  provider=shared_hosting.get(suffix)
  sec += [
   f"### {rule}",
   f"- Scope: {', '.join(sorted(info['scopes']))}",
   f"- Feed(s): {', '.join(sorted(info['feeds']))}",
   f"- Rule files: {', '.join(sorted(info['paths']))}",
   f"- Matched feed host examples: {', '.join(sorted(info['matched_domains'])[:12])}",
  ]
  if provider:
   sec.append(f"- Classification: {provider}; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.")
  elif "block_or_filter" in info["scopes"]:
   sec.append("- Classification: match occurs in a block/filter list; this is generally expected and should not be treated as an App allow/routing problem.")
  else:
   sec.append("- Classification: app/routing match; verify that the domain is genuinely required by the App and is not an overly broad shared service.")
  sec.append("")
 sec += ["","## Known shared-hosting suffixes in the rule library","","The curated suffix scan covers all upstream rule files, not only threat-feed matches. These are broad multi-tenant or shared-platform namespaces; presence is not proof of maliciousness and no rule is automatically removed.","","| Suffix | Classification | Rule occurrences | Folders |","|---|---|---:|---|"]
 for x in data["shared_hosting_suffix_matches"]:
  sec.append(f"| {x['suffix']} | {x['classification']} | {x['rule_occurrences']} | {', '.join(x['folders'])} |")
 if not data["shared_hosting_suffix_matches"]: sec.append("| — | No curated suffix matches | 0 | — |")
 sec += ["## Stale/private single-label suffixes",""]
 sec += [f"- {x}" for x in examples.get("stale_or_private_root_suffix",[])] if examples.get("stale_or_private_root_suffix") else ["- None detected or IANA TLD feed unavailable."]
 sec += ["","## Financial-service domains","",
  f"- Financial-domain rule matches found: {len(financial)}",
  "- These are retained. The user's rule is to remove dedicated bank/payment App folders only, not payment-related domains embedded in other App or block/filter lists.",
  "- Rule/Personal was not modified.","",
  "## Interpretation",
  "- OpenPhish/URLhaus matches under a shared CDN or hosting suffix are not direct evidence that the App rule itself is malicious.",
  "- Shared hosting suffixes can match unrelated tenants. Review broad suffixes before assigning them to an App-specific policy group.",
  "- No automatic deletion or rewriting is performed by this report.",""
 ]
 (ROOT/"SECURITY-REVIEW.md").write_text("\n".join(sec),encoding="utf-8")
 print(json.dumps(data["summary"],ensure_ascii=False))

if __name__=="__main__": main()
