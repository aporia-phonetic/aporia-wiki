# leitmotif

*Source: `heterodyne/agents/leitmotif.py`*

agents/leitmotif.py

Character leitmotif wiring (item L). Deterministic, world-agnostic, pure code.

Leitmotifs were defined but never fired: each character declares a
`stem_trigger` and a `leitmotif_description` in the world's console_state, and
the stem manifest ships `<name>_leitmotif` stems for some casts — but nothing
emitted a leitmotif music cue on a character's beats, so a character's theme
never returned across a season (one of the strongest cross-season
emotional-consistency devices in scored drama).

This module:
  - builds a world-agnostic leitmotif map (CHARACTER → trigger) from the roster
    the ledger already carries (stem_trigger, else `<name>_leitmotif`);
  - injects a subtle, ducked leitmotif music cue at each main character's FIRST
    appearance in the episode — a musical entrance — without disturbing any
    cue the script already authored.

Nothing here assumes a specific cast: it reads whatever the active world's
roster declares. A cue whose stem is absent from the manifest is simply silent
downstream (harmless) and lights up automatically once the stem exists — see
Maestro._resolve_trigger's leitmotif fallback.

## Top-level functions

- **`build_leitmotif_map()`** — CHARACTER(upper) → leitmotif trigger, from the living roster.
- **`inject_first_appearance_leitmotifs()`** — Insert a ducked leitmotif cue before each character's first line.
