# judge

*Source: `heterodyne/agents/dramatist_local/judge.py`*

agents.dramatist_local.judge — local fidelity judges (quality loop).

Two cheap structured checks over each segment's raw prose, run BEFORE
annotation so a failed segment regenerates without wasting metadata calls:

  world fidelity   — does any line contradict the world's setting facts?
                     (the llama3.3:70b "sea in an aerial world" bug class)
  premise fidelity — does the segment honor the gate's dramatic direction?
                     (the inverted-asylum bug class)

World facts are data-driven (world_config via context.build_world_context);
nothing here knows any world. Judges are advisory: they gate regeneration
attempts, never crash the pipeline.

## Top-level functions

- **`judge_world_fidelity()`** — Setting-contradiction flags plus the count of unchecked passages.
- **`verify_world_flags()`** — Second-opinion pass on each world flag: literal contradiction, or
- **`judge_premise_fidelity()`** — Gate-direction check: {"honors_gate": bool, "direction_errors": [...]}.
- **`judge_continuity()`** — Cross-segment check: does SEG n's opening contradict SEG n-1's
- **`run_segment_judges()`** — All judges; returns the verdict doc stored in SEG{n}_judge.json.
- **`fidelity_feedback_block()`** — System-prompt addendum for a regeneration run: what to avoid.
