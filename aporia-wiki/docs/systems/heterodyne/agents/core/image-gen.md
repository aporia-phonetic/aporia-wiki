# image_gen

*Source: `heterodyne/agents/image_gen.py`*

Image Generator — produces scene illustrations via local Stable Diffusion.

Generates images for each segment, storing them in the episode directory.
Uses diffusers library for local inference (no API calls).

## Defined here

### `ImageGenError`

Base class for image generation failures.

### `StableDiffusionGenerator`

Generates scene illustrations using local Stable Diffusion.
