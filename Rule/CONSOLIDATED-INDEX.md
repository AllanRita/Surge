# Canonical Surge rule-set index

Updated: 2026-11-27

This index defines the single maintenance target for rule sets whose contents have been verified identical across upstream categories.

## Verified canonical targets

| App / rule set | Scenario | Canonical maintenance path | Legacy compatibility path |
|---|---|---|---|
| Assassin's Creed Odyssey | Standard | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list` | `Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list` |
| Assassin's Creed Odyssey | Resolve | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list` | `Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list` |
| Assassin's Creed Origins | Standard | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list` | `Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list` |
| Assassin's Creed Origins | Resolve | `Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list` | `Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list` |
| PChome | Standard | `Rule/Upstream/PChomeTW/PChomeTW.list` | `Rule/Upstream/PChome/PChome.list` |

## Maintenance rules

1. Edit and review only the canonical path for each row above.
2. Keep the legacy path available for existing raw-file subscription URLs.
3. When upstream sync refreshes either copy, compare rule bodies and restore byte-equivalent rule content before publication; never let two paths silently diverge.
4. Do not merge Standard and Resolve variants. Their resolution behavior is intentionally distinct.
5. Do not merge any file from `Rule/Personal/` into upstream or canonical app sets.
6. Remove a legacy path only after subscriber migration and explicit compatibility verification.

The machine-readable source of truth is `Rule/CONSOLIDATION-PLAN.json`.
