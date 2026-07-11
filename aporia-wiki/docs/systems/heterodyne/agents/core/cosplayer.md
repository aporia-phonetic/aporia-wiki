# cosplayer

*Source: `heterodyne/agents/cosplayer.py`*

agents/cosplayer.py — The Cosplayer (Agent 25)

Generates costume reference packs for characters — NOT sewing patterns.

Phase 1 scope (current):
  - Multiple-angle character reference art (via image_agent.py)
  - Material list with cost estimates (LLM)
  - Color palette extracted from portrait (PIL)
  - Makeup & styling guide (LLM)
  - Construction notes — how to achieve the look, not cut-and-sew patterns
  - PDF output for Gumroad sale
  - ZIP bundle: PDF + reference images

Phase 2 (deferred — quality risk):
  - Scaled sewing patterns (XS–3XL) require geometrically precise garment data.
    LLMs do not reliably generate correct garment geometry. Revisit when a
    human-verified pattern template system or dedicated library is available.

Dependencies:
  Pillow    pip install Pillow
  fpdf2     pip install fpdf2

## Defined here

### `CosplayerReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `character_id` | `str` |
| `reference_images` | `list[str]` |
| `palette_colors` | `list[str]` |
| `output_paths` | `dict[str, str]` |
| `warnings` | `list[str]` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `Cosplayer`

Costume reference pack generator.

Parameters
----------
data_dir:
    Path to data/worlds/ root.
image_output_dir:
    Where image_agent writes output. Defaults to audio/output/images/.
output_dir:
    Base output directory. Packs go to {output_dir}/cosplay/.
image_backend:
    Backend for reference image generation (stub/openai/replicate/local_sd).
llm_router:
    LLMRouter instance. None → build default.
stub:
    If True, skip LLM and image calls.

## Top-level functions

- **`main()`** — 
