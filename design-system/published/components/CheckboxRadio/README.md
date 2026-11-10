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
