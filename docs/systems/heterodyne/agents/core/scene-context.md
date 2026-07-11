# scene_context

*Source: `heterodyne/agents/scene_context.py`*

Scene-context extraction for image generation.

Turns an episode JSON + cast into, per distinct location, the data an
ImageRequest needs: a canonical place description and the figures present.
Pure/stateless so it is easy to test and reuse from main.py runners.

Used by --scene-art / --covers / --location-plates / --hero-shots.

## Defined here

### `SceneContext`

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `location` | `str` |
| `characters` | `list[str]` |
| `energy` | `str` |
| `beat` | `str` |

## Top-level functions

- **`world_name()`** — Human-readable world name for fallback text, falling back to the raw
- **`canon_locations()`** — The world's canonical 'visual bible' plates (slug, title) for
- **`humanize()`** — `lower_city_canal_walkway` → `lower city canal walkway`.
- **`location_brief()`** — Canonical place description for an episode location slug, plus the
- **`build_cast_index()`** — Index the cast by BOTH a full-name slug and the leading name token, so a
- **`resolve_character()`** — Map a script character token to its cast entry (exact slug → first-name).
- **`describe_present()`** — `["Magdalene Voss, a lean Black woman ...", ...]` for up to max_n figures
- **`extract_scene_contexts()`** — Group an episode's scene_blocks by location, in first-appearance order.
