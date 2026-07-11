# analyst

*Source: `heterodyne/agents/analyst.py`*

agents/analyst.py — The Analyst (Agent 30)

Aggregates revenue and performance data from all connected platforms into
a single P&L report and local HTML dashboard. Zero API generation cost —
pure data aggregation and reporting.

Platforms supported:
  Patreon        (PATREON_ACCESS_TOKEN + PATREON_CAMPAIGN_ID)
  Stripe         (STRIPE_SECRET_KEY)
  Gumroad        (GUMROAD_ACCESS_TOKEN)
  YouTube        (YOUTUBE_ANALYTICS_CREDENTIALS_PATH — OAuth JSON)

Output:
  exports/analytics/analyst_YYYYMM.md      Markdown P&L summary
  exports/analytics/dashboard.html         Local HTML dashboard (refreshed on each run)

Unconfigured platforms are skipped with a warning — the Analyst runs with
whatever credentials are present and reports coverage gaps.

## Defined here

### `RevenueRecord`

| Field | Type |
|---|---|
| `platform` | `str` |
| `amount_usd` | `float` |
| `gross_usd` | `float` |
| `transaction_count` | `int` |
| `period_start` | `date` |
| `period_end` | `date` |
| `notes` | `str` |

### `PerformanceRecord`

| Field | Type |
|---|---|
| `platform` | `str` |
| `metric` | `str` |
| `value` | `float` |
| `period_start` | `date` |
| `period_end` | `date` |

### `AnalystBundle`

| Field | Type |
|---|---|
| `period_start` | `date` |
| `period_end` | `date` |
| `revenue` | `list[RevenueRecord]` |
| `performance` | `list[PerformanceRecord]` |
| `missing_platforms` | `list[str]` |
| `errors` | `list[str]` |

### `PatreonConnector`

Fetch patron count and pledge revenue from Patreon API v2.

### `StripeConnector`

Fetch net revenue from Stripe balance transactions.

### `GumroadConnector`

Fetch sales data from Gumroad API.

### `YouTubeAnalyticsConnector`

Fetch view counts and estimated revenue from YouTube Analytics API.

Requires OAuth 2.0 credentials. Pass credentials_path to a token JSON
file (same format as used by YouTubeUploader in distributor.py).

### `Analyst`

Aggregates revenue + performance data and produces reports.

Credentials are read from environment variables:
  PATREON_ACCESS_TOKEN, PATREON_CAMPAIGN_ID
  STRIPE_SECRET_KEY
  GUMROAD_ACCESS_TOKEN
  YOUTUBE_ANALYTICS_CREDENTIALS_PATH

Parameters
----------
output_dir:
    Where to write report files. Defaults to exports/analytics/.

## Top-level functions

- **`main()`** — 
