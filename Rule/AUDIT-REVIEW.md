# Surge manual review notes

Generated: 2026-11-27
Repository: AllanRita/Surge

## Scope

This file records manual interpretation of the static audit. It does not replace a live Surge subscription import or device-level traffic test. No subscription files or personal rules were deleted or rewritten during this review.

## Single-label suffix audit

- Historical manual snapshot: 912 broad-domain rows and 79 distinct single-label suffix values.
- Historical IANA check: `2026112503` (updated 2026-11-26 UTC) found 78 delegated values covering 895 rows; `xihuan` was absent from the root-zone list and was previously reported in 17 rows.
- Current generated cleanup inventory: 894 single-label suffix occurrences; it records no `stale_or_private_root_suffix` finding.
- The latest cleanup workflow completed successfully. Its IANA-gated remediation script reports 0 `DOMAIN-SUFFIX,xihuan` occurrences removed and no files changed. Therefore, the historical 17-row `xihuan` count is not current; the exact rule was already absent when that remediation pass ran.
- The historical 912-row broad-domain metric and the current 894-row single-label metric come from different snapshots/labels and should not be compared as if they were the same counter.

Interpretation:
- A one-label suffix is not automatically malformed. Many are real delegated TLDs, including brand TLDs and IDN/punycode TLDs.
- These rules can still be broad in scope: for example, `DOMAIN-SUFFIX,cn` matches the entire `.cn` namespace. Whether that is correct depends on the intended scenario and policy.
- No remaining single-label suffix was automatically removed in the latest cleanup pass. Keep the remaining rules pending scenario-aware review rather than deleting them based on shape alone.

## Financial-domain audit

- 238 upstream financial-domain review matches.
- 1 personal financial-rule match in `Rule/Personal/PayPay.list`.
- 29 distinct domain values across the report.
- The personal PayPay file remains unchanged.

### Location of the 238 upstream financial-domain matches

| Rule folder | Matched lines |
|---|---:|
| AdvertisingTest | 63 |
| Advertising | 57 |
| AdGuardSDNSFilter | 36 |
| EasyPrivacy | 18 |
| AdvertisingLite | 9 |
| Global | 9 |
| Privacy | 9 |
| China | 6 |
| ChinaMax | 6 |
| ChinaNoMedia | 6 |
| ChinaTest | 6 |
| Alibaba | 3 |
| ChinaMaxNoIP | 3 |
| ChinaMaxNoMedia | 3 |
| Copilot | 2 |
| OpenAI | 2 |
| **Total** | **238** |

Most matches are in advertising, privacy, or filter-category lists; the remainder are in aggregate or other App lists. A domain-name match does not by itself prove that a payment/checkout endpoint is being blocked. The current inventory finds zero dedicated bank/payment App folders, and the 14 dedicated folders removed earlier remain absent. These 238 upstream domain entries were not deleted. The single personal PayPay match was also left untouched.


Important interpretation:
- Matches in advertising, privacy, or AdGuard-native lists may represent tracking, telemetry, email, or measurement endpoints; they do not by themselves prove that payment or checkout traffic is blocked.
- Broad service rules such as `alipay.com`, `unionpay.com`, `paypal.com`, `visa.com`, and `stripe.com` need to be interpreted in the context of their category and the user's policy. They were not deleted or rewritten automatically.
- Keep the PayPay personal rule separate from upstream blocklists. Do not remove it as an audit cleanup.

## Duplicate and App-folder consolidation (current status)

The earlier preliminary duplicate-candidate report has been superseded by the completed App-folder consolidation and the latest generated inventory.

- The approved consolidation processed 14 App groups.
- 19 alias folders and 25 alias `.list` files were removed after comparing and merging their rule bodies.
- 73 rule entries were added across canonical files/formats; these represent 39 unique App-level additions after counting Standard/Resolve mirrors once.
- All 14 canonical folders exist in the current `main` tree, and all 19 alias folders are absent.
- The current inventory reports 2 byte-identical file groups and 3 identical rule-payload groups. These are the intended `All` / `All_No_Resolve` pairs in AdGuardSDNSFilter, ChinaMaxNoIP, and EasyPrivacy. They remain separate because the format/resolution intent is distinct.
- The current plan records 18 cross-App overlap boundaries as keep-separate. DuoWan/HuanJu were manually checked: HuanJu's 20 domain rules are all contained in DuoWan's 27 rules, with 7 additional DuoWan rules; their READMEs describe distinct named rule scopes, so they remain separate.
- AmazonIP and ClubhouseIP also remain separate from their similarly named App folders. AmazonIP is a broad 1,521-entry IP-CIDR inventory; ClubhouseIP's README explicitly specifies direct routing while Clubhouse's domain rules are proxied.

### Subscription path compatibility

The 19 old alias folders were physically removed after the canonical union was verified. GitHub raw URLs do not redirect from removed paths. No active Surge `.conf` profile is stored in this repository, so external subscription references cannot be checked here. If an external profile still uses an old alias URL, it must be changed to the canonical folder/file path listed in `Rule/CONSOLIDATED-INDEX.md`.

## Additional author source: Aoang/Surge

- Repository reviewed: https://github.com/Aoang/Surge
- License: MIT; source license is retained as `Rule/Upstream/LICENSE-MIT-AOANG`.
- Imported source files: 9, with commit and source-path provenance recorded in `Rule/Upstream/SourceMetadata/Aoang-*.json`.
- Apple: 69 unique domain rules reviewed; 61 were already covered by existing exact rules or broader suffix rules, and 8 additional domain rules were appended to the existing Apple list.
- Microsoft OneDrive and Teams: 8 domain rules reviewed; all were already covered by the existing Microsoft rule set, so no duplicate entries were added.
- Separate scenario lists retained: DNS blocking, YouTube URL-regex ad blocking, Parallels blocking, other blocking, process routing, and unavailable-service handling.
- PayPal source rules were deliberately excluded from automatic import pending financial-policy review.
- Existing SukkaLab supplements are preserved; Aoang additions are appended as a separately attributed supplement.

## Current validation limits

- The latest workflow run validates and publishes a static snapshot and audit artifact.
- It does not prove live DNS resolution, actual routing decisions, payment completion, or real-device Surge subscription behavior.
- Device-level regression must verify the intended policy for Alipay, UnionPay, PayPal, Visa, Stripe, and PayPay before any payment-related rule is changed.

## Safety decision

No broad-domain or financial-domain rule was automatically deleted. Keep potentially useful rules pending scenario-aware and live behavior verification.

## OpenPhish shared-hosting review (2026-11-27; refreshed feed snapshot)

The refreshed OpenPhish comparison contains **77 rule-to-feed match rows**, representing **15 distinct matched hostnames under 15 suffix rules**. Repeated rows come from the same suffix appearing in Standard/Resolve variants or aggregate lists; they are not 77 independent malicious parent domains. All 77 matches are classified as app/routing scope.

| Suffix rule | Matched host example | Match rows | Rule folders |
|---|---|---:|---|
| `amazonaws.com` | `n8turz.s3.us-east-1.amazonaws.com` | 10 | Amazon, Global, GlobalMedia, Proxy, ProxyLite |
| `cloudfront.net` | `d1by761p31t71v.cloudfront.net` | 10 | Amazon, Global, GlobalMedia, Proxy, ProxyLite |
| `pages.dev` | `brige-traezor-io.pages.dev` | 6 | Cloudflare, Global, Proxy |
| `trycloudflare.com` | `drainage-possess-unavailable-focal.trycloudflare.com` | 4 | Cloudflare, Global |
| `workers.dev` | `substantiating-proof-f2d1.63186834.workers.dev` | 6 | Cloudflare, Global, Proxy |
| `gitbook.io` | `matumasklogie.gitbook.io` | 5 | GitBook, Global, Proxy |
| `github.io` | `wargreymon9.github.io` | 3 | GitHub, Global |
| `azurefd.net` | `35ctt56wc6hcja27hkpd-d4g3a2apa2g2ergs.z03.azurefd.net` | 3 | Global, Microsoft |
| `blogspot.com` | `rejekishopee23.blogspot.com` | 4 | Google, Global |
| `eu.org` | `wisayq9065.embih.eu.org` | 2 | Global |
| `azurewebsites.net` | `forrit-tb-csmr-prod-dev-02.azurewebsites.net` | 5 | Global, Microsoft, Proxy |
| `duckdns.org` | `hizliyapiyoruzherseyi.duckdns.org` | 6 | NaSDDNS, Global, Proxy |
| `netlify.app` | `boisterous-sprite-d1fe49.netlify.app` | 4 | Global, Proxy |
| `vercel.app` | `www.vakifbank.vercel.app` | 5 | Global, Proxy, Vercel |
| `weebly.com` | `www.xhdfh7hfnrrjjjff.weebly.com` | 4 | Global, Proxy |

### App-specific shared-platform scope

The refreshed matches place broad shared-platform suffixes in these named App folders:

- Amazon: `amazonaws.com` and `cloudfront.net`.
- Cloudflare: `pages.dev`, `trycloudflare.com`, and `workers.dev`.
- GitBook: `gitbook.io`.
- GitHub: `github.io`.
- Microsoft: `azurefd.net` and `azurewebsites.net`.
- Google: `blogspot.com`.
- Vercel: `vercel.app`.

These are multi-tenant cloud, hosting, CDN, or temporary-tunnel namespaces. A phishing hostname under one tenant does not prove the parent suffix is malicious, but a broad suffix in an App policy group can route unrelated tenants through that App's selected country/region.

### Disposition

- No parent suffix was deleted or rewritten. The rules remain pending scenario-aware routing review; no change is made solely from a feed match.
- Exact matched hostnames remain audit evidence only and were not added to App routing or block lists.
- The refreshed scan adds `amazonaws.com`, `trycloudflare.com`, `azurefd.net`, `azurewebsites.net`, and `weebly.com` to the known shared-platform review set.
- URLhaus remains unavailable in this run because the repository secret `URLHAUS_AUTH_KEY` is not configured. The feed status is **not loaded**, not clean.
- No new author rule sets were fetched, and no rule files were modified by this manual review.
