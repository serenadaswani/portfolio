# Changes applied

## v1.8 one type family and split layout (approved from the v1.8 review)
| # | Change | Type |
|---|---|---|
| A | Metadata voice moves from Geist Mono to Instrument Sans: new `typography.fontFamily.meta` (`--font-meta`) replaces `mono` (`--font-mono` is gone). Every metadata selector now sets `--font-meta` at `type-label` (13px), weight 400, tertiary, tabular figures. Classes renamed: `pm-mono` → `pm-meta-text`, `pm-badge--mono` → `pm-badge--meta`. Geist Mono is no longer loaded. | Token + type role |
| B | **SplitLayout** (`pm-split`, `pm-intro`, `pm-split__nav`, `pm-split__foot`, `pm-split__section`): 360px sticky intro + vertical nav beside the work column at ≥1024px; one column below, with the nav as a wrapping row. `.pm-split__main` is a container. | New |
| B2 | Card `--showcase` + `pm-showcase-grid`: one large surface container per project. The card is its own container, so the same markup lays out copy-left/screen-right at ≥768px and copy-over-screen when narrower. Strongest work full width (`pm-showcase-grid__wide`), supporting work two-up. Hover: sunken fill, screen lifts 8px. | Variant |
| B3 | SideNavigation supports `aria-current="location"` (scroll-spy): weight 500 + cobalt tick, moving under the label in the row layout. | Behaviour |
Landing prototype rebuilt on the split layout with real content (Mensio, Deploy, Apple, Procense, OmniSynkAI, LA time, socials).

## v1.7 one-page portfolio patterns (approved from the side-by-side review)
| # | Change | Type |
|---|---|---|
| 01 | TopNavigation `--floating`: centred, sticky, sized to content, ring + `shadow-xs` → `shadow-md` once scrolled; no current-page indicator; `--bare` drops the container | Variant |
| 02 | Hero: centred sentence (`type-h3`), "Currently designing" chip, Copy email + Résumé | New |
| 03 | Card `--tile`: neutral stage, full screenshot rising flush from the bottom edge, whole-card hover (stage deepens, artwork lifts, ↗ chip) | Variant |
| 04 | `pm-work-grid`: two columns from 768px, right column offset `space-24` | Layout |
| 05 | ExperienceList: mono initials mark, organisation + role, mono years, scope line; `--plain` | New |
| 06 | StatRow: big numbers with mono labels for case-study headers; `--sm` | New |
No token changes.

## v1.6 depth and Bento
| Token | Before | After |
|---|---|---|
| `shadow-xs` | 0 1px 2px ink 6% | 0 1px 2px midnight 4% |
| `shadow-sm` | two layers, ink 4–6% | 0 1px 2px midnight 4%, 0 4px 12px −4px midnight 8% |
| `shadow-md` | 0 8px 24px ink 8% | 0 2px 4px −2px midnight 5%, 0 12px 24px −8px midnight 10% |
| `shadow-lg` (new) | — | 0 4px 8px −4px midnight 5%, 0 24px 48px −16px midnight 16% |
Dark-theme values are black at 24–60% (shadows need more weight to read on Midnight).

Usage: containers (panels, outlined cards, bento tiles, secondary buttons, the selected segment) rest with a `border-subtle` ring + `shadow-xs`. Interactive surfaces get `border-default` + `shadow-sm` on hover. Popover `shadow-md`, Dialog `shadow-lg`, Tooltip `shadow-sm`. Structural hairlines (top nav, tab baseline, footers) moved to `border-subtle`. Inputs keep the 3:1 `border-control`. New component: **Bento**.

## v1.5 icons, alignment and HIG
- **Icons:** every icon is now Lucide (`lucide-static` 0.460.0, ISC), the set shadcn/ui uses: 24 grid, stroke 2. Sizes are 16 (UI), 14 (xs, status, field errors), 12 (badges, checks) and 20 (empty states). Status shapes: circle-check, circle-dot, circle-dashed, info, triangle-alert, octagon-x.
- **Alignment:** text-adjacent icons and checkbox/radio controls centre on the first line using token math (this replaced `1lh`, which resolved against the wrong line box on native inputs). The inline external-link icon can no longer wrap away from its word. A measured check holds every pairing within 1px.
- **Choice spacing:** control → label 8px, option → option 8px, legend → options 8px.
- **Apple HIG:** hover only on hover-capable devices; `touch-action: manipulation`; Increase Contrast and Reduce Transparency overrides (also in tokens.css); safe-area insets; Dialog becomes a bottom sheet below 768px. See "HIG review".

## v1.4 typeface
| Token | Before | After |
|---|---|---|
| `font-sans` | "Geist", sans-serif | "Instrument Sans", sans-serif |
| `font-mono` | "Geist Mono", monospace | unchanged |
| `font-width-display` | — | 90% (new; `display-xl`, `display-lg`) |
| `font-width-text` | — | 100% (new) |
| `tracking-display` | −0.045em | −0.025em |
| `tracking-heading` (h1, h2) | −0.03em | −0.015em |
| `tracking-h3` | −0.02em | −0.01em |
| `tracking-h4` | −0.015em | −0.005em |
Sizes, line heights and weights are unchanged. UI labels stay at 500 (checked at 14px). See the Typeface card for the before and after.

## v1.3 refinement
No token values changed. Component usage changed per the refinement audit: shape language (sm/md/lg roles), no hover shadows (`shadow-md` reserved for overlays), frameless cards, bordered panels, single-cue selection, a mono metadata voice, no uppercase labels, consistent 16px icons with non-scaling strokes. Added Tabs, Input, CheckboxRadio, Popover and Dialog. Shadow token usage notes now read "overlays only".

## v1.2
| Change | Detail |
|---|---|
| X-small controls | `control-height-xs` 24px. `pm-btn--xs` uses `type-caption` at 500, `space-2` padding, `radius-sm` and a 14px icon. |
| Compact sizes | `control-height-md` 44 → **40px**, `lg` 52 → **48px**, `control-min-target` 44 → **24px** for pointers. Under `pointer: coarse`: 44 / 52 / 44px. |
| Hover shadows | `shadow-xs`, `shadow-sm` and `shadow-md`, with deeper dark-theme values. Applied to button, card, thumbnail and frame-expand hover only. |
| Lighter secondary border | New `color-border-button`: light `silver` (was `#7A8496`), dark unchanged. `color-border-control` stays for inputs and thumbnails. |
| Links | Text only: weight 500, no underline at rest, underline on hover. Focus has no outline (2px focus-colour underline + tint). |
| No overlaps | Inset focus rings in nav lists, toolbars, the video bar and the lightbox bar. Wider thumbnail gaps (`space-3`). Panel headers and side-nav meta wrap. Machine-checked on every preview. |

## v1.1

You approved these, and they're now in `design-tokens.json`, `tokens.css` and this system's tokens.

## Color
| # | Change | Light | Dark |
|---|---|---|---|
| A1 | `color-text-link` / `-hover` / `-visited` | cobalt-600 / cobalt-700 / = link | dark-accent / dark-accent-hover / = link |
| A2 | `light-border-strong` `#8D98A8` → `#7A8496`; new `color-border-control` | 3.03–3.77:1 | dark-border-strong 3.03–3.98:1 |
| A3 | `color-selected-indicator` | cobalt-500 | dark-accent |
| — | `color-action-pressed` | cobalt-700 | cobalt-200 |
| — | `color-disabled-text` / `-bg` / `-border` | #7A8496 / mist / silver | dark-border-strong / deep-blue / dark-border-default |
| — | `color-overlay-scrim` | ink 72% | ink 72% |
| — | `color-text-on-image` | white | dark-text-primary |
| — | `color-state-*` ported to CSS | — | — |

## Component-driven additions (new in this round)
| Token | Light | Dark | Why |
|---|---|---|---|
| `color-bg-inverse` | ink | dark-text-primary | Tooltip fill, device bezel |
| `color-text-inverse` | paper | ink | Tooltip text (17.92 / 17.30:1) |
| `color-overlay-backdrop` | ink 92% | ink 92% | Lightbox (white text 15.34:1 over white imagery) |

## Interaction, type and system
- A4 `link-underline-thickness` 1px, `-hover` 2px, `link-underline-offset` 0.2em.
- A5 `focus-ring-width` 3px, `focus-ring-offset` 3px.
- T1 label tracking resolved to 0.02em. T2 `tracking-h3` -0.02em and `tracking-h4` -0.015em.
- T3 `micro`, per-style weights and status tokens added to tokens.css.
- T4 sizes in rem and line heights unitless (`$extensions.designPx` keeps the px design values).
- T5 `weight-wordmark` → semibold.
- S1 `motion-duration-fast` 120ms, `motion-duration-base` 200ms, `motion-ease`. S2 `control-height-sm|md|lg` 32/44/52px and `control-min-target` 44px. S3 `shadow-none`. S4 dark theme follows `prefers-color-scheme` unless `data-theme="light"`.

## Not applied (optional, no failure)
O1 renaming role-named primitives to ramps · O2 tertiary headroom tweak · O3 snapping the dark accent to cobalt-300. Ask if you want any of them.
