# voice_sentinel

*Source: `heterodyne/agents/voice_sentinel.py`*

agents/voice_sentinel.py

Voice Sentinel — post-generation dialogue consistency checker.

Runs on completed scene blocks after the Dramatist generates them but before
the Archivist writes the final ledger. Checks whether dialogue conforms to
each character's vocal personality rules.

Two coverage modes:

FREE PATH (default, VOICE_SENTINEL_FULL_COVERAGE=false):
  Runs only on blocks flagged high_stakes=True in the scene block.
  Approximately 20-30 blocks per episode (closing hooks, secret disclosures,
  relationship rupture scenes). No additional cost above standard QA.

PAID PATH (opt-in, VOICE_SENTINEL_FULL_COVERAGE=true):
  Runs on all dialogue blocks in the episode.
  Hard cap: VOICE_SENTINEL_MAX_SPEND_USD env var (default $0.50/episode).
  Once cap is hit, sentinel stops for the remainder of the episode.
  Remaining unchecked blocks are logged but not flagged.

Both paths use identical prompt and output structure.
Switch is a single env flag — no code changes required.

Violation handling:
  high severity  → trigger regeneration of that specific block (caller decides)
  medium severity → logged, passed to review queue
  low severity   → logged only

Cost model (claude-sonnet-4-6):
  ~250 tokens per call (input + output)
  ~$0.0014 per call at current pricing
  Full episode coverage (~160 dialogue blocks): ~$0.22
  Cap at $0.50 provides safe runway for episode variation

## Defined here

### `SentinelResult`

Result for a single dialogue block check.

| Field | Type |
|---|---|
| `block_id` | `str` |
| `character` | `str` |
| `violation` | `bool` |
| `rule_violated` | `Optional[str]` |
| `suggested_fix` | `Optional[str]` |
| `severity` | `Optional[str]` |
| `skipped` | `bool` |

### `EpisodeSentinelReport`

Complete Voice Sentinel report for one episode.

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `coverage_mode` | `str` |
| `blocks_checked` | `int` |
| `blocks_skipped` | `int` |
| `violations_found` | `int` |
| `high_severity_count` | `int` |
| `estimated_cost_usd` | `float` |
| `cap_reached` | `bool` |
| `results` | `List[SentinelResult]` |

### `VoiceSentinelAgent`

Voice Sentinel — post-generation dialogue consistency checker.

Checks whether dialogue lines conform to their character's vocal personality
rules. Closes the feedback loop that vocal personality prompts open but
cannot complete alone.

Vocal distinctiveness is the primary mechanism through which audio drama
creates the impression of real characters. Over a 12-episode season,
characters without this check gradually converge toward the Dramatist's
default voice. The sentinel prevents that convergence.
