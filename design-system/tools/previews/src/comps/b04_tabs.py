from lib import cell, h, frames
NAME = 'Tabs'; GROUP = 'Navigation'; HEIGHT = 1300; WIDTH = 1100
SUB = 'Underline tabs on a hairline (default) and segmented control for view switches; arrow-key roving focus.'

def tabs(kind='', items=(('Overview', None), ('Process', '04'), ('Outcomes', None), ('Archive', None)), sel=0, disabled=3, n='a'):
    t = ''.join(
        f'<button type="button" role="tab" class="pm-tabs__tab" id="tab-{{T}}{{V}}{n}{i}" aria-controls="tp-{{T}}{{V}}{n}{i}" aria-selected="{"true" if i == sel else "false"}" tabindex="{0 if i == sel else -1}"'
        + (' aria-disabled="true"' if i == disabled else '') + f'>{lab}' + (f'<span class="pm-tabs__count">{c}</span>' if c else '') + '</button>'
        for i, (lab, c) in enumerate(items))
    p = ''.join(f'<div role="tabpanel" class="pm-tabs__panel" id="tp-{{T}}{{V}}{n}{i}" aria-labelledby="tab-{{T}}{{V}}{n}{i}" tabindex="0"{"" if i == sel else " hidden"}>{lab}: panel content for this view.</div>' for i, (lab, c) in enumerate(items))
    return f'<div class="pm-tabs{kind}" data-tabs><div role="tablist" aria-label="Case study views" class="pm-tabs__list">{t}</div>{p}</div>'

SEG = (('Grid', None), ('List', None), ('Timeline', None))
BODY = (h('Underline · default') + '<div style="max-width:640px">' + tabs() + '</div>' +
        h('Small') + '<div style="max-width:480px">' + tabs(' pm-tabs--sm', n='s') + '</div>' +
        h('Segmented · switching views of the same content') + tabs(' pm-tabs--segmented', SEG, 0, -1, 'g') +
        h('Tab states') + '<div class="pm-spec__row"><div class="pm-tabs__list" style="border:0">' +
        cell('<button type="button" class="pm-tabs__tab">Process</button>', 'default') +
        cell('<button type="button" class="pm-tabs__tab is-hover">Process</button>', 'hover') +
        cell('<button type="button" class="pm-tabs__tab is-focus">Process</button>', 'focus-visible') +
        cell('<button type="button" class="pm-tabs__tab is-active">Process</button>', 'active') +
        cell('<button type="button" class="pm-tabs__tab" aria-selected="true">Process</button>', 'selected') +
        cell('<button type="button" class="pm-tabs__tab" aria-disabled="true">Archive</button>', 'disabled') + '</div></div>' +
        h('Responsive · the list scrolls horizontally; it never wraps') + frames('<div style="padding:var(--space-4)">' + tabs(items=(('Overview', None), ('Process', '04'), ('Research', '12'), ('Outcomes', None), ('Reflection', None)), disabled=-1, n='r') + '</div>', 820, 375))
PAIRS = [('tab', '--color-text-secondary', '--color-bg-canvas', 4.5), ('selected', '--color-text-primary', '--color-bg-canvas', 4.5),
         ('indicator', '--color-selected-indicator', '--color-bg-canvas', 3), ('segment edge', '--color-border-control', '--color-bg-surface', 3),
         ('count', '--color-text-tertiary', '--color-bg-canvas', 4.5)]
SCRIPT = r'''
document.querySelectorAll('[data-tabs]').forEach(function(T){
  var tabs=[].slice.call(T.querySelectorAll('[role="tab"]')).filter(function(t){return t.getAttribute('aria-disabled')!=='true';});
  function sel(t,focus){T.querySelectorAll('[role="tab"]').forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;
    var p=document.getElementById(x.getAttribute('aria-controls'));if(p)p.hidden=!on;});if(focus)t.focus();}
  tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(t);});
    t.addEventListener('keydown',function(e){var k=e.key,j=null;if(k==='ArrowRight')j=(i+1)%tabs.length;else if(k==='ArrowLeft')j=(i-1+tabs.length)%tabs.length;else if(k==='Home')j=0;else if(k==='End')j=tabs.length-1;
      if(j!==null){e.preventDefault();sel(tabs[j],true);}});});
});
pmCheck();
'''
README = r'''
# Tabs

Switches between sibling views inside one page section. Underline tabs sit on a hairline, like a table of contents. The segmented control is reserved for showing the same content a different way (grid, list or timeline).

## Anatomy
1. **Tablist**: `role="tablist"` with `aria-label`, plus a 1px `color-border-default` baseline.
2. **Tab**: `<button role="tab">`, `type-body-sm` at 500, `space-3` padding x, `radius-sm` top corners.
3. **Count** (optional): metadata label, tertiary, tabular (`04`).
4. **Indicator**: a 2px `color-selected-indicator` rule on the baseline.
5. **Panel**: `role="tabpanel"`, labelled by its tab, `space-5` above.

## Variants
| Variant | Class | Use |
|---|---|---|
| Underline | default | Different content per tab (Overview, Process, Outcomes). |
| Segmented | `pm-tabs--segmented` | Same content, different arrangement. Tonal track (`color-bg-surface`, `radius-md`, `space-1` inset) with an elevated selected segment (`radius-sm`, 1px `color-border-control`). The radii nest: 8 = 4 + 4. |

## Sizes
md: `control-height-md` (40, 44 on touch). `pm-tabs--sm`: `control-height-sm`, `type-label`, `space-2` padding. Segmented items are the track height minus 2 × `space-1`.

## States
| State | Underline | Segmented |
|---|---|---|
| Default | `color-text-secondary` | `color-text-secondary` |
| Hover | `color-text-primary` + 2px `color-border-default` rule | `color-text-primary` |
| Focus-visible | 3px ring, inset | 3px ring, inset |
| Active | `color-bg-surface` | same |
| Selected | `aria-selected="true"`, `color-text-primary`, cobalt rule | elevated fill + 1px `color-border-control` (3.33:1 on the track) |
| Disabled | `aria-disabled="true"`, `color-disabled-text`, skipped by arrow keys | same |
| Error | n/a | n/a |

## Themes
The cobalt rule is 4.95 / 6.88:1 on canvas. The segmented edge uses `color-border-control`, so the selected segment holds 3:1 in both themes.

## Responsive behavior
The tablist scrolls horizontally (scrollbar hidden) and never wraps to two lines. Prefer five or fewer tabs. More than that is navigation, not tabs.

## Accessibility
- WAI-ARIA tabs pattern with roving tabindex: Tab enters the selected tab. ←/→ move and select (automatic activation), and Home/End jump to the ends.
- Each panel is `tabindex="0"` so its content is reachable, and hidden panels use `hidden`.
- Don't use tabs for page navigation (that's TopNavigation, or InPageNavigation with links).

## Token dependencies
`color-text-primary|secondary|tertiary` `color-border-default|subtle|control` `color-selected-indicator` `color-bg-surface|elevated` `color-disabled-text` `color-focus-ring` · `control-height-sm|md` · `space-1|2|3|5` · `radius-sm|md` · `type-body-sm|label|caption` · `font-meta` · `weight-medium`
'''
