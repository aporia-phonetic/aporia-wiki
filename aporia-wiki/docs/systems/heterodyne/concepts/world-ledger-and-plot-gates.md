# World Ledger & Plot Gates

## World Ledger

The World Ledger (`schemas/world_ledger.py`) is the engine's persistent
narrative memory — the reason Episode 12 remembers what happened in
Episode 3. It's a single schema covering:

- **Knowledge State** — who knows what, and how confidently (confirmed →
  observed → suspected → rumored, decaying over in-world time).
- **Trust Map** — directional trust between characters, independent of
  raw relationship "bond strength."
- **Emotional Baseline** — each character's baseline vs. current
  emotional affect.
- **Location Registry** — named locations with status flags (sealed,
  active, discovered...).
- **Resource Inventory / Time & Fatigue** — supplies, elapsed hours,
  fatigue level.
- **Callback Registry** — a SQLite-backed table of planted narrative
  threads and whether they've been triggered/resolved.
- **World Clock / Temporal Position** — authoritative in-world time and
  whether the story is being told from the present, historically, or
  across multiple eras.

The [`archivist`](../agents/core/archivist.md) agent owns reading,
committing, and updating the Ledger (write-lock pattern over SQLite) and
assembles the dynamic context block the Dramatist reads at the start of
each episode.

## Plot Gates

A season's story structure is expressed as **plot gates** — the
`{world_id}/seasons/{season_id}/plot_gates.json` file per season. Each
gate is a narrative checkpoint the season's episodes need to pass
through; the Dramatist consumes gate data (loaded by the Archivist) to
know what has to happen and in what order, while still generating the
actual scene-by-scene prose freely within those constraints.

See the [Seasons](../../../seasons/index.md) pages for the plot-gate counts and
episode lists of produced seasons.
