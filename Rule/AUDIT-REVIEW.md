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

Important interpretation:
- Matches in advertising, privacy, or AdGuard-native lists may represent tracking, telemetry, email, or measurement endpoints; they do not by themselves prove that payment or checkout traffic is blocked.
- Broad service rules such as `alipay.com`, `unionpay.com`, `paypal.com`, `visa.com`, and `stripe.com` need to be interpreted in the context of their category and the user's policy. They were not deleted or rewritten automatically.
- Keep the PayPay personal rule separate from upstream blocklists. Do not remove it as an audit cleanup.

## Identical-content candidates

The audit reports 8 groups:
- 3 same-app scenario pairs: `All` and `All_No_Resolve` variants. These are intentionally kept separate because their resolution behavior differs.
- 5 cross-category exact-content candidates. The Assassin's Creed Odyssey and Origins rule bodies, and the PChome/PChomeTW rule bodies, were checked and are identical in the paired paths (rule payloads match; metadata timestamps can differ).

No cross-category file was deleted. Keeping both paths avoids silently breaking any existing raw-file subscription URL. Consolidation to one canonical subscription path requires a separate compatibility/redirect plan.

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

## OpenPhish shared-hosting review (2026-11-27)

The current cleanup inventory contains 61 rule-to-feed match rows. These collapse to 12 distinct matched hostnames and 12 distinct suffix rules; repeated rows come from the same rule being present in Standard/Resolve variants or aggregate lists. They are not 61 independent malicious parent domains.

| Suffix rule | Matched host example | Match rows | Current rule context |
|---|---|---:|---|
| `blogspot.com` | `www.infoundianshopee98.blogspot.com` | 4 | Google, Global |
| `cloudfront.net` | `d33wubrfki0l68.cloudfront.net` | 10 | Amazon, Global, GlobalMedia, Proxy, ProxyLite |
| `duckdns.org` | `www.yeninesilhizli.duckdns.org` | 6 | NaSDDNS, Global, Proxy |
| `eu.org` | `five.seafn.eu.org` | 2 | Global |
| `gitbook.io` | `robinhxnoodlogin.gitbook.io` | 5 | GitBook, Global, Proxy |
| `github.io` | `sugosh1.github.io` | 3 | GitHub, Global |
| `is.gd` | `is.gd` | 6 | Global, Proxy, ProxyLite |
| `netlify.app` | `netflis-gpt.netlify.app` | 4 | Global, Proxy |
| `pages.dev` | `5ywlo-sem-pief-p3s1m-21-10-2026-aa.pages.dev` | 6 | Cloudflare, Global, Proxy |
| `vercel.app` | `www.netflix-clone-rust-zeta.vercel.app` | 5 | Vercel, Global, Proxy |
| `web.app` | `netflix-bobby.web.app` | 4 | Google, Global |
| `workers.dev` | `huqxs-hqbv-6r1l.467908b25f25758e1432524e.workers.dev` | 6 | Cloudflare, Global, Proxy |

### App-specific shared-hosting scope

Eight shared-platform suffixes appear in six brand-named App rule sets:

- Amazon: `cloudfront.net` (Standard and Resolve).
- Cloudflare: `pages.dev` and `workers.dev` (Standard and Resolve).
- GitBook: `gitbook.io`.
- GitHub: `github.io`.
- Vercel: `vercel.app`.
- Google: `blogspot.com` and `web.app` (Standard and Resolve).

These are platform-owned namespaces, but they are shared across many customer projects or tenants. An OpenPhish match on one tenant hostname does not prove that the parent suffix is malicious or that the parent rule should be deleted. At the same time, retaining a broad suffix in an App-specific policy group can route unrelated tenants through that App's selected country/region.

### Disposition

- No parent suffix was deleted or rewritten. The current evidence confirms multi-tenant scope, but does not establish the user's desired routing for every tenant; keep the existing rules pending an explicit policy decision rather than silently changing App routing.
- The exact matched hostnames remain audit evidence only; they were not added to an App routing list or a block list.
- The other shared/utility suffixes (`duckdns.org`, `eu.org`, `is.gd`, and `netlify.app`) occur in DDNS, Global, Proxy, or ProxyLite contexts rather than a brand-named App folder; retain their current scenario separation.
- URLhaus contributed no domains because its authenticated hostfile was unavailable without the repository secret `URLHAUS_AUTH_KEY`. This pass therefore used 278 OpenPhish domains only and is not a complete multi-feed reputation check.
- No App rule file, scenario format, personal rule, or cached author-source file was modified during this manual review.
