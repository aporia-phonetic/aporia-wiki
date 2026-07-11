# pitch_artist

*Source: `heterodyne/agents/pitch_artist.py`*

agents/pitch_artist.py — The Pitch Artist (Agent 23)

Kickstarter campaign asset generator. Seasonal batch tool, not a pipeline stage.

Kickstarter has no API for campaign creation. This agent generates all assets
for manual upload. TJ submits the campaign; the agent supplies everything needed.

Outputs:
  exports/pitch/{world_id}/S{N}/
    kickstarter_copy.md          Full campaign copy (description, FAQ, risk statement)
    creator_bio.md               Creator bio block
    reward_tiers.md              Reward tier descriptions
    shot_list.md                 Video storyboard — shot list + narration draft
    hero_image.png               Hero image (1552×868) via image_agent
    character_spotlights/        Character spotlight images (1000×1000)
    reward_mockups/              Reward tier mockup image prompts (manual execution)
    campaign_bundle.zip          Everything zipped for submission

Usage:
  python -m agents.pitch_artist --world verdant_deep --season 1
  python -m agents.pitch_artist --world verdant_deep --season 1 --stub

Dependencies:
  fpdf2     pip install fpdf2

## Defined here

### `PitchArtistReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `season` | `int` |
| `output_paths` | `dict[str, str]` |
| `characters_spotlit` | `list[str]` |
| `warnings` | `list[str]` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `PitchArtist`

Kickstarter campaign asset generator. Seasonal batch tool.

Parameters
----------
data_dir:
    Path to data/worlds/ root.
output_dir:
    Base output directory. Pitch assets go to {output_dir}/pitch/.
image_backend:
    Image backend for hero/spotlight images (stub/openai/replicate/local_sd).
llm_router:
    LLMRouter instance. None → build default.
stub:
    If True, skip LLM and image calls.

## Top-level functions

- **`main()`** — 
