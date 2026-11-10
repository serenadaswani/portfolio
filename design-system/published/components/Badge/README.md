# Badge

A small static label: a discipline tag, a version or year, "Featured", or a status. Shape and type tell them apart: a frosted tag for disciplines, meta for technical values, a tonal fill for status. All of them are square-cornered.

## Anatomy
1. **Container**: `<span>` or `<li>` (in a `<ul>` of tags), `radius-sm`, 24px tall.
2. **Glyph** (status only): a 12px Lucide icon (`circle-check`, `triangle-alert`, `octagon-x`, `info`), `aria-hidden`, centred on the text.
3. **Text**: `type-caption` (12px) at 500, sentence case, no tracking.

## Variants
| Variant | Class | Treatment | Use |
|---|---|---|---|
| Tag | default (`--outline` is an alias) | Frosted (v1.9): `color-badge-bg` (white at 55%; 6% in dark) + 1px `color-badge-border` (ink at 8%; white at 10% in dark), secondary text. No blur. | Disciplines on cards |
| Meta | `pm-badge--meta` | Metadata voice at 400, tabular | Years, versions, counts |
| Accent | `pm-badge--accent` | `color-action-selected-bg` / `-text` | One per view |
| Status | `--success` `--warning` `--error` `--info` | tonal state fill + glyph + word | Project or content status |

Pills were removed in v1.3. Status is distinguished by fill and glyph, not by a rounder shape. v1.9 replaced the tag's silver outline with the frosted fill so tags sit quietly on project washes; it stays flat (no backdrop blur).

## Sizes
md 24px with `space-2` padding · `pm-badge--sm` 20px with `space-1` padding.

## States
None. Badges aren't interactive. A clickable filter is a chip (not yet in the system).

## Themes
The tag fill is translucent, so it takes on the surface beneath it. Its text is secondary on any surface (≥6.45:1 light, ≥8.64:1 dark); the fill only lightens light surfaces and barely shifts dark ones. With `prefers-contrast: more` the edge becomes `color-border-default`. Status pairs are ≥5.75:1 (light) and ≥6.12:1 (dark).

## Responsive behavior
Rows wrap with a `space-1` gap. Badges never truncate.

## Accessibility
Plain text · status glyphs are decorative and the word carries the meaning · wrap live-changing badges in `role="status"`.

## Token dependencies
`color-badge-bg|border` `color-border-default` (high contrast) `color-text-secondary` `color-action-selected-bg|text` `color-state-*` and `-bg` · `space-1|2` · `radius-sm` · `type-caption` · `font-meta` · `weight-medium|regular`
