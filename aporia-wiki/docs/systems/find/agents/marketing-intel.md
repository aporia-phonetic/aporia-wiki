# marketing_intel

*Source: `find/find/agents/marketing_intel.py`*

MarketingIntelAgent — drafts daily social content + tracks performance.

Three cron job paths (all routed to this same agent via find/scheduler/jobs.py):
    - MarketingNoon     · daily 12:00 LA · drafts a noon-window post
    - MarketingEvening  · daily 17:00 LA · drafts an evening-window post
    - MarketingScrape   · daily 18:00 LA · placeholder for performance scraping

The agent doesn't know which job triggered it (only that it ran). It uses
local time and minutes-since-midnight as a tiebreaker:
    - hour ~12  → noon draft
    - hour ~17  → evening draft
    - hour ~18  → scrape

Channel rotation per day-of-week (so each channel hits ~weekly):
    Mon TikTok        | Tue Instagram     | Wed Reddit       | Thu X
    Fri TikTok        | Sat Instagram     | Sun Reddit

Each draft is a P3 decision with the post text inline. Founder approves,
edits, posts manually. When social accounts go live, we add real-post
bindings without changing the drafting logic.

Performance scrape is intentionally a no-op stub right now — all social
accounts in the inventory are "to create". Replace with real fetch logic
once at least one account exists.

## Defined here

### `MarketingIntelAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
