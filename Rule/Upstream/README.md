# Surge Upstream Rule Sets

This directory is maintained from one upstream source only:

- Source: https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Surge
- Scope: Surge `.list` rule-set files only.
- Sync workflow: `.github/workflows/batch-preflight.yml` (daily schedule and manual dispatch).
- Security report: `SECURITY-SYNC-REPORT.json`.
- Threat-removal evidence: `ThreatQuarantine/removed-indicators.jsonl`.

The sync process mirrors upstream rule files without manual domain additions, narrowing, expansion, policy-target changes, or rule reordering. Exact phishing/malware host entries are removed only when the exact host is independently present in both configured OpenPhish and URLhaus feeds. If either feed is unavailable, automatic threat deletion is disabled for that run. Parent suffixes and shared hosting/provider domains are never deleted based on a child-host match.

OpenPhish and URLhaus do not provide comprehensive scam/fraud coverage. Security findings and feed coverage limitations are recorded in the report.

`Rule/Personal`, the user's Surge main configuration, and its rule order are outside this workflow and must never be modified.
