# publication_buffer

*Source: `heterodyne/schemas/publication_buffer.py`*

schemas/publication_buffer.py

Publication buffer schema for the Aeon Pulp Drama Engine.

The buffer system separates production from publication with a configurable
rolling window, preventing content staleness while protecting against pipeline
failures.

Two parameters define the buffer:
  buffer_weeks     — Minimum weeks of pre-produced content to maintain ahead of air.
                     This is the safety net: if the pipeline fails, this is the
                     runway before an air date is missed.
  max_advance_weeks — Furthest ahead the scheduler is allowed to produce.
                     This is the staleness cap: content cannot be produced more
                     than max_advance_weeks ahead of its intended air date.

Recommended settings:
  buffer_weeks:      2  (two weeks of safety net)
  max_advance_weeks: 4  (content is at most 4 weeks old when it airs)
  alert_threshold:   10 (alert when buffer drops below 10 days)

Ideal operating state: 2–3 weeks ahead. Scheduler tops up to 3 weeks when
possible, idles when 3 weeks of coverage exist, alerts if below 2 weeks.

BufferState is not persisted. It is derived at evaluation time from the
channel archive + episode air date schedule.

Per spec section 2.6, ChannelArchiveEntry tracks language variants,
extending the existing archive.json structure.

## Defined here

### `BufferConfig`

Publication buffer configuration for a single channel.

Stored per channel at data/channels/{channel}/buffer_config.json.
Managed via the Scheduler tab Buffer Management section.

Args:
    channel:               Channel identifier ("aces", "hero", "hart", "echo").
    release_cadence_days:  Days between episode air dates. 1 = daily, 7 = weekly.
    buffer_weeks:          Minimum weeks of pre-produced content to maintain.
    max_advance_weeks:     Maximum weeks ahead production is allowed to run.
    alert_threshold_days:  Alert when buffer drops below this many days of coverage.

| Field | Type |
|---|---|
| `channel` | `str` |
| `release_cadence_days` | `int` |
| `buffer_weeks` | `int` |
| `max_advance_weeks` | `int` |
| `alert_threshold_days` | `int` |

### `BufferState`

Current production-vs-publication state for a channel.

Calculated by the Archivist/scheduler at evaluation time.
Not persisted — derived from channel archive and episode air dates.

status values:
  healthy  — Buffer is above buffer_weeks. No action needed.
  low      — Buffer is below buffer_weeks but above alert_threshold_days.
             Top-up batch should fire at next trigger.
  critical — Buffer is below alert_threshold_days. Immediate alert.
  maxed    — Production is at max_advance_weeks. Do not produce.

production_recommended: True when scheduler should initiate a top-up run.

| Field | Type |
|---|---|
| `channel` | `str` |
| `episodes_in_buffer` | `int` |
| `days_of_coverage` | `float` |
| `weeks_of_coverage` | `float` |
| `latest_produced_air_date` | `Optional[str]` |
| `next_air_date` | `Optional[str]` |
| `advance_weeks` | `float` |
| `buffer_status` | `str` |
| `production_recommended` | `bool` |

### `ChannelArchiveEntry`

A single episode entry in the channel archive.

Extends the existing archive.json structure (per spec section 2.6) to
track language variants and per-language output paths.

Stored in data/channels/{channel}/archive.json as a JSON array.

| Field | Type |
|---|---|
| `episode_id` | `str` |
| `season` | `int` |
| `episode` | `int` |
| `first_aired` | `Optional[str]` |
| `intended_air_date` | `Optional[str]` |
| `languages_available` | `list[str]` |
| `output_paths` | `dict[str, str]` |
| `production_complete` | `bool` |
| `has_aired` | `bool` |

## Top-level functions

- **`calculate_buffer_state()`** — Derive current BufferState from archive data and config.
- **`evaluate_buffer_and_schedule()`** — Evaluate buffer state and decide whether to initiate a production run.
- **`calculate_topup_size()`** — Calculate how many episodes to produce in a top-up batch.
