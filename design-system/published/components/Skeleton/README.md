# Skeleton

A grey placeholder in the shape of the content that's loading. It holds layout steady (no shift when the content arrives) and signals that something is coming. Use it for loads over about 300ms. For quicker loads, show nothing.

## Anatomy
1. **Group**: `.pm-skeleton-group` with `aria-busy="true"` on the region being loaded.
2. **Shapes**: `.pm-skeleton--text | --text-md | --heading | --label | --media | --button`, all `aria-hidden`.
3. **Announcement**: a visually hidden `role="status"` "Loading projects…", replaced by "Projects loaded".
4. **Shimmer**: a `::after` gradient sweep, only when motion is allowed.

## Variants
- **Elements**: individual shapes, matched to the type token they stand in for. Text bars are the cap height of `type-body-sm`/`type-body-md`, with margins making up the token line height, so lines occupy exactly what the real text will.
- **Card composition** (`pm-skeleton-group--card`): mirrors the frameless Card (well, mono eyebrow line, title, two summary lines). No container fill.
- **Static**: under `prefers-reduced-motion: reduce`, no shimmer, just flat fills.

## Sizes
Taken from tokens: text bars follow `type-*` and `line-*`, heading = `type-h4`, media = the container ratio (`--pm-ratio`, default 16:10), button = `control-height-md`. Set widths to vary line lengths (60–95%), never full justification.

## States
Loading (shapes + `aria-busy="true"`) → loaded (content + `aria-busy="false"`). There are no interactive states. If loading fails, replace it with a StatusIndicator error message. Don't leave skeletons up indefinitely.

## Themes
Fill `color-bg-sunken`, shimmer `color-bg-surface` (`color-bg-elevated` inside cards). In dark, the sunken fill is ink on midnight (1.08:1), so skeletons are deliberately very quiet there. That's acceptable because they're decorative and paired with the status text.

## Responsive behavior
Compositions follow the real layout's grid (1 → 2 → 3). The media keeps its ratio, so height scales with width.

## Accessibility
- Shapes are `aria-hidden`. Announce loading once through a polite live region, then announce completion.
- `aria-busy="true"` on the updating region tells assistive tech to wait.
- Motion: the shimmer runs only in `prefers-reduced-motion: no-preference` (WCAG 2.3.3) and conveys no information.
- Don't make skeletons focusable, and don't put them in the tab order.

## Token dependencies
`color-bg-sunken` `color-bg-surface` `color-bg-elevated` · `type-body-sm` `type-body-md` `type-h4` `type-label` + lines · `control-height-md` · `space-2|3|4|6` · `radius-sm` `radius-md` `radius-lg` · `motion-ease`
