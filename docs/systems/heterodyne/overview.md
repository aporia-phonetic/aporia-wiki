# heterodyne — Aeon Pulp Drama Engine

The engine. Feed it a cast of characters, a story structure (plot gates),
and a world description; it produces a complete, broadcast-ready audio
drama episode: script, voice-acted dialogue, foley, music cues, a final
mixed MP3, and updated world state so later episodes remember what
happened earlier. A full 12-episode season takes roughly 8–16 hours of
compute and $10–$40 in API costs.

Branded externally as *Sideris Narrative Systems / Axiom Synthetic
Pipeline*.

## Shape of the codebase

| Area | Size | Purpose |
|---|---|---|
| [`agents/`](agents/core/index.md) | ~78 modules + 2 subpackages | One module per production role (Dramatist, Archivist, Mixer, Voice Engine, Foley pipeline, Translation, Publisher...) |
| [`agents/dramatist_local/`](agents/dramatist-local/index.md) | 12 modules | Self-hosted local-LLM rewrite of the Dramatist, multi-pass (beats → draft → judge → checkpoints) |
| [`agents/writers_room/`](agents/writers-room/index.md) | 15 modules | Alternate opt-in scripted pipeline (planner → scene writer → season architect → prose lint → quality) |
| [`schemas/`](schemas/index.md) | 25 modules | Pydantic data models — the contracts between agents |
| `data/worlds/{world_id}/` | 5 worlds | Per-world config, sourcebook, seasons, episodes, ledgers |
| `data/characters/{character_id}/` | global registry | Character identity + cross-world appearances |
| `gui/` | — | PyQt production console |
| `aeon.py` | — | Unified CLI (`aeon world create/build/chronicle/sourcebook/list/show`) |

See [Agent reference](agents/core/index.md) and [Schema reference](schemas/index.md) for
the generated per-module pages.

## Core concepts

- **[World-agnostic engine code](concepts/world-agnosticism.md)** — the
  architecture rule that keeps `agents/`, `schemas/`, `config/`, and
  `main.py` free of any specific world's genre, era, or names.
- **[World Ledger & Plot Gates](concepts/world-ledger-and-plot-gates.md)**
  — how the engine remembers state across episodes and structures a
  season's story.
- **[CLI & LLM routing](concepts/cli-and-routing.md)** — `aeon.py`, the
  LLM router, and `resolve_world_id`.

## Operations

Runbooks for standing up and operating the engine live in
[operations.md](operations.md) — cold start, hardware migration,
secrets, TTS backend setup, known issues.

## Existing deep-dive docs (not mirrored here)

The engine repo already carries a full user-manual suite at
`documents/USER MANUAL/` (README, quick start, tab reference,
troubleshooting/FAQ, and an 1700-line manual with its own glossary and
changelog) — that stays the canonical *operator* manual. This wiki
complements it with cross-linked reference/lore browsing; it doesn't
replace it.
