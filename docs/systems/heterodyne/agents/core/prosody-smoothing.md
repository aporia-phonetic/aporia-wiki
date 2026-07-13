# prosody_smoothing

*Source: `heterodyne/agents/prosody_smoothing.py`*

agents/prosody_smoothing.py

Deterministic per-line emotional glide (item P). Pure code, no LLM.

acoustic_intent.intensity and pace_modifier are authored per line, each in
isolation — so a character can snap from intensity 0.2 to 0.9 between two
consecutive lines. Real emotion ramps and decays; TTS AMPLIFIES the
discontinuity into an "each line acted alone" flatness. This pass eases the
jump between adjacent lines of the SAME character that share the SAME surface
emotion, turning a snap into a ramp. It never touches:

  - a change of speaker (each character's line stands on its own),
  - a change of emotion (a deliberate pivot — grief to anger is allowed to
    jump; that IS the beat),
  - a subtext leak (subtext is an intentional contradiction — left intact),
  - narration between dialogue (resets the run).

So only same-character, same-emotion, no-subtext runs are smoothed — exactly
the case where a large step is authoring noise rather than intent.

## Top-level functions

- **`smooth_blocks()`** — Ease intensity/pace snaps within same-character same-emotion runs.
- **`smooth_segment()`** — Smooth a SegmentScript's scene_blocks. Returns values adjusted.
