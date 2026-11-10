# SideNavigation

A vertical list for moving between sibling pages. Rows are compact (32px with a pointer). The current page reads through type, with primary colour and weight 500, plus a short cobalt tick. Nothing is filled.

## Anatomy
1. **Nav**: `<nav class="pm-sidenav" aria-label="Projects">`.
2. **Toggle** (<1024px): secondary button naming the current page.
3. **Heading**: `type-caption` at 500, `color-text-tertiary`, sentence case. It names the list.
4. **Item**: `type-body-sm` at 400, `color-text-secondary`, `radius-sm`, `space-3` padding x.
5. **Count / meta**: metadata voice (`font-meta`, 13px regular), tertiary, tabular figures, right-aligned.
6. **Group**: `<button aria-expanded>` + a nested list on a 1px `color-border-subtle` rail.
7. **Tick**: 2px × (row − 16px) `color-selected-indicator`, inset at the left edge.

## Variants
Flat · grouped (one level) · with meta.

## Sizes
Rows `control-height-sm` 32px (44px under `pointer: coarse`), 1px apart. Groups of lists are separated by `space-6`. Column width is 3 of 12 columns.

## States
| State | Treatment |
|---|---|
| Default | `color-text-secondary`, weight 400 |
| Hover | `color-bg-surface` + `color-text-primary` |
| Focus-visible | 3px ring, inset |
| Active | `color-bg-sunken` |
| Selected | `aria-current="page"` + `color-text-primary` + weight 500 + cobalt tick |
| Expanded | chevron rotates; `aria-expanded` |
| Disabled | `<span aria-disabled="true">`, `color-disabled-text`, with the reason in meta |
| Error | n/a |

## Themes
The tick is 4.95:1 (light) and 6.88:1 (dark) on canvas. The weight and text-colour shift carries selection in greyscale.

## Responsive behavior
≥1024px container: sticky beside the content. Below that: a full-width toggle that opens the list on an elevated panel with a 1px border. Esc closes it.

## Accessibility
Specific `aria-label` · `aria-current="page"` · groups use `aria-expanded` + `aria-controls` · disabled entries aren't focusable and are explained in text · the toggle names the current location.

## Token dependencies
`color-text-primary|secondary|tertiary` `color-bg-surface|sunken|elevated` `color-border-subtle|default` `color-selected-indicator` `color-disabled-text` `color-focus-ring` · `control-height-sm` `control-min-target` · `space-1|2|3|6` · `radius-sm|md` · `type-body-sm` `type-caption` · `font-meta` · `weight-regular|medium`
