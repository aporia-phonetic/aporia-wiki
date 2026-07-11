# strategic_intel

*Source: `find/find/agents/strategic_intel.py`*

StrategicIntelAgent — weekly strategic synthesis across all AOL state.

Runs Sundays at 18:00 LA. Pulls together signals from every other domain:
    - Pipeline (funnel state, wins, losses, stuck deals)
    - Customers (patron counts, MRR, churn)
    - Finance (runway, recent burn, big transactions)
    - Compliance (upcoming deadlines, regulation changes)
    - Identity (renewals, due verifications)
    - Documents (expirations)

Feeds those signals to Claude with a strategic-advisor prompt asking for:
    1. Top 3 risks to address this week
    2. Top 3 opportunities to lean into
    3. One overdue decision the founder keeps deferring

Output lands as a single P3 "Weekly Strategic Brief" decision. The founder
reads it Monday morning. Approve to acknowledge; reject to discard.

Distinct from operational agents: this one reads everything but writes only
the brief decision. It doesn't drive deadlines, doesn't poll external
services. Pure synthesis.

## Defined here

### `StrategicIntelAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
