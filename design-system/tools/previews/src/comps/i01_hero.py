from lib import I, cell, h, frames
NAME = 'Hero'; GROUP = 'Page sections'; HEIGHT = 1100; WIDTH = 1100
SUB = 'Centred, sentence-sized landing hero: name in primary, a “currently designing” chip, Copy email and Résumé.'

def hero(hid):
    return (f'<section class="pm-hero" aria-labelledby="hh-{hid}">'
            f'<h1 class="pm-hero__title" id="hh-{hid}"><b>Hi, I’m Serena Daswani,</b> a product designer building calm tools for complicated work in AI and enterprise software.</h1>'
            f'<div class="pm-hero__now"><span class="pm-meta-text pm-hero__now-label">Currently designing {I["arrow"]}</span>'
            '<span class="pm-hero__chip"><span class="pm-hero__dot" aria-hidden="true"></span>Review queue v3, in pilot</span></div>'
            f'<div class="pm-hero__actions"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-copy="hello@serenadaswani.com">{I["copy"]}<span>Copy email</span></button>'
            f'<a class="pm-btn pm-btn--ghost pm-btn--sm" href="#h">Résumé{I["ext"]}</a></div>'
            '<p class="pm-sr" aria-live="polite" data-copy-live></p></section>')

BODY = h('Responsive · copy email works (it shows “Copied”)') + frames(hero('{T}{V}'), 1024, 375)
PAIRS = [('name', '--color-text-primary', '--color-bg-canvas', 4.5), ('sentence', '--color-text-secondary', '--color-bg-canvas', 4.5),
         ('metadata label', '--color-text-tertiary', '--color-bg-canvas', 4.5), ('chip', '--color-text-primary', '--color-bg-elevated', 4.5)]
SCRIPT = r'''
document.querySelectorAll('[data-copy]').forEach(function(b){var label=b.querySelector('span'),live=b.closest('.pm-hero').querySelector('[data-copy-live]');
  b.addEventListener('click',function(){var e=b.getAttribute('data-copy');function done(ok){label.textContent=ok?'Copied':e;live.textContent=ok?'Email address copied':'Copy failed. The address is '+e;setTimeout(function(){label.textContent='Copy email';},2000);}
  try{navigator.clipboard.writeText(e).then(function(){done(true);},function(){done(false);});}catch(x){done(false);}});});
document.querySelectorAll('a[href="#h"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();});});
pmCheck();
'''
README = r'''
# Hero

The landing-page opener: one centred sentence that says who you are and what you make, a live “currently designing” chip, and two quiet actions. It's deliberately small. The work grid right below it is the first visual and the real call to action.

## Anatomy
1. **Section**: `<section class="pm-hero" aria-labelledby>`, centred grid, `space-6` rhythm, `space-20`/`space-16` block padding (`space-24`/`space-20` at ≥1024px).
2. **Title**: the page's `<h1 class="pm-hero__title">`, `type-h3` at 500, max 30ch, balanced. The name sits in `<b>` (`color-text-primary`), the rest in `color-text-secondary`.
3. **Now label**: metadata label, tertiary, with a 12px Lucide arrow.
4. **Chip**: elevated, `radius-sm`, 1px subtle ring + `shadow-xs`, with a 6px `color-state-success` dot that pulses only without reduced motion.
5. **Actions**: secondary sm “Copy email” (copy icon) + ghost sm “Résumé ↗”.
6. **Live region**: visually hidden and polite. It announces the copy result.

## Variants
One. Leave out the chip when there's nothing current to show. Never add a primary button: the page should have a single loud element, and that's the work.

## Sizes
One size. The title follows `type-h3` (23px on mobile, 24px from tablet).

## States
Copy email: default → “Copied” for 2s, or the address shown as text if the clipboard is refused. Buttons otherwise follow Button states.

## Themes
Same in both. Primary/secondary text gives the two-tone sentence in light and dark (17.92 / 7.66:1 light, 15.98 / 10.46:1 dark).

## Responsive behavior
Centred at every width. The sentence wraps within 30ch, and the actions wrap and stay centred.

## Accessibility
- The title is the page's only `h1`.
- Copy email uses the Clipboard API inside the click and falls back to showing the address. It never relies on `mailto:`. The result is announced politely.
- The pulsing dot is decorative (`aria-hidden`) and respects reduced motion.

## Token dependencies
`type-h3` `line-h3` `tracking-h3` · `color-text-primary|secondary|tertiary` · `color-bg-elevated` `color-border-subtle` `color-state-success` · `shadow-xs` · `font-meta` · `radius-sm` · `space-1|2|3|6|16|20|24` · `motion-ease` · Button
'''
