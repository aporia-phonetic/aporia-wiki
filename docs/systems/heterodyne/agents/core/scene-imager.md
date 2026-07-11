# scene_imager

*Source: `heterodyne/agents/scene_imager.py`*

Variant rendering + selection for batch scene/cover/plate/hero images.

The user churns several candidates per image and keeps the best. This module
renders N seed-variants of each target into a `_candidates/` folder, auto-promotes
v0 to the canonical filename (so the video pipeline has something immediately),
and records a manifest. `--select-images` later re-promotes a chosen variant.

Pure orchestration over ImageAgent.generate(); the targets (ImageRequest +
final path) are built by the main.py runners that know the world/episode data.

## Defined here

### `ImageTarget`

One image to produce: the request, where the keeper lands, and a label.

| Field | Type |
|---|---|
| `req` | `ImageRequest` |
| `final_path` | `Path` |
| `label` | `str` |

## Top-level functions

- **`make_candidates()`** — Render n seed-variants of a target into its `_candidates/` dir. Variant i
- **`promote()`** — 
- **`generate_targets()`** — Render variants for every target, auto-promote v0, and write a manifest.
- **`apply_selection()`** — Re-promote each target's `chosen` candidate per the manifest. Edit the
