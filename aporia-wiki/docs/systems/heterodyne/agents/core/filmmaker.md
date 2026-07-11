# filmmaker

*Source: `heterodyne/agents/filmmaker.py`*

agents/filmmaker.py — The Filmmaker (Agent 27)

Generates compilation videos from existing episode assets using FFmpeg.
Zero new API dependencies — pure FFmpeg assembly over pipeline outputs.

Compilation types:
  season_recap         N-second clip from each episode concatenated in order.
  character_arc        Scenes featuring a specific character, across episodes.
  theme_compilation    Scenes matching a theme (battles/romance/cliffhangers).
  social_clip          A short clip from a single specific episode.

All input comes from files the pipeline has already produced:
  audio/output/video/S{S}E{E:02d}_illustrated.mp4   — per-episode video
  data/worlds/{world_id}/seasons/.../S{S}E{E:02d}.json  — episode JSON

Output:  exports/compilations/{compilation_type}_{label}_{timestamp}.mp4
         exports/compilations/shorts/{label}_{timestamp}.mp4  (for social_clip)

## Defined here

### `ClipSpec`

One time-window to extract from a source MP4.

| Field | Type |
|---|---|
| `source_path` | `Path` |
| `start_s` | `float` |
| `duration_s` | `float` |
| `episode` | `int` |
| `label` | `str` |

### `FilmmakerReport`

| Field | Type |
|---|---|
| `compilation_type` | `str` |
| `output_path` | `Optional[Path]` |
| `label` | `str` |
| `source_episodes` | `list[int]` |
| `clips_assembled` | `int` |
| `total_duration_s` | `float` |
| `ffmpeg_return_code` | `int` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `Filmmaker`

Assembles compilation videos from existing episode MP4 outputs.

Parameters
----------
output_dir:
    Root audio/video output directory. Episode MP4s are at
    {output_dir}/video/S{S}E{E:02d}_illustrated.mp4.
data_dir:
    Path to worlds data root (data/worlds/).
compilations_dir:
    Where output compilations are written. Defaults to exports/compilations/.
ffmpeg_path:
    Path to the ffmpeg binary. Defaults to FFMPEG_PATH env var or "ffmpeg".
stub:
    If True, skip FFmpeg execution (dry-run / test mode).

## Top-level functions

- **`main()`** — 
