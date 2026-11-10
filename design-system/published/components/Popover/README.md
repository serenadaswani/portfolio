# Popover

A small non-modal panel anchored to its trigger, used for a short task or a closer look (share link, filter options, a definition with an action). It takes `shadow-md`, a soft, layered, Midnight-tinted shadow, because it really does sit above the page.

## Anatomy
1. **Anchor**: `.pm-popover-anchor` wraps the trigger and the panel.
2. **Trigger**: a Button with `aria-haspopup="dialog"`, `aria-expanded` and `aria-controls`.
3. **Panel**: `role="dialog"` + `aria-labelledby`, `color-bg-elevated`, 1px `color-border-subtle`, `radius-md`, `shadow-md`, `space-4` padding, max 320px.
4. **Title**: `type-body-sm` at 500. **Body**: `type-body-sm`, secondary.
5. **Actions**: sm buttons, right-aligned, `space-4` above.

## Variants
Default (left-aligned to the trigger) · `pm-popover--end` (right-aligned, for triggers at the right edge). Use a Tooltip for a name and a Dialog for anything that blocks.

## Sizes
Width `min(320px, 100vw − space-8)`. Content decides the height. Keep it under about 40% of the viewport.

## States
Closed (`hidden`) → open. Focus moves into the panel on open and returns to the trigger on close. Controls inside follow their own states.

## Themes
Elevated paper or night-raised + hairline + `shadow-md` (deeper in dark). The shadow is there to separate the overlay from content of the same colour, not for decoration.

## Responsive behavior
Width is capped at the viewport minus `space-8`. Below 768px, if the content exceeds about 4 lines, use a Dialog instead.

## Accessibility
- Non-modal: no focus trap, so Tab can leave it. Esc closes and returns focus. Clicking outside closes.
- The trigger exposes `aria-expanded`. The panel is labelled by its title.
- Don't put the only route to essential content inside a popover.

## Token dependencies
`color-bg-elevated` `color-border-subtle` `color-text-primary|secondary` `color-focus-ring` · `shadow-md` · `space-1|2|3|4|8` · `radius-md` · `type-body-sm` · `weight-medium`
