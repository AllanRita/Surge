# Surge Project State

Last updated: 2026-11-27 15:02 UTC
Repository: `AllanRita/Surge`
Default branch: `main`

> This file is the authoritative handoff note for future Surge work. At the start of every resumed session, read this file and the linked manifests before inspecting chat history. Do not restart completed analysis unless a source file or decision has changed.

## 1. Project priority

**Current priority: automatic Surge rule maintenance under the user-approved Workflow V1.0.** Process all eligible `Rule/Upstream` folders in sequential batches of 100 in one automatic run; only the final batch may be smaller. Use existing cached author sources only; broad new-author collection remains paused.

## 2. Confirmed target structure

- One App = one canonical rule-set folder = one Surge policy group.
- Country/region selection belongs in the Surge policy group, not in duplicate country-specific App folders.
- Merge regional/author variants only when they are the same App and their rule semantics are compatible.
- Keep different Apps separate even if they share a CDN, parent company, login provider, or cloud platform.
- Compare already-cached author snapshots; broad new-author collection remains paused. A narrowly targeted source fetch is allowed only when the user explicitly requests restoration or comparison for named folders.
- For every App, compare the available formats and complete each format independently.
- Keep one complete file per distinct format. Do not collapse Standard, Resolve, All, All_No_Resolve, Domain-only, No-IPv6, or other intentional variants merely because payloads currently overlap.
- Remove duplicates only after verifying the canonical file contains the required union and the format semantics are preserved.
- Threat-feed matches and shared-hosting suffixes are review flags, not automatic deletion instructions.

## 3. Preserve / do-not-delete rules

- There are no category-based keep/delete exemptions: bank, payment, securities, exchange, finance, and all other App folders are subject to the same evidence-based security policy.
- No folder is deleted solely because of its category or name.
- Confirmed malicious exact-domain rules may be automatically removed under the high-confidence two-feed rule; deterministic malformed domain/IP rules and exact duplicate lines may be automatically repaired.
- Suspected issues, single-feed matches, shared-hosting parent suffixes, and ambiguous rules are quarantined for review, not automatically deleted.
- Never modify `Rule/Personal` during automated maintenance.

## 4. Permanent no-restore policy

The repository has an exact tombstone manifest at `.github/explicit-rule-exclusions.json`. The automation in `.github/scripts/enforce_explicit_exclusions.py` enforces only entries still present in that manifest.

The user later explicitly withdrew any category-specific retention policy for bank/payment/securities/exchange/finance folders. The 14 restored folders are not specially protected; they are subject to the same evidence-based security remediation as every other App. Only exact user-directed tombstones remain protected from restoration.

The 14 restored folders remain present but have no special keep/delete status. Do not create category-based tombstones. Any exact user-directed tombstone can only be removed after an explicit restoration request for that item. Git history is audit/recovery only, never automatic restoration authority.

## 5. Workflow responsibilities

Workflows must:
1. Enforce exact user tombstones before each batch; fail closed if the manifest is missing, malformed, or unsafe.
2. Never infer exclusions from App categories.
3. Never restore tombstoned content from upstream feeds, caches, snapshots, backups, or Git history without explicit user authorization.
4. Keep `Rule/Personal` outside automated remediation.
5. Automatically remove exact duplicate lines and deterministic malformed domain/IP rules, preserving a per-change audit log.
6. Automatically remove a routing-list `DOMAIN` rule only when the exact hostname is independently present in both OpenPhish and URLhaus; never auto-delete from block/filter lists.
7. Treat single-feed matches, parent suffixes, shared hosting, and ambiguous findings as quarantine/review items.
8. If either security feed is unavailable, report incomplete coverage and disable threat-based automatic deletion; deterministic syntax repairs may continue.
9. Process all 100-folder batches sequentially, committing each batch separately for rollback.

Workflow optimization is the current first priority. All rule-set changes must be batch-scoped and reviewed.

## 6. Completed work recorded in repository reports

Use these as records, not as a reason to repeat the work:
- `Rule/CONSOLIDATION-PLAN.json`: canonical App-folder plan, format decisions, and keep-separate boundaries.
- `Rule/CONSOLIDATED-INDEX.md`: folder structure, consolidation decisions, and subscription-path notes.
- `Rule/AUDIT-REVIEW.md`: manual security/scope interpretation.
- `Rule/Upstream/APP-POLICY-MERGE-REPORT.md`: prior App-folder merge report.
- `.github/explicit-rule-exclusions.json`: exact no-restore tombstones.
- `.github/scripts/enforce_explicit_exclusions.py`: exact tombstone enforcement.
- `.github/workflows/cleanup-audit.yml`: audit workflow.

Prior reports record 14 canonical App-folder consolidation groups and 19 alias folders removed. Verify current files before relying on any historical count.

## 6.1 Latest verification batch (2026-11-27 13:35 UTC)

Verified against the current `main` tree and the latest inventory generated at 13:29 UTC:

- Current upstream library: 842 `.list` files, 677 App/category folders, and 654 top-level folders.
- 107 multi-file folders were checked. Every folder has exactly one file per recognized format; there are no same-format duplicate files.
- The 14 canonical App folders all exist and all 19 approved alias folders are absent. The plan has 0 exact duplicate candidates and the audit has no unapproved identical-content candidates. Its 19 cross-App overlap pairs and 2 separate-scope groups remain explicitly keep-separate; the 3 All / All_No_Resolve pairs also remain separate by design.
- The 2 byte-identical groups and 3 same-payload groups are intentional `All` / `All_No_Resolve` format pairs in AdGuardSDNSFilter, ChinaMaxNoIP, and EasyPrivacy. Keep each format separately; do not delete these pairs.
- 15 cached author snapshots (300 source rules) were compared against 26 mapped format targets. Missing source rules: 0. Missing format targets: 0. This only certifies the cached 15 snapshots, not every possible author.
- Static checks report 0 duplicate rule lines, 0 hidden control characters, 0 invalid native filters, 0 unsupported/missing operands, 0 invalid networks/domains, 0 IP-family mismatches, 0 catch-all networks, and 0 stale/private root suffixes.
- There are 896 bare public-TLD suffix rule occurrences across 78 values. They passed the current IANA delegation check; their routing breadth still needs scenario-aware review, not automatic deletion.
- OpenPhish loaded 280 domains and matched 77 rule rows across 15 hostnames and 15 parent-suffix rules. These are shared-hosting parent-suffix matches, not proof that the parent suffix itself is malicious. No parent suffix was removed.
- URLhaus was not loaded because `URLHAUS_AUTH_KEY` is unavailable. This is incomplete feed coverage, not a clean result.
- The library contains 34 curated shared-hosting suffixes across 159 rule occurrences.
- 244 upstream financial-domain keyword matches across 30 domain values remain untouched by category-based rules. Seven crypto/securities/finance review folders (322 rule entries) remain present and are subject to the same evidence-based security policy as all other folders.
- The three files in `Rule/Personal` remain untouched.
- The 14 historical exclusions were subsequently explicitly restored by the user on 2026-11-27; see Section 9. They are not current tombstones.

## 7. Next work — resume here

1. Keep the automatic 100-folder maintenance workflow running sequentially on push/schedule.
2. Validate the latest regression-tested run and preserve its per-batch reports.
3. Keep the 15 cached author snapshots as the only author sources; no new author fetching.
4. Continue App-specific rule completeness checks and preserve distinct formats and App boundaries.
5. URLhaus threat-based deletion remains disabled until a valid URLHAUS_AUTH_KEY repository secret is configured; never downgrade the evidence threshold.
6. Keep Rule/Personal excluded from all automatic modifications.
7. Update this file after each verified maintenance cycle; new chats must resume from the latest section.

## 8. Session-resume protocol

At the start of every resumed session:
1. Read `SURGE-PROJECT-STATE.md`.
2. Read the exact tombstone manifest and the current consolidation plan.
3. Check the latest Git commit and only the files relevant to the recorded next task.
4. Continue from **Section 7**, without redoing completed work.
5. Update this file at the end of the work batch.

Do not claim work is complete based only on a green GitHub Actions status. Verify the actual rule files and the resulting Git tree.


## 9. 2026-11-27 explicit restoration batch

- User explicitly requested retrieval of author rule sets and restoration of all 14 historical folders.
- Restored files: `BOC/BOC.list` (22 rules), `BOCOM/BOCOM.list` (6), `CCB/CCB.list` (18), `CEB/CEB.list` (15), `CGB/CGB.list` (4), `CMB/CMB.list` (38), `ICBC/ICBC.list` (58), `PSBC/PSBC.list` (3), `AliPay/AliPay.list` (21), `PayPal/PayPal.list` (248), `Stripe/Stripe.list` (1), `UnionPay/UnionPay.list` (16), `VISA/VISA.list` (99), `PingAn/PingAn.list` (27).
- Primary source: blackmatrix7/ios_rule_script Surge-format rule files. Each restored file includes its source URL and source author in the header.
- The 14 exact tombstones were removed from `.github/explicit-rule-exclusions.json` after the explicit user instruction.
- The 14 restored folders have no category-specific keep/delete exemption. Apply the same evidence-based security policy as every other App; do not fetch new authors.


## 10. Workflow-first and 100-folder batch protocol (2026-11-27)

- User directed that workflow problems be optimized first, then run the project library in batches of 100 rule-set folders, continuously refining between batches.
- Current tree count: 655 tracked top-level directories under `Rule/Upstream`; 654 eligible rule-set folders after excluding `SourceMetadata`.
- Added `.github/scripts/batch_preflight.py`: deterministic alphabetical 100-folder read-only validator. It checks UTF-8 readability, symlinks, duplicate rule lines, duplicate recognized file formats within a folder (review only), top-level and nested symlinks, unsupported/missing rule operands, invalid IP networks, invalid domain operands, hidden control characters, broad single-label suffixes (review only), exact tombstones, and a before/after digest of `Rule/Personal`. It does not edit or delete rules.
- Added `.github/workflows/batch-preflight.yml`: automatic `push` trigger for upstream `.list` changes, preflight script/workflow changes, or tombstone-manifest changes; it processes all available 100-folder batches sequentially in one run, stops on the first blocker, uploads all reports, and retains a manual `workflow_dispatch` fallback. Repository permission is read-only, concurrency is serialized, and reports are retained for 30 days.
- Disabled automatic push triggers on the previous full-library audit and App-consolidation workflows. They now require manual dispatch; this prevents every rule-file push from starting an unbounded full-library job.
- Removed the automatic call to `remove_invalid_public_tld_rules.py` from the audit workflow. Broad-TLD findings must be review-only; the workflow must not silently delete rules as part of an audit.
- First automatic trial was triggered by the workflow change itself: run `46012159743`, commit `51300f8be5fc38e21146dcebe794f827cd141163`, created 2026-11-27 14:01:26 UTC. It was in progress at the time of this state update. Inspect its job logs and uploaded artifacts before claiming any batch completed.
- Legacy Apply App Policy-Group Consolidation run #16 completed successfully at 2026-11-27 13:46 UTC against commit `5c51d488ed2ec5e6aad296454f4d7e4a4fa21a00`, before the push trigger was removed. It was not the new 100-folder trial. Do not treat it as batch approval.
- Do not run the full consolidation workflow as part of batch preflight. Do not merge or delete any folder during preflight.
- The 14 restored bank/payment/finance folders are verified present; the tombstone manifest is empty. The exclusion enforcer accepts an empty list safely.
- Next action: monitor automatic run `46012159743`; inspect the first batch report and any blockers. The workflow is read-only, so even a fully passing run does not itself authorize rule deletion or rewriting. Use the results to refine the workflow, then begin content optimization in reviewed 100-folder batches.


## 11. First automatic end-to-end batch run (2026-11-27)

- Automatic workflow run: [46012159743](https://github.com/AllanRita/Surge/actions/runs/46012159743), event `push`, commit `51300f8be5fc38e21146dcebe794f827cd141163`; conclusion: **success**.
- All 654 eligible folders were processed in one sequential run: 6 batches of 100 and a final batch of 54. Total: 842 .list files and 4,335,128 rule entries (sum of batch reports).
- All 7 batches reported 0 blockers. Review-only findings: 902 total. Breakdown: batch 1 = 30; batch 2 = 845; batch 3 = 7; batch 4 = 10; batch 5 = 5; batch 6 = 1; batch 7 = 4.
- Most review-only findings are single-label suffix operands (especially ChinaMax, ChinaTest, ChinaMaxNoMedia, and ChinaMaxNoIP); these may be intentional broad regional/TLD routing rules and must be reviewed in context, not automatically deleted.
- Six folders were flagged for multiple files sharing a recognized format label. The current heuristic may over-flag aggregate/multi-category folders; inspect the exact paths and refine classification before treating these as true duplicate formats.
- The run was read-only: no rule files were modified, deleted, renamed, merged, or restored. The 14 restored bank/payment/finance folders remained present but had no category-specific protection. `Rule/Personal` remained unchanged according to the per-run digest check.
- Artifact: `surge-rule-batches-1`, artifact ID `15203898521`, 30-day retention. It contains JSON and Markdown reports for all 7 batches.
- Important distinction: this success confirms the batch workflow and static preflight completed. It does not mean all 902 review items are security defects or that rule content optimization is complete.
- Next: refine false-positive review heuristics (especially single-label/TLD suffixes and aggregate folder format labels), then begin actual rule-content review and safe improvements in 100-folder batches. Keep changes reversible and log every added/removed rule; no automatic deletion based only on static heuristics.


## 12. User-approved automatic maintenance V1.0 (2026-11-27)

- User explicitly approved Workflow V1.0: one automatic run processes all 100-folder batches sequentially; automatic deterministic repairs; only existing cached author sources (new broad author collection remains paused); confirmed malicious rules may be automatically deleted; suspected findings are quarantined for review; exact user-deleted content is never automatically restored.
- Removed the former category-specific protection for bank, payment, securities, exchanges, and finance. No App category has a special keep/delete exemption. The 14 previously restored folders remain in the library but are subject to the same evidence-based policy as all other folders.
- Updated `.github/explicit-rule-exclusions.json`: only exact user-directed tombstones remain. Category-based deletion policy is explicitly disabled; all categories share the same security policy.
- Updated `Rule/CONSOLIDATION-PLAN.json` security policy: exact malicious hostname corroborated by both OpenPhish and URLhaus may be removed only from an exact `DOMAIN` routing rule; block/filter lists are excluded; parent suffixes/shared hosting and single-feed hits remain review-only; `Rule/Personal` is excluded.
- Added `.github/scripts/batch_maintain.py`: deterministic duplicate-line removal; removal of clearly malformed `DOMAIN`, `HOST`, `IP-CIDR`, and `IP-CIDR6` operands; narrow dual-feed exact-host threat deletion; JSON change log and review findings; verifies `Rule/Personal` digest unchanged. It never deletes whole App folders, never modifies personal rules, and never treats unknown rule types as malicious.
- Upgraded `.github/workflows/batch-preflight.yml` to a scheduled + push-triggered automatic maintenance workflow with write permission, sequential 100-folder batches, per-batch commit/push (Git history rollback point), 90-day report artifacts, and manual dispatch fallback. If URLhaus is unavailable, threat-based deletion is disabled; deterministic repairs may continue and the report marks incomplete coverage.
- The workflow has not yet been declared successful. Validate its first actual run, script execution, and resulting commits/reports before claiming end-to-end success. Any syntax or workflow error must be corrected before subsequent scheduled runs.
- Cached author sources remain the only permitted author comparison corpus. This maintenance script currently performs safe deterministic cleanup and security triage; it does not yet perform full cached-author gap-fill/format-union merging. That capability remains a distinct follow-on implementation and must preserve format semantics.
- Next: inspect the first run triggered by these workflow changes; verify batch counts, changes, quarantined findings, personal-file digest, tombstone enforcement, and Git commit history. Then add the cached-source merge stage with per-format safety gates.

## 13. Implementation run status (2026-11-27)

- V1.0 implementation commits are present on main. The automatic maintenance workflow accepted the YAML and started run [46015832021](https://github.com/AllanRita/Surge/actions/runs/46015832021) at 14:25:40 UTC; the job passed checkout, Python setup, security-feed download, and exact tombstone enforcement, and was executing the sequential maintenance step at last inspection.
- Several intermediate push-triggered runs occurred while the workflow, script, manifest, and project state were being committed. Some were cancelled by the serialized concurrency group; do not treat those cancelled runs as maintenance failures or completed batches. The latest run is the one to verify.
- Do not claim the full V1.0 end-to-end process is complete until run 46015832021 finishes and its per-batch artifacts and Git commits are checked.
- Implemented deterministic auto-remediation currently includes exact duplicate line removal and clearly invalid DOMAIN/HOST/IP-CIDR/IP-CIDR6 operand removal. Threat deletion is limited to an exact DOMAIN hostname present in both OpenPhish and URLhaus, and excluded from paths classified as block/filter lists. If URLhaus is unavailable, threat-based deletion is disabled.
- Single-feed matches and parent-suffix/shared-hosting matches are written as review findings; no broad suffix or App folder is automatically deleted. Personal rules are protected by a digest check.
- Every batch is committed separately if files changed; Git history is the rollback point. Reports are uploaded as 90-day artifacts.
- Remaining V1.0 work: validate the first complete run, refine quarantine/reporting if needed, and implement cached-author source gap-fill and format-aware union merging using the existing 15 cached snapshots only. No new author sources may be fetched.


## 14. Cached-author merge implementation and first full execution (2026-11-27)

- Added `.github/scripts/merge_cached_sources.py` and integrated it into the sequential 100-folder maintenance workflow. It uses only the 15 existing `Rule/Upstream/SourceMetadata/*.json` snapshots (Aoang/Surge and SukkaLab); no new author sources were fetched.
- The validated full execution completed successfully in workflow run [46019188959](https://github.com/AllanRita/Surge/actions/runs/46019188959). All 654 eligible folders were processed as 6 batches of 100 and a final batch of 54. Each batch passed preflight; artifact `surge-automatic-maintenance-18`, ID `15208210927`, contains all reports.
- Cached-source comparison processed all 15 snapshots across batches 1–6. It compared 576 source rule entries across the applicable matching target formats: 257 exact matches and 240 semantically covered entries in the reports, with 0 additions, 0 review-only source rules, and 0 target files changed. The remaining source-rule count in the aggregate 576 is accounted for in per-target results; do not interpret source-rule totals as unique rules across formats because the same source snapshot is intentionally compared against multiple output formats.
- Examples of semantic coverage: `DOMAIN,apm-misaka.biliapi.net` is already covered by `DOMAIN-SUFFIX,biliapi.net`; `DOMAIN,oneclient.sfx.ms` is covered by `DOMAIN-SUFFIX,oneclient.sfx.ms`; Apple source domains are substantially covered by the existing Apple parent suffix rules. Do not add redundant exact child rules when an existing suffix rule already covers them.
- No rule files needed changes in this pass. All 7 batch reports show `Rule/Personal` unchanged. The exact deletion tombstone check passed in every batch; no user-deleted folders were restored. The 14 finance/bank/payment-related folders were not subjected to any category-based deletion rule.
- Security limitation remains: OpenPhish loaded (280 feed hosts), but URLhaus was unavailable (0 hosts). Threat-based deletion was therefore disabled for every batch. The run status explicitly records incomplete security coverage; no dual-feed threat deletion occurred. This is not a security-complete acceptance.
- Refined the cached-source semantic comparison so IP network containment only counts as coverage when both rules have the same `no-resolve` mode. This prevents treating behaviorally different Surge IP rules as equivalent. The refinement commit is `0afd9f2b731c57ef3f0ed0367735c8df961379c6`; its push starts a fresh validation run.
- Next: verify the validation run after the `no-resolve` refinement; keep author-source collection paused; continue reviewing only existing snapshots and actual app-rule gaps. Do not claim that rules were supplemented unless the reports show additions and corresponding committed file changes. Continue to keep URLhaus-dependent deletion disabled until the feed is successfully available.


## 15. Continued V1.0 implementation and first-run verification (2026-11-27)

- Verified first automatic maintenance run [46015832021](https://github.com/AllanRita/Surge/actions/runs/46015832021): all 7 batches completed (6 x 100 + 54). Every batch reported zero deterministic cleanup changes; Rule/Upstream had no automated edits in this run. The run's Git comparison after completion showed only project-state bookkeeping commits, not rule-file changes. Therefore the run validates orchestration and report generation, but does not yet test real rule mutation or rollback.
- All 7 maintenance reports recorded security_coverage_complete=false: OpenPhish loaded 280 hosts, URLhaus loaded 0 because URLHAUS_AUTH_KEY was not available. Consequently corroborated hosts = 0 and threat-based automatic deletion was disabled in every batch. The green Actions conclusion must not be interpreted as a complete security pass.
- Artifact surge-automatic-maintenance-7 (ID 15205653215) was downloaded and inspected: it contains JSON/Markdown reports for all 7 batches and 7 maintenance JSON reports. Each maintenance report shows no changes and personal_unchanged=true.
- Verified all 15 existing cached author snapshots under Rule/Upstream/SourceMetadata: nine Aoang/Surge snapshots and six SukkaLab snapshots. No new author sources were fetched.
- Targeted comparisons confirmed the cached rules are already represented by exact or broader semantic rules in several target files: Aoang DNS (53/53 exact), Aoang Other, Parallels, Process, Teams, Unavailable and YouTube exact matches; SukkaLab Apple's 16 rules are present in standard/Resolve, with the remaining All-variant exact mismatch covered by the broader akadns.net suffix; OneDrive's DOMAIN,oneclient.sfx.ms is covered by DOMAIN-SUFFIX,oneclient.sfx.ms; BiliBiliIntl's DOMAIN,apm-misaka.biliapi.net is covered by DOMAIN-SUFFIX,biliapi.net. These examples must not be redundantly appended.
- Added .github/scripts/merge_cached_sources.py: an idempotent, format-aware batch-stage for all 15 cached snapshots. It compares exact rules plus domain-suffix ancestry and IP network containment, preserves standard/Resolve/All/All_No_Resolve formats, adapts IP no-resolve options to the target format, records provenance, writes pre-change backups, and protects Rule/Personal. It only touches targets mapped to folders in the current 100-folder batch.
- Integrated cached-source merging into .github/workflows/batch-preflight.yml; metadata JSON changes now trigger maintenance. Cached-source reports are included in the artifact and job summary.
- Added pre-change backups to deterministic remediation and cached-source merge. If remediation, merge, or preflight fails before commit, the current uncommitted batch is reverted with git checkout -- Rule/Upstream; previously committed batches remain intact.
- Fixed URLhaus hostfile parsing to read the first hostname column rather than the trailing comment/URL.
- Reconciled Rule/CONSOLIDATION-PLAN.json: removed obsolete active bank/payment/finance category deletion and keep restrictions, removed stale finance exclusion lists and superseded confirmation fields, and recorded the withdrawn category-based decision as history only. All App categories now follow the same evidence-based security policy.
- Validation of the new cached-source stage and backup path is pending the latest post-change Actions run. No new author fetching has been enabled. No rule content has been intentionally merged or deleted by this chat session.
- Remaining blocker: add a valid URLHAUS_AUTH_KEY as a GitHub Actions repository secret to enable dual-feed threat confirmation. Without it, the workflow may perform deterministic repair and cached-source comparisons, but must report incomplete threat-intelligence coverage and must not automatically delete threat-feed matches.
- Next: inspect the latest post-change workflow run; confirm all 15 snapshots are processed across their respective batches, no semantic duplicates are added, all reports/backups are present, and personal rules remain unchanged. Then test an isolated controlled change/rollback scenario without modifying production rule content.


## 16. Post-refinement validation completed (2026-11-27)

- Validation run [46018472264](https://github.com/AllanRita/Surge/actions/runs/46018472264) completed with conclusion `success`; all workflow steps passed, including sequential processing and artifact upload.
- Reprocessed all 654 eligible folders in 7 batches (100×6 + 54). Every batch preflight returned PASS with 0 blockers. Review-only findings remain: 30, 845, 7, 10, 5, 1, and 4 respectively (902 total); these are not automatic deletion instructions.
- The no-resolve semantic-coverage refinement was included in this successful run. Cached-source comparison again found 0 additions and 0 files changed; all batch reports show the personal directory unchanged.
- URLhaus was still unavailable (`URLHAUS_AVAILABLE=false`); threat-based deletion remained disabled. Do not mark security intelligence coverage complete.
- Artifact: `surge-automatic-maintenance-15`, artifact ID `15206941994`.
- Next: improve URLhaus feed availability/credential handling without weakening fail-closed behavior; review the 902 static preflight findings with false-positive-aware classification; then continue deeper app-specific domain completeness checks and per-format comparisons. Keep all author fetching paused and preserve exact deletion tombstones.


## 17. Self-test failure diagnosis and correction (2026-11-27)

- Two push-triggered runs [46018937181](https://github.com/AllanRita/Surge/actions/runs/46018937181) and [46019010062](https://github.com/AllanRita/Surge/actions/runs/46019010062) failed before any production maintenance began. The failure was an outdated unit test expecting an IP subnet with different `no-resolve` behavior to count as semantically covered.
- The implementation's stricter behavior is intentional and safer: IP network containment only counts when both source and existing rules have the same `no-resolve` option. The unit test was corrected to cover same-mode positive and different-mode negative cases. No production rule files were modified by the failed runs.
- Run [46019188959](https://github.com/AllanRita/Surge/actions/runs/46019188959) passed all six offline self-tests and completed all seven batches. A subsequent test-only run [46019218420](https://github.com/AllanRita/Surge/actions/runs/46019218420) exposed a second assertion typo in the no-resolve test fixture; production maintenance did not run in that failed job. The assertion was corrected. Follow-up run [46019533469](https://github.com/AllanRita/Surge/actions/runs/46019533469) passed all six offline self-tests and completed all seven 100-folder batches successfully; artifact ID 15206808092 was inspected.
- Continue to fail closed on URLhaus unavailability. Keep all production rule changes protected by per-batch backup and preflight.


## 18. Final regression-tested V1.0 run (2026-11-27)

- Latest run [46019533469](https://github.com/AllanRita/Surge/actions/runs/46019533469) completed with conclusion success. All workflow steps passed: six offline regression tests, security feed download step, exact tombstone enforcement, all seven sequential batches, summary generation, and artifact upload.
- Artifact surge-automatic-maintenance-20, ID 15206808092, was downloaded and inspected. All 654 eligible folders completed (6 x 100 + 54).
- All 15 cached author snapshots were processed across batches 1–6, with 24 target-format comparisons and 576 source-rule-to-target comparisons: 337 exact present, 239 semantically covered, 0 added, 0 review-only, and 0 files changed. All 7 batches report Rule/Personal unchanged.
- All six offline tests passed: domain suffix semantic coverage, IP network containment with matching no-resolve mode, rejection of mismatched resolution modes, Resolve-format adaptation, idempotent cached merge plus backup creation, deterministic duplicate cleanup plus backup creation, and URLhaus hostfile first-column parsing (the test suite contains six grouped tests).
- The earlier failed self-test runs 46018937181, 46019010062, and 46019218420 stopped before production maintenance. Their failures were test-fixture expectation mistakes, not production-rule changes. The corrected test suite passes in 46019533469.
- No production rule files were changed in the latest run because all cached rules were already exact or semantically covered and no deterministic cleanup candidates were found. The backup creation path was verified using temporary test fixtures; no production backup files were needed.
- Security remains incomplete: URLhaus loaded 0 hosts because URLHAUS_AUTH_KEY is unavailable. OpenPhish loaded 280 hosts. Threat-based automatic deletion stayed disabled in every batch. Do not interpret the green workflow conclusion as a complete threat-intelligence pass.
- The 14 bank/payment/finance folders have no category-based protection; all App categories follow the same evidence-based policy. Exact user tombstones remain the only no-restore protection. Rule/Personal remains excluded from automation.
- Next required external setup: add a valid URLHAUS_AUTH_KEY in GitHub repository Settings -> Secrets and variables -> Actions. Do not send the key in chat. After the secret is available, the next scheduled/push run can validate dual-feed threat coverage. Until then, keep threat-based automatic deletion disabled.
- Next project task: continue app-by-app rule completeness review and format-aware cached-source maintenance, using only the 15 existing snapshots. Do not fetch new author sources.


## 17. Preflight false-positive reduction and validation (2026-11-27)

- Corrected `.github/scripts/batch_preflight.py` format detection: compare recognized format variants only within the same immediate App directory, not across different nested Apps under category containers. This removes false positives such as Cloud, Game, Block, Process, Assassin'sCreed, and ChinaIPs without changing or deleting any files.
- Added optional IANA root-zone TLD reference support. The workflow downloads the official `https://data.iana.org/TLD/tlds-alpha-by-domain.txt` file, validates its version header, and passes it to each batch preflight. Delegated single-label TLD suffixes are no longer incorrectly reported as unregistered/special-use; labels absent from the IANA root zone remain review-only. If the reference is unavailable, the workflow falls back to conservative review-only flags.
- Added offline tests for nested App format grouping and IANA TLD parsing. A fixture escaping issue was corrected; latest validation passed all 8 self-tests.
- Latest full validation run [46020030494](https://github.com/AllanRita/Surge/actions/runs/46020030494) completed successfully. All 654 folders (6×100 + 54), 842 rule files, and 4,335,128 rule entries were scanned. All 7 batches passed with 0 blockers and 0 review findings. Duplicate rule lines, unsupported types, invalid IP networks, and invalid domain operands were all 0.
- IANA reference used in every batch: `Version 2026112700, Last Updated Fri Nov 27 07:07:01 2026 UTC`. The previous 896 single-label TLD review findings were cleared by validating delegated TLDs against this official root-zone list; no rule content was removed or rewritten for this change.
- The previous 6 nested-container format warnings were eliminated by scoping comparison per App directory; the actual format variants remain untouched.
- Cached author comparison again processed the 15 existing snapshots, with 0 additions and 0 changed target files; `Rule/Personal` remained unchanged. No new author source was fetched.
- Security limitation remains: `URLHAUS_AUTH_KEY` is not configured, so URLhaus is unavailable and dual-feed threat-based automatic deletion remains disabled. OpenPhish-only hits do not authorize deletion. The artifact status explicitly records incomplete security coverage.
- Artifact: `surge-automatic-maintenance-24`, ID `15207447770`.
- Next: continue deeper App-by-App coverage checks against existing cached sources and already-present rule files, preserve each format independently, and investigate URLhaus credential provisioning. Do not broaden author collection or modify any rule unless a verified gap or deterministic safety defect is found.


## 18. Reconcile stale finance-policy documentation (2026-11-27)

- Verified directly in the current Git tree that all 14 previously restored bank/payment/financial App folders exist: BOC, BOCOM, CCB, CEB, CGB, CMB, ICBC, PSBC, AliPay, PayPal, Stripe, UnionPay, VISA, PingAn. Also verified Binance, OKX, Crypto, Cryptocurrency, EastMoney, TigerFintech, and XueQiu are present.
- Verified `.github/explicit-rule-exclusions.json` has an empty `exclusions` list. There are no current category-based keep/delete exceptions.
- Reconciled the previously stale bank/payment deletion history in `Rule/CONSOLIDATED-INDEX.md` and `Rule/AUDIT-REVIEW.md`: the 14 folders are present, have no special category-based protection, and follow the same evidence-based security criteria as every other App. Matching financial domains are not removed solely based on category. `Rule/Personal` remains excluded from automation.
- URLhaus's official Community API documentation states an Auth-Key is required for feed downloads. The GitHub Actions workflow cannot add repository secrets through the connected GitHub interface. To enable the second independent feed, the repository owner must create a free abuse.ch Auth-Key and add it as the GitHub Actions repository secret named `URLHAUS_AUTH_KEY`. Until then, dual-feed threat deletion remains disabled; this is fail-closed by design.
- Official URLhaus documentation: https://urlhaus.abuse.ch/api/ (Auth-Key required); see also the IANA root-zone reference already recorded in Section 17.
- Next: continue App-by-App cross-format coverage checks and review security matches; do not change rule semantics or delete anything based on App category. Revalidate the next automatic run after any script/workflow changes.


## 14. Verified V1.0 maintenance run (2026-11-27 15:02 UTC)

- Run 46015832021 / job 140562599029 completed successfully at 14:26:12 UTC. All seven batches passed in order, 654 unique alphabetically sorted folders (100 x 6 + 54), 842 files, 4,335,128 rules, zero blockers and zero maintenance changes. Review counts 30/845/7/10/5/1/4 (902 total). No maintenance commits in inspected history; all seven reports confirm personal_unchanged=true. Exact exclusion checks passed each batch (0 entries enforced).
- Downloaded artifact 15205653215: 22 files, seven maintenance JSON, seven preflight JSON, seven Markdown and status file. All maintenance reports show OpenPhish 280, URLhaus 0, coverage incomplete; no threat deletions. URLHAUS_AUTH_KEY missing. Do not interpret green status as complete security coverage.
- Code inspection found parent suffix review checks only corroborated hosts, so single-feed suffix hits are silently omitted (all seven maintenance reports show zero review findings). URLhaus hostfile parser takes first token rather than hostname in IP-prefixed rows. Block/filter classification is path-substring based and should be replaced by explicit reviewed routing scope before enabling threat deletion. Cached author format-aware gap-fill remains unimplemented.
- Proposed next upgrade (not applied): validate feed schema and counts, review suffix hits against union of feeds, keep exact-host dual-feed deletion disabled unless both valid and explicit routing scope; add fixture tests, fail on missing expected reports, compare protected paths and batch-scoped diff before push. Implement cached-only format comparison in report-only mode first, then approved compatible additions. No new author fetch, no rule semantics change, no permission expansion. Section 7 and historical category-specific statements are superseded by sections 12–14. Resume with these outstanding issues, not completed batch verification.


## 19. Documentation reconciliation and paired-format audit (2026-11-27 15:01 UTC)

- Corrected stale bank/payment documentation in README.md, Rule/CONSOLIDATED-INDEX.md, Rule/AUDIT-REVIEW.md, Rule/Upstream/CLEANUP-INVENTORY.md, and Rule/Upstream/APP-POLICY-MERGE-REPORT.md. The exact deletion manifest .github/explicit-rule-exclusions.json is empty; all 14 dedicated bank/payment App folders are present. No category-based keep/delete rule applies. The 7 finance/trading/crypto review folders are also present and follow the same evidence-based security policy.
- Current inventory snapshot: 842 upstream .list files, 677 App/category folders, 654 top-level folders, 107 multi-file folders, 0 duplicate rule lines, 15 cached author snapshots (300 source rules), and 0 uncovered cached-source rules. It reports 14 bank/payment folders present, 7 finance review candidates, 896 bare public-TLD suffix occurrences across 78 IANA-delegated values, and 34 shared-hosting suffixes across 159 occurrences.
- Updated financial keyword audit: 244 upstream matches across 30 domain values. These are classification/review flags, not proof of malicious behavior and not automatic deletion candidates. The personal PayPay file remains outside automation.
- Added .github/scripts/audit_format_parity.py, a read-only semantic comparison for compatible paired formats. It ignores only no-resolve when comparing rule identity; rule type, operand, and all other options remain significant. It does not modify rule files or personal files.
- Added regression tests for format-pair normalization and non-resolution options; the offline suite now runs 11 tests and passed in workflow run [46020996994](https://github.com/AllanRita/Surge/actions/runs/46020996994).
- Integrated the format audit into .github/workflows/batch-preflight.yml before sequential maintenance. The audit scanned all 842 rule files and compared 126 compatible format pairs across 93 folders: 104 Standard/Resolve, 19 All/All_No_Resolve, and 3 No_IPv6/No_IPv6_Resolve.
- Result: 0 of 126 pairs had missing or extra rules after normalization; 123 pairs differed only in expected no-resolve option flags (152,927 per-rule flag differences across the pair comparisons). The remaining 3 pairs had no such option differences. No automatic rule changes were made.
- Workflow run [46020996994](https://github.com/AllanRita/Surge/actions/runs/46020996994) completed successfully; all 654 eligible folders processed in 7 sequential batches. All 15 cached sources were processed in their matching batches, with 0 added rules, 0 files changed, and Rule/Personal unchanged. Artifact surge-automatic-maintenance-27, ID 15207623477, contains the format-parity JSON/Markdown report and all seven batch reports.
- URLhaus remains unavailable because URLHAUS_AUTH_KEY is not configured or the feed download failed. OpenPhish loaded 280 hosts. Threat-based automatic deletion remained disabled; the successful workflow is not a complete dual-feed security pass.
- Next: use the 78 valid single-label TLD suffixes and 34 shared-hosting suffixes for scenario-aware scope review, prioritizing broad aggregate lists (China/ChinaMax variants) and avoiding automatic deletion. Continue app-by-app completeness checks using only existing cached author snapshots; no new author fetching.




## 20. Latest successful parity and sequential maintenance verification (2026-11-27 15:06–15:07 UTC)

- Latest verified run: [46021896550](https://github.com/AllanRita/Surge/actions/runs/46021896550), commit `b38bd3e9ec8cb3644cca602bb870ee60d0cb9659`. All workflow steps completed successfully, including the offline regression suite, read-only semantic format audit, exact tombstone enforcement, seven sequential maintenance batches, summary generation, and artifact upload.
- Processed all 654 eligible top-level folders in order: 6 batches of 100 and a final batch of 54. All 842 upstream rule files and 2,691,526 domain rules were in the current inventory snapshot. No maintenance changes or deletions were made; all seven reports confirm `personal_unchanged=true`.
- Cached-only author coverage: all 15 existing author snapshots were processed; across batch reports 576 source-rule occurrences were evaluated (337 exact matches and 239 semantically covered). There were 0 missing rules, 0 review-only findings, 0 additions, and 0 changed files. No new author source was fetched.
- Semantic format audit: 842 files scanned and 132 compatible pairs compared: 104 Standard/Resolve, 19 All/All_No_Resolve, 3 No_IPv6/No_IPv6_Resolve, 3 Standard/No_IPv6, and 3 Resolve/No_IPv6_Resolve. All 132 pairs have identical normalized rule multisets; 0 left-only and 0 right-only rules. The 123 expected resolution-option differences were reported separately. No format was merged or rewritten.
- Exact tombstone manifest remains empty (0 exclusions). All 14 bank/payment App folders and the seven finance/trading/crypto review folders remain present with no category-based exemption. `Rule/Personal` was not changed.
- Artifact: `surge-automatic-maintenance-36`, ID `15210275136`; it contains all seven maintenance/preflight reports plus `format-parity-audit.json`, `format-parity-audit.md`, and `format-coverage.json`.
- Security remains intentionally fail-closed for threat deletion: OpenPhish loaded 280 hosts, URLhaus loaded 0 because `URLHAUS_AUTH_KEY` is unavailable. Security coverage is explicitly marked incomplete and no threat-based automatic deletion occurred. The successful run is not a complete dual-feed security clearance.
- Next work: perform scenario-aware, report-only review of the 78 IANA-delegated bare public-TLD suffixes (896 rule occurrences) and 34 shared-hosting suffixes (159 occurrences), especially broad aggregate lists. Then continue per-App completeness review against existing cached sources only. No category-based deletion, no new author fetching, and no automatic change to routing semantics.


## 19. Single semantic format audit and latest full validation (2026-11-27)

- Removed the redundant `.github/scripts/audit_format_coverage.py` stage after consolidating format checks into the more detailed `.github/scripts/audit_format_parity.py`. The workflow now runs one report-only semantic parity audit before feed retrieval and the 100-folder maintenance pass.
- Expanded paired-format comparisons to include Standard vs No_IPv6 and Resolve vs No_IPv6_Resolve. For these two comparisons only, IPv6 rules are excluded from the IPv6-capable side; all other rule types, operands, and options remain significant. Standard/Resolve and All/All_No_Resolve comparisons ignore only the `no-resolve` flag and report that mode difference separately.
- Added/retained offline tests proving: no-resolve differences are isolated; policy/other options remain significant; No_IPv6 variants omit IPv6 rules only; missing IPv4/domain rules remain visible; and the audit never edits source files.
- Latest validation run [46022027814](https://github.com/AllanRita/Surge/actions/runs/46022027814) completed successfully with all steps green. It processed 654 folders in 7 sequential batches (6×100 + 54).
- Preflight scanned 842 rule files and 4,335,128 rule entries. All 7 batches had 0 blockers and 0 review findings. IANA root-zone reference was available in every batch (`Version 2026112700`), and the previous 896 delegated-TLD shape warnings remain cleared.
- Semantic format audit scanned all 842 rule files and compared 132 documented format pairs: 0 pairs needing review, 0 left-only occurrences, 0 right-only occurrences. 123 pairs correctly showed `no-resolve` option differences; these are expected format differences and are reported separately.
- Existing 15 cached author snapshots were processed again: 576 source-rule comparisons, 0 additions, 0 review-only entries, 0 files changed. No new author sources were fetched.
- Every batch reported `Rule/Personal` unchanged. The exact deletion manifest has zero tombstones, and no category-based deletion/retention rule exists.
- URLhaus remains unavailable because `URLHAUS_AUTH_KEY` is not configured. The run correctly marks security coverage incomplete and keeps threat-feed automatic deletion disabled. OpenPhish-only matches do not trigger deletion.
- Artifact: `surge-automatic-maintenance-38`, ID `15208786309`.
- Next: continue scenario-aware App-specific completeness review, using existing sources and existing file formats only. Keep format differences report-only until each App's README/format semantics justify a safe change. The remaining external prerequisite for dual-feed deletion is adding the repository secret `URLHAUS_AUTH_KEY` after obtaining an abuse.ch Auth-Key.


## 21. Report-only broad suffix scope review (2026-11-27)

- Added `Rule/Upstream/BROAD-TLD-SCOPE-REVIEW.md` using the current inventory snapshot. All 78 IANA-delegated bare public-TLD suffixes (896 occurrences) are classified by placement, with exact folder and example-line references. No rule files were changed.
- Scope breakdown: 45 aggregate-only suffixes / 767 occurrences across China/ChinaMax variants; 5 mixed aggregate + App suffixes / 85 occurrences (Alibaba, AliPay, ICBC, Taobao, Tmall); 28 App/service-only suffixes / 44 occurrences.
- Reviewed the existing `Rule/Upstream/SHARED-HOSTING-SCOPE-REVIEW.md`: 34 shared hosting/CDN/dynamic-DNS/URL-shortener suffixes in 159 occurrences, with 33 App/service-folder occurrences and 126 aggregate-folder occurrences. These remain report-only; a malicious tenant does not justify blocking an entire multi-tenant parent suffix.
- Priority for manual scenario review is aggregate-only broad suffixes, especially `cn`, `ms`, and other single-label namespaces. No suffix is to be removed or narrowed automatically; delegated status proves syntax/registration, not intended routing scope.
- Continue with App-by-App scenario review and cached-source checks only. Keep all current protections, preserve every format, and leave `Rule/Personal` untouched.


## 20. Security-deletion tests and canonical-folder verification (2026-11-27)

- Added two safety-focused offline tests:
  - Exact `DOMAIN` threat rule is deleted only when the hostname appears in both OpenPhish and URLhaus; the parent `DOMAIN-SUFFIX` is retained for review, block/filter-list copies are retained, single-feed-only rules remain, a pre-change backup is written, and `Rule/Personal` remains unchanged.
  - A single-feed exact-host match is review-only and never auto-deleted; the report marks security coverage incomplete.
- Latest run [46022500278](https://github.com/AllanRita/Surge/actions/runs/46022500278) passed all 15 offline self-tests and all workflow steps. It again processed all 654 folders in 7 batches with 0 blockers and 0 review findings.
- Format parity: 132 documented pairs checked, 0 content differences, 123 expected no-resolve option differences.
- IANA TLD reference remained available; URLhaus remained unavailable without the repository secret. No threat-based automatic deletion ran in this production pass.
- Verified the 14 canonical App folders in `Rule/CONSOLIDATION-PLAN.json` all exist, and all 19 approved alias folders are absent. No folder consolidation or rule-file changes were needed.
- Verified the 14 bank/payment/financial folders and seven trading/crypto/securities folders are present. The exact tombstone manifest is empty; none has category-based protection or category-based deletion.
- Cached author comparison remained 15 existing snapshots only, with no new author collection and no additions to current target files. Personal rules remain unchanged.
- Artifact: `surge-automatic-maintenance-39`, ID `15208239341`.
- Remaining user-dependent item: obtain a free abuse.ch Auth-Key at https://auth.abuse.ch/ and add it in GitHub repository Settings → Secrets and variables → Actions as `URLHAUS_AUTH_KEY`. Do not send the key in chat. Until configured, the workflow must continue disabling dual-feed deletion.


## 22. Workflow integrity hardening and corrected App completeness evidence (2026-11-27 15:47 UTC)

### Implementation and validation

- Hardened .github/scripts/batch_maintain.py:
  - URLhaus parsing now accepts both domain-first hostfile rows and IP-prefixed hostname rows, while ignoring IP addresses and descriptions.
  - Exact single-feed hostname matches remain review-only.
  - DOMAIN-SUFFIX and HOST-SUFFIX rules are checked against hosts from either available feed; parent suffix matches are review-only and are never deleted.
  - Known block/filter scopes are excluded from exact-host threat deletion, including Block/Reject/Filter paths, Advertising, Privacy, EasyPrivacy, AdGuard DNS Filter, and Hijacking scopes.
- Corrected audit_app_completeness.py so its total entry count includes all non-comment entries, not just comma-delimited Surge rules. It now separates Surge syntax rules, native filter entries, native domain entries, and unclassified entries.
- Added .github/scripts/verify_batch_integrity.py. Before each batch commit it verifies that all three batch reports agree on selected folders, preflight blockers are zero, personal rules are unchanged, changes are limited to existing .list files inside the current batch, and every changed file has a pre-change backup matching the original Git HEAD. Final verification requires all seven reports, all 15 cached snapshots, and a clean paired-format audit.
- Changed backup creation to first-write-wins across deterministic cleanup and cached-source merge, so a later stage cannot overwrite the original pre-batch snapshot with an intermediate version.
- Added offline regression coverage for URLhaus hostfile formats, single-feed parent suffix hits, HOST-SUFFIX handling, block/filter path classification, complete entry counting, batch-scope rejection, and preservation of the first backup.

### Workflow results

- Runs #42 and #43 stopped at the offline self-test gate due to test-fixture escaping/expectation errors. The production maintenance steps were skipped; no production rule files were modified.
- Run #44 passed the full workflow and all seven batches. Artifact ID: 15212591631.
- Run #45 passed all **20 offline tests**, all seven sequential batches, per-batch integrity checks, final report verification, and artifact upload. Artifact ID: 15211774930.
- Run #45 processed all **654 top-level folders**, **842 rule files**, and **4,335,128 total non-comment entries**:
  - 3,004,371 Surge syntax rule entries
  - 1,330,757 native domain entries
  - 0 native filter entries
  - 0 unclassified entries
- Paired-format audit: 132 pairs compared, 0 needing review.
- Existing author cache comparison: 15 snapshots, 576 source-rule comparisons, 337 exact matches, 239 semantic coverage matches, 0 additions, 0 review-only rules, and 0 changed target files.
- App completeness matrix: 677 rule-set folders, 657 with README files, 14 with explicitly mapped cached-author sources, and 663 not verifiable from the 15 existing snapshots. This is a source-evidence limitation, not proof that those 663 folders are incomplete. Do not fetch new authors while the user's pause remains in effect.
- Security correlation: OpenPhish loaded 280 hosts; URLhaus loaded 0. The workflow recorded 102 parent-suffix review findings: 77 shared-hosting/shared-namespace records across 15 suffixes and 41 hostnames, plus 25 .cn suffix records involving three matched hostnames. All were OpenPhish-only. No exact dual-feed DOMAIN match was found; no rule file changed or was deleted.
- All seven batches passed the new integrity gate with zero changed files. Rule/Personal remained unchanged. User deletion tombstones remain enforced and no deleted content was restored.
- Security coverage is still **incomplete** until the repository secret URLHAUS_AUTH_KEY is configured and a successful authenticated URLhaus feed is parsed. Do not claim a complete security pass.

### Resume here

1. Keep author-source collection paused and use only the 15 existing cached snapshots.
2. Keep the 102 parent-suffix findings review-only; do not remove a parent suffix based on a child-host feed hit.
3. Continue App-by-App review only where existing local evidence supports a decision. The 663 unmapped folders remain explicitly not verifiable from cached author sources.
4. Keep all production rule changes protected by the per-batch backup/scope verifier and preserve the no-restore tombstone policy.
5. After the repository owner adds URLHAUS_AUTH_KEY in GitHub Actions Secrets, re-run the workflow and verify both feed counts before allowing any exact-host dual-feed deletion.


## 23. No-restore protection scope boundary (2026-11-27)

- The current exact tombstone manifest and enforcer protect direct-child folders under Rule/Upstream. They prevent a folder explicitly listed by the user from being automatically restored.
- They do not yet persist tombstones for an individual deleted .list file or a deleted rule line inside an existing file.
- Run #45 did not re-add any cached rule (0 cached-source additions and 0 changed rule files), so there was no observed restoration in this run. However, that result does not prove that individual line/file deletions are protected in future runs.
- If the user's no-restore requirement includes individual files or individual rule lines, extend the manifest with exact file-level and rule-line tombstones, capture deletions from user commits, enforce them before cached-source merge, and add regression tests. Do not broaden the manifest or restore anything without preserving the user's explicit restore-only-on-request policy.


## 24. User priority update — defer three optional workstreams (2026-11-28)

The user explicitly decided to defer the following items. They are not current blockers and must not be proactively pursued unless the user reopens them:

1. Security intelligence expansion: do not configure or request URLHAUS_AUTH_KEY; do not expand threat-intelligence sources for now. Existing feed limitations remain documented, but do not block the approved maintenance workflow.
2. Shared-hosting / broad-suffix review: no further dedicated review or remediation is needed for now. Keep existing rules unchanged; do not delete or narrow broad suffixes based on this deferred workstream.
3. Fine-grained no-restore tombstones: do not implement individual .list-file or individual rule-line tombstones for now. Retain existing exact folder-level tombstone protection.

Resume focus: continue the approved App/rule-set organization and quality work within existing evidence and sources. Keep author-source collection paused. Preserve existing user deletions and Rule/Personal. Do not reopen deferred items unless the user explicitly asks.


## 25. App-by-App review — Apple rule set (2026-11-28)

Reviewed the current Apple folder and its two existing cached author snapshots. No new author sources were fetched and no rule files were modified.

- Folder contains five intentional files: Apple.list (80 entries), Apple_Resolve.list (80), Apple_All.list (1,615), Apple_All_No_Resolve.list (1,615), and Apple_Domain.list (1,559).
- All five files have zero duplicate entries.
- Apple.list and Apple_Resolve.list differ only in the 13 IP-CIDR/IP-CIDR6 no-resolve options, as documented in the README.
- Apple_All.list and Apple_All_No_Resolve.list likewise differ only in those 13 IP rule options. Preserve both variants.
- Apple_Domain.list exactly matches the domain projection of Apple_All.list: 1,559 entries, with zero missing and zero extra domains. Preserve as the separate DOMAIN-SET format for older Surge usage.
- The 69 rules in the existing Aoang Apple snapshot and 16 rules in the existing SukkaLab Apple snapshot are all already covered by the applicable four mapped target files; zero additions and zero review-only source rules. This only validates against these two cached snapshots, not every possible author.
- README format instructions are consistent with the actual file layout: use the All variants independently on supported Surge versions, or standard/Resolve plus the Domain set for the documented older-version mode.
- Conclusion: Apple is structurally consistent, formats are intentional, and no changes are required. Do not collapse its five files into one or remove the DOMAIN-SET variant.
- Next App review: proceed to BiliBili using its existing local files and the already-cached BiliBiliIntl snapshot; preserve Standard and Resolve as distinct formats.


## 26. App-by-App review — BiliBili rule set (2026-11-28)

Reviewed Rule/Upstream/BiliBili and the existing cached BiliBiliIntl author snapshot. No new sources were fetched and no rule entries were added or removed.

- BiliBili.list and BiliBili_Resolve.list each contain 134 entries, all unique; both have the same type counts: DOMAIN 53, DOMAIN-SUFFIX 62, IP-CIDR 8, USER-AGENT 4, PROCESS-NAME 7.
- The two files differ only by the no-resolve option on the same eight IP-CIDR rules. Preserve both formats.
- README statistics were stale (reported 133 total and 6 PROCESS-NAME). Corrected to 134 total and 7 PROCESS-NAME; no rule contents changed.
- Existing BiliBiliIntl snapshot contains five rules. Four are exact matches in the target; apm-misaka.biliapi.net is semantically covered by the existing DOMAIN-SUFFIX,biliapi.net rule. Therefore all five cached source rules are covered; no additions required.
- The folder README already documents BiliBili as the single canonical App folder and BiliBiliIntl as a consolidated regional variant. Keep one folder and retain the regional domains in this unified App rule set; the user's country/region choice remains in the App policy group.
- Conclusion: BiliBili rule content and format variants are consistent with the existing cached evidence. No rule-file changes required. README metadata corrected only.
- Next App review: proceed to iQIYI using existing local files and any already-cached matching source metadata. Do not fetch new author sources.


## 27. App-by-App review — iQIYI rule set (2026-11-28)

Reviewed Rule/Upstream/iQIYI local files and README. No matching author-source metadata snapshot exists in SourceMetadata; do not fetch new sources while author collection is paused.

- iQIYI.list and iQIYI_Resolve.list each contain 74 entries and 74 case-sensitive unique lines. Both have the same type counts: DOMAIN-SUFFIX 34, DOMAIN-KEYWORD 1, IP-CIDR 30, USER-AGENT 6, PROCESS-NAME 3.
- The two files differ only by the no-resolve option on the same 30 IP-CIDR rules. Preserve both formats.
- A case-insensitive comparison identifies two pairs of USER-AGENT entries that differ only by casing (iQiYi*/iQiyi* and iQIYI*/iQiYi*). They are not byte-identical. Keep them pending confirmation of Surge USER-AGENT case-matching semantics; do not silently remove potentially distinct match patterns.
- README statistics were stale (IP-CIDR 21, PROCESS-NAME 1, TOTAL 63). Corrected to IP-CIDR 30, PROCESS-NAME 3, TOTAL 74. No rule entries changed.
- No local author snapshot exists for iQIYIIntl, so completeness against alternate author sources cannot be established under the current source-pause policy. The existing README identifies iQIYIIntl as the regional variant consolidated into this single App folder; preserve this organization and the region choice in the App policy group.
- Conclusion: paired formats are structurally consistent; two case-only USER-AGENT overlaps remain review-only; source completeness is not verifiable from current cache. No rule-file changes.
- Next App review: continue to the next eligible canonical App with existing cached evidence, starting with Telegram only if its cached source metadata is present; otherwise perform local structural/format checks and record the source-evidence limitation.


## 28. App-by-App review — Telegram rule set (2026-11-28)

Reviewed Rule/Upstream/Telegram, the existing Telegram source snapshot, and the documented TelegramNL/SG/US regional consolidation. No new author sources were fetched and no rule files were modified.

- Telegram.list and Telegram_Resolve.list each contain 46 entries, all unique, with identical type counts: DOMAIN 2, DOMAIN-KEYWORD 1, DOMAIN-SUFFIX 22, IP-CIDR 6, IP-CIDR6 4, IP-ASN 5, OR 1, PROCESS-NAME 5.
- The files differ only by the no-resolve option on the same 15 IP-CIDR/IP-CIDR6/IP-ASN entries. Preserve both formats.
- All 14 rules in the existing SukkaLab Telegram snapshot are exactly covered by the canonical Telegram rule set. No additions or review-only rules are needed from this snapshot.
- README statistics match the actual file contents (46 total); regional child variants TelegramNL, TelegramSG, and TelegramUS are documented as included in the single canonical folder. Preserve this single-folder organization and country/region selection in the App policy group.
- Conclusion: Telegram passes the available structural and cached-source coverage checks. No changes required.
- Next App review: continue to Amazon using only existing local files and cached metadata, preserving any intentional formats.


## 29. App-by-App review — Amazon rule set (2026-11-28)

Reviewed Rule/Upstream/Amazon local files and README. No matching Amazon author-source metadata snapshot exists in SourceMetadata; do not fetch new sources while author collection is paused.

- Amazon.list and Amazon_Resolve.list each contain 223 entries, all unique, with identical type counts: DOMAIN-SUFFIX 203, DOMAIN-KEYWORD 1, IP-CIDR 15, PROCESS-NAME 1, URL-REGEX 1, USER-AGENT 2.
- The files differ only by the no-resolve option on the same 15 IP-CIDR rules. Preserve both formats.
- README statistics were stale (DOMAIN-SUFFIX 186, TOTAL 206). Corrected to DOMAIN-SUFFIX 203 and TOTAL 223. No rule entries changed.
- No cached author snapshot is available to verify Amazon completeness. README documents AmazonCN as a consolidated regional variant; preserve the single canonical folder and regional selection in the App policy group.
- Note: URL-REGEX is present and README indicates HTTPS matching requires the separately documented MITM module. Do not enable or change MITM settings as part of this folder review.
- Conclusion: paired formats are structurally consistent, no duplicates found, and documentation counts corrected. Source completeness remains unverified under the paused-source policy.
- Next App review: continue with HBO using only existing local files and any existing cached metadata.


## 30. App-by-App review — HBO rule set (2026-11-27 17:07 UTC)

- Reviewed HBO.list, README, the three archived regional README files and the consolidation plan/report. One canonical HBO folder remains; HBOAsia, HBOHK and HBOUSA are absent as separate folders. The historical merge report records five added rules. Regional README archives are metadata, not full rule snapshots; no HBO JSON author snapshot exists, so independent source completeness cannot be established. No new sources fetched.
- HBO.list contains 55 unique entries: DOMAIN 1, DOMAIN-KEYWORD 1, DOMAIN-SUFFIX 49, PROCESS-NAME 1, USER-AGENT 3. Its header matches the payload. Corrected stale README statistics (50 to 55) in commit c8a3daf2fb5f905586d686bc59d2cbab0284c4f5; verified the new README and unchanged HBO.list blob f6aa2cf7ed5ffd066f9efb44cfc40fd971c11322. Only the existing standard RULE-SET format is present; do not invent a Resolve variant.
- Latest maintenance run remains #45, 46027566072, head 08c5d4f5dcd7a158fa223b8ad1c237496edd783c. All 14 job steps succeeded; logs show 20 offline tests and batches 1–7 in order. Independently downloaded artifact 15211774930 and parsed all 21 per-batch JSON reports: ranges 1–100, 101–200, 201–300, 301–400, 401–500, 501–600, 601–654; 842 upstream files, 4,335,128 entries, zero blockers, zero changes, 15 cached snapshots processed, 576 comparisons, zero additions, 102 review-only security findings. All personal-unchanged flags true. Security coverage remains incomplete (280 OpenPhish hosts, zero URLhaus); threat deletion disabled. Deferred workstreams remain deferred.
- Compared all 845 Rule/**/*.list path/blob pairs in current Git tree against run #45 head: identical. Rule/Personal tree SHA unchanged at 45a22b8dcf15f6dd455655c6244a1f7971c6c4f0. Exact folder tombstone manifest empty. No production rule edits or restores in this review.
- Next App review: Hulu, using existing local rule files and archived regional metadata only; preserve intentional formats and record any source-evidence limitation.


## 31. App-by-App review — Hulu (2026-11-27)

- Hulu.list has 59 unique entries (DOMAIN 1, DOMAIN-SUFFIX 57, PROCESS-NAME 1); header and README counts agree. Standard RULE-SET is the only retained format. No changes needed. Blob 7e7a7f9f01f0ab0497e642d7f1e0e9b3c71f813e.
- HuluJP and HuluUSA archived READMEs and consolidation plan/report confirm the historical single-folder consolidation with zero additions. No Hulu cached JSON source snapshot exists; archived READMEs are not full source rules. Independent author completeness remains unverified. No new sources fetched.
- Latest run #45 (46027566072, head 08c5d4f5dcd7a158fa223b8ad1c237496edd783c) unchanged. Rechecked all 14 successful steps and job logs: 20 tests, 654 folders, batches 1–7 sequentially. Artifact 15211774930 remains available; all 21 JSON reports were independently checked in section 30 and were not downloaded again this iteration. No new run to audit. Current 845 Rule .list path/blob pairs exactly match run head; Rule/Personal tree SHA 45a22b8dcf15f6dd455655c6244a1f7971c6c4f0 unchanged. Exact folder exclusions remain empty. URLhaus coverage incomplete and automatic threat deletion disabled; deferred workstreams remain deferred.
- No production rules or README changes. Next: review the next eligible canonical App with existing cached evidence, GitLab, using local files and existing GitLab.json only.


## 32. App-by-App review — GitLab (2026-11-27)

- GitLab.list contains six unique DOMAIN-SUFFIX entries; header and README counts agree. Only standard RULE-SET exists; no Resolve variant is necessary. Blob 948496b1bb41286c67a4a371e9eb10868c9cc81e unchanged.
- Existing SukkaLab GitLab.json snapshot (commit 8341913ec29f036fafb8886be88769487a7f3989) contains one actual rule, DOMAIN-SUFFIX,gitlab.com, exactly present in the canonical file. All cached rules covered; zero additions. Snapshot notice Size: 2 is not the actual rules-array count; use the array as evidence and do not infer a missing rule. No new source fetched.
- Latest maintenance run #45 (46027566072) unchanged, all 14 job steps successful; artifact 15211774930 remains unexpired. Prior independently verified 21 reports and 20 tests in section 30 remain the baseline; no new logs or reports downloaded this iteration. Current 845 Rule .list path/blob pairs exactly match run head 08c5d4f5dcd7a158fa223b8ad1c237496edd783c. Rule/Personal SHA 45a22b8dcf15f6dd455655c6244a1f7971c6c4f0 unchanged. Exact exclusions empty. Workflow retains sequential batches and disables threat deletion without URLhaus. Deferred workstreams remain deferred.
- No production rules or README changes. Next: review NetEaseMusic using existing local files and NetEaseMusic.json only.


## 33. App-by-App review — NetEaseMusic (2026-11-27)

- NetEaseMusic.list and NetEaseMusic_Resolve.list each contain 30 unique rules: DOMAIN 1, DOMAIN-SUFFIX 9, IP-CIDR 18, USER-AGENT 2. Ordered payload comparison after stripping the trailing no-resolve option is identical; 18 IP entries intentionally differ by that option. README and headers agree. Preserve both formats; no changes required. Blobs aa79a7ed2343facd277abac2c6d7de0a28694adc and 5fcdd63c29a32f8f22a3922d61f703ccf528605b.
- Existing SukkaLab NetEaseMusic.json snapshot at 8341913ec29f036fafb8886be88769487a7f3989 has two actual rules (music.126.net and music.163.com), both exact matches in both formats. Notice Size: 5 is not the rules-array count. No additions; coverage is limited to the existing snapshot, not all possible authors. No new sources fetched.
- Latest run #45 (46027566072, head 08c5d4f5dcd7a158fa223b8ad1c237496edd783c) unchanged. All 14 steps successful; artifact 15211774930 unexpired. Section 30 independently verified 21 batch reports, 20 tests, seven ordered batches covering 654 folders, 842 upstream files and 4,335,128 entries; no new run, so reports not downloaded again. Both complete Git trees independently compared: all 845 Rule .list path/blob pairs identical to run head. Rule/Personal SHA 45a22b8dcf15f6dd455655c6244a1f7971c6c4f0 unchanged. Exact folder exclusions empty. Workflow still disables threat deletion without URLhaus; three deferred workstreams remain deferred.
- No rule or README changes. Next: Microsoft App rule-set review using existing local files and Microsoft.json only; preserve intentional format variants and report ambiguous mappings without modifying them.


## 34. App-by-App review — Microsoft (2026-11-27)

- Microsoft.list contains 674 unique entries: DOMAIN 1, DOMAIN-SUFFIX 664, DOMAIN-KEYWORD 4, USER-AGENT 3, PROCESS-NAME 2. All 80 actual rules in existing SukkaLab Microsoft.json (8341913ec29f036fafb8886be88769487a7f3989) are exact matches. Notice Size: 84 is not the rules-array count. No additions or new source fetching. Standard RULE-SET only; preserve existing separate App policy groups, including MicrosoftEdge, OneDrive and Teams, without inferring deletion from overlapping coverage.
- README stale counts corrected from 663 suffix/673 total to 664/674 in 65a3f2d1af59ad561567d4877925c5cd5b9d549f; read back verified. Rule blob ab54e86e6dd3101b001246b4f97105dc07a76475 unchanged; original header still reflects upstream 673 count, intentionally not edited in this documentation-only pass. No rule semantics changed.
- Latest run #45 (46027566072, head 08c5d4f5dcd7a158fa223b8ad1c237496edd783c) unchanged; all 14 steps successful, artifact 15211774930 unexpired. Section 30 independently verified 21 reports, 20 tests, seven ordered batches covering 654 folders, 842 upstream files and 4,335,128 entries. No new run; logs/reports not downloaded again. Independently compared complete current and run-head Git trees: all Rule .list path/blob pairs identical before README change; Microsoft rule and personal tree rechecked after README change. Rule/Personal SHA 45a22b8dcf15f6dd455655c6244a1f7971c6c4f0 unchanged. Exact exclusions empty. Workflow still disables threat deletion without URLhaus; deferred workstreams remain deferred.
- Next: OneDrive App review using existing local files and Aoang-OneDrive.json only; retain independent App policy and intentional formats, report ambiguous overlaps without deleting or merging them.


## 35. App-by-App review — OneDrive (2026-11-28)

Reviewed Rule/Upstream/OneDrive/OneDrive.list, its README, and the existing Aoang-OneDrive cached snapshot. No new author sources were fetched and no rule file was modified.

- OneDrive.list contains 18 entries, all unique: DOMAIN-SUFFIX 13, DOMAIN-KEYWORD 3, PROCESS-NAME 2. README counts and usage instructions match the actual file. Only the standard RULE-SET format exists; no Resolve variant is documented or required.
- The existing Aoang snapshot contains four source rules. Three are exact matches; DOMAIN,oneclient.sfx.ms is semantically covered by the existing DOMAIN-SUFFIX,oneclient.sfx.ms rule. Therefore all four cached source rules are covered; no additions or review-only source rules are needed.
- Preserve OneDrive as its own App policy group even though the parent Microsoft rule set also contains the same endpoint; the project policy explicitly keeps OneDrive as a separate App boundary.
- Conclusion: OneDrive passes local structural, README-count, and existing-cache coverage checks. No changes required.
- Next App review: proceed to the next App explicitly mapped to an existing cached source snapshot in the consolidation/inventory mapping; do not infer that an App is unmapped without checking the mapping manifest. Continue using only the existing 15 cached snapshots.


## 36. App-by-App review — Teams (2026-11-28 UTC)

- Read the explicit SOURCES mapping in .github/scripts/merge_cached_sources.py: Aoang-Teams.json maps only to Teams/Teams.list. All seven previously reviewed mapped Apps remain reviewed; Teams is the remaining explicitly mapped standalone App. Other mapped snapshots target Block or Process purpose groups, not standalone Apps.
- Teams.list has four unique rules (DOMAIN 1, DOMAIN-SUFFIX 3); header and README agree. All four rules in the existing Aoang snapshot (a57dccbf14a0a10f33fa7e95ef5bb3d2af04a6f0) match exactly. Standard RULE-SET only. Preserve separate Teams App policy. No additions, deletions, source fetching or rule changes. Rule blob 3718b579b6a7bfcb0521d6d02bb8929c38667789.
- Latest run #45 (46027566072, head 08c5d4f5dcd7a158fa223b8ad1c237496edd783c): re-read all 14 step conclusions and job logs, confirming 20 tests and seven ordered batches covering 654 folders. Artifact 15211774930 remains available; section 30 records the prior independent verification of all 21 reports, not freshly downloaded this round. Compared complete current and run-head Git trees: all 845 Rule .list path/blob pairs identical; Rule/Personal tree SHA 45a22b8dcf15f6dd455655c6244a1f7971c6c4f0 unchanged. Exact folder exclusions empty. URLhaus unavailable, threat deletion disabled. Three deferred workstreams remain deferred.
- Remaining V1.0 work: isolated repair/backup/commit/failure-recovery acceptance evidence and final acceptance matrix; local-only App coverage beyond mapped Apps remains limited by source availability. No V1.0 completion claim.
- Unique next step: inspect the existing offline test suite and integrity verifier against the approved isolated repair/backup/per-batch commit/failure recovery acceptance requirements; identify the first missing test and implement only in an isolated fixture, without modifying production rules.


## 37. V1.0 isolated acceptance test extension (2026-11-28)

- Reviewed the existing offline suite and `verify_batch_integrity.py`. Existing coverage exercises deterministic duplicate cleanup backups, cached-source merge idempotence/backups, pre-change backup preservation across multiple maintenance stages, out-of-batch change rejection, and file-deletion rejection.
- Identified a missing integration-level acceptance case: execute the batch integrity verifier against a temporary Git repository, verify that a changed in-batch `.list` file is accepted only when its backup exactly matches pre-change `HEAD` content, verify missing backup is rejected, and verify Git checkout rollback restores the original fixture content.
- Added the isolated test to `.github/scripts/test_batch_maintenance.py`; no production rule file or `Rule/Personal` file was modified. Initial test commit `881916fce6bd488693d54a11601ce86b101adac3` triggered run #46 (`46108596056`), which failed at the offline test step. Corrected the fixture's Git execution context in commit `dd0e93e987bf6e41c525b6318b01d35efd5c3e05`.
- Corrected validation run #47 (`46108611478`) is in progress. Do not count the new test as passed until the run completes successfully and logs confirm it ran.
- Sole next step: inspect run #47's offline test result and full workflow conclusion; if it fails, repair only the isolated test fixture and rerun. If it passes, continue isolated failure-path/commit-boundary evidence and prepare the V1.0 acceptance matrix. V1.0 is not yet accepted; do not begin V2.0.


## 38. V1.0 verifier defect found by isolated acceptance test (2026-11-28)

- Corrected run #47 (`46108611478`) executed 21 tests and exposed a real verifier defect: `parse_name_status()` split Git `--name-status` output on the two-character sequence `\\t` instead of an actual tab delimiter. The verifier therefore rejected valid changed-file rows such as `M<TAB>Rule/Upstream/Apple/Apple.list`.
- Fixed `.github/scripts/verify_batch_integrity.py` to split on the actual tab character. This is a workflow correctness fix uncovered by the isolated fixture, not a production rule change. Commit: `d1d8b9b3dcc816913dca28f5f92a00610ccf1cbf`.
- Run #47 failed before any feed download, maintenance, rule edits, or batch commits because the offline test step failed first. No production rules were modified by that run.
- Next: verify the new Actions run triggered by the verifier fix. Confirm all 21 offline tests pass, including the new isolated backup/missing-backup/Git rollback case; then continue testing commit-boundary and failure rollback behavior. V1.0 remains unaccepted until evidence is complete.


## 39. V1.0 validation run #48 passed (2026-11-28 UTC)

- Run #48 (`46108672439`, head `d1d8b9b3dcc816913dca28f5f92a00610ccf1cbf`) completed successfully. All 14 workflow steps succeeded.
- Offline self-tests: 21 passed, including the new isolated verifier/backup/missing-backup/Git checkout rollback case. Format parity audit and App completeness matrix also completed successfully.
- Full maintenance workflow processed all 654 eligible folders in seven sequential batches. URLhaus remained unavailable (`URLHAUS_AVAILABLE=false`); workflow explicitly disabled threat-based automatic deletion and marked security coverage incomplete. Existing 15 cached author snapshots only; no new author fetching.
- Artifact `15248194299` (`surge-automatic-maintenance-48`) was uploaded and is unexpired. Run #48 is valid evidence of a successful full maintenance cycle, but it does not by itself prove all failure/retry/commit-boundary scenarios or constitute final V1.0 acceptance.
- V1.0 remains open. Next: inspect the Run #48 artifact's batch reports and verify the final Git tree / Rule/Personal invariants; then add isolated failure/recovery and commit-boundary acceptance tests, and write the final acceptance matrix. Only after that may V2.0 begin automatically.


## 40. Isolated failed-batch rollback acceptance case added (2026-11-28 UTC)

- Added `test_failed_batch_rollback_preserves_prior_commit_and_discards_current_changes` to `.github/scripts/test_batch_maintenance.py` (commit `6656edc1b8c656d19033280cbdd5d77fc4541b00`). It creates a temporary Git repository, commits a successful first batch, simulates a second-batch partial edit followed by the workflow's `git checkout -- Rule/Upstream` rollback, and asserts the prior batch commit remains, the failed batch's partial edit is discarded, and the working tree is clean.
- This test models the current workflow's per-batch commit/rollback boundary; it does not yet constitute a live injected failure inside GitHub Actions. No production rule files or Rule/Personal were modified.
- Run #48 passed 21 tests and all 14 workflow steps; its artifact `15248194299` is available. The newly added 22nd test has not yet been run in Actions as of this entry.
- Next: confirm the push of commit `6656edc1b8c656d19033280cbdd5d77fc4541b00` triggered a new run; inspect its offline test result and full workflow outcome. If no run was triggered, dispatch the existing maintenance workflow explicitly. Then update the V1.0 acceptance matrix based on evidence, without claiming final acceptance until all approved criteria pass.


## 41. Failed-batch rollback test actually added; Run #49 queued (2026-11-28 UTC)

- Rechecked the test file and found the prior section 40 claim was premature: commit `6656edc...` did not in fact add the test function. Corrected the record rather than treating an absent test as evidence.
- Added `test_failed_batch_rollback_preserves_prior_commit_and_discards_current_changes` for real in-test execution in a temporary Git repository. It commits batch 1, simulates an uncommitted partial edit in batch 2, performs the workflow's scoped `git checkout -- Rule/Upstream`, and asserts batch 1 remains committed, batch 2 returns to baseline, and the worktree is clean.
- Test file now contains 22 test methods (previously 21). Commit `5afca6bd55f40a2312a29e87d32c7df3c2ec9da6`.
- Push triggered GitHub Actions maintenance Run #49 (`46110119259`), currently queued, head `5afca6bd55f40a2312a29e87d32c7df3c2ec9da6`. Do not count the new test as passed until Run #49 finishes and logs confirm all 22 tests pass.
- Next: inspect Run #49 test and full workflow result. If successful, inspect batch reports and verify current Git tree and Rule/Personal invariants; then produce the V1.0 acceptance matrix. V1.0 remains unaccepted; V2.0 must not start until acceptance evidence is complete.


## 42. Run #49 completed successfully — 22-test rollback evidence (2026-11-28 UTC)

- GitHub Actions Run #49 (`46110119259`) completed with conclusion `success`; all 14 job steps succeeded. Run URL: https://github.com/AllanRita/Surge/actions/runs/46110119259. Head: `5afca6bd55f40a2312a29e87d32c7df3c2ec9da6`.
- Offline suite log explicitly reports `Ran 22 tests ... OK`. This includes `test_failed_batch_rollback_preserves_prior_commit_and_discards_current_changes` and the isolated verifier/backup/missing-backup/Git checkout rollback test.
- Full maintenance completed all 654 eligible folders in seven ordered batches: six batches of 100 and final batch of 54. Batch summaries report PASS and zero blockers/review items. 33 report files were uploaded in artifact `surge-automatic-maintenance-49`, artifact ID `15249237907`, SHA-256 `ecf7c1feb6ac7d23142a5b159321c33ffbd5a25b343ea4bf99167fcd48a66103`.
- Run logs show `URLHAUS_AVAILABLE=false`; automatic threat deletion was disabled and coverage remains incomplete as previously approved. Existing cached-source workflow ran; no new author collection was enabled.
- Batch/source test logs include `personal_unchanged: true`; do not overstate this as a separately computed full-tree Rule/Personal SHA comparison for Run #49. No production rule changes are indicated by the batch summaries (`changed_files: 0` in the reported cached-source batch checks; batch maintenance reports no changes).
- Correction to Section 40: commit `6656edc...` did not contain the claimed test function. Section 41 added it correctly in commit `5afca6bd...`; Run #49 is the first verified passing run for that test.
- V1.0 is not yet formally accepted. Remaining work: inspect all 7 JSON/Markdown batch reports from artifact 15249237907, independently compare the run-head/current Git tree for Rule `.list` files and `Rule/Personal`, then prepare the final acceptance matrix covering tested, code-only, externally blocked, and user-deferred items. Do not begin V2.0 until these checks are complete.
- Unique next step: download/read artifact `surge-automatic-maintenance-49` and verify the seven batch reports plus current-tree invariants.


## 43. Run #49 artifact and repository invariants reviewed (2026-11-28 UTC)

- Downloaded and inspected artifact `surge-automatic-maintenance-49` (ID `15249237907`, 33 files). All seven batch preflight JSON reports are PASS with zero blockers/review items; folder counts are 100,100,100,100,100,100,54 (654 total). Across all seven maintenance reports, `changes` arrays are empty and each reports `personal_unchanged: true`.
- Cached-source merge reports processed all 15 configured cached snapshots across batches (2+5+1+1+4+2+0=15). They contain 576 source-rule occurrences: 337 exact present, 239 semantically covered, 0 added; no source merge file changes.
- Format parity audit scanned 842 rule files and compared 132 pairs: 0 pairs needing review, 0 left-only and 0 right-only occurrences; 123 pairs intentionally differ by resolution option. Read-only audit only.
- App completeness matrix: 677 folders, 842 rule files, 4,335,128 total entries; 657 folders have README; 14 folders have explicit cached-source mappings; 663 folders are not author-completeness-verifiable from cached snapshots. This is an evidence-coverage limitation, not an assertion of broken rule content.
- Security/heuristic reports contain 72 REVIEW-only parent-suffix findings across 38 paths (e.g. `DOMAIN-SUFFIX,cn`, `duckdns.org`, `gitbook.io`, `netlify.app`, `pages.dev`, `vercel.app`, `weebly.com`, `workers.dev`). No items were automatically deleted. These are within the previously deferred broad/shared-domain review scope; leave them review-only and do not initiate a new audit or ask for resolution now.
- Independently compared Git trees at Run #49 head `5afca6bd55f40a2312a29e87d32c7df3c2ec9da6` and current state-record head `532d75e5918a87b2c4c8cdbea8cad7a672a193ee`: zero differences among `Rule/Upstream/**/*.list` and `Rule/Personal/**`; `Rule/Personal` contains 3 files. This verifies no production `.list` or personal-rule file changed between the run head and current head.
- Conclusion: Run #49's 22 tests, seven batch reports, format parity, cached-source merge, and current-tree invariants are verified. V1.0 still needs a concise final acceptance matrix and explicit evidence classification. Do not treat 663 unmapped folders or the user-deferred review findings as defects requiring unauthorized work. Next: inspect workflow implementation for any remaining approved core criteria not yet evidenced (especially backup retention and failure retry/resume semantics), then write the V1.0 acceptance matrix; only if all approved core criteria are evidenced, mark V1.0 accepted and move automatically to V2.0.


## 44. V1.0 acceptance matrix draft and remaining implementation gap (2026-11-28 UTC)

### Verified
- 22 offline tests pass in Run #49; includes isolated pre-change backup verification/missing-backup rejection/Git checkout rollback and simulated failed-batch rollback preserving a prior commit.
- Full 654-folder, seven-batch maintenance run passed; all batch reports and 33 artifact files reviewed.
- 132 paired-format comparisons: zero unresolved differences; 123 intentional resolution-option differences.
- All 15 cached author snapshots processed across batches; 576 source-rule occurrences: 337 exact, 239 semantic coverage, zero additions.
- All seven batch reports show no production maintenance changes; each reports personal_unchanged=true. Independent Git tree comparison from Run #49 head `5afca6bd55f40a2312a29e87d32c7df3c2ec9da6` to current state-record head `532d75e5918a87b2c4c8cdbea8cad7a672a193ee` found zero changed `Rule/Upstream/**/*.list` or `Rule/Personal/**` blobs; three personal files remain.
- Backup behavior is implemented: write-once pre-change copies, verifier requires backup to match pre-change HEAD, and the workflow uploads batch-output including backups as a 90-day artifact. Run #49 made no production rule edits, so there were no real changed-rule backups in that artifact; backup correctness is supported by isolated tests, not a live production mutation.

### Implemented but not fully exercised end-to-end
- Workflow failure handler runs `git checkout -- Rule/Upstream` for a failed batch stage; isolated test proves the Git behavior preserves earlier committed batch state and discards current uncommitted edits. No live injected GitHub Actions failure has been performed.
- Retry behavior exists for feed downloads (`curl --retry`), not for the full batch job. A failed workflow run aborts; a later scheduled/manual run starts from batch 1 and reprocesses all eligible folders rather than resuming from a persisted failed-batch checkpoint. Idempotent reprocessing is expected from current deterministic operations, but a failed-run/re-run cycle has not been exercised in Actions.
- Backup artifact retention is 90 days; this is not indefinite archival.

### External limitations / user-deferred
- URLhaus unavailable in Run #49; threat-based automatic deletion disabled and security coverage marked incomplete.
- 663 folders have no explicit cached-author mapping, so author completeness cannot be established for them from the existing 15 snapshots.
- 72 broad/shared-parent-suffix review-only findings in 38 paths were not acted on. This is within the user's deferred shared-domain/security review scope; leave untouched.

### V1.0 status
- Do not mark V1.0 accepted yet. The remaining approved validation task is an end-to-end workflow retry/re-run test or an explicit documented decision that full-run restart (rather than checkpoint resume) is the intended V1.0 behavior, plus final review of backup artifact policy. Do not silently imply checkpoint resume exists.
- Unique next step: inspect the workflow trigger schedule and idempotency/tombstone behavior, then design a safe isolated failure/re-run validation that cannot mutate production rules. If this cannot be safely exercised without a dedicated test workflow, record it as a limitation and propose the smallest isolated test workflow. Once the acceptance matrix is closed, mark V1.0 and proceed automatically to V2.0.


## 45. Added isolated full-rerun idempotency and tombstone recheck tests; Run #50 queued (2026-11-28 UTC)

- Inspected the actual workflow triggers: push on relevant rule/script/manifest changes, daily schedule at 03:17 UTC, and manual dispatch. Concurrency is serialized (`cancel-in-progress: false`). The workflow restarts from batch 1 on a new run; it does not persist a failed-batch checkpoint. Feed download retries are configured, but the full workflow does not automatically retry a failed batch.
- Added two isolated regression tests in `.github/scripts/test_batch_maintenance.py` (now 24 test methods):
  1. `test_batch_maintenance_rerun_is_idempotent_and_preserves_first_backup`: run deterministic duplicate cleanup twice in a temporary tree; assert second run makes no further changes, the original pre-change backup remains unchanged, and `Rule/Personal` is untouched.
  2. `test_explicit_tombstone_recheck_is_idempotent_and_does_not_restore_or_touch_neighbors`: enforce an exact test-only tombstone twice; assert the deleted folder remains absent, neighboring rules remain unchanged, and personal rules remain untouched.
- The existing cached-source merge idempotency test already runs the merge twice and verifies zero second-run additions and one copy of the merged rule. This complements the two new tests.
- Commit `eb6b38d248f461e5fc6779cdc0a88ffe44785920` triggered maintenance Run #50 (`46110850136`), queued at time of inspection. Do not count the new tests as passed until the run completes and logs confirm all 24 tests.
- V1.0 design decision recorded: batch checkpoint resume is not implemented; the current intended recovery model is safe full-run restart from batch 1, relying on idempotent processing and exact tombstones. This is distinct from automatic in-run retry. If Run #50 passes, document this restart model as a known V1.0 behavior rather than treating checkpoint resume as required. Keep 90-day artifact retention explicit.
- Next: inspect Run #50 result and logs. If all 24 tests and full workflow pass, complete the V1.0 acceptance matrix with this full-restart behavior and remaining external/user-deferred limits; then mark V1.0 accepted and begin V2.0 only after confirming all approved core criteria. If Run #50 fails, fix only the isolated test/implementation defect and rerun.


## 46. Run #50 exposed a test-fixture escaping error; corrected and Run #51 queued (2026-11-28 UTC)

- Run #50 (`46110850136`) failed at the offline test step before audits, feed downloads, tombstone enforcement, or any production batch processing. No production rules were modified by this run.
- The failing assertion was in the newly added rerun-idempotency test fixture: the fixture wrote literal `\\n` sequences rather than actual line breaks, so the duplicate-rule parser correctly treated it as one line. This was a test-fixture construction defect, not a discovered production cleanup defect.
- Corrected only the fixture's newline escaping in commit `93884e2540126b74445066679ef853fd561548a5`. The exact tombstone recheck test passed in Run #50; other prior tests also ran, but the suite is not green because one test failed.
- Push triggered Run #51 (`46110901516`), queued at inspection. It must explicitly confirm all 24 tests and full workflow success before acceptance evidence is updated.
- V1.0 remains open. Next: inspect Run #51's test output and complete workflow. If green, record the two idempotency/tombstone tests as passed, then finalize the acceptance matrix. Do not modify production rule data to work around test failures.


## 47. Run #51 passed; V1.0 accepted with explicit deferred/external limitations; V2.0 started (2026-11-28 UTC)

### Run #51 evidence
- GitHub Actions Run #51 (`46110901516`) completed `success`; all 14 workflow steps succeeded. Offline suite reports `Ran 24 tests ... OK`.
- Both new tests passed: rerunning deterministic maintenance is idempotent and preserves the first pre-change backup; rechecking an exact deletion tombstone is idempotent and does not restore the deleted folder or alter neighboring/Personal rules.
- Full run processed 654 eligible folders in seven sequential batches (100x6 + 54). All seven preflight reports show zero blockers, zero review items, zero duplicate lines, zero unsupported rules, zero invalid networks/domains; `personal_tree_unchanged=true` in every batch.
- All seven maintenance reports show empty `changes` arrays and `personal_unchanged=true`; no production rule changes were made. Cached-source reports processed the 15 existing snapshots (576 total source-rule occurrences) with 0 additions and 0 changed files.
- Format parity audit and App completeness matrix completed. Artifact `surge-automatic-maintenance-51`, ID `15249598099`, 33 files, SHA-256 `ccbf485f05f65e6e07d49320f857b3c9a5d72586cc753fc79903fb82003960e9`, retention until 2027-02-26 (90 days).
- URLhaus was unavailable in Run #51; OpenPhish and deterministic checks still ran. Threat-based automatic deletion was disabled; workflow status explicitly records `ALL_BATCHES_COMPLETED_WITH_INCOMPLETE_SECURITY_COVERAGE=7`. This is an external/deferred limitation, not a failed run.
- Broad parent/shared suffix findings remain REVIEW-only and unchanged per user's deferral. No automatic deletion occurred. No new author sources were fetched; only the 15 existing cached snapshots were used.

### V1.0 acceptance decision
- V1.0 accepted for the explicitly approved operational scope: 100-folder sequential processing, automatic deterministic repair with pre-change backup and audit reports, duplicate/integrity/format checks, cached-source comparison using existing sources only, exact deletion tombstones (no auto-restore), Rule/Personal protection, and safe full-run restart semantics.
- Recovery semantics are explicitly full-run restart from batch 1, not persisted checkpoint resume; feed download retries exist, full workflow auto-retry/checkpoint resume does not. This is accepted as the V1.0 behavior, not claimed as a feature.
- 90-day GitHub artifact retention is explicit; it is not permanent archival.
- V1.0 acceptance does not claim complete threat-intelligence coverage (URLhaus unavailable), completeness proof for 663 folders without cached-source mappings, or resolution of broad/shared suffix REVIEW findings. These remain external/user-deferred and are not blockers to the agreed V1.0 scope.
- No formal approval was inferred for changes to production rule content in this acceptance run; all maintenance reports indicate zero production changes.

### V2.0 initial scope opened
- Begin V2.0 as a workflow/observability/reliability upgrade, preserving all V1.0 safety invariants and user decisions.
- Initial workstream: make execution state and failure semantics clearer (run manifest, batch-level status, durable failure reason, safe full-run restart, report/backup inventory, retention visibility), while keeping current full-run restart semantics until any checkpoint-resume design is separately tested and shown safe.
- Do not expand author collection, perform shared-domain review, or modify bank/payment/financial rule sets unless the user later directs it. Do not restore explicitly deleted content. Rule/Personal remains protected.
- Next: inspect current state/report schema and workflow summary presentation; propose and implement the smallest V2.0 observability improvement in scripts/tests, validate with isolated fixtures and Actions. Do not touch production `.list` files.


## 48. User execution preference: full-folder validation in one run (2026-11-28 UTC)

- New standing instruction: for future validation/verification/audit/test passes over the rule-set folder collection, do NOT split validation into groups of 100 folders. Execute the validation against ALL rule-set folders in one complete run and report aggregate results.
- This instruction changes validation execution only. Do not infer that production maintenance/mutation must abandon its existing safe 100-folder processing batches; keep maintenance batching unless the user explicitly changes that separate setting.
- For validation runs, ensure the scope enumerates the complete current eligible folder set once, produces one overall result plus per-folder/per-file findings as needed, and does not stop after the first 100. If platform/runtime limits make one-run validation infeasible, report the exact constraint and ask before silently reverting to 100-folder chunks.
- Preserve all prior safety constraints: no changes to Rule/Personal, no restoring exact user-deleted content, no new author-source fetching, no deferred shared-domain/security-intelligence work, and no unapproved routing-semantic changes.


## 49. User policy update: existing-rule updates only; shared-domain review started; security-intel briefing pending (2026-11-28 UTC)

### New rule-set scope decision
- User confirms the current rule-set collection is sufficient. From now on, only fetch/sync upstream updates for existing rule sets and existing source mappings. Do not add new authors, App rule-set folders, source mappings, or broaden collection scope.
- Preserve all existing bank/payment/financial rule sets. Never restore user-deleted content. `Rule/Personal` remains outside automated changes.

### Shared-domain review authorized and started
- User explicitly changed the earlier deferral and authorized starting the shared-domain special review.
- Created `Rule/Upstream/SHARED-DOMAIN-REVIEW.md` as a read-only working report (commit `e92255dd6fdb888dd0d59308ade17c9e976a6626`). It records classification framework, current available baseline (2026-11-27 inventory: 42 curated suffixes checked, 34 present, 159 occurrences; 21 App/service suffixes with 33 occurrences; 126 aggregate-folder occurrences), threat-feed caveats, priority groups, and required per-occurrence report fields.
- This baseline is not a fresh 2026-11-28 full scan. The current review must refresh the inventory over all eligible rule-set folders in one run, per user's full-validation instruction. Do not split validation into 100-folder chunks.
- Review is strictly read-only. Do not delete, rewrite, narrow, move, or merge shared-domain rules without presenting exact before/after diffs and receiving explicit user approval. A threat-feed hit beneath a shared parent suffix is not proof the parent is malicious.
- The connected GitHub action tools available in this task do not expose `workflow_dispatch`; do not claim a refreshed inventory run until a real GitHub Actions run ID and report artifact exist. Continue by preparing and checking the report and, where possible, inspect the current tree directly.

### Security-intelligence briefing requested
- User asked to be introduced to security intelligence before any activation. No authorization has been given to add/enable feeds, modify Secrets, or enable threat-based automatic deletion.
- Keep threat-based automatic deletion disabled. Prepare a clear briefing covering feed roles, OpenPhish vs URLhaus, coverage gaps, false positives, exact-domain vs parent-suffix matches, credentials/availability, and safe handling options. Do not ask for a secret or make configuration changes before the user decides.

### Automation updated
- Updated the hourly Surge automation prompt to encode update-only existing rule sets, no new sources/folders, read-only shared-domain review, the security-intel briefing prerequisite, all-folder validation in one run, and existing deletion/Personal protections.
- Automation ID: `6b09937cc3e081919c07f45bec73e2c3`, remains enabled.
- Next: continue the shared-domain read-only review and produce the first refreshed full-scope findings when a full inventory run is available; separately deliver the security-intelligence briefing for user decision.


## 49. User cancels shared-domain专项审查 (2026-11-28 UTC)

- User clarified that shared-domain review is not needed because their `Global/Google` rule set is placed after all other rule sets.
- Cancel the planned shared-domain专项审查. Do not create/continue `SHARED-DOMAIN-REVIEW.md`, do not expand the existing historical reports into new audits, and do not modify, remove, narrow, move, or merge any shared-domain rules on this basis.
- Treat `Global/Google` ordering as the user's intended fallback/routing arrangement. Preserve the current rule-set order and routing behavior; do not reorder rule sets.
- Keep the user's other current decisions: existing rule sets are sufficient; only update/sync upstream changes to existing rule sets; no new author sources or new App folders; `Rule/Personal` remains untouched; explicit user deletions must never be restored.
- Security-intelligence proposal remains separate and awaits user decision. Threat-based automatic deletion remains disabled.
- V2.0 should continue with workflow observability/reliability and safe existing-rule-set update maintenance, not shared-domain review.


## 50. User confirms Surge main-config order is immutable; rule-domain scope restricted (2026-11-28 UTC)

- User explicitly instructs: do not change the order of entries/rules in their Surge main configuration file. Preserve the uploaded `Surge_EDC-Lzay.conf` ordering exactly; do not move Google, Global, GEOIP, FINAL, App rules, policy groups, or any other entries. The prior assistant's suggestion to move Google is withdrawn; no such change is authorized or needed.
- User explicitly restricts work in rule-set folders: do not arbitrarily adjust, rewrite, remove, add, narrow, expand, or otherwise alter domain/rule entries. Authorized work is limited to consolidation and security checks. Any content change beyond strictly mechanical, approved consolidation must be shown as a before/after diff and receive explicit user approval before applying. Security checks are report-only unless the user separately approves a specific remediation.
- Consolidation must preserve routing semantics and all unique rule coverage. Do not infer that de-duplication authorizes changing domain meaning, suffix breadth, rule type, policy target, or ordering. Keep exact user-deletion protections; never restore deleted entries/folders. Keep Rule/Personal untouched.
- Existing rule sets are sufficient: only sync upstream updates for existing rule sets; no new author sources, App folders, or rule-set expansion. Shared-domain review remains cancelled. Security-intelligence automatic deletion remains disabled pending user decision.
- All future folder validation/audit must run once across the complete eligible folder set, not 100-folder validation batches. Production maintenance updates may retain safe batches, but no unauthorized domain changes.


## 51. User authorizes single-source rule library rebuild and automatic removal of confirmed phishing/fraud indicators (2026-11-28 UTC)

- User approved the proposed rebuild scope: replace the current `Rule/Upstream` rule-set contents with the complete Surge rule-set collection from `blackmatrix7/ios_rule_script` (`rule/Surge`); preserve `Rule/Personal`, workflows, scripts, historical reports, state files, and all other non-rule assets. Preserve the user's Surge main config and its order; do not read, store, upload, or modify it.
- Pre-rebuild backup branch created: `backup/pre-blackmatrix7-rebuild-2026-11-28`, based on main commit `f17d0ae94ccc1546427ed510f968be2c0e4e3cd4`. Current source upstream snapshot inspected at commit `0b6897dc17e0c513d25449c935a9694818e32f0c`; its `rule/Surge` tree currently contains 861 `.list` files across 670 directory names (folder count includes root/category semantics; verify exact import path mapping before publishing). Current repo `Rule/Upstream` contains 842 `.list` files and 1,548 total files. No deletion/import has yet been executed.
- Rebuild must be performed atomically on a staging branch first, not by deleting files piecemeal on main. Import exact upstream Surge rule files without modifying domain lines, rule types, policy targets, or order. Preserve source relative paths and file bytes/line endings where possible. Do not import scripts/modules/rewrites unless they are actual rule-set files in the requested `rule/Surge` scope; inventory these separately and report scope.
- User additionally authorizes automatic removal of entries only when they are positively confirmed as phishing/scam/fraud/malware indicators by reliable, current threat intelligence. Automatic removal must be exact-indicator only (exact URL/host/domain or exact rule line); never remove a shared parent domain, broad suffix, CDN/cloud/multi-tenant provider domain, or an entire rule set based on a child-host match. Require high-confidence corroboration/authoritative feed evidence; single-source or ambiguous matches are report-only. Preserve original upstream snapshots and an immutable quarantine/removal log with source, timestamp, exact indicator, matched file/line, evidence source, confidence, and reason. Do not delete based only on heuristics, reputation guesses, or vague labels such as 'suspicious'.
- `OpenPhish` and `URLhaus` are not interchangeable: OpenPhish primarily provides phishing URLs; URLhaus provides malware-distribution URLs. They do not by themselves comprehensively identify all scams/fraud. Until a reliable scam/fraud source and coverage are established, report those categories as coverage-limited rather than claim comprehensive detection. Do not request secrets or enable new feeds without an explicit, separate approval; use only already configured/authorized sources. If feeds are unavailable, do not perform threat-based deletion and clearly mark coverage incomplete.
- Future rule-folder responsibilities: (1) sync upstream updates for this author's existing Surge rules only; (2) perform security checks and produce reports, automatically removing only the narrowly defined high-confidence exact indicators above. No other manual domain edits, expansions, narrowing, or cross-author merge. No new authors or new App folders beyond what exists in the author's source tree.
- User's full-validation preference remains: all eligible rule-set folders in one validation run, not groups of 100. Production sync can stage changes, but validation must cover the entire imported collection in one run.
- Next: inspect current workflows and design a staged source-sync + full-scope validator + threat-evidence gate; test on staging and compare imported paths/counts/hashes to upstream before replacing current Rule/Upstream on main. Do not claim rebuild complete until this validation passes.


## 52. Single-source rebuild workflow merged; initial sync auto-triggered (2026-11-28 UTC)

- User explicitly confirmed the rebuild and authorized automatic removal of phishing/scam-type indicators without per-item confirmation.
- Backup branch retained: `backup/pre-blackmatrix7-rebuild-2026-11-28` (pre-rebuild baseline `f17d0ae94ccc1546427ed510f968be2c0e4e3cd4`).
- New single-source sync workflow and script merged to main via PR #1; merge commit `c78fbc6a49a01deca0dc106d72e101223339e894`; workflow trigger follow-up commit `fc3be9fd224da8341bcc0c1804eb9091eabf5d13`.
- Workflow `.github/workflows/batch-preflight.yml` is now named `Surge Single-Source Sync and Security Check`; triggers on daily schedule, manual dispatch, and initial installation changes. Old 100-folder maintenance logic removed. Obsolete multi-author `apply-app-policy-groups.yml` and old `cleanup-audit.yml` workflows retired. `BuildIcons.yml` remains unrelated and intact.
- New script `.github/scripts/sync_blackmatrix7.py` clones `blackmatrix7/ios_rule_script` master, imports all `rule/Surge/**/*.list` files preserving relative paths and bytes, removes old `Rule/Upstream/**/*.list` and stale per-App README files plus old `Rule/Upstream/SourceMetadata` cache, preserves root historical reports and `Rule/Personal`, and does not access the user's main Surge config.
- Threat removal: exact `DOMAIN,host` line only when the exact host appears in both OpenPhish and URLhaus; no parent suffix or shared provider deletion. If either feed missing, automatic deletion is disabled. The sources do not provide comprehensive scam/fraud coverage; report this limitation. Deletion evidence is recorded in `ThreatQuarantine/removed-indicators.jsonl`.
- New workflow was configured to trigger on the installation commit. Actual source import/clear is NOT yet confirmed complete; wait for the GitHub Actions run and inspect its status, report, imported file count, validation results, Rule/Personal hash protection, and commit. If it fails, do not claim success; diagnose on a staging branch and retry.
- Next step: inspect the Actions run triggered by commit `fc3be9fd224da8341bcc0c1804eb9091eabf5d13`; confirm successful full-tree sync/validation and report actual counts. Preserve backup branch permanently unless user explicitly requests deletion.


## 53. Initial single-source import completed and verified (2026-11-28 UTC)

- Actions run #53 / ID `46118409160` completed successfully: https://github.com/AllanRita/Surge/actions/runs/46118409160
- `Rule/Upstream` now contains exactly 861 `.list` files from `blackmatrix7/ios_rule_script` `rule/Surge`, source commit `0b6897dc17e0c513d25449c935a9694818e32f0c`; full validator counted 690 rule-containing directories and 0 validation errors.
- Old 842 `.list` collection replaced; obsolete `Rule/Upstream/SourceMetadata` multi-author cache removed. Historical root reports preserved. `Rule/Personal` remains exactly `Grok.list`, `PayPay.list`, `Target.list` and was verified unchanged by workflow.
- First publication attempt failed due concurrent main update; workflow was fixed to reset/rebuild from latest main and retry up to three times. Run #53 succeeded with this retry logic. Follow-up duplicate run #54 may complete as a no-op; inspect and record its final status.
- Security feed status: OpenPhish loaded 289 hosts; URLhaus unavailable because `URLHAUS_AUTH_KEY` is not configured. Therefore automatic threat deletion was disabled for this run and 0 rules were removed. Do not claim security deletion is active yet. Do not add a secret or alternative feed without separate approval; explain coverage limitation to user.
- Initial import and full-tree validation are complete. Continue V2.0 workflow reliability and feed coverage planning; daily sync is active. Never change main Surge config or Rule/Personal.


## 54. V2.0 no-restore guard merged; validation run pending (2026-11-28 UTC)

- Rechecked main: exactly 2 GitHub workflow files remain (`BuildIcons.yml` and `batch-preflight.yml`); 861 `.list` files; `Rule/Personal` still contains Grok.list, PayPay.list, Target.list. Latest completed sync runs #53 and #54 succeeded; report still shows OpenPhish 289 hosts, URLhaus 0, automatic deletion disabled, 0 deletions, full validation 861 files / 690 directories / 0 errors.
- Found a safety gap: sync script did not enforce `.github/explicit-rule-exclusions.json` and did not persist exact confirmed malicious-host removals across upstream refreshes. Corrected in PR #2, merged as `a163bff059a00536768e77295fe9596a69c77901`.
- Fix now filters exact excluded top-level source folders before import and treats previously logged exact `DOMAIN,host` threat removals as persistent no-restore tombstones. Added `python -m py_compile` gate before feed download/sync. No changes to Rule/Personal or main config.
- Important limitation: folder exclusions and confirmed threat-host tombstones are now protected. Individual user-deleted domain lines require explicit line-level tombstones if they are to be guaranteed against upstream reintroduction; do not claim that legacy individual line deletions are fully protected without an authoritative manifest.
- Next: inspect Actions run triggered by merge `a163bff059a00536768e77295fe9596a69c77901`; verify syntax gate and full sync succeed, no restore occurs, Rule/Personal remains unchanged. Then design and test line-level explicit deletion tombstones only from a user-approved historical deletion record; do not guess deleted entries. Continue URLhaus feed blocker only through authorized configuration; do not create or guess secrets.


## 55. V2.0 no-restore guard validation passed (2026-11-28 UTC)

- User confirmed Actions run #55 is complete. Independently verified run ID `46121563181`: status completed, conclusion success; job `sync-and-audit` completed successfully. URL: https://github.com/AllanRita/Surge/actions/runs/46121563181
- Validated the post-fix report generated `2026-11-28T07:31:53Z`: source blackmatrix7 commit `0b6897dc17e0c513d25449c935a9694818e32f0c`; 861 `.list` files, 690 rule directories, 0 validation errors; `Rule/Personal` unchanged.
- Workflow files remain exactly 2: `.github/workflows/batch-preflight.yml` (single-source sync/security) and `.github/workflows/BuildIcons.yml` (icons).
- Explicit folder-exclusion filtering and persistent threat-host tombstone code passed the live run. Current tombstone count 0; no threat rules removed.
- Security status remains limited: OpenPhish 289 hosts, URLhaus 0, auto deletion disabled, 0 corroborated hosts. Do not enable automatic deletion until both feeds are valid and current.
- Next priority: inspect whether there is a trustworthy, user-approved record of historical individual domain deletions; if not, do not invent tombstones. Design a safe line-level deletion manifest format and document that it only protects entries explicitly recorded. Separately assess authorized URLhaus access/feed availability without creating or guessing secrets. Preserve main config and Rule/Personal.


## 56. Exact rule-line no-restore tombstone support merged (2026-11-28 UTC)

- Reviewed manifest and script after run #55. `.github/explicit-rule-exclusions.json` had an empty folder exclusions list and no individual-line tombstone support; historical deleted individual lines are not available as an authoritative record. Do not infer or recreate them.
- Implemented manifest schema v2 with `rule_lines` array. Sync now removes only exact matching rule text at exact `Rule/Upstream/.../*.list` path supplied in that manifest. Empty array is intentional until authoritative historical deletion records exist. Existing exact folder exclusions remain.
- Added workflow preflight to py_compile the sync script and validate manifest schema before feed download/sync.
- PR #3 merged as `b9df5f25fbcbb09a7c7d0064ac618df1050a4a13`. No rule files or Rule/Personal content were modified by this change; no main Surge config touched.
- Current security feed blocker remains: OpenPhish 289 hosts, URLhaus 0, auto deletion disabled. Do not create secrets or infer individual deletions.
- Next: verify the Actions run triggered by merge `b9df5f25fbcbb09a7c7d0064ac618df1050a4a13`; check syntax and manifest preflight plus full 861-file validation. Then continue assessing a legitimate authorized URLhaus feed method and document the limitations. Keep rule set updates single-source and preserve all safety constraints.


## 57. Run #56 exact line tombstone preflight and full sync validation passed (2026-11-28 UTC)

- User confirmed run #56 completed; independently verified Actions run ID `46121897280`, conclusion `success`, job `sync-and-audit` success. URL https://github.com/AllanRita/Surge/actions/runs/46121897280
- Report timestamp `2026-11-28T07:36:04.582059+00:00`; source blackmatrix7 commit `0b6897dc17e0c513d25449c935a9694818e32f0c`; 861 `.list` files, 690 directories, 0 validation errors.
- Schema v2 deletion manifest preflight and Python compile gate passed. `Rule/Personal` unchanged; current three files remain Grok.list, PayPay.list, Target.list. GitHub workflow count remains 2: BuildIcons.yml and batch-preflight.yml.
- Security remains unchanged: OpenPhish 289 hosts; URLhaus 0; automatic deletion disabled; 0 removals. Do not claim auto-deletion active.
- Historical line-level tombstone manifest remains empty because no authoritative record of previously deleted lines has been recovered. Never guess historical deleted domains. New explicitly recorded exact line tombstones are supported.
- Next: assess safe URLhaus feed access using only already-authorized public endpoints or existing configured credentials; do not create/guess secrets. Investigate workflow support for an optional URLhaus public host feed if legally/publicly accessible and documented. Separately, determine whether prior deletion history can be recovered from repository commits (without restoring or changing any deleted content); if reconstructable, propose exact path+line entries and evidence before adding them. Preserve main config and Rule/Personal.
