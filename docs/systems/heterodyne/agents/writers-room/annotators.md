# annotators

*Source: `heterodyne/agents/writers_room/annotators.py`*

agents/writers_room/annotators.py

Stage 4 — audio annotation over finished text: foley cues, optional foley
events, sparse music cues, per-line acoustic intent. Pure tagging — far
more reliable than asking the writer to emit production metadata while
composing dialogue, and cheap enough for a local model.
Route: call_type "wr_annotator_audio".

Annotations are applied leniently: a malformed foley_event or music_cue is
dropped (logged), never fatal — the assembler's defaults keep every block
valid.

## Top-level functions

- **`annotate_scene()`** — Return {line_number: annotation_dict}. Empty dict on total failure —
- **`apply_annotation_to_block()`** — Merge one line's annotation into a raw SceneBlock dict, leniently.
