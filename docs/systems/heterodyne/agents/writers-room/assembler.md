# assembler

*Source: `heterodyne/agents/writers_room/assembler.py`*

agents/writers_room/assembler.py

Stage 6 — pure code, no LLM. Assembles draft scenes + annotations +
extraction into a validated SegmentScript:

- deterministic block_ids (S{s}E{ee}_SEG{n}_B{nnn}) — kills ID drift
- voice_seed_id assignment from the cast roster (same mapping discipline
  as Dramatist._apply_voice_seeds; the model never touches seeds)
- duration estimates by words-per-minute heuristic (no LLM needed)
- final Pydantic validation through the same SegmentScript schema the
  monolith emits

## Top-level functions

- **`build_voice_map()`** — Name-token → VS-ID map from the bridged roster (same logic as the
- **`resolve_voice_seed()`** — 
- **`assemble_segment()`** — Assemble one segment's scenes into a validated SegmentScript.
