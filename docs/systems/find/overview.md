# find — Founders Input Needed Daily

Internal business-ops tool for Aporia Phonetic Group. No story content of
its own — it's the company's operations layer, grouped with heterodyne,
auralbouros, and godot-pipeline organizationally (the "launch trio" + one
parked piece) but not part of the fiction.

FastAPI + Vite/React/TypeScript, Dockerized. Runs ten scheduled agents
that watch finance, contracts, subscriptions, customers, documents, and
compliance, surfacing anything needing founder attention into a single
**Decision Queue**:

- Finance, Billing, Payments, Contract, Sales, CustomerSuccess,
  Compliance, Identity, Documents, MorningBriefing, MarketingIntel,
  StrategicIntel — see [Ops Agents](agents/index.md) for the generated
  per-module reference.

Backed by a single-writer SQLite ledger with HMAC-chained audit logging.
Notifications route by priority: P1 → SMS + email, P2 → email, P3 →
digest only.

## Since 2026-06: fleet, board, votes, lore, clock

- **SLM fleet** (`find/fleet/`) — every agent LLM call routes by call-type
  through `config/llm_routing.yaml` with fallback chains and a per-call cost
  ledger; visible at `GET /api/fleet/models` and on the Agents page.
- **Advisory board** — multi-persona deliberation sessions (Board page).
- **Votes** — the Episode-6 branching-season ballot system: hash-chained
  ballot log; closing a window writes the heterodyne `branch_lock.json`
  (Votes page, `/api/votes/...`).
- **Lore feed** — `GET /api/lore` serves the heterodyne lore export to the
  auralbouros app.
- **Clock** — read-only view of the ~22 cron jobs + one-shots that drive
  everything (`GET /api/scheduler/jobs`, Clock page).
- **Rebrand** — the frontend now presents as **FIND** (formerly AOL); stored
  `'AOL'`/`'AEON'` enum values are an intentional DB/API contract.

## Engine bridge

find's own roadmap notes a bidirectional sync with **the-heterodyne** as
"sketched but minimal" — the integration point for royalties/
customer-success data flowing between the ops tool and the story engine.
See [Decision Queue](decision-queue.md) and
[Engine bridge](engine-bridge.md).

## Existing docs (not mirrored here)

`README.md` (overview + quick start), `ARCHITECTURE.md` (contributor
guide, bird's-eye system diagram), `DEPLOY.md` (Dockerfile/VPS deployment),
`PREREQUISITES.md` (external account setup — Mercury, Stripe, LLC) are the
canonical ops docs and stay in the find repo. The
[cheat sheet](cheatsheet.md) is mirrored here from `find/CHEATSHEET.md`.
