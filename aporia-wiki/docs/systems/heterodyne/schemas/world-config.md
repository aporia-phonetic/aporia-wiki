# world_config

*Source: `heterodyne/schemas/world_config.py`*

schemas.world_config — World identity and genre configuration.

A World is the persistent container for all production within a genre/setting.
Seasons are story arcs that live inside a World. Characters belong to a World
by default (origin_world) but can appear in foreign worlds via crossover episodes.

World config files live at:
    data/worlds/{world_id}/world_config.json

The World Config is read-only during generation — it is never modified by the
Dramatist or Archivist. Changes require a manual edit and are versioned by
the bootstrap script.

## Defined here

### `ForgettingCurve`

Per-world override for the KnowledgeState decay pass.

Thresholds are measured in idle WorldClock years since a fact was last
referenced. SELF_KNOWN facts and facts at or above ``anchor_weight``
never decay. RUMORED facts have their thresholds multiplied by
``rumor_factor`` (e.g. 0.5 = rumors fade twice as fast).

| Field | Type |
|---|---|
| `confirmed_to_observed_years` | `float` |
| `observed_to_suspected_years` | `float` |
| `suspected_to_rumored_years` | `float` |
| `rumored_removal_years` | `float` |
| `anchor_weight` | `float` |
| `rumor_factor` | `float` |

### `WorldGenreSettings`

Narrative register and genre rules for this world.

These flow into the Dramatist system prompt as world-level constraints,
supplementing the per-season NarrativeRules on the WorldLedger.

| Field | Type |
|---|---|
| `genre` | `str` |
| `tone_descriptors` | `list[str]` |
| `narrator_voice_register` | `str` |
| `magic_system_summary` | `str` |
| `allow_second_person_narration` | `bool` |

### `WorldProductionProfile`

Audio production settings tied to this world's aesthetic.

| Field | Type |
|---|---|
| `default_reverb_location` | `str` |
| `active_foley_families` | `list[str]` |
| `active_stem_triggers` | `list[str]` |
| `world_theme_stem_id` | `str` |

### `WorldChronicleSettings`

Sediment Engine inputs — the world's deep-history parameters.

Recorded on the world so the Sediment Engine can run automatically as the
last step of new-world creation, with no showrunner prompting. Origin /
present conditions left blank are derived from the world description at
chronicle-generation time.

| Field | Type |
|---|---|
| `auto_generate_chronicle` | `bool` |
| `origin_condition` | `str` |
| `present_condition` | `str` |
| `fundamental_tension` | `str` |
| `time_span_years` | `int` |
| `era_count_target` | `int` |
| `significant_figures_per_era` | `int` |
| `geography_seed` | `str` |

### `WorldConfig`

Complete world definition. Stored at data/worlds/{world_id}/world_config.json.

Parameters
----------
world_id:
    Snake_case canonical identifier. Never changes after creation.
    Examples: verdant_deep, noir_city, open_sea, iron_cathedral.
world_name:
    Human-readable display name. Shown in sidebar and exports.
description:
    One-paragraph world description. Shown in GUI and injected into
    the Dramatist system prompt as world context.
available_species:
    Species that can exist in this world. Populates character sheet
    species dropdown. Human is always available.
default_season_episode_count:
    How many episodes a new season in this world defaults to.
    Showrunner can override per season. Max 26.

| Field | Type |
|---|---|
| `world_id` | `str` |
| `world_name` | `str` |
| `description` | `str` |
| `genre_settings` | `WorldGenreSettings` |
| `production_profile` | `WorldProductionProfile` |
| `chronicle_settings` | `WorldChronicleSettings` |
| `forgetting_curve` | `ForgettingCurve` |
| `available_species` | `list[str]` |
| `default_season_episode_count` | `int` |
| `created_at` | `str` |
| `migrated_from_season` | `Optional[int]` |
