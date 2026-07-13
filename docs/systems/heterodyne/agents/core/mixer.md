# mixer

*Source: `heterodyne/agents/mixer.py`*

Mixer — FFmpeg-driven assembly of voice + foley + music into a finished episode.

Phase 4C scope: full three-layer production mix.

Public surface (backward compatible with Phase 3):

    Mixer(voice_dir, foley_dir, output_dir)
    mixer.mix_episode(
        episode_json_path,
        voice_manifest_path,
        music_cue_list_path=None,   ← Phase 4C: optional music layer
        location="grand_atrium",    ← Phase 4C: reverb profile selector
    ) -> MixReport

Three layers:

  Voice layer   : per-block .wav files concatenated in block_id order.
                  Source: VoiceEngine manifest.

  Foley layer   : ambient SFX placed at block timestamps.
                  Source: foley_cues in episode JSON → catalog → .wav.
                  Sidechained against voice (ducks under speech).

  Music layer   : leitmotif stems placed at cue list timestamps.
                  Source: EpisodeMusicCueList JSON → audio/stems/*.wav.
                  Sidechained against voice (ducks under speech).
                  Loopable stems are extended to fill their cue window.
                  Stinger cues play once (≤2s), no loop.

Final mix chain (3-layer):
  1. Foley ducked against voice via sidechaincompress
  2. Music ducked against voice via sidechaincompress
  3. voice + ducked_foley + ducked_music → amix (normalize=0)
  4. Per-location convolution reverb (afir against a synthesized IR —
     see scripts/generate_reverb_irs.py — replacing the former aecho
     slap-echo approximation)
  5. [A3] Transmission band filter (when transmission_enabled=True):
       HPF 300 Hz → LPF 3400 Hz → pink noise bed → optional AM tremor
       → 0.5s static stamps at open/close
  6. EBU R128 loudness normalization: -16 LUFS, -1 dBTP (loudnorm filter)
  7. Encode to MP3 (192kbps, 48kHz stereo — mono via MixerSettings.stereo_master_enabled=False)
  8. Copy pre-norm WAV master to output/masters/ (pre-transmission, clean master)

Reverb profiles (afir convolution IR + wet gain — see REVERB_PROFILES /
audio/impulse_responses/):
  grand_atrium    — large resonant hall, longer/brighter decay
  eastern_passage — tight corridor, short bright decay
  camp_1          — small room, subtle decay
  jungle          — open air, very short/dark decay (foliage-damped)
  seed_chamber    — large enclosed chamber, longest/darkest decay
  default         — moderate middle-ground

Resumability: re-running on a completed episode is a no-op (output MP3
already on disk). Use --force in the orchestration script to rebuild.

## Defined here

### `MixerError`

Base class for Mixer failures.

### `FFmpegNotFoundError`

ffmpeg binary is not on PATH.

### `FFmpegFailedError`

ffmpeg subprocess returned non-zero. Stderr captured for diagnosis.

### `FoleyCueResult`

One foley placement attempt.

| Field | Type |
|---|---|
| `cue_name` | `str` |
| `block_id` | `str` |
| `timestamp_seconds` | `float` |
| `placed` | `bool` |
| `source_path` | `Path | None` |
| `reason` | `str | None` |
| `manifest_applied` | `bool` |
| `rhythmic_repeats` | `int` |

### `MusicStemResult`

One music stem placement attempt.

| Field | Type |
|---|---|
| `stem_id` | `str` |
| `source_block_id` | `str` |
| `start_seconds` | `float` |
| `end_seconds` | `float` |
| `placed` | `bool` |
| `source_path` | `Path | None` |
| `reason` | `str | None` |

### `RhythmicLoop`

Repeat a trimmed clip on a rhythmic schedule.

| Field | Type |
|---|---|
| `interval_ms` | `int` |
| `jitter_ms` | `int` |
| `count` | `int` |
| `seed` | `int | None` |

### `FoleyManifest`

Optional sidecar metadata for a foley source file.

| Field | Type |
|---|---|
| `trim_start_seconds` | `float` |
| `trim_duration_seconds` | `float | None` |
| `loop` | `bool` |
| `rhythmic_loop` | `RhythmicLoop | None` |
| `volume_db_offset` | `float` |
| `notes` | `str | None` |

### `MixReport`

Outcome of a mix_episode call.

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `output_path` | `Path` |
| `master_path` | `Path | None` |
| `mp4_path` | `Path | None` |
| `duration_seconds` | `float` |
| `voice_blocks_concatenated` | `int` |
| `foley_cues_placed` | `int` |
| `foley_cues_missing` | `int` |
| `foley_cue_results` | `list[FoleyCueResult]` |
| `music_stems_placed` | `int` |
| `music_stems_missing` | `int` |
| `music_stem_results` | `list[MusicStemResult]` |
| `location` | `str` |
| `lufs_normalized` | `bool` |
| `started_at` | `datetime` |
| `completed_at` | `datetime` |

### `Mixer`

Assembles per-block WAV files into a finished episode MP3.

Phase 3 (voice + foley) and Phase 4C (voice + foley + music) share
the same public interface. Pass music_cue_list_path to mix_episode()
to enable the music layer. Omit it for Phase 3 behavior.

Foley resolution order:
  1. FoleyCatalog (if attached and cue matches a catalog_id)
  2. Legacy flat directory at <foley_dir>/<cue>.wav
  3. Skip with warning.

## Top-level functions

- **`compute_block_pause()`** — Seconds of silence to place after a spoken block.
