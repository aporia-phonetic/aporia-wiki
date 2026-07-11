# animator

*Source: `heterodyne/agents/animator.py`*

agents/animator.py — The Animator (Agent 26)

Generates professional animation briefs and storyboards from existing
episode assets. This is a storyboard/brief GENERATOR — it produces
documentation to hand to an animation studio, not an animation system.

Reads from:
  output/video/{world_id}/season_XX/S{S}E{E:02d}_illustrated.mp4 — source for keyframe extraction
  output/audio/{world_id}/season_XX/voice/S{S}E{E:02d}/S{S}E{E:02d}_manifest.json — per-block timing
  data/worlds/{world_id}/seasons/.../S{S}E{E:02d}.json — episode script

Outputs:
  output/storyboards/{world_id}/season_XX/S{S}E{E:02d}_storyboard.pdf — Studio-ready PDF storyboard
  output/storyboards/{world_id}/season_XX/S{S}E{E:02d}_timing.json    — Frame-by-frame timing JSON

Hardware: CPU only (FFmpeg frame extraction, fpdf2 PDF). Zero GPU needed.

## Defined here

### `StoryboardPanel`

One panel in the storyboard.

| Field | Type |
|---|---|
| `panel_index` | `int` |
| `scene_index` | `int` |
| `start_s` | `float` |
| `end_s` | `float` |
| `location` | `str` |
| `dominant_character` | `str` |
| `dialogue_sample` | `str` |
| `action_description` | `str` |
| `camera_direction` | `str` |
| `frame_path` | `Optional[Path]` |

### `AnimatorReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `season` | `int` |
| `episode` | `int` |
| `storyboard_path` | `Optional[Path]` |
| `timing_path` | `Optional[Path]` |
| `panels_generated` | `int` |
| `frames_extracted` | `int` |
| `total_duration_s` | `float` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `Animator`

Generates animation storyboards and timing documents from episode assets.

Parameters
----------
video_dir:
    Where VideoCompositor wrote the illustrated MP4, e.g.
    schemas.paths.output_season_dir("video", world_id, season).
    MP4 read from {video_dir}/{ep_tag}_illustrated.mp4.
voice_dir:
    Where VoiceEngine wrote its per-episode manifest, e.g.
    schemas.paths.output_season_dir("audio", world_id, season) / "voice".
    Manifest read from {voice_dir}/{ep_tag}/{ep_tag}_manifest.json.
    Defaults to video_dir for backward compatibility, but audio and
    video are separate output types with separate roots — pass this
    explicitly.
data_dir:
    World data root (data/worlds/).
storyboards_dir:
    Where storyboard PDFs and timing JSONs are written, e.g.
    schemas.paths.output_season_dir("storyboards", world_id, season).
ffmpeg_path:
    Path to ffmpeg binary. Defaults to FFMPEG_PATH env var or "ffmpeg".
llm_router:
    Optional LLMRouter for LLM-generated camera annotations. If None,
    template-based annotations are used (no API cost).
stub:
    If True, skip frame extraction and PDF generation (dry run).

## Top-level functions

- **`main()`** — 
