# image_workflows

*Source: `heterodyne/agents/image_workflows.py`*

agents/image_workflows.py

Workflow agents on top of ImageAgent (agents/image_agent.py).

ImageAgent handles backend selection and the generate() call. These
workflows know what FIELDS to fill in for each artifact type — character
portraits, episode covers, scene cards — so callers can ask for
"portraits for everyone in episode 3" or "cover art for S2E07" without
constructing ImageRequest by hand.

All three workflows go through ImageAgent's existing backend logic, so
the STUB backend (default on the current rig) writes placeholder PNGs;
the LOCAL_SD backend will paint real art once the new GPU is online.
No hardware-day code changes needed in these workflows — the swap is
the IMAGE_BACKEND env var or ImageAgent constructor arg.

Usage:
    from agents.image_agent import ImageAgent
    from agents.image_workflows import PortraitAgent, CoverArtAgent, SceneCardAgent

    img = ImageAgent(output_dir="output/images/verdant_deep")   # respects IMAGE_BACKEND env

    portrait = PortraitAgent(img)
    result = portrait.generate_for_character(
        name="Maren Voss",
        description="Tall, broad-shouldered, close-cropped gray hair...",
        world_aesthetic="1930s pulp adventure, jungle ruins, sepia warmth",
    )

    cover = CoverArtAgent(img)
    result = cover.generate_for_episode(
        season=1, episode=3, title="Rootwork and Ruin",
        synopsis="The crew discovers a sealed vault beneath a root-choked atrium.",
        world_aesthetic="1930s pulp magazine cover, Art Deco, golden hour jungle",
    )

    scene = SceneCardAgent(img)
    result = scene.generate_for_scene(
        location="Bluff Aerodock",
        atmosphere="Storm gathering, airships straining at moorings",
        season=1, episode=3, scene_index=2,
    )

## Defined here

### `CharacterPortraitSpec`

Minimal info needed to render a character portrait.

Populate from world_ledger or pass in directly. The workflow agent
forwards these into the ImageRequest.

| Field | Type |
|---|---|
| `name` | `str` |
| `description` | `str` |
| `voice_description` | `str` |
| `archetype` | `str` |

### `PortraitAgent`

Generates character portraits via ImageAgent.

Knows the prompt fields portraits need (name, physical description,
voice cue for energy/posture). Batches across a roster when given a
list.

### `CoverArtAgent`

Generates episode/season cover art via ImageAgent.

Tall 1024×1792 format by default (podcast-cover friendly). Override
via the `size` parameter if a campaign needs square or wide.

### `SceneCardAgent`

Generates landscape scene snapshots (1792×1024) for Ken Burns video
composition and episode promo cards.

Reads a location + atmosphere description and produces one card. The
Video Compositor (B1) consumes these for the visual layer of MP4s.

### `CosmeticsAgent`

Alternate outfit and seasonal variant generator (Agent 21: The Cosmetologist).

Phase 1 — FLUX Redux on Replicate (reference-image-guided, interim quality).
Phase 2 — ControlNet + IP-Adapter on local AUTOMATIC1111 (hardware day, best quality).

FLUX Redux takes a reference image and a style/outfit prompt and produces
a new image that preserves character identity while changing costume/season.
This is the best available identity-consistency approach without a local GPU.

When REPLICATE_API_TOKEN is not set, falls back to stub mode (placeholder files).

Usage:
    from agents.image_agent import ImageAgent
    from agents.image_workflows import CosmeticsAgent
    from schemas import paths

    img = ImageAgent(output_dir=paths.output_type_dir("images", "verdant_deep"), backend="replicate")
    cosm = CosmeticsAgent(img, output_dir=paths.output_type_dir("images", "verdant_deep") / "cosmetics")
    results = cosm.generate_variants(
        world_id="verdant_deep",
        character_id="ticker",
        character_name="TICKER",
        reference_image_path=paths.output_type_dir("images", "verdant_deep") / "portraits" / "ticker.png",
        world_aesthetic="1930s pulp adventure, sepia warmth",
    )

Phase 2 note (hardware day):
    Replace the Replicate call with an AUTOMATIC1111 img2img call using
    ControlNet OpenPose + IP-Adapter for per-pixel identity preservation.
    The public API in this class stays identical — only _generate_via_replicate()
    needs to be swapped for _generate_via_local_sd().

| Field | Type |
|---|---|
| `_VARIANTS` | `dict[str, dict]` |
