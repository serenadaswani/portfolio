from lib import cell, h, frames
NAME = 'InPageNavigation'; GROUP = 'Navigation'; HEIGHT = 1300; WIDTH = 1100
SUB = 'Mono-numbered index on a hairline rail with scroll-spy; horizontal strip below 1024px.'

SECTIONS = ['Overview', 'The problem', 'Research', 'Decisions', 'Outcome', 'Reflection']
def toc():
    items = ''.join(f'<li><a class="pm-toc__item" href="#ip-{{T}}{{V}}-{i}"{" aria-current=\"location\"" if i == 1 else ""}><span class="pm-toc__num">0{i+1}</span>{s}</a></li>' for i, s in enumerate(SECTIONS))
    secs = ''.join(f'<section id="ip-{{T}}{{V}}-{i}" class="ip-sec" aria-labelledby="iph-{{T}}{{V}}-{i}"><h3 id="iph-{{T}}{{V}}-{i}" class="h4" style="margin:0 0 var(--space-2)">{s}</h3><div class="pm-skeleton pm-skeleton--text" style="width:92%"></div><div class="pm-skeleton pm-skeleton--text" style="width:80%"></div><div class="pm-skeleton pm-skeleton--text" style="width:60%"></div></section>' for i, s in enumerate(SECTIONS))
    return ('<div class="ip-layout">'
            f'<nav class="pm-toc" aria-labelledby="toch-{{T}}{{V}}"><p class="pm-toc__heading" id="toch-{{T}}{{V}}">On this page</p><ol class="pm-toc__list">{items}</ol></nav>'
            f'<div class="ip-scroll" tabindex="0" aria-label="Case study content (scrollable)">{secs}</div></div>')

BODY = (h('Responsive · click an item or scroll the content') + frames(toc(), 1024, 375) +
        h('Item states') + '<div class="pm-spec__row" style="flex-direction:column;gap:var(--space-2)"><ol class="pm-toc__list" style="width:240px">' +
        '<li><a class="pm-toc__item" href="#x">Default</a></li><li><a class="pm-toc__item is-hover" href="#x">Hover</a></li>'
        '<li><a class="pm-toc__item is-focus" href="#x">Focus-visible</a></li><li><a class="pm-toc__item is-active" href="#x">Active</a></li>'
        '<li><a class="pm-toc__item" href="#x" aria-current="location">Selected · aria-current</a></li></ol></div>')
STYLE = ('.ip-layout{display:grid;grid-template-columns:220px 1fr;gap:var(--space-8);padding:var(--space-4)}'
         '.ip-scroll{height:260px;overflow:auto;padding-right:var(--space-2);border-radius:var(--radius-sm)}'
         '.ip-sec{padding:0 0 var(--space-8)}'
         '@container (max-width:1023px){.ip-layout{grid-template-columns:1fr;gap:var(--space-4)}}')
PAIRS = [('item', '--color-text-secondary', '--color-bg-canvas', 4.5), ('current', '--color-text-primary', '--color-bg-canvas', 4.5),
         ('indicator', '--color-selected-indicator', '--color-bg-canvas', 3), ('rail', '--color-border-default', '--color-bg-canvas', 0), ('hover rail', '--color-border-strong', '--color-bg-canvas', 3)]
SCRIPT = r'''
var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('.ip-layout').forEach(function(L){
  var links=[].slice.call(L.querySelectorAll('.pm-toc__item')), box=L.querySelector('.ip-scroll');
  function set(id){links.forEach(function(a){if(a.getAttribute('href')==='#'+id){a.setAttribute('aria-current','location');a.scrollIntoView({block:'nearest',inline:'nearest'});}else a.removeAttribute('aria-current');});}
  links.forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var t=L.querySelector(a.getAttribute('href'));
    box.scrollTo({top:t.offsetTop-box.offsetTop,behavior:reduce?'auto':'smooth'});set(t.id);t.setAttribute('tabindex','-1');t.focus({preventScroll:true});});});
  box.addEventListener('scroll',function(){var cur=null;L.querySelectorAll('.ip-sec').forEach(function(s){if(s.offsetTop-box.offsetTop-box.scrollTop<=40)cur=s.id;});if(cur)set(cur);});
});
document.querySelectorAll('a[href="#x"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();});});
pmCheck();
'''
README = r'''
# InPageNavigation

An "On this page" index for long case studies. Mono numbers on a hairline rail give it a technical, editorial index feel without adding decoration.

## Anatomy
1. **Nav**: `<nav class="pm-toc" aria-labelledby>`.
2. **Heading**: "On this page", caption at 500, tertiary, sentence case.
3. **List**: `<ol>` on a 1px `color-border-default` rail.
4. **Item**: mono number (`01`, tertiary, tabular) + title (`type-body-sm`), baseline-aligned with a `space-3` gap.
5. **Indicator**: a 2px cobalt segment over the rail.

## Variants
Numbered (default) · plain (omit `pm-toc__num`). Vertical rail or horizontal strip is chosen by container width.

## Sizes
Vertical rows `control-height-sm` 32px (44 on touch). Strip items `control-height-md`.

## States
Default `color-text-secondary` · hover `color-text-primary` + `color-border-strong` rail segment · focus inset ring · active `color-bg-surface` · selected `aria-current="location"` + primary text + weight 500 + cobalt segment · disabled and error n/a.

## Themes
The segment is 4.95:1 and 6.88:1 on canvas. The numbers stay tertiary (5.55 / 7.86:1) in both themes.

## Responsive behavior
≥1024px container: sticky rail in a 3-column aside. Below: a horizontal strip with its scrollbar hidden. The current item scrolls into view.

## Accessibility
Links to real ids (works without JS) · `aria-current="location"` · focus moves to the target section after a jump · smooth scrolling only without reduced motion · not a tablist.

## Token dependencies
`color-text-primary|secondary|tertiary` `color-border-default|strong` `color-selected-indicator` `color-bg-surface` `color-focus-ring` · `control-height-sm|md` · `space-1|3|4` · `radius-sm` · `type-body-sm` `type-caption` · `font-mono` · `weight-medium`
'''
