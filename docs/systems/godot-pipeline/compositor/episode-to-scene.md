# episode_to_scene

*Source: `godot-pipeline/compositor/episode_to_scene.py`*

compositor/episode_to_scene.py — AEON episode JSON → Godot scene data (B2)

Converts a rendered episode JSON (from HETERODYNE) into:
  out/{S}E{E:02d}_{clip_type}/
    clip.json          Godot-readable clip spec (loaded by render.gd)
    rms_{char}.json    Per-character amplitude envelopes for talking animation
    manifest.json      Lists all clips for this episode

Usage:
    python -m compositor.episode_to_scene <episode_json> [--world-id verdant_deep]

or imported:
    from compositor.episode_to_scene import build_episode_clips
    clips = build_episode_clips(episode_path, audio_root, images_root)

## Defined here

### `CharacterSlot`

| Field | Type |
|---|---|
| `slot_id` | `str` |
| `voice_seed_id` | `str` |
| `speaker_name` | `str` |
| `sprite_sheet` | `str` |
| `talking_wav` | `Optional[str]` |
| `pose` | `str` |

### `ClipBlock`

| Field | Type |
|---|---|
| `block_index` | `int` |
| `start_s` | `float` |
| `duration_s` | `float` |
| `location` | `str` |
| `scene_template` | `str` |
| `characters` | `list[CharacterSlot]` |
| `dialogue_line` | `str` |
| `speaker_name` | `str` |
| `scene_energy` | `str` |

### `ClipSpec`

| Field | Type |
|---|---|
| `clip_type` | `ClipType` |
| `aspect` | `Aspect` |
| `season` | `int` |
| `episode` | `int` |
| `world_id` | `str` |
| `title` | `str` |
| `blocks` | `list[ClipBlock]` |
| `audio_path` | `str` |
| `duration_cap_s` | `float` |

### `EpisodeManifest`

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `world_id` | `str` |
| `clips` | `list[dict]` |

## Top-level functions

- **`build_episode_clips()`** — Convert one episode JSON into Godot clip specs under out_root.
