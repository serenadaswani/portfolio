"""OmniSynkAI case-study hero: one-click AI autofill as four frames that follow the flow, looped (12s).

Every component is a crop of Serena's final prototype exports at its measured region (1000 x 740 grid of the 2880px
files), so components, buttons and spacing are exactly as designed; frames float on OmniSynkAI's brand gradient.
  1. Title bar. The title types in and the category fills while the view zooms into both fields; then the view glides
     to the AI autofill icon and the cursor clicks it.
  2. Loading. The title bar fades out, a soft scrim settles over the gradient and the "Filling out your listing" dialog
     (its AI icon redrawn in SVG so the two sparkles merge into one star and split back, as in the first-concept video)
     floats in.
  3. Skeletons. Only the sections autofill writes to appear, Description and Brand & Tags, with grey skeleton content
     inside them.
  4. Generated. The skeletons give way to the AI content: description lines rise in with a clean per-line purple
     highlight (the brand and tags chips' colours), the brand and tag chips land, and the "Listing Autofilled" title bar
     arrives on top at the same width as the sections. Hold, fade, loop.
Final frame (reduced motion, no JS): frame 4, complete. Starts when in view, the tab is visible and the screens have
decoded; pauses off screen and on Pause (WCAG 2.2.2).
"""

V = '?v=3'
W, H = 1000, 740   # grid of the exports at 1000 px wide

# Sharp sources: each piece is its own crop of the 2880px Figma exports (omnisynkai/assets/hero/<name>.jpg), so the page
# downloads only what it shows. Regions are (x, y, w, h) in the export grid, from the pixel crops (2.88 px per unit).
SPRITES = {
    '01-bar': (87.8472, 106.9444, 897.2222, 88.8889), '01-desc': (87.8472, 202.4306, 661.1111, 142.7083),
    '01-meta': (87.8472, 645.4861, 661.1111, 83.6806), '03-bar': (87.8472, 106.9444, 897.2222, 88.8889),
    '03-desc': (92.7083, 260.7639, 654.1667, 84.375), '03-chips': (111.8056, 685.7639, 444.0972, 22.2222),
    '02-dialog': (347.9167, 273.9583, 305.2083, 190.9722),
}

def _place(cls, sp, sbox, dbox, frame):
    """Crop sbox (x, y, w, h in the export grid) of sprite sp = (url, region) into dbox (in the frame's own grid)."""
    url, (rx, ry, rw, rh) = sp
    sx, sy, sw, sh = sbox
    assert rx - .01 <= sx and sx + sw <= rx + rw + .01 and ry - .01 <= sy and sy + sh <= ry + rh + .01, (cls, sbox, rx, ry, rw, rh)
    dx, dy, dw, dh = dbox
    fw, fh = frame
    bs = rw / sw * 100
    px = (sx - rx) / (rw - sw) * 100 if rw - sw > .01 else 0
    py = (sy - ry) / (rh - sh) * 100 if rh - sh > .01 else 0
    return (f'<span class="oh-c {cls}" style="left:{dx / fw * 100:.3f}%;top:{dy / fh * 100:.3f}%;width:{dw / fw * 100:.3f}%;height:{dh / fh * 100:.3f}%;'
            f'background-image:url({url});background-size:{bs:.3f}% auto;background-position:{px:.3f}% {py:.3f}%"></span>')

def _rect(cls, dbox, frame):
    dx, dy, dw, dh = dbox
    fw, fh = frame
    return f'<span class="{cls}" style="left:{dx / fw * 100:.3f}%;top:{dy / fh * 100:.3f}%;width:{dw / fw * 100:.3f}%;height:{dh / fh * 100:.3f}%"></span>'

CURSOR = ('<svg class="oh-cursor" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
          '<path d="M4 2.5 L4 19.5 L8.6 15.4 L11.4 21.6 L14.2 20.4 L11.5 14.3 L17.6 14.1 Z" fill="#FFFFFF" stroke="#111827" stroke-width="1.4" stroke-linejoin="round"/></svg>')

# ---- regions measured from the exports ----
BAR = (89, 108.3, 895, 86.8)                      # title bar (01 empty, 03 autofilled)
DESC_CARD = (89, 203.5, 659, 140.3)
META_CARD = (89, 646.5, 659, 81.3)
DIALOG = (349, 275, 302.5, 188.5)                 # 02 loading dialog
SPARK = (361, 292, 20, 20)                        # 02 dialog's AI icon, redrawn so it can animate (as in the first-concept video)
TYPE_TITLE = (246, 152, 150, 20, 20)              # 03 field text (x, y, w, h), shifted dx onto 01's title input
TYPE_CAT = (471, 152, 150, 20, 13)
# description lines in 03: crop bands (non-overlapping) and text boxes (x extents, ascender to descender)
DESC_BANDS = [(263, 284), (284, 300.5), (300.5, 314.5), (314.5, 328.3), (328.3, 343)]
HILITE = [(95, 268, 532, 12.3), (109, 287.5, 439.2, 12.3), (109, 301.4, 558.3, 12.3), (109, 315.3, 631, 12.3), (109, 329.2, 144.4, 12.3)]
CHIPS = [(114, 688.5, 52.5, 17), (436.5, 688.5, 54.5, 17), (496, 688.5, 57, 17)]
SK_DESC = [(97, 270, 520, 8), (110, 290, 430, 7.5), (110, 304, 540, 7.5), (110, 318, 600, 7.5), (110, 332, 150, 7.5)]
SK_FIELDS = [(114, 690.5, 52.5, 13), (436.5, 690.5, 116.5, 13)]

# ---- frame 3/4 layout: the "Listing Autofilled" bar scaled to the sections' width, then Description, Brand & Tags ----
GAP = 9
BAR_H = BAR[3] * DESC_CARD[2] / BAR[2]                    # the bar at 659 wide
Y_DESC = BAR_H + GAP
Y_META = Y_DESC + DESC_CARD[3] + GAP
STACK = (DESC_CARD[2], Y_META + META_CARD[3])             # frame grid

def _desc(sbox):   # export coords inside the description card -> stack coords
    x, y, w, h = sbox
    return (x - DESC_CARD[0], y - DESC_CARD[1] + Y_DESC, w, h)

def _meta(sbox):
    x, y, w, h = sbox
    return (x - META_CARD[0], y - META_CARD[1] + Y_META, w, h)

STAR = 'M0 -.94C.07 -.42 .42 -.07 .94 0C.42 .07 .07 .42 0 .94C-.07 .42 -.42 .07 -.94 0C-.42 -.07 -.07 -.42 0 -.94Z'

def _spark(s2, uid):
    """The dialog's two-star AI icon as SVG, over a patch of the same export's blank dialog (so the paper matches exactly)."""
    x, y, w, h = SPARK
    patch = _place('oh-patch', s2, (612, y, w, h), (x - DIALOG[0], y - DIALOG[1], w, h), DIALOG[2:])
    pos = (f'left:{(x - DIALOG[0]) / DIALOG[2] * 100:.3f}%;top:{(y - DIALOG[1]) / DIALOG[3] * 100:.3f}%;'
           f'width:{w / DIALOG[2] * 100:.3f}%;height:{h / DIALOG[3] * 100:.3f}%')
    star = f'<path d="{STAR}" fill="url(#oh-sg{uid})" stroke="url(#oh-sg{uid})" stroke-width=".16" stroke-linejoin="round"/>'
    return patch + (f'<span class="oh-spark" style="{pos}"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false">'
            f'<defs><linearGradient id="oh-sg{uid}" x1="0" x2="1" y1="0" y2="0">'
            '<stop offset="0" stop-color="#5B8CFF"/><stop offset=".48" stop-color="#A566FF"/><stop offset="1" stop-color="#AC6AFF"/>'
            f'</linearGradient></defs><g class="oh-st oh-st--b">{star}</g><g class="oh-st oh-st--s">{star}</g></svg></span>')

def _stage(base, uid):
    """The three layers (title bar, loading dialog, sections) and the root's custom properties; shared by the
    case-study hero and the landing's OmniSynkAI card."""
    sp = {n: (f'{base}/{n}.jpg{V}', r) for n, r in SPRITES.items()}
    s1b, s1d, s1m, s2, s3b, s3d, s3k = (sp[n] for n in ('01-bar', '01-desc', '01-meta', '02-dialog', '03-bar', '03-desc', '03-chips'))
    fb = BAR[2:]
    # Frame 1: the title bar, with a camera that zooms to the fields, then to the AI autofill icon
    tx, ty, tw, th, tdx = TYPE_TITLE
    cx, cy, cw, ch, cdx = TYPE_CAT
    f1 = ('<div class="oh-f oh-f1"><div class="oh-cam">'
          + _place('oh-card', s1b, BAR, (0, 0) + fb, fb)
          + _place('oh-type', s3b, (tx, ty, tw, th), (tx + tdx - BAR[0], ty - BAR[1], tw, th), fb)
          + _place('oh-cat', s3b, (cx, cy, cw, ch), (cx + cdx - BAR[0], cy - BAR[1], cw, ch), fb)
          + CURSOR + '</div></div>')
    # Frame 2: the loading dialog over a soft scrim
    f2 = ('<span class="oh-scrim"></span><div class="oh-f oh-f2">'
          + _place('oh-dialog', s2, DIALOG, (0, 0) + DIALOG[2:], DIALOG[2:]) + _spark(s2, uid) + '</div>')
    # Frames 3 and 4: Description and Brand & Tags (skeletons, then content), with the autofilled bar arriving on top
    sk = ('<span class="oh-sks">' + ''.join(_rect('oh-sk', _desc(b), STACK) for b in SK_DESC)
          + ''.join(_rect('oh-sk', _meta(b), STACK) for b in SK_FIELDS) + '</span>')
    lines = ''.join(_place(f'oh-d oh-d--{i + 1}', s3d, (95, y0, 650, y1 - y0), _desc((95, y0, 650, y1 - y0)), STACK)
                    for i, (y0, y1) in enumerate(DESC_BANDS))
    # clean highlight: per measured line, 'screen' turns black text purple and 'multiply' tints the paper (siblings, so both blend)
    hl = ''.join(_rect(f'oh-hl oh-hl--t oh-d--{i + 1}', _desc(b), STACK) + _rect(f'oh-hl oh-hl--f oh-d--{i + 1}', _desc(b), STACK)
                 for i, b in enumerate(HILITE))
    chips = ''.join(_place(f'oh-k oh-k--{i + 1}', s3k, b, _meta(b), STACK) for i, b in enumerate(CHIPS))
    f34 = ('<div class="oh-f oh-f3"><div class="oh-stack">'
           + _place('oh-card oh-bar', s3b, BAR, (0, 0, STACK[0], BAR_H), STACK)
           + _place('oh-card oh-sec', s1d, DESC_CARD, (0, Y_DESC) + DESC_CARD[2:], STACK)
           + _place('oh-card oh-sec', s1m, META_CARD, (0, Y_META) + META_CARD[2:], STACK)
           + sk + lines + hl + chips + '</div></div>')
    style = (f'--f1-ar:{BAR[2]} / {BAR[3]};--f2-ar:{DIALOG[2]} / {DIALOG[3]};--f3-ar:{STACK[0]} / {STACK[1]:.2f};'
             f'--stack-shift:{(BAR_H + GAP) / 2 / STACK[1] * 100:.3f}%')
    return f1 + f2 + f34, style


def html(base='assets/hero', I=None):
    inner, style = _stage(base, 'h')
    pause = I['pause'] if I else ''
    play = I['play'] if I else ''
    return ('  <div class="cs-hero-well oh-wrap">'
            f'<div class="pm-media pm-media--21x9 oh" data-oh role="img" style="{style}" '
            'aria-label="OmniSynkAI AI autofill in four steps: a seller types a title and a category, and the view zooms to the AI autofill icon, which they click; '
            'a loading dialog appears; skeletons fill the description and the brand and tags fields; then the AI-written description, highlighted in purple, '
            'and the brand and tag chips appear, with the title bar reading Listing Autofilled.">'
            f'{inner}</div>'
            '<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-btn--sm oh-toggle" aria-pressed="false" aria-label="Pause animation" data-oh-toggle hidden>'
            f'<span class="oh-ic oh-ic--pause">{pause}</span><span class="oh-ic oh-ic--play" hidden>{play}</span></button></div>\n'
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("oh--anim")})(document.querySelector("[data-oh]"))</script>\n')

CSS = r"""
/* ===== OmniSynkAI hero (omnisynkai_hero.py): four frames that follow the autofill flow ===== */
.oh-wrap { position: relative; }
.oh { container-type: inline-size; overflow: hidden; background: radial-gradient(90% 120% at 50% 110%, rgb(255 255 255 / 22%) 0%, rgb(255 255 255 / 0%) 60%), linear-gradient(160deg, #4745B0 0%, #5B43E8 40%, #755CFB 75%, #9B94E0 100%); }
.oh-f { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); }
.oh-f1 { width: 78cqw; aspect-ratio: var(--f1-ar); opacity: 0; }
.oh-f2 { width: 36cqw; aspect-ratio: var(--f2-ar); opacity: 0; }
.oh-f3 { width: 68cqw; aspect-ratio: var(--f3-ar); }
@container (max-width: 599px) { .oh-f1 { width: 88cqw; } .oh-f2 { width: 52cqw; } .oh-f3 { width: 86cqw; } }
.oh-cam, .oh-stack { position: absolute; inset: 0; }
.oh-c, .oh-sk, .oh-hl { position: absolute; }
.oh-c { background-repeat: no-repeat; }
.oh-card { border-radius: .8cqw; box-shadow: 0 .6cqw 2.4cqw rgb(20 12 70 / 26%), 0 .1cqw .3cqw rgb(20 12 70 / 12%); }
.oh-dialog { inset: 0; border-radius: 1cqw; box-shadow: 0 1.4cqw 4cqw rgb(20 12 70 / 40%), 0 0 0 1px rgb(255 255 255 / 40%); }
.oh-spark { position: absolute; }
.oh-spark svg { display: block; width: 100%; height: 100%; overflow: visible; }
.oh-st { transform-box: view-box; transform-origin: 0 0; }
.oh-st--b { transform: translate(6.9px, 12.2px) scale(5.4, 5.9); }
.oh-st--s { transform: translate(15.05px, 4.9px) scale(3.1, 3.5); }
.oh-scrim { position: absolute; inset: 0; background: rgb(20 14 60 / 38%); opacity: 0; }
.oh-sks { position: absolute; inset: 0; opacity: 0; }
.oh-sk { border-radius: .3cqw; background: linear-gradient(90deg, #E6E8EC 0%, #F1F2F5 45%, #E6E8EC 90%); background-size: 300% 100%; }
.oh-hl { border-radius: .25cqw; }
.oh-hl--t { background: #9447E0; mix-blend-mode: screen; }
.oh-hl--f { background: #F0E8F7; mix-blend-mode: multiply; }
.oh-cursor { position: absolute; left: 81.2%; top: 47%; width: 2.4%; aspect-ratio: 1; opacity: 0; filter: drop-shadow(0 .2cqw .4cqw rgb(0 0 0 / 25%)); pointer-events: none; }

/* Pause / Play, outside the image role */
.oh-toggle { position: absolute; right: var(--space-3); bottom: var(--space-3); z-index: 2; }
.oh-toggle[hidden], .oh-ic[hidden] { display: none; }
.oh-ic { display: contents; }

/* ---- The loop (12s). The rules above are the final frame (frame 4 complete); with motion every layer runs from its 0%
   frame, held paused until the hero is ready and in view. One soft ease throughout. ---- */
.oh--anim * { animation-duration: 12s; animation-iteration-count: infinite; animation-fill-mode: both; animation-timing-function: cubic-bezier(.45, 0, .2, 1); animation-play-state: paused; }
.oh--anim.is-play:not(.is-paused) * { animation-play-state: running; }
.oh--anim .oh-f1 { animation-name: oh-f1; }
.oh--anim .oh-cam { animation-name: oh-cam; }
.oh--anim .oh-type { animation-name: oh-type; }
.oh--anim .oh-cat { animation-name: oh-cat; }
.oh--anim .oh-cursor { animation-name: oh-cursor; }
.oh--anim .oh-scrim { animation-name: oh-scrim; }
.oh--anim .oh-f2 { animation-name: oh-f2; }
.oh--anim .oh-st--b { animation-name: oh-stb; }
.oh--anim .oh-st--s { animation-name: oh-sts; }
.oh--anim .oh-f3 { animation-name: oh-f3; }
.oh--anim .oh-stack { animation-name: oh-stack; }
.oh--anim .oh-bar { animation-name: oh-bar; }
.oh--anim .oh-sks { animation-name: oh-sks; }
.oh--anim .oh-sk { animation: oh-sweep 1.6s linear infinite; }
.oh--anim .oh-d--1 { animation-name: oh-d1; } .oh--anim .oh-d--2 { animation-name: oh-d2; } .oh--anim .oh-d--3 { animation-name: oh-d3; }
.oh--anim .oh-d--4 { animation-name: oh-d4; } .oh--anim .oh-d--5 { animation-name: oh-d5; }
.oh--anim .oh-k--1 { animation-name: oh-k1; } .oh--anim .oh-k--2 { animation-name: oh-k2; } .oh--anim .oh-k--3 { animation-name: oh-k3; }

/* 1. Title bar: in, zoom to the fields while they fill, glide to the AI autofill icon, click, out */
@keyframes oh-f1 { 0% { opacity: 0; transform: translate(-50%, -46%); } 3%, 26% { opacity: 1; transform: translate(-50%, -50%); } 29.5%, 100% { opacity: 0; transform: translate(-50%, -50%); } }
@keyframes oh-cam { 0%, 4% { transform: none; } 9%, 16% { transform: scale(1.45) translateX(3.2%); } 22%, 30% { transform: scale(2.1) translateX(-31.4%); } 100% { transform: scale(2.1) translateX(-31.4%); } }
@keyframes oh-type { 0%, 7% { clip-path: inset(0 100% 0 0); animation-timing-function: steps(15, end); } 14%, 100% { clip-path: inset(0 0 0 0); } }
@keyframes oh-cat { 0%, 14% { opacity: 0; } 16.5%, 100% { opacity: 1; } }
@keyframes oh-cursor { 0%, 20% { opacity: 0; left: 90%; top: 95%; } 22% { opacity: 1; } 25.5%, 27% { opacity: 1; left: 81.2%; top: 47%; } 29%, 100% { opacity: 0; left: 81.2%; top: 47%; } }
/* 2. Loading: scrim and dialog */
@keyframes oh-scrim { 0%, 28% { opacity: 0; } 32%, 44% { opacity: 1; } 49%, 100% { opacity: 0; } }
@keyframes oh-f2 { 0%, 29.5% { opacity: 0; transform: translate(-50%, -44%) scale(.97); } 33.5%, 44% { opacity: 1; transform: translate(-50%, -50%); } 47.5%, 100% { opacity: 0; transform: translate(-50%, -54%) scale(.98); } }
/* The icon, as in the first-concept video: the small sparkle slides into the large one and they merge into one star, then split back */
@keyframes oh-stb { 0%, 34.5% { transform: translate(6.9px, 12.2px) scale(5.4, 5.9); } 37% { transform: translate(10px, 10.4px) scale(6.3, 6.7); } 39% { transform: translate(10px, 10.4px) scale(6.7, 7.1); } 41% { transform: translate(10px, 10.4px) scale(6.3, 6.7); } 43.5%, 100% { transform: translate(6.9px, 12.2px) scale(5.4, 5.9); } }
@keyframes oh-sts { 0%, 34.5% { opacity: 1; transform: translate(15.05px, 4.9px) scale(3.1, 3.5); } 36.5% { opacity: .8; } 37%, 41% { opacity: 0; transform: translate(10px, 10.4px) scale(1.2, 1.3); } 41.5% { opacity: .8; } 43.5%, 100% { opacity: 1; transform: translate(15.05px, 4.9px) scale(3.1, 3.5); } }
/* 3. Description and Brand & Tags with skeletons (centred), 4. content and the autofilled bar (the stack rises to make room) */
@keyframes oh-f3 { 0%, 47% { opacity: 0; } 50.5%, 92% { opacity: 1; } 97%, 100% { opacity: 0; } }
@keyframes oh-stack { 0%, 63% { transform: translateY(calc(-1 * var(--stack-shift))); } 69%, 100% { transform: none; } }
@keyframes oh-bar { 0%, 63.5% { opacity: 0; transform: translateY(-1.2cqw); } 69%, 100% { opacity: 1; transform: none; } }
@keyframes oh-sks { 0%, 48% { opacity: 1; } 56% { opacity: 1; } 61%, 100% { opacity: 0; } }
@keyframes oh-sweep { from { background-position: 100% 0; } to { background-position: -50% 0; } }
@keyframes oh-d1 { 0%, 56% { opacity: 0; transform: translateY(.5cqw); } 60%, 100% { opacity: 1; transform: none; } }
@keyframes oh-d2 { 0%, 57.2% { opacity: 0; transform: translateY(.5cqw); } 61.2%, 100% { opacity: 1; transform: none; } }
@keyframes oh-d3 { 0%, 58.4% { opacity: 0; transform: translateY(.5cqw); } 62.4%, 100% { opacity: 1; transform: none; } }
@keyframes oh-d4 { 0%, 59.6% { opacity: 0; transform: translateY(.5cqw); } 63.6%, 100% { opacity: 1; transform: none; } }
@keyframes oh-d5 { 0%, 60.8% { opacity: 0; transform: translateY(.5cqw); } 64.8%, 100% { opacity: 1; transform: none; } }
@keyframes oh-k1 { 0%, 60% { opacity: 0; transform: translateY(.4cqw); } 64%, 100% { opacity: 1; transform: none; } }
@keyframes oh-k2 { 0%, 61.5% { opacity: 0; transform: translateY(.4cqw); } 65.5%, 100% { opacity: 1; transform: none; } }
@keyframes oh-k3 { 0%, 63% { opacity: 0; transform: translateY(.4cqw); } 67%, 100% { opacity: 1; transform: none; } }
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


# ---------- The same animation on the landing's OmniSynkAI card ----------
def card(base='omnisynkai/assets/hero', uid='c'):
    """The hero animation in the landing card's media spot (the same size and place as Procense's tablet). It rests on
    the final frame (frame 4, complete) and plays once from the start each time the OmniSynkAI card becomes active."""
    inner, style = _stage(base, uid)
    return f'<div class="oh oh--card" data-ohc aria-hidden="true" style="{style}">{inner}</div>'

# The media box matches the Procense tablet / placeholder: 52 x 39.55 units at 1.48% of the slot's width per unit.
# Frames are sized for its 4:3-ish shape. Plays once (no loop): frame 4 holds at the end instead of fading out.
CARD_CSS = """
.oh.oh--card { position: relative; width: calc(52 * 1.48cqw); aspect-ratio: 52 / 39.55; border-radius: calc(1.2 * 1.48cqw);
  box-shadow: 0 1px 2px rgb(0 0 0 / 6%), 0 var(--space-5) var(--space-10) calc(-1 * var(--space-2)) rgb(0 0 0 / 30%), inset 0 0 0 1px rgb(255 255 255 / 14%); }
.oh.oh--card .oh-f1 { width: 92cqw; } .oh.oh--card .oh-f2 { width: 64cqw; } .oh.oh--card .oh-f3 { width: 90cqw; }
.oh.oh--card::after { content: ""; position: absolute; inset: 0; z-index: 2; border-radius: inherit; background: var(--cx-tint); opacity: var(--dim, 0); pointer-events: none; }
.oh--card.oh--anim * { animation-iteration-count: 1; }
.oh--card.oh--anim .oh-sk { animation-iteration-count: infinite; }
.oh--card.oh--anim .oh-f3 { animation-name: oh-f3c; }
@keyframes oh-f3c { 0%, 47% { opacity: 0; } 50.5%, 100% { opacity: 1; } }
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
