from lib import I, cell, h, frames
NAME = 'SideNavigation'; GROUP = 'Navigation'; HEIGHT = 1700; WIDTH = 1100
SUB = 'Compact 32px rows; current page = primary text, weight 500 and a cobalt tick; counts; disclosure below 1024px.'

def side():
    return ('<div style="display:grid;grid-template-columns:minmax(0,260px) 1fr;gap:var(--space-6);padding:var(--space-4)" class="sn-layout">'
            '<nav class="pm-sidenav" data-open="false" aria-label="Projects">'
            f'<button type="button" class="pm-btn pm-btn--secondary pm-sidenav__toggle" aria-expanded="false" aria-controls="sn-{{T}}{{V}}">Projects: Review queue{I["chev"]}</button>'
            '<div class="pm-sidenav__panel" id="sn-{T}{V}">'
            '<p class="pm-sidenav__heading" id="snh-{T}{V}">Selected work</p>'
            '<ul class="pm-sidenav__list" aria-labelledby="snh-{T}{V}">'
            '<li><a class="pm-sidenav__item" href="#s" aria-current="page">Review queue</a></li>'
            '<li><a class="pm-sidenav__item" href="#s">Token system</a></li>'
            '<li><a class="pm-sidenav__item" href="#s">Permissions console</a></li>'
            f'<li><button type="button" class="pm-sidenav__item" aria-expanded="true" aria-controls="sng-{{T}}{{V}}">Archive <span style="display:flex;align-items:center;gap:var(--space-2)"><span class="pm-sidenav__count">3</span>{I["chev"]}</span></button>'
            '<ul class="pm-sidenav__sub" id="sng-{T}{V}"><li><a class="pm-sidenav__item" href="#s">Billing redesign · 2021</a></li><li><a class="pm-sidenav__item" href="#s">Search · 2020</a></li><li><a class="pm-sidenav__item" href="#s">Onboarding · 2019</a></li></ul></li>'
            '<li><span class="pm-sidenav__item" aria-disabled="true">Payments platform <span class="pm-sidenav__count">Under NDA</span></span></li>'
            '</ul></div></nav>'
            '<div class="sn-content"><p class="pm-spec__cap" style="margin:0">Page content</p><div class="pm-skeleton pm-skeleton--heading" style="margin-top:var(--space-3)"></div><div class="pm-skeleton pm-skeleton--text" style="width:90%"></div><div class="pm-skeleton pm-skeleton--text" style="width:75%"></div></div></div>')

BODY = (h('Responsive · inline at ≥1024px, disclosure below') + frames(side(), 1024, 375) +
        h('Item states') + '<div class="pm-spec__row" style="width:260px;flex-direction:column;gap:var(--space-2)">' +
        cell('<a class="pm-sidenav__item" href="#s" style="width:240px">Token system</a>', 'default') +
        cell('<a class="pm-sidenav__item is-hover" href="#s" style="width:240px">Token system</a>', 'hover') +
        cell('<a class="pm-sidenav__item is-focus" href="#s" style="width:240px">Token system</a>', 'focus-visible') +
        cell('<a class="pm-sidenav__item is-active" href="#s" style="width:240px">Token system</a>', 'active') +
        cell('<a class="pm-sidenav__item" href="#s" aria-current="page" style="width:240px">Review queue</a>', 'selected · aria-current') +
        cell('<span class="pm-sidenav__item" aria-disabled="true" style="width:240px">Payments platform</span>', 'disabled · aria-disabled') +
        '</div>')
STYLE = '@container (max-width: 1023px) { .sn-layout { grid-template-columns: 1fr !important; } }'
PAIRS = [('item', '--color-text-secondary', '--color-bg-canvas', 4.5), ('hover', '--color-text-primary', '--color-bg-surface', 4.5),
         ('selected', '--color-text-primary', '--color-bg-canvas', 4.5), ('tick', '--color-selected-indicator', '--color-bg-canvas', 3), ('count', '--color-text-tertiary', '--color-bg-canvas', 4.5),
         ('group rail', '--color-border-default', '--color-bg-canvas', 0), ('disabled', '--color-disabled-text', '--color-bg-canvas', 0)]
SCRIPT = r'''
document.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();});});
document.querySelectorAll('.pm-sidenav__toggle').forEach(function(b){b.addEventListener('click',function(){var n=b.closest('.pm-sidenav'),o=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',o);n.setAttribute('data-open',o);});});
document.querySelectorAll('.pm-sidenav__item[aria-expanded]').forEach(function(b){b.addEventListener('click',function(){b.setAttribute('aria-expanded',b.getAttribute('aria-expanded')!=='true');});});
document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;document.querySelectorAll('.pm-sidenav[data-open="true"]').forEach(function(n){var b=n.querySelector('.pm-sidenav__toggle');n.setAttribute('data-open','false');b.setAttribute('aria-expanded','false');b.focus();});});
pmCheck();
'''
README = r'''
# SideNavigation

A vertical list for moving between sibling pages. Rows are compact (32px with a pointer). The current page reads through type, with primary colour and weight 500, plus a short cobalt tick. Nothing is filled.

## Anatomy
1. **Nav**: `<nav class="pm-sidenav" aria-label="Projects">`.
2. **Toggle** (<1024px): secondary button naming the current page.
3. **Heading**: `type-caption` at 500, `color-text-tertiary`, sentence case. It names the list.
4. **Item**: `type-body-sm` at 400, `color-text-secondary`, `radius-sm`, `space-3` padding x.
5. **Count / meta**: metadata voice (`font-meta`, 13px regular), tertiary, tabular figures, right-aligned.
6. **Group**: `<button aria-expanded>` + a nested list on a 1px `color-border-subtle` rail.
7. **Tick**: 2px × (row − 16px) `color-selected-indicator`, inset at the left edge.

## Variants
Flat · grouped (one level) · with meta.

## Sizes
Rows `control-height-sm` 32px (44px under `pointer: coarse`), 1px apart. Groups of lists are separated by `space-6`. Column width is 3 of 12 columns.

## States
| State | Treatment |
|---|---|
| Default | `color-text-secondary`, weight 400 |
| Hover | `color-bg-surface` + `color-text-primary` |
| Focus-visible | 3px ring, inset |
| Active | `color-bg-sunken` |
| Selected | `aria-current="page"` + `color-text-primary` + weight 500 + cobalt tick |
| Expanded | chevron rotates; `aria-expanded` |
| Disabled | `<span aria-disabled="true">`, `color-disabled-text`, with the reason in meta |
| Error | n/a |

## Themes
The tick is 4.95:1 (light) and 6.88:1 (dark) on canvas. The weight and text-colour shift carries selection in greyscale.

## Responsive behavior
≥1024px container: sticky beside the content. Below that: a full-width toggle that opens the list on an elevated panel with a 1px border. Esc closes it.

## Accessibility
Specific `aria-label` · `aria-current="page"` · groups use `aria-expanded` + `aria-controls` · disabled entries aren't focusable and are explained in text · the toggle names the current location.

## Token dependencies
`color-text-primary|secondary|tertiary` `color-bg-surface|sunken|elevated` `color-border-subtle|default` `color-selected-indicator` `color-disabled-text` `color-focus-ring` · `control-height-sm` `control-min-target` · `space-1|2|3|6` · `radius-sm|md` · `type-body-sm` `type-caption` · `font-meta` · `weight-regular|medium`
'''
