# sophrosyne — a personal honesty engine

Standalone APORIA repo (formerly **LODESTAR**, renamed 2026-06) — not part
of the launch trio and not part of the fiction. A single-user, on-device,
encrypted system that holds an honest model of where you actually are versus
where you say you want to be, tracks the drift between the two, and helps
you close the gap yourself. Its core stance: *"I can't get you there. You
can."*

Architecturally it is the heterodyne **World Ledger / Chronicle / Archivist**
stack redirected from a fictional world onto a real person: Knowledge State,
Trust Map, Callback registry, the dual-track Historian, the Perception-Drift
model, and the LLM router all ported and renamed.

- **Stack** — TypeScript (Node ≥ 20) locked core; Expo/React Native shell
  with SQLCipher on-device; `@anthropic-ai/sdk` reasoning layer.
- **Talk to it** — `npm run harness` (text loop) and `npm run observe`
  (autonomous workspace calibration). See the [cheat sheet](cheatsheet.md)
  (mirrored from `sophrosyne/CHEATSHEET.md`).
- **Privacy boundary** — Gmail/Drive/Calendar arrive only as JSONL digests
  dropped into an inbox directory; the engine never gets Google write
  access. Everything at rest is encrypted (AES-256-GCM / SQLCipher).

Canonical docs live in the repo: `README.md`, `MANUAL.md`, `STATUS.md`,
`MCP_SETUP.md`. This system is excluded from the wiki's generated reference
(it's personal tooling, not ecosystem content) — only this overview and the
cheat-sheet mirror live here.
