# extractor

*Source: `heterodyne/agents/writers_room/extractor.py`*

agents/writers_room/extractor.py

Stage 5 — ledger extraction over the finished segment: world-ledger
updates, tone signature, closing positions, and setup tracking, read out
of the text that was actually written. Extraction is far more reliable
than simultaneous emission — the model reads a finished artifact instead
of bookkeeping while composing.
Route: call_type "wr_ledger_extractor".

## Top-level functions

- **`extract_segment()`** — Return the extraction dict (ledger updates, tone, positions, setup
