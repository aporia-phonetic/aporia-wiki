# maestro

*Source: `heterodyne/agents/maestro.py`*

Maestro — music cue resolver and cue-list builder.

Phase 4B agent. Given a complete episode JSON (4 segments already generated
by the Dramatist), Maestro:

  1. Loads the stem manifest from data/stem_manifest.db into an in-memory
     trigger resolver (built once per run).
  2. Reads the episode's four SegmentScript objects from the JSON wrapper.
  3. Walks every ScriptBlock in order, accumulating wall-clock time from
     duration_estimate_seconds + INTER_BLOCK_PAD.
  4. When a block carries a music_cue, resolves the trigger through a
     four-step fallback chain:
       a. Exact match  — trigger in stem_triggers table
       b. Token inference — split trigger on '_', match any token against
          any registered trigger_key
       c. Emotional bed — single Claude API call classifies the unmatched
          trigger as tension_low | tension_high | wonder → bed stem
       d. Silence — logged to unresolved_triggers, not an error
  5. Determines cue duration: a cue runs from its start_seconds until the
     NEXT cue's start (minus fade overlap) or episode end.
  6. Writes EpisodeMusicCueList to:
       data/seasons/season_{S:02d}/episodes/S{S}E{E:02d}_music_cues.json

Intensity → mix parameter table (mirrors script_block.py MusicIntensity):

  sparse    → -22 dB,  1.5s fade in / 1.5s fade out
  moderate  → -20 dB,  1.8s fade in / 1.8s fade out
  building  → -18 dB,  2.0s fade in / 2.0s fade out
  full      → -12 dB,  3.0s fade in / 3.0s fade out
  duck      → -28 dB,  1.0s fade in / 1.0s fade out  (barely audible bed)
  stinger   → -10 dB,  0.3s fade in / 0.3s fade out, capped at 2.0s (plays once)

Cue duration model:
  - Each cue starts at its block's wall-clock position.
  - It ends when the next cue fires (accounting for fade_out overlap).
  - stinger: always ends at start + min(stem_duration, STINGER_MAX_SECONDS).
  - Episode end: final cue fades out over EPISODE_END_FADE_SECONDS.
  - Loopable stems are extended to fill the gap; non-loopable play once.

## Defined here

### `MaestroError`

Raised when Maestro fails to build the music cue list.

### `StemRecord`

| Field | Type |
|---|---|
| `stem_id` | `str` |
| `file_path` | `str` |
| `duration_seconds` | `float` |
| `is_loopable` | `bool` |
| `trigger_keys` | `list[str]` |

### `PendingCue`

Cue event collected during block-walk, before end_seconds is known.

| Field | Type |
|---|---|
| `block_id` | `str` |
| `trigger` | `str` |
| `stem` | `StemRecord` |
| `intensity` | `str` |
| `duck_under_dialogue` | `bool` |
| `start_seconds` | `float` |
| `resolve_method` | `str` |

### `Maestro`

Music cue resolver and cue-list builder.

Usage::

    maestro = Maestro(db_path=Path("data/stem_manifest.db"))
    cue_list = maestro.build_cue_list(
        episode_json_path=Path("data/seasons/season_01/episodes/S1E05_....json"),
        season=1,
        episode=5,
    )
    cue_list.save(Path("data/seasons/season_01/episodes/S1E05_music_cues.json"))
