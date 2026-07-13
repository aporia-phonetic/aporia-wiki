# voice_engine

*Source: `heterodyne/agents/voice_engine.py`*

Voice Engine — TTS dispatch from ScriptBlock to .wav.

Backend-agnostic via the TTSClient protocol (agents/tts_client.py). Currently
ships with KokoroTTS as the only implementation; ElevenLabsTTS lands when the
user configures it.

Public surface:

    VoiceEngine(tts, output_dir, model_dir)
    engine.render_block(block, season, episode)        -> AudioResult
    engine.render_episode(episode_json_path)           -> EpisodeRenderReport

`render_episode` walks all blocks in an episode, dispatches each to the TTS
backend, writes per-block .wav files, generates a manifest JSON for the
Mixer, and produces a summary report. Resumable: re-running the same call
skips blocks whose .wav files already exist.

## Defined here

### `VoiceEngineError`

Base class for Voice Engine failures.

### `ModelNotAvailableError`

Model file is missing and auto-download failed.

### `AudioResult`

Outcome of rendering a single block.

`success` distinguishes the happy path (audio on disk) from skips
(foley/music-cue blocks with no speech) and failures (errors caught
so the batch can continue).

| Field | Type |
|---|---|
| `block_id` | `str` |
| `success` | `bool` |
| `path` | `Path | None` |
| `duration_seconds` | `float | None` |
| `voice_id` | `str | None` |
| `backend` | `str | None` |
| `skipped` | `bool` |
| `cached` | `bool` |
| `unconditioned` | `bool` |
| `error` | `str | None` |

### `EpisodeRenderReport`

Summary of a render_episode() run.

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `started_at` | `datetime` |
| `completed_at` | `datetime` |
| `total_blocks` | `int` |
| `rendered` | `int` |
| `cached` | `int` |
| `skipped` | `int` |
| `failed` | `int` |
| `manifest_path` | `Path` |
| `results` | `list[AudioResult]` |

### `VoiceEngine`

Synthesizes audio from ScriptBlocks via a TTSClient backend.

Parameters
----------
tts:
    A TTSClient implementation. If provided, `tts_engine` and
    `model_dir` are ignored. Use this for injecting custom backends.
output_dir:
    Where rendered .wav files go. Subdirectories per episode.
model_dir:
    Required when `tts_engine` is "kokoro" and `tts` is None. Where
    kokoro-v1.0.int8.onnx and voices-v1.0.bin live (auto-downloaded
    first run).
tts_engine:
    Which backend to auto-construct when `tts` is None.
    "kokoro"   — KokoroTTS (default, requires model_dir)
    "orpheus"  — OrpheusTTS (requires Orpheus server or package)
orpheus_mode:
    "api" (default) or "native". See OrpheusTTS for setup details.
orpheus_api_url:
    Override Orpheus FastAPI server URL. Default: http://localhost:5005.
