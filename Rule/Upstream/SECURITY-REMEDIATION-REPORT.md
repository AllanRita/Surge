# Security remediation report

## Removed rule
- Rule: DOMAIN-SUFFIX,xihuan
- Reason: xihuan is not present in the IANA root-zone TLD list. This public root-suffix rule cannot match a normal public DNS suffix; it was repeated in ChinaMax-family variants.
- Occurrences removed: 0
- Files changed:
  - none

## Safety boundaries
- Only the exact DOMAIN-SUFFIX,xihuan rule was removed.
- No other domain, App folder, file format, cached source metadata, or personal rule was changed by this remediation.
- Other single-label suffixes were retained; their IANA/private status requires separate review.
