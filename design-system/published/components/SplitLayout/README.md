# Split layout

A two-column page for the portfolio home (v1.8), after Megan Yap and Dakota Sumner. The left column introduces you and holds the navigation, and it stays put. The right column scrolls through the work. It reads like a spec sheet beside a gallery: who, then what.

## Anatomy
1. **Split**: `.pm-split`, a grid. Put `.pm-cq` on its parent. ≥1024px container: `360px` + `minmax(0, 1fr)`.
2. **Aside**: `<aside class="pm-split__aside">`, a flex column with `space-6` gaps. At ≥1024px it's sticky, one viewport tall (`--pm-split-h`, default `100dvh`), with a `color-border-subtle` rule on its right edge and its own scroll if the window is short.
3. **Intro** `.pm-intro`: 40px mark (initials now, photo later), name as the page's `<h1 class="pm-intro__name">` (`type-h2` size, with the descriptor in a tertiary `<span>`), one line of text, a status with the live dot, and Copy email + Résumé (`pm-btn--sm`).
4. **Vertical nav**: the SideNavigation component with `.pm-split__nav`, pushed to the bottom of the aside (`margin-top: auto`). Links point to sections on the page.
5. **Foot** `.pm-split__foot`: social links (`pm-link--subtle`) and local time in the metadata voice, above a hairline.
6. **Main** `.pm-split__main`: the content column, and itself a container, so its contents respond to the column's width rather than the window's.
7. **Sections** `.pm-split__section` with a quiet `.pm-split__h` label (body-md, 500, secondary). `space-20` between sections.

## Variants
- **Showcase work** (default): `pm-showcase-grid` with Card `--showcase`. Strongest projects first, full width; supporting projects two-up.
- **Tile work**: `pm-work-grid pm-work-grid--even` with Card `--tile`, for a longer list.

## Sizes
Aside 360px. Main padding `space-12` top, `space-10` sides, `space-24` bottom at ≥1024px; `space-10`/`space-4` sides below.

## States
| State | Behaviour |
|---|---|
| Scroll-spy (current section) | `aria-current="location"` on the nav link: primary text, weight 500, 2px `color-selected-indicator` tick (left on desktop, underneath in the row). Use `location`, not `page`: every link is on this page. |
| Hover / focus / active | From SideNavigation: surface fill, 3px inset focus ring, sunken press. |
| Disabled / error | n/a: a layout. |

## Themes
Same structure in both. The aside sits on canvas with only a subtle rule, so the work column carries the colour.

## Responsive behavior
- **≥1024px:** two columns, sticky aside.
- **768–1023px and phones:** one column. Intro first, then the nav as a wrapping row of links (the tick moves under the label), then the foot, then the work. The aside scrolls away with the page.
- The showcase grid goes two-up only when the main column is ≥768px wide (roughly a 1200px window). Below that, every card is full width and lays itself out by its own width.
- Edge padding respects `safe-area-inset-*`.

## Accessibility
- Landmarks: `<aside aria-label="Introduction">`, `<nav aria-label="Sections">`, `<main class="pm-split__main">`. One `<h1>` (the name); section labels are `<h2>`, card titles `<h3>`.
- The sticky aside never traps focus, and the tab order matches the visual order (aside, then main).
- Scroll-spy updates `aria-current` only; it doesn't announce. Smooth scrolling is skipped under reduced motion.
- 44px nav targets under `pointer: coarse` (SideNavigation).

## Token dependencies
`color-bg-canvas|surface` `color-border-subtle` `color-text-primary|secondary|tertiary` `color-selected-indicator` `color-state-success` · `space-2|3|4|6|8|10|12|16|20|24` · `radius-sm` · `type-h2|body-md|body-sm|label` · `font-meta` · `tracking-heading` · `weight-medium`
