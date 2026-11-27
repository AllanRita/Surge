#!/usr/bin/env python3
"""Merge approved same-App and regional folders into one App policy folder."""
from pathlib import Path
from collections import Counter
import ipaddress, json, re, shutil

ROOT=Path("Rule/Upstream")
PLAN=Path("Rule/CONSOLIDATION-PLAN.json")
REPORT=ROOT/"APP-POLICY-MERGE-REPORT.md"
DOMAIN_TYPES={"DOMAIN","DOMAIN-SUFFIX","HOST","HOST-SUFFIX"}
IP_TYPES={"IP-CIDR","IP-CIDR6"}
SUFFIXES=(("_All_No_Resolve","all_no_resolve"),("_No_IPv6_Resolve","no_ipv6_resolve"),("_NoIPv6_Resolve","no_ipv6_resolve"),("_All_NoResolve","all_no_resolve"),("_No_Resolve","no_resolve"),("_NoResolve","no_resolve"),("_No_IPv6","no_ipv6"),("_NoIPv6","no_ipv6"),("_Resolve","resolve"),("_Domain","domain_only"),("_All","all"))

def format_for(stem):
    for suffix,label in SUFFIXES:
        if stem.endswith(suffix):
            return stem[:-len(suffix)],label
    return stem,"standard"

def safe_path(rel, must_exist=True):
    p=Path(rel)
    if not rel or p.is_absolute() or ".." in p.parts or not rel.startswith("Rule/Upstream/"):
        raise SystemExit("Unsafe path outside Rule/Upstream: "+str(rel))
    q=Path(".")/p
    if q.is_symlink():
        raise SystemExit("Symlink is not allowed: "+str(q))
    parent=q.parent
    while parent!=Path("."):
        if parent.is_symlink():
            raise SystemExit("Symlink parent is not allowed: "+str(parent))
        parent=parent.parent
    if must_exist and not q.exists():
        raise SystemExit("Required path missing: "+str(q))
    return q

def rule_lines(path):
    out=[]
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        line=raw.strip()
        if line and not line.startswith(("#",";","//")):
            out.append(line)
    return out

def split_header_body(path):
    rows=path.read_text(encoding="utf-8-sig").splitlines()
    first=None
    for i,line in enumerate(rows):
        s=line.strip()
        if s and not s.startswith(("#",";","//")):
            first=i
            break
    if first is None:
        raise SystemExit("Empty canonical file: "+str(path))
    return rows[:first],rows[first:]

def normalize_for_format(rule,fmt):
    p=rule.split(",")
    if len(p)<2 or p[0].upper() not in IP_TYPES:
        return rule
    kind=p[0].strip()
    value=p[1].strip()
    options=[x.strip() for x in p[2:] if x.strip()]
    options=[x for x in options if x.lower()!="no-resolve"]
    if fmt=="standard":
        options.append("no-resolve")
    return ",".join([kind,value]+options)

def domain_covered(rule,target_rules):
    p=rule.split(",")
    if len(p)<2 or p[0].upper() not in DOMAIN_TYPES:
        return False
    value=p[1].strip().lower().rstrip(".")
    for target in target_rules:
        q=target.split(",")
        if len(q)<2:
            continue
        kind=q[0].strip().upper()
        domain=q[1].strip().lower().rstrip(".")
        if kind in {"DOMAIN-SUFFIX","HOST-SUFFIX"} and (value==domain or value.endswith("."+domain)):
            return True
    return False

def ip_covered(rule,target_rules):
    p=rule.split(",")
    if len(p)<2 or p[0].upper() not in IP_TYPES:
        return False
    try:
        source=ipaddress.ip_network(p[1].strip(),strict=False)
    except ValueError:
        return False
    for target in target_rules:
        q=target.split(",")
        if len(q)<2 or q[0].strip().upper() not in IP_TYPES:
            continue
        try:
            net=ipaddress.ip_network(q[1].strip(),strict=False)
            if net.version==source.version and source.subnet_of(net):
                return True
        except ValueError:
            continue
    return False

def covered(rule,target_rules):
    lower=rule.lower()
    if any(x.lower()==lower for x in target_rules):
        return True
    return domain_covered(rule,target_rules) or ip_covered(rule,target_rules)

def write_canonical(path,app,body_lines):
    header,old_body=split_header_body(path)
    old_rules=rule_lines(path)
    # Preserve original comments/body; append only new rules in source order.
    merged=list(dict.fromkeys(old_rules+body_lines))
    clean=[]
    for line in header:
        s=line.strip()
        if not s:
            continue
        if re.match(r"^# [A-Z0-9_-]+:\s*\d+\s*$",s):
            continue
        if s.startswith(("# CANONICAL-RULESET:","# MERGED-ALIASES:","# APP-POLICY-GROUP:")):
            continue
        clean.append(line)
    clean.append("# APP-POLICY-GROUP: "+app)
    counts=Counter(x.split(",",1)[0].strip().upper() for x in merged)
    for kind in sorted(counts):
        clean.append(f"# {kind}: {counts[kind]}")
    clean.append(f"# TOTAL: {len(merged)}")
    # Retain existing body comments, but avoid retaining rule rows twice.
    comments=[x for x in old_body if not (x.strip() and not x.strip().startswith(("#",";","//")))]
    content="\n".join(clean)+"\n\n"+"\n".join(merged)
    if comments:
        content+="\n"+"\n".join(comments)
    path.write_text(content.rstrip()+"\n",encoding="utf-8")
    return len(merged),len(merged)-len(old_rules)

def archive_non_rule_files(alias_path,alias_rel):
    archive=ROOT/"SourceMetadata"/"RegionalVariants"
    archived=[]
    safe_name=alias_rel.replace("/","__")
    for f in sorted(alias_path.rglob("*")):
        if f.is_symlink():
            raise SystemExit("Symlink in alias folder: "+str(f))
        if not f.is_file() or f.suffix.lower()==".list":
            continue
        rel=f.relative_to(alias_path).as_posix().replace("/","__")
        dest=archive/(safe_name+"--"+rel)
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(f,dest)
        archived.append(str(dest.relative_to(ROOT)))
    return archived

def main():
    if not PLAN.is_file() or PLAN.is_symlink():
        raise SystemExit("Consolidation plan missing or unsafe")
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    groups=plan.get("app_policy_groups",[])
    if not isinstance(groups,list) or not groups:
        raise SystemExit("No app_policy_groups in consolidation plan")

    report=[
        "# App policy-group consolidation report","",
        "One App now maps to one folder. Country/region selection remains in the Surge policy group. Distinct rule formats are preserved.","",
        "| App | Alias folders removed | Rule files removed | New rules added to canonical files | Final formats |",
        "|---|---:|---:|---:|---|",
    ]
    total_alias_folders=0
    total_list_files_removed=0
    total_added_file_rules=0
    total_unique_added=set()
    completed=[]

    for group in groups:
        app=group["app"]
        canonical_rel=group["canonical_folder"]
        aliases=group.get("alias_folders",[])
        canonical_dir=safe_path("Rule/Upstream/"+canonical_rel)
        if not canonical_dir.is_dir():
            raise SystemExit("Canonical App folder missing: "+canonical_rel)

        canonical_files={}
        for f in sorted(canonical_dir.rglob("*.list")):
            if f.is_symlink():
                raise SystemExit("Symlink canonical list: "+str(f))
            _,fmt=format_for(f.stem)
            if fmt in canonical_files:
                raise SystemExit("Multiple canonical files of the same format in "+canonical_rel+": "+fmt)
            canonical_files[fmt]=f
        if not canonical_files:
            raise SystemExit("No canonical .list files in "+canonical_rel)

        added_by_format=Counter()
        alias_rule_count=0
        alias_file_count=0
        archived=[]
        alias_folders_removed=0
        alias_files_removed=0

        for alias_rel in aliases:
            alias_dir=safe_path("Rule/Upstream/"+alias_rel,must_exist=False)
            if not alias_dir.exists():
                continue
            if not alias_dir.is_dir():
                raise SystemExit("Alias path is not a folder: "+alias_rel)
            alias_lists=sorted(alias_dir.rglob("*.list"))
            if any(x.is_symlink() for x in alias_dir.rglob("*")):
                raise SystemExit("Symlink in alias folder: "+alias_rel)
            if not alias_lists:
                raise SystemExit("Alias folder has no .list files; refusing silent deletion: "+alias_rel)

            for source in alias_lists:
                _,source_fmt=format_for(source.stem)
                source_rules=rule_lines(source)
                alias_rule_count+=len(source_rules)
                alias_file_count+=1

                if source_fmt in {"standard","resolve"}:
                    targets=[(fmt,path) for fmt,path in canonical_files.items() if fmt in {"standard","resolve"}]
                    if not targets:
                        targets=[(source_fmt,canonical_files.get(source_fmt))]
                else:
                    targets=[(source_fmt,canonical_files.get(source_fmt))]
                targets=[x for x in targets if x[1] is not None]
                if not targets:
                    raise SystemExit("No canonical target format for "+str(source.relative_to(ROOT))+" ("+source_fmt+")")

                for target_fmt,target_path in targets:
                    current=rule_lines(target_path)
                    additions=[]
                    for rule in source_rules:
                        normalized=normalize_for_format(rule,target_fmt)
                        if not covered(normalized,current+additions):
                            additions.append(normalized)
                    if additions:
                        write_canonical(target_path,app,additions)
                        added_by_format[target_fmt]+=len(additions)
                        total_added_file_rules+=len(additions)
                        for x in additions:
                            # Count unique app-level rules once, even when mirrored into Standard and Resolve.
                            total_unique_added.add((canonical_rel,x.split(",",1)[0].upper(),x.split(",",2)[1].lower() if len(x.split(","))>1 else x))

                # Verify all source rules are covered by every canonical format that applies.
                for target_fmt,target_path in targets:
                    current=rule_lines(target_path)
                    for rule in source_rules:
                        normalized=normalize_for_format(rule,target_fmt)
                        if not covered(normalized,current):
                            raise SystemExit("Alias rule not covered after merge: "+str(source.relative_to(ROOT))+": "+rule+" -> "+str(target_path))

            archived.extend(archive_non_rule_files(alias_dir,alias_rel))
            shutil.rmtree(alias_dir)
            alias_folders_removed+=1
            alias_files_removed+=len(alias_lists)

        # Canonical headers and README make the single-App grouping explicit.
        final_formats=sorted(canonical_files)
        readme=canonical_dir/"README.md"
        existing=readme.read_text(encoding="utf-8-sig") if readme.is_file() else "# "+app+"\n"
        marker="## App policy group"
        if marker not in existing:
            existing=existing.rstrip()+"\n\n"+marker+"\n\n"
            existing+="This folder is the single Surge rule folder for "+app+". Select the country/region in the App's Surge policy group; regional variants are not separate rule folders.\n\n"
            if aliases:
                existing+="Consolidated regional/alternate folders: "+", ".join(aliases)+".\n\n"
            existing+="Retained formats: "+", ".join(final_formats)+".\n"
            readme.write_text(existing,encoding="utf-8")

        total_alias_folders+=alias_folders_removed
        total_list_files_removed+=alias_files_removed
        completed.append({
            "app":app,"canonical_folder":canonical_rel,"aliases_removed":alias_folders_removed,
            "list_files_removed":alias_files_removed,"alias_rule_occurrences":alias_rule_count,
            "added_by_format":dict(added_by_format),"formats":final_formats,"archived_source_files":archived,
        })
        report.append(
            f"| {app} | {alias_folders_removed} | {alias_files_removed} | {sum(added_by_format.values())} | {', '.join(final_formats)} |"
        )
        report += ["",f"## {app}",f"- Canonical folder: {canonical_rel}",
                  f"- Alias folders removed: {alias_folders_removed}; .list files removed: {alias_files_removed}",
                  f"- Alias rule occurrences checked: {alias_rule_count}",
                  f"- New rules added by format: {dict(added_by_format)}",
                  f"- Source README/license files archived: {len(archived)}"]

    report += [
        "",
        "## Summary",
        f"- App groups processed: {len(completed)}",
        f"- Alias folders removed: {total_alias_folders}",
        f"- Alias .list files removed: {total_list_files_removed}",
        f"- New rule lines added across files/formats: {total_added_file_rules}",
        f"- Unique new App-level rules added (counting Standard/Resolve mirrors once): {len(total_unique_added)}",
        "",
        "## Preserved boundaries",
        "- Personal rules were not read or modified.",
        "- No dedicated bank/payment App folders were found in the current Upstream inventory; payment-related domains in other Apps were not deleted.",
        "- Standard and Resolve remain separate files; regional variants are folded into the same App folder.",
        "- Source README/license material from removed alias folders is archived under SourceMetadata/RegionalVariants.",
        "- No new author rule sets were fetched.",
        "",
    ]
    REPORT.write_text("\n".join(report)+"\n",encoding="utf-8")
    print(json.dumps({"groups":len(completed),"alias_folders_removed":total_alias_folders,"list_files_removed":total_list_files_removed,"new_rule_lines_across_formats":total_added_file_rules,"unique_app_rules_added":len(total_unique_added)},ensure_ascii=False))

if __name__=="__main__":
    main()
