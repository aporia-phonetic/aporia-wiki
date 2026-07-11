# contract

*Source: `find/find/agents/contract.py`*

Contract Agent (AOL-4)
Schedule: daily 9am (review queue + expiration scan)

Responsibilities:
- Maintain contract template library (Operating Agreement, NDA, Licensee, Vendor)
- Draft contracts for new counterparties using Claude (fills template from context)
- Send via DocuSign (mock or real) and track envelope status
- Scan for upcoming contract expirations (≤30 days) → P2 decision
- Scan for overdue obligations → P1 decision if legal deadline
- Update signed contracts in ledger when DocuSign webhook fires

## Defined here

### `ContractAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
