# Shared-domain review — read-only working report

Status: IN PROGRESS  
Started: 2026-11-28  
Authority: explicit user instruction to begin shared-domain review  
Mutation policy: READ ONLY. No rule may be deleted, rewritten, narrowed, moved, or merged without explicit user approval.

## 1. User's current rule-set policy

- The existing rule-set collection is considered sufficient.
- Future upstream work is update-only: fetch updates for existing rule sets and existing source mappings only.
- Do not add new authors, new App rule-set folders, new source mappings, or broaden collection scope.
- Preserve exact user-deletion tombstones. Never restore explicitly deleted content.
- Do not modify Rule/Personal.
- Preserve all existing bank, payment, and financial App rule sets.

## 2. Review scope and baseline

The latest available full-library inventory in the repository is dated 2026-11-27 13:46 UTC. Its shared-hosting scan checked 42 curated suffixes against the upstream rule library and found 34 suffixes in 159 rule occurrences. The report records 21 suffixes in App/service folders (33 occurrences) and 126 occurrences in aggregate folders Global, GlobalMedia, Proxy, and ProxyLite.

This is a historical baseline, not a claim that a new 2026-11-28 full scan has completed. The current review must refresh the inventory against the current main tree before making final per-rule recommendations. The repository's read-only inventory workflow can generate this report, but the connected GitHub action interface currently available to this task does not expose workflow_dispatch; do not claim a new run until a run ID exists.

## 3. Classification framework

Every occurrence will be reviewed in its actual routing context, not by suffix alone:

1. App/service-specific: appears in the matching provider's App folder (for example, Cloudflare in Cloudflare, GitHub in GitHub, Microsoft in Microsoft).
2. Aggregate routing: appears in Global, GlobalMedia, Proxy, or ProxyLite. These are separate policy scopes and must not be merged with App-specific rules.
3. Shared infrastructure: multi-tenant cloud, CDN, app hosting, edge functions, or temporary tunnel.
4. Dynamic DNS / user-hosted namespace.
5. URL shortener / redirect platform.
6. Cross-App overlap: same parent suffix appears under more than one App; determine whether it is intentional shared infrastructure or an accidental broad inclusion.
7. Evidence insufficient: preserve unchanged and list the exact missing evidence.

## 4. Initial inventory baseline

### Cloud/CDN/shared infrastructure
- amazonaws.com — 10 occurrences; Amazon plus aggregate folders
- cloudfront.net — 10; Amazon plus aggregate folders
- azureedge.net — 5; Microsoft plus aggregate folders
- azurefd.net — 3; Microsoft plus Global
- azurewebsites.net — 5; Microsoft plus Global/Proxy
- azurestaticapps.net — 2; Global only
- cloudapp.net — 3; Microsoft plus Global
- pages.dev — 6; Cloudflare plus Global/Proxy
- workers.dev — 6; Cloudflare plus Global/Proxy
- trycloudflare.com — 4; Cloudflare plus Global
- firebaseapp.com — 4; Google plus Global
- web.app — 4; Google plus Global
- appspot.com — 6; Google plus Global/Proxy

### Shared hosting / developer platforms
- blogspot.com — 4; Google plus Global
- gitbook.io — 5; GitBook plus Global/Proxy
- github.io — 3; GitHub plus Global
- gitlab.io — 7; Developer plus Global/Proxy/ProxyLite
- bitbucket.io — 2; Global
- herokuapp.com — 6; Heroku/Salesforce plus Global/Proxy
- vercel.app — 5; Vercel plus Global/Proxy
- netlify.app — 4; Global/Proxy
- weebly.com — 4; Global/Proxy
- fly.dev — 2; Global

### Dynamic DNS / delegated subdomain services
- duckdns.org — 6; NaSDDNS plus Global/Proxy
- dynu.net — 5; Dynu plus Global/Proxy
- no-ip.org — 4; Global/Proxy
- eu.org — 2; Global

### URL shorteners / redirects
- bit.ly — 6; Global/Proxy/ProxyLite
- cutt.ly — 2; Global
- is.gd — 6; Global/Proxy/ProxyLite
- linktr.ee — 4; Global/Proxy
- shorturl.at — 2; Global
- t.co — 8; Twitter plus Global/Proxy/ProxyLite
- tinyurl.com — 4; Global/Proxy

The above counts and placements are taken from the repository's 2026-11-27 SHARED-HOSTING-SCOPE-REVIEW.md baseline. They must be refreshed before final decisions.

## 5. Threat-feed correlation — interpretation only

The baseline security report recorded 77 OpenPhish parent-suffix match rows across 20 rule files, 15 suffix rules, and 41 distinct matched hostnames in one earlier feed snapshot. These are not 77 unique malicious parent domains. URLhaus was unavailable (0 hostnames loaded), and no exact-domain dual-feed confirmation was available.

A feed-listed tenant beneath a shared suffix does NOT make the parent suffix malicious. Parent-suffix matches are context for manual review only. Threat-based automatic deletion remains disabled pending a separate user decision on security-intelligence sources and thresholds.

## 6. Review priorities

Priority A — cross-scope broad suffixes:
- Identify parent suffixes that appear in both an App-specific folder and aggregate folders.
- Determine whether each App placement is required for that App's traffic or is simply inherited from a broad aggregate list.
- Preserve distinct aggregate policies (Global, GlobalMedia, Proxy, ProxyLite).

Priority B — high-impact shared namespaces:
- cloudfront.net, amazonaws.com, pages.dev, workers.dev, vercel.app, netlify.app, herokuapp.com, azurefd.net, azurewebsites.net, appspot.com, firebaseapp.com, web.app.
- Assess the possible impact of routing unrelated tenants under the same parent suffix.

Priority C — DDNS and URL shorteners:
- duckdns.org, dynu.net, no-ip.org, eu.org, bit.ly, is.gd, t.co, tinyurl.com, linktr.ee, etc.
- Determine whether the rule's presence is intentional in each aggregate policy.

## 7. Required output for each reviewed occurrence

- Exact rule and file path (including format variant)
- Folder classification (App/service or aggregate)
- Suffix provider/category
- Cross-folder occurrence count
- Evidence and source timestamp
- Expected routing impact and overbreadth risk
- Recommendation: retain / investigate / candidate to narrow / insufficient evidence
- Explicit note that no change has been made

## 8. Safety and completion criteria

- First refresh the full current inventory across all eligible rule-set folders in one run (not 100-folder validation batches).
- Produce one consolidated report with per-occurrence findings.
- Do not delete, rewrite, narrow, move, merge, or restore any rule during this review.
- Present any proposed routing-semantic changes to the user with before/after diffs and wait for explicit approval.
- Do not treat IANA delegation, a threat-feed parent match, or the presence of a provider name as proof that a suffix is malicious or unnecessary.
- Keep Rule/Personal unchanged and preserve all exact deletion tombstones.
