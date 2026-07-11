# social_poster

*Source: `heterodyne/agents/social_poster.py`*

agents/social_poster.py

Social media queue manager and posting agent for the Axiom Synthetic Pipeline.

Flow
----
  AppState.zingers (approved catchphrases)
      ↓  SocialPoster.queue_zinger()
  data/social_queue.json  ← staging area; persisted across runs
      ↓  SocialPoster.flush_pending()
  Reddit (via praw)  /  Bluesky (via atproto)

Credentials are read from environment variables only — never stored in
AppState or on disk.

Required environment variables
-------------------------------
Reddit (set all four to enable):
    REDDIT_CLIENT_ID
    REDDIT_CLIENT_SECRET
    REDDIT_USERNAME
    REDDIT_PASSWORD

Bluesky (set both to enable):
    BLUESKY_HANDLE       e.g. yourhandle.bsky.social
    BLUESKY_APP_PASSWORD

Platform selection
------------------
Pass `platforms=["reddit", "bluesky"]` to queue_zinger/queue_text.
If a platform's credentials are absent at flush time, that platform is
skipped and the entry is marked "skipped" for that platform (not failed).

Dependencies
------------
    pip install praw        (Reddit)
    pip install atproto     (Bluesky)

Both are optional — the poster works with neither, one, or both installed.

## Defined here

### `SocialQueueEntry`

One social post waiting to be submitted (or already submitted).

| Field | Type |
|---|---|
| `entry_id` | `str` |
| `platforms` | `list[str]` |
| `text` | `str` |
| `character` | `str` |
| `voice_seed_id` | `str` |
| `episode` | `int` |
| `season` | `int` |
| `segment` | `int` |
| `context` | `str` |
| `queued_at` | `str` |
| `status` | `str` |
| `posted_at` | `str | None` |
| `reddit_url` | `str | None` |
| `bluesky_uri` | `str | None` |
| `buffer_update_id` | `str | None` |
| `youtube_community_post_id` | `str | None` |
| `instagram_media_id` | `str | None` |
| `tiktok_publish_id` | `str | None` |
| `image_path` | `str | None` |
| `caption` | `str | None` |
| `error` | `str | None` |

### `FlushReport`

Summary of a flush_pending() call.

| Field | Type |
|---|---|
| `attempted` | `int` |
| `posted` | `int` |
| `skipped` | `int` |
| `failed` | `int` |
| `entries` | `list[SocialQueueEntry]` |

### `SocialPoster`

Queue social posts from zingers and flush them to Reddit / Bluesky.

Parameters
----------
queue_path:
    Path to the JSON queue file. Created on first queue_* call.
    Recommended: data/social_queue.json (or world-scoped variant).
reddit_subreddit:
    Target subreddit (without r/ prefix). e.g. "AeonPulp".
    Required to post to Reddit; ignored if REDDIT_* env vars absent.
reddit_post_template:
    f-string template for the Reddit post title.
    Available vars: {character}, {episode}, {season}, {short_text}.
    Default: "[{character}] S{season}E{episode:02d}"
bluesky_post_template:
    f-string template for the Bluesky post text.
    Available vars: {character}, {episode}, {season}, {text}.
    Must produce ≤300 chars including the quote.
    Default: '"{text}" — {character} (Ep. {episode})'

### `Socialite`

Extended social media queue generator (Agent 19: The Socialite).

Wraps SocialPoster and adds:
- LLM caption generation from episode JSON
- Image crops for Instagram (1:1) and TikTok (9:16) via PIL
- Buffer scheduling integration
- YouTube Community tab support

Platform API setup required:
- Buffer: BUFFER_ACCESS_TOKEN env var (https://buffer.com/developers/api)
- YouTube Community: YOUTUBE_ANALYTICS_CREDENTIALS_PATH (YouTube Data API)
- Instagram Graph API: INSTAGRAM_ACCESS_TOKEN + INSTAGRAM_USER_ID
  (requires Meta Business Account + API app approval — apply separately)
- TikTok Content Posting API: TIKTOK_ACCESS_TOKEN
  (requires TikTok developer app approval — apply separately)

Note: Instagram and TikTok API access requires application approval that
takes time. Apply for both at the same time as development:
  - TikTok: https://developers.tiktok.com/products/content-posting-api/
  - Instagram: https://developers.facebook.com/docs/instagram-api/
