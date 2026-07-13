# extractor

*Source: `heterodyne/agents/dramatist_local/extractor.py`*

agents.dramatist_local.extractor — structured segment-meta extraction.

One small-JSON call per segment over the finished prose: world ledger
updates, closing character positions, locations, time elapsed, tone
signature. Retried with error feedback; on final failure it salvages
rather than silently losing state: every raw failed response is dumped to
SEG{n}_extract_failed.json for later recovery, a minimal positions-only
fallback call is tried, and the returned meta carries extraction_failed
so the caller can surface it — the isolated runner still produces a
valid episode rather than discarding an hour of prose generation.

## Top-level functions

- **`extract_segment_meta()`** — Extract SegmentScript bookkeeping fields from one segment's prose.
