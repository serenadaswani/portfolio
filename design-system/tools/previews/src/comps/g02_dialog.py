from lib import I, cell, h, frames
NAME = 'Dialog'; GROUP = 'Overlays'; HEIGHT = 1500; WIDTH = 1100
SUB = 'Modal dialog on a scrim; becomes a bottom sheet on compact width (HIG). Native <dialog>, focus contained and returned.'

def dlg(tag='div', idx='', inline=True):
    cls = 'pm-dialog pm-dialog--inline pm-dialog--sheet-preview' if inline else 'pm-dialog'
    role = ' role="dialog" aria-modal="false"' if inline else ''
    return (f'<{tag} class="{cls}"{role} aria-labelledby="dt-{{T}}{{V}}{idx}" aria-describedby="dd-{{T}}{{V}}{idx}" data-dlg>'
            '<div class="pm-dialog__header">'
            f'<h2 class="pm-dialog__title" id="dt-{{T}}{{V}}{idx}">Request full case study</h2>'
            f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--sm" aria-label="Close" data-close>{I["close"]}</button></div>'
            '<div class="pm-dialog__body">'
            f'<p id="dd-{{T}}{{V}}{idx}">The payments case study is under NDA. I’ll share a walkthrough on a call.</p>'
            '<div class="pm-field" style="margin-top:var(--space-4)">'
            f'<label class="pm-field__label" for="de-{{T}}{{V}}{idx}">Work email</label>'
            f'<input class="pm-input" id="de-{{T}}{{V}}{idx}" type="email" autocomplete="email"></div></div>'
            '<div class="pm-dialog__footer"><button type="button" class="pm-btn pm-btn--secondary" data-close>Cancel</button>'
            '<button type="button" class="pm-btn pm-btn--primary">Send request</button></div>'
            f'</{tag}>')

BODY = (h('Open state · centred when wide, bottom sheet when compact') +
        frames('<div class="scrim-stage">' + dlg() + '</div>', 820, 375) +
        h('Live · opens a real modal') +
        '<button type="button" class="pm-btn pm-btn--secondary" data-open="dlg-{T}">Request access</button>' +
        dlg('dialog', 'm', False).replace('data-dlg', 'data-dlg id="dlg-{T}"').replace('{V}', 'x'))
STYLE = '.scrim-stage{display:grid;place-items:center;padding:var(--space-10) var(--space-4);background:var(--color-overlay-scrim)}.scrim-stage .pm-dialog{width:min(440px,100%)}@container (max-width:767px){.scrim-stage{place-items:end stretch;padding:var(--space-16) 0 0}}'
PAIRS = [('title', '--color-text-primary', '--color-bg-elevated', 4.5), ('body', '--color-text-secondary', '--color-bg-elevated', 4.5),
         ('footer text', '--color-text-primary', '--color-bg-surface', 4.5), ('edge', '--color-border-default', '--color-bg-elevated', 0)]
SCRIPT = r'''
document.querySelectorAll('[data-open]').forEach(function(b){var d=document.getElementById(b.dataset.open);
  b.addEventListener('click',function(){d.showModal();var f=d.querySelector('input');(f||d.querySelector('[data-close]')).focus();});
  d.querySelectorAll('[data-close]').forEach(function(c){c.addEventListener('click',function(){d.close();});});
  d.addEventListener('click',function(e){if(e.target===d)d.close();});
  d.addEventListener('close',function(){b.focus();});});
pmCheck();
'''
README = r'''
# Dialog

A modal for a short, focused task that has to be finished or dismissed before continuing (request access, confirm, a short form). It sits on the scrim with a hairline edge and `shadow-lg`, the system's deepest shadow.

## Anatomy
1. **Dialog**: native `<dialog class="pm-dialog">` opened with `showModal()`, `aria-labelledby` the title and `aria-describedby` the lead sentence.
2. **Backdrop**: `::backdrop` = `color-overlay-scrim`.
3. **Surface**: `color-bg-elevated`, 1px `color-border-subtle`, `radius-md`, `shadow-lg`.
4. **Header**: title (`type-h4` at 500, `tracking-h4`) + ghost sm close button, optically aligned to the title's first line and pulled `space-2` into the padding.
5. **Body**: `type-body-sm`, secondary, `space-5` padding. Can hold fields.
6. **Footer**: tonal `color-bg-surface` strip under a hairline. Secondary then primary, right-aligned.

## Variants
Default 440px · `pm-dialog--md` 560px (forms). No destructive variant until there's a destructive action in the product.

## Sizes
Width `min(440 | 560px, 100% − space-8)`, max height 100% − `space-8` (the body scrolls). Padding `space-5`, or `space-4` below 768px.

## States
Closed → open (fades over `motion-duration-base`; none with reduced motion) → closed. Inner controls follow their own states.

## Themes
Light: white on a 72% ink scrim. Dark: night-raised on the same scrim, with a deeper `shadow-lg`. Title and body keep the same hierarchy in both.

## Responsive behavior
Below 768px the dialog becomes a **sheet** (Apple HIG: modals on compact width present from the bottom edge). It's full width, anchored to the bottom, has top corners only, and fits to content up to 100% − `space-10`. It rises `space-6` over `motion-duration-base` (none with reduced motion). The footer stacks the actions full-width with the primary on top, and pads for the home indicator (`env(safe-area-inset-bottom)`). There's no grabber, because the sheet can't be dragged.

## Accessibility
- Native modal: background inert, Esc closes, focus is contained.
- On open, focus goes to the first field (or Close). On close, it **returns to the trigger**.
- The visible Close button has `aria-label="Close"`. Clicking the backdrop also closes, but there's always a visible way out.
- Don't stack dialogs. Keep dialog copy under about 3 sentences.

## Token dependencies
`color-bg-elevated|surface` `color-border-subtle` `color-overlay-scrim` `color-text-primary|secondary` `color-focus-ring` · `shadow-lg` · `space-2|3|4|5|8` · `radius-md` · `type-h4|body-sm` · `tracking-h4` · `weight-medium` · `motion-duration-base` `motion-ease` · Button, Input
'''
