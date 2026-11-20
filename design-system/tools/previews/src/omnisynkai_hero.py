"""OmniSynkAI hero: one-click AI autofill on the full listing screen, on a laptop (14s).

Serena's final prototype screens (2880px Figma exports) sit in a laptop frame; a camera inside the screen does the zooms,
so each step is seen up close and in the context of the whole page:
  1. Empty listing (screen 01). The camera zooms to Title and Product category as they fill, then glides to the AI
     autofill icon, which the cursor clicks.
  2. Loading (screen 02, scrim + dialog), once the camera is back out. The dialog's AI icon is redrawn in SVG so its two
     sparkles merge into one star and split back (as in the first-concept video).
  3-4. Skeletons in every section autofill writes to (Description, Media, Brand and Tags). The camera visits each as its
     content arrives: description lines with a clean per-line purple highlight, the product photos, the brand and tag
     chips, then the title bar turning into "Listing Autofilled"; then the whole page.
The finished state is screen 03 exactly: the only regions that differ from 01 (measured by pixel diff) are the bar, the
description, the media grid and the chips, and each is a crop of 03 at its measured place (1000 x 740 grid). Final frame
(reduced motion, no JS): the finished listing. The case-study hero loops with Pause/Play (WCAG 2.2.2); the landing card
plays once.
"""

V = '?v=5'
W, H = 1000, 740.28   # export grid (2880 x 2132 px at 1000 wide)
SCREEN = (W, H)

SPRITES = {   # (x, y, w, h) in the grid, from the pixel crops (2.88 px per unit); files in omnisynkai/assets/hero/
    '01-screen': (0, 0, W, H), '02-screen': (0, 0, W, H),
    '03-bar': (87.8472, 106.9444, 897.2222, 88.8889), '03-desc': (92.7083, 260.7639, 654.1667, 84.375),
    '03-chips': (111.8056, 685.7639, 444.0972, 22.2222), '03-media': (97.9167, 454.8611, 640.2778, 177.0833),
}

def _place(cls, sp, sbox, dbox, frame=SCREEN):
    """Crop sbox (grid) of sprite sp = (url, region) into dbox (frame grid)."""
    url, (rx, ry, rw, rh) = sp
    sx, sy, sw, sh = sbox
    assert rx - .01 <= sx and sx + sw <= rx + rw + .01 and ry - .01 <= sy and sy + sh <= ry + rh + .01, (cls, sbox)
    dx, dy, dw, dh = dbox
    fw, fh = frame
    bs = rw / sw * 100
    px = (sx - rx) / (rw - sw) * 100 if rw - sw > .01 else 0
    py = (sy - ry) / (rh - sh) * 100 if rh - sh > .01 else 0
    return (f'<span class="oh-c {cls}" style="left:{dx / fw * 100:.3f}%;top:{dy / fh * 100:.3f}%;width:{dw / fw * 100:.3f}%;height:{dh / fh * 100:.3f}%;'
            f'background-image:url({url});background-size:{bs:.3f}% auto;background-position:{px:.3f}% {py:.3f}%"></span>')

def _rect(cls, b, frame=SCREEN):
    x, y, w, h = b
    fw, fh = frame
    return f'<span class="{cls}" style="left:{x / fw * 100:.3f}%;top:{y / fh * 100:.3f}%;width:{w / fw * 100:.3f}%;height:{h / fh * 100:.3f}%"></span>'

CURSOR = ('<svg class="oh-cursor" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
          '<path d="M4 2.5 L4 19.5 L8.6 15.4 L11.4 21.6 L14.2 20.4 L11.5 14.3 L17.6 14.1 Z" fill="#FFFFFF" stroke="#111827" stroke-width="1.4" stroke-linejoin="round"/></svg>')

# ---- regions measured from the exports ----
BAR = (89, 108.3, 895, 86.8)
SPARK = (361, 292, 20, 20)                        # 02 dialog's AI icon (redrawn so it can animate)
TYPE_TITLE = (252, 152, 80, 20, 20)               # 03 field text (x, y, w, h), shifted dx onto 01's title input
TYPE_CAT = (477, 152, 44, 20, 13)    # crops end at the text, so each typing step is one character
DESC_BANDS = [(263, 284), (284, 300.5), (300.5, 314.5), (314.5, 328.3), (328.3, 343)]
HILITE = [(95, 268, 532, 12.3), (109, 287.5, 439.2, 12.3), (109, 301.4, 558.3, 12.3), (109, 315.3, 631, 12.3), (109, 329.2, 144.4, 12.3)]
CHIPS = [(114, 688.5, 52.5, 17), (436.5, 688.5, 54.5, 17), (496, 688.5, 57, 17)]
SK_DESC = [(97, 270, 520, 8), (110, 290, 430, 7.5), (110, 304, 540, 7.5), (110, 318, 600, 7.5), (110, 332, 150, 7.5)]
SK_FIELDS = [(114, 690.5, 52.5, 13), (436.5, 690.5, 116.5, 13)]
MEDIA = (97.9167, 454.8611, 640.2778, 177.0833)  # 03's photo grid (the whole media body, so the result is exactly 03)
MEDIA_COVER = (100, 457, 636, 170)              # 01's empty slots, hidden under the media skeleton
MEDIA_SLOTS = (616, 457, 118, 170)              # 03's two empty upload slots (kept in the skeleton)
TILES = [(103.1, 460.1, 163.9, 163.9)] + [(x, y, 79.2, 78.5) for y in (460.1, 545.5) for x in (274, 360.1, 446.2, 532.3)]

STAR = 'M0 -.94C.07 -.42 .42 -.07 .94 0C.42 .07 .07 .42 0 .94C-.07 .42 -.42 .07 -.94 0C-.42 -.07 -.07 -.42 0 -.94Z'

def _spark(s2, uid):
    """The dialog's two-star AI icon as SVG, over a patch of the same screen's blank dialog (so the paper matches)."""
    x, y, w, h = SPARK
    patch = _place('oh-patch', s2, (612, y, w, h), (x, y, w, h))
    star = f'<path d="{STAR}" fill="url(#oh-sg{uid})" stroke="url(#oh-sg{uid})" stroke-width=".16" stroke-linejoin="round"/>'
    pos = f'left:{x / W * 100:.3f}%;top:{y / H * 100:.3f}%;width:{w / W * 100:.3f}%;height:{h / H * 100:.3f}%'
    return patch + (f'<span class="oh-spark" style="{pos}"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false">'
            f'<defs><linearGradient id="oh-sg{uid}" x1="0" x2="1" y1="0" y2="0">'
            '<stop offset="0" stop-color="#5B8CFF"/><stop offset=".48" stop-color="#A566FF"/><stop offset="1" stop-color="#AC6AFF"/>'
            f'</linearGradient></defs><g class="oh-st oh-st--b">{star}</g><g class="oh-st oh-st--s">{star}</g></svg></span>')


def _stage(base, uid):
    """The monitor with the full screen and its camera; shared by the case-study hero and the landing card."""
    sp = {n: (f'{base}/{n}.jpg{V}', r) for n, r in SPRITES.items()}
    tx, ty, tw, th, tdx = TYPE_TITLE
    cx, cy, cw, ch, cdx = TYPE_CAT
    typed = (_place('oh-type', sp['03-bar'], (tx, ty, tw, th), (tx + tdx, ty, tw, th))
             + _place('oh-cat', sp['03-bar'], (cx, cy, cw, ch), (cx + cdx, cy, cw, ch)))
    lines = ''.join(_place(f'oh-d oh-d--{i + 1}', sp['03-desc'], (95, y0, 650, y1 - y0), (95, y0, 650, y1 - y0))
                    for i, (y0, y1) in enumerate(DESC_BANDS))
    # clean highlight per measured line: 'screen' turns black text purple, 'multiply' tints the paper (siblings, so both blend)
    hl = ''.join(_rect(f'oh-hl oh-hl--t oh-d--{i + 1}', b) + _rect(f'oh-hl oh-hl--f oh-d--{i + 1}', b) for i, b in enumerate(HILITE))
    chips = ''.join(_place(f'oh-k oh-k--{i + 1}', sp['03-chips'], b, b) for i, b in enumerate(CHIPS))
    skm = ('<span class="oh-skm">' + _rect('oh-skw', MEDIA_COVER) + _place('oh-slots', sp['03-media'], MEDIA_SLOTS, MEDIA_SLOTS)
           + ''.join(_rect('oh-sk', t) for t in TILES) + '</span>')
    s2 = sp['02-screen']
    cam = ('<div class="oh-cam">'
           + _place('oh-scr', sp['01-screen'], (0, 0, W, H), (0, 0, W, H))
           + '<span class="oh-skd">' + ''.join(_rect('oh-sk', b) for b in SK_DESC) + '</span>' + skm
           + '<span class="oh-skf">' + ''.join(_rect('oh-sk', b) for b in SK_FIELDS) + '</span>'
           + '<div class="oh-ov">' + typed + _place('oh-bar', sp['03-bar'], BAR, BAR) + lines + hl
           + _place('oh-media', sp['03-media'], MEDIA, MEDIA) + chips + '</div>'
           + '<div class="oh-s2">' + _place('oh-scr', s2, (0, 0, W, H), (0, 0, W, H)) + _spark(s2, uid) + '</div>'
           + '</div>')
    return ('<div class="od" aria-hidden="true"><div class="od-lid"><span class="od-cam-dot"></span><div class="od-screen">' + cam + CURSOR + '</div></div>'
            '<span class="od-base"></span></div>')


def html(base='assets/hero', I=None):
    pause = I['pause'] if I else ''
    play = I['play'] if I else ''
    return ('  <div class="cs-hero-well oh-wrap">'
            '<div class="pm-media pm-media--21x9 oh" data-oh role="img" '
            'aria-label="OmniSynkAI AI autofill on the listing page, shown on a laptop: a seller types a title and a category, and the view zooms to the AI autofill icon, which they click; '
            'a loading dialog appears; skeletons fill the description, media and brand and tags fields; then the AI-written description, highlighted in purple, '
            'the product photos and the brand and tag chips appear, and the title bar reads Listing Autofilled.">'
            + _stage(base, 'h') + '</div>'
            '<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-btn--sm oh-toggle" aria-pressed="false" aria-label="Pause animation" data-oh-toggle hidden>'
            f'<span class="oh-ic oh-ic--pause">{pause}</span><span class="oh-ic oh-ic--play" hidden>{play}</span></button></div>\n'
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("oh--anim")})(document.querySelector("[data-oh]"))</script>\n')


def card(base='omnisynkai/assets/hero', uid='c'):
    """The same animation in the landing card's media spot: rests on step 4 complete, plays once each time the card
    becomes the active card."""
    return '<div class="oh oh--card" data-ohc aria-hidden="true">' + _stage(base, uid) + '</div>'

CSS = r"""
/* ===== OmniSynkAI hero (omnisynkai_hero.py): the full listing screen on a laptop, with a camera inside the screen ===== */
.oh-wrap { position: relative; }
.oh { --u: .946cqw; container-type: inline-size; overflow: hidden; background: radial-gradient(90% 120% at 50% 110%, rgb(255 255 255 / 22%) 0%, rgb(255 255 255 / 0%) 60%), linear-gradient(160deg, #4745B0 0%, #5B43E8 40%, #755CFB 75%, #9B94E0 100%); }
/* Laptop, front view (project art, like Procense's tablet): a 52-unit lid with a thin black bezel (no outline ring), the screen at the export's ratio, and a wider aluminium base with the thumb notch. 58 x 40.76 units. */
.od { position: absolute; left: 50%; top: 50%; width: calc(58 * var(--u)); height: calc(40.76 * var(--u)); transform: translate(-50%, -50%); }
.od-lid { position: absolute; left: calc(3 * var(--u)); top: 0; width: calc(52 * var(--u)); height: calc(39.56 * var(--u)); border-radius: calc(1.8 * var(--u)) calc(1.8 * var(--u)) calc(.3 * var(--u)) calc(.3 * var(--u)); background: #0B0D12;
  box-shadow: 0 calc(2.4 * var(--u)) calc(6 * var(--u)) rgb(0 0 0 / 32%); }
.od-cam-dot { position: absolute; left: 50%; top: calc(.42 * var(--u)); width: calc(.34 * var(--u)); aspect-ratio: 1; border-radius: 50%; transform: translateX(-50%); background: #23272F; }
.od-screen { position: absolute; left: calc(.9 * var(--u)); top: calc(1.1 * var(--u)); width: calc(50.2 * var(--u)); aspect-ratio: 1000 / 740.28; overflow: hidden; border-radius: calc(.2 * var(--u)); background: #FFFFFF; }
.od-base { position: absolute; left: 0; top: calc(39.56 * var(--u)); width: 100%; height: calc(1.2 * var(--u)); border-radius: calc(.15 * var(--u)) calc(.15 * var(--u)) calc(1.6 * var(--u)) calc(1.6 * var(--u)) / calc(.15 * var(--u)) calc(.15 * var(--u)) calc(1 * var(--u)) calc(1 * var(--u));
  background: linear-gradient(#E4E6EB, #BEC2CA 65%, #9298A3); box-shadow: 0 calc(1.2 * var(--u)) calc(2.6 * var(--u)) rgb(0 0 0 / 28%); }
.od-base::before { content: ""; position: absolute; left: 50%; top: 0; width: calc(9 * var(--u)); height: calc(.5 * var(--u)); transform: translateX(-50%); border-radius: 0 0 calc(.6 * var(--u)) calc(.6 * var(--u)); background: #A9AEB7; }
.oh-cam, .oh-ov, .oh-s2, .oh-skd, .oh-skm, .oh-skf { position: absolute; inset: 0; }
.oh-cam { transform-origin: 50% 50%; will-change: transform; }
.oh-c, .oh-sk, .oh-skw, .oh-hl { position: absolute; }
.oh-c { background-repeat: no-repeat; }
.oh-s2, .oh-skd, .oh-skm, .oh-skf { opacity: 0; }
.oh-skw { background: #FFFFFF; }
.oh-sk { border-radius: .5%/.7%; background: linear-gradient(90deg, #E6E8EC 0%, #F1F2F5 45%, #E6E8EC 90%); background-size: 300% 100%; }
.oh-hl { border-radius: 2px; }
.oh-hl--t { background: #9447E0; mix-blend-mode: screen; }
.oh-hl--f { background: #F0E8F7; mix-blend-mode: multiply; }
.oh-spark { position: absolute; }
.oh-spark svg { display: block; width: 100%; height: 100%; overflow: visible; }
.oh-st { transform-box: view-box; transform-origin: 0 0; }
.oh-st--b { transform: translate(6.9px, 12.2px) scale(5.4, 5.9); }
.oh-st--s { transform: translate(15.05px, 4.9px) scale(3.1, 3.5); }
.oh-cursor { position: absolute; left: 55.97%; top: 45.16%; width: 4.5%; aspect-ratio: 1; opacity: 0; filter: drop-shadow(0 1px 2px rgb(0 0 0 / 25%)); pointer-events: none; transform-origin: 17% 10%; }

/* Pause / Play, outside the image role */
.oh-toggle { position: absolute; right: var(--space-3); bottom: var(--space-3); z-index: 2; }
.oh-toggle[hidden], .oh-ic[hidden] { display: none; }
.oh-ic { display: contents; }

/* ---- The timeline (14s). The rules above are the final frame (screen 03, with the highlight); with motion every
   layer runs from its 0% frame, held paused until ready and in view. One ease-in-out throughout. ---- */
.oh--anim * { animation-duration: 14s; animation-iteration-count: infinite; animation-fill-mode: both; animation-timing-function: cubic-bezier(.65, 0, .35, 1); animation-play-state: paused; }
.oh--anim.is-play:not(.is-paused) * { animation-play-state: running; }
.oh--anim .oh-cam { animation-name: oh-cam; }
.oh--anim .oh-ov { animation-name: oh-ov; }
.oh--anim .oh-type { animation-name: oh-type; }
.oh--anim .oh-cat { animation-name: oh-cat; }
.oh--anim .oh-cursor { animation-name: oh-cursor; }
.oh--anim .oh-s2 { animation-name: oh-s2; }
.oh--anim .oh-st--b { animation-name: oh-stb; }
.oh--anim .oh-st--s { animation-name: oh-sts; }
.oh--anim .oh-skd { animation-name: oh-skd; }
.oh--anim .oh-skm { animation-name: oh-skm; }
.oh--anim .oh-skf { animation-name: oh-skf; }
.oh--anim .oh-sk { animation: oh-sweep 1.6s linear infinite; }
.oh--anim .oh-bar { animation-name: oh-bar; }
.oh--anim .oh-media { animation-name: oh-media; }
.oh--anim .oh-d--1 { animation-name: oh-d1; } .oh--anim .oh-d--2 { animation-name: oh-d2; } .oh--anim .oh-d--3 { animation-name: oh-d3; }
.oh--anim .oh-d--4 { animation-name: oh-d4; } .oh--anim .oh-d--5 { animation-name: oh-d5; }
.oh--anim .oh-k--1 { animation-name: oh-k1; } .oh--anim .oh-k--2 { animation-name: oh-k2; } .oh--anim .oh-k--3 { animation-name: oh-k3; }

/* Camera (scale, then the shift that centres a point of the screen): the whole page -> Title and Product category
   (507, 200) x1.9 -> AI icon (790, 165) x2.4 -> out for loading -> Description (360, 285) x1.8 -> down to Media
   (418, 430) x1.45 -> down to Brand and Tags (418, 488.5) x1.47 -> up to the Listing Autofilled bar (395, 218) x1.7 ->
   the whole page. Media and Brand/Tags views show their sections' full width (no left or right edge cut off). */
@keyframes oh-cam { 0%, 4% { transform: scale(1) translate(0, 0); } 9.5%, 21% { transform: scale(1.9) translate(-.7%, 22.98%); } 26.5%, 30.5% { transform: scale(2.4) translate(-29%, 27.71%); }
  36%, 49% { transform: scale(1) translate(0, 0); } 54%, 61.5% { transform: scale(1.8) translate(14%, 11.5%); } 65.5%, 69% { transform: scale(1.45) translate(8.2%, -8.09%); }
  72.5%, 75.5% { transform: scale(1.47) translate(8.2%, -15.99%); } 80%, 84% { transform: scale(1.7) translate(10.5%, 20.55%); } 89.5%, 100% { transform: scale(1) translate(0, 0); } }
/* 1. Title, then Product category, type in (one character at a time, the same way) while zoomed in; the cursor glides to the AI autofill icon and clicks it */
@keyframes oh-type { 0%, 9.5% { clip-path: inset(0 100% 0 0); animation-timing-function: steps(15, end); } 15%, 100% { clip-path: inset(0 0 0 0); } }
@keyframes oh-cat { 0%, 15.5% { clip-path: inset(0 100% 0 0); animation-timing-function: steps(8, end); } 18.5%, 100% { clip-path: inset(0 0 0 0); } }
@keyframes oh-cursor { 0%, 22% { opacity: 0; left: 72%; top: 84%; transform: none; } 24% { opacity: 1; } 28.5% { opacity: 1; left: 55.97%; top: 45.16%; transform: none; }
  29.2% { transform: scale(.85); } 30% { opacity: 1; transform: none; } 32%, 100% { opacity: 0; left: 55.97%; top: 45.16%; transform: none; } }
/* 2. The loading screen (scrim + dialog) once the camera is back out; the icon's sparkles merge and split */
@keyframes oh-s2 { 0%, 34.5% { opacity: 0; } 37.5%, 49% { opacity: 1; } 52%, 100% { opacity: 0; } }
@keyframes oh-stb { 0%, 39.5% { transform: translate(6.9px, 12.2px) scale(5.4, 5.9); } 42% { transform: translate(10px, 10.4px) scale(6.3, 6.7); } 43.5% { transform: translate(10px, 10.4px) scale(6.7, 7.1); } 45% { transform: translate(10px, 10.4px) scale(6.3, 6.7); } 47.5%, 100% { transform: translate(6.9px, 12.2px) scale(5.4, 5.9); } }
@keyframes oh-sts { 0%, 39.5% { opacity: 1; transform: translate(15.05px, 4.9px) scale(3.1, 3.5); } 41.5% { opacity: .8; } 42%, 45% { opacity: 0; transform: translate(10px, 10.4px) scale(1.2, 1.3); } 45.5% { opacity: .8; } 47.5%, 100% { opacity: 1; transform: translate(15.05px, 4.9px) scale(3.1, 3.5); } }
/* 3-4. Skeletons in the sections autofill writes to, each giving way to its content as the camera reaches it */
@keyframes oh-skd { 0%, 34% { opacity: 0; } 36%, 54.5% { opacity: 1; } 57.5%, 100% { opacity: 0; } }
@keyframes oh-skm { 0%, 34% { opacity: 0; } 36%, 65% { opacity: 1; } 68%, 100% { opacity: 0; } }
@keyframes oh-skf { 0%, 34% { opacity: 0; } 36%, 71.5% { opacity: 1; } 74%, 100% { opacity: 0; } }
@keyframes oh-sweep { from { background-position: 100% 0; } to { background-position: -50% 0; } }
@keyframes oh-d1 { 0%, 54.5% { opacity: 0; transform: translateY(20%); } 57.5%, 100% { opacity: 1; transform: none; } }
@keyframes oh-d2 { 0%, 55.6% { opacity: 0; transform: translateY(20%); } 58.6%, 100% { opacity: 1; transform: none; } }
@keyframes oh-d3 { 0%, 56.7% { opacity: 0; transform: translateY(20%); } 59.7%, 100% { opacity: 1; transform: none; } }
@keyframes oh-d4 { 0%, 57.8% { opacity: 0; transform: translateY(20%); } 60.8%, 100% { opacity: 1; transform: none; } }
@keyframes oh-d5 { 0%, 58.9% { opacity: 0; transform: translateY(20%); } 61.9%, 100% { opacity: 1; transform: none; } }
@keyframes oh-media { 0%, 65% { opacity: 0; } 68.5%, 100% { opacity: 1; } }
@keyframes oh-k1 { 0%, 71.5% { opacity: 0; transform: translateY(20%); } 74.5%, 100% { opacity: 1; transform: none; } }
@keyframes oh-k2 { 0%, 72.5% { opacity: 0; transform: translateY(20%); } 75.5%, 100% { opacity: 1; transform: none; } }
@keyframes oh-k3 { 0%, 73.5% { opacity: 0; transform: translateY(20%); } 76.5%, 100% { opacity: 1; transform: none; } }
@keyframes oh-bar { 0%, 80% { opacity: 0; } 83%, 100% { opacity: 1; } }
/* Loop reset (hero only): the filled-in parts fade back to the empty listing */
@keyframes oh-ov { 0%, 95% { opacity: 1; } 99%, 100% { opacity: 0; } }
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
    var srcs = {}; [].forEach.call(hero.querySelectorAll('.oh-c'), function (e) { var m = e.style.backgroundImage.match(/url\(["']?(.*?)["']?\)/); if (m) srcs[m[1]] = 1; });
    var loads = Object.keys(srcs).map(function (s) { var i = new Image(); i.src = s; return i.decode ? i.decode().catch(function () {}) : 0; });
    Promise.race([Promise.all(loads), new Promise(function (r) { setTimeout(r, 2500); })]).then(function () { ready = true; sync(); });
  })();
"""


# Landing card: the laptop sits where Procense's tablet does (1.48% of the slot's width per unit: 58 units = 86% of the
# slot); plays once and holds the finished listing (no loop reset); side cards tint the laptop itself.
CARD_CSS = """
.oh.oh--card { --u: 1.48cqw; position: absolute; inset: 0; background: none; overflow: visible; }
.oh--card .od-lid::after, .oh--card .od-base::after { content: ""; position: absolute; inset: 0; z-index: 1; border-radius: inherit; background: var(--cx-tint, transparent); opacity: var(--dim, 0); pointer-events: none; }
.oh--card.oh--anim * { animation-iteration-count: 1; }
.oh--card.oh--anim .oh-sk { animation-iteration-count: infinite; }
.oh--card.oh--anim .oh-ov { animation-name: none; }
"""

CARD_JS = r"""
  // OmniSynkAI card: rest on the final frame; play the hero animation once whenever the card becomes the active card
  (function () {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    document.querySelectorAll('[data-ohc]').forEach(function (oh) {
      var shot = oh.closest('.cx-img'); if (!shot) return;
      var srcs = {}; [].forEach.call(oh.querySelectorAll('.oh-c'), function (e) { var m = e.style.backgroundImage.match(/url\(["']?(.*?)["']?\)/); if (m) srcs[m[1]] = 1; });
      var ready;
      function load() { return ready || (ready = Promise.race([Promise.all(Object.keys(srcs).map(function (s) { var i = new Image(); i.src = s; return i.decode ? i.decode().catch(function () {}) : 0; })), new Promise(function (r) { setTimeout(r, 2500); })])); }
      function active() { return shot.getAttribute('data-active') === 'true'; }
      function play() {
        oh.classList.remove('oh--anim', 'is-play'); void oh.offsetWidth; oh.classList.add('oh--anim');
        load().then(function () { requestAnimationFrame(function () { if (active()) oh.classList.add('is-play'); }); });
      }
      function rest() { oh.classList.remove('oh--anim', 'is-play'); }
      new MutationObserver(function () { if (active()) { if (!oh.classList.contains('oh--anim')) play(); } else rest(); })
        .observe(shot, { attributes: true, attributeFilter: ['data-active'] });
      if (active()) play();
    });
  })();
"""
