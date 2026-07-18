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

## 2026-07-15 — heterodyne: sourcebook re-ingest, beat-level regen surgery, GPU routing

- Sourcebook re-ingest loop: `aeon.py world ingest <world_id> [--season N]`
  (`agents/sourcebook_ingest.py`, new) captures human edits to a compiled
  `sourcebook.md` as `canon_overrides.json`, colocated with the file it
  governs. Every later compile re-applies stored overrides after
  rendering, and `build_sourcebook_context()` injects them into episode
  context as a highest-authority CANON OVERRIDES block — human edits
  survive recompiles and reach generation, not just the document.
  `--baseline`/`--clear SECTION`/`--clear-all` round out the loop.
- Local Dramatist beat-level regeneration surgery
  (`LOCAL_SURGICAL_REGEN`, default on): when a gating flag maps onto a
  beat span, only the flagged tail regenerates instead of the whole
  segment; falls back to whole-segment regen when a flag can't be pinned
  to a beat.
- `config/llm_routing.local.yaml`'s `local_32b`/`local_gemma26` backends
  now read `${OLLAMA_GPU_URL:-http://localhost:11434}` and set a fixed
  `timeout: 1800`, for pointing the local-LLM routes at a remote GPU host.

## 2026-07-16 — heterodyne: TTS shootout (Qwen3-TTS), image-gen genre-neutralization

- TTS shootout benchmarked 8 free TTS engines against ZONOS2 on a shared
  50-line segment (`docs/TTS_SHOOTOUT_2026-07.md`). **Qwen3-TTS**
  (x-vector cloning) came within 0.018 speaker-similarity of ZONOS2 with
  the field's best WER and is now wired in as an available `tts_backend`
  (`agents/tts_client.py::Qwen3TTS`, `scripts/qwen3tts_server.py`) —
  ZONOS2 remains the production default; no cast seed switched. Also
  added: an opt-in render-verify-reroll QA loop
  (`ENABLE_RENDER_QA_LOOP`) and ZONOS2 server-side speaker-embedding
  caching.
- Image-gen genre-neutralization fix: `agents/image_agent.py` /
  `agents/animator.py` / `agents/video_compositor.py` had a 1930s/pulp
  aesthetic hardcoded into engine code, firing for every world regardless
  of declared genre — the exact bug shape [World-agnostic engine
  code](../systems/heterodyne/concepts/world-agnosticism.md) warns about.
  Fixed by genre-neutralizing the engine fallbacks, adding a
  `portrait_style` key to `image_style.json`, and moving Animator's
  per-location camera templates into per-world
  `data/worlds/<id>/camera_directions.json`. Also wired the previously-
  unused IP-Adapter FaceID/LoRA machinery into `--character-art` so a
  cast member's bust/full/action shots share one face reference.

## 2026-07-18 — heterodyne: image-gen subject-truncation fix, local-pipeline character-intro fix

- Image-gen subject-truncation fix: CLIP's 77-token-per-encoder limit meant
  a long, freely-edited world style banner could push the actual
  per-request subject (which character, which named vessel/location) past
  the truncation point, silently collapsing every request of that image
  type to the same generic result — confirmed happening for both
  `PORTRAIT` and `SCENE_SNAPSHOT`. Every `image_type` with per-request
  identifying content now leads with that content and carries the style
  banner as a secondary qualifier (only `MERCH` still leads with the
  banner). Adds a `location_plate_style` key to `image_style.json`
  (`IMAGE_LOCATION_PLATE_STYLE` env override) as a dedicated look for
  `--location-plates`, separate from `house_style`/`portrait_style`;
  `--covers` scene descriptions now thread in the episode's plot-gate
  title/hook and dominant tone; `--hero-shots` now prefers a character's
  own `action_setting` override over a scene-derived location brief.
- Local-pipeline character-intro + season-1 world-scoping fix: the local
  Dramatist's `orientation_opening_beat()` only forced the strong
  character-introduction treatment for series/season premieres, so an
  ordinary mid-season debut fell back to a system-prompt-only instruction
  and produced unnamed dialogue — now fires for any debut.
  `bootstrap_ledger()`'s season-1 path also unconditionally skipped a
  world's own `console_state_1.json` scaffold and fell back to
  `WorldLedger.episode_1_baseline()` (Verdant Deep's seed state) for every
  world; the scaffold lookup is now scoped to the active world via
  `resolve_world_id()`.

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
