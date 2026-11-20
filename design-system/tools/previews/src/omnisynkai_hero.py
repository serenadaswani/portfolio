"""OmniSynkAI case-study hero: one-click AI autofill, told with the four sections that matter, as a smooth loop.

Only the sections that change are shown, each floating directly on OmniSynkAI's brand gradient with no page container:
the title bar on top, then Description, Media and Brand & Tags (centred under it). Every section is a crop of Serena's
final prototype exports at its measured region (1000 x 740 grid of the 2880px files), so components, buttons and spacing
are exactly as designed. One CSS timeline (10s, looped), all soft fades and small drifts:
  1. The title types in and the category fills.
  2. The cursor goes to the AI autofill icon; the click just brings up loading: the sections dim and the
     "Filling out your listing" dialog (from the loading export) floats in above them.
  3. The dialog leaves and grey skeleton content appears inside each input (description lines, media slots, brand and
     tags), then cross-fades into the AI content: description lines rise in with the same purple highlight as the chips,
     photos fade in one by one, the brand and tags chips land, and the title bar becomes "Listing Autofilled".
  4. Hold, then everything fades back to empty.
Final frame (reduced motion, no JS): the autofilled sections. Starts when in view, the tab is visible and the screens
have decoded; pauses off screen and on Pause (WCAG 2.2.2).
"""

V = '?v=2'
W, H = 1000, 740   # the grid every region is measured in (the exports at 1000 px wide)
DX = 118           # the lower sections move right by this much, to centre them under the title bar (895 vs 659 wide)
VIEW = (89, 108, 895, 620)   # title bar's left edge and top, to the bottom of Brand & Tags

def _box(x, y, w, h):
    vx, vy, vw, vh = VIEW
    return f'left:{(x - vx) / vw * 100:.3f}%;top:{(y - vy) / vh * 100:.3f}%;width:{w / vw * 100:.3f}%;height:{h / vh * 100:.3f}%'

def _crop(cls, src, x, y, w, h, dx=0, dy=0):
    """Region (x, y, w, h) of an export, placed at (x + dx, y + dy) in the view."""
    bs = W / w * 100
    px = x / (W - w) * 100 if w < W else 0
    py = y / (H - h) * 100 if h < H else 0
    return (f'<span class="oh-c {cls}" style="{_box(x + dx, y + dy, w, h)};background-image:url({src});'
            f'background-size:{bs:.3f}% auto;background-position:{px:.3f}% {py:.3f}%"></span>')

def _bar(cls, x, y, w, h, dx=0):
    return f'<span class="oh-sk {cls}" style="{_box(x + dx, y, w, h)}"></span>'

CURSOR = ('<svg class="oh-cursor" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
          '<path d="M4 2.5 L4 19.5 L8.6 15.4 L11.4 21.6 L14.2 20.4 L11.5 14.3 L17.6 14.1 Z" fill="#FFFFFF" stroke="#111827" stroke-width="1.4" stroke-linejoin="round"/></svg>')

# Sections (card edges measured from the exports)
CARDS = {'tb': (89, 108.3, 895, 86.8), 'desc': (89, 203.5, 659, 140.3), 'media': (89, 352.1, 659, 286.1), 'meta': (89, 646.5, 659, 81.3)}
# Content regions (1000 x 740 grid)
DESC = [(95, 263, 650, 18), (95, 283, 650, 15), (95, 298, 650, 14), (95, 312, 650, 30)]      # 03 description, line by line
PHOTOS = [(103, 460.5, 164, 163.5)] + [(x, y, 79.5, 79) for y in (460.5, 545) for x in (274, 360, 446, 532)]  # 03 media
CHIPS = [(114, 688.5, 52.5, 17), (436.5, 688.5, 54.5, 17), (496, 688.5, 57, 17)]          # 03 brand chip, tag chips
SK_DESC = [(97, 268, 520, 8), (110, 288, 470, 7), (110, 302, 520, 7), (110, 316, 560, 7), (110, 330, 260, 7)]
SK_FIELDS = [(114, 690.5, 52.5, 13), (436.5, 690.5, 116.5, 13)]
# AI-written description, highlighted like the brand and tags chips (chip fill #F0E8F7, text #9447E0, from 03):
# one box per line of text (extents measured from the export), with the description line it arrives with
HILITE = [((95, 267.5, 532, 13.5), 1), ((109, 287.5, 439, 12), 2), ((109, 300, 558, 13), 3),
          ((109, 313.5, 631, 13.5), 4), ((109, 327, 630, 14), 4)]
# Typed values: 03's field text, shifted onto 01's fields (01 title input starts at 260, 03's at 240; category 478 vs 465)
TYPE_TITLE = (246, 152, 150, 20, 20)
TYPE_CAT = (471, 152, 150, 20, 13)
DIALOG = (349, 275, 302.5, 188.5)   # 02: the "Filling out your listing" dialog

def html(base='assets/screens', I=None):
    s1, s2, s3 = (f'{base}/{f}{V}' for f in ('01-empty-listing.jpg', '02-autofill-in-progress.jpg', '03-listing-autofilled.jpg'))
    vx, vy, vw, vh = VIEW
    cards = ''.join(_crop(f'oh-card oh-card--{k}', s1, *b, dx=0 if k == 'tb' else DX) for k, b in CARDS.items())
    lower = (
        '<span class="oh-mbg" style="' + _box(100 + DX, 456, 636, 172) + '"></span>'
        + _crop('oh-slots', s3, 614, 456, 120, 172, dx=DX)
        + '<span class="oh-sks">' + ''.join(_bar('oh-sk--d', *b, dx=DX) for b in SK_DESC)
        + ''.join(_bar('oh-sk--m', *b, dx=DX) for b in PHOTOS) + ''.join(_bar('oh-sk--f', *b, dx=DX) for b in SK_FIELDS) + '</span>'
        + ''.join(_crop(f'oh-d oh-d--{i + 1}', s3, *b, dx=DX) for i, b in enumerate(DESC))
        # purple highlight: 'screen' turns the black text purple, 'multiply' tints the paper (siblings, so both blend)
        + ''.join(f'<span class="oh-hl oh-hl--t oh-d--{d}" style="{_box(b[0] + DX, *b[1:])}"></span>'
                  f'<span class="oh-hl oh-hl--f oh-d--{d}" style="{_box(b[0] + DX, *b[1:])}"></span>' for b, d in HILITE)
        + ''.join(_crop(f'oh-p oh-p--{i + 1}', s3, *b, dx=DX) for i, b in enumerate(PHOTOS))
        + ''.join(_crop(f'oh-k oh-k--{i + 1}', s3, *b, dx=DX) for i, b in enumerate(CHIPS)))
    top = (_crop('oh-type', s3, *TYPE_TITLE[:4], dx=TYPE_TITLE[4]) + _crop('oh-cat', s3, *TYPE_CAT[:4], dx=TYPE_CAT[4])
           + _crop('oh-card oh-tb', s3, *CARDS['tb']))
    dx, dy = vx + (vw - DIALOG[2]) / 2 - DIALOG[0], vy + (vh - DIALOG[3]) / 2 - DIALOG[1]
    dialog = _crop('oh-dialog', s2, *DIALOG, dx=dx, dy=dy)
    pause = I['pause'] if I else ''
    play = I['play'] if I else ''
    return ('  <div class="cs-hero-well oh-wrap">'
            '<div class="pm-media pm-media--21x9 oh" data-oh role="img" '
            'aria-label="OmniSynkAI AI autofill: a seller types a title and a category and clicks the AI autofill icon; a loading dialog floats in, '
            'then skeleton content in each field turns into the AI-written description, highlighted in purple, product photos, brand and tags, and the title bar reads Listing Autofilled.">'
            f'<div class="oh-stage"><div class="oh-app"><div class="oh-cards">{cards}{lower}{top}</div>{dialog}{CURSOR}</div></div></div>'
            '<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-btn--sm oh-toggle" aria-pressed="false" aria-label="Pause animation" data-oh-toggle hidden>'
            f'<span class="oh-ic oh-ic--pause">{pause}</span><span class="oh-ic oh-ic--play" hidden>{play}</span></button></div>\n'
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("oh--anim")})(document.querySelector("[data-oh]"))</script>\n')

CSS = r"""
/* ===== OmniSynkAI hero (omnisynkai_hero.py): the four sections that matter, floating on the gradient ===== */
.oh-wrap { position: relative; }
.oh { container-type: inline-size; background: radial-gradient(90% 120% at 50% 110%, rgb(255 255 255 / 22%) 0%, rgb(255 255 255 / 0%) 60%), linear-gradient(160deg, #4745B0 0%, #5B43E8 40%, #755CFB 75%, #9B94E0 100%); }
.oh-stage { position: absolute; inset: 0; display: grid; place-items: center; }
.oh-app { position: relative; width: 55cqw; aspect-ratio: 895 / 620; container-type: inline-size; }
@container (max-width: 599px) { .oh-app { width: 78cqw; } }
.oh-cards { position: absolute; inset: 0; }
.oh-c { position: absolute; background-repeat: no-repeat; }
/* each section is its own card on the gradient: the export's card, its corners rounded to match, a soft shadow */
.oh-card { border-radius: .7cqw; box-shadow: 0 .6cqw 2.2cqw rgb(20 12 70 / 24%), 0 .1cqw .3cqw rgb(20 12 70 / 12%); }
.oh-tb { box-shadow: none; }
.oh-dialog { border-radius: 1cqw; box-shadow: 0 1.4cqw 4cqw rgb(20 12 70 / 38%), 0 0 0 1px rgb(255 255 255 / 40%); opacity: 0; }
.oh-mbg { position: absolute; background: #FFFFFF; }
.oh-sks { position: absolute; inset: 0; opacity: 0; }
.oh-sk { position: absolute; border-radius: .35cqw; background: linear-gradient(90deg, #E6E8EC 0%, #F1F2F5 45%, #E6E8EC 90%); background-size: 300% 100%; }
.oh-sk--m { border-radius: .6cqw; }
.oh-hl { position: absolute; border-radius: .3cqw; }
.oh-hl--t { background: #9447E0; mix-blend-mode: screen; }
.oh-hl--f { background: #F0E8F7; mix-blend-mode: multiply; }
.oh-cursor { position: absolute; left: 92%; top: 60%; width: 3.6cqw; height: 3.6cqw; opacity: 0; filter: drop-shadow(0 .3cqw .5cqw rgb(0 0 0 / 25%)); pointer-events: none; }

/* Pause / Play, outside the image role */
.oh-toggle { position: absolute; right: var(--space-3); bottom: var(--space-3); z-index: 2; }
.oh-toggle[hidden], .oh-ic[hidden] { display: none; }
.oh-ic { display: contents; }

/* ---- The loop (10s). The rules above are the final frame; with motion, every layer runs from its 0% frame, held
   paused until the hero is ready and in view. Soft easing throughout. ---- */
.oh--anim .oh-app, .oh--anim .oh-app * { animation-duration: 10s; animation-iteration-count: infinite; animation-fill-mode: both; animation-timing-function: cubic-bezier(.45, 0, .2, 1); animation-play-state: paused; }
.oh--anim.is-play:not(.is-paused) .oh-app, .oh--anim.is-play:not(.is-paused) .oh-app * { animation-play-state: running; }
.oh--anim .oh-cards { animation-name: oh-dim; }
.oh--anim .oh-type { animation-name: oh-type; }
.oh--anim .oh-cat { animation-name: oh-cat; }
.oh--anim .oh-cursor { animation-name: oh-cursor; }
.oh--anim .oh-dialog { animation-name: oh-dialog; }
.oh--anim .oh-mbg, .oh--anim .oh-slots { animation-name: oh-mbg; }
.oh--anim .oh-sks { animation-name: oh-sks; }
.oh--anim .oh-sk { animation: oh-sweep 1.6s linear infinite; }
.oh--anim .oh-d--1 { animation-name: oh-d1; } .oh--anim .oh-d--2 { animation-name: oh-d2; } .oh--anim .oh-d--3 { animation-name: oh-d3; } .oh--anim .oh-d--4 { animation-name: oh-d4; }
.oh--anim .oh-p { animation-name: oh-p1; }
.oh--anim .oh-p--2, .oh--anim .oh-p--6 { animation-name: oh-p2; } .oh--anim .oh-p--3, .oh--anim .oh-p--7 { animation-name: oh-p3; }
.oh--anim .oh-p--4, .oh--anim .oh-p--8 { animation-name: oh-p4; } .oh--anim .oh-p--5, .oh--anim .oh-p--9 { animation-name: oh-p5; }
.oh--anim .oh-k--1 { animation-name: oh-k1; } .oh--anim .oh-k--2 { animation-name: oh-k2; } .oh--anim .oh-k--3 { animation-name: oh-k3; }
.oh--anim .oh-tb { animation-name: oh-tb; }

@keyframes oh-type { 0%, 5% { opacity: 1; clip-path: inset(0 100% 0 0); animation-timing-function: steps(15, end); } 16%, 91% { opacity: 1; clip-path: inset(0 0 0 0); } 96%, 100% { opacity: 0; clip-path: inset(0 0 0 0); } }
@keyframes oh-cat { 0%, 17% { opacity: 0; } 20%, 91% { opacity: 1; } 96%, 100% { opacity: 0; } }
@keyframes oh-cursor { 0%, 20% { opacity: 0; left: 90%; top: 62%; } 23% { opacity: 1; left: 88%; top: 52%; } 29%, 30.5% { opacity: 1; left: 81.2%; top: 6.4%; } 33%, 100% { opacity: 0; left: 81.2%; top: 6.4%; } }
/* loading: the sections dim and the dialog floats in above them */
@keyframes oh-dim { 0%, 30.5% { filter: brightness(1) saturate(1); } 33.5%, 44% { filter: brightness(.72) saturate(.85); } 48%, 100% { filter: brightness(1) saturate(1); } }
@keyframes oh-dialog { 0%, 30.5% { opacity: 0; transform: translateY(1.2cqw) scale(.96); } 34%, 44% { opacity: 1; transform: none; } 47.5%, 100% { opacity: 0; transform: translateY(-.6cqw) scale(.98); } }
/* skeletons inside each input, then the content cross-fades in */
@keyframes oh-mbg { 0%, 45% { opacity: 0; } 48%, 91% { opacity: 1; } 96%, 100% { opacity: 0; } }
@keyframes oh-sks { 0%, 45% { opacity: 0; } 49%, 54% { opacity: 1; } 62%, 100% { opacity: 0; } }
@keyframes oh-sweep { from { background-position: 100% 0; } to { background-position: -50% 0; } }
@keyframes oh-d1 { 0%, 53% { opacity: 0; transform: translateY(.5cqw); } 57.5%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-d2 { 0%, 54.5% { opacity: 0; transform: translateY(.5cqw); } 59%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-d3 { 0%, 56% { opacity: 0; transform: translateY(.5cqw); } 60.5%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-d4 { 0%, 57.5% { opacity: 0; transform: translateY(.5cqw); } 62%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-p1 { 0%, 54% { opacity: 0; transform: scale(.97); } 59%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-p2 { 0%, 55.5% { opacity: 0; transform: scale(.97); } 60.5%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-p3 { 0%, 57% { opacity: 0; transform: scale(.97); } 62%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-p4 { 0%, 58.5% { opacity: 0; transform: scale(.97); } 63.5%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-p5 { 0%, 60% { opacity: 0; transform: scale(.97); } 65%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-k1 { 0%, 60% { opacity: 0; transform: translateY(.4cqw); } 64%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-k2 { 0%, 61.5% { opacity: 0; transform: translateY(.4cqw); } 65.5%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-k3 { 0%, 63% { opacity: 0; transform: translateY(.4cqw); } 67%, 91% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; transform: none; } }
@keyframes oh-tb { 0%, 65% { opacity: 0; } 70%, 91% { opacity: 1; } 96%, 100% { opacity: 0; } }
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
