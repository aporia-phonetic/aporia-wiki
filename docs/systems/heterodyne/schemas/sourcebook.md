# sourcebook

*Source: `heterodyne/schemas/sourcebook.py`*

schemas.sourcebook — Typed models for the world/season sourcebook.

Replaces the untyped dicts agents/sourcebook_compiler.py used to pass around
directly. The narrative pass (agents.sourcebook_compiler.generate_world_narrative)
is an LLM call, so its output is validated *permissively* here — a faction
missing suit/power_tier, or a slightly malformed narrative response, degrades
gracefully (matching this module's existing "fully non-fatal" design) rather
than raising and aborting the whole sourcebook compile.

Nothing here is a hard gate: SourcebookCompiler still writes a sourcebook
even when the LLM narrative pass fails or returns something unexpected.

## Defined here

### `Faction`

One standing power in a world's present-day (or season-era) situation.

| Field | Type |
|---|---|
| `name` | `str` |
| `description` | `str` |
| `agenda` | `str` |
| `suit` | `Optional[str]` |
| `power_tier` | `Optional[str]` |

### `PresentDayNarrative`

The Claude narrative pass's output -- present-day situation, factions,
power map, and story-ready tensions/hooks. Empty/default when the
narrative pass was skipped or failed (run_narrative=False or a
non-fatal exception in generate_world_narrative).

| Field | Type |
|---|---|
| `present_situation` | `str` |
| `factions` | `list[Faction]` |
| `power_map` | `str` |
| `open_tensions` | `list[str]` |
| `story_hooks` | `list[str]` |

### `ACESStats`

| Field | Type |
|---|---|
| `athletics` | `int` |
| `cunning` | `int` |
| `eloquence` | `int` |
| `strange` | `int` |

### `NPCArchetype`

A deterministic ACES stat block -- for a real character
(agents.aces_mechanics.build_stat_block) or an abstract faction/era
figure with no CharacterIdentity backing it
(agents.aces_mechanics.archetype_stat_block).

| Field | Type |
|---|---|
| `name` | `str` |
| `archetype` | `str` |
| `species` | `str` |
| `suit` | `str` |
| `affinity_domain` | `str` |
| `resonance_school` | `str` |
| `flaw` | `str` |
| `aces_stats` | `ACESStats` |
| `total_power` | `int` |
| `difficulty` | `str` |
| `physical` | `dict[str, Any]` |
| `catchphrases` | `list[str]` |
| `voice_description` | `str` |
| `npc_role` | `str` |
| `encounter_notes` | `str` |
| `power_tier` | `Optional[str]` |
| `description` | `Optional[str]` |
| `origin` | `str` |

### `SourcebookMechanics`

The mechanics half of the merged sourcebook -- currently just
faction-derived NPC archetypes; figure-derived archetypes are additive
to this same list, not a separate section.

| Field | Type |
|---|---|
| `npc_archetypes` | `list[NPCArchetype]` |

### `Sourcebook`

The full compiled sourcebook -- world (or season-era) lore + mechanics.

World-level compiles (season_number=None) omit season_number/target_year
entirely, matching the pre-existing on-disk shape exactly (no schema
migration needed for future world-level sourcebooks).

| Field | Type |
|---|---|
| `world_id` | `str` |
| `world_name` | `str` |
| `genre` | `str` |
| `description` | `str` |
| `magic_system` | `str` |
| `tone_descriptors` | `list[str]` |
| `available_species` | `list[str]` |
| `present_day` | `PresentDayNarrative` |
| `history_digest` | `str` |
| `mechanics` | `SourcebookMechanics` |
| `season_number` | `Optional[int]` |
| `target_year` | `Optional[int]` |
