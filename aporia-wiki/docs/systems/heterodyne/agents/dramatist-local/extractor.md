# extractor

*Source: `heterodyne/agents/dramatist_local/extractor.py`*

agents.dramatist_local.extractor — structured segment-meta extraction.

One small-JSON call per segment over the finished prose: world ledger
updates, closing character positions, locations, time elapsed, tone
signature. Retried with error feedback; degrades to safe defaults on
final failure (the isolated runner still produces a valid episode, with
a loud warning) rather than discarding an hour of prose generation.

## Top-level functions

- **`extract_segment_meta()`** — Extract SegmentScript bookkeeping fields from one segment's prose.
