# letterer

*Source: `heterodyne/agents/letterer.py`*

agents/letterer.py — The Letterer (Agent 18)

Converts scene images + dialogue into fixed-grid webcomic pages with speech balloons.

Phase 1 scope (current):
  - Fixed 2×2 panel grid per page
  - Sequential dialogue placed in speech balloons in scene order
  - Character portrait insets as speaker indicators
  - Output: PNG pages + ZIP bundle

Phase 2 (hardware day, deferred):
  - Spatial balloon placement aligned to character faces
  - Requires local object detection (YOLO / Grounding DINO) for bounding boxes
  - DALL·E 3 / FLUX return no spatial metadata — auto-placement is impossible without it

Platform note:
  Webtoon and Tapas have no creator APIs for submission.
  Output files are formatted for manual upload:
    - Webtoon: 800×1280px vertical strip format
    - Tapas: standard comic page format

Dependencies:
  Pillow    pip install Pillow

## Defined here

### `ComicPanel`

| Field | Type |
|---|---|
| `panel_index` | `int` |
| `scene_image_path` | `Optional[Path]` |
| `speaker` | `str` |
| `dialogue` | `str` |
| `location` | `str` |
| `portrait_path` | `Optional[Path]` |

### `LettererReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `season` | `int` |
| `episode` | `int` |
| `panels_rendered` | `int` |
| `pages_rendered` | `int` |
| `output_paths` | `dict[str, str]` |
| `warnings` | `list[str]` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `Letterer`

Fixed-grid webcomic page generator.

Parameters
----------
data_dir:
    Path to data/worlds/ root (for episode JSON).
image_dir:
    Base directory for scene images and portraits, e.g.
    schemas.paths.output_type_dir("images", world_id).
portrait_dir:
    Directory for character portrait images.
    Defaults to {image_dir}/portraits/.
output_dir:
    Comic files go directly under this directory (caller is expected to
    pass an already type/world/season-scoped path, e.g.
    schemas.paths.output_season_dir("comics", world_id, season)).
stub:
    If True, generate placeholder panels without loading real images.

## Top-level functions

- **`main()`** — 
