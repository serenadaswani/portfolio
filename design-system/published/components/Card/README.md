# Card

The project card. By default it's frameless: an image well with a hairline edge, then type. Hierarchy comes from typography and alignment, not from a filled container, and the work itself is the figure.

## Anatomy
1. **Card**: `<article class="pm-card">`, no fill, `radius-md` (used only for the focus ring's shape).
2. **Image well**: `.pm-media.pm-card__media`, 16:10, `radius-md`, 1px `color-border-subtle` edge. `color-bg-sunken` shows while loading.
3. **Eyebrow**: Geist Mono caption, tertiary, year first ("2024 · AI tooling"). It's metadata, so it's set as metadata.
4. **Title**: `<h3>` + stretched link, `type-h4` at 500, `tracking-h4`, balanced wrapping.
5. **Summary**: `type-body-sm`, `color-text-secondary`, max 48ch.
6. **Tags**: Badges, 1px outline, `space-1` apart.

Rhythm: well → `space-4` → eyebrow → `space-1` → title → `space-2` → summary → `space-4` → tags. Tight inside each group, more space between groups.

Removed in v1.3: the surface fill and the "Read case study →" line (the whole card is the link, so the line added nothing).

## Variants
| Variant | Class | Use |
|---|---|---|
| **Tile** (v1.7) | `pm-card--tile` | **Default for selected work.** No outline. The artwork sits on a `color-bg-surface` stage (`radius-md`) and rises flush from its bottom edge: the stage is padded `space-12` top and `space-8` sides (`space-8`/`space-5` below 768px), and the full 16:10 screenshot gets top-only `radius-sm` and `shadow-md`, never cropped. Below it are the title (`type-body-lg` at 500) with a mono year on the same baseline, then one "Discipline · Area" line. Hover covers the whole card: the stage goes to `color-bg-sunken`, the artwork lifts `space-2` (no lift with reduced motion), and a ↗ chip appears. Focus shows the card ring and the chip. Lay tiles out in `pm-work-grid`: two columns from 768px, with the right column offset `space-24`. |
| Frameless | default | Work grids, the main index. |
| Outlined | `pm-card--outlined` | Dense grids and related lists. Elevated paper, 1px `color-border-subtle` ring + `shadow-xs`, image flush to the frame with a hairline under it. |
| Compact | `+ pm-card--compact` | Next and related project, no image: `space-3`/`space-4` padding, `body-md` title. |
| Featured | `pm-card--featured` | One lead project: 16:9, `type-h3` title, `body-md` summary. |
| Horizontal | `pm-card--horizontal` | At ≥768px container: image 7/12, text 5/12. Deliberately asymmetric. |
| Locked | `pm-card--locked` | NDA work: no link, lock fallback, warning badge. |

## Sizes
One size. Width comes from the grid (each card spans 4 columns). Grid gaps are `space-6` horizontal and `space-10` vertical: rows need more air than columns, because the eye reads down a card.

## States
| State | Frameless | Outlined |
|---|---|---|
| Hover | well edge → `color-border-default` + soft `shadow-sm`; title underlines | ring → `color-border-default`, `shadow-xs` → `shadow-sm` |
| Focus-visible | 3px ring around the card (via `:has()`) | same |
| Active | title → `color-text-secondary` | `color-bg-surface` |
| Selected | `aria-current` → 2px cobalt ring on the well | same |
| Disabled | Use Locked: unavailable work is explained, not dimmed | same |
| Error | well fallback + "Image unavailable"; text is unaffected | same |

## Themes
In dark, the well edge is `dark-border-subtle`, hover `dark-border-strong` (3.67:1). The text colours hold hierarchy the same way in both themes: title 15.98:1, summary 10.46:1, eyebrow 7.86:1 on midnight.

## Responsive behavior
The grid goes 1 → 2 → 3 per row, and Horizontal stacks below 768px. Titles wrap with `text-wrap: balance` and never truncate.

## Accessibility
- One link per card (the title), stretched over the card, so there's one tab stop.
- Card images are `alt=""` when the title says it all.
- Heading level follows the outline. Don't nest other interactive controls inside a stretched card.
- Contrast: title ≥15.07:1, summary ≥6.45:1, eyebrow ≥4.67:1 on every light surface.

## Token dependencies
`color-text-primary|secondary|tertiary` `color-border-subtle|default|strong` `color-bg-elevated|surface|sunken` `color-selected-indicator` `color-focus-ring` · `shadow-xs|sm` · `space-1|2|3|4|5|6|8|10` · `radius-md` · `type-h4|h3|body-sm|body-md|caption` · `font-mono` · `weight-medium` · `tracking-h4|h3` · `link-underline-*` · Badge, ImageContainer
