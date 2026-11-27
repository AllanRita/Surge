# Surge Project State

Last updated: 2026-11-27 13:43 UTC (21:43 Asia/Shanghai)
Repository: `AllanRita/Surge`
Default branch: `main`

> This file is the authoritative handoff note for future Surge work. At the start of every resumed session, read this file and the linked manifests before inspecting chat history. Do not restart completed analysis unless a source file or decision has changed.

## 1. Project priority

**Current priority: harden the workflows first, then process `Rule/Upstream` in deterministic batches of exactly 100 top-level rule-set folders.**

Run a read-only preflight on each batch, inspect the report, fix workflow/script issues, and only then approve any content remediation for that batch. Do not start the next batch until the current batch is reviewed and accepted.

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

- The latest user instruction says bank, payment, and other finance-related rule folders are **not to be deleted as a category** during the current rule-library optimization.
- Do not delete bank/payment/finance folders merely because their names or contents match a category.
- Do not delete financial/payment domains embedded in other Apps' rule sets.
- Never modify `Rule/Personal` without a direct, specific user instruction.
- Do not delete any other App folder or rule based only on overlap, shared infrastructure, threat-feed matches, or an automated classification.

## 4. Permanent no-restore policy

The repository has an exact tombstone manifest at `.github/explicit-rule-exclusions.json`. The automation in `.github/scripts/enforce_explicit_exclusions.py` enforces only entries still present in that manifest.

The user explicitly authorized restoration of all 14 historical exclusions on 2026-11-27. They were restored as current author-source rule files under `Rule/Upstream`: `BOC`, `BOCOM`, `CCB`, `CEB`, `CGB`, `CMB`, `ICBC`, `PSBC`, `AliPay`, `PayPal`, `Stripe`, `UnionPay`, `VISA`, `PingAn`. The 14 entries were removed from the exact tombstone manifest. All 14 files were re-verified in the current Git tree. Their restored folders must not be deleted again by category-based cleanup.

There is no unresolved disposition conflict for these 14: the latest explicit instruction restored all of them and they are no longer tombstoned. Do not re-delete them by category-based cleanup. Do not add new bank/payment/finance exclusions without a direct, specific user instruction. Any future exact tombstone can only be removed after an explicit restoration request for that folder. Git history is audit/recovery only, never automatic restoration authority.

## 5. Workflow responsibilities

Workflows must:
1. Enforce the exact tombstone manifest before and after inventory/consolidation.
2. Fail safely if the manifest is missing, malformed, or unsafe.
3. Never infer new deletions from category names or security matches.
4. Never restore tombstoned folders from upstream feeds, caches, snapshots, backups, or Git history.
5. Keep `Rule/Personal` outside automated remediation.
6. Clearly distinguish a failed/unavailable security feed from a clean result.

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
- 238 upstream financial-domain matches across 29 domain values remain untouched. Seven crypto/securities/finance review folders (322 rule entries) remain present and are not deletion targets.
- The three files in `Rule/Personal` remain untouched.
- The 14 historical exclusions were subsequently explicitly restored by the user on 2026-11-27; see Section 9. They are not current tombstones.

## 7. Next work — resume here

1. Finish workflow hardening and validate the new batch preflight implementation.
2. Run Batch 1 (first 100 eligible top-level folders in deterministic case-insensitive alphabetical order) in read-only mode.
3. Review all blockers and review-only findings; refine the validator based on real Batch 1 output.
4. Only after approval, perform any rule-content optimization for Batch 1. Keep a full change log and verify before/after rule counts and protected paths.
5. Repeat with batches 2, 3, and onward, exactly 100 folders each (final batch may contain fewer), without starting the next batch before the current one passes review.
6. Keep broad new-author fetching paused; compare cached snapshots. Do not modify `Rule/Personal`.
7. Do not repeat completed 14-group consolidation or earlier audit work unless source files or decisions change.
8. At the end of each batch, update this file with folder range, files/rules checked, paths changed, checks, findings, and next batch.

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
- Follow-up: compare these 14 against other established author sources, inspect rule safety and completeness, then update the audit inventory. Do not delete the restored folders.


## 10. Workflow-first and 100-folder batch protocol (2026-11-27)

- User directed that workflow problems be optimized first, then run the project library in batches of 100 rule-set folders, continuously refining between batches.
- Current tree count: 666 direct child folders under `Rule/Upstream`; 665 eligible top-level folders after excluding `SourceMetadata`.
- Added `.github/scripts/batch_preflight.py`: deterministic alphabetical 100-folder read-only validator. It checks UTF-8 readability, symlinks, duplicate rule lines, unsupported/missing rule operands, invalid IP networks, invalid domain operands, hidden control characters, broad single-label suffixes (review only), exact tombstones, and a before/after digest of `Rule/Personal`. It does not edit or delete rules.
- Added `.github/workflows/batch-preflight.yml`: manual `workflow_dispatch`, batch number input, fixed batch size 100, read-only repository permission, serialized concurrency, and 30-day report artifact.
- Disabled automatic push triggers on the previous full-library audit and App-consolidation workflows. They now require manual dispatch; this prevents every rule-file push from starting an unbounded full-library job.
- Removed the automatic call to `remove_invalid_public_tld_rules.py` from the audit workflow. Broad-TLD findings must be review-only; the workflow must not silently delete rules as part of an audit.
- First trial target: Batch 1, first 100 eligible folders sorted by casefolded folder name. No batch preflight has been run yet; the workflow is prepared but must be manually dispatched from GitHub Actions because this connection supports reading/writing repository files and reading runs, but not dispatching a new workflow.
- Legacy Apply App Policy-Group Consolidation run #16 completed successfully at 2026-11-27 13:46 UTC against commit `5c51d488ed2ec5e6aad296454f4d7e4a4fa21a00`, before the push trigger was removed. It was not the new 100-folder trial. Do not treat it as batch approval.
- Do not run the full consolidation workflow as part of batch preflight. Do not merge or delete any folder during preflight.
- The 14 restored bank/payment/finance folders are verified present; the tombstone manifest is empty. The exclusion enforcer accepts an empty list safely.
- Next action: dispatch `Surge 100-Folder Batch Trial` with `batch_number=1`, inspect its JSON/Markdown artifact, fix the validator/workflow based on actual output, then decide whether Batch 1 is approved for any content changes.
