from lib import cell, h, frames
NAME = 'Skeleton'; GROUP = 'Feedback'; HEIGHT = 1200; WIDTH = 1100
SUB = 'Loading placeholders sized from type tokens: text, heading, label, media, button and a card composition.'

CARD = ('<div class="pm-skeleton-group pm-skeleton-group--card" aria-hidden="true">'
        '<span class="pm-skeleton pm-skeleton--media"></span><span class="pm-skeleton pm-skeleton--label" style="margin-top:var(--space-2)"></span>'
        '<span class="pm-skeleton pm-skeleton--heading"></span><span class="pm-skeleton pm-skeleton--text" style="width:95%"></span><span class="pm-skeleton pm-skeleton--text" style="width:70%"></span></div>')

BODY = (h('Elements') + '<div class="pm-spec__grid" style="grid-template-columns:repeat(auto-fill,minmax(260px,1fr))">' +
        cell('<div style="width:100%" aria-hidden="true"><span class="pm-skeleton pm-skeleton--text" style="width:100%"></span><span class="pm-skeleton pm-skeleton--text" style="width:85%"></span></div>', 'text · body-sm line') +
        cell('<div style="width:100%" aria-hidden="true"><span class="pm-skeleton pm-skeleton--text-md" style="width:100%"></span><span class="pm-skeleton pm-skeleton--text-md" style="width:60%"></span></div>', 'text-md · body-md line') +
        cell('<div style="width:100%" aria-hidden="true"><span class="pm-skeleton pm-skeleton--heading"></span></div>', 'heading · h4') +
        cell('<div style="width:100%" aria-hidden="true"><span class="pm-skeleton pm-skeleton--label"></span></div>', 'label') +
        cell('<div style="width:100%" aria-hidden="true"><span class="pm-skeleton pm-skeleton--media"></span></div>', 'media · 16:10') +
        cell('<span class="pm-skeleton pm-skeleton--button" aria-hidden="true"></span>', 'button · 44px') + '</div>' +
        h('Composition · project grid loading') +
        frames('<div style="padding:var(--space-4)" aria-busy="true"><span class="pm-sr" role="status">Loading projects…</span><div class="sk-grid">' + CARD * 3 + '</div></div>', 1024, 375) +
        h('Loading → loaded') + '<div class="sk-swap" style="max-width:340px"><div aria-busy="true" data-sk><span class="pm-sr" role="status">Loading project…</span>' + CARD + '</div>'
        '<button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" style="margin-top:var(--space-3)" data-sk-toggle>Toggle loaded</button></div>')
STYLE = ('.sk-grid{display:grid;gap:var(--space-6);grid-template-columns:1fr}'
         '@container (min-width:768px){.sk-grid{grid-template-columns:repeat(2,1fr)}}@container (min-width:1024px){.sk-grid{grid-template-columns:repeat(3,1fr)}}'
         '.pm-spec__grid .pm-spec__cell{align-items:stretch}')
PAIRS = [('skeleton/canvas', '--color-bg-sunken', '--color-bg-canvas', 0), ('skeleton/surface', '--color-bg-sunken', '--color-bg-surface', 0)]
SCRIPT = r'''
document.querySelectorAll('[data-sk-toggle]').forEach(function(b){var w=b.parentNode.querySelector('[data-sk]'),orig=w.innerHTML,loaded=false;
  b.addEventListener('click',function(){loaded=!loaded;w.setAttribute('aria-busy',!loaded);
    w.innerHTML=loaded?'<span class="pm-sr" role="status">Project loaded</span><article class="pm-card"><p class="pm-card__eyebrow">AI tooling · 2024</p><h3 class="pm-card__title"><a href="#c">Review queue for model evaluations</a></h3><p class="pm-card__summary">Cut median triage time with a ranked, explainable queue.</p></article>':orig;});});
pmCheck();
'''
README = r'''
# Skeleton

A grey placeholder in the shape of the content that's loading. It holds layout steady (no shift when the content arrives) and signals that something is coming. Use it for loads over about 300ms. For quicker loads, show nothing.

## Anatomy
1. **Group**: `.pm-skeleton-group` with `aria-busy="true"` on the region being loaded.
2. **Shapes**: `.pm-skeleton--text | --text-md | --heading | --label | --media | --button`, all `aria-hidden`.
3. **Announcement**: a visually hidden `role="status"` "Loading projects…", replaced by "Projects loaded".
4. **Shimmer**: a `::after` gradient sweep, only when motion is allowed.

## Variants
- **Elements**: individual shapes, matched to the type token they stand in for. Text bars are the cap height of `type-body-sm`/`type-body-md`, with margins making up the token line height, so lines occupy exactly what the real text will.
- **Card composition** (`pm-skeleton-group--card`): mirrors the frameless Card (well, eyebrow line, title, two summary lines). No container fill.
- **Static**: under `prefers-reduced-motion: reduce`, no shimmer, just flat fills.

## Sizes
Taken from tokens: text bars follow `type-*` and `line-*`, heading = `type-h4`, media = the container ratio (`--pm-ratio`, default 16:10), button = `control-height-md`. Set widths to vary line lengths (60–95%), never full justification.

## States
Loading (shapes + `aria-busy="true"`) → loaded (content + `aria-busy="false"`). There are no interactive states. If loading fails, replace it with a StatusIndicator error message. Don't leave skeletons up indefinitely.

## Themes
Fill `color-bg-sunken`, shimmer `color-bg-surface` (`color-bg-elevated` inside cards). In dark, the sunken fill is ink on midnight (1.08:1), so skeletons are deliberately very quiet there. That's acceptable because they're decorative and paired with the status text.

## Responsive behavior
Compositions follow the real layout's grid (1 → 2 → 3). The media keeps its ratio, so height scales with width.

## Accessibility
- Shapes are `aria-hidden`. Announce loading once through a polite live region, then announce completion.
- `aria-busy="true"` on the updating region tells assistive tech to wait.
- Motion: the shimmer runs only in `prefers-reduced-motion: no-preference` (WCAG 2.3.3) and conveys no information.
- Don't make skeletons focusable, and don't put them in the tab order.

## Token dependencies
`color-bg-sunken` `color-bg-surface` `color-bg-elevated` · `type-body-sm` `type-body-md` `type-h4` `type-label` + lines · `control-height-md` · `space-2|3|4|6` · `radius-sm` `radius-md` `radius-lg` · `motion-ease`
'''
