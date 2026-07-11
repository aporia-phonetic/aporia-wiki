# foley_sourcer

*Source: `heterodyne/agents/foley_sourcer.py`*

agents.foley_sourcer — multi-backend foley audio acquisition.

Replaces stub catalog entries with real audio sourced from external
services. Three backends ship in this phase:

  • FreesoundSourcer    — search freesound.org, download CC-licensed audio
  • AudioCraftSourcer   — generate locally via Meta AudioCraft (free, GPU)
  • ElevenLabsSourcer   — generate via ElevenLabs API (paid, fast, fallback)

The orchestrator (BestOfThree) tries them in order, respecting the
toggles in .env. First success wins; on each failure it falls through
to the next enabled backend.

Public surface:

    sourcer = build_sourcer_from_env(catalog)
    if sourcer is not None:
        result = sourcer.source(catalog_entry)
        # entry's audio is now on disk + catalog row updated atomically

The catalog is the single source of truth; this module never modifies
catalog rows except via FoleyCatalog.update_file_path. Spending caps
are enforced per-call; an over-cap call raises and does not write.

Important: the sourcer NEVER deletes existing audio. If a catalog entry
already has source != 'stub', re-sourcing replaces the file (after
backing up the old one with a .bak extension) but the catalog row is
updated atomically so callers always see consistent state.

## Defined here

### `SourcerError`

Base class for sourcing failures.

### `BackendUnavailableError`

A backend can't run (missing API key, missing GPU, etc.).

### `BackendFailedError`

A backend ran but couldn't produce audio.

### `SpendingCapExceededError`

A paid backend would push monthly spend over the cap.

### `SourcerDisabledError`

Master toggle is off.

### `SourceResult`

Outcome of a successful sourcing call.

Attributes describe both what happened and what it cost so callers
can audit and accumulate.

| Field | Type |
|---|---|
| `catalog_id` | `str` |
| `backend_name` | `str` |
| `file_path` | `Path` |
| `license` | `CatalogLicense` |
| `attribution` | `str | None` |
| `source_url` | `str | None` |
| `source_query` | `str` |
| `cost_usd` | `float` |
| `duration_seconds` | `float` |
| `notes` | `str | None` |

### `SourcerBackend`

One audio-acquisition strategy.

Implementations must:
  • Be safe to construct without side effects (no API calls in __init__)
  • Surface availability via .is_available() — checked before .source()
  • Write the audio to disk at the requested path before returning
  • Raise BackendFailedError on any error after .source() begins so
    the orchestrator can fall through to the next backend

| Field | Type |
|---|---|
| `name` | `str` |

### `FreesoundSourcer`

Search and download CC-licensed audio from freesound.org.

Uses the v2 API: https://freesound.org/docs/api/

License policy: only CC0, CC-BY, and CC-BY-SA are accepted. CC-BY-NC
is rejected — the show is intended to be commercially distributable.
Attribution is recorded for CC-BY/CC-BY-SA so we can comply when
publishing.

Search strategy:
  1. Build query from entry family + tags
  2. Filter by duration_seconds proximity (±50% of target)
  3. Filter by licenses ∈ {Creative Commons 0, Attribution, Attribution NonCommercial → reject}
  4. Sort by 'rating_avg' descending
  5. Take top result; download; normalize to 24kHz mono WAV

### `AudioCraftSourcer`

Generate audio locally via Meta's AudioCraft (AudioGen model).

Cost: free. Speed: 30-60 seconds per generation on consumer GPU,
several minutes on CPU. Quality varies — best for sustained
atmospheric sounds (drones, ambient beds), weaker for sharp
discrete events (footsteps, clicks).

Lazy imports because AudioCraft + torch is a heavy dependency that
not every install will have. is_available() returns True only after
a successful import probe.

### `ElevenLabsSourcer`

Generate audio via ElevenLabs Sound Effects API.

Cost: ~$0.08/effect (varies by plan). Fast (5-15s per effect).
Highest quality on-demand option, used as last-resort fallback.

API docs: https://elevenlabs.io/docs/api-reference/sound-effects/text-to-sound-effects

### `BestOfThree`

Orchestrates multiple backends with toggle-aware fallback.

Order: Freesound → AudioCraft → ElevenLabs (free → free local → paid).
Each disabled backend is skipped. First successful backend wins.

Wraps the catalog so a successful sourcing automatically calls
`catalog.update_file_path` to register the result. The catalog stays
consistent: either the entry has the new file + new source/license,
or nothing changed.

Spending tracking:
  • Each backend reports cost_usd_per_call
  • Orchestrator accumulates spend across calls
  • If next backend would push total over `spending_cap_usd`, the
    orchestrator skips that backend and tries the next
  • If all backends are skipped or fail, raises BackendFailedError

## Top-level functions

- **`build_sourcer_from_env()`** — Construct a BestOfThree orchestrator from environment variables.
