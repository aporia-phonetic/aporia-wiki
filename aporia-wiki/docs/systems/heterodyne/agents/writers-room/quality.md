# quality

*Source: `heterodyne/agents/writers_room/quality.py`*

agents/writers_room/quality.py

Scene-grain quality stages:

- Scene critic (call_type "wr_scene_critic"): one round of self-refine.
  Concrete, line-referenced notes → the scene writer applies them in one
  revision pass.
- Blind voice attribution (call_type "wr_voice_attribution"): the prompt's
  "unlabeled voice test" made measurable. Speaker labels stripped, a cheap
  judge attributes each dialogue line; accuracy below threshold means the
  voices are converging.

## Top-level functions

- **`critique_scene()`** — Return (verdict, notes). Failure degrades to ('pass', []) — the
- **`attribution_accuracy()`** — Blind-attribute the scene's dialogue lines; return accuracy in
- **`distinctness_note()`** — The note fed into a regeneration pass when voices converge.
