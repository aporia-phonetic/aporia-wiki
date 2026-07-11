# video_compositor

*Source: `heterodyne/agents/video_compositor.py`*

agents/video_compositor.py — Illustrated Video Compositor (B1)

Assembly agent: reads existing episode artifacts (audio, scene imagery,
character portraits, segment JSON) and produces an illustrated MP4 using
FFmpeg's zoompan filter (Ken Burns effect).

No new content is generated — everything needed already exists as discrete
timed artifacts from the audio drama pipeline. This is a pure assembly agent.

Outputs:
  {output_dir}/video/S{S}E{E:02d}_illustrated.mp4   — 16:9 landscape (YouTube)
  {output_dir}/video/S{S}E{E:02d}_shorts.mp4         — 9:16 vertical (Shorts/TikTok)
                                                        built only when a social-flagged
                                                        block exists in the episode

Gate: before Day 1 launch (B1). YouTube monetisation requires watch hours;
watch hours require video. The 60-episode buffer can be uploaded as illustrated
video on launch day.

FFmpeg is required (in PATH or set FFMPEG_PATH). All other processing uses
stdlib + existing pipeline artifacts.

## Defined here

### `SceneSegment`

One timed image segment in the video timeline.

| Field | Type |
|---|---|
| `image_path` | `Optional[Path]` |
| `duration_s` | `float` |
| `location` | `str` |
| `dominant_character` | `str` |
| `zoom_direction` | `str` |
| `pan_x` | `float` |

### `CompositeReport`

Output from VideoCompositor.compose_episode().

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `output_path` | `Optional[Path]` |
| `shorts_path` | `Optional[Path]` |
| `total_duration_s` | `float` |
| `scene_count` | `int` |
| `images_used` | `int` |
| `fallback_frames` | `int` |
| `ffmpeg_return_code` | `int` |
| `error` | `str` |

### `VideoCompositor`

Assembles an illustrated video from episode audio drama artifacts.

Parameters
----------
output_dir:
    Video files are written directly under this directory (caller
    passes an already type/world/season-scoped path, e.g.
    schemas.paths.output_season_dir("video", world_id, season)).
audio_dir:
    Directory where the Mixer wrote the finished episode MP3
    ({audio_dir}/{ep_tag}.mp3), e.g.
    schemas.paths.output_season_dir("audio", world_id, season).
    Defaults to output_dir for backward compatibility, but audio and
    video are now separate output types with separate roots — pass
    this explicitly.
images_dir:
    Directory where ImageAgent stores generated images, e.g.
    schemas.paths.output_type_dir("images", world_id). Defaults to
    output_dir for backward compatibility.
data_dir:
    Path to the worlds data directory (data/worlds/).
    Used to locate episode JSON files.
ffmpeg_path:
    Path to the ffmpeg binary. Defaults to "ffmpeg" (assumes in PATH).
stub:
    If True, skip actual FFmpeg execution (dry-run / test mode).
    CompositeReport will be returned with ffmpeg_return_code=0 and
    output_path pointing to where the file WOULD be.
