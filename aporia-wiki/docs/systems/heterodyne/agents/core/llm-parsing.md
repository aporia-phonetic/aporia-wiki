# llm_parsing

*Source: `heterodyne/agents/llm_parsing.py`*

agents/llm_parsing.py

Shared tolerant-parsing helpers for LLM output.

Extracted from agents/dramatist.py so any agent (Dramatist, the
writers'-room pipeline stages, judges) can reuse the same repair logic
without importing the Dramatist. The Dramatist's static methods delegate
here, preserving their public names.

These helpers normalize the *presentation variance* of model output —
markdown fences, stray prose around JSON, field-shape drift — so retry
loops only fire on genuine content failures.

## Top-level functions

- **`strip_json_wrapping()`** — Strip markdown fences and leading/trailing prose around a JSON object.
- **`strip_json_array_wrapping()`** — Like strip_json_wrapping but for a top-level JSON array.
- **`normalize_ssml_tags()`** — Normalize scene_blocks[].ssml_tags to List[str] format in place.
- **`normalize_music_cues()`** — Normalize scene_blocks[].music_cue to a MusicCue dict or None in place.
- **`normalize_foley_cues()`** — Normalize scene_blocks[].foley_cues to a non-empty List[str] in place.
- **`normalize_ledger_updates()`** — Ensure world_ledger_updates[] entries carry required fields in place.
- **`parse_json_object()`** — strip_json_wrapping + json.loads, returning the parsed dict.
- **`parse_json_array()`** — strip_json_array_wrapping + json.loads, returning the parsed list.
