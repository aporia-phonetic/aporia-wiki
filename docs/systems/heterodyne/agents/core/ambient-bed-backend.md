# ambient_bed_backend

*Source: `heterodyne/agents/ambient_bed_backend.py`*

agents.ambient_bed_backend — pluggable rendering backends for A9.

Three backends mirror the A6 TTS stub pattern:

    StubAmbientBedBackend       — FFmpeg `anoisesrc=color=pink`, seeded.
                                  Zero asset dependency; smoke tests pass on
                                  CPU; deterministic on re-render.
    FileAmbientBedBackend       — Loops a real WAV file from disk.
                                  Used when `entry.file_path` is set.
    AudiocraftAmbientBedBackend — Fully implemented. Procedural ambient
                                  generation via local MusicGen, now that
                                  the hardware-day rig (dual RTX 3090) is
                                  live. `main.py::run_ambient_bed` selects
                                  this backend automatically whenever
                                  `audiocraft` is importable, falling back
                                  to the stub only in CPU-only/no-GPU
                                  environments.

Backends are injected at `AmbientBedMaster` construction. The agent picks
a backend per segment via `pick_backend(entry, default=stub_backend)` —
file backend if `entry.file_path` exists, otherwise default.

Sample rate / format
====================
Output is **stereo, 24 kHz, 16-bit PCM WAV** to match the existing voice and
foley intermediate format in `agents/mixer.py`. Phase B's mixer integration
amixes the bed track with voice/foley/music at this rate; downstream
loudness normalization and the A3 transmission filter handle the rest.

## Defined here

### `AmbientBedBackend`

Minimal interface every bed-rendering backend must satisfy.

### `StubAmbientBedBackend`

Pink-noise placeholder backend.

Renders FFmpeg `anoisesrc=color=pink:seed=<deterministic>` trimmed to
`duration_s`, with the output level set so that the rendered RMS equals
`entry.intrinsic_db` at intensity=0.6. The volume filter argument is
computed by `_intensity_to_db_adjustment`, which compensates for
anoisesrc's native -14.2 dBFS RMS so that `intrinsic_db` acts as an
absolute target level in dBFS.

The seed is derived deterministically from (bed_id, intrinsic_db,
duration_s, intensity), so re-rendering produces byte-identical WAV.
This matters for the Phase A determinism test.

### `FileAmbientBedBackend`

Backend that loops a real WAV asset from disk.

Reads `entry.file_path`, uses FFmpeg `-stream_loop -1` to repeat it
indefinitely, trims to `duration_s`, applies intensity-derived gain,
and writes stereo 24 kHz PCM. The source file may be any sample rate
or channel layout; FFmpeg handles resampling and up/downmix to stereo.

### `AudiocraftAmbientBedBackend`

Procedural ambient generation via Meta AudioCraft / MusicGen.

Generates loopable ambient beds from bed_id + location_tags using
MusicGen. First call loads the model (~2–4 GB VRAM for medium).
Output is resampled from MusicGen's 32kHz to 24kHz (Mixer target).

Usage:
    bed_backend = AudiocraftAmbientBedBackend()
    agent = AmbientBedMaster(catalog, backend=bed_backend)

## Top-level functions

- **`pick_backend()`** — Choose the right backend for a given catalog entry.
