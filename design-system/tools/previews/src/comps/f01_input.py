from lib import I, S, cell, h, frames
NAME = 'Input'; GROUP = 'Forms'; HEIGHT = 1900; WIDTH = 1100
SUB = 'Text input, textarea and select sharing one field anatomy: label, control, hint, error. 3:1 boundary; 2px focus border.'

def field(fid, label, control, hint=None, error=None, optional=False, count=None):
    desc = ' '.join(x for x in [f'{fid}-h' if hint else '', f'{fid}-e' if error else ''] if x)
    control = control.replace('{DESC}', f' aria-describedby="{desc}"' if desc else '')
    opt = '<span class="pm-field__optional">Optional</span>' if optional else ''
    cnt = f'<span class="pm-field__count" aria-hidden="true">{count}</span>' if count else ''
    hn = f'<p class="pm-field__hint" id="{fid}-h">{hint}</p>' if hint else ''
    er = (f'<p class="pm-field__error" id="{fid}-e">{S["error"]}<span>Error: {error}</span></p>') if error else ''
    return f'<div class="pm-field"><label class="pm-field__label" for="{fid}">{label}{opt}{cnt}</label>{control}{hn}{er}</div>'

def inp(fid, extra='', value='', ph='', cls='', typ='text'):
    v = f' value="{value}"' if value else ''
    p = f' placeholder="{ph}"' if ph else ''
    return f'<input class="pm-input{cls}" id="{fid}" type="{typ}"{v}{p}{extra}{{DESC}}>'

SEL = ('<span class="pm-select"><select class="pm-input" id="{id}"{{DESC}}><option>Product design</option><option>Design systems</option><option>Research</option></select>' + I['chev'] + '</span>')

FORM = ('<form class="demo-form" onsubmit="return false" novalidate>' +
        field('n-{T}{V}', 'Name', inp('n-{T}{V}', ' autocomplete="name"')) +
        field('e-{T}{V}', 'Email', inp('e-{T}{V}', ' autocomplete="email" aria-invalid="true"', 'alex@', typ='email'), error='enter a full email address, like name@example.com.') +
        field('t-{T}{V}', 'Topic', SEL.replace('{id}', 't-{T}{V}')) +
        field('m-{T}{V}', 'Message', '<textarea class="pm-input" id="m-{T}{V}"{DESC}></textarea>', hint='Links to work are welcome.', count='0 / 500') +
        '<div style="display:flex;gap:var(--space-2);justify-content:flex-end"><button type="button" class="pm-btn pm-btn--secondary">Cancel</button><button type="submit" class="pm-btn pm-btn--primary">Send message</button></div></form>')

BODY = (h('States') + '<div class="pm-spec__grid" style="grid-template-columns:repeat(auto-fill,minmax(240px,1fr))">' +
        cell(field('s1-{T}', 'Name', inp('s1-{T}', ph='Your name')), 'default · placeholder') +
        cell(field('s2-{T}', 'Name', inp('s2-{T}', value='Alex Rivera', cls=' is-hover')), 'hover') +
        cell(field('s3-{T}', 'Name', inp('s3-{T}', value='Alex Rivera', cls=' is-focus')), 'focus · 2px focus border') +
        cell(field('s4-{T}', 'Email', inp('s4-{T}', ' aria-invalid="true"', 'alex@'), error='enter a full email address.'), 'error') +
        cell(field('s5-{T}', 'Company', inp('s5-{T}', ' disabled', 'Not required')), 'disabled') +
        cell(field('s6-{T}', 'Portfolio URL', inp('s6-{T}', ' readonly', 'paper-midnight.design')), 'read-only') + '</div>' +
        h('Field anatomy · optional, hint, counter') + '<div class="pm-spec__grid" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">' +
        cell(field('a1-{T}', 'Company', inp('a1-{T}'), hint='Where you’re hiring for.', optional=True), 'optional + hint') +
        cell(field('a2-{T}', 'Website', '<div class="pm-input-group"><span class="pm-input-group__addon" aria-hidden="true">https://</span>' + inp('a2-{T}', ' aria-label="Website, without https"', ph='example.com') + '</div>'), 'with mono prefix') +
        cell(field('a3-{T}', 'Topic', SEL.replace('{id}', 'a3-{T}')), 'select') +
        cell(field('a4-{T}', 'Search', inp('a4-{T}', ph='Search work', cls=' pm-input--sm', typ='search')), 'sm · 32px') + '</div>' +
        h('Composed form · responsive') + frames('<div style="padding:var(--space-6) var(--space-4)">' + FORM + '</div>', 820, 375))
STYLE = ('.pm-spec__grid .pm-spec__cell{align-items:stretch}.pm-spec__grid .pm-field{width:100%}'
         '.demo-form{display:grid;gap:var(--space-5);max-width:520px}')
PAIRS = [('boundary', '--color-border-control', '--color-bg-elevated', 3), ('boundary/canvas', '--color-border-control', '--color-bg-canvas', 3),
         ('value', '--color-text-primary', '--color-bg-elevated', 4.5), ('placeholder', '--color-text-tertiary', '--color-bg-elevated', 4.5),
         ('hint', '--color-text-secondary', '--color-bg-canvas', 4.5), ('error', '--color-state-error', '--color-bg-canvas', 4.5),
         ('focus border', '--color-focus-ring', '--color-bg-elevated', 3)]
SCRIPT = r'''
document.querySelectorAll('textarea.pm-input').forEach(function(t){var c=t.closest('.pm-field').querySelector('.pm-field__count');if(!c)return;t.maxLength=500;t.addEventListener('input',function(){c.textContent=t.value.length+' / 500';});});
pmCheck();
'''
README = r'''
# Input

Text input, textarea and select share one field anatomy. The control is the one place where a 3:1 border is mandatory, so inputs carry the system's strongest resting edge. Labels are bold and readable rather than tiny, and nothing floats.

## Anatomy
1. **Field**: `.pm-field`, a vertical stack with a `space-2` gap.
2. **Label**: a `<label for>`, `type-body-sm` at 500, primary. Always visible: no placeholder-as-label, no floating labels.
3. **Optional marker**: "Optional" in tertiary. Mark the exception, not every required field.
4. **Counter** (textarea): mono caption, right of the label, `aria-hidden` (the limit is enforced by `maxlength`).
5. **Control**: `.pm-input` on `color-bg-elevated`, 1px `color-border-control`, `radius-sm`, `space-3` padding x.
6. **Prefix** (optional): `.pm-input-group__addon`, mono caption on a tonal cell ("https://").
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
`color-bg-elevated|surface` `color-border-control|default` `color-text-primary|secondary|tertiary` `color-state-error` `color-focus-ring` `color-disabled-bg|text|border` · `control-height-sm|md` · `space-1|2|3|5` · `radius-sm` · `type-body-sm|body-md|label|caption` · `font-mono` · `weight-medium`
'''
