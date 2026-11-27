# Surge App rule-set structure

Updated: 2026-11-27

## Final architecture

**One App = one rule-set folder = one Surge policy group.**

The App rule set identifies all domains and other matching rules used by that App. The country/region is selected in the App's Surge policy group, not by maintaining separate USA/Japan/Hong Kong folders.

## Consolidation rules

1. Merge regional variants of the same App into its canonical App folder.
2. Compare the rule bodies from every already-cached author source before merging; add missing rules only after checking their semantics and safety.
3. Keep distinct file formats separately. For example, standard and Resolve are different formats; keep one completed file for each format.
4. Do not merge different Apps because they share a CDN, parent company, login provider, or cloud platform.
5. Preserve provenance and source licenses under SourceMetadata; do not fetch new author rule sets during this cleanup.
6. Do not delete payment-related domains from unrelated App lists.
7. Do not modify Rule/Personal.

## Approved App-folder consolidation

| Canonical App folder | Regional / alternate folders to consolidate | Rule handling |
|---|---|---|
| Abema | AbemaTV | Same payload; one folder |
| Gemini | BardAI | Same payload; one folder |
| PChome | PChomeTW | Same payload; one folder |
| GlobalScholar | Scholar | Same payload family; keep the union |
| BiliBili | BiliBiliIntl | Add the international process name to standard and Resolve |
| iQIYI | iQIYIIntl | Add missing international IP ranges/process names to both formats |
| Hulu | HuluUSA, HuluJP | Existing Hulu list already covers the regional sets |
| Telegram | TelegramNL, TelegramSG, TelegramUS | Regional IP ranges already covered by Telegram's broad ranges |
| Amazon | AmazonCN | Add 17 additional China-region rules to standard and Resolve |
| HBO | HBOAsia, HBOHK, HBOUSA | Add five additional regional rules |
| Cloudflare | Cloudflarecn | Existing Cloudflare list covers the regional set |
| Steam | SteamCN | Add five China CDN/service rules to standard and Resolve |
| Assassin's Creed Odyssey | Game/Assassin'sCreed-Odyssey | Remove duplicate category copy; retain standard and Resolve |
| Assassin's Creed Origins | Game/Assassin'sCreed-Origins | Remove duplicate category copy; retain standard and Resolve |

## Bank and payment App folders

The current inventory found no dedicated bank/payment App folders under Rule/Upstream. Therefore, no such folder needs deletion at this stage.

- Keep payment-related domains that are part of other App rule sets.
- Keep Rule/Personal/PayPay.list unchanged.
- The current inventory also flags six other finance/trading/crypto folders for review only: Binance (12 entries), Crypto (201), Cryptocurrency (43), EastMoney (33), OKX (3), and TigerFintech (19). They are not classified as dedicated bank/payment App folders and were not removed.
- Future bank/payment domains belong in the user's personal rule set, not in the shared App library.
- Separate classification note: the current audit flags Binance and OKX as crypto-exchange rule folders, EastMoney and TigerFintech as securities/investment rule folders, and Crypto/Cryptocurrency as category lists. These six are review-only; they are not automatically treated as bank/payment Apps and have not been deleted.

## File formats

Keep each distinct existing format once within its App folder. Standard and Resolve files remain separate; other explicit variants such as All, All_No_Resolve, Domain-only, and No-IPv6 are not collapsed merely because they currently contain identical rules.

## Current source comparison

The 15 author-source snapshots already cached in SourceMetadata have been compared against their correctly mapped App/category rule files: 300 source-rule entries checked, zero uncovered. Scope limitation: this verifies only the snapshots already cached; it does not establish that every App has been compared against every possible author. No new author rule sets were fetched.

## Security and review records

- The current plan records 19 cross-App overlap pairs as keep-separate/manual-review boundaries. Similarity alone never authorizes a merge.
- SECURITY-REVIEW.md records the current threat-feed matches and broad shared-hosting suffixes. Feed matches are review signals only; no shared-hosting parent suffix is automatically removed.
- SECURITY-REMEDIATION-REPORT.md records the latest IANA-gated check for `DOMAIN-SUFFIX,xihuan`: zero matching occurrences were found, so no rule files were changed. The earlier 17-occurrence figure is historical and is not the current repository state.
- The latest OpenPhish comparison found 77 rule-to-feed matches (all classified as app/routing scope) under shared hosting/CDN suffixes; these are review flags, not proof that the parent domains are malicious. URLhaus's old keyless hostfile endpoint is retired; authenticated checks run only when the GitHub Actions secret URLHAUS_AUTH_KEY is configured. Without it, URLhaus is explicitly marked as not loaded, not clean.

## Current audit scope

- 828 upstream .list files across 663 App/category folders.
- 15 cached author-source snapshots compared; zero uncovered source rules.
- Three personal rule files are kept outside the automated upstream audit/remediation scope.
- New author rule-set fetching remains paused. Public threat-intelligence reference feeds may still be used for static review.

See:
- CLEANUP-INVENTORY.md for the file inventory, cached-source coverage, static syntax checks, and feed-match summary.
- SECURITY-REVIEW.md for the detailed threat-feed and shared-hosting review.
- SECURITY-REMEDIATION-REPORT.md for the exact rule removed and why.
- APP-POLICY-MERGE-REPORT.md for the completed folder consolidation and rule additions.


## Post-consolidation verification and subscription migration

The current `main` tree was checked against the consolidation plan:

- All 14 canonical App folders exist.
- All 19 approved alias folders are absent.
- The merge report records 25 alias `.list` files removed, 73 rule entries added across formats, and 39 unique App-level additions.
- The 15 cached author-source snapshots cover 300 source rules with zero uncovered rules.
- The current inventory contains 828 upstream `.list` files across 663 App/category folders.
- The 14 dedicated bank/payment App folders removed earlier remain absent. The three files in `Rule/Personal` remain separate and unchanged.

### Old folder path to canonical folder

GitHub raw-content URLs do not automatically redirect after a folder is removed. If an external Surge profile still subscribes to an old alias path, update it to the canonical folder and select the canonical file for the same format.

| Removed alias folder | Canonical folder |
|---|---|
| `Rule/Upstream/AbemaTV/` | `Rule/Upstream/Abema/` |
| `Rule/Upstream/BardAI/` | `Rule/Upstream/Gemini/` |
| `Rule/Upstream/PChomeTW/` | `Rule/Upstream/PChome/` |
| `Rule/Upstream/Scholar/` | `Rule/Upstream/GlobalScholar/` |
| `Rule/Upstream/BiliBiliIntl/` | `Rule/Upstream/BiliBili/` |
| `Rule/Upstream/iQIYIIntl/` | `Rule/Upstream/iQIYI/` |
| `Rule/Upstream/HuluUSA/` | `Rule/Upstream/Hulu/` |
| `Rule/Upstream/HuluJP/` | `Rule/Upstream/Hulu/` |
| `Rule/Upstream/TelegramNL/` | `Rule/Upstream/Telegram/` |
| `Rule/Upstream/TelegramSG/` | `Rule/Upstream/Telegram/` |
| `Rule/Upstream/TelegramUS/` | `Rule/Upstream/Telegram/` |
| `Rule/Upstream/AmazonCN/` | `Rule/Upstream/Amazon/` |
| `Rule/Upstream/HBOAsia/` | `Rule/Upstream/HBO/` |
| `Rule/Upstream/HBOHK/` | `Rule/Upstream/HBO/` |
| `Rule/Upstream/HBOUSA/` | `Rule/Upstream/HBO/` |
| `Rule/Upstream/Cloudflarecn/` | `Rule/Upstream/Cloudflare/` |
| `Rule/Upstream/SteamCN/` | `Rule/Upstream/Steam/` |
| `Rule/Upstream/Game/Assassin'sCreed-Odyssey/` | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/` |
| `Rule/Upstream/Game/Assassin'sCreed-Origins/` | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/` |

The repository does not contain the user's active Surge profile/configuration, so external subscription references and device-level refresh cannot be verified here. The migration map is provided to avoid silently assuming that old raw URLs still work.

### Separate scope folders — intentionally not merged

- `AmazonIP` remains separate from `Amazon`: it is a 1,521-entry IP-CIDR inventory, not an Amazon retail App-only domain list.
- `ClubhouseIP` remains separate from `Clubhouse`: its README specifies direct routing for the IP list and proxy routing for the Clubhouse domain list.
- `DuoWan` and `HuanJu` remain separate. HuanJu's 20 rules are a subset of DuoWan's 27, but their READMEs describe distinct rule scopes; overlap alone is not sufficient reason to merge them.
- The 19 cross-App overlap boundaries remain separate. Shared CDN, parent-company, login, or analytics domains do not establish that two folders represent one App.


## Expanded shared-hosting audit

The cleanup inventory now scans a curated set of 42 shared CDN/hosting, dynamic-DNS, and URL-shortener suffixes across every upstream rule file, not only those suffixes that happen to match OpenPhish. The latest run found 34 suffixes in 159 rule occurrences: 33 occurrences in App/service folders across 21 suffixes and 126 in aggregate folders (Global, GlobalMedia, Proxy, ProxyLite). The result is recorded in `CLEANUP-INVENTORY.json` and `CLEANUP-INVENTORY.md`, with the affected folders and rule occurrences. This is a review-only scan: no rule is automatically removed because a suffix is shared or multi-tenant. The plan records these App/service-folder candidates for manual routing review.
