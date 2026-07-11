# beats

*Source: `heterodyne/agents/dramatist_local/beats.py`*

agents.dramatist_local.beats — beat-sheet generation (pipeline stage 1).

One writer-model call (episode scope, default) turns the plot gate + ledger
into 6-10 concrete beats per segment. The tiny JSON schema here is the whole
point: local models that fail on the 19-field SceneBlock handle
{"segments":[{"segment":n,"beats":[...]}]} reliably.

## Defined here

### `SegmentBeats`

| Field | Type |
|---|---|
| `segment` | `int` |
| `beats` | `list[str]` |

### `BeatSheet`

| Field | Type |
|---|---|
| `segments` | `list[SegmentBeats]` |

## Top-level functions

- **`extract_json_object()`** — Strip fences/prose around a JSON object, then parse.
- **`escalation_targets()`** — Per-segment escalation target ranges, generalized to N segments.
- **`crisis_types()`** — Per-segment crisis types: config overrides, else the rotation.
- **`build_segment_plan_block()`** — Human-readable per-segment dramatic plan for the beat-sheet prompt.
- **`generate_beat_sheet()`** — Generate and validate the episode's beat sheet, retrying with error
