# foley_quality

*Source: `heterodyne/agents/foley_quality.py`*

agents.foley_quality — librosa-based quality gate for foley ingest.

The user's complaint about the Freesound route was four-fold: bad QUALITY,
inconsistent LENGTH, inconsistent loudness/format (CONSISTENCY), and
unsearchability. This module owns the first three. Searchability is solved
by CLAP embeddings in agents.foley_embeddings.

Given a wav file, analyze() returns a QualityReport with objective metrics
and a verdict (accept / flag / reject). The ingest agent uses the verdict to
decide whether a clip enters the catalog, and uses the trim/loudness numbers
to normalize it on the way in so the whole library is consistent.

Pure numpy/soundfile/librosa/pyloudnorm — no model downloads, no network.
Safe to import on any machine that has the audio stack installed.

## Defined here

### `QualityConfig`

| Field | Type |
|---|---|
| `min_duration_s` | `float` |
| `max_duration_s` | `float` |
| `reject_clip_pct` | `float` |
| `flag_clip_pct` | `float` |
| `min_peak_dbfs` | `float` |
| `flag_flatness` | `float` |
| `dc_offset_warn` | `float` |
| `silence_db` | `float` |
| `target_lufs` | `float` |

### `QualityReport`

| Field | Type |
|---|---|
| `path` | `str` |
| `ok` | `bool` |
| `verdict` | `Verdict` |
| `reasons` | `list[str]` |
| `duration_s` | `float` |
| `sample_rate` | `int` |
| `channels` | `int` |
| `peak_dbfs` | `float` |
| `rms_dbfs` | `float` |
| `clip_pct` | `float` |
| `dc_offset` | `float` |
| `noise_floor_dbfs` | `float` |
| `snr_db` | `float` |
| `spectral_flatness` | `float` |
| `loudness_lufs` | `float | None` |
| `lead_silence_s` | `float` |
| `tail_silence_s` | `float` |
| `trimmed_duration_s` | `float` |

## Top-level functions

- **`analyze()`** — Measure objective quality metrics for a wav and assign a verdict.
