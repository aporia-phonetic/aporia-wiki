# novelist

*Source: `heterodyne/agents/novelist.py`*

agents/novelist.py — The Novelist (Agent 17)

Expands episode scripts into full prose chapters for serialized fiction.

Takes the Dramatist's episode JSON (4 segments of scene blocks with dialogue,
narration, and stage directions) and produces a prose chapter that:
  - Preserves all dialogue verbatim
  - Adds interior monologue, sensory detail, and emotional subtext
  - Reads as self-contained serialized fiction

Outputs (caller passes output_dir=schemas.paths.output_season_dir("prose", world_id, season)):
  {output_dir}/S{S}E{E:02d}/{lang}/chapter.md    Markdown source
  {output_dir}/S{S}E{E:02d}/{lang}/chapter.epub  EPUB file

Languages: uses the same 7-language codes as the Translation Agent.
If only_english=True is set, skips the multilingual fan-out.

Publishing scope (what this agent automates):
  - Gumroad: direct EPUB sale (via the Vendor agent when wired)
  - All other platforms (KDP, Wattpad, Royal Road, Scribd): manual upload
    using the generated EPUB files. Platform APIs are not publicly available.

## Defined here

### `NovelistReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `season` | `int` |
| `episode` | `int` |
| `languages_completed` | `list[str]` |
| `languages_failed` | `list[str]` |
| `output_paths` | `dict[str, Path]` |
| `word_count_en` | `int` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `Novelist`

Expands episode scripts into serialized prose chapters.

Parameters
----------
data_dir:
    Path to data/worlds/ root.
output_dir:
    Base output directory. Prose files go to {output_dir}/prose/.
    Defaults to exports/.
llm_router:
    A LLMRouter instance. If None, build_default_router() is used.
only_english:
    If True, only produce the English chapter (skip 6-language fan-out).
stub:
    If True, skip LLM calls and write placeholder prose (for testing).

## Top-level functions

- **`main()`** — 
