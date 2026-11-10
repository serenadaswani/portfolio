# Dialog

A modal for a short, focused task that has to be finished or dismissed before continuing (request access, confirm, a short form). It sits on the scrim with a hairline edge and `shadow-lg`, the system's deepest shadow.

## Anatomy
1. **Dialog**: native `<dialog class="pm-dialog">` opened with `showModal()`, `aria-labelledby` the title and `aria-describedby` the lead sentence.
2. **Backdrop**: `::backdrop` = `color-overlay-scrim`.
3. **Surface**: `color-bg-elevated`, 1px `color-border-subtle`, `radius-md`, `shadow-lg`.
4. **Header**: title (`type-h4` at 500, `tracking-h4`) + ghost sm close button, optically aligned to the title's first line and pulled `space-2` into the padding.
5. **Body**: `type-body-sm`, secondary, `space-5` padding. Can hold fields.
6. **Footer**: tonal `color-bg-surface` strip under a hairline. Secondary then primary, right-aligned.

## Variants
Default 440px · `pm-dialog--md` 560px (forms). No destructive variant until there's a destructive action in the product.

## Sizes
Width `min(440 | 560px, 100% − space-8)`, max height 100% − `space-8` (the body scrolls). Padding `space-5`, or `space-4` below 768px.

## States
Closed → open (fades over `motion-duration-base`; none with reduced motion) → closed. Inner controls follow their own states.

## Themes
Light: white on a 72% ink scrim. Dark: night-raised on the same scrim, with a deeper `shadow-lg`. Title and body keep the same hierarchy in both.

## Responsive behavior
Below 768px the dialog becomes a **sheet** (Apple HIG: modals on compact width present from the bottom edge). It's full width, anchored to the bottom, has top corners only, and fits to content up to 100% − `space-10`. It rises `space-6` over `motion-duration-base` (none with reduced motion). The footer stacks the actions full-width with the primary on top, and pads for the home indicator (`env(safe-area-inset-bottom)`). There's no grabber, because the sheet can't be dragged.

## Accessibility
- Native modal: background inert, Esc closes, focus is contained.
- On open, focus goes to the first field (or Close). On close, it **returns to the trigger**.
- The visible Close button has `aria-label="Close"`. Clicking the backdrop also closes, but there's always a visible way out.
- Don't stack dialogs. Keep dialog copy under about 3 sentences.

## Token dependencies
`color-bg-elevated|surface` `color-border-subtle` `color-overlay-scrim` `color-text-primary|secondary` `color-focus-ring` · `shadow-lg` · `space-2|3|4|5|8` · `radius-md` · `type-h4|body-sm` · `tracking-h4` · `weight-medium` · `motion-duration-base` `motion-ease` · Button, Input
