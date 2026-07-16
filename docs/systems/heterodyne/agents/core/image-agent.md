# image_agent

*Source: `heterodyne/agents/image_agent.py`*

agents/image_agent.py

Image generation agent for the Axiom Synthetic Pipeline.

Produces visual assets alongside the audio drama pipeline:
  - Episode cover art (character silhouette + title + atmosphere)
  - Character portraits (from CharacterSheet.physical_description)
  - Scene snapshots (location + atmosphere for a specific block)
  - Merch designs (logo/wordmark + character art compositions)

Backend support (configured at runtime via ImageAgent.backend):
  STUB        — Returns a placeholder path; no API call. Default for dry runs.
  OPENAI      — OpenAI DALL·E 3 via official Python client.
  REPLICATE   — Replicate API (Stable Diffusion XL or FLUX models).
  LOCAL_SD    — Local Stable Diffusion via AUTOMATIC1111 REST API.
  DIFFUSERS   — Local diffusers run out-of-process via the dedicated
                .venv-imagegen interpreter (carries its own torch/diffusers,
                isolated from the main venv's voice stack). Needs no server.

All generated images are saved directly under output_dir/ with structured
filenames (caller passes an already type/world-scoped path, e.g.
schemas.paths.output_type_dir("images", world_id)). The path is written
back to CharacterSheet.visual_seed_id (portraits) or to the episode
manifest (cover art / scene snapshots).

Usage:
    from agents.image_agent import ImageAgent, ImageRequest, ImageType
    from schemas import paths

    agent = ImageAgent(output_dir=paths.output_type_dir("images", "caelum_reach"), backend="openai")

    # Character portrait
    req = ImageRequest(
        image_type=ImageType.PORTRAIT,
        character_name="Maren Voss",
        physical_description="Tall, broad-shouldered woman, close-cropped gray hair, ...",
        world_aesthetic="painterly studio portrait, coal-black and amber gaslight palette",
    )
    result = agent.generate(req)
    print(result.path)   # Path to saved PNG

    # Episode cover art
    req = ImageRequest(
        image_type=ImageType.COVER_ART,
        episode=3,
        season=1,
        title="Rootwork and Ruin",
        scene_description="Crew discovers a sealed vault beneath a root-choked atrium",
        world_aesthetic="moody illustrated magazine cover, coal-black and amber gaslight palette",
    )
    result = agent.generate(req)

## Defined here

### `ImageGenError`

Raised when an image backend cannot produce an image.

### `ImageType`

### `ImageBackend`

### `ImageRequest`

Specification for a single image generation request.

| Field | Type |
|---|---|
| `image_type` | `ImageType` |
| `character_name` | `str` |
| `physical_description` | `str` |
| `voice_description` | `str` |
| `archetype` | `str` |
| `public_role` | `str` |
| `subject_note` | `str` |
| `action_setting` | `str` |
| `episode` | `int` |
| `season` | `int` |
| `title` | `str` |
| `scene_description` | `str` |
| `present_characters` | `list[str]` |
| `world_aesthetic` | `str` |
| `size` | `str` |
| `extra_prompt` | `str` |
| `seed` | `Optional[int]` |
| `out_path_override` | `str` |
| `identity_ref` | `str` |
| `identity_scale` | `Optional[float]` |
| `identity_kind` | `str` |
| `lora_path` | `str` |
| `lora_scale` | `Optional[float]` |
| `merch_type` | `str` |
| `include_character` | `str` |

### `ImageResult`

Output of a single image generation call.

| Field | Type |
|---|---|
| `path` | `Path` |
| `backend_used` | `str` |
| `prompt_used` | `str` |
| `size` | `str` |
| `is_stub` | `bool` |
| `error` | `str` |

### `ImageAgent`

Generates visual assets for the Axiom Synthetic Pipeline.

Parameters
----------
output_dir:
    Root output directory. Images are saved under {output_dir}/images/.
backend:
    Which image generation service to use.
    "stub": placeholder PNG (no API call, safe for dry runs).
    "openai": OpenAI DALL·E 3 (requires OPENAI_API_KEY env var or api_key param).
    "replicate": Replicate API (requires REPLICATE_API_TOKEN env var).
    "local_sd": AUTOMATIC1111 local SD REST API.
api_key:
    API key for the selected backend. If None, reads from environment.
openai_model:
    DALL·E model. Default: "dall-e-3".
replicate_model:
    Replicate model ref. Default: FLUX schnell for fast generation.
local_sd_url:
    Base URL for AUTOMATIC1111 API. Default: http://127.0.0.1:7860
diffusers_python:
    Path to the isolated .venv-imagegen Python interpreter used by the
    DIFFUSERS backend. Default: env DIFFUSERS_PYTHON, else the repo's
    .venv-imagegen/bin/python.
diffusers_model:
    HF model id (or local path) for the DIFFUSERS backend. Default: env
    DIFFUSERS_MODEL, else the public SD-1.5 mirror.
diffusers_gpu:
    CUDA device index the DIFFUSERS worker is pinned to (via
    CUDA_VISIBLE_DEVICES). Default: env DIFFUSERS_GPU, else "1" to keep
    off the voice/TTS GPU 0.

| Field | Type |
|---|---|
| `_ACTION_SETTINGS` | `tuple[tuple[str, str], ...]` |

## Top-level functions

- **`compose_house_style()`** — Assemble a style banner from adjustable per-world dimensions.
