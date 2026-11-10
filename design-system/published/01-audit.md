# Audit: tokens and WCAG 2.2 AA

> **Resolved in v1.1.** All five failures below are fixed by the applied changes (see "Changes applied"). Re-check with the v1.1 tokens: light link 5.65–7.02:1 on every surface, light control border 3.03–3.77:1, selection indicator ≥4.56:1, and every component preview's live contrast strip passes in both themes. The matrices below record the original v1.0 audit.

Sources: `tokens.css`, `design-tokens.json`, `CONTRAST-SPOT-CHECKS.md`, `ACCESSIBILITY-TEST-PLAN.md`. The ratios use WCAG 2 relative luminance, computed from exact hex values. The ColorSurfaces and States previews recompute them live from the tokens.

## 1. Token hierarchy

| Tier | What | Count | Notes |
|---|---|---:|---|
| Primitive: neutrals | paper, white, mineral, mist, silver · ink, midnight, deep-blue, night-raised · blue-slate, steel | 11 | Two families: warm-light and blue-dark. |
| Primitive: cobalt ramp | cobalt-50 … cobalt-700 | 8 | 100, 300, 400 are unassigned. |
| Primitive: role-named | lightTertiary, lightBorderStrong, darkText*, darkBorder*, darkAccent*, darkSelected* | 11 | **Leak:** primitives named for a role and theme. The dark accents sit off the cobalt ramp. |
| Primitive: status | success/warning/error/info × light/dark × fg/bg | 16 | **JSON only.** Missing from tokens.css. |
| Semantic | bg ×4, text ×4, border ×3, action ×4, focus ×1, state ×8 | 24 | CSS has 16 (no state). Themes switch via `[data-theme="dark"]` only. |
| Type | 2 families, 3 weights, 4 tracking, 12 styles, responsive steps | — | CSS exposes raw sizes and line-heights; weight and tracking per style live only in JSON. |
| Space / radius / layout | 12 spacing, 4 radii, 2 widths, 4 breakpoints, 3 grid counts | — | Breakpoints and grid are JSON only. |

## 2. Contrast matrix: text (needs 4.5:1)

| Foreground | canvas | surface | elevated | sunken |
|---|---:|---:|---:|---:|
| **Light** text-primary `#0B1220` | 17.92 | 16.53 | 18.72 | 15.07 |
| text-secondary `#455166` | 7.66 | 7.07 | 8.01 | 6.45 |
| text-tertiary `#5C6677` | 5.55 | 5.12 | 5.80 | 4.67 |
| action-primary / link `#2F5BFF` | 4.95 | 4.56 | 5.17 | **4.16 ✕** |
| action-hover `#2448D8` | 6.71 | 6.19 | 7.02 | 5.65 |
| selected-text `#1D37B8` | 8.77 | 8.09 | 9.17 | 7.38 |
| success · warning · error · info | 6.82 · 6.56 · 6.29 · 6.71 | 6.29 · 6.05 · 5.80 · 6.19 | 7.13 · 6.85 · 6.57 · 7.02 | 5.74 · 5.51 · 5.29 · 5.65 |
| **Dark** text-primary `#F4F6FA` | 15.98 | 14.58 | 13.19 | 17.30 |
| text-secondary `#C2CAD6` | 10.46 | 9.55 | 8.64 | 11.33 |
| text-tertiary `#A4B0C0` | 7.86 | 7.17 | 6.49 | 8.51 |
| action-primary / link `#7EA0FF` | 6.88 | 6.28 | 5.68 | 7.45 |
| action-hover `#A0B7FF` | 8.82 | 8.04 | 7.28 | 9.55 |
| selected-text `#C7D4FF` | 11.76 | 10.73 | 9.71 | 12.74 |
| success · warning · error · info | 9.91 · 10.88 · 8.52 · 8.82 | 9.04 · 9.93 · 7.77 · 8.04 | 8.18 · 8.99 · 7.03 · 7.28 | 10.73 · 11.79 · 9.23 · 9.55 |

Margins to watch: light link on surface is 4.56:1, and light tertiary on sunken is 4.67:1.

## 3. Contrast matrix: fills, states, non-text (3:1 unless text)

| Pair | Light | Dark | Result |
|---|---:|---:|---|
| on-accent label on action-primary | 5.17 | 7.45 | Pass |
| on-accent on action-hover | 7.02 | 9.55 | Pass |
| on-accent on pressed (**no token**) | — | — | Missing |
| selected-text on selected-bg | 8.20 | 8.16 | Pass |
| selected-bg vs canvas (does the fill alone signal selection?) | 1.07 | 1.44 | **Not perceivable**: needs a non-color cue |
| status text on own status bg (S · W · E · I) | 6.42 · 6.32 · 5.75 · 6.27 | 7.04 · 7.46 · 6.50 · 6.12 | Pass |
| text-primary on status bgs | 16.4–17.3 | 10.9–12.2 | Pass |
| focus-ring vs canvas · surface · elevated · sunken | 6.71 · 6.19 · 7.02 · 5.65 | 8.82 · 8.04 · 7.28 · 9.55 | Pass |
| focus-ring vs action-primary fill | 1.36 | 1.28 | Pass **only because of the 3px offset** |
| focus-ring vs selected-bg | 6.27 | 6.12 | Pass |
| border-strong (input boundary) on canvas · surface · elevated · sunken | **2.80 · 2.58 · 2.92 · 2.35** | 3.67 · 3.35 · 3.03 · 3.98 | **Light fails** |
| border-default | 1.53 · 1.42 · 1.60 · 1.29 | 1.95 · 1.78 · 1.61 · 2.11 | Decorative only |
| border-subtle | 1.19 · 1.10 · 1.24 · 1.00 | 1.43 · 1.31 · 1.18 · 1.55 | Decorative only (invisible on sunken) |
| link vs surrounding body text (if not underlined) | 3.62 (source) / 2.67 (proposed) | 2.32 | **Underline required** |
| disabled (no token) | — | — | Missing. Exempt from 1.4.3, but must stay legible |
| visited link (no token) | — | — | Missing |
| text on imagery / scrim (no token) | — | — | Missing |

## 4. Failures

1. **Light link text on sunken: 4.16:1** (`color-action-primary` on `color-bg-sunken`). Fails 1.4.3.
2. **Light `color-border-strong`: 2.35–2.92:1** on every surface. Fails 1.4.11 when used for inputs or secondary-button boundaries.
3. **Selection by fill alone**: `color-action-selected-bg` against canvas is 1.07:1 (light) and 1.44:1 (dark). Fails 1.4.1/1.4.11 unless paired with another cue.
4. **Links by color alone**: in dark, the link differs from body text by 2.32:1, under the 3:1 needed to rely on color plus a hover/focus cue. Fails 1.4.1 without an underline.
5. **Focus ring on fills**: 1.28–1.36:1 against the cobalt button. This passes only while the 3px offset keeps the ring on the canvas. Any `outline-offset: 0` or clipping container makes it fail 2.4.7 visibility and 1.4.11.

## 5. Missing semantic tokens

`color-text-link`, `color-text-link-hover`, `color-text-link-visited` · `color-action-pressed` · `color-disabled-text`, `-bg`, `-border` · `color-border-control` (3:1) · `color-selected-indicator` · `color-overlay-scrim`, `color-text-on-image` · status tokens in CSS · focus-ring width and offset · link underline thickness and offset · motion duration and easing · control min-height (target size) · elevation/shadow (or an explicit "none") · a `prefers-color-scheme` hook for the dark theme.

## 6. Inconsistencies between the two files

| Item | tokens.css | design-tokens.json |
|---|---|---|
| Label tracking | `--tracking-label: 0.02em` | `tracking.label: 0.04em`, but `labelMd` uses 0.02em |
| h3 / h4 tracking | not tokenized | -0.02em / -0.015em in the style, no tracking token |
| `micro` style | absent | 11/15, 500 |
| Weight per style | absent | in each style |
| Status colors | absent | 16 primitives + 8 semantic |
| Breakpoints, grid columns | only as raw media queries | tokenized |
| Dark theme trigger | `[data-theme="dark"]` only | n/a |
| Primitive naming | `--color-text-tertiary:#5C6677` raw in the semantic layer | `lightTertiary` primitive |
| Dark accent ramp | #7EA0FF / #A0B7FF / #C7D4FF | same, but none are cobalt-ramp steps (cobalt-300 is #8CA5FF) |
| `info` | — | duplicates cobalt-600 / focus (light) and dark-accent-hover / focus (dark) |

Units: sizes and line-heights are in px. Browser zoom works (1.4.4 passes), but a user's default font-size setting is ignored, and px line-heights don't scale with text. See the proposals.

## 7. Interaction checks (to run on the rendered build)

- **Focus visibility:** passes on all four surfaces in both themes (≥5.65:1). Keep the 3px offset, and don't put `overflow: hidden` on card and frame wrappers that contain focusable children (the card in the layout previews moves focus to the card outline using `:has()`).
- **Non-color cues:** links get an underline, selection gets an indicator plus `aria-current` plus weight, status gets an icon and a word, and errors get text tied to the field with `aria-describedby`.
- **Reflow and text size:** the 375px preview shows no horizontal scroll and no fixed-height text containers. Test 200% zoom and 1.4.12 text-spacing overrides in the real build.
- **Keyboard:** nav, cards (one tab stop per card through the title link) and buttons are all reachable in DOM order, with no traps. `aria-disabled` keeps disabled buttons focusable so they can be discovered.
- **Semantics:** one H1, ordered H2/H3, `nav` with `aria-label`, `article` per case study, `dl` for metadata, `figure`/`figcaption`.
- **Reduced motion:** transitions are wrapped in `prefers-reduced-motion: no-preference`, and no information is animated.
- Not yet done: screen-reader pass, forms and error states (out of scope until components), real imagery.
