# StatusIndicator

Shows the state of a project or process with a shape icon and a word ("Shipped", "In progress"). Colour adds speed, but the shape and the word carry the meaning.

## Anatomy
1. **Container**: `<span class="pm-status pm-status--{tone}">`.
2. **Icon**: a 14px Lucide outline icon, `aria-hidden`, a different shape per status (see below), centred on the first text line.
3. **Label**: `weight-medium`, `color-text-primary` (error labels use `color-state-error`).
4. **Description** (optional): `color-text-secondary`, on a second line.
5. **Message form**: `.pm-status-message--{tone}`, a tinted full-width row with "Word:" + sentence.

## Variants
| Tone | Shape | Example |
|---|---|---|
| success | `circle-check` | Shipped |
| progress | `circle-dot` | In progress |
| neutral | `circle-dashed` | Concept, Archived |
| info | `info` | Pilot, Note |
| warning | `triangle-alert` | Under NDA |
| error | `octagon-x` | Discontinued, Error |

## Sizes
| Size | Icon | Text |
|---|---|---|
| `pm-status--sm` | 12px | `type-caption` |
| md (default) | 14px | `type-body-sm` |
The icon is centred on the first line (margin-top = (line-height × size − icon) / 2), so it stays aligned when the text wraps.

## States
Static. Indicators don't take hover, focus or selected states. Status changes are content updates, announced through a live region (below).

## Themes
Icons ≥5.29:1 (light) and ≥6.49:1 (dark) on every surface, well above the 3:1 needed for graphics. Message fills use the `-bg` state tokens with `color-text-primary` text (≥16.37 / 10.95:1).

## Responsive behavior
None. The description wraps under the label, and messages stretch to their container.

## Accessibility
- Never colour alone: the shape and the word identify the status, which also covers colour-blind and greyscale viewing.
- Lead messages with a word ("Error:", "Sent.") so they're understood when read out of context.
- Live updates: wrap in `role="status"` (polite) for success and info, and `role="alert"` only for errors that block the person. The region must exist before its text changes.
- Form errors: put the message next to the field, link it with `aria-describedby`, and set `aria-invalid="true"` on the field.

## Token dependencies
`color-state-success|warning|error|info` and `-bg` · `color-text-primary` `color-text-secondary` `color-text-tertiary` `space-1|2|3|4` · `radius-md` · `type-body-sm` `type-caption` · `weight-medium`
