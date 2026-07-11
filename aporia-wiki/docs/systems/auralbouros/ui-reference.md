# UI element reference

Condensed pointer to the app's own
`docs/AURALBOUROS_UI_ELEMENT_REFERENCE.md` ("for theme deck design, all
values sourced directly from the codebase") — kept there, not mirrored
here, because it's a living design-token reference that changes with the
codebase.

Key facts worth surfacing:

- **Single source of truth for theming:** `src/theme/colors.ts`. Every
  screen/component imports color values from this one file — a full
  visual re-skin means replacing values there (two documented
  exceptions live in that doc's §9).
- **Current palette:** Dracula (`bg #282a36`, `surface #1e1f29`, ...).
- **No custom fonts** — system defaults throughout, except one
  hardcoded `fontFamily: 'monospace'` in the Settings screen.

See that file directly for the full color token table, typography
scale, border-radius scale, navigation chrome spec, and the
screen-by-screen inventory.
