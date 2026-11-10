from lib import I, IMG, IMG_ALT, h, frames
NAME = 'Lightbox'; GROUP = 'Media'; HEIGHT = 2300; WIDTH = 1100
SUB = 'Modal image viewer: always dark-scoped, counter, caption, previous/next, thumbnails; Esc, arrows, focus return.'
KEYS = ['queue', 'grid', 'form', 'chart', 'mobile']
CAPS = ['The ranked queue, after triage rules.', 'Token library, dark mode.', 'Role templates replaced a 40-field form.', 'Median triage time over ten weeks.', 'Mobile review queue.']

def lb(inline=True, idx=1):
    k = KEYS[idx]
    thumbs = ''.join(f'<li><button type="button" class="pm-thumb pm-thumb--sm" data-i="{i}"{" aria-current=\"true\"" if i == idx else ""} aria-label="Image {i+1} of 5"><img src="{IMG[kk]}" alt="" width="112" height="112"><span class="pm-thumb__check" aria-hidden="true"></span></button></li>' for i, kk in enumerate(KEYS))
    tag = 'div' if inline else 'dialog'
    cls = 'pm-lightbox pm-lightbox--inline' if inline else 'pm-lightbox'
    role = ' role="dialog" aria-modal="false"' if inline else ''
    return (f'<{tag} class="{cls}" data-theme="dark" data-lb{role} aria-labelledby="lbc-{{T}}{{V}}">'
            f'<div class="pm-lightbox__bar"><span class="pm-lightbox__count" aria-live="polite"><span data-n>{idx+1}</span> of 5</span>'
            f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon" data-close aria-label="Close">{I["close"]}</button></div>'
            '<div class="pm-lightbox__stage">'
            f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-lightbox__prev" data-prev aria-label="Previous image">{I["prev"]}</button>'
            f'<figure class="pm-lightbox__figure" style="margin:0"><div class="pm-media pm-media--16x10 pm-media--contain" style="background:transparent"><img data-img src="{IMG[k]}" alt="{IMG_ALT[k]}"></div></figure>'
            f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-lightbox__next" data-next aria-label="Next image">{I["next"]}</button></div>'
            f'<div class="pm-lightbox__footer"><p class="pm-lightbox__caption" id="lbc-{{T}}{{V}}" data-cap>{CAPS[idx]}</p>'
            f'<div class="pm-lightbox__mobile-nav"><button type="button" class="pm-btn pm-btn--on-image" data-prev>{I["prev"]}Previous</button><button type="button" class="pm-btn pm-btn--on-image" data-next>Next{I["next"]}</button></div>'
            f'<ul class="pm-thumbs" aria-label="All images">{thumbs}</ul></div></{tag}>')

BODY = (h('Open state · rendered inline for the specimen') + frames(lb(), 1024, 375) +
        h('Live · opens a real modal dialog') +
        f'<button type="button" class="pm-btn pm-btn--secondary" data-open="dlg-{{T}}">{I["expand"]}Open lightbox</button>' +
        lb(False, 0).replace('data-lb', 'data-lb id="dlg-{T}"').replace('{V}', 'm'))
PAIRS_THEME = 'dark'
PAIRS = [('caption', '--color-text-on-image', '--color-overlay-backdrop', 4.5), ('counter', '--color-text-secondary', '--color-overlay-backdrop', 4.5),
         ('focus ring', '--color-focus-ring', '--color-overlay-backdrop', 3)]
SCRIPT = r'''
var LB_IMG=%s, LB_ALT=%s, LB_CAP=%s;
document.querySelectorAll('[data-lb]').forEach(function(L){
  var i=+L.querySelector('[data-n]').textContent-1;
  function show(n){i=(n+5)%%5;L.querySelector('[data-img]').src=LB_IMG[i];L.querySelector('[data-img]').alt=LB_ALT[i];L.querySelector('[data-cap]').textContent=LB_CAP[i];L.querySelector('[data-n]').textContent=i+1;
    L.querySelectorAll('.pm-thumb').forEach(function(t){if(+t.dataset.i===i)t.setAttribute('aria-current','true');else t.removeAttribute('aria-current');});}
  L.querySelectorAll('[data-prev]').forEach(function(b){b.addEventListener('click',function(){show(i-1);});});
  L.querySelectorAll('[data-next]').forEach(function(b){b.addEventListener('click',function(){show(i+1);});});
  L.querySelectorAll('.pm-thumb').forEach(function(t){t.addEventListener('click',function(){show(+t.dataset.i);});});
  L.addEventListener('keydown',function(e){if(e.key==='ArrowLeft'){show(i-1);}else if(e.key==='ArrowRight'){show(i+1);}});
  var c=L.querySelector('[data-close]');
  if(L.tagName==='DIALOG'){c.addEventListener('click',function(){L.close();});L.addEventListener('click',function(e){if(e.target===L)L.close();});}
});
document.querySelectorAll('[data-open]').forEach(function(b){var d=document.getElementById(b.dataset.open);
  b.addEventListener('click',function(){d.showModal();d.querySelector('[data-close]').focus();});
  d.addEventListener('close',function(){b.focus();});});
pmCheck();
''' % (str([IMG[k] for k in KEYS]).replace("'", '"'), str([IMG_ALT[k] for k in KEYS]).replace("'", '"'), str(CAPS).replace("'", '"'))
README = r'''
# Lightbox

A modal viewer for looking closely at project artifacts. It's always rendered in the dark scope, because imagery reads best on a dark ground, whatever the page theme.

## Anatomy
1. **Dialog**: native `<dialog class="pm-lightbox" data-theme="dark">` opened with `showModal()`, labelled by the caption (`aria-labelledby`).
2. **Backdrop**: `color-overlay-backdrop` (ink at 92%).
3. **Top bar**: counter "2 of 5" (`aria-live="polite"`, metadata voice, `color-text-secondary`) and a Close icon button.
4. **Stage**: Previous button · figure (`pm-media--contain`, never cropped) · Next button.
5. **Footer**: caption (`color-text-on-image`, `reading-max-width`), a mobile previous/next pair, and a thumbnail strip.

## Variants
- **Gallery** (default): counter, previous/next and thumbnails.
- **Single image**: omit the counter, previous/next and thumbnails. Close and caption only.
- **Inline** (`pm-lightbox--inline`): specimen and documentation only. Never use it as a real viewer.

## Sizes
Full viewport. The image is constrained to `content-max-width` (1200px) and contained in the remaining height. Bars use `space-2`/`space-4` padding. Controls are `control-height-md` 44px icon buttons. Thumbnails are sm (56px).

## States
| Element | States |
|---|---|
| Dialog | closed → open (fade over `motion-duration-base`, none with reduced motion) → closed |
| Prev / Next / Close | default · hover (1px inset ring) · focus-visible (3px ring, ≥7.83:1 on the backdrop) · active · disabled (at the ends of a non-looping set: `aria-disabled`) |
| Thumbnails | Thumbnail states. The current image is `aria-current="true"`. |
| Image | loading (sunken) · loaded · error (ImageContainer fallback with alt text) |

## Themes
Always dark-scoped, so light and dark pages show an identical viewer. That's deliberate: in light, the focus ring (`cobalt-600`) would be only about 2.3:1 on the backdrop. In the dark scope the ring is `dark-accent-hover`, at 7.83:1 even over white imagery. Caption text: 14.18:1.

## Responsive behavior
- **≥768px container:** side previous/next buttons and a thumbnail strip.
- **<768px:** the image goes full-bleed, side arrows and thumbnails hide, and "Previous / Next" text buttons appear under the caption (larger, labelled targets). Support swipe as an addition, never as the only way.

## Accessibility
- Native `<dialog>` + `showModal()` handles focus containment, Esc to close and inert background. Focus moves to Close on open and **returns to the trigger** on close.
- Left/Right arrows navigate. Tab cycles through the controls. The counter is a polite live region, so changes are announced.
- Each image keeps real alt text, and the caption labels the dialog.
- Clicking the backdrop closes it, but there's always a visible Close button.
- Don't autoplay slideshows.

## Token dependencies
`color-overlay-backdrop` `color-text-on-image` `color-text-secondary` `color-focus-ring` (dark scope) `color-selected-indicator` · `content-max-width` `reading-max-width` · `control-height-md` · `space-2|3|4` · `radius-md` `radius-lg` · `type-body-sm` `type-caption` · `font-meta` · `motion-duration-base` `motion-ease` · Button (on-image), Thumbnail, ImageContainer
'''
