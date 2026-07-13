# tts_client

*Source: `heterodyne/agents/tts_client.py`*

TTSClient protocol — the interface every TTS backend implements.

Same pattern as LLMClient in agents/dramatist.py: define a minimal protocol,
write multiple implementations, inject at construction time. The Voice Engine
talks to the protocol, never to Kokoro or ElevenLabs directly.

Implementations:
    KokoroTTS   — local, free, ~80MB ONNX model, 0.5-0.7x realtime on CPU
    OrpheusTTS  — local LLM-based TTS (Llama 3.2 3B + SNAC), theatrical quality,
                  8 built-in voices with emotion tags, 24kHz WAV, Apache 2.0.
                  Two modes: 'native' (orpheus_tts package) or 'api' (FastAPI endpoint).

When ElevenLabs lands, the Voice Engine doesn't change. Per-character TTS
backend selection becomes a constructor argument:

    engine = VoiceEngine(
        tts_clients={
            "VS-000": ElevenLabsTTS(voice_id="..."),  # narrator gets the premium
            "VS-001": KokoroTTS(...),                 # rest stay free
            ...
        },
        output_dir=...,
    )

## Defined here

### `TTSResponse`

What every TTS backend returns from synthesize().

`samples` is the raw audio buffer (1D float array of waveform values).
`sample_rate` is the rate that buffer was generated at — Kokoro is
24kHz, ElevenLabs returns 22050Hz or 44100Hz depending on tier. The
Voice Engine writes the WAV at whatever rate the backend gives it;
the Mixer (Phase 3) resamples if needed.

`voice_used` is informational — what the backend resolved the request
to. Useful for the manifest log.

| Field | Type |
|---|---|
| `samples` | `list[float] | bytes` |
| `sample_rate` | `int` |
| `voice_used` | `str` |
| `backend` | `str` |

### `TTSClient`

Minimal interface any TTS backend must satisfy.

### `KokoroTTS`

Kokoro-onnx adapter satisfying the TTSClient protocol.

Lazy-loads the model on first synthesize() call. Auto-downloads
model files if missing. All previous VoiceEngine logic that called
`kokoro.create()` directly now goes through this adapter.

### `OrpheusTTS`

Orpheus TTS adapter satisfying the TTSClient protocol.

Orpheus uses an LLM backbone (Llama 3.2 3B) + SNAC decoder for
theatrical-quality speech with natural emotion. 24kHz WAV output,
Apache 2.0 license.

Built-in voices: tara, leah, jess, leo, dan, mia, zac, zoe.
Emotion tags in text: <laugh>, <sigh>, <gasp>, <chuckle>, <yawn>,
  <cough>, <sob>, <groan>, <sniffle>.

Two modes
---------
native  — imports orpheus_tts and runs in-process.
          Requires: pip install orpheus-tts
          Hardware: NVIDIA GPU ≥8GB VRAM recommended.
api     — posts to an Orpheus-FastAPI endpoint (OpenAI-compatible).
          Start the server: github.com/lex-au/orpheus-fastapi
          Default URL: http://localhost:5005

Speed is accepted for protocol compatibility but is not applied —
Orpheus does not expose a speed control in its current API.

### `ElevenLabsTTS`

ElevenLabs API adapter satisfying the TTSClient protocol.

Studio-quality TTS with 29+ voices in 12+ languages, voice cloning,
and streaming support. Requires ELEVENLABS_API_KEY environment variable
or passed at construction.

Model options:
  • eleven_monolingual_v1 (default) — fast, optimized for English
  • eleven_multilingual_v2 — supports 12+ languages, slower
  • eleven_turbo_v2 — streaming-capable, lower latency

For max quality production: use eleven_multilingual_v2 with
stability=0.5-0.75 (higher = more consistent), similarity_boost
increased to 0.75+ for character consistency.

Rate limits: Standard tier = 10k chars/month. Check
https://elevenlabs.io/pricing for your account limits.

### `ChatterboxTTS`

Chatterbox TTS adapter satisfying the TTSClient protocol.

A6 (Dual TTS Routing) prep — installed when the new GPU is configured.
Chatterbox is a local-GPU theatrical TTS engine; this adapter is the
integration seam.

Today this is a **stub**: it generates silent WAV-equivalent samples
so the pipeline runs end-to-end without the model installed. On
hardware day, replace `_synthesize_real` with the actual library call
(the model package, GPU device selection, voice loading).

The stub honors a small-but-realistic timing: silence duration is
proportional to text length (~150ms per word) so downstream mix
timing is roughly realistic even without the real model.

Hardware-day TODO:
    from chatterbox import ChatterboxModel  # or whatever the real import is
    self._model = ChatterboxModel.load(self.model_path, device=self.device)

### `ZonosTTS`

Zonos TTS adapter satisfying the TTSClient protocol.

A6 (Dual TTS Routing) prep — companion to ChatterboxTTS. Same stub
pattern: silent PCM at the right sample rate keeps the pipeline
runnable without the model. Real inference lands on hardware day.

Zonos voices are zero-shot — the `voice` argument is a path to (or
name of) a reference audio sample. The stub accepts any string.

Hardware-day TODO:
    from zonos import ZonosModel
    self._model = ZonosModel.from_pretrained(self.model_id, device=self.device)

### `Zonos2TTS`

ZONOS2 adapter satisfying the TTSClient protocol (server/api mode).

ZONOS2 (Zyphra, Apache-2.0, MoE) is too large to co-load in-process with the
other engines, so it runs as a standalone GPU server (see the runbook in
ORPHEUS_SETUP-style docs / scripts/zonos2-server.service). This client clones
by POSTing the per-character reference WAV inline (base64) to /tts/generate
and parses the float32 PCM (44.1 kHz mono) response.

`voice` is the reference WAV path (same convention as chatterbox/zonos). When
the server is unreachable the call raises, which the VoiceEngine health probe
turns into a fallback to the secondary backend (chatterbox) → kokoro.

## Top-level functions

- **`ensure_zonos2_server()`** — Make sure the ZONOS2 server is up, launching it if it isn't.
