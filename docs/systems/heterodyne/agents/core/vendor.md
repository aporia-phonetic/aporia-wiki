# vendor

*Source: `heterodyne/agents/vendor.py`*

agents/vendor.py — The Vendor (Agent 28)

Event-driven asset listing agent. Watches for new exportable assets and
triggers platform API calls to list them for sale.

Integrations:
  Printful    — POD products (via Merchandiser payloads)
  Gumroad     — Digital products (EPUB, art downloads, cosplay packs)
  Etsy        — Listings (after API approval; stubs until then)

Permanently excluded:
  Redbubble   — No public API. Will never be automated.

Trigger modes:
  1. watchdog (continuous): File system watcher on exports/ directory.
     Triggers on new files matching registered asset patterns.
  2. scan (one-shot): Scan exports/ for unlisted assets and list them.
     Run this in a cron job or after a pipeline run.

Asset registry:
  data/vendor_registry.json — tracks which assets have already been listed,
  preventing duplicate submissions.

Environment variables required:
  GUMROAD_ACCESS_TOKEN
  PRINTFUL_API_KEY
  ETSY_API_KEY + ETSY_SHOP_ID  (optional; Etsy listing stubs until approved)

Dependencies:
  watchdog    pip install watchdog   (required for watch mode)
  requests    pip install requests

## Defined here

### `ListingRecord`

| Field | Type |
|---|---|
| `asset_path` | `str` |
| `platform` | `str` |
| `listing_type` | `str` |
| `listed_at` | `str` |
| `platform_id` | `str` |
| `platform_url` | `str` |
| `error` | `str` |
| `status` | `str` |

### `Vendor`

Asset listing agent. Lists new AEON engine outputs to sales platforms.

Parameters
----------
exports_dir:
    Root exports/ directory to watch or scan.
registry_path:
    Path to the vendor registry JSON. Tracks already-listed assets.
stub:
    If True, log what would be listed but make no API calls.

## Top-level functions

- **`main()`** — 
