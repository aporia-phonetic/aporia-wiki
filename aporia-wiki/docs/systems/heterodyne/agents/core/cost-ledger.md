# cost_ledger

*Source: `heterodyne/agents/cost_ledger.py`*

Persistent cost ledger — one SQLite row per LLM call.

Stores every routed call's token counts and computed dollar cost so
spend is visible across runs (not just within a single router instance).

Usage:
    from agents.cost_ledger import CostLedger

    ledger = CostLedger()
    ledger.record(run_id="s01e03", call_type="dramatist_segment",
                  backend="anthropic", model="claude-sonnet-4-6",
                  input_tok=4200, output_tok=8100, cost_usd=0.1341)
    print(ledger.run_summary("s01e03"))
    print(ledger.all_time_summary())

## Defined here

### `CostLedger`

SQLite-backed ledger. Thread-safe: a process-wide lock serializes every
connection access, and WAL mode lets concurrent readers proceed without
blocking on the writer, so concurrent batch/episode runs can't interleave
writes and lose or double-count cost rows.
