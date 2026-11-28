# Surge Upstream Rule Sets

This directory is maintained from one upstream source only:

- Source: https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Surge
- Scope: Surge `.list` rule-set files only.
- Sync workflow: `.github/workflows/batch-preflight.yml` (daily schedule and manual dispatch).
- Security report: `SECURITY-SYNC-REPORT.json`.
- Threat-removal evidence: `ThreatQuarantine/removed-indicators.jsonl`.

The sync process mirrors upstream rule files without manual domain additions, narrowing, expansion, policy-target changes, or rule reordering. The report lists exact DOMAIN matches against OpenPhish with the file path, line number and hostname. Matches are reported for review. Existing explicit exclusions and recorded removals continue to apply.

`Rule/Personal`, the user's Surge main configuration, and its rule order are outside this workflow and must never be modified.
