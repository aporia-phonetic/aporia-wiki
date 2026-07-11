# season_config

*Source: `heterodyne/schemas/season_config.py`*

schemas.season_config — The editable spec for a season, between Clean Slate
and bootstrap.

A SeasonConfig is what the showrunner tweaks before a season is locked in.
It starts from a ChannelPreset (which fills the structural shape), carries
the three knobs (channel / genre / cast), and records the cast plan and
branching choice. The CLI `bootstrap_season.py` and the GUI Season Builder
both consume a SeasonConfig to autonomously build a complete season:
world + cast + plot gates + World Ledger + season scaffold.

Flow:
    Clean Slate generates a WorldSeed (world + gates + cast)
        -> a SeasonConfig links to that seed and the chosen channel
        -> showrunner reviews / tweaks
        -> bootstrap_season(config) builds everything

This module may import from schemas.channel (same package), but never from
gui/ — the engine core stays independent of the GUI layer. to_pipeline_settings()
therefore returns a plain dict that the GUI/CLI spreads into PipelineSettings.

## Defined here

### `CastSource`

Where a season's character cast comes from.

GENERATE        — Claude generates a fresh cast, biased by genre+channel+world.
ROSTER          — assemble from existing CharacterSheets by voice-seed id.
EXISTING_WORLD  — carry forward the cast of a prior world (crossover / continuation).

### `SeasonConfig`

The editable spec for one season. Drives autonomous bootstrap.

| Field | Type |
|---|---|
| `season_number` | `int` |
| `world_id` | `str` |
| `is_new_world` | `bool` |
| `channel_id` | `str` |
| `genre` | `str` |
| `cast_source` | `CastSource` |
| `episode_count` | `int` |
| `segments_per_episode` | `int` |
| `minutes_per_segment` | `int` |
| `plot_gates_per_episode` | `int` |
| `escalation_curve` | `list[int]` |
| `fichtean_crisis_mode` | `bool` |
| `narrator_mode` | `str` |
| `production_weights` | `ChannelWeights` |
| `is_branching_season` | `bool` |
| `branch_episode` | `Optional[int]` |
| `existing_cast_ids` | `list[str]` |
| `generate_cast_count` | `int` |
| `carry_world_id` | `str` |
| `world_seed_id` | `str` |
| `status` | `SeasonConfigStatus` |
| `created_at` | `str` |
