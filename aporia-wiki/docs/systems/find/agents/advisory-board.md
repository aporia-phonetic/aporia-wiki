# advisory_board

*Source: `find/find/agents/advisory_board.py`*

AdvisoryBoardAgent — on-demand multi-lens pressure-tester.

Not scheduled. Called via POST /api/advisory-board with a business question
(or an existing Decision Queue item to pressure-test). Runs six sequential
Claude passes — CEO, CFO, CTO, Operator, Critic, Chair — each with a
role-specific mandate, then submits the Chair synthesis as a Decision item.

Results are stored in advisory_board_sessions; execute() is a no-op stub.

## Defined here

### `AdvisoryBoardAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
