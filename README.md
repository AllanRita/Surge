# Surge Rule Library

This repository keeps the shared rule library separate from personal additions.

## Start here

- [Consolidated rule index](Rule/CONSOLIDATED-INDEX.md) — current App folders, supported formats, merge decisions, and old-path migration map.
- [Cleanup inventory](Rule/Upstream/CLEANUP-INVENTORY.md) — current file counts, duplicate checks, cached-source coverage, finance-folder review, and shared-hosting inventory.
- [Manual audit review](Rule/AUDIT-REVIEW.md) — interpretation of broad suffixes, financial-domain matches, cross-App boundaries, and validation limits.
- [Broad suffix scope review](Rule/Upstream/BROAD-SUFFIX-SCOPE-REVIEW.md) — 78 IANA-valid single-label suffixes classified by routing scope; review only, no automatic deletion.
- [Shared-hosting scope review](Rule/Upstream/SHARED-HOSTING-SCOPE-REVIEW.md) — 34 shared CDN/hosting suffixes and their App versus aggregate placement.
- [Security review](Rule/Upstream/SECURITY-REVIEW.md) — threat-feed matches and broad shared-hosting suffixes. Matches are review signals, not automatic deletion instructions.
- [App policy-group merge report](Rule/Upstream/APP-POLICY-MERGE-REPORT.md) — completed regional/alias consolidation.
- Paired-format parity audit — generated in each maintenance workflow artifact; checks compatible formats without changing rule files.

> **Visibility note:** This repository is public. Files under `Rule/Personal/` are therefore publicly readable too. Keep only entries you are comfortable publishing here; if those personal additions should remain private, store them in a separate private repository rather than changing this repository's visibility without checking subscription access.

## Folder structure

- `Rule/Upstream/` — consolidated upstream rule library. One App/service folder is the canonical location; distinct formats such as Standard and Resolve remain separate.
- `Rule/Personal/` — personal rule additions, kept separate from upstream imports and automated upstream cleanup.

## Maintenance boundaries

- New author rule-set imports are paused.
- Existing cached author snapshots may be compared, but no claim is made that every App has been compared against every possible author.
- Personal rule files are not rewritten by upstream consolidation.
- App consolidation is restricted to approved same-App/regional aliases and is guarded by the exact deletion manifest; deleted folders cannot be used as canonical or alias sources.
- The 14 dedicated bank/payment App folders are currently present in `Rule/Upstream`. The exact deletion manifest currently contains zero entries. No category-based keep/delete exemption exists; every App follows the same evidence-based security policy. Only a future exact user-directed deletion may create a tombstone. Matching domains in other rule sets are not removed by category.
- Shared CDN/hosting suffixes and threat-feed matches are reviewed manually; they are never deleted solely because of a feed match.
- Regional country/area selection belongs in the corresponding Surge policy group, not in separate regional App folders.
