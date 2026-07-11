# music_cue_list

*Source: `heterodyne/schemas/music_cue_list.py`*

Music cue list schema — Maestro's output, the Mixer's music contract.

Maestro reads an episode JSON (4 segments) and emits one EpisodeMusicCueList
per episode. The Mixer reads this file at Phase 4C mix time to place and
blend the music layer against the voice + foley timeline.

This is NOT a streaming contract — Maestro writes the complete cue list
before the Mixer starts. The Mixer reads it once and builds the music layer.

File path convention:
    data/seasons/season_{S:02d}/episodes/S{S}E{E:02d}_music_cues.json

## Defined here

### `MusicCueEvent`

One resolved, timestamped music placement instruction.

The Mixer reads each event and:
  1. Loads `file_path` as the stem source
  2. Seeks to `start_seconds` on the master timeline
  3. Loops the stem if `is_loopable` until `end_seconds`
  4. Applies `fade_in_seconds` at start and `fade_out_seconds` at end
  5. Scales volume to `target_db`
  6. If `duck_under_dialogue` is True, applies sidechain compression
     against the voice activity track (built from voice block timestamps)

`stinger` intensity events have `end_seconds = start_seconds + stem_cap_seconds`
(≤ 2.0s). They play once; the Mixer does not loop them.

| Field | Type |
|---|---|
| `event_id` | `str` |
| `stem_id` | `str` |
| `file_path` | `str` |
| `start_seconds` | `float` |
| `end_seconds` | `float` |
| `target_db` | `float` |
| `fade_in_seconds` | `float` |
| `fade_out_seconds` | `float` |
| `duck_under_dialogue` | `bool` |
| `is_loopable` | `bool` |
| `intensity` | `MusicIntensity` |
| `source_block_id` | `str` |
| `source_trigger` | `str` |
| `resolve_method` | `ResolveMethod` |

### `UnresolvedTrigger`

A music_cue trigger that fell through all resolver steps.

| Field | Type |
|---|---|
| `source_block_id` | `str` |
| `source_trigger` | `str` |
| `intensity` | `str` |
| `timestamp_seconds` | `float` |
| `reason` | `str` |

### `EpisodeMusicCueList`

Complete music cue list for one episode.

Written by Maestro to:
    data/seasons/season_{S:02d}/episodes/S{S}E{E:02d}_music_cues.json

Read by Mixer (Phase 4C) during the music layer assembly step.

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `total_duration_seconds` | `float` |
| `events` | `list[MusicCueEvent]` |
| `unresolved_triggers` | `list[UnresolvedTrigger]` |
| `generated_at` | `datetime` |
| `maestro_version` | `str` |
