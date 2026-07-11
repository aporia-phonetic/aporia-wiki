# audio_widen

*Source: `heterodyne/agents/audio_widen.py`*

agents.audio_widen — shared FFmpeg stereo-widening filter for generated audio.

`MusicGenClient` and `AudiocraftAmbientBedBackend` both generate true mono
audio and duplicate it to 2 channels to satisfy the pipeline's stereo format
— a dead duplicate with zero real width until this filter runs. Factored out
here so the filter string and its (non-default) parameter choices live in one
place instead of being copy-pasted between the two call sites.

## Top-level functions

- **`apply_stereo_widen()`** — Apply the shared Haas stereo-widening filter to a 2-channel WAV in place.
