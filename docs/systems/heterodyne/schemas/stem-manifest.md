# stem_manifest

*Source: `heterodyne/schemas/stem_manifest.py`*

Stem manifest schemas.

A stem is a generated music file representing a leitmotif (character, magic
school, season theme, or emotional bed). The registry defines what should
exist; the manifest tracks what does exist on disk after generation.

The Maestro agent reads the manifest at episode-time to resolve music_cue
triggers to actual file paths.

## Defined here

### `StemRegistryEntry`

One row in the registry — declarative description of a stem that should
exist. Drives the generator. Does not represent file state.

| Field | Type |
|---|---|
| `stem_id` | `str` |
| `category` | `str` |
| `trigger_keys` | `list[str]` |
| `leitmotif_description` | `str` |
| `musicgen_prompt` | `str` |
| `duration_seconds` | `float` |
| `target_bpm` | `Optional[int]` |
| `target_key` | `Optional[str]` |
| `is_loopable` | `bool` |
| `notes` | `Optional[str]` |

### `StemManifestRow`

One row in the manifest DB — represents an actual file on disk.
Written by the generator, read by Maestro.

| Field | Type |
|---|---|
| `stem_id` | `str` |
| `category` | `str` |
| `trigger_keys_json` | `str` |
| `file_path` | `str` |
| `duration_seconds` | `float` |
| `sample_rate` | `int` |
| `channels` | `int` |
| `target_bpm` | `Optional[int]` |
| `target_key` | `Optional[str]` |
| `is_loopable` | `bool` |
| `musicgen_prompt` | `str` |
| `musicgen_model` | `str` |
| `generated_at` | `datetime` |
| `file_sha256` | `str` |
