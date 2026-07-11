# channel

*Source: `heterodyne/schemas/channel.py`*

schemas.channel — Distribution channel presets.

A Channel is a structural preset that bundles the production "shape" of a
season: how many episodes, how long each one runs, how many plot gates drive
it, and the narrative defaults (escalation curve, crisis mode, narrator
register, production weighting) that suit the channel's storytelling rhythm.

The mental model the showrunner works with:
    channel = HOW (format / length / pacing)
    genre   = WHAT (the kind of story)
    cast    = WHO  (the characters)
    -- the WHEN and WHY emerge inside the episodes themselves.

Channels are referenced by bare id strings elsewhere in the engine
(`PipelineSettings.channel_id`, `BatchConfig.channel_id`,
`EpisodeConfig.channel_id`). This module is what those ids resolve to.

The four channels and their consumer-facing brand names are fixed by the
Parallax Signal Network brand identity. The structural numbers below are
production defaults — a SeasonConfig may override episode_count etc. per
season, but the preset is where a new season starts.

## Defined here

### `ChannelWeights`

Character / action / atmosphere production weighting for a channel.

Mirrors the GUI's ProductionWeights but lives in schemas/ so the engine
core never imports from gui/. The three values must sum to 100.

| Field | Type |
|---|---|
| `character` | `int` |
| `action` | `int` |
| `atmosphere` | `int` |

### `ChannelPreset`

The structural + tonal preset for one distribution channel.

Resolves a bare channel id (e.g. "aces") into concrete production
defaults: episode count, episode length, plot-gate structure, and the
narrative knobs that match the channel's rhythm.

| Field | Type |
|---|---|
| `channel_id` | `str` |
| `display_name` | `str` |
| `brand_name` | `str` |
| `story_type` | `str` |
| `genre_default` | `str` |
| `episodes_per_season` | `int` |
| `segments_per_episode` | `int` |
| `minutes_per_segment` | `int` |
| `plot_gates_per_episode` | `int` |
| `default_escalation_curve` | `list[int]` |
| `fichtean_crisis_default` | `bool` |
| `narrator_mode_default` | `str` |
| `production_weights` | `ChannelWeights` |
| `resonance_school` | `str` |
| `description` | `str` |

## Top-level functions

- **`get_channel_preset()`** — Resolve a bare channel id to its ChannelPreset.
- **`list_channel_ids()`** — Return the four known channel ids in display order.
