# Changelog

A cross-system timeline. heterodyne's own version-by-version changelog
(`documents/USER MANUAL/AEON_PULP_DRAMA_ENGINE_USER_MANUAL.md` §33, v1.0.0
through v2.3) is the detailed record for the engine specifically — this
page pulls out the entries that matter for wiki cross-references
(world transitions, cross-system integration points) rather than
reproducing every release.

## World transitions

- **`verdant_deep` → `caelum_reach`** — `verdant_deep` was the original
  prototype world; `caelum_reach` is the world currently in active
  production. `verdant_deep`'s config and legacy console state remain on
  disk (see the [verdant_deep](../worlds/verdant_deep.md) page) but
  active work targets `caelum_reach`. Key git history:
  - `519eda3` — "Fix prototype-world assumptions hardcoded into engine
    code" — the general world-agnosticism cleanup commit (see
    [World-agnostic engine code](../systems/heterodyne/concepts/world-agnosticism.md))
  - `31a0cec` — "Fix world-agnostic violation in music stem registry; add
    Caelum Reach stems"
  - `9392a17` — "Fix trust_map silent-drop + genericize two hardcoded
    Verdant Deep prompt examples"
  - `c51ba34` — "fix(worlds): normalize world_config.json to the
    canonical WorldConfig schema"
  - `_LEGACY_DEFAULT_WORLD_ID = "verdant_deep"` still lives in
    `schemas/paths.py::resolve_world_id` as a last-resort fallback — not
    a genre default, just a bootstrap artifact from before `WorldConfig`
    existed.

## 2026-07-13 — ecosystem consolidation

Everything brought to mainline and documented in one pass:

- **heterodyne** — GUI v2.2 engine catch-up: ⏰ Automation clock panel
  (wires the previously-orphaned scheduler core + publication buffer),
  🎨 Art Kit, 📕 Novelist, Writers'-Room/quality-tier/QA-toggle pipeline
  controls, ambient-bed in Mixer; "Scheduler" tab renamed **Channels**.
  Manual set refreshed (TAB_REFERENCE v2.2, DOCUMENTATION_INDEX v2.4).
- **find** — Votes + Clock pages, fleet/lore visibility, AOL→FIND frontend
  rebrand; first README; ARCHITECTURE §5b for the post-rename subsystems.
- **auralbouros** — real README (was a one-line stub); STATUS refreshed.
- **godot-pipeline** — MANUAL regenerated against the implemented B1/B2
  code (the old one described an empty scaffold); still parked.
- **sophrosyne** — LODESTAR→SOPHROSYNE rename finished in MANUAL
  (env vars were documented wrong).
- **Every repo** gained a root `CHEATSHEET.md` (mirrored on each system's
  wiki page); this wiki's generator paths became env-configurable
  (`APORIA_SOURCES_ROOT`); the update Routine moved from weekly to
  **daily** (see [update agent](update-agent.md)).

## 2026-07-14 — heterodyne: character authoring, dialogue memory, pressure-engine scaffold

- Multi-pass character authoring (`agents/character_author.py`): idiolect
  card + in-voice sample + blind-distinctness judge on top of character
  generation, env-gated (`CHARACTER_AUTHOR_DEEP`, default on).
- Dialogue memory (`agents/dialogue_memory.py`): per-character line
  history recorded automatically at every Archivist commit, fed into
  voice briefs.
- Homeostatic pressure engine scaffolded (`schemas/pressures.py`,
  `agents/pressure_engine.py`) — decaying drives + desensitizing moral
  costs — but not yet wired into generation; `CharacterExtension`'s new
  `pressure_state` field defaults to `None`/no-op.
- New Chronicle system reference doc landed in heterodyne
  (`docs/CHRONICLE_SYSTEM.md`, not mirrored into this wiki); sourcebook
  compilation now runs an automatic season-scoped World QA gate (logs,
  doesn't block) and can render a Gazetteer section from `locations.json`.
- `scripts/run_phase4.py` gained `--world-id`/`--pipeline`/`--run-label`
  flags in place of a hardcoded world default.

## heterodyne engine (selected — full log in the manual §33)

- **v2.3 (2026-06-28)** — ZONOS2 adopted as the production voice-cloning
  engine (won the TTS bake-off on speaker similarity + WER), Chatterbox
  as fallback; CLAP-based foley library ingest replaces Freesound; 48 kHz
  full pipeline.
- **v2.0 (2026-05-19)** — GUI tab consolidation (15 → 5 top-level tabs);
  `BatchConfig` slimmed from 30 fields to 9 as part of a single-source-
  of-truth cleanup; new 3-page Season wizard.

## Other systems

- **auralbouros** — A.C.E.S. engine at Revision 3 ("Universal 21") in
  code, while `docs/AURALBOUROS MANUAL.md` still documents the older
  Revision 2 rules. See
  [Game systems](../systems/auralbouros/game-systems.md) for the
  divergence.
- **godot-pipeline** — B2 Track 0 (schema reconciliation) completed
  2026-06-29: `compositor/episode_to_scene.py` reconciled to the live
  heterodyne episode schema. Repo otherwise parked per its `STATUS.md`.
