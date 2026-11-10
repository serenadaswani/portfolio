# TopNavigation

The site header: wordmark, primary destinations and global actions. It's quiet by design. The current page is marked by one precise cue, a 2px cobalt rule sitting on the header hairline, rather than a filled tab.

## Anatomy
1. **Header**: `<header class="pm-topnav">`, canvas, 1px `color-border-default` bottom hairline.
2. **Bar**: 56px, `content-max-width`. Items stretch to the full bar height, so the indicator lands exactly on the hairline.
3. **Wordmark**: text, `weight-semibold`, `tracking-heading`.
4. **Nav**: `<nav aria-label="Primary">` with a `<ul>`.
5. **Item**: `type-body-sm` at 500, `space-3` padding x, full bar height.
6. **Actions**: ghost icon button (theme) and secondary sm button (Résumé). Action buttons align to the bar centre, while items align to its baseline edge.
7. **Menu button** (narrow): ghost icon with `aria-expanded` and `aria-controls`.

## Variants
**Floating** (`pm-topnav--floating`, v1.7): the landing-page header. A centred bar sized to its content floats `space-3` below the top edge. It's sticky, with a 1px `color-border-subtle` ring and `shadow-xs`, and adding `is-scrolled` (set by script once the page scrolls) deepens it to `shadow-md`. Its parts: brand · separator · items · separator · theme toggle. Items are 32px (44px on touch), `radius-sm`, hover `color-bg-surface`. **No current-page indicator**: on a one-page site every item is an anchor. Keyboard focus is unchanged (inset ring). Below 768px the brand hides and the items stay inline, with no menu. `pm-topnav--bare` removes the fill, ring, shadow and separators for a links-only header. The bar keeps `radius-md` (8px) for consistency with every other container.


Default · `pm-topnav--sticky` (long pages; stays on canvas, no blur or translucency) · `pm-topnav--compact` (48px bar, when a Tabs row sits directly below).

## Sizes
Bar 56px (compact 48). Item hit area = bar height × (label + 24px). Gutters `space-4` narrow and `space-6` at ≥768px container.

## States
| State | Treatment |
|---|---|
| Default | `color-text-secondary` |
| Hover | `color-text-primary`. Text only; no fill and no bar, to keep the header calm. |
| Focus-visible | 3px ring drawn inset (items are 4px apart) |
| Active | `color-bg-surface` |
| Selected | `aria-current="page"` + `color-text-primary` + 2px `color-selected-indicator` rule on the hairline |
| Disabled / error | n/a: unavailable destinations aren't shown |

## Themes
The rule is 4.95:1 (light) and 6.88:1 (dark) against canvas. Secondary to primary text is the supporting cue in both themes.

## Responsive behavior
Below a 768px container, the list moves behind the menu button and opens as a full-width stack under a hairline. The active item's rule moves to a 2px left tick. Résumé folds into the list.

## Accessibility
- One `<nav aria-label="Primary">`, with `aria-current="page"` on the active item.
- Menu: `aria-expanded` and `aria-controls`. Opening moves focus to the first item, and Esc closes and returns focus. It isn't modal, so there's no focus trap.
- Contrast: items 7.66 / 10.46:1, active 17.92 / 15.98:1, rule 4.95 / 6.88:1.

## Token dependencies
`color-bg-canvas` `color-bg-surface` `color-border-default` `color-border-subtle` `color-text-primary|secondary` `color-selected-indicator` `color-focus-ring` · `content-max-width` · `control-height-md` · `space-1|2|3|4|6` · `radius-sm` · `type-body-sm` `type-body-md` · `weight-medium` `weight-semibold` · `tracking-heading`
