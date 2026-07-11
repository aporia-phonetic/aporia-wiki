# episode_config

*Source: `heterodyne/schemas/episode_config.py`*

schemas/episode_config.py

Per-run configuration for the Aeon Pulp Drama Engine pipeline.

Extended with three new fields per the Batch API / Multilingual spec:
  - BatchMode enum (REALTIME / BATCH)
  - batch_mode:          Routes API calls to synchronous or asynchronous Batch API.
  - use_prompt_caching:  Enables ephemeral cache headers on system prompt blocks.
  - target_languages:    Language codes for translation variants to produce.

Existing NarratorMode enum and EpisodeConfig fields are preserved unchanged.

## Defined here

### `NarratorMode`

Controls the narrative presence and style of the NARRATOR voice.

SILENT      — No narrator. Scene-setting through dialogue and foley only.
LIGHT       — Minimal narrator. Scene transitions and time jumps only.
BALANCED    — Standard pulp radio narrator. Present at transitions and
              emotional beats.
HEAVY       — Persistent narrator. Frames every scene. Old-school radio drama.
OMNISCIENT  — Unreliable/omniscient narrator. Knows more than the characters.
              Used for special episodes and season finales.

### `NarratorPerspective`

### `POVMode`

### `ChildPresence`

### `ViolenceLevel`

### `DeathLevel`

### `ChildPerilLevel`

### `BatchMode`

Controls whether Dramatist API calls go through the synchronous Messages API
or the asynchronous Message Batches API.

REALTIME:
  Synchronous. Results stream to the Pipeline tab log immediately.
  Used for manual Pipeline tab runs where the showrunner is watching.
  The Pipeline tab always overrides to REALTIME regardless of any other setting.
  This override is automatic — it is not user-configurable on the Pipeline tab.

BATCH:
  Asynchronous. All calls for an episode (or set of episodes) are submitted
  as a single batch. Results polled at 30-second intervals.
  50% discount on all input and output tokens.
  Default for all Scheduler-triggered and Seasons tab bulk runs.

The rule:
  If the showrunner can wait up to one hour for results → BATCH.
  If the showrunner is watching the log in real time → REALTIME.

### `EpisodeConfig`

Complete per-run configuration for a pipeline execution.

Passed from the GUI (Pipeline tab or Scheduler) into run_episode().
The Dramatist, Archivist, Voice Engine, and Mixer all read from this.

Fields marked EXISTING are unchanged from the prior schema.
Fields marked NEW are additions from the Batch/Multilingual spec.

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `world_id` | `str` |
| `narrator_mode` | `NarratorMode` |
| `narrator_presence` | `float` |
| `narrator_perspective` | `NarratorPerspective` |
| `pov_mode` | `POVMode` |
| `pov_character_id` | `Optional[str]` |
| `violence_level` | `ViolenceLevel` |
| `death_level` | `DeathLevel` |
| `child_presence` | `ChildPresence` |
| `child_peril_level` | `ChildPerilLevel` |
| `story_vault_entries` | `list` |
| `ledger_db_path` | `Optional[Path]` |
| `plot_gates_path` | `Optional[Path]` |
| `chroma_path` | `Optional[Path]` |
| `dry_run` | `bool` |
| `skip_audio` | `bool` |
| `parallax_qa_enabled` | `bool` |
| `script_pipeline` | `Literal['dramatist', 'writers_room']` |
| `quality_tier` | `Literal['standard', 'premiere']` |
| `batch_mode` | `BatchMode` |
| `use_prompt_caching` | `bool` |
| `channel_id` | `str` |
| `escalation_level` | `int` |
| `fichtean_crisis_mode` | `bool` |
| `escalation_targets` | `List[List[int]]` |
| `crisis_type_overrides` | `List[Optional[str]]` |
| `resolution_system` | `str` |
| `resolution_manifest` | `Optional[dict]` |
| `chronicle_branch` | `str` |
| `temporal_position` | `Optional[TemporalPosition]` |
| `current_temporal_year` | `Optional[int]` |
| `convergence_id` | `Optional[str]` |
| `include_intro` | `bool` |
| `include_recap` | `bool` |
| `include_outro` | `bool` |
| `next_gate_title` | `Optional[str]` |
| `next_gate_dramatic_function` | `Optional[str]` |
| `is_series_premiere` | `bool` |
| `is_season_premiere` | `bool` |
| `character_debut_ids` | `List[str]` |
| `character_reintroduction_ids` | `List[str]` |
| `target_languages` | `list[str]` |
