# lint

*Source: `heterodyne/agents/dramatist_local/lint.py`*

agents.dramatist_local.lint — deterministic prose lint for the local pipeline.

A thin bridge to the Writers' Room linter (agents.writers_room.prose_lint):
same AI-tell lexicon, same banned constructions, zero LLM cost. Runs on each
segment's raw transcript inside the judge loop, so lexicon hits can gate
regeneration exactly like fidelity flags (LOCAL_LINT_ACTION=regen) or be
recorded in SEG{n}_judge.json (the default, report).

## Top-level functions

- **`transcript_lint_lines()`** — Convert a plain tagged transcript into the linter's line dicts.
- **`run_transcript_lint()`** — 
- **`lint_report_dict()`** — JSON-serializable form for SEG{n}_judge.json / episode reports.
