# checkpoints

*Source: `heterodyne/agents/dramatist_local/checkpoints.py`*

agents.dramatist_local.checkpoints — file-based resume state for long runs.

The unit of recoverable work is finer than the cloud path's per-segment
checkpoint: prose is checkpointed after every accepted continuation batch,
so an overnight run interrupted mid-segment resumes mid-beat.

Layout under checkpoint_dir/S{S}E{EE}/ (same subdir convention as
Dramatist._checkpoint_subdir):

    beats.json               validated beat sheet
    SEG{n}_prose.txt         running plain-script transcript
    SEG{n}_prose_state.json  {beat_index, batch_count, hook, done}
    SEG{n}_blocks.json       post-parse/annotation intermediate
    SEG{n}.json              final validated SegmentScript (cloud format)
    SEG{n}_judge.json        judge verdicts

All writes are atomic (temp file + rename), matching Dramatist._write_checkpoint.

## Top-level functions

- **`episode_subdir()`** — 
- **`atomic_write_text()`** — 
- **`atomic_write_json()`** — 
- **`save_beats()`** — 
- **`load_beats()`** — 
- **`save_prose()`** — 
- **`load_prose()`** — 
- **`save_blocks()`** — 
- **`load_blocks()`** — 
- **`save_segment()`** — 
- **`load_segment()`** — 
- **`save_judge()`** — 
- **`load_judge()`** — 
- **`clear_segment_work()`** — Remove one segment's prose/blocks/final checkpoints (judge history
- **`clear_episode()`** — Remove every checkpoint file for one episode (post-success cleanup).
