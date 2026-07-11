# intentions

*Source: `heterodyne/agents/writers_room/intentions.py`*

agents/writers_room/intentions.py

Stage 2 — actor intentions: the actors-advise-playwright-writes hybrid.
For each character in a scene, one tiny parallel call produces their
private wants / hides / would-do, scoped to what THEY know. The scene
writer receives these as advisory material; the friction between agendas
is what makes dialogue feel inhabited rather than orchestrated.
Route: call_type "wr_actor_intention" (local-recommended — tiny calls).

## Top-level functions

- **`gather_intentions()`** — Fire one intention call per non-narrator character in the scene,
- **`format_intentions()`** — ACTOR INTENTIONS block for the scene-writer user message.
