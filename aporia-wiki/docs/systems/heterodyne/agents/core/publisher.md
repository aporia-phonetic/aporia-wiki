# publisher

*Source: `heterodyne/agents/publisher.py`*

agents/publisher.py — The Publisher (Agent 29)

Automated episode and chapter publishing agent.

What CAN be automated (APIs exist):
  Transistor.fm   — Full REST API: create episode, upload audio, set publish time.
  Gumroad         — EPUB upload and digital product publish via API.

What CANNOT be automated (no public publishing APIs):
  Royal Road      — No API.
  Wattpad         — Partner-restricted.
  Scribd          — No upload API.
  KDP             — No publishing API.
  Smashwords      — Manual EPUB submission.

For non-automatable platforms, Publisher generates files and queues a reminder
notification so TJ knows which uploads are pending. Reminder log is written to
exports/publishing/pending_uploads.md.

Environment variables:
  TRANSISTOR_API_KEY          — From app.transistor.fm/account
  TRANSISTOR_SHOW_ID          — Transistor show UUID
  GUMROAD_ACCESS_TOKEN        — From app.gumroad.com/settings/advanced

Dependencies:
  requests    (already a dep)

## Defined here

### `PendingUpload`

| Field | Type |
|---|---|
| `platform` | `str` |
| `asset_type` | `str` |
| `asset_path` | `str` |
| `world_id` | `str` |
| `season` | `int` |
| `episode` | `int` |
| `title` | `str` |
| `instructions` | `str` |

### `PublisherReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `season` | `int` |
| `episode` | `int` |
| `transistor_episode_id` | `str` |
| `transistor_episode_url` | `str` |
| `gumroad_product_ids` | `list[str]` |
| `pending_uploads` | `list[dict]` |
| `warnings` | `list[str]` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `Publisher`

Automated publishing agent for AEON episode releases.

Parameters
----------
exports_dir:
    Root exports/ directory for artifacts not part of the output/
    reorg (currently just the pending-uploads reminder log).
audio_dir, prose_dir:
    Legacy fallback roots, used only if the fresh per-call lookup
    (schemas.paths.output_season_dir, computed from world_id/season in
    publish_episode) doesn't find anything — publish_episode is always
    called with a specific (world_id, season, episode), so the real
    audio/EPUB directories are recomputed per call rather than fixed
    at construction time.
data_dir:
    Path to data/worlds/ root.
stub:
    If True, skip all API calls.

## Top-level functions

- **`main()`** — 
