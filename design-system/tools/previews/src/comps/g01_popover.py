from lib import I, cell, h
NAME = 'Popover'; GROUP = 'Overlays'; HEIGHT = 900
SUB = 'Non-modal panel anchored to a trigger: border + shadow-md (a real overlay), Esc and outside-click close, focus returns.'

POP = ('<p class="pm-popover__title" id="pt-{T}{N}">Share this case study</p>'
       '<p class="pm-popover__body">Anyone with the link can view it. Visuals under NDA stay hidden.</p>'
       '<div class="pm-input-group" style="margin-top:var(--space-3)"><span class="pm-input-group__addon" aria-hidden="true">https://</span><input class="pm-input pm-input--sm" readonly value="pm.design/review-queue" aria-label="Share link"></div>'
       '<div class="pm-popover__actions"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-close>Done</button><button type="button" class="pm-btn pm-btn--primary pm-btn--sm">' + I['copy'] + 'Copy link</button></div>')

BODY = (h('Open state') + '<div style="padding-bottom:var(--space-2)"><div class="pm-popover pm-popover--inline" role="dialog" aria-labelledby="pt-{T}s">' + POP.replace('{N}', 's') + '</div></div>' +
        h('Live · click the trigger; Esc or click outside to close') +
        '<div style="min-height:300px"><span class="pm-popover-anchor">'
        '<button type="button" class="pm-btn pm-btn--secondary" aria-haspopup="dialog" aria-expanded="false" aria-controls="pop-{T}" data-pop>Share</button>'
        '<div class="pm-popover" id="pop-{T}" role="dialog" aria-labelledby="pt-{T}l" tabindex="-1" hidden>' + POP.replace('{N}', 'l') + '</div></span></div>')
PAIRS = [('title', '--color-text-primary', '--color-bg-elevated', 4.5), ('body', '--color-text-secondary', '--color-bg-elevated', 4.5),
         ('edge', '--color-border-default', '--color-bg-canvas', 0)]
SCRIPT = r'''
document.querySelectorAll('[data-pop]').forEach(function(t){var p=document.getElementById(t.getAttribute('aria-controls'));
  function close(f){p.hidden=true;t.setAttribute('aria-expanded','false');if(f)t.focus();}
  t.addEventListener('click',function(){var o=p.hidden;p.hidden=!o;t.setAttribute('aria-expanded',o);if(o)p.focus();});
  p.addEventListener('keydown',function(e){if(e.key==='Escape'){close(true);}});
  p.querySelectorAll('[data-close]').forEach(function(b){b.addEventListener('click',function(){close(true);});});
  document.addEventListener('click',function(e){if(!p.hidden&&!p.contains(e.target)&&e.target!==t)close(false);});
});
pmCheck();
'''
README = r'''
# Popover

A small non-modal panel anchored to its trigger, used for a short task or a closer look (share link, filter options, a definition with an action). It takes `shadow-md`, a soft, layered, Midnight-tinted shadow, because it really does sit above the page.

## Anatomy
1. **Anchor**: `.pm-popover-anchor` wraps the trigger and the panel.
2. **Trigger**: a Button with `aria-haspopup="dialog"`, `aria-expanded` and `aria-controls`.
3. **Panel**: `role="dialog"` + `aria-labelledby`, `color-bg-elevated`, 1px `color-border-subtle`, `radius-md`, `shadow-md`, `space-4` padding, max 320px.
4. **Title**: `type-body-sm` at 500. **Body**: `type-body-sm`, secondary.
5. **Actions**: sm buttons, right-aligned, `space-4` above.

## Variants
Default (left-aligned to the trigger) · `pm-popover--end` (right-aligned, for triggers at the right edge). Use a Tooltip for a name and a Dialog for anything that blocks.

## Sizes
Width `min(320px, 100vw − space-8)`. Content decides the height. Keep it under about 40% of the viewport.

## States
Closed (`hidden`) → open. Focus moves into the panel on open and returns to the trigger on close. Controls inside follow their own states.

## Themes
Elevated paper or night-raised + hairline + `shadow-md` (deeper in dark). The shadow is there to separate the overlay from content of the same colour, not for decoration.

## Responsive behavior
Width is capped at the viewport minus `space-8`. Below 768px, if the content exceeds about 4 lines, use a Dialog instead.

## Accessibility
- Non-modal: no focus trap, so Tab can leave it. Esc closes and returns focus. Clicking outside closes.
- The trigger exposes `aria-expanded`. The panel is labelled by its title.
- Don't put the only route to essential content inside a popover.

## Token dependencies
`color-bg-elevated` `color-border-subtle` `color-text-primary|secondary` `color-focus-ring` · `shadow-md` · `space-1|2|3|4|8` · `radius-md` · `type-body-sm` · `weight-medium`
'''
