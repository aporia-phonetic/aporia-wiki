# distributor

*Source: `heterodyne/agents/distributor.py`*

agents/distributor.py

Multilingual RSS feed generator for the Axiom Synthetic Pipeline.

Takes finished episode MP3 files (one per language variant) and generates
standard podcast RSS 2.0 XML feeds — one feed file per language.

Architecture:
  output/audio/{world_id}/season_XX/S1E01.mp3       → English master
  output/audio/{world_id}/season_XX/S1E01_es.mp3    → Spanish variant
  output/audio/{world_id}/season_XX/S1E01_fr.mp3    → French variant
                  ↓
  distributor.generate_feeds(...)
                  ↓
  output/rss/{world_id}/feed_en.xml
  output/rss/{world_id}/feed_es.xml
  output/rss/{world_id}/feed_fr.xml

The RSS files are standard podcast RSS 2.0 with iTunes extension tags.
Feed them to your podcast host, Anchor, Buzzsprout, or a static hosting CDN.

No upload logic is included — the generator writes local XML files.
Deployment to a host is outside the pipeline; just drop the XML files on
your podcast host per their instructions.

Classes
-------
LanguageFeedConfig  — configuration for one language's feed
DistributorReport   — summary of a generate_feeds() run
LanguageDistributor — main class; call generate_feeds()

## Defined here

### `LanguageFeedConfig`

Configuration for one language's podcast RSS feed.

### `DistributorReport`

Summary of a generate_feeds() call.

### `LanguageDistributor`

Generates per-language podcast RSS XML feeds from episode outputs.

Parameters
----------
episodes_dir:
    Where episode JSON files live (used to extract title/description).
    e.g. data/seasons/season_01/episodes/
audio_output_dir:
    Where finished MP3 files live.
    e.g. schemas.paths.output_season_dir("audio", world_id, season)
output_dir:
    Where RSS XML files are written (whole-show, no season).
    e.g. schemas.paths.output_type_dir("rss", world_id)
season:
    Season number.

### `YouTubeUploadReport`

Summary of a YouTube upload attempt.

### `YouTubeUploader`

Upload finished episode MP4 files to a YouTube channel.

Uses the YouTube Data API v3 via the official Google API Python client.

Authentication:
    Requires OAuth 2.0 credentials stored in a client_secrets.json file
    (downloaded from Google Cloud Console → Credentials → OAuth 2.0 Client).
    On first run, a browser window opens for authorization. The resulting
    token is cached at token_cache_path for subsequent runs.

    Alternatively, pass credentials_json_path pointing to service account
    credentials for server-side (headless) auth.

Requirements:
    pip install google-api-python-client google-auth-oauthlib

Parameters
----------
client_secrets_path:
    Path to OAuth 2.0 client_secrets.json. Default: data/yt_client_secrets.json
token_cache_path:
    Where to store the OAuth token after first authorization.
    Default: data/yt_token.json
channel_id:
    YouTube channel ID (optional). Used for display only — upload always goes
    to the authenticated account's default channel.
default_privacy:
    Default video privacy setting: "public", "unlisted", or "private".
    Default: "unlisted" (safe for review before going public).
default_category_id:
    YouTube category ID. 22 = People & Blogs, 24 = Entertainment (default).
