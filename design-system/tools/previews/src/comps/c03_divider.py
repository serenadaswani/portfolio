from lib import I, cell, h
NAME = 'Divider'; GROUP = 'Containers'; HEIGHT = 1000
SUB = 'Horizontal rules in three strengths and three spacings, labelled dividers, and vertical separators.'

BODY = (h('Strength') +
        '<div style="max-width:680px">' +
        '<p class="pm-spec__cap" style="margin:0">subtle (default) · decorative</p><hr class="pm-divider pm-divider--sm">' +
        '<p class="pm-spec__cap" style="margin:0">default · decorative</p><hr class="pm-divider pm-divider--default pm-divider--sm">' +
        '<p class="pm-spec__cap" style="margin:0">strong · ≥3:1, can carry meaning</p><hr class="pm-divider pm-divider--strong pm-divider--sm"></div>' +
        h('Spacing') + '<div style="max-width:680px;background:var(--color-bg-surface);border-radius:var(--radius-md);padding:0 var(--space-4)">' +
        '<p class="pm-spec__cap" style="margin:0;padding-top:var(--space-2)">sm · space-4</p><hr class="pm-divider pm-divider--default pm-divider--sm">'
        '<p class="pm-spec__cap" style="margin:0">md · space-8</p><hr class="pm-divider pm-divider--default">'
        '<p class="pm-spec__cap" style="margin:0">lg · space-12 → space-16 at ≥768px container</p><hr class="pm-divider pm-divider--default pm-divider--lg" style="margin-bottom:var(--space-2)"><span class="pm-spec__cap">↑ between case-study chapters</span><div style="height:var(--space-2)"></div></div>' +
        h('Labelled') + '<div style="max-width:680px">' +
        '<h3 class="pm-divider-label">2023</h3>' +
        '<h3 class="pm-divider-label pm-divider-label--center">Earlier work · 2019–2022</h3></div>' +
        h('Vertical · in toolbars') +
        f'<div style="display:flex;align-items:center" role="toolbar" aria-label="Image tools"><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-label="Copy link">{I["copy"]}</button><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-label="Download">{I["download"]}</button>'
        '<span class="pm-divider pm-divider--vertical" role="separator" aria-orientation="vertical"></span>'
        f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-label="Full screen">{I["full"]}</button></div>')
PAIRS = [('subtle', '--color-border-subtle', '--color-bg-canvas', 0), ('default', '--color-border-default', '--color-bg-canvas', 0),
         ('strong/canvas', '--color-border-strong', '--color-bg-canvas', 3), ('strong/surface', '--color-border-strong', '--color-bg-surface', 3),
         ('label', '--color-text-tertiary', '--color-bg-canvas', 4.5)]
SCRIPT = 'pmCheck();'
README = r'''
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
| Labelled | `pm-divider-label` (left-aligned; `--center` for centred) | label 4.67:1+ | Timeline years, archive splits. Mono caption, sentence case, no uppercase. |
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
`color-border-subtle` `color-border-default` `color-border-strong` `color-text-tertiary` · `space-1|2|3|4|8|12|16` · `type-caption` · `font-mono`
'''
