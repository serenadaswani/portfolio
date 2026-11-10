from lib import S, cell, h
NAME = 'CheckboxRadio'; GROUP = 'Forms'; HEIGHT = 1000
SUB = 'Native checkbox and radio tinted with cobalt, aligned to the first text line, grouped in a fieldset.'

def ch(t, i, label, desc=None, checked=False, disabled=False, name=None):
    d = f'<span class="pm-choice__desc">{desc}</span>' if desc else ''
    nm = f' name="{name}"' if name else ''
    return f'<label class="pm-choice"><input type="{t}"{nm}{" checked" if checked else ""}{" disabled" if disabled else ""}><span>{label}</span>{d}</label>'

BODY = (h('Checkbox') + '<div class="pm-spec__row" style="gap:var(--space-6) var(--space-10)">' +
        cell(ch('checkbox', 0, 'Send a copy to me'), 'default') + cell(ch('checkbox', 0, 'Send a copy to me', checked=True), 'checked') +
        cell(ch('checkbox', 0, 'Send a copy to me', disabled=True), 'disabled') + cell(ch('checkbox', 0, 'Send a copy to me', checked=True, disabled=True), 'checked · disabled') + '</div>' +
        h('Radio group · fieldset + legend') +
        '<fieldset class="pm-field" style="max-width:420px"><legend class="pm-field__label">Reason for reaching out</legend><div class="pm-choice-group">' +
        ch('radio', 0, 'Hiring', 'Full-time or contract roles.', True, name='r-{T}') + ch('radio', 1, 'Collaboration', 'Research, writing or talks.', name='r-{T}') +
        ch('radio', 2, 'Something else', name='r-{T}') + ch('radio', 3, 'Mentoring', 'Not available this quarter.', disabled=True, name='r-{T}') + '</div></fieldset>' +
        h('Group error') +
        '<fieldset class="pm-field" style="max-width:420px" aria-describedby="ce-{T}"><legend class="pm-field__label">Consent</legend>' +
        ch('checkbox', 0, 'I agree to be contacted about this request') +
        f'<p class="pm-field__error" id="ce-{{T}}" style="margin-top:var(--space-1)">{S["error"]}<span>Error: tick the box so I can reply.</span></p></fieldset>')
PAIRS = [('label', '--color-text-primary', '--color-bg-canvas', 4.5), ('description', '--color-text-secondary', '--color-bg-canvas', 4.5),
         ('checked fill', '--color-action-primary', '--color-bg-canvas', 3), ('error', '--color-state-error', '--color-bg-canvas', 4.5)]
SCRIPT = 'pmCheck();'
README = r'''
# CheckboxRadio

Native checkboxes and radios, tinted with the accent through `accent-color`. Native controls keep platform accessibility (forced colours, zoom, screen readers) for free. The system only sets their size, colour and alignment.

## Anatomy
1. **Row**: `<label class="pm-choice">`, a two-column grid (16px control, then text) with a `space-3` gap.
2. **Control**: native `<input type="checkbox|radio">`, 16px, vertically centred on the **first** text line (`1lh`), so it stays aligned when the label wraps.
3. **Label**: `type-body-sm`, primary.
4. **Description** (optional): `type-label`, secondary, aligned to the label column.
5. **Group**: `<fieldset class="pm-field">` + `<legend class="pm-field__label">`, rows `space-3` apart.
6. **Error**: the Input error pattern, linked to the fieldset with `aria-describedby`.

## Variants
Checkbox (independent options) · radio (one of many, always in a group). No custom toggles or switches until a real need appears.

## Sizes
One size: 16px control. Under `pointer: coarse`, each row is at least `control-min-target` tall, and the whole label is the hit area.

## States
| State | Treatment |
|---|---|
| Default | native border |
| Hover / active | native |
| Focus-visible | system 3px `color-focus-ring` at 3px offset |
| Checked | `color-action-primary` fill (4.95 / 6.88:1 on canvas) |
| Disabled | `color-disabled-text` on the label and description; native dimmed control |
| Error | message under the group, "Error:" + fix |

## Themes
`color-scheme` follows the theme, so native controls render dark in dark mode, with a `dark-accent` fill.

## Responsive behavior
None. Groups stay vertical. Horizontal radio rows are only for 2–3 short options at ≥768px.

## Accessibility
Native semantics · clicking the label toggles the control · `fieldset`/`legend` name the group · arrow keys move within a radio group (native) · error text is linked to the group.

## Token dependencies
`color-action-primary` `color-text-primary|secondary` `color-disabled-text` `color-state-error` `color-focus-ring` · `control-min-target` · `space-1|3|6` · `type-body-sm|label` · `weight-medium`
'''
