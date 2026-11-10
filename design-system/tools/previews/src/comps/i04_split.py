from lib import I, h, frames, showcase
NAME = 'SplitLayout'; GROUP = 'Page sections'; HEIGHT = 2300; WIDTH = 1340
SUB = 'Sticky left column (intro, status, actions, vertical nav with scroll-spy, socials, clock) beside a scrolling work column. Stacks below 1024px.'

NAV = ['Work', 'About', 'Experience', 'Contact']
def page(uid):
    nav = ''.join(f'<li><a class="pm-sidenav__item" href="#{uid}-{s.lower()}"{" aria-current=\"location\"" if j == 0 else ""} data-spy>{s}</a></li>' for j, s in enumerate(NAV))
    work = ('<ul class="pm-showcase-grid">'
            f'<li class="pm-showcase-grid__wide">{showcase("form", "Redesigning Mensio’s Data Explorer for self-serve analysis", "Shipped 2026.", ["Product design", "Analytics"], "2026 · Mensio", href="#s")}</li>'
            f'<li>{showcase("queue", "Placeholder project", "", ["Product design"], "Placeholder", href="#s")}</li>'
            f'<li>{showcase("grid", "Placeholder project", "", ["Design systems"], "Placeholder", href="#s")}</li></ul>')
    return f'''<div class="sl-device" style="--pm-split-h:720px"><div class="pm-split">
  <aside class="pm-split__aside" aria-label="Introduction">
    <div class="pm-intro">
      <span class="pm-intro__mark" aria-hidden="true">SD</span>
      <h2 class="pm-intro__name">Serena Daswani <span>is a product designer who builds for fun.</span></h2>
      <p class="pm-intro__text">Currently designing at Deploy. Previously Apple and Procense.</p>
      <span class="pm-intro__status"><span class="pm-hero__dot" aria-hidden="true"></span>Designing at Deploy</span>
      <div class="pm-intro__actions"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm">{I["copy"]}<span>Copy email</span></button><a class="pm-btn pm-btn--ghost pm-btn--sm" href="#s">Résumé{I["ext"]}</a></div>
    </div>
    <nav class="pm-sidenav pm-split__nav" aria-label="Sections"><ul class="pm-sidenav__list">{nav}</ul></nav>
    <div class="pm-split__foot"><ul aria-label="Elsewhere"><li><a class="pm-link pm-link--subtle" href="#s">LinkedIn</a></li><li><a class="pm-link pm-link--subtle" href="#s">GitHub</a></li></ul><span class="pm-meta-text" data-clock>--:-- PT</span></div>
  </aside>
  <div class="pm-split__main">
    <section class="pm-split__section" id="{uid}-work" aria-label="Work"><h3 class="pm-split__h">Selected work</h3>{work}</section>
    <section class="pm-split__section" id="{uid}-about" aria-label="About"><h3 class="pm-split__h">About</h3><p class="pm-intro__text" style="max-width:60ch">A short first-person bio.</p></section>
    <section class="pm-split__section" id="{uid}-experience" aria-label="Experience"><h3 class="pm-split__h">Experience</h3><p class="pm-intro__text">Experience list.</p></section>
    <section class="pm-split__section" id="{uid}-contact" aria-label="Contact" style="padding-bottom:480px"><h3 class="pm-split__h">Contact</h3><p class="pm-intro__text">Closing line and Copy email.</p></section>
  </div>
</div></div>'''

BODY = (h('Desktop (≥1024px container): the left column stays put while the work scrolls. Scroll inside the frame; the nav follows.') +
        frames(page('{T}{V}'), 1280, 390, 'Wide container · 1280px, scrollable', 'Narrow container · 390px: intro, nav row, then work'))
STYLE = ('.sl-device{height:720px;overflow-y:auto;overscroll-behavior:contain}'
         '.pm-spec__viewport .sl-device{max-width:100%}')
PAIRS = [('intro name', '--color-text-primary', '--color-bg-canvas', 4.5), ('intro tail', '--color-text-tertiary', '--color-bg-canvas', 4.5),
         ('intro text', '--color-text-secondary', '--color-bg-canvas', 4.5), ('nav item', '--color-text-secondary', '--color-bg-canvas', 4.5),
         ('scroll-spy tick', '--color-selected-indicator', '--color-bg-canvas', 3), ('aside rule', '--color-border-subtle', '--color-bg-canvas', 0)]
SCRIPT = r'''
document.querySelectorAll('.sl-device').forEach(function(dev){var links=[].slice.call(dev.querySelectorAll('[data-spy]'));
  function spy(){var top=dev.getBoundingClientRect().top,cur=links[0];links.forEach(function(a){var s=dev.querySelector(a.getAttribute('href'));if(s&&s.getBoundingClientRect().top-top<dev.clientHeight*0.35)cur=a;});
    links.forEach(function(a){if(a===cur)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}
  dev.addEventListener('scroll',spy,{passive:true});
  links.forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var s=dev.querySelector(a.getAttribute('href'));dev.scrollTo({top:s.offsetTop-24,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});});});});
function clk(){var t=new Intl.DateTimeFormat('en-US',{hour:'numeric',minute:'2-digit',timeZone:'America/Los_Angeles'}).format(new Date());document.querySelectorAll('[data-clock]').forEach(function(c){c.textContent=t+' PT';});}
clk();setInterval(clk,30000);
document.querySelectorAll('a[href="#s"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();});});
pmCheck();
'''
README = r'''
# Split layout

A two-column page for the portfolio home (v1.8), after Megan Yap and Dakota Sumner. The left column introduces you and holds the navigation, and it stays put. The right column scrolls through the work. It reads like a spec sheet beside a gallery: who, then what.

## Anatomy
1. **Split**: `.pm-split`, a grid. Put `.pm-cq` on its parent. ≥1024px container: `360px` + `minmax(0, 1fr)`.
2. **Aside**: `<aside class="pm-split__aside">`, a flex column with `space-6` gaps. At ≥1024px it's sticky, one viewport tall (`--pm-split-h`, default `100dvh`), with a `color-border-subtle` rule on its right edge and its own scroll if the window is short.
3. **Intro** `.pm-intro`: 40px mark (initials now, photo later), name as the page's `<h1 class="pm-intro__name">` (`type-h2` size, with the descriptor in a tertiary `<span>`), one line of text, a status with the live dot, and Copy email + Résumé (`pm-btn--sm`).
4. **Vertical nav**: the SideNavigation component with `.pm-split__nav`, pushed to the bottom of the aside (`margin-top: auto`). Links point to sections on the page.
5. **Foot** `.pm-split__foot`: social links (`pm-link--subtle`) and local time in the metadata voice, above a hairline.
6. **Main** `.pm-split__main`: the content column, and itself a container, so its contents respond to the column's width rather than the window's.
7. **Sections** `.pm-split__section` with a quiet `.pm-split__h` label (body-md, 500, secondary). `space-20` between sections.

## Variants
- **Showcase work** (default): `pm-showcase-grid` with Card `--showcase`. Strongest projects first, full width; supporting projects two-up.
- **Tile work**: `pm-work-grid pm-work-grid--even` with Card `--tile`, for a longer list.

## Sizes
Aside 360px. Main padding `space-12` top, `space-10` sides, `space-24` bottom at ≥1024px; `space-10`/`space-4` sides below.

## States
| State | Behaviour |
|---|---|
| Scroll-spy (current section) | `aria-current="location"` on the nav link: primary text, weight 500, 2px `color-selected-indicator` tick (left on desktop, underneath in the row). Use `location`, not `page`: every link is on this page. |
| Hover / focus / active | From SideNavigation: surface fill, 3px inset focus ring, sunken press. |
| Disabled / error | n/a: a layout. |

## Themes
Same structure in both. The aside sits on canvas with only a subtle rule, so the work column carries the colour.

## Responsive behavior
- **≥1024px:** two columns, sticky aside.
- **768–1023px and phones:** one column. Intro first, then the nav as a wrapping row of links (the tick moves under the label), then the foot, then the work. The aside scrolls away with the page.
- The showcase grid goes two-up only when the main column is ≥768px wide (roughly a 1200px window). Below that, every card is full width and lays itself out by its own width.
- Edge padding respects `safe-area-inset-*`.

## Accessibility
- Landmarks: `<aside aria-label="Introduction">`, `<nav aria-label="Sections">`, `<main class="pm-split__main">`. One `<h1>` (the name); section labels are `<h2>`, card titles `<h3>`.
- The sticky aside never traps focus, and the tab order matches the visual order (aside, then main).
- Scroll-spy updates `aria-current` only; it doesn't announce. Smooth scrolling is skipped under reduced motion.
- 44px nav targets under `pointer: coarse` (SideNavigation).

## Token dependencies
`color-bg-canvas|surface` `color-border-subtle` `color-text-primary|secondary|tertiary` `color-selected-indicator` `color-state-success` · `space-2|3|4|6|8|10|12|16|20|24` · `radius-sm` · `type-h2|body-md|body-sm|label` · `font-meta` · `tracking-heading` · `weight-medium`
'''
