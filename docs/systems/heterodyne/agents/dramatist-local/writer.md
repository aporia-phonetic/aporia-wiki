# writer

*Source: `heterodyne/agents/dramatist_local/writer.py`*

agents.dramatist_local.writer — the plain-prose continuation loop.

This stage is the density fix. Local instruct models treat "write this
segment" as "write one complete scene and stop" (~1,000 words); no prompt
overrides that prior. So instead of asking once, we ask repeatedly: each
call advances the scene toward the current beat by a bounded batch of
exchanges, with the running transcript's tail as context, until the beat's
word share is met or the model signals [BEAT COMPLETE]. Segment length
becomes a loop bound we control instead of a model disposition.

## Defined here

### `TokenTally`

Accumulates token usage across every pipeline call.

| Field | Type |
|---|---|
| `input_tokens` | `int` |
| `output_tokens` | `int` |
| `calls` | `int` |

### `SegmentProse`

| Field | Type |
|---|---|
| `segment` | `int` |
| `transcript` | `str` |
| `hook` | `str` |
| `batches` | `int` |
| `beats_completed` | `int` |

## Top-level functions

- **`transcript_tail()`** — Last ~max_words of the transcript, cut on line boundaries.
- **`clean_batch()`** — Normalize one continuation batch into clean tagged script lines.
- **`ngram_overlap()`** — Fraction of new_text's n-grams that already appear in prior_text.
- **`narration_stats()`** — (word share of NARRATION lines, longest consecutive NARRATION run).
- **`prose_to_readable()`** — Convert 'SPEAKER: text' lines to the '[SPEAKER] text' readable format
- **`generate_segment_prose()`** — Run the continuation loop for one segment; returns its prose + hook.
- **`generate_episode_prose()`** — Prose for every segment in order, chaining hooks between segments.
