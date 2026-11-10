from lib import I, S, cell, h, frames
import itertools
_c = itertools.count(1)
NAME = 'Panel'; GROUP = 'Containers'; HEIGHT = 1900; WIDTH = 1100
SUB = 'Dimensional (default: light ring + shadow-xs) and tonal regions, hairline metadata rows, collapsible, error, tonal footer.'

META = ('<dl class="pm-meta"><dt>Role</dt><dd>Lead product designer</dd><dt>Team</dt><dd>2 designers, 6 engineers, 1 PM</dd>'
        '<dt>Timeline</dt><dd><span class="pm-mono">2024.02 – 2024.11</span></dd><dt>Outcome</dt><dd>Median triage time roughly halved in the pilot</dd></dl>')

def panel(cls='', title='Project details', body=META, action=True, footer=False, desc=None):
    n = next(_c)
    act = '<button type="button" class="pm-btn pm-btn--tertiary pm-btn--sm">Edit</button>' if action else ''
    d = f'<p class="pm-panel__desc">{desc}</p>' if desc else ''
    ft = ('<div class="pm-panel__footer"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm">Cancel</button><button type="button" class="pm-btn pm-btn--primary pm-btn--sm">Send</button></div>' if footer else '')
    return (f'<section class="pm-panel{cls}" aria-labelledby="p-{{T}}{{V}}-{n}">'
            f'<div class="pm-panel__header"><h3 class="pm-panel__title" id="p-{{T}}{{V}}-{n}">{title}</h3>{act}{d}</div>'
            f'<div class="pm-panel__body">{body}</div>{ft}</section>')

def coll(n, expanded=True):
    return ('<section class="pm-panel pm-panel--collapsible"><div class="pm-panel__header">'
            f'<h3 style="margin:0;flex:1"><button type="button" class="pm-panel__toggle" aria-expanded="{"true" if expanded else "false"}" aria-controls="pc-{{T}}{n}" id="pt-{{T}}{n}">Research methods<span class="pm-panel__chev">{I["chev"]}</span></button></h3></div>'
            f'<div class="pm-panel__body" id="pc-{{T}}{n}" role="region" aria-labelledby="pt-{{T}}{n}"><p>Twelve contextual interviews, a four-week diary study, and two rounds of usability testing on the ranked queue.</p></div></section>')

ERR = ('<section class="pm-panel pm-panel--error" role="alert" aria-labelledby="pe-{T}">'
       f'<div class="pm-panel__header"><h3 class="pm-panel__title" id="pe-{{T}}"><span class="pm-status pm-status--error" style="display:contents">{S["error"]}</span>Message not sent</h3></div>'
       '<div class="pm-panel__body"><p>Error: check the email address and try again. Your message has been kept.</p></div></section>')

BODY = (h('Variants') + '<div class="pm-spec__grid" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">' +
        cell(panel(), 'default · light ring + shadow-xs') +
        cell(panel(' pm-panel--tonal', action=False), 'tonal · Mineral fill, no border') +
        cell(panel(' pm-panel--sunken', title='Raw data', action=False, body='<p class="pm-mono" style="margin:0">n = 412 evaluations · p50 18m → 9m</p>'), 'sunken · code and data') +
        cell(panel(title='Contact', desc='I reply within two working days.', body='<p>Messages go straight to my inbox.</p>', action=False, footer=True), 'with description + tonal footer') +
        cell(coll('a'), 'collapsible · expanded') + cell(coll('b', False), 'collapsible · collapsed') +
        cell(ERR, 'error') + '</div>' +
        h('Collapsible header states') + '<div class="pm-spec__row">' +
        cell(f'<button type="button" class="pm-panel__toggle" aria-expanded="false" style="width:240px">Research methods<span class="pm-panel__chev">{I["chev"]}</span></button>', 'default') +
        cell(f'<button type="button" class="pm-panel__toggle is-hover" aria-expanded="false" style="width:240px">Research methods<span class="pm-panel__chev">{I["chev"]}</span></button>', 'hover') +
        cell(f'<button type="button" class="pm-panel__toggle" aria-expanded="false" style="width:240px;outline:var(--focus-ring-width) solid var(--color-focus-ring);outline-offset:var(--focus-ring-offset)">Research methods<span class="pm-panel__chev">{I["chev"]}</span></button>', 'focus-visible') +
        '</div>' +
        h('Sizes and responsive padding') + frames('<div style="padding:var(--space-4);display:grid;gap:var(--space-4)">' +
              panel(' pm-panel--sm', title='Small · space-4', action=False, body='<p>Dense asides.</p>') +
              panel(title='Medium · space-5', action=False, body='<p>Default.</p>') +
              panel(' pm-panel--lg', title='Large · space-8', action=False, body='<p>Feature regions; h4 title. Every size drops to space-4 below 768px.</p>') + '</div>', 820, 375))
STYLE = '.pm-spec__grid .pm-spec__cell{align-items:stretch}'
PAIRS = [('title', '--color-text-primary', '--color-bg-elevated', 4.5), ('body', '--color-text-secondary', '--color-bg-elevated', 4.5),
         ('body/tonal', '--color-text-secondary', '--color-bg-surface', 4.5), ('key', '--color-text-tertiary', '--color-bg-elevated', 4.5),
         ('mono/sunken', '--color-text-tertiary', '--color-bg-sunken', 4.5), ('error edge', '--color-state-error', '--color-bg-elevated', 3),
         ('edge', '--color-border-default', '--color-bg-canvas', 0)]
SCRIPT = r'''
document.querySelectorAll('.pm-panel__toggle[aria-controls]').forEach(function(b){b.addEventListener('click',function(){b.setAttribute('aria-expanded',b.getAttribute('aria-expanded')!=='true');});});
pmCheck();
'''
README = r'''
# Panel

A titled region for grouped content: project details, an aside, a form or an error summary. It's separated by a light 1px ring with a whisper of `shadow-xs` (flat but dimensional), or by a tonal step.

## Anatomy
1. **Region**: `<section>` or `<aside>`, `aria-labelledby` its title, `radius-md`.
2. **Header**: title (`type-body-md` at 500; `type-h4` at lg) + optional sm action, pulled to the right edge by `space-2` so its label aligns with the padding. An optional description (secondary) wraps under the title.
3. **Body**: `type-body-sm`, `color-text-secondary`, `space-3` under the header.
4. **Metadata rows** (`pm-meta`): key (`type-label`, tertiary) and value (`type-body-sm`, primary) on `color-border-subtle` hairlines, like a spec sheet. Dates and numbers are Geist Mono.
5. **Footer**: tonal `color-bg-surface` strip under a `color-border-default` hairline, actions right-aligned.

## Variants
| Variant | Class | Use |
|---|---|---|
| Default | — | Elevated paper + 1px `color-border-subtle` ring + `shadow-xs`. Forms, contact, details. |
| Tonal | `pm-panel--tonal` | Mineral fill, no border. Asides beside prose. |
| Sunken | `pm-panel--sunken` | Code, raw data, quotes. |
| Collapsible | `pm-panel--collapsible` | Optional depth (methods, appendices). |
| Error | `pm-panel--error` | `color-state-error` edge, shape icon, sentence starting "Error:". |

`--elevated`, `--outlined` and `--surface` from v1.2 are kept as aliases (default, default, tonal), so nothing breaks.

## Sizes
`pm-panel--sm` `space-4` · md `space-5` · `pm-panel--lg` `space-8` with an h4 title. All drop to `space-4` below a 768px container.

## States
Static panels have no states. Collapsible header: hover (the chevron gets a `color-bg-surface` square), focus-visible (3px ring), expanded/collapsed (`aria-expanded`, chevron rotates). Error is a variant. Selected and disabled: n/a.

## Themes
Default is white + silver hairline in light, and night-raised + `dark-border-default` in dark. Tonal is mineral / deep-blue. Same structure, same hierarchy.

## Responsive behavior
Padding compresses below 768px. The header wraps its action under the title before they can collide. Metadata stays two-column (keys are short).

## Accessibility
- Label regions you want people to jump to. Not every panel needs to be a landmark.
- Collapsible: a button inside the heading, `aria-controls` → body `role="region"`. Collapsed content is `display: none`.
- Error: word + shape + colour. Move focus to the summary after a failed submit.
- Contrast: body 8.01 / 8.64:1 on elevated, keys 5.80 / 6.49:1.

## Token dependencies
`color-bg-elevated|surface|sunken` `color-border-default|subtle` `shadow-xs` `color-text-primary|secondary|tertiary` `color-state-error` `color-focus-ring` · `space-2|3|4|5|6|8` · `radius-sm|md` · `type-body-md|body-sm|label|h4|caption` · `font-mono` · `weight-medium` · `control-height-sm`
'''
