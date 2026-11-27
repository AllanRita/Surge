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

- Current upstream library: 828 `.list` files, 663 App/category folders, and 640 top-level folders.
- 107 multi-file folders were checked. Every folder has exactly one file per recognized format; there are no same-format duplicate files.
- The 14 canonical App folders all exist and all 19 approved alias folders are absent. The plan has 0 exact duplicate candidates and the audit has no unapproved identical-content candidates. Its 19 cross-App overlap pairs and 2 separate-scope groups remain explicitly keep-separate; the 3 All / All_No_Resolve pairs also remain separate by design.
- The 2 byte-identical groups and 3 same-payload groups are intentional `All` / `All_No_Resolve` format pairs in AdGuardSDNSFilter, ChinaMaxNoIP, and EasyPrivacy. Keep each format separately; do not delete these pairs.
- 15 cached author snapshots (300 source rules) were compared against 26 mapped format targets. Missing source rules: 0. Missing format targets: 0. This only certifies the cached 15 snapshots, not every possible author.
- Static checks report 0 duplicate rule lines, 0 hidden control characters, 0 invalid native filters, 0 unsupported/missing operands, 0 invalid networks/domains, 0 IP-family mismatches, 0 catch-all networks, and 0 stale/private root suffixes.
- There are 894 bare public-TLD suffix rule occurrences across 78 values. They passed the current IANA delegation check; their routing breadth still needs scenario-aware review, not automatic deletion.
- OpenPhish loaded 280 domains and matched 77 rule rows across 15 hostnames and 15 parent-suffix rules. These are shared-hosting parent-suffix matches, not proof that the parent suffix itself is malicious. No parent suffix was removed.
- URLhaus was not loaded because `URLHAUS_AUTH_KEY` is unavailable. This is incomplete feed coverage, not a clean result.
- The library contains 34 curated shared-hosting suffixes across 159 rule occurrences.
- 238 upstream financial-domain matches across 29 domain values remain untouched by category-based rules. Seven crypto/securities/finance review folders (322 rule entries) remain present and are subject to the same evidence-based security policy as all other folders.
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
