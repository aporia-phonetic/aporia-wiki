# scene_writer

*Source: `heterodyne/agents/writers_room/scene_writer.py`*

agents/writers_room/scene_writer.py

Stage 3 — the scene writer: dialogue and narration ONLY, one call per
scene. The single authorial mind that keeps drama coherent; everything
production-related happens in later passes.
Route: call_type "wr_scene_writer" (the strongest model you have; the last
stage to migrate off cloud).

Includes the revision loop: the prose linter runs on every draft (free),
and when the critic stage is enabled its notes drive ONE revision pass.
Hard lexicon violations trigger a mechanical retry even with the critic
disabled.

## Top-level functions

- **`build_user_message()`** — 
- **`parse_draft()`** — 
- **`write_scene()`** — 
- **`lint_and_retry()`** — Run the deterministic linter; on hard violations (banned lexicon),
- **`revise_with_notes()`** — ONE revision pass driven by critic notes. Failure keeps the draft.
