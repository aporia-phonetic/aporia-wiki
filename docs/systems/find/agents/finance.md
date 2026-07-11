# finance

*Source: `find/find/agents/finance.py`*

Finance Agent (AOL-1)
Schedules: daily 6am (sync + categorize), weekly Mon 7am (P&L), monthly 1st (close)

Responsibilities:
- Sync account balances from Mercury (mock or real)
- Categorize uncategorized transactions using Claude
- Compute monthly P&L and runway snapshot
- Queue P2 decision if burn rate increases >20% month-over-month
- Queue P1 decision if runway drops below 3 months

## Defined here

### `FinanceAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
