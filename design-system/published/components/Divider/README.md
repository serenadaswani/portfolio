# Divider

A rule that separates content when space alone isn't enough. Use it sparingly: proximity and surface changes group content first, and a divider is the last resort.

## Anatomy
1. **Rule**: `<hr class="pm-divider">`, 1px top border.
2. **Label** (optional): `.pm-divider-label`, a heading or text flanked by rules (`::before`/`::after`).
3. **Vertical separator**: `<span role="separator" aria-orientation="vertical">` inside toolbars. Toolbars keep a `space-1` gap and draw focus rings inset.

## Variants
| Variant | Class | Contrast | Use |
|---|---|---|---|
| Subtle | default | 1.00–1.55:1 · decorative | Between list rows, inside panels. |
| Default | `pm-divider--default` | 1.29–2.11:1 · decorative | Between page sections, panel footers. |
| Strong | `pm-divider--strong` | 3.03–3.98:1 | When the rule itself means something (end of a table, a hard boundary). |
| Labelled | `pm-divider-label` (left-aligned; `--center` for centred) | label 4.67:1+ | Timeline years, archive splits. Metadata label, sentence case, no uppercase. |
| Vertical | `pm-divider--vertical` | default | Grouping buttons in a toolbar. |

## Sizes
Vertical margin: `pm-divider--sm` `space-4` · default `space-8` · `pm-divider--lg` `space-12`, then `space-16` at ≥768px container · `pm-divider--flush` 0. Vertical separator: min height 24px, `space-2` side margin.

## States
None. Dividers aren't interactive.

## Themes
Subtle `mist` / `dark-border-subtle`, default `silver` / `dark-border-default`, strong `light-border-strong` / `dark-border-strong`.

## Responsive behavior
Only `pm-divider--lg` changes (`space-12` → `space-16`). Labelled dividers keep their rules; the label wraps.

## Accessibility
- `<hr>` is a thematic break and is announced as a separator. If a rule is purely visual, use a CSS border on the container instead of an `<hr>`, so screen readers aren't told "separator" repeatedly.
- A labelled divider that starts a section should be a real heading (`<h3 class="pm-divider-label">`) so it appears in the heading outline.
- Vertical separators in a `role="toolbar"` use `role="separator" aria-orientation="vertical"`.
- Decorative strengths must never be the only cue for a boundary that matters. Use Strong, or a surface change.

## Token dependencies
`color-border-subtle` `color-border-default` `color-border-strong` `color-text-tertiary` · `space-1|2|3|4|8|12|16` · `type-caption` · `font-meta`
