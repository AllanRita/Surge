# Surge Project State

Last updated: 2026-11-27
Repository: `AllanRita/Surge`
Default branch: `main`

> This file is the authoritative handoff note for future Surge work. At the start of every resumed session, read this file and the linked manifests before inspecting chat history. Do not restart completed analysis unless a source file or decision has changed.

## 1. Project priority

**Primary work: optimize the actual Surge rule-set folders and rule files under `Rule/Upstream`.**

GitHub Actions, scripts, inventories, and reports are supporting tools only. Do not let workflow maintenance displace the actual rule-file work.

## 2. Confirmed target structure

- One App = one canonical rule-set folder = one Surge policy group.
- Country/region selection belongs in the Surge policy group, not in duplicate country-specific App folders.
- Merge regional/author variants only when they are the same App and their rule semantics are compatible.
- Keep different Apps separate even if they share a CDN, parent company, login provider, or cloud platform.
- Compare already-cached author snapshots; do not fetch new authors while the collection pause is in force.
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

The repository currently has the exact tombstone manifest at `.github/explicit-rule-exclusions.json`. The automation in `.github/scripts/enforce_explicit_exclusions.py` enforces only those exact entries.

The current manifest lists these 14 historical exclusions:
`BOC`, `BOCOM`, `CCB`, `CEB`, `CGB`, `CMB`, `ICBC`, `PSBC`, `AliPay`, `PayPal`, `Stripe`, `UnionPay`, `VISA`, `PingAn`.

**Decision conflict requiring explicit resolution:** the repository's historical manifest/index records the 14 folders above as explicitly deleted at the user's direction on 2026-11-27. The user's latest instruction now says bank/payment/finance folders should not be deleted. Until the user explicitly clarifies the disposition of these exact 14 historical entries:
- Do not restore any of the 14.
- Do not add any new bank/payment/finance exclusions.
- Do not silently change the tombstone manifest.
- Continue protecting the exact existing tombstones from restoration by feeds, cached snapshots, backups, Git history, or automated jobs.
- Ask one concise clarification before changing the disposition of any of the 14.

A tombstoned folder may be restored only after the user explicitly requests restoration of that specific folder. Git history is a source for audit/recovery only, never automatic restoration authority.

## 5. Workflow responsibilities

Workflows must:
1. Enforce the exact tombstone manifest before and after inventory/consolidation.
2. Fail safely if the manifest is missing, malformed, or unsafe.
3. Never infer new deletions from category names or security matches.
4. Never restore tombstoned folders from upstream feeds, caches, snapshots, backups, or Git history.
5. Keep `Rule/Personal` outside automated remediation.
6. Clearly distinguish a failed/unavailable security feed from a clean result.

Workflow optimization is secondary to rule-set file optimization.

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

## 7. Next work — resume here

1. Start with the actual `Rule/Upstream` folders and `.list` files, not with workflow refactoring.
2. Inventory the current folders against `Rule/CONSOLIDATION-PLAN.json` and the latest inventory report.
3. Review App rule completeness using the already-cached `SourceMetadata` snapshots.
4. Compare every available format separately; do not mistake a Domain-only or other intentional format for an incomplete Standard/Resolve file.
5. Review duplicates and missing rules App by App. Make file edits only after semantic and security review.
6. Preserve all existing finance folders except the exact historical tombstones while their disposition remains unresolved.
7. After each completed batch, update this file with: paths changed, rules added/removed, checks performed, unresolved findings, and the exact next task.
8. Only after the rule files are in good shape, perform the final workflow hardening and end-to-end verification.

## 8. Session-resume protocol

At the start of every resumed session:
1. Read `SURGE-PROJECT-STATE.md`.
2. Read the exact tombstone manifest and the current consolidation plan.
3. Check the latest Git commit and only the files relevant to the recorded next task.
4. Continue from **Section 7**, without redoing completed work.
5. Update this file at the end of the work batch.

Do not claim work is complete based only on a green GitHub Actions status. Verify the actual rule files and the resulting Git tree.
