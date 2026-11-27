# Canonical Surge rule-set index

Updated: 2026-11-27

This index defines the one maintenance target for verified same-app rule sets. Legacy paths remain available as compatibility mirrors; they are not independent maintenance targets.

## Canonical rule sets and compatibility paths

| App / rule set | Scenario | Canonical maintenance path | Legacy compatibility path |
|---|---|---|---|
| Assassin's Creed Odyssey | Standard | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list` | `Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list` |
| Assassin's Creed Odyssey | Resolve | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list` | `Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list` |
| Assassin's Creed Origins | Standard | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list` | `Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list` |
| Assassin's Creed Origins | Resolve | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list` | `Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list` |
| PChome | Standard | `Rule/Upstream/PChomeTW/PChomeTW.list` | `Rule/Upstream/PChome/PChome.list` |
| GlobalScholar / Scholar | Standard | `Rule/Upstream/GlobalScholar/GlobalScholar.list` | `Rule/Upstream/Scholar/Scholar.list` |
| Gemini (formerly BardAI) | Standard | `Rule/Upstream/Gemini/Gemini.list` | `Rule/Upstream/BardAI/BardAI.list` |
| ABEMA (formerly AbemaTV) | Standard | `Rule/Upstream/Abema/Abema.list` | `Rule/Upstream/AbemaTV/AbemaTV.list` |

## Region and purpose variants intentionally preserved

| App | Kept separate paths | Reason |
|---|---|---|
| Hulu | Hulu, HuluUSA, HuluJP | Region-specific routing choices; the general Hulu list currently covers the regional subsets, but the USA/JP lists remain available for region-specific policies |
| HBO | HBO, HBOHK | Separate regional service scopes |
| Cloudflare | Cloudflare, Cloudflarecn | Global and China-specific service scopes |
| DNS | DNS, Block/DNS | DNS resolver routing vs HTTPDNS blocking |
| YouTube | YouTube, Block/YouTube | Service routing domains vs URL-REGEX ad-block rules |
| Direct | Direct, AdGuardSDNSFilter/Direct | General direct-routing destinations vs AdGuard SDNS filter direct-category rules |

## Merge and compatibility policy

1. Edit only the canonical path for each approved group.
2. During upstream synchronization, union exact rule lines from canonical and legacy inputs, deduplicate exact duplicate lines, and mirror the resulting rule payload to every legacy path.
3. Keep each file's own NAME/header identity, while refreshing rule-type counts from the merged payload.
4. Do not merge Standard, Resolve, No-Resolve, No-IPv6, regional, blocking, and routing scenarios into one list.
5. Similarity or shared domains alone never authorizes a merge. Parent-company relationships and shared CDN/authentication domains are not proof that two apps are the same.
6. Personal rules under `Rule/Personal/` are never included in canonical merges.
7. Never delete legacy paths until subscription migration and compatibility have been explicitly verified.

## Source identity references

- GlobalScholar README documents Scholar as a contained sub-rule: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/GlobalScholar/README.md
- Gemini README documents BardAI as a contained sub-rule: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Gemini/README.md
- ABEMA was renamed from AbemaTV in April 2020: https://av.watch.impress.co.jp/docs/series/rt/1246004.html

The machine-readable source of truth is `Rule/CONSOLIDATION-PLAN.json`.
The synchronization applies the approved groups from `.github/scripts/apply_canonical_app_merges.py`.
