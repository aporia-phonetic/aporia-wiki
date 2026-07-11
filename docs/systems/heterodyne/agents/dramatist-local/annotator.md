# annotator

*Source: `heterodyne/agents/dramatist_local/annotator.py`*

agents.dramatist_local.annotator — audio-production metadata pass.

Fills the SceneBlock fields the writer deliberately did not produce:
foley_cues, scene_energy, music_cue, duration estimates, social/merch
flags. Behavior per metadata mode:

  derive — every narration/dialogue block goes through batched annotator
           calls; standalone foley blocks don't exist.
  hints  — writer-authored [bracket hints] became foley blocks / inline
           cues in the parser; the annotator refines hint text into cue
           phrases and derives the rest exactly like derive mode.
  author — the writer produced full SceneBlocks already; this module is
           skipped entirely (see agent.py).

Annotation is best-effort by design: a failed batch degrades to defaults
(medium energy, ambient cues) rather than failing the episode — these are
"intent" fields the Foley Master and Maestro re-resolve downstream.

## Top-level functions

- **`estimate_durations()`** — Deterministic duration heuristic, in place.
- **`annotate_blocks()`** — Batched foley/energy/music annotation over spoken blocks, in place.
- **`refine_hint_cues()`** — hints mode: turn raw writer hints ("timbers straining") on foley
- **`pick_social_posts()`** — One call per segment: flag up to 2 pull-quote dialogue lines.
- **`annotate_segment()`** — Full metadata pass for one segment's parsed blocks (derive/hints).
