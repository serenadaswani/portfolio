# InPageNavigation

An "On this page" index for long case studies. Mono numbers on a hairline rail give it a technical, editorial index feel without adding decoration.

## Anatomy
1. **Nav**: `<nav class="pm-toc" aria-labelledby>`.
2. **Heading**: "On this page", caption at 500, tertiary, sentence case.
3. **List**: `<ol>` on a 1px `color-border-default` rail.
4. **Item**: mono number (`01`, tertiary, tabular) + title (`type-body-sm`), baseline-aligned with a `space-3` gap.
5. **Indicator**: a 2px cobalt segment over the rail.

## Variants
Numbered (default) · plain (omit `pm-toc__num`). Vertical rail or horizontal strip is chosen by container width.

## Sizes
Vertical rows `control-height-sm` 32px (44 on touch). Strip items `control-height-md`.

## States
Default `color-text-secondary` · hover `color-text-primary` + `color-border-strong` rail segment · focus inset ring · active `color-bg-surface` · selected `aria-current="location"` + primary text + weight 500 + cobalt segment · disabled and error n/a.

## Themes
The segment is 4.95:1 and 6.88:1 on canvas. The numbers stay tertiary (5.55 / 7.86:1) in both themes.

## Responsive behavior
≥1024px container: sticky rail in a 3-column aside. Below: a horizontal strip with its scrollbar hidden. The current item scrolls into view.

## Accessibility
Links to real ids (works without JS) · `aria-current="location"` · focus moves to the target section after a jump · smooth scrolling only without reduced motion · not a tablist.

## Token dependencies
`color-text-primary|secondary|tertiary` `color-border-default|strong` `color-selected-indicator` `color-bg-surface` `color-focus-ring` · `control-height-sm|md` · `space-1|3|4` · `radius-sm` · `type-body-sm` `type-caption` · `font-mono` · `weight-medium`
