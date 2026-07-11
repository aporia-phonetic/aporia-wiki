# aces_mechanics

*Source: `heterodyne/agents/aces_mechanics.py`*

agents/aces_mechanics.py — Shared, dependency-free ACES stat-block mechanics.

Extracted from agents/game_designist.py, which originally computed these
deterministically (no LLM) as part of its per-episode VTT module packages.
game_designist.py re-exports everything here unchanged (a pure
extract-and-re-export refactor — its own behavior is untouched), so this
module can also be used by agents/sourcebook_compiler.py to generate
era-appropriate NPC archetypes for the world/season sourcebook, without
game_designist's episode/world_ledger/VTT-export dependencies.

Two kinds of stat block:
  - build_stat_block(char)      — from a real CharacterIdentity-shaped dict
                                   (has "aces" stats already).
  - archetype_stat_block(...)   — for an abstract faction/era figure that has
                                   no CharacterIdentity, only a narrative
                                   name/description/suit/power_tier. Baselines
                                   its ACES stats from TIER_ACES_BASELINE
                                   rather than a real character sheet.

Both are 100% deterministic — no LLM call for the stats themselves, matching
game_designist's original design principle (LLM is only ever used upstream,
if at all, to decide qualitative fields like suit/power_tier/description).

## Top-level functions

- **`infer_figure_suit_and_tier()`** — Deterministic suit/power_tier guess for a historical figure, from its
- **`infer_npc_role()`** — 
- **`build_stat_block()`** — Generate an ACES NPC stat block from CharacterIdentity data.
- **`archetype_stat_block()`** — Deterministic NPC archetype stat block for a faction/era figure —
