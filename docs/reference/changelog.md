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
