# Additional-source merge coverage report

Generated: 2026-11-27 09:34 UTC

Coverage is measured against the final target rule list. Exact matches and matches covered by a parent DOMAIN-SUFFIX are distinguished. This is a static coverage check, not proof of routing correctness.

| Source contribution | License | Source rules | Exact | Parent suffix | Single-label suffix | Missing | Target |
|---|---:|---:|---:|---:|---:|---:|---|
| Aoang-Apple | MIT | 69 | 12 | 57 | 0 | 0 | Apple/Apple.list |
| Aoang-DNS | MIT | 53 | 53 | 0 | 0 | 0 | Block/DNS/DNS.list |
| Aoang-OneDrive | MIT | 4 | 2 | 2 | 0 | 0 | Microsoft/Microsoft.list |
| Aoang-Other | MIT | 1 | 1 | 0 | 0 | 0 | Block/Other/Other.list |
| Aoang-Parallels | MIT | 12 | 12 | 0 | 0 | 0 | Block/Parallels/Parallels.list |
| Aoang-Process | MIT | 23 | 23 | 0 | 0 | 0 | Process/Process/Process.list |
| Aoang-Teams | MIT | 4 | 0 | 4 | 0 | 0 | Microsoft/Microsoft.list |
| Aoang-Unavailable | MIT | 1 | 1 | 0 | 0 | 0 | Process/Unavailable/Unavailable.list |
| Aoang-YouTube | MIT | 15 | 15 | 0 | 0 | 0 | Block/YouTube/YouTube.list |
| Apple | AGPL-3.0 | 16 | 16 | 0 | 0 | 0 | Apple/Apple.list |
| BiliBiliIntl | AGPL-3.0 | 5 | 5 | 0 | 0 | 0 | BiliBiliIntl/BiliBiliIntl.list |
| GitLab | AGPL-3.0 | 1 | 1 | 0 | 0 | 0 | GitLab/GitLab.list |
| Microsoft | AGPL-3.0 | 80 | 80 | 0 | 0 | 0 | Microsoft/Microsoft.list |
| NetEaseMusic | AGPL-3.0 | 2 | 2 | 0 | 0 | 0 | NetEaseMusic/NetEaseMusic.list |
| Telegram | AGPL-3.0 | 14 | 14 | 0 | 0 | 0 | Telegram/Telegram.list |

## Interpretation
- A source rule covered by a parent suffix is already matched by the target list; it is not appended again.
- A source rule missing from the target is a supplementation candidate, not an automatic insertion. Confirm that it belongs to the same app and routing scenario first.
- Source licenses and provenance remain recorded in SourceMetadata.
- No personal rules are imported or merged.
