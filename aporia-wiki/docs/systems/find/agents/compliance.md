# compliance

*Source: `find/find/agents/compliance.py`*

ComplianceAgent — keeps the AOL's compliance posture current.

Four responsibilities:

1. **Recurring deadlines.** Daily 7am, idempotently upsert known annual /
   quarterly deadlines (Delaware franchise tax, IRS quarterly estimates).
   These have fixed calendar dates so the agent can roll them forward
   without external input.

2. **Deadline alerting.** Same daily run, scan all `deadlines` rows.
   - <= 30 days → P2 "Upcoming: <kind>"
   - past due, status still upcoming/due → flip to overdue + P1

3. **USPTO trademark monitoring.** Weekly Wednesday 8am. For each row in
   `trademarks` with a serial_number, hit TSDR and update status. Status
   change → P2 decision. New rejection/abandonment → P1.

4. **Regulations watch.** Weekly Wednesday 8am. For each row in
   `regulations_watch`, fetch + hash the URL. Hash change vs. stored
   content_hash → P3 FYI (page mutated; user should glance).

Also seeds the standard set of trademarks-to-watch + regulations-to-watch
on first run (idempotent — checks if any rows exist before inserting).

## Defined here

### `ComplianceAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
