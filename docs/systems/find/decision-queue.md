# Decision Queue

Core principle: **decisions over actions.** Agents never take
consequential actions directly — they draft a proposal and submit a
Decision; the founder approves. The only auto-actions are within
thresholds explicitly set in `config.py` (e.g.
`auto_approve_threshold_cents`).

Flow: the ten [ops agents](agents/index.md) read ledger state via
`LedgerSnapshot`, submit proposals through `decision_queue/`
(submit / act / defer / notify), and the `Notifier` routes by priority —
P1 → SMS + email, P2 → email, P3 → digest only.

Decisions and every founder action land in an **HMAC-chained audit log**
(`audit/`) — a tamper-evident chain with triggers preventing UPDATE/
DELETE on the underlying rows.
