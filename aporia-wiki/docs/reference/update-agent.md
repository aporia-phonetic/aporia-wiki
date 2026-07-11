# How this wiki stays current

Two different maintenance paths, by page type:

## Generated pages

`systems/*/agents/`, `systems/*/schemas/`, `worlds/`, `characters/`, and
`seasons/` are built by
[`scripts/generate_reference.py`](https://github.com/aporia-phonetic/aporia-wiki/blob/main/scripts/generate_reference.py).
It reads module docstrings/class fields (via `ast`, never imports the
code) out of heterodyne, auralbouros, godot-pipeline, and find, plus
`world_config.json`/`identity.json`/`appearances.json`/`plot_gates.json`
data files, and renders one markdown page per entity. The script holds
no world/system-specific content itself — only the path list to the four
source repos — so re-running it against updated source repos regenerates
these pages mechanically. **Don't hand-edit files under these paths** —
edits will be overwritten on the next generator run.

## Hand-authored pages

Everything else (overviews, concept pages, the glossary, this page) is
written and maintained like normal documentation. Edit these directly.

## The update Routine

A scheduled Claude Code Remote Routine (`create_new_session_on_fire`,
weekly) does the following each run:

1. Pulls the latest default branch of heterodyne, auralbouros,
   godot-pipeline, find, and this wiki repo.
2. Compares each source repo's tracked paths (`agents/*.py`,
   `schemas/*.py`, `data/worlds/*`, `data/characters/*`, find's agent
   modules, godot-pipeline's `compositor/`) against the last-synced
   commit SHA recorded in `.wiki-sync-state.json`.
3. Re-runs `scripts/generate_reference.py` if anything changed.
4. Leaves hand-authored pages untouched — only notes in the PR body if
   their source material (e.g. a system's README) moved, so a human can
   decide whether to update the prose.
5. Opens **one PR** per run summarizing what changed and why (e.g.
   "heterodyne@abc123 added agents/foo.py → new page"), including the
   updated `.wiki-sync-state.json`. Nothing auto-merges.

This is the same discipline as heterodyne's own
[world-agnosticism rule](../systems/heterodyne/concepts/world-agnosticism.md)
applied to the tooling that documents it: the generator must read
whatever the source repos currently contain, never encode a specific
world/system's content into the generation logic itself.
