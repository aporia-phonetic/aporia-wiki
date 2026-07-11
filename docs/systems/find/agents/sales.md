# sales

*Source: `find/find/agents/sales.py`*

SalesAgent — manages the B2B/licensing prospect pipeline.

APG's revenue is mostly B2C (Patreon, app, merch, TTRPG product sales), but
the business plan calls out a B2B partnership track:
    - Language-learning licensees (Duolingo, Babbel, Rosetta Stone — Horizon 2-3)
    - VTT marketplace partners (Roll20, Foundry — already in inventory)
    - Audio publishers (Audible, Libro.fm — competitor-watch upgrades to partner)
    - Tabletop community partnerships

The SalesAgent doesn't *discover* prospects (web research is deferred). It
operates on the prospects table that the founder seeds (manually or via the
Pipeline tab) and:

    Daily 10am (SalesAgent):
      For each prospect with next_action_at <= today (and stage not won/lost):
        - Draft an outreach message via Claude, framed for the prospect's
          stage (lead → cold intro, qualified → discovery call invite,
          proposal → close-attempt nudge).
        - Submit as a P2 decision asking the founder to approve sending.

    Weekly Mon 9am (SalesDigest):
      Funnel summary: stage counts + value + weighted forecast + this
      week's wins/losses + prospects stuck > 14 days.
      Submitted as a single P3 "Sales weekly digest" decision.

Idempotency: outreach decisions deduped by context tag (outreach:prospect_id).
Per-prospect outreach is bumped to a new decision when next_action_at moves
past the existing decision's creation time.

## Defined here

### `SalesAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
