# planner

*Source: `heterodyne/agents/writers_room/planner.py`*

agents/writers_room/planner.py

Stage 1 — episode beat planner. ONE call per episode plans all four
segments' scenes, so the episode's structure (setups early, payoff late,
one crisis peak per segment) is globally coherent.
Route: call_type "wr_beat_planner".

## Top-level functions

- **`crisis_types()`** — Per-segment crisis types: config overrides over the default rotation.
- **`plan_episode()`** — Plan the whole episode's beats in one routed call.
