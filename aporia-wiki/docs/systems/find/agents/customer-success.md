# customer_success

*Source: `find/find/agents/customer_success.py`*

CustomerSuccessAgent — polls Patreon, maintains the customer roster, and
surfaces lifecycle decisions.

Runs every 15 minutes against Patreon's API (mock or real). For each pass:

1. Fetch current patron list.
2. Diff against last known state (stored per-patron in `checkpoints`):
     - New patron in list  → upsert customers row, log interaction,
                              submit P3 "Welcome new patron" decision.
     - Patron pledge_cents changed → log interaction, P3 "X upgraded/
                              downgraded their tier".
     - Patron dropped from list (was active, now absent) → submit
                              P2 "X churned" decision so founder can
                              consider a save-attempt.
3. Fetch recent pledges, log each as an interaction.
4. Update checkpoint per patron with current pledge_cents.

Idempotency: decisions deduped by context_json tag (kind:patron_id).
The 15-min cadence keeps polling fresh while staying well under Patreon's
rate limits.

Refund-queue + anniversary work (the daily 11am cadence implied by the
original CustomerSuccessQueue job) is deferred — needs a real Patreon
account to be useful. Both job names route to this same agent, so the
daily run is harmless duplication for now.

## Defined here

### `CustomerSuccessAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
