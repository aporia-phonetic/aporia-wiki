# dialogue_memory

*Source: `heterodyne/agents/dialogue_memory.py`*

agents/dialogue_memory.py — per-character dialogue memory (C4).

Write side (Archivist, at episode commit): every committed dialogue line by
character into world_ledger.db's ``dialogue_history`` table.

Read side (context builders, read-only): top-k prior lines per character,
scored by recency plus lexical overlap with an optional query (the episode
gate) — no embeddings needed at this scale. Injected into voice briefs so
generation hears how a character has *actually sounded*, enabling callbacks
and voice continuity beyond descriptions.

World-agnostic: keys on character/voice tags and the world_id column only.

## Top-level functions

- **`record_lines()`** — Store all dialogue lines of a committed episode. Re-commits of the
- **`recent_lines()`** — Top-k prior lines for a character: recency-ordered pool, re-ranked by
