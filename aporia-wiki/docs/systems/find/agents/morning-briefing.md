# morning_briefing

*Source: `find/find/agents/morning_briefing.py`*

MorningBriefingAgent — the single push that orients the founder each morning.

Runs daily 6am LA. Pulls together signals from across the AOL into one
concise email (sent via SendGrid) + a short SMS companion (via Twilio if
configured). The intent is to replace "open laptop, check 8 tabs" with
"check phone, decide what matters today."

Contents:
    - **Yesterday's pulse**: agent runs completed, decisions submitted by
      tier, runway/MRR delta if any.
    - **Today's priorities**: open P1/P2 items, today's deadlines/events
      from the Calendar aggregator, prospects due for outreach.
    - **One thing**: an LLM-distilled "the most important thing today" —
      asks Claude to pick a single focus item from everything above.

The morning briefing is NOT a Decision Queue item — it's an outbound
push. Founder receives it on phone over coffee; the AOL doesn't expect
a response. Distinct from StrategicIntelAgent's Sunday brief (which IS
a decision and surveys the whole week).

## Defined here

### `MorningBriefingAgent`

| Field | Type |
|---|---|
| `name` | `ClassVar[str]` |
| `schedule` | `ClassVar[Optional[str]]` |
| `cost_budget_usd_per_run` | `ClassVar[float]` |
