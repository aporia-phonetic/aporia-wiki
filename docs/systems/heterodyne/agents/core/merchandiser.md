# merchandiser

*Source: `heterodyne/agents/merchandiser.py`*

agents/merchandiser.py — The Merchandiser (Agent 22)

POD merchandise listing generator.

Reads existing merch images from the image pipeline output
(audio/output/images/merch/ or exports/images/), upscales them
to 300 DPI via Replicate Real-ESRGAN (required for print), and
produces Printful + Gumroad product listing payloads.

IMPORTANT: Redbubble has no public API and is permanently excluded.

Outputs:
  exports/merch/{character_slug}/
    upscaled_{merch_type}.png     300-DPI upscaled image
    printful_payload.json         Ready to POST to Printful Products API
    gumroad_payload.json          Ready to POST to Gumroad Products API

Platform accounts required:
  PRINTFUL_API_KEY     env var — from store.printful.com
  GUMROAD_ACCESS_TOKEN env var — from app.gumroad.com/settings/advanced

Upscaling:
  REPLICATE_API_TOKEN  env var — Real-ESRGAN x4plus via Replicate
  If not present, upscaling is skipped and original image is used.

## Defined here

### `MerchItem`

| Field | Type |
|---|---|
| `character_id` | `str` |
| `character_name` | `str` |
| `merch_type` | `str` |
| `source_image` | `Path` |
| `upscaled_image` | `Optional[Path]` |
| `printful_payload` | `Optional[dict]` |
| `gumroad_payload` | `Optional[dict]` |
| `warnings` | `list[str]` |

### `MerchandiserReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `items_processed` | `int` |
| `items_uploaded_printful` | `int` |
| `items_uploaded_gumroad` | `int` |
| `output_paths` | `dict[str, str]` |
| `warnings` | `list[str]` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `Merchandiser`

POD merchandise listing generator.

Parameters
----------
image_dir:
    Directory containing merch source images. Defaults to audio/output/images/merch/.
output_dir:
    Base output directory for upscaled images and payloads. Defaults to exports/.
stub:
    If True, skip all API calls. Generates payloads but does not upload.
upload_printful:
    If True, POST product listings to Printful.
upload_gumroad:
    If True, POST digital product listings to Gumroad.

## Top-level functions

- **`main()`** — 
