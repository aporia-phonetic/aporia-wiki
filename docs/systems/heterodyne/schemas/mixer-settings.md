# mixer_settings

*Source: `heterodyne/schemas/mixer_settings.py`*

## Defined here

### `MixerSettings`

Audio mixer configuration for foley, music, and voice levels.

| Field | Type |
|---|---|
| `voice_db` | `float` |
| `foley_db` | `float` |
| `music_db` | `float` |
| `master_lufs` | `float` |
| `sidechain_foley_ratio` | `float` |
| `sidechain_music_ratio` | `float` |
| `sidechain_bed_ratio` | `float` |
| `transmission_enabled` | `bool` |
| `transmission_intensity` | `float` |
| `transmission_band_low` | `int` |
| `transmission_band_high` | `int` |
| `transmission_noise_enabled` | `bool` |
| `transmission_tremor_enabled` | `bool` |
| `transmission_tremor_hz` | `float` |
| `transmission_stamps_enabled` | `bool` |
| `foley_pan_spread` | `float` |
| `stereo_master_enabled` | `bool` |
