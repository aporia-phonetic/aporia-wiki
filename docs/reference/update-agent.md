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

## Mirrored cheat sheets

Each system repo keeps a root `CHEATSHEET.md` (every terminal command for
that engine). The wiki copy at `systems/<system>/cheatsheet.md` is a
**mirror** — the repo file is the source of truth, and the update Routine
refreshes the mirror. Don't edit the wiki copy.

## The update Routine (daily)

A scheduled Claude Code Remote Routine (`create_new_session_on_fire`,
**daily**, moved from weekly 2026-07-13) does the following each run:

1. Fetches the latest default branch of heterodyne, find, auralbouros,
   godot-pipeline, sophrosyne, and this wiki repo.
2. Compares each source repo's HEAD against the last-synced commit SHA
   recorded in `.wiki-sync-state.json`. Unchanged repos are skipped
   entirely; if nothing changed anywhere, the run exits with no PR.
3. For each changed repo, reviews the diff for **user-facing** changes:
   new/changed CLI flags and scripts, GUI panels/pages/routes, API
   endpoints, npm scripts, env vars, and config keys — then:
   - updates that repo's manuals (`MANUAL.md` / `documents/USER MANUAL/`,
     `README.md`, `STATUS.md`) and `CHEATSHEET.md` to match, via a PR to
     that repo;
   - re-runs `scripts/generate_reference.py`
     (`APORIA_SOURCES_ROOT` points it at the checkouts);
   - refreshes the wiki's `systems/<system>/cheatsheet.md` mirrors and
     updates hand-authored system pages **only** where they now state
     something false (prose style stays human);
   - adds a dated line to the [changelog](changelog.md).
4. Flags — without fixing — repo drift: local/default branches diverged,
   unpushed feature branches, docs referencing files that don't exist.
5. Runs `mkdocs build --strict`; a broken build blocks the PR.
6. Opens **one PR per changed repo** plus one wiki PR (never pushes
   mainline directly), each summarizing what changed and what was
   documented, including the updated `.wiki-sync-state.json` in the wiki
   PR. Nothing auto-merges.

This is the same discipline as heterodyne's own
[world-agnosticism rule](../systems/heterodyne/concepts/world-agnosticism.md)
applied to the tooling that documents it: the generator must read
whatever the source repos currently contain, never encode a specific
world/system's content into the generation logic itself.
