# paths

*Source: `heterodyne/schemas/paths.py`*

schemas.paths — Canonical filesystem locations for engine data.

A single source of truth for where worlds, characters, and seasons live on
disk, so the new World / Character / Story decoupling doesn't scatter path
math across scripts, agents, and the GUI. Mirrors the layout the legacy
scripts already use (scripts/bootstrap_world.py:_world_dir), but adds the
new global character registry and per-world instance locations.

Engine core only — never imports from gui/.

## Top-level functions

- **`project_root()`** — Repo root (the AEON-ENGINE directory). schemas/ -> parent.
- **`resolve_world_id()`** — Single source of truth for 'which world is active.'
- **`data_dir()`** — 
- **`worlds_dir()`** — 
- **`world_dir()`** — 
- **`world_config_path()`** — 
- **`deep_ledger_path()`** — 
- **`world_ledger_path()`** — 
- **`world_series_bible_path()`** — Per-world ChromaDB series-bible vector store directory.
- **`sourcebook_json_path()`** — 
- **`sourcebook_md_path()`** — 
- **`world_qa_path()`** — 
- **`world_build_status_path()`** — Small marker file recording the world-build lifecycle stage.
- **`world_locations_path()`** — Per-world location gazetteer (canonical place descriptions + the
- **`world_stem_registry_path()`** — Per-world music stem registry (character leitmotifs, magic/power-
- **`instances_dir()`** — 
- **`instance_path()`** — 
- **`seasons_dir()`** — 
- **`season_dir()`** — 
- **`story_seed_path()`** — 
- **`plot_gates_path()`** — 
- **`season_sourcebook_json_path()`** — Season-scoped sourcebook — same shape as sourcebook_json_path, but
- **`season_sourcebook_md_path()`** — 
- **`console_state_path()`** — The per-world season scaffold the live pipeline reads (main.bootstrap_ledger
- **`characters_dir()`** — 
- **`character_dir()`** — 
- **`character_identity_path()`** — 
- **`character_appearances_path()`** — 
- **`output_dir()`** — 
- **`output_type_dir()`** — output/<type>/<world_id>/ — whole-show root for one output type.
- **`output_season_dir()`** — output/<type>/<world_id>/season_XX/ — season-scoped root for one output type.
