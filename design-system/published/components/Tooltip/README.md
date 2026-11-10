# Tooltip

A short text bubble that names an icon-only control or adds a one-line explanation. It appears on hover and keyboard focus. A tooltip never holds anything a person needs to complete a task.

## Anatomy
1. **Anchor**: `.pm-tooltip-anchor` wraps the trigger and the bubble (so the bubble is hoverable).
2. **Trigger**: a focusable control (button or link). Never a plain `span`.
3. **Bubble**: `<span role="tooltip" id>`, `color-bg-inverse` / `color-text-inverse`, `radius-sm`, `type-caption` at 500. There's no arrow: the `space-2` offset and inverse contrast make the link to the trigger clear, and an arrow is decoration.
4. **Shortcut** (optional): `<kbd>` in the metadata voice at 72% opacity ("⌘C").
5. **Hover bridge**: an invisible `::before` covering the gap, so moving the pointer onto the bubble doesn't close it.

## Variants
| Variant | Wiring | Use |
|---|---|---|
| Label | trigger `aria-labelledby="tip-id"` | Names an icon-only button (the tooltip is its accessible name). |
| Description | trigger `aria-describedby="tip-id"` | Supplementary detail for a control that already has a name. |
| Rich | `pm-tooltip--rich` | Title + one sentence, max 280px. No links or buttons inside (that would make it a popover). |
| Placement | default top · `--bottom` · `--end` | Pick the side with room. Flip near viewport edges. |

## Sizes
Label: `type-caption` at 500, padding `space-1` `space-2`, max 240px. Rich: `type-body-sm`, padding `space-2` `space-3`, max 280px. Both are capped at viewport minus `space-8`. Offset from the trigger: `space-2`.

## States
| State | Behaviour |
|---|---|
| Hidden | default |
| Shown | trigger `:hover` or `:focus-within`, fading in over `motion-duration-fast` (no fade with reduced motion) |
| Dismissed | Esc hides it without moving focus (WCAG 1.4.13). It resets on pointer leave or blur. |
| Persistent | Stays while the pointer is over the trigger or the bubble. No timeout. |
| Disabled trigger | Use `aria-disabled` (not `disabled`), so the tooltip can still explain why. |

## Themes
Inverse in both: ink on paper (17.92:1) in light, paper-white on midnight (17.30:1) in dark. The bubble is ≥14.58:1 against any surface, so it needs no border. A soft `shadow-sm` separates it from busy content below.

## Responsive behavior
No hover on touch: tooltips show on focus only. Every icon button keeps its name through `aria-labelledby`, so nothing is lost. Width is capped at the viewport. On narrow containers, prefer `--bottom` or `--end` placement so the bubble isn't clipped by the top bar.

## Accessibility
- WCAG 1.4.13: dismissible (Esc), hoverable (bridge), persistent (no timeout).
- Triggers must be focusable. Tooltips on non-interactive text aren't reachable by keyboard; use visible text instead.
- Only the label or the description, never both with the same text (avoid "Copy link, Copy link").
- No interactive content inside. If you need a link, use a popover or dialog.

## Token dependencies
`color-bg-inverse` `color-text-inverse` · `space-1|2|3|8` · `radius-sm` · `type-caption` `type-body-sm` · `font-meta` · `weight-regular` `weight-medium` · `motion-duration-fast` `motion-ease`
