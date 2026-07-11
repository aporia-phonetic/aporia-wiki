# character

*Source: `heterodyne/schemas/character.py`*

schemas.character — Voice Seed registry and character identity models.

Voice Seeds are the bridge between the Dramatist (which tags every block with
a voice_seed_id) and the Voice Engine (which calls KokoroTTS with the resolved
kokoro_voice and kokoro_speed). Adding a new character = add a VoiceSeed entry
here and a personality prompt in prompts/vocal_personalities/.

Kokoro voice IDs ship with kokoro-onnx >= 0.4.0. Full list:
  American female : af_heart, af_bella, af_nicole, af_sky, af_sarah, af_nova
  American male   : am_adam, am_echo, am_eric, am_fenrir, am_liam, am_michael, am_onyx
  British female  : bf_emma, bf_isabella
  British male    : bm_george, bm_lewis, bm_daniel

Voice assignments are chosen to match the tonal spec in 03_TECHNICAL_STACK_AND_BUILD_PLAN.md.
Swap kokoro_voice values here to audition different voices without touching any other file.

## Defined here

### `LanguageVoiceOverride`

Voice parameters to use when synthesizing a non-English language variant.

When `VoiceEngine` is constructed with `language != "en"`, it checks
`VoiceSeed.language_overrides[language_code]` before falling back to
the default `kokoro_voice` / `orpheus_voice` fields.

Fields are optional — omit `kokoro_speed` to inherit the parent seed's
speed. Omit `orpheus_voice` to fall back to the parent seed's orpheus_voice.

Kokoro multilingual voice naming convention:
  Voices prefixed `ef_`, `em_`, `ff_`, `fm_`, `zf_`, `zm_` etc. indicate
  language variant (e: English, f: French, z: Chinese, etc.) + gender.
  Install the relevant Kokoro language pack before populating these values.

| Field | Type |
|---|---|
| `kokoro_voice` | `str` |
| `kokoro_speed` | `float | None` |
| `orpheus_voice` | `str | None` |
| `ssml_adjustments` | `str | None` |

### `VoiceSeed`

All TTS parameters and narrative identity for one character voice.

Parameters
----------
seed_id:
    Canonical ID used in every ScriptBlock.voice_seed_id field.
    Format: VS-NNN (zero-padded three digits).
character_name:
    Human-readable name for logs and manifests.
description:
    One-line voice descriptor for prompts and debug output.
kokoro_voice:
    Kokoro voice ID string (e.g. "am_onyx"). Must be a voice
    shipped with the installed kokoro-onnx version.
kokoro_speed:
    Speech rate multiplier. 1.0 = natural rate. Range 0.5–2.0.
    Values below 0.85 suit measured/deliberate speakers.
    Values above 1.05 suit energetic/anxious speakers.
orpheus_voice:
    Orpheus TTS voice name (e.g. "leo"). One of the 8 built-in
    Orpheus voices: tara, leah, jess, leo, dan, mia, zac, zoe.
    None means the Kokoro voice is used as fallback when Orpheus
    backend is selected.
ssml_defaults:
    Optional SSML attribute hints the Dramatist may embed in
    block.ssml_tags. The Voice Engine strips these before synthesis
    (Kokoro does not consume SSML) but they are preserved in the
    episode JSON for future ElevenLabs upgrade.
personality_prompt_file:
    Filename (no path) of the personality prompt in
    prompts/vocal_personalities/. Used by the Dramatist to
    colour each character's dialogue generation.
is_narrator:
    True only for VS-000. Controls whether the Voice Engine
    applies narrator-specific post-processing (slight room tone,
    slightly slower fade-out).

| Field | Type |
|---|---|
| `seed_id` | `str` |
| `character_name` | `str` |
| `description` | `str` |
| `tts_backend` | `TTSBackend` |
| `tts_backend_secondary` | `TTSBackend | None` |
| `elevenlabs_voice_id` | `str | None` |
| `kokoro_voice` | `str` |
| `kokoro_speed` | `float` |
| `orpheus_voice` | `str | None` |
| `language_overrides` | `dict[str, LanguageVoiceOverride]` |
| `ssml_defaults` | `dict[str, str]` |
| `personality_prompt_file` | `str | None` |
| `is_narrator` | `bool` |
| `flat_affect` | `bool` |
| `voice_design_prompt` | `Optional[str]` |
| `zonos2_tempo` | `float` |
| `voice_gender` | `Optional[Literal['masculine', 'feminine', 'neutral']]` |
| `prosody_tags` | `list[str]` |
| `sampling_temperature` | `float | None` |
| `pitch_semitones` | `float` |
| `formant_shift` | `float` |
| `golden_age_texture` | `str | None` |
