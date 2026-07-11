# setups

*Source: `heterodyne/agents/writers_room/setups.py`*

agents/writers_room/setups.py

Setup/payoff registry — the mechanism that makes twists earned.

Setups are planted narrative elements tracked per world+season in
data/worlds/{world_id}/seasons/season_NN/setup_registry.json. The beat
planner receives the open ones and must advance/pay off aging setups; the
ledger extractor reports what the finished segment actually did, and this
module persists the state transitions.

## Top-level functions

- **`registry_path()`** — 
- **`load_setups()`** — Load all setups for a world+season; [] when no registry exists yet.
- **`save_setups()`** — Persist atomically (temp file + rename).
- **`open_setups()`** — 
- **`format_for_prompt()`** — OPEN SETUPS block for the beat planner / extractor user messages.
- **`apply_extraction()`** — Apply the ledger extractor's setup report to the registry state.
