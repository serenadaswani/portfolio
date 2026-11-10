# Input

Text input, textarea and select share one field anatomy. The control is the one place where a 3:1 border is mandatory, so inputs carry the system's strongest resting edge. Labels are bold and readable rather than tiny, and nothing floats.

## Anatomy
1. **Field**: `.pm-field`, a vertical stack with a `space-2` gap.
2. **Label**: a `<label for>`, `type-body-sm` at 500, primary. Always visible: no placeholder-as-label, no floating labels.
3. **Optional marker**: "Optional" in tertiary. Mark the exception, not every required field.
4. **Counter** (textarea): metadata label, right of the label, `aria-hidden` (the limit is enforced by `maxlength`).
5. **Control**: `.pm-input` on `color-bg-elevated`, 1px `color-border-control`, `radius-sm`, `space-3` padding x.
6. **Prefix** (optional): `.pm-input-group__addon`, metadata label on a tonal cell ("https://").
7. **Select**: native `<select>` + a 16px chevron.
8. **Hint**: `type-label`, secondary, below the control (`aria-describedby`).
9. **Error**: `type-label` at 500, `color-state-error`, octagon icon + "Error:" + a fix ("enter a full email address").

## Variants
Text (`input`) · multiline (`textarea`, min 112px, resizes vertically) · select · with prefix · search.

## Sizes
md `control-height-md` (40, 44 on touch), text `type-body-sm`. Under `pointer: coarse` the text becomes `type-body-md`, which also prevents iOS zoom-on-focus. sm (`pm-input--sm`) `control-height-sm` for filters and search.

## States
| State | Treatment |
|---|---|
| Default | `color-border-control` (3.03–3.77:1) |
| Hover | border → `color-text-secondary` |
| Focus | border + 1px spread in `color-focus-ring`: a crisp 2px edge, no offset glow |
| Error | `aria-invalid="true"`, `color-state-error` border (2px on focus) + message |
| Disabled | `color-disabled-bg`, `color-disabled-text`, `color-disabled-border` |
| Read-only | `color-bg-surface`, `color-border-default`. Selectable, not editable. |
| Selected / active | n/a |

## Themes
Dark: night-raised field, `dark-border-strong` edge (3.03:1 on elevated), `dark-accent-hover` focus. Placeholder is tertiary in both themes (≥4.67:1).

## Responsive behavior
Fields are fluid (100% of their column). Composed forms cap at about 520px wide. Below 768px, actions can switch to `pm-btn--block-mobile`.

## Accessibility
- Every control has a `<label for>`. The hint and error are joined with `aria-describedby`.
- Errors: `aria-invalid`, text that says how to fix the problem, an icon shape, and focus moved to the first invalid field on submit.
- Use `autocomplete` tokens (`name`, `email`) for faster entry.
- Don't disable submit to signal errors. Validate on submit and explain.

## Token dependencies
`color-bg-elevated|surface` `color-border-control|default` `color-text-primary|secondary|tertiary` `color-state-error` `color-focus-ring` `color-disabled-bg|text|border` · `control-height-sm|md` · `space-1|2|3|5` · `radius-sm` · `type-body-sm|body-md|label|caption` · `font-meta` · `weight-medium`
