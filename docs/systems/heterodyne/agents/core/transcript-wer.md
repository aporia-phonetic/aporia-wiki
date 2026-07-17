# transcript_wer

*Source: `heterodyne/agents/transcript_wer.py`*

agents/transcript_wer.py — Engine-neutral ASR transcript normalization + WER.

Factored out of scripts/voice_qa.py so agents/voice_engine.py's render-verify-
reroll QA loop (ENABLE_RENDER_QA_LOOP) shares the exact same normalization and
edit-distance logic as the offline voice_qa.py report, instead of two subtly
different WER implementations drifting apart over time.

## Top-level functions

- **`normalize_words()`** — 
- **`word_error_rate()`** — Word error rate via Levenshtein edit distance over word lists.
