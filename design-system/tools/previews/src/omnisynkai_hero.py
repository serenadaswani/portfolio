"""OmniSynkAI case-study hero: one-click AI autofill on the shipped listing page, as a short loop.

Built from Serena's final prototype exports, so the layout, buttons and spacing are exactly as designed: the empty
listing (01) is the base, and every part that changes is a crop of the export that shows it, laid at its exact place
(regions measured from the 2880px exports, in a 1000 x 740 grid). On OmniSynkAI's brand gradient, no copy.
One CSS timeline (10s, looped):
  1. The title types in and the category fills.
  2. The cursor clicks the AI autofill icon, which simply brings up the loading scrim and the "Filling out your
     listing" dialog (the loading screen, 02, fades in; no click effects).
  3. The dialog closes and skeleton content appears inside each input: description lines, the media slots, the brand
     and tags fields (neutral grey with a soft sweep).
  4. Each skeleton resolves into the real AI content (crops of 03): description lines write in, photos appear one by
     one, the brand and tags chips land; the title bar becomes "Listing Autofilled" with Publish on. Hold, then reset.
Final frame (reduced motion, no JS): the autofilled listing (03). Starts when in view, the tab is visible and the
screens have decoded; pauses off screen and on Pause (WCAG 2.2.2).
"""

V = '?v=2'
W, H = 1000, 740   # the grid every region is measured in (the exports at 1000 px wide)

def _box(x, y, w, h):
    return f'left:{x / W * 100:.3f}%;top:{y / H * 100:.3f}%;width:{w / W * 100:.3f}%;height:{h / H * 100:.3f}%'

def _crop(cls, src, x, y, w, h, dx=0):
    """A region (x, y, w, h) of an export, placed at the same spot on the page (or dx to the right)."""
    bs = W / w * 100
    px = x / (W - w) * 100 if w < W else 0
    py = y / (H - h) * 100 if h < H else 0
    return (f'<span class="oh-c {cls}" style="{_box(x + dx, y, w, h)};background-image:url({src});'
            f'background-size:{bs:.3f}% auto;background-position:{px:.3f}% {py:.3f}%"></span>')

def _bar(cls, x, y, w, h):
    return f'<span class="oh-sk {cls}" style="{_box(x, y, w, h)}"></span>'

CURSOR = ('<svg class="oh-cursor" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
          '<path d="M4 2.5 L4 19.5 L8.6 15.4 L11.4 21.6 L14.2 20.4 L11.5 14.3 L17.6 14.1 Z" fill="#FFFFFF" stroke="#111827" stroke-width="1.4" stroke-linejoin="round"/></svg>')

# Regions (1000 x 740 grid)
DESC = [(95, 263, 650, 18), (95, 283, 650, 15), (95, 298, 650, 14), (95, 312, 650, 30)]      # 03 description, line by line
PHOTOS = [(103, 460.5, 164, 163.5)] + [(x, y, 79.5, 79) for y in (460.5, 545) for x in (274, 360, 446, 532)]  # 03 media
CHIPS = [(114, 688.5, 52.5, 17), (436.5, 688.5, 54.5, 17), (496, 688.5, 57, 17)]          # 03 brand chip, tag chips
SK_DESC = [(97, 268, 520, 8), (110, 288, 470, 7), (110, 302, 520, 7), (110, 316, 560, 7), (110, 330, 260, 7)]
SK_FIELDS = [(114, 690.5, 52.5, 13), (436.5, 690.5, 116.5, 13)]
# Typed values: 03's field text (unscrimmed), shifted onto 01's fields (01 title input starts at 260, 03's at 240;
# 01 category at 478, 03's at 465)
TYPE_TITLE = (246, 152, 150, 20, 20)
TYPE_CAT = (471, 152, 150, 20, 13)

def html(base='assets/screens', I=None):
    s1, s2, s3 = (f'{base}/{f}{V}' for f in ('01-empty-listing.jpg', '02-autofill-in-progress.jpg', '03-listing-autofilled.jpg'))
    parts = [
        f'<img class="oh-scr" src="{s1}" width="2000" height="1480" alt="" loading="eager" decoding="async">',
        _crop('oh-type', s3, *TYPE_TITLE[:4], dx=TYPE_TITLE[4]),
        _crop('oh-cat', s3, *TYPE_CAT[:4], dx=TYPE_CAT[4]),
        '<span class="oh-mbg" style="' + _box(100, 456, 636, 172) + '"></span>',
        _crop('oh-slots', s3, 614, 456, 120, 172),
        '<span class="oh-sks">' + ''.join(_bar('oh-sk--d', *b) for b in SK_DESC)
        + ''.join(_bar('oh-sk--m', *b) for b in PHOTOS) + ''.join(_bar('oh-sk--f', *b) for b in SK_FIELDS) + '</span>',
        ''.join(_crop(f'oh-d oh-d--{i + 1}', s3, *b) for i, b in enumerate(DESC)),
        ''.join(_crop(f'oh-p oh-p--{i + 1}', s3, *b) for i, b in enumerate(PHOTOS)),
        ''.join(_crop(f'oh-k oh-k--{i + 1}', s3, *b) for i, b in enumerate(CHIPS)),
        _crop('oh-tb', s3, 89, 108, 895, 88),
        f'<img class="oh-scr oh-s2" src="{s2}" width="2000" height="1480" alt="" loading="eager" decoding="async">',
        f'<img class="oh-scr oh-final" src="{s3}" width="2000" height="1480" alt="" loading="eager" decoding="async">',
        CURSOR,
    ]
    pause = I['pause'] if I else ''
    play = I['play'] if I else ''
    return ('  <div class="cs-hero-well oh-wrap">'
            '<div class="pm-media pm-media--21x9 oh" data-oh role="img" '
            'aria-label="OmniSynkAI AI autofill on the listing page: a seller types a title and a category and clicks the AI autofill icon; a loading dialog appears, '
            'then skeleton content fills each field and resolves into the AI-written description, product photos, brand and tags, and the bar reads Listing Autofilled.">'
            f'<div class="oh-stage"><div class="oh-app">{"".join(parts)}</div></div></div>'
            '<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-btn--sm oh-toggle" aria-pressed="false" aria-label="Pause animation" data-oh-toggle hidden>'
            f'<span class="oh-ic oh-ic--pause">{pause}</span><span class="oh-ic oh-ic--play" hidden>{play}</span></button></div>\n'
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("oh--anim")})(document.querySelector("[data-oh]"))</script>\n')

CSS = r"""
/* ===== OmniSynkAI hero (omnisynkai_hero.py): one-click AI autofill on the shipped listing page ===== */
.oh-wrap { position: relative; }
.oh { container-type: inline-size; background: radial-gradient(90% 120% at 50% 110%, rgb(255 255 255 / 22%) 0%, rgb(255 255 255 / 0%) 60%), linear-gradient(160deg, #4745B0 0%, #5B43E8 40%, #755CFB 75%, #9B94E0 100%); }
.oh-stage { position: absolute; inset: 0; display: grid; place-items: center; }
.oh-app { position: relative; width: 54cqw; aspect-ratio: 1000 / 740; border-radius: .6cqw; overflow: hidden; background: #F5F5F7; isolation: isolate;
  box-shadow: 0 2cqw 5cqw rgb(20 12 70 / 35%), 0 0 0 1px rgb(255 255 255 / 30%); }
@container (max-width: 599px) { .oh-app { width: 70cqw; border-radius: .9cqw; } }
.oh-scr { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }
.oh-c { position: absolute; background-repeat: no-repeat; }
.oh-s2 { opacity: 0; }
.oh-final { opacity: 1; }
/* skeletons: neutral grey with a soft sweep */
.oh-sks { position: absolute; inset: 0; opacity: 0; }
.oh-sk { position: absolute; border-radius: .25cqw; background: linear-gradient(90deg, #E6E8EC 0%, #F1F2F5 45%, #E6E8EC 90%); background-size: 300% 100%; }
.oh-sk--m { border-radius: .45cqw; }
.oh-mbg { position: absolute; background: #FFFFFF; opacity: 0; }
.oh-cursor { position: absolute; left: 92%; top: 82%; width: 3cqw; height: 3cqw; opacity: 0; filter: drop-shadow(0 .2cqw .4cqw rgb(0 0 0 / 25%)); pointer-events: none; }

/* Pause / Play, outside the image role */
.oh-toggle { position: absolute; right: var(--space-3); bottom: var(--space-3); z-index: 2; }
.oh-toggle[hidden], .oh-ic[hidden] { display: none; }
.oh-ic { display: contents; }

/* ---- The loop (10s). The rules above are the final frame (03 on top); with motion, the overlays build it, held
   paused until the hero is ready and in view. ---- */
.oh--anim .oh-final { opacity: 0; }
.oh--anim .oh-app * { animation-duration: 10s; animation-iteration-count: infinite; animation-fill-mode: both; animation-timing-function: ease-in-out; animation-play-state: paused; }
.oh--anim.is-play:not(.is-paused) .oh-app * { animation-play-state: running; }
.oh--anim .oh-type { animation-name: oh-type; }
.oh--anim .oh-cat { animation-name: oh-cat; }
.oh--anim .oh-cursor { animation-name: oh-cursor; }
.oh--anim .oh-s2 { animation-name: oh-s2; }
.oh--anim .oh-sks { animation-name: oh-sks; }
.oh--anim .oh-sk { animation: oh-sweep 1.4s linear infinite; }
.oh--anim .oh-mbg, .oh--anim .oh-slots { animation-name: oh-mbg; }
.oh--anim .oh-d--1 { animation-name: oh-d1; } .oh--anim .oh-d--2 { animation-name: oh-d2; } .oh--anim .oh-d--3 { animation-name: oh-d3; } .oh--anim .oh-d--4 { animation-name: oh-d4; }
.oh--anim .oh-p { animation-name: oh-p; }
.oh--anim .oh-p--2, .oh--anim .oh-p--6 { animation-name: oh-p2; } .oh--anim .oh-p--3, .oh--anim .oh-p--7 { animation-name: oh-p3; }
.oh--anim .oh-p--4, .oh--anim .oh-p--8 { animation-name: oh-p4; } .oh--anim .oh-p--5, .oh--anim .oh-p--9 { animation-name: oh-p5; }
.oh--anim .oh-k { animation-name: oh-k; } .oh--anim .oh-k--2 { animation-name: oh-k2; } .oh--anim .oh-k--3 { animation-name: oh-k3; }
.oh--anim .oh-tb { animation-name: oh-tb; }

@keyframes oh-type { 0%, 5% { opacity: 1; clip-path: inset(0 100% 0 0); animation-timing-function: steps(15, end); } 16%, 95% { opacity: 1; clip-path: inset(0 0 0 0); } 98%, 100% { opacity: 0; clip-path: inset(0 0 0 0); } }
@keyframes oh-cat { 0%, 17% { opacity: 0; } 19%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
/* the cursor moves to the AI autofill icon and clicks; the click just opens the loading scrim */
@keyframes oh-cursor { 0%, 20% { opacity: 0; left: 92%; top: 82%; } 22% { opacity: 1; left: 90%; top: 74%; } 28.5%, 30% { opacity: 1; left: 81.2%; top: 19.6%; } 32%, 100% { opacity: 0; left: 81.2%; top: 19.6%; } }
@keyframes oh-s2 { 0%, 30% { opacity: 0; } 31%, 43% { opacity: 1; } 45%, 100% { opacity: 0; } }
@keyframes oh-sks { 0%, 44% { opacity: 0; } 46%, 53% { opacity: 1; } 62%, 100% { opacity: 0; } }
@keyframes oh-sweep { from { background-position: 100% 0; } to { background-position: -50% 0; } }
@keyframes oh-mbg { 0%, 44% { opacity: 0; } 46%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-d1 { 0%, 53% { clip-path: inset(0 100% 0 0); opacity: 1; } 58%, 95% { clip-path: inset(0 0 0 0); opacity: 1; } 98%, 100% { clip-path: inset(0 0 0 0); opacity: 0; } }
@keyframes oh-d2 { 0%, 55% { clip-path: inset(0 100% 0 0); opacity: 1; } 59.5%, 95% { clip-path: inset(0 0 0 0); opacity: 1; } 98%, 100% { clip-path: inset(0 0 0 0); opacity: 0; } }
@keyframes oh-d3 { 0%, 57% { clip-path: inset(0 100% 0 0); opacity: 1; } 61%, 95% { clip-path: inset(0 0 0 0); opacity: 1; } 98%, 100% { clip-path: inset(0 0 0 0); opacity: 0; } }
@keyframes oh-d4 { 0%, 59% { clip-path: inset(0 100% 0 0); opacity: 1; } 63.5%, 95% { clip-path: inset(0 0 0 0); opacity: 1; } 98%, 100% { clip-path: inset(0 0 0 0); opacity: 0; } }
@keyframes oh-p { 0%, 54% { opacity: 0; } 57%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-p2 { 0%, 56% { opacity: 0; } 59%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-p3 { 0%, 58% { opacity: 0; } 61%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-p4 { 0%, 60% { opacity: 0; } 63%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-p5 { 0%, 62% { opacity: 0; } 65%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-k { 0%, 62% { opacity: 0; } 65%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-k2 { 0%, 64% { opacity: 0; } 67%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-k3 { 0%, 65.5% { opacity: 0; } 68.5%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
@keyframes oh-tb { 0%, 67% { opacity: 0; } 70%, 95% { opacity: 1; } 98%, 100% { opacity: 0; } }
"""

JS = r"""
  // OmniSynkAI hero: loops while in view and the tab is visible, once the screens have decoded; Pause/Play (WCAG 2.2.2)
  (function () {
    var hero = document.querySelector('[data-oh].oh--anim'); if (!hero) return;
    var btn = document.querySelector('[data-oh-toggle]'), inView = false, ready = false, user = false;
    function sync() {
      var run = ready && inView && document.visibilityState === 'visible' && !user;
      if (ready) hero.classList.add('is-play');
      hero.classList.toggle('is-paused', !run);
      btn.setAttribute('aria-pressed', String(user)); btn.setAttribute('aria-label', user ? 'Play animation' : 'Pause animation');
      btn.querySelector('.oh-ic--pause').hidden = user; btn.querySelector('.oh-ic--play').hidden = !user;
    }
    btn.hidden = false;
    btn.addEventListener('click', function () { user = !user; sync(); });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { inView = es[0].isIntersecting; sync(); }, { threshold: .25 }).observe(hero);
    else inView = true;
    document.addEventListener('visibilitychange', sync);
    var imgs = [].map.call(hero.querySelectorAll('img'), function (i) { return i.decode ? i.decode().catch(function () {}) : 0; });
    Promise.race([Promise.all(imgs), new Promise(function (r) { setTimeout(r, 2500); })]).then(function () { ready = true; sync(); });
  })();
"""
