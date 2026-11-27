# Security remediation report

## Removed rule
- Rule: DOMAIN-SUFFIX,xihuan
- Reason: xihuan is not present in the IANA root-zone TLD list. This public root-suffix rule cannot match a normal public DNS suffix; it was repeated in ChinaMax-family variants.
- Occurrences removed: 17
- Files changed:
  - ChinaMax/ChinaMax.list
  - ChinaMax/ChinaMax_All.list
  - ChinaMax/ChinaMax_All_No_Resolve.list
  - ChinaMax/ChinaMax_No_IPv6.list
  - ChinaMax/ChinaMax_No_IPv6_Resolve.list
  - ChinaMax/ChinaMax_Resolve.list
  - ChinaMaxNoIP/ChinaMaxNoIP.list
  - ChinaMaxNoIP/ChinaMaxNoIP_All.list
  - ChinaMaxNoIP/ChinaMaxNoIP_All_No_Resolve.list
  - ChinaMaxNoMedia/ChinaMaxNoMedia.list
  - ChinaMaxNoMedia/ChinaMaxNoMedia_All.list
  - ChinaMaxNoMedia/ChinaMaxNoMedia_All_No_Resolve.list
  - ChinaMaxNoMedia/ChinaMaxNoMedia_Resolve.list
  - ChinaTest/ChinaTest.list
  - ChinaTest/ChinaTest_All.list
  - ChinaTest/ChinaTest_All_No_Resolve.list
  - ChinaTest/ChinaTest_Resolve.list

## Safety boundaries
- Only the exact DOMAIN-SUFFIX,xihuan rule was removed.
- No other domain, App folder, file format, cached source metadata, or personal rule was changed by this remediation.
- Other single-label suffixes were retained; their IANA/private status requires separate review.
