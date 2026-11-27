# Canonical same-app merge report

Generated during the validated upstream sync. Rule lines are unioned exactly; no legacy path is deleted.

| App | Scenario | Source rule occurrences | Unique merged rules | Exact duplicates collapsed | Canonical path | Legacy mirrors |
|---|---|---:|---:|---:|---|---|
| Assassin's Creed Odyssey | standard | 30 | 15 | 15 | Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list | Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list |

## Assassin's Creed Odyssey (standard)
- Canonical path: Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list
- Legacy paths mirrored: Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list
- Rule lines before merge: 30; after exact deduplication: 15
- Exact duplicate lines collapsed across inputs: 15
- Reason: Verified identical 15-rule payloads.
| Assassin's Creed Odyssey | resolve | 30 | 15 | 15 | Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list | Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list |

## Assassin's Creed Odyssey (resolve)
- Canonical path: Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list
- Legacy paths mirrored: Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list
- Rule lines before merge: 30; after exact deduplication: 15
- Exact duplicate lines collapsed across inputs: 15
- Reason: Verified identical 15-rule payloads; keep Resolve separate from Standard.
| Assassin's Creed Origins | standard | 32 | 16 | 16 | Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list | Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list |

## Assassin's Creed Origins (standard)
- Canonical path: Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list
- Legacy paths mirrored: Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list
- Rule lines before merge: 32; after exact deduplication: 16
- Exact duplicate lines collapsed across inputs: 16
- Reason: Verified identical 16-rule payloads.
| Assassin's Creed Origins | resolve | 32 | 16 | 16 | Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list | Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list |

## Assassin's Creed Origins (resolve)
- Canonical path: Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list
- Legacy paths mirrored: Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list
- Rule lines before merge: 32; after exact deduplication: 16
- Exact duplicate lines collapsed across inputs: 16
- Reason: Verified identical 16-rule payloads; keep Resolve separate from Standard.
| PChome | standard | 10 | 5 | 5 | Rule/Upstream/PChomeTW/PChomeTW.list | Rule/Upstream/PChome/PChome.list |

## PChome (standard)
- Canonical path: Rule/Upstream/PChomeTW/PChomeTW.list
- Legacy paths mirrored: Rule/Upstream/PChome/PChome.list
- Rule lines before merge: 10; after exact deduplication: 5
- Exact duplicate lines collapsed across inputs: 5
- Reason: Verified identical 5-rule payloads.
| GlobalScholar / Scholar | standard | 461 | 231 | 230 | Rule/Upstream/GlobalScholar/GlobalScholar.list | Rule/Upstream/Scholar/Scholar.list |

## GlobalScholar / Scholar (standard)
- Canonical path: Rule/Upstream/GlobalScholar/GlobalScholar.list
- Legacy paths mirrored: Rule/Upstream/Scholar/Scholar.list
- Rule lines before merge: 461; after exact deduplication: 231
- Exact duplicate lines collapsed across inputs: 230
- Reason: Upstream README documents Scholar as a contained sub-rule; union the locally missing cnki.net rule.
| Gemini / BardAI | standard | 23 | 14 | 9 | Rule/Upstream/Gemini/Gemini.list | Rule/Upstream/BardAI/BardAI.list |

## Gemini / BardAI (standard)
- Canonical path: Rule/Upstream/Gemini/Gemini.list
- Legacy paths mirrored: Rule/Upstream/BardAI/BardAI.list
- Rule lines before merge: 23; after exact deduplication: 14
- Exact duplicate lines collapsed across inputs: 9
- Reason: Upstream README documents BardAI as a contained sub-rule; preserve all exact rules from both names.
| ABEMA / AbemaTV | standard | 44 | 29 | 15 | Rule/Upstream/Abema/Abema.list | Rule/Upstream/AbemaTV/AbemaTV.list |

## ABEMA / AbemaTV (standard)
- Canonical path: Rule/Upstream/Abema/Abema.list
- Legacy paths mirrored: Rule/Upstream/AbemaTV/AbemaTV.list
- Rule lines before merge: 44; after exact deduplication: 29
- Exact duplicate lines collapsed across inputs: 15
- Reason: Same streaming service after the 2020 name change; combine the newer AbemaTV-specific rule types.

## Safety
- All inputs are required to exist; missing or unsafe files block publication.
- Only paths explicitly listed in Rule/CONSOLIDATION-PLAN.json are merged.
- Standard, Resolve, No-Resolve, No-IPv6, region, block, and routing scenarios remain distinct unless a group is explicitly approved.
- Each legacy file keeps its own NAME/header identity and receives the same merged rule payload as the canonical file.
- Personal rules are never read or modified.
- No legacy file is deleted.
