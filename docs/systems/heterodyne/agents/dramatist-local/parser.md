# parser

*Source: `heterodyne/agents/dramatist_local/parser.py`*

agents.dramatist_local.parser — plain script text -> SceneBlock-shaped dicts.

Pure and deterministic: no LLM calls, and it never raises on writer output.
Anything it cannot classify is coerced (unknown speaker -> narration) and
counted in the ParseReport so the metrics layer can see parse quality.

Character canonicalization is roster-derived at runtime (build_alias_map),
never hardcoded — this replaces the cloud path's world-specific
_canonicalize_character_names table (a standing CLAUDE.md violation there).

## Defined here

### `ParseReport`

Parse-quality accounting for one segment's transcript.

| Field | Type |
|---|---|
| `total_lines` | `int` |
| `dialogue_blocks` | `int` |
| `narration_blocks` | `int` |
| `foley_blocks` | `int` |
| `parentheticals_stripped` | `int` |
| `inline_hints` | `int` |
| `continuation_joins` | `int` |
| `dropped_lines` | `int` |
| `unknown_speakers` | `Counter` |

## Top-level functions

- **`build_alias_map()`** — Alias (uppercased) -> canonical character name, derived from the
- **`make_block_id()`** — Deterministic ID in the cloud path's format: S{s}E{ee}_SEG{n}_B{iii}.
- **`parse_plain_script()`** — Convert one segment's plain script into SceneBlock-shaped dicts.
- **`apply_voice_seeds()`** — Set voice_seed_id from the roster (authoritative, in place).
