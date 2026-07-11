# musicgen_client

*Source: `heterodyne/agents/musicgen_client.py`*

MusicGen client — local audiocraft wrapper.

Tuned for the music box specs:
- NVIDIA GTX 1060 6GB (Pascal)
- 16 GB system RAM
- Windows 10

Default model is facebook/musicgen-medium loaded in fp16, which fits in
~3 GB of VRAM and leaves headroom for generation buffers. The 'small'
model is available as a fallback if VRAM pressure shows up.

This client:
- Lazy-loads the model (one cold start per process)
- Generates 32kHz mono audio (MusicGen native)
- Resamples to 48kHz stereo for pipeline consistency with voice/foley
- Writes 24-bit PCM .wav so downstream FFmpeg has clean source material
- Computes SHA-256 of the output for the manifest

The class is structured so a Replicate or HF Inference client could be
swapped in later — Maestro and the generation script only depend on the
generate() interface.

## Defined here

### `GenerationResult`

Result of a single MusicGen generation.

| Field | Type |
|---|---|
| `file_path` | `Path` |
| `duration_seconds` | `float` |
| `sample_rate` | `int` |
| `channels` | `int` |
| `model_id` | `str` |
| `file_sha256` | `str` |

### `MusicGenClient`

Local audiocraft MusicGen wrapper.

Heavy imports (torch, audiocraft) are deferred to first generate()
call so that the rest of the pipeline can import this module without
paying the cost.

## Top-level functions

- **`build_default_client()`** — Construct the default client for the music box.
