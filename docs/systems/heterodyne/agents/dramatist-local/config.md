# config

*Source: `heterodyne/agents/dramatist_local/config.py`*

agents.dramatist_local.config — runtime configuration for the local pipeline.

Everything is env-overridable so A/B runs need no code changes. Model
selection is per stage: the writer does beats + prose (the creative work),
the annotator derives audio metadata (a small fast model is fine), the judge
runs fidelity checks. All default to the writer model so a single
WRITER_MODEL env var is enough to get started.

## Defined here

### `LocalDramatistConfig`

Per-run knobs for LocalDramatist. Build with from_env() in runners.

| Field | Type |
|---|---|
| `writer_model` | `str` |
| `annotator_model` | `str` |
| `judge_model` | `str` |
| `ollama_url` | `str` |
| `num_ctx` | `int` |
| `timeout` | `float` |
| `writer_max_tokens` | `int` |
| `annotator_max_tokens` | `int` |
| `judge_max_tokens` | `int` |
| `metadata_mode` | `str` |
| `words_per_minute` | `int` |
| `max_beat_continuations` | `int` |
| `beat_sheet_scope` | `str` |
| `min_beats_per_segment` | `int` |
| `max_beats_per_segment` | `int` |
| `judge_enabled` | `bool` |
| `judge_max_regen` | `int` |
| `world_judge_action` | `str` |
| `judge_noverdict_action` | `str` |
| `lint_action` | `str` |
| `segments_override` | `int | None` |
| `segments_per_episode` | `int` |
| `minutes_per_segment` | `int` |
| `extra` | `dict` |

## Top-level functions

- **`load_segment_plan()`** — Resolve (segments_per_episode, minutes_per_segment) for a season.
