# story_seed

*Source: `heterodyne/schemas/story_seed.py`*

schemas.story_seed — The thin "story" entity in the World / Character / Story split.

A StorySeed is everything a season needs *on top of* an already-built world and
a registry of portable characters. It does three things and nothing more:

  1. References a built world (world_id) and a distribution channel.
  2. Declares its cast by role — primary / secondary / tertiary — pointing at
     global character ids (schemas.character_identity), with an optional
     per-character memory bridge for crossovers.
  3. Specifies world deltas — what this story needs *added to* or *changed in*
     the world for the season (a new location, a faction in motion, an artifact
     surfacing), without rewriting the world's foundation.

Plus the plot gates: the story-shape commitments the season must hit.

SeasonConfig / EpisodeConfig remain the runtime "mold", but are now derived
*from* a StorySeed rather than being the seed. Persisted to
data/worlds/{world_id}/seasons/season_NN/story_seed.json.

Engine core only — never imports from gui/. PlotGate mirrors gui.state.PlotGate
(plus a stable `id`) so the two round-trip without a cross-layer import.

## Defined here

### `CastTier`

How central a character is to this season's story.

PRIMARY   — always live; the Dramatist keeps them available every segment.
SECONDARY — recurring; surface on the gates/episodes they're tied to.
TERTIARY  — incidental; appear only where a gate explicitly needs them.

### `CastRole`

A character's casting in this season, by global id and tier.

| Field | Type |
|---|---|
| `character_id` | `str` |
| `tier` | `CastTier` |
| `memory_bridge_from` | `Optional[str]` |
| `generate` | `bool` |

### `WorldDelta`

An additive/altering change the story needs in the world for this season.

| Field | Type |
|---|---|
| `kind` | `Literal['add', 'change']` |
| `category` | `str` |
| `name` | `str` |
| `description` | `str` |

### `PlotGate`

One story-shape commitment the season must hit.

| Field | Type |
|---|---|
| `id` | `str` |
| `episode` | `int` |
| `title` | `str` |
| `dramatic_function` | `str` |
| `closing_hook` | `str` |

### `StorySeed`

The story layer: a season's references, cast roles, deltas, and gates.

| Field | Type |
|---|---|
| `season_number` | `int` |
| `world_id` | `str` |
| `channel_id` | `str` |
| `title` | `str` |
| `logline` | `str` |
| `plot_gates` | `list[PlotGate]` |
| `cast` | `list[CastRole]` |
| `world_deltas` | `list[WorldDelta]` |
| `temporal_position` | `Optional[TemporalPosition]` |
| `created_at` | `str` |
