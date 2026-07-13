# script_block

*Source: `heterodyne/schemas/script_block.py`*

schemas/script_block.py

JSON-Audio-Map schema for the Aeon Pulp Drama Engine.

Base schema: SceneBlock, SegmentScript (original Phase 1 spec).

Latent Extension additions:
  - ContinuityWarning     (P2) — Dramatist flags potential contradictions
  - ToneSignature         (P9) — Segment-level tonal arc for Maestro
  - new_locations_introduced (P4 support) — Flags new location IDs to Archivist
  - segment_closing_positions (P11) — Character positions at segment end
  - AcousticIntent        (Phase 2) — Per-line emotional intent for TTS prosody
  - FoleyEvent            (Phase 3) — Structured foley events for parametric processing
  - tts_engine_override   (Proposal 6) — Per-line TTS backend override for high-stress lines

Foley validator: empty foley_cues auto-repair to ['ambient_general'] with
a log warning rather than failing validation. This behavior is preserved.

## Defined here

### `MusicCue`

Music cue embedded in a scene block.

| Field | Type |
|---|---|
| `trigger` | `str` |
| `intensity` | `str` |
| `duck_under_dialogue` | `bool` |

### `AcousticIntent`

Per-line emotional intent for TTS synthesis (Phase 2).

Adds prosodic control beyond the character-level register. Each scene block
can specify the emotional tone, intensity, contour shape, and pace for its
spoken line. Voice Engine translates this per backend:
  - Orpheus: injects inline emotion tags (<sigh>, <gasp>, etc.) and adjusts temperature
  - ElevenLabs: maps intensity to stability (inverse); emotion is informational for UI
  - Kokoro: no-op (ONNX API doesn't expose prosody control)

Text field ALWAYS remains plain English — Voice Sentinel validates it, and
this field is a TTS hint only, not a replacement for the spoken line.

| Field | Type |
|---|---|
| `emotion` | `str` |
| `subtext_emotion` | `Optional[str]` |
| `subtext_strength` | `float` |
| `paralinguistics` | `list[str]` |
| `intensity` | `float` |
| `contour_hint` | `str` |
| `pace_modifier` | `float` |

### `FoleyEvent`

Structured foley impact or ambient event (Phase 3).

Replaces free-text foley intent with structured event records,
enabling procedural post-processing and tighter catalog matching.

| Field | Type |
|---|---|
| `actor` | `Optional[str]` |
| `action` | `str` |
| `object` | `Optional[str]` |
| `surface` | `Optional[str]` |
| `material` | `Optional[str]` |
| `intensity` | `float` |
| `distance_m` | `float` |
| `duration_s` | `Optional[float]` |
| `room_size` | `Literal['intimate', 'small', 'medium', 'large', 'cathedral', 'outdoor']` |

### `LedgerUpdate`

A single World Ledger state change produced by a segment.

| Field | Type |
|---|---|
| `variable` | `str` |
| `previous` | `Any` |
| `updated` | `Any` |
| `cause` | `str` |

### `SceneBlock`

A single block in a segment's scene_blocks list.

Types: narration | dialogue | foley | music_cue

| Field | Type |
|---|---|
| `block_id` | `str` |
| `type` | `str` |
| `character` | `str` |
| `voice_seed_id` | `str` |
| `text` | `Optional[str]` |
| `ssml_tags` | `List[str]` |
| `foley_cues` | `List[str]` |
| `foley_events` | `List['FoleyEvent']` |
| `music_cue` | `Optional[MusicCue]` |
| `acoustic_intent` | `Optional[AcousticIntent]` |
| `tts_engine_override` | `Optional[Literal['zonos', 'chatterbox', 'kokoro']]` |
| `duration_estimate_seconds` | `Optional[float]` |
| `scene_energy` | `str` |
| `location` | `Optional[str]` |
| `social_post_flag` | `bool` |
| `social_post_text` | `Optional[str]` |
| `merch_trigger_flag` | `bool` |
| `merch_trigger_note` | `Optional[str]` |
| `narrator_move` | `Optional[str]` |
| `reported_speech_source` | `Optional[str]` |

### `ContinuityWarning`

A potential continuity violation flagged by the Dramatist during generation.

The Dramatist populates this array when it detects uncertainty about
whether generated content contradicts World Ledger state.

Processed by the Archivist post-generation:
  - blocking  → pipeline halted; requires resolution before commit
  - high      → flagged for immediate human review
  - medium    → logged; passed to next review cadence
  - low       → logged only

| Field | Type |
|---|---|
| `severity` | `str` |
| `type` | `str` |
| `description` | `str` |
| `affected_block_id` | `Optional[str]` |
| `suggested_resolution` | `Optional[str]` |

### `ToneSignature`

Segment-level tonal arc summary.

Produced by the Dramatist as part of each segment's JSON output.
Consumed by the Maestro for segment-level stem selection and intensity
scaling rather than reacting block-by-block.

This is the difference between an episode that has competent moment-to-moment
underscore and one that has a musical shape.

| Field | Type |
|---|---|
| `dominant_tone` | `str` |
| `arc_position` | `str` |
| `intensity_curve` | `str` |
| `recommended_music_approach` | `str` |
| `closing_hook_emotional_register` | `str` |

### `SegmentScript`

Complete output of a single Dramatist segment generation call.

This is the JSON-Audio-Map unit: one segment per episode slot (count set
by the season config's segments_per_episode).
All downstream agents (Voice Engine, Foley Master, Maestro, Mixer)
consume this structure.

| Field | Type |
|---|---|
| `segment` | `int` |
| `episode` | `int` |
| `season` | `int` |
| `scene_blocks` | `List[SceneBlock]` |
| `world_ledger_updates` | `List[LedgerUpdate]` |
| `segment_end_hook` | `str` |
| `continuity_warnings` | `List[ContinuityWarning]` |
| `tone_signature` | `Optional[ToneSignature]` |
| `new_locations_introduced` | `List[str]` |
| `segment_closing_character_positions` | `Dict[str, str]` |
| `segment_escalation_level` | `Optional[int]` |
| `crisis_type` | `Optional[str]` |
| `time_elapsed_days` | `int` |
