# sourcebook_ingest

*Source: `heterodyne/agents/sourcebook_ingest.py`*

agents.sourcebook_ingest — the publish -> edit -> feed-back canon loop (B6).

A compiled sourcebook.md is meant to be edited by a human: worldbuilding is
editorial work, and the world-first pipeline treats the edited book as canon.
Recompiling from the deep ledger would silently clobber those edits, so this
module makes them durable:

  * every compile snapshots exactly what it wrote (sourcebook.md.pristine);
  * ``aeon world ingest`` diffs the current file against that snapshot,
    section by section (``## `` headings), and stores changed sections in
    canon_overrides.json next to the sourcebook;
  * every later compile re-applies the overrides after rendering, so
    human-edited sections win over regenerated machine text;
  * episode context (dramatist_local.context.build_sourcebook_context)
    injects the stored override text as the highest-authority canon block,
    so the writer and the world judge both see the human edits.

Overrides are markdown-level and colocated with the file they govern
(world-level or season-scoped). sourcebook.json stays machine-truth;
sourcebook.md is the human-facing canon. Nothing here knows any world.

## Top-level functions

- **`pristine_path()`** — 
- **`overrides_path()`** — 
- **`split_sections()`** — Ordered (key, text) pairs; text includes the ``## `` heading line.
- **`load_overrides()`** — {section_key: {"text": ..., "ingested_at": ...}} or {}.
- **`save_overrides()`** — 
- **`apply_overrides()`** — Re-impose stored human edits on freshly rendered markdown.
- **`snapshot_pristine()`** — Record exactly what was just written — the diff base for ingest.
- **`set_baseline()`** — Accept the current file as the machine baseline (bootstrap for
- **`ingest()`** — Diff the (human-edited) sourcebook against the pristine snapshot and
- **`clear_overrides()`** — Drop one stored override (by ``## `` heading text) or all of them.
- **`overrides_context_block()`** — Human-edited canon as a context block, clipped to a line boundary at
