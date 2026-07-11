# parler_client

*Source: `heterodyne/agents/parler_client.py`*

Parler-TTS client — local text-described voice generation.

Parler-TTS (Apache 2.0, https://github.com/huggingface/parler-tts) is the
open-weight analogue of ElevenLabs Voice Design: you describe a voice in
natural language ("a contralto with flat affect, slow and deliberate, very
clear close-microphone recording") and it synthesizes speech in that voice —
no reference audio, no cloning of a real person.

We use it to mint ONE reference clip per character, which the local cloning
backends (chatterbox, zonos) then reuse for every production line. Because the
model runs locally under a permissive licence, the generated clip is ours to
use downstream — including as a clone reference — with no provider Terms of
Service governing the output (unlike cloud TTS vendors).

This client mirrors agents/musicgen_client.py:
- Lazy-loads the model (one cold start per process)
- Deferred heavy imports (torch, transformers, parler_tts) so importing this
  module stays cheap
- Writes a mono PCM_16 .wav and computes its SHA-256 for the manifest
- generate() is the only interface scripts depend on

Usage:
    client = build_default_client()
    result = client.generate(description="...", text="...", output_path=Path(...))
    client.unload()

## Defined here

### `VoiceRefResult`

Result of a single Parler-TTS reference-clip generation.

| Field | Type |
|---|---|
| `file_path` | `Path` |
| `duration_seconds` | `float` |
| `sample_rate` | `int` |
| `channels` | `int` |
| `model_id` | `str` |
| `file_sha256` | `str` |

### `ParlerClient`

Local Parler-TTS wrapper.

Heavy imports (torch, transformers, parler_tts) are deferred to the first
generate() call so the rest of the pipeline can import this module without
paying the cost.

## Top-level functions

- **`build_default_client()`** — Construct the default Parler client.
