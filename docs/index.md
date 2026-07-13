# Aporia Phonetic Group — Project Wiki

This wiki is the cross-referenced index for everything under **Aporia
Phonetic Group**: the engines and apps ("systems") and the story universe
they produce and run on ("worlds"). It exists so you can start at any
entry point — an agent, a schema, a world, a character — and follow links
to everything connected to it, without digging through four separate
repos.

## Systems

The repos that make up the "launch trio" (+ one parked piece + one
standalone). Each system page includes a **cheat sheet** mirrored from the
repo's root `CHEATSHEET.md` — every terminal command for that engine.

- **[heterodyne](systems/heterodyne/overview.md)** — the engine. Generates
  full audio-drama episodes (script, voice, foley, music, mix) from a
  world + season + plot gates. 100+ agent modules, 25 schema files, 5
  worlds produced so far.
- **[auralbouros](systems/auralbouros/overview.md)** — the public
  companion app ("Sideris Narrative Systems"): podcast player, lore
  archive, card game systems (A.C.E.S./E.C.H.O./H.E.R.O./H.A.R.T.), CYOA
  engine.
- **[godot-pipeline](systems/godot-pipeline/overview.md)** — offline
  render pipeline that turns heterodyne episode JSON into MP4 clips
  (cliffhangers, resolutions, social clips). Currently parked.
- **[find](systems/find/overview.md)** — internal business-ops tool
  ("Founders Input Needed Daily"). No story content of its own; bridges
  to heterodyne for royalties/customer-success data.
- **[sophrosyne](systems/sophrosyne/overview.md)** — standalone personal
  honesty engine (formerly LODESTAR); the World Ledger stack pointed at a
  real person instead of a fictional world.

## Worlds, characters, seasons

The creative output produced by heterodyne, browsable independently of
the engine internals:

- **[Worlds](worlds/index.md)** — one page per world (`caelum_reach`,
  `aetherships`, `verdant_deep`, plus two early-stage stubs), each with
  genre/tone, status, characters, and seasons.
- **[Characters](characters/index.md)** — the global character registry, each
  cross-linked to every world/season they appear in.
- **[Seasons](seasons/index.md)** — per-world season indexes: episodes, plot
  gates.

## Reference

- **[Glossary](reference/glossary.md)** — shared terminology across all
  four systems.
- **[Changelog](reference/changelog.md)** — unified timeline, including
  the verdant_deep → caelum_reach world transition.

## How this wiki stays current

Pages under `systems/*/agents/`, `systems/*/schemas/`, `worlds/`,
`characters/`, and `seasons/` are **generated** by
[`scripts/generate_reference.py`](https://github.com/aporia-phonetic/aporia-wiki/blob/main/scripts/generate_reference.py)
directly from the source repos' docstrings and data files — never
hand-edited. Everything else here is hand-authored and edited normally.
A scheduled agent re-runs the generator and opens a PR when the source
repos change; see [reference/update-agent.md](reference/update-agent.md).
