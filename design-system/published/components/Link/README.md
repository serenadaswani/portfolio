# Link

Links go somewhere: another page, a section, a file or an external site. A link is just its text, in the link colour at weight 500. If the element does something on the current page, it's a Button.

## Anatomy
1. **Anchor**: `<a href>`.
2. **Text**: says where it goes ("the evaluation write-up", not "here"). `color-text-link`, `weight-medium`.
3. **Underline** (hover and focus only): 1px at 0.2em on hover. On focus it's 2px in `color-focus-ring`.
4. **Focus tint**: a `color-action-selected-bg` wash with a 2px spread, replacing the outline.
5. **Icon** (standalone/external): arrow → or external ↗, `aria-hidden`.
6. **Hidden text** (external): `<span class="pm-sr"> (opens in a new tab)</span>`.

## Variants
| Variant | Class | Use |
|---|---|---|
| Inline | `pm-link` | Inside paragraphs, lists, captions. Text only, weight 500. |
| Standalone | `pm-link--standalone` | Alone on a line ("Read case study →"). Adds the arrow and a `control-min-target` height. |
| Subtle | `pm-link--subtle` | Footers, metadata, colophon. `color-text-secondary` at weight 400 with a quiet 1px `color-border-strong` underline (its non-colour cue), which turns `currentColor` on hover. |
| External | ↗ icon + hidden text | Off-site destinations. |
| On image | `pm-link--on-image` | Only over `color-overlay-scrim`. |

## Sizes
Links inherit the size of their text. Standalone links keep a `control-min-target` height (24px pointer, 44px touch).

## States
| State | Treatment |
|---|---|
| Default | `color-text-link`, weight 500, no underline |
| Hover | `color-text-link-hover` + 1px underline |
| Focus-visible | **No outline.** 2px `color-focus-ring` underline + `color-action-selected-bg` tint |
| Active | `color-action-pressed` |
| Visited | `color-text-link-visited` (= default: one accent, no purple) |
| Selected | `aria-current="page"`: `color-text-primary` + 2px `color-selected-indicator` underline |
| Disabled | Links can't be disabled. Use plain text with `pm-link-unavailable` and a reason ("Under NDA"). |
| Error | n/a |

## Themes
Light: `cobalt-600` (5.65–7.02:1 on every surface), hover `cobalt-700`. Dark: `dark-accent` (5.68–7.45:1), hover `dark-accent-hover`. The focus line on its tint is 6.27:1 (light) and 6.12:1 (dark).

## Responsive behavior
None. Standalone links wrap. Inline icons are bound to the last word with `<span class="pm-nowrap">`, so an icon never wraps onto a line by itself.

## Accessibility
- **The non-colour cue is weight.** Body text is 400 and links are 500, plus an underline on hover and focus. That keeps WCAG 1.4.1 met without an underline at rest: the dark link is only 2.32:1 against body text, so colour alone wouldn't be enough. Don't set links in prose at weight 400, and don't put them inside text that's already 500.
- **Focus without an outline still meets 2.4.7**: the 2px focus-colour line plus the tint is a clearly visible indicator, at ≥6.12:1. Don't remove both.
- Link text must make sense out of context. Never "click here" alone.
- External: say "(opens in a new tab)" in hidden text, and use `rel="noopener"`.
- Keyboard: Tab to focus, Enter to follow.

## Token dependencies
`color-text-link` `color-text-link-hover` `color-text-link-visited` `color-action-pressed` `color-action-selected-bg` `color-focus-ring` `color-text-primary` `color-text-secondary` `color-text-on-image` `color-selected-indicator` `color-disabled-text` `color-overlay-scrim` · `weight-medium` `weight-regular` · `link-underline-thickness` `link-underline-thickness-hover` `link-underline-offset` · `control-min-target` · `space-1`
