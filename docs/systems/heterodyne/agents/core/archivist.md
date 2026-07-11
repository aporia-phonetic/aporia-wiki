# archivist

*Source: `heterodyne/agents/archivist.py`*

agents/archivist.py

World Ledger manager for the Aeon Pulp Drama Engine.

Responsibilities:
  - Load and commit World Ledger state via SQLite (write-lock pattern)
  - Load plot gate data for the Dramatist
  - Load Series Bible context via ChromaDB
  - Prepare dynamic context block for the Dramatist (episode open)
  - Write-back segment closing positions after each segment
  - Manage the callback registry (SQLite table, active callback list)
  - Classify conflict types at episode open (NarrativeState)
  - Update knowledge states, trust maps, emotional states from episode events
  - Register new locations introduced during generation
  - Filter dead/inactive variables from Dramatist context
  - Process continuity warnings post-generation

Latent Extension additions in this version:
  P1  — KnowledgeState update logic (update_knowledge_state)
  P2  — ContinuityWarning processor (process_continuity_warnings)
  P3  — TrustMap update logic (update_trust)
  P4  — Location registry management (register_new_locations, seal_location, unseal_location)
  P5  — EmotionalState update logic (update_emotional_state)
  P6  — Callback registry SQLite table + management (init_callback_table,
          get_active_callbacks, mark_callback_triggered, mark_callback_resolved)
  P7  — Dead variable filter (get_active_context_variables, deactivate_variable,
          evaluate_reactivation_triggers)
  P8  — Supply depletion (decrement_supplies) — called by Archivist from ledger updates
  P10 — Time/fatigue update (update_time_state)
  P11 — Segment closing position write-back (write_segment_closing_positions)
  NC  — Conflict type classifier (classify_conflict_type)

## Defined here

### `CommitValidationError`

Raised when commit_episode fails due to invalid ledger state.

Subclass of RuntimeError so existing `except RuntimeError` callers still
catch it. main.py catches this specifically to optionally trigger
--repair-commit (Literal-coercion repair).

### `Archivist`

World Ledger manager for the Aeon Pulp Drama Engine.

The Archivist holds the write lock on the World Ledger during all
generation steps. No concurrent writes are possible.

Args:
    ledger_db_path: Path to the SQLite World Ledger database.
    plot_gates_path: Path to the season's plot_gates.json file.
    chroma_path: Path to the ChromaDB series bible vector store.

| Field | Type |
|---|---|
| `_STORY_CIRCLE_BEAT_SIGNALS` | `Dict[int, list]` |

## Top-level functions

- **`get_life_stage()`** — Return the life stage string for an age under the given aging rate.
