# Tabs

Switches between sibling views inside one page section. Underline tabs sit on a hairline, like a table of contents. The segmented control is reserved for showing the same content a different way (grid, list or timeline).

## Anatomy
1. **Tablist**: `role="tablist"` with `aria-label`, plus a 1px `color-border-default` baseline.
2. **Tab**: `<button role="tab">`, `type-body-sm` at 500, `space-3` padding x, `radius-sm` top corners.
3. **Count** (optional): metadata label, tertiary, tabular (`04`).
4. **Indicator**: a 2px `color-selected-indicator` rule on the baseline.
5. **Panel**: `role="tabpanel"`, labelled by its tab, `space-5` above.

## Variants
| Variant | Class | Use |
|---|---|---|
| Underline | default | Different content per tab (Overview, Process, Outcomes). |
| Segmented | `pm-tabs--segmented` | Same content, different arrangement. Tonal track (`color-bg-surface`, `radius-md`, `space-1` inset) with an elevated selected segment (`radius-sm`, 1px `color-border-control`). The radii nest: 8 = 4 + 4. |

## Sizes
md: `control-height-md` (40, 44 on touch). `pm-tabs--sm`: `control-height-sm`, `type-label`, `space-2` padding. Segmented items are the track height minus 2 × `space-1`.

## States
| State | Underline | Segmented |
|---|---|---|
| Default | `color-text-secondary` | `color-text-secondary` |
| Hover | `color-text-primary` + 2px `color-border-default` rule | `color-text-primary` |
| Focus-visible | 3px ring, inset | 3px ring, inset |
| Active | `color-bg-surface` | same |
| Selected | `aria-selected="true"`, `color-text-primary`, cobalt rule | elevated fill + 1px `color-border-control` (3.33:1 on the track) |
| Disabled | `aria-disabled="true"`, `color-disabled-text`, skipped by arrow keys | same |
| Error | n/a | n/a |

## Themes
The cobalt rule is 4.95 / 6.88:1 on canvas. The segmented edge uses `color-border-control`, so the selected segment holds 3:1 in both themes.

## Responsive behavior
The tablist scrolls horizontally (scrollbar hidden) and never wraps to two lines. Prefer five or fewer tabs. More than that is navigation, not tabs.

## Accessibility
- WAI-ARIA tabs pattern with roving tabindex: Tab enters the selected tab. ←/→ move and select (automatic activation), and Home/End jump to the ends.
- Each panel is `tabindex="0"` so its content is reachable, and hidden panels use `hidden`.
- Don't use tabs for page navigation (that's TopNavigation, or InPageNavigation with links).

## Token dependencies
`color-text-primary|secondary|tertiary` `color-border-default|subtle|control` `color-selected-indicator` `color-bg-surface|elevated` `color-disabled-text` `color-focus-ring` · `control-height-sm|md` · `space-1|2|3|5` · `radius-sm|md` · `type-body-sm|label|caption` · `font-meta` · `weight-medium`
