# billing

*Source: `find/find/agents/billing.py`*

Billing Agent (AOL-2)
Schedules: daily 8am (issue + remind), monthly 1st (recurring invoices)

Responsibilities:
- Issue invoices for new billable events (licensee agreements, B2B services)
- Send payment reminders for open invoices past due
- Process Stripe webhook events for payment confirmations
- Queue P2 decision for overdue invoices >7 days (if amount ≥ $100)
- Generate recurring invoices for active subscription customers (monthly 1st)

## Defined here

### `BillingAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
