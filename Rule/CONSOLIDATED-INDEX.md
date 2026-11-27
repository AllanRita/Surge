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
- Future bank/payment domains belong in the user's personal rule set, not in the shared App library.

## File formats

Keep each distinct existing format once within its App folder. Standard and Resolve files remain separate; other explicit variants such as All, All_No_Resolve, Domain-only, and No-IPv6 are not collapsed merely because they currently contain identical rules.

## Current source comparison

The 15 author-source snapshots already cached in SourceMetadata have been compared against their correctly mapped App/category rule files. The current audit reports zero uncovered source rules. No new author rule sets were fetched.

See:
- CLEANUP-INVENTORY.md for the file inventory, cached-source coverage, static syntax checks, and OpenPhish review matches.
- APP-POLICY-MERGE-REPORT.md for the completed folder consolidation and rule additions.
