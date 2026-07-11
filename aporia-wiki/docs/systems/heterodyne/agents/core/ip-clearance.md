# ip_clearance

*Source: `heterodyne/agents/ip_clearance.py`*

agents/ip_clearance.py

IP Clearance Agent — A1 from the voice-update spec.

Runs between Dramatist output and Archivist ledger commit. Checks every NEW
name introduced in an episode (characters, locations) against three independent
IP conflict signals before the canonical ledger commit lands.

Three checks per name:
  1. USPTO TESS — live trademark search, International Class 41 (Entertainment
     Services) and Class 28 (Games / Toys). Catches active registrations and
     pending applications.
  2. Semantic Similarity — Claude API call (routes to local LLM once A7 is live)
     asking whether the name is confusingly similar to well-known IP in
     entertainment, games, or media.
  3. LOC Title Catalog — Library of Congress catalog search for exact or
     near-exact title matches across registered copyrighted works.

Verdicts:
  GREEN  — No conflict found. Archivist proceeds with commit.
  YELLOW — Possible conflict; human review advised. Archivist commits but
           writes a P2 DecisionItem to the ip_clearance_queue table.
  RED    — Clear conflict. Archivist blocks the commit with RuntimeError.
           Regenerate the offending name and re-run.

Cleared names are cached in the SQLite World Ledger DB (table: ip_clearance_cache)
so names are never re-checked once GREEN. YELLOW/RED results re-check after 90 days.

Configuration (.env):
  IP_CLEARANCE_ENABLED   true | false  (default: true)
  IP_CLEARANCE_LOG_LEVEL verbose | normal | quiet (default: normal)

The agent is safe to instantiate with llm_client=None — the semantic check
will return YELLOW (conservative) and log a warning, rather than error out.

## Defined here

### `ClearanceVerdict`

### `ClearanceMode`

Per-check evidence requirement.

LENIENT (default — current production behavior, byte-identical to pre-mode code):
    Each check returns its natural verdict. Failure-to-verify cases
    (USPTO unreachable, LLM unavailable, LOC unreachable) fall back to
    conservative defaults — YELLOW for USPTO/semantic, GREEN for LOC.

STRICT (opt-in, off until post-hardware-transition wiring):
    Each check must produce POSITIVE evidence of clearance to return
    GREEN. Failure-to-verify cases return RED instead of the lenient
    fallback. This closes the "we couldn't check so we'll assume it's
    fine" gap.

### `ClearanceResult`

Clearance result for a single name.

| Field | Type |
|---|---|
| `result_id` | `str` |
| `name` | `str` |
| `verdict` | `ClearanceVerdict` |
| `reason` | `str` |
| `uspto_verdict` | `ClearanceVerdict` |
| `uspto_hits` | `List[str]` |
| `semantic_verdict` | `ClearanceVerdict` |
| `semantic_flags` | `List[str]` |
| `loc_verdict` | `ClearanceVerdict` |
| `loc_hits` | `List[str]` |
| `checked_at` | `datetime` |
| `from_cache` | `bool` |

### `IPClearanceAgent`

Three-check IP clearance gate for newly introduced names.

Usage (Archivist instantiates this):
    # Preferred — route through the A7 LLM router:
    from agents.llm_router import get_default_router
    agent = IPClearanceAgent(db_path=ledger_db_path, llm_router=get_default_router())

    # Legacy — direct anthropic client (still supported for backward compat):
    agent = IPClearanceAgent(db_path=ledger_db_path, llm_client=llm)

    results = agent.check_names(["Maren", "Verdant Deep"], context="pulp audio drama")
    red  = [r for r in results if r.verdict == ClearanceVerdict.RED]
    yellow = [r for r in results if r.verdict == ClearanceVerdict.YELLOW]
