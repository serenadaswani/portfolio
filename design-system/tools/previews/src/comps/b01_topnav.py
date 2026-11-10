from lib import I, cell, h, frames
NAME = 'TopNavigation'; GROUP = 'Navigation'; HEIGHT = 1500; WIDTH = 1100
SUB = 'Site header: full-height items, one 2px cobalt rule on the hairline for the current page; menu below 768px.'

def nav(open_=False, extra=''):
    return (f'<header class="pm-topnav{extra}" data-open="{"true" if open_ else "false"}">'
            '<div class="pm-topnav__bar">'
            '<a class="pm-topnav__brand" href="#t">Portfolio</a>'
            '<nav class="pm-topnav__nav" id="tn-{T}{V}" aria-label="Primary"><ul class="pm-topnav__list">'
            '<li><a class="pm-topnav__item" href="#t" aria-current="page">Work</a></li>'
            '<li><a class="pm-topnav__item" href="#t">About</a></li>'
            '<li><a class="pm-topnav__item" href="#t">Writing</a></li>'
            '<li><a class="pm-topnav__item" href="#t">Contact</a></li>'
            '<li class="pm-topnav__mobile-only"><a class="pm-topnav__item" href="#t">Résumé (PDF)</a></li>'
            '</ul></nav>'
            '<div class="pm-topnav__actions">'
            f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-pressed="false" aria-label="Dark theme">{I["moon"]}</button>'
            '<a class="pm-btn pm-btn--secondary pm-btn--sm pm-topnav__desktop-only" href="#t">Résumé</a>'
            '</div>'
            f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-topnav__menu" aria-expanded="{"true" if open_ else "false"}" aria-controls="tn-{{T}}{{V}}" aria-label="Menu">{I["menu"]}</button>'
            '</div></header>')

ITEM_STATES = ('<div class="pm-spec__row">' +
  cell('<a class="pm-topnav__item" href="#t">About</a>', 'default') +
  cell('<a class="pm-topnav__item is-hover" href="#t">About</a>', 'hover') +
  cell('<a class="pm-topnav__item is-focus" href="#t">About</a>', 'focus-visible') +
  cell('<a class="pm-topnav__item is-active" href="#t">About</a>', 'active') +
  cell('<a class="pm-topnav__item" href="#t" aria-current="page">Work</a>', 'selected · aria-current') +
  '</div>')

BODY = (h('Default · responsive') + frames(nav(), 1024, 375) +
        h('Narrow · menu open') + '<div class="pm-spec__viewport pm-cq" style="width:375px;max-width:100%">' + nav(True).replace('{V}', 'o') + '</div>' +
        h('Compact variant') + '<div class="pm-spec__viewport pm-cq" style="width:1024px;max-width:100%">' + nav(False, ' pm-topnav--compact').replace('{V}', 'c') + '</div>' +
        h('Item states') + ITEM_STATES)
PAIRS = [('item', '--color-text-secondary', '--color-bg-canvas', 4.5), ('selected', '--color-text-primary', '--color-bg-canvas', 4.5),
         ('indicator', '--color-selected-indicator', '--color-bg-canvas', 3), ('hairline', '--color-border-default', '--color-bg-canvas', 0)]
SCRIPT = r'''
document.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();});});
document.querySelectorAll('.pm-topnav__menu').forEach(function(b){
  b.addEventListener('click',function(){var hd=b.closest('.pm-topnav'),o=b.getAttribute('aria-expanded')!=='true';
    b.setAttribute('aria-expanded',o);hd.setAttribute('data-open',o);
    if(o){var f=hd.querySelector('.pm-topnav__item');f&&f.focus();}});
});
document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;
  document.querySelectorAll('.pm-topnav[data-open="true"]').forEach(function(hd){var b=hd.querySelector('.pm-topnav__menu');
    if(getComputedStyle(b).display==='none')return;hd.setAttribute('data-open','false');b.setAttribute('aria-expanded','false');b.focus();});});
document.querySelectorAll('[aria-label="Dark theme"]').forEach(function(b){b.addEventListener('click',function(){b.setAttribute('aria-pressed',b.getAttribute('aria-pressed')!=='true');});});
pmCheck();
'''
README = r'''
# TopNavigation

The site header: wordmark, primary destinations and global actions. It's quiet by design. The current page is marked by one precise cue, a 2px cobalt rule sitting on the header hairline, rather than a filled tab.

## Anatomy
1. **Header**: `<header class="pm-topnav">`, canvas, 1px `color-border-default` bottom hairline.
2. **Bar**: 56px, `content-max-width`. Items stretch to the full bar height, so the indicator lands exactly on the hairline.
3. **Wordmark**: text, `weight-semibold`, `tracking-heading`.
4. **Nav**: `<nav aria-label="Primary">` with a `<ul>`.
5. **Item**: `type-body-sm` at 500, `space-3` padding x, full bar height.
6. **Actions**: ghost icon button (theme) and secondary sm button (Résumé). Action buttons align to the bar centre, while items align to its baseline edge.
7. **Menu button** (narrow): ghost icon with `aria-expanded` and `aria-controls`.

## Variants
Default · `pm-topnav--sticky` (long pages; stays on canvas, no blur or translucency) · `pm-topnav--compact` (48px bar, when a Tabs row sits directly below).

## Sizes
Bar 56px (compact 48). Item hit area = bar height × (label + 24px). Gutters `space-4` narrow and `space-6` at ≥768px container.

## States
| State | Treatment |
|---|---|
| Default | `color-text-secondary` |
| Hover | `color-text-primary`. Text only; no fill and no bar, to keep the header calm. |
| Focus-visible | 3px ring drawn inset (items are 4px apart) |
| Active | `color-bg-surface` |
| Selected | `aria-current="page"` + `color-text-primary` + 2px `color-selected-indicator` rule on the hairline |
| Disabled / error | n/a: unavailable destinations aren't shown |

## Themes
The rule is 4.95:1 (light) and 6.88:1 (dark) against canvas. Secondary to primary text is the supporting cue in both themes.

## Responsive behavior
Below a 768px container, the list moves behind the menu button and opens as a full-width stack under a hairline. The active item's rule moves to a 2px left tick. Résumé folds into the list.

## Accessibility
- One `<nav aria-label="Primary">`, with `aria-current="page"` on the active item.
- Menu: `aria-expanded` and `aria-controls`. Opening moves focus to the first item, and Esc closes and returns focus. It isn't modal, so there's no focus trap.
- Contrast: items 7.66 / 10.46:1, active 17.92 / 15.98:1, rule 4.95 / 6.88:1.

## Token dependencies
`color-bg-canvas` `color-bg-surface` `color-border-default` `color-border-subtle` `color-text-primary|secondary` `color-selected-indicator` `color-focus-ring` · `content-max-width` · `control-height-md` · `space-1|2|3|4|6` · `radius-sm` · `type-body-sm` `type-body-md` · `weight-medium` `weight-semibold` · `tracking-heading`
'''

# ---- v1.7: floating variant ----
def floating(extra='', vid='f'):
    return (f'<header class="pm-topnav pm-topnav--floating{extra}"><div class="pm-topnav__bar">'
            '<a class="pm-topnav__brand" href="#t">Serena Daswani</a><span class="pm-topnav__sep pm-topnav__sep--brand" aria-hidden="true"></span>'
            f'<nav class="pm-topnav__nav" aria-label="Primary ({vid})"><ul class="pm-topnav__list">'
            '<li><a class="pm-topnav__item" href="#t">Work</a></li><li><a class="pm-topnav__item" href="#t">About</a></li>'
            '<li><a class="pm-topnav__item" href="#t">Experience</a></li><li><a class="pm-topnav__item" href="#t">Contact</a></li></ul></nav>'
            '<span class="pm-topnav__sep" aria-hidden="true"></span>'
            f'<div class="pm-topnav__actions"><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--sm" aria-pressed="false" aria-label="Dark theme">{I["moon"]}</button></div>'
            '</div></header>')
FILL = '<div style="padding:var(--space-10) var(--space-6);display:grid;gap:var(--space-3)" aria-hidden="true">' + '<span class="pm-skeleton pm-skeleton--text" style="width:70%"></span><span class="pm-skeleton pm-skeleton--text" style="width:90%"></span>' * 4 + '</div>'
BODY = BODY + (h('Floating variant · one-page sites (scroll inside)') +
  frames('<div class="tn-scroll" data-scroll>' + floating() + FILL + '</div>', 1024, 375) +
  h('Floating · bare (no container)') + '<div class="pm-spec__viewport pm-cq" style="width:1024px;max-width:100%;padding:var(--space-3) 0">' + floating(' pm-topnav--bare', 'b') + '</div>' +
  h('Floating item states') + '<div class="pm-spec__row pm-topnav--floating" style="position:static;pointer-events:auto;padding:0"><div class="pm-topnav__bar" style="width:auto;margin:0;gap:var(--space-4);padding:var(--space-2) var(--space-3)"><ul class="pm-topnav__list" style="gap:var(--space-6)">' +
  cell('<a class="pm-topnav__item" href="#t">About</a>', 'default') + cell('<a class="pm-topnav__item is-hover" href="#t">About</a>', 'hover') +
  cell('<a class="pm-topnav__item is-focus" href="#t">About</a>', 'focus-visible') + cell('<a class="pm-topnav__item is-active" href="#t">About</a>', 'active') + '</ul></div></div>')
STYLE = getattr(__import__('sys').modules[__name__], 'STYLE', '') + '.tn-scroll{height:260px;overflow:auto;padding-top:var(--space-3)}'
SCRIPT = SCRIPT.replace("pmCheck();", "document.querySelectorAll('[data-scroll]').forEach(function(s){var f=s.querySelector('.pm-topnav--floating');s.addEventListener('scroll',function(){f.classList.toggle('is-scrolled',s.scrollTop>8);});});\npmCheck();")
SUB = 'Site header: full-width bar for multi-page sites, or the floating, centred variant (with an optional bare mode) for the one-page landing.'
README = README.replace("## Variants", """## Variants
**Floating** (`pm-topnav--floating`, v1.7): the landing-page header. A centred bar sized to its content floats `space-3` below the top edge. It's sticky, with a 1px `color-border-subtle` ring and `shadow-xs`, and adding `is-scrolled` (set by script once the page scrolls) deepens it to `shadow-md`. Its parts: brand · separator · items · separator · theme toggle. Items are 32px (44px on touch), `radius-sm`, hover `color-bg-surface`. **No current-page indicator**: on a one-page site every item is an anchor. Keyboard focus is unchanged (inset ring). Below 768px the brand hides and the items stay inline, with no menu. `pm-topnav--bare` removes the fill, ring, shadow and separators for a links-only header. The bar keeps `radius-md` (8px) for consistency with every other container.

""",1)
