# season_architect

*Source: `heterodyne/agents/writers_room/season_architect.py`*

agents/writers_room/season_architect.py

Season-level gate-chain quality: a critic pass that audits the whole chain
(escalation shape, function/hook variety, setup-before-payoff, cast
distribution) and a refine pass that applies accepted rewrites.

Never mutates plot_gates.json — proposals go to plot_gates.proposed.json
beside it for showrunner approval (Story Vault pattern: the engine
proposes, the human disposes).

Routes: call_type "wr_gate_critic" / "wr_gate_refiner".

## Top-level functions

- **`load_gate_chain()`** — Return (raw_file_dict, gates_list) for a world+season.
- **`critique_gate_chain()`** — One critic call over the whole chain. Returns the findings dict:
- **`refine_gate_chain()`** — One refiner call applying the critic's proposed rewrites. Returns
- **`review_season_gates()`** — Full season gate review. Writes findings (and, when refine=True and
