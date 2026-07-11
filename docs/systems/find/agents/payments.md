# payments

*Source: `find/find/agents/payments.py`*

Payments Agent (AOL-3)
Schedules: hourly (approved queue), daily 4pm (bill batch)

Responsibilities:
- Process the approved payment queue — execute ACH transfers for approved PaymentOut rows
- Batch vendor bill payments (consolidated daily run at 4pm)
- Enforce authorization tiers via Authorizer before any transfer
- High-value payments require Mercury high-value key (loaded only after HMAC signature)
- Verify daily aggregate cap before each execution

## Defined here

### `PaymentsAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
