# prose_lint

*Source: `heterodyne/agents/writers_room/prose_lint.py`*

agents/writers_room/prose_lint.py

Deterministic prose linter — pure code, zero LLM cost, runs on every draft
scene. Catches what no single-call prompt can see:

  - AI-tell lexicon hits (single source: data/style/ai_tell_lexicon.txt,
    shared with the generation prompts)
  - banned constructions (em-dash chains, present-participle narration
    openers, "not X, but Y" hinges)
  - sentence-length uniformity and repeated consecutive openers
  - cross-episode n-gram repetition against recent episodes' scripts

Output feeds the scene critic's notes; hard violations (lexicon hits)
trigger a mechanical retry even when the critic stage is disabled.

## Defined here

### `LintReport`

Result of linting one scene's lines.

| Field | Type |
|---|---|
| `lexicon_hits` | `list[dict]` |
| `construction_hits` | `list[dict]` |
| `variance_issues` | `list[dict]` |
| `repetition_hits` | `list[dict]` |

## Top-level functions

- **`load_lexicon()`** — Load the AI-tell lexicon (one term per line, '#' comments).
- **`lint_lines()`** — Lint one scene's lines: [{'character','type','text'}, ...] (1-indexed
- **`build_recent_ngrams()`** — Collect word n-grams from the most recent committed episode scripts.
- **`check_repetition()`** — Flag lines that reuse an n-gram from a recent episode. Common
