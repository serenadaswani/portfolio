from lib import S, cell, h
NAME = 'StatusIndicator'; GROUP = 'Feedback'; HEIGHT = 1100
SUB = 'Icon + label status for projects and processes: six shapes, inline or with description, sm/md, and message form.'

def ind(k, label, desc=None, size=''):
    d = f'<span class="pm-status__desc">{desc}</span>' if desc else ''
    return f'<span class="pm-status pm-status--{k}{size}">{S[k]}<span class="pm-status__text"><span class="pm-status__label">{label}</span>{d}</span></span>'

BODY = (h('Statuses · each a different shape') + '<div class="pm-spec__row">' +
        cell(ind('success', 'Shipped'), 'success') + cell(ind('progress', 'In progress'), 'progress') + cell(ind('neutral', 'Concept'), 'neutral') +
        cell(ind('info', 'Pilot'), 'info') + cell(ind('warning', 'Under NDA'), 'warning') + cell(ind('error', 'Discontinued'), 'error') + '</div>' +
        h('With description') + '<div class="pm-spec__row">' +
        cell(ind('success', 'Shipped', 'Live for 14 review teams since March'), 'success + desc') +
        cell(ind('progress', 'In progress', 'Phase 2 of 3: ranking rules'), 'progress + desc') + '</div>' +
        h('Sizes') + '<div class="pm-spec__row" style="align-items:center">' +
        cell(ind('success', 'Shipped', size=' pm-status--sm'), 'sm · 12px icon · caption') + cell(ind('success', 'Shipped'), 'md · 14px icon · body-sm') + '</div>' +
        h('Message form · live') +
        '<div style="display:grid;gap:var(--space-3);max-width:560px">' +
        f'<div class="pm-status-message pm-status-message--success" role="status"><span class="pm-status pm-status--success" style="display:contents">{S["success"]}</span><span><b style="font-weight:500">Sent.</b> I’ll reply within two working days.</span></div>' +
        f'<div class="pm-status-message pm-status-message--error" role="alert"><span class="pm-status pm-status--error" style="display:contents">{S["error"]}</span><span><b style="font-weight:500">Error:</b> enter an email address, like name@example.com.</span></div>' +
        f'<div class="pm-status-message pm-status-message--info" role="status" id="live-{{T}}"><span class="pm-status pm-status--info" style="display:contents">{S["info"]}</span><span><b style="font-weight:500">Note:</b> metrics are from the pilot.</span></div>' +
        '<div><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-live="live-{T}">Simulate update</button></div></div>')
PAIRS = [('label', '--color-text-primary', '--color-bg-canvas', 4.5), ('success icon', '--color-state-success', '--color-bg-canvas', 3),
         ('warning icon', '--color-state-warning', '--color-bg-canvas', 3), ('error icon', '--color-state-error', '--color-bg-canvas', 3),
         ('info icon', '--color-state-info', '--color-bg-canvas', 3), ('neutral icon', '--color-text-tertiary', '--color-bg-canvas', 3),
         ('error msg', '--color-text-primary', '--color-state-error-bg', 4.5)]
SCRIPT = r'''
document.querySelectorAll('[data-live]').forEach(function(b){b.addEventListener('click',function(){var r=document.getElementById(b.dataset.live);r.lastElementChild.innerHTML='<b style="font-weight:500">Updated:</b> metrics refreshed at '+new Date().toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'})+'.';});});
pmCheck();
'''
README = r'''
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
'''
