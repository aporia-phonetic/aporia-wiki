# speaker_embedding

*Source: `heterodyne/agents/speaker_embedding.py`*

agents/speaker_embedding.py — Engine-neutral speaker-verification embeddings.

Shared WavLM-SV (microsoft/wavlm-base-plus-sv, via transformers) loader and
embedder. Originally inlined in scripts/voice_bakeoff.py; factored out here
so scripts/voice_ref_qa.py can reuse the same encoder to check that a newly
minted reference clip's takes all sound like the same speaker, without
duplicating the model-loading/embedding code.

Kept engine-neutral: this is a speaker-verification model, not any one TTS
engine's own encoder, so similarity scores are comparable across engines/uses.

## Defined here

### `SpeakerEmbedder`

Loaded WavLM-SV feature extractor + model, pinned to one device.

| Field | Type |
|---|---|
| `feature_extractor` | `Any` |
| `model` | `Any` |
| `device` | `str` |

## Top-level functions

- **`load_speaker_embedder()`** — Load the shared WavLM-SV feature extractor + model.
- **`embed_waveform()`** — Embed an in-memory mono waveform (1-D torch tensor) at `sample_rate`.
- **`embed_file()`** — Embed a wav file on disk. Used by voice_bakeoff.py's cross-engine scoring.
- **`cosine_similarity()`** — 
