"""Procense case-study hero: the paper form's elements become the shipped screen's elements, landing exactly.

On Procense's navy (the landing card's art), a paper QC tests form fills in by hand (batch number, product, date and
time finished). The sheet settles level into a tablet's place, the app's chrome (top bar, nav rail, action bar) fades
in around it, and each part of the paper glides and reshapes into its counterpart on Serena's real QC tests screen:
the sheet into the white card, the bordered section into the grey panel, each ruled field into its input box, the
printed table into the test table; the "Add sample" button grows in. Every target rect, border colour and radius was
measured from the pixels of the shipped exports (TARGETS below, in 1.5x export px), so the boxes land exactly on the
real ones. Only then does the real screen fade in, so the last change is just the text resolving (the handwritten
date and time give way to the auto-filled 04/02/2024 and 14:36). It holds on the whole tablet, level and in frame.

Layers in the screen: the base image (chrome), the morph layer laid exactly over the content box (80, 56, 944, 631 in
1x px) and clipped to it as the boxes land, then the slice of the scroll export (from y = 540) on top.

One CSS timeline (~4.7s): the morph boxes animate left/top/width/height through custom properties, everything else is
transform, opacity, clip-path and colour; soft easing; plays once when in view and the tab is visible. An inline
script sets the start frame before first paint; no JS or reduced motion show the final frame. Sized in --u.
Colours are project art (navy, paper, pen ink, and the shipped UI's own colours).
"""
import re

HEAD = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&display=swap">'
        '<!-- Caveat: handwriting in the hero art only -->\n')

SLICE_Y, SLICE_H, EXPORT_W, EXPORT_H = 540, 946.5, 1416, 2337   # scroll export (1.5x px) and the visible slice
BOX = (7.8125, 7.2917, 92.1875, 82.1615)                          # content box, % of the screen (80, 56, 944, 631 at 1x)

# Shipped element rects in the scroll export (1.5x px, inclusive), measured from the pixels on 2026-11-17
TARGETS = {
    'card': (36, 504, 1379, 1486), 'title': (76, 552, 232, 582), 'button': (1104, 552, 1341, 623),
    'panel': (73, 670, 1342, 1327),
    'yield': (109, 754, 488, 827), 'date': (518, 754, 897, 828), 'time': (927, 754, 1306, 828),
    'made': (109, 949, 693, 1023), 'pack': (722, 949, 1306, 1023), 'comments': (109, 1099, 1306, 1293),
    'table': (74, 1364, 1341, 1486),
}
# Paper rects, % of the screen (left, top, width, height)
PAPER = {
    'card': (0, 0, 100, 100), 'title': (30, 4.5, 40, 6), 'panel': (5, 16.5, 90, 46),
    'yield': (9, 24, 25, 5.5), 'date': (38, 24, 25, 5.5), 'time': (67, 24, 24, 5.5),
    'made': (9, 36, 40, 5.5), 'pack': (51, 36, 40, 5.5), 'comments': (9, 48, 82, 10), 'table': (5, 66, 90, 27),
}
LABELS = {'yield': 'Actual yield', 'date': 'Date finished', 'time': 'Time finished', 'made': 'Made by',
          'pack': 'Packaged by', 'comments': 'Misc. comments'}
HAND = {'date': '4/2/24', 'time': '2:36 pm'}
TESTS = [('QA-10', 'Visual inspection', 'Smooth surface, no bloom or air bubbles'),
         ('QA-11', 'Snap test', 'Clean, crisp break when snapped'),
         ('QA-12', 'Taste test', 'Balanced flavor, not overly bitter')]


def _target(name):
    """Target rect as % of the content box."""
    x0, y0, x1, y1 = TARGETS[name]
    return (x0 / EXPORT_W * 100, (y0 - SLICE_Y) / SLICE_H * 100, (x1 - x0 + 1) / EXPORT_W * 100, (y1 - y0 + 1) / SLICE_H * 100)


def _paper(name):
    """Paper rect (screen %) as % of the content box."""
    l, t, w, h = PAPER[name]
    bl, bt, bw, bh = BOX
    return ((l - bl) / bw * 100, (t - bt) / bh * 100, w / bw * 100, h / bh * 100)


def _vars(name):
    p = _paper(name) if name in PAPER else _target(name)
    s = _target(name)
    return ';'.join(f'--{a}:{v:.3f}%' for a, v in zip(('pl', 'pt', 'pw', 'ph', 'sl', 'st', 'sw', 'sh'), p + s))


def _stage(base='assets/screens'):
    """The animated stage (paper -> tablet), shared by the case-study hero and the landing's Procense card."""
    els = [f'<div class="ph-m ph-m--card" style="{_vars("card")}"></div>',
           f'<div class="ph-m ph-m--title" style="{_vars("title")}"><span class="ph-p ph-tp">QC Tests</span></div>',
           f'<div class="ph-m ph-m--button" style="{_vars("button")}"></div>',
           f'<div class="ph-m ph-m--panel" style="{_vars("panel")};--d:1"></div>']
    for k, name in enumerate(['yield', 'date', 'time', 'made', 'pack', 'comments']):
        hand = f'<span class="ph-p ph-hw ph-val" style="--i:{k}">{HAND[name]}</span>' if name in HAND else ''
        els.append(f'<div class="ph-m ph-m--field" style="{_vars(name)};--d:{k + 2}"><span class="ph-p ph-lab">{LABELS[name]}</span>{hand}</div>')
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td></td><td></td></tr>' for a, b, c in TESTS)
    els.append(f'<div class="ph-m ph-m--table" style="{_vars("table")};--d:8">'
               '<table class="ph-p"><colgroup><col style="width:11%"><col style="width:22%"><col style="width:41%"><col style="width:13%"><col style="width:13%"></colgroup>'
               '<thead><tr><th>Test ID</th><th>Test name</th><th>Standard</th><th>Result</th><th>Initials</th></tr></thead>'
               f'<tbody>{rows}</tbody></table><i class="ph-thead"></i></div>')
    paper_only = ('<p class="ph-po ph-meta">Batch No. <span class="ph-hw" style="--i:-2">32000102</span>'
                  '<span>Product <span class="ph-hw" style="--i:-1">Dark Chocolate</span></span></p>'
                  '<p class="ph-po ph-foot">Reviewed by ____________ &nbsp; Date __/__/__ &nbsp; Signature ____________</p>')
    slice_top = -SLICE_Y / EXPORT_H * 100
    return ('<div class="ph-stage" aria-hidden="true"><div class="ph-in"><div class="ph-obj">'
            '<div class="ph-bezel"></div><div class="ph-screen">'
            f'<img class="ph-base" src="{base}/landscape-qc-tests.webp" width="1536" height="1152" alt="" decoding="async">'
            '<div class="ph-mc">' + ''.join(els) + paper_only + '</div>'
            f'<div class="ph-view"><img src="{base}/landscape-qc-tests-scroll.webp" width="{EXPORT_W}" height="{EXPORT_H}" alt="" decoding="async" style="transform:translateY({slice_top:.4f}%)"></div>'
            '</div></div></div></div>')


def html():
    return ('  <div class="pm-media pm-media--21x9 cs-hero-well ph" data-ph role="img" '
            'aria-label="A paper quality form for a Dark Chocolate batch, filled in by hand, settles into a tablet; its sheet, sections, fields and test table glide into the shipped Digital Forms screen for the same form, where the date and time are filled in automatically.">'
            + _stage() + '</div>\n'
            # Set the start frame before first paint, so the final frame never flashes (no JS: the final frame stays)
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("ph--anim")})(document.querySelector("[data-ph]"))</script>\n')


# 1.5x export px -> u: the screen area is 49.8u wide for 1536 px, so 1 px = 0.03242u
_CSS = r"""
/* ===== Procense hero (procense_hero.py): paper elements land exactly on the shipped screen's elements ===== */
.ph { --u: 1cqw; container-type: inline-size; background: radial-gradient(120% 90% at 90% 100%, #2483FF 0%, rgb(36 131 255 / 0%) 60%), #1B2026; }
.ph-stage { position: absolute; left: 50%; top: 50%; width: 100u; height: 42.857u; transform: translate(-50%, -50%); }
@container (max-width: 599px) { .ph-stage { --u: 1.25cqw; } }
/* Final place: the whole tablet, level and centred (screen area 49.8 x 37.35u = 4:3, like the screen image) */
.ph-in { position: absolute; left: 24u; top: 1.65u; width: 52u; height: 39.55u; }
.ph-obj { position: absolute; inset: 0; transform-origin: 50% 50%; }
.ph-bezel { position: absolute; inset: 0; border-radius: 2.4u; background: #0D1117; box-shadow: 0 0 0 .12u rgb(255 255 255 / 9%), 0 2.6u 7u rgb(0 0 0 / 45%); }
.ph-screen { position: absolute; inset: 1.1u; overflow: hidden; border-radius: 1.3u; background: #FFFFFF; font-family: var(--font-sans); }
.ph-base { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }
/* The morph layer and the real slice share the content box exactly */
.ph-mc, .ph-view { position: absolute; left: 7.8125%; top: 7.2917%; width: 92.1875%; height: 82.1615%; }
.ph-mc { background: #F5F6F8; clip-path: inset(0); }
.ph-view { overflow: hidden; background: #FFFFFF; }
.ph-view img { display: block; width: 100%; height: auto; }
/* Morph boxes: at their shipped rects, in the shipped colours (the animation brings them in from paper) */
.ph-m { position: absolute; left: var(--sl); top: var(--st); width: var(--sw); height: var(--sh); box-sizing: border-box; }
.ph-p { opacity: 0; }
.ph-m--card { background: #FFFFFF; box-shadow: inset 0 0 0 .049u #E1E4EA; border-radius: .45u; }
.ph-m--title { display: grid; align-items: center; justify-items: center; overflow: visible; }
.ph-tp { white-space: nowrap; font-size: 1.9u; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: #2B2B2B; }
.ph-m--button { border-radius: .26u; background: #4A67E0; }
.ph-m--panel { border-radius: .45u; background: #F0F2F6; }
.ph-m--field { border: .049u solid #848C98; border-radius: .32u; background: #FFFFFF; }
.ph-lab { position: absolute; left: 0; bottom: 100%; margin-bottom: .45u; white-space: nowrap; font-size: .78u; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; color: #4A473F; }
.ph-val { position: absolute; left: .6u; bottom: .1u; font-size: 2u; }
.ph-m--table { overflow: hidden; border: .049u solid #E1E4EA; border-radius: .39u .39u 0 0; background: #FFFFFF; }
.ph-thead { position: absolute; inset: 0 0 auto; height: 2.33u; background: #F5F6F8; border-bottom: .049u solid #EBEDF1; }
.ph-m--table table { width: 100%; height: 100%; border-collapse: collapse; table-layout: fixed; font-size: .82u; color: #2B2B2B; }
.ph-m--table th, .ph-m--table td { border: .1u solid #8E8A7C; padding: .4u .6u; text-align: left; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
.ph-m--table th { background: #EFEDE4; font-weight: 600; font-size: .75u; }
/* Paper-only parts (header line, footer), in content-box coordinates */
.ph-po { position: absolute; margin: 0; font-size: .9u; color: #4A473F; opacity: 0; }
.ph-meta { left: -3%; right: 5.4%; top: 4.5%;  /* 5% paper margins on both sides of the sheet (content-box coordinates) */  display: flex; justify-content: space-between; align-items: baseline; }
.ph-meta .ph-hw { font-size: 1.9u; margin-left: .4u; }
.ph-foot { left: -3%; top: 107%; }
.ph-hw { display: inline-block; font-family: Caveat, "Bradley Hand", cursive; font-weight: 600; line-height: 1; color: #22356F; white-space: nowrap; }

/* ---- Timeline: write (0.6-1.8s), settle (1.8-3.0s), morph (2.7-4.1s) with the chrome in (3.0-3.9s),
        button (3.6-4.1s), bezel (3.2-4.2s), real text (3.95-4.5s, as the boxes settle) ---- */
.ph--anim .ph-in { animation: ph-in .7s cubic-bezier(.2,0,0,1) .1s both; }
.ph--anim .ph-obj { animation: ph-settle 1.2s cubic-bezier(.65,0,.35,1) 1.8s both; }
.ph--anim .ph-hw { animation: ph-write .5s cubic-bezier(.4,0,.2,1) both; animation-delay: calc(1.0s + var(--i, 0) * 220ms); }
.ph--anim .ph-po { animation: ph-out .5s ease-in 2.5s both; }
.ph--anim .ph-base { animation: ph-fade-in .9s ease-in-out 3.0s both; }
.ph--anim .ph-mc { animation: ph-mc 1.4s cubic-bezier(.65,0,.35,1) 2.7s both; }
.ph--anim .ph-m { animation: ph-geo 1.4s cubic-bezier(.65,0,.35,1) both; animation-delay: calc(2.7s + var(--d, 0) * 25ms); }
.ph--anim .ph-m--card { animation-name: ph-geo, ph-card; }
.ph--anim .ph-m--panel { animation-name: ph-geo, ph-panel; }
.ph--anim .ph-m--field { animation-name: ph-geo, ph-field; }
.ph--anim .ph-m--table { animation-name: ph-geo, ph-table; }
.ph--anim .ph-m--button { animation: ph-grow .5s cubic-bezier(.2,0,0,1) 3.6s both; }
.ph--anim .ph-thead { animation: ph-fade-in .6s ease-in-out 3.4s both; }
.ph--anim .ph-m .ph-p { animation: ph-out .55s ease-in both; animation-delay: calc(2.75s + var(--d, 0) * 25ms); }
.ph--anim .ph-m .ph-p.ph-hw { animation: ph-write .5s cubic-bezier(.4,0,.2,1) both, ph-out .55s ease-in both;
  animation-delay: calc(1.0s + var(--i, 0) * 220ms), calc(3.55s + var(--d, 0) * 25ms); }  /* handwriting rides along until just before landing */
.ph--anim .ph-bezel { animation: ph-bezel 1s cubic-bezier(.2,0,0,1) 3.2s both; }
.ph--anim .ph-view { animation: ph-fade-in .55s ease-in-out 3.95s both; }
/* Held at the start frame until the script says go */
.ph--anim:not(.is-play), .ph--anim:not(.is-play) * { animation-play-state: paused !important; }

@keyframes ph-in { from { opacity: 0; translate: 0 1.5u; } to { opacity: 1; translate: 0 0; } }
@keyframes ph-settle { from { transform: translate(var(--ph-sx, -15u), 1u) rotate(-5deg) scale(.8); } to { transform: none; } }  /* --ph-sx: where the sheet starts (the card starts it nearer) */
@keyframes ph-write { from { clip-path: inset(-25% 100% -25% 0); } to { clip-path: inset(-25% -5% -25% 0); } }
@keyframes ph-out { from { opacity: 1; } to { opacity: 0; } }
@keyframes ph-fade-in { from { opacity: 0; } to { opacity: 1; } }
@keyframes ph-grow { from { opacity: 0; transform: scale(.85); } to { opacity: 1; transform: none; } }
/* The paper sheet is the morph layer's card: no clip and no page colour until the boxes land */
@keyframes ph-mc { from { background-color: rgb(245 246 248 / 0%); clip-path: inset(-40% -40% -40% -40%); } to { background-color: #F5F6F8; clip-path: inset(0); } }
@keyframes ph-geo { from { left: var(--pl); top: var(--pt); width: var(--pw); height: var(--ph); } to { left: var(--sl); top: var(--st); width: var(--sw); height: var(--sh); } }
@keyframes ph-card { from { background: #FBFAF6; box-shadow: inset 0 0 0 .049u rgb(225 228 234 / 0%); border-radius: .4u; } to { background: #FFFFFF; box-shadow: inset 0 0 0 .049u #E1E4EA; border-radius: .45u; } }
@keyframes ph-panel { from { background: rgb(240 242 246 / 0%); box-shadow: inset 0 0 0 .1u #8E8A7C; border-radius: 0; } to { background: #F0F2F6; box-shadow: inset 0 0 0 .1u rgb(142 138 124 / 0%); border-radius: .45u; } }
@keyframes ph-field { from { border-width: 0 0 .1u; border-color: #8E8A7C; border-radius: 0; background: rgb(255 255 255 / 0%); } to { border-width: .049u; border-color: #848C98; border-radius: .32u; background: #FFFFFF; } }
@keyframes ph-table { from { border-color: rgb(225 228 234 / 0%); background: rgb(255 255 255 / 0%); border-radius: 0; } to { border-color: #E1E4EA; background: #FFFFFF; border-radius: .39u .39u 0 0; } }
@keyframes ph-bezel { from { opacity: 0; transform: scale(.97); } to { opacity: 1; transform: scale(1); } }
"""
CSS = re.sub(r'(?<![\w.#-])(-?(?:\d+(?:\.\d+)?|\.\d+))u\b', lambda m: f'calc({m.group(1)} * var(--u))', _CSS)

JS = r"""
  // Procense hero: start the timeline once, when the hero is in view, the tab is visible and the font and screens are ready
  (function () {
    var hero = document.querySelector('[data-ph].ph--anim'); if (!hero) return;
    var inView = false, ready = false, io = null;
    function go() {
      if (!ready || !inView || document.visibilityState !== 'visible' || hero.classList.contains('is-play')) return;
      hero.classList.add('is-play'); document.removeEventListener('visibilitychange', go); if (io) io.disconnect();
    }
    var r = hero.getBoundingClientRect(); inView = r.top < window.innerHeight && r.bottom > 0;
    if ('IntersectionObserver' in window) {
      io = new IntersectionObserver(function (es) { inView = es.some(function (e) { return e.isIntersecting; }); go(); }, { threshold: .4 });
      io.observe(hero);
    } else inView = true;
    document.addEventListener('visibilitychange', go);
    var imgs = [].map.call(hero.querySelectorAll('img'), function (i) { return i.decode ? i.decode().catch(function () {}) : 0; });
    var fonts = document.fonts ? document.fonts.ready : Promise.resolve();
    Promise.race([Promise.all(imgs.concat([fonts])), new Promise(function (res) { setTimeout(res, 1500); })]).then(function () { ready = true; go(); });
    // For checking from the console: restart the timeline
    hero.phReplay = function () { hero.getAnimations({ subtree: true }).forEach(function (a) { a.cancel(); a.play(); }); };
  })();
"""


# ---------- The same animation on the landing's Procense card ----------
def card(base='procense/assets/screens'):
    """The hero animation inside the landing card's screenshot slot. It rests on the final frame (the level tablet with
    the shipped QC tests screen) and plays from the start each time the Procense card becomes the active card."""
    return '<div class="ph ph--card" data-phc aria-hidden="true">' + _stage(base) + '</div>'

# In the slot: no navy fill (the card is already navy); the stage is larger than in the hero (1.48% of the slot's width
# per u, so the tablet is 77% of the slot, about 13% larger than before), and the starting sheet begins 2u nearer the centre so it stays in the slot.
CARD_CSS = """
.ph.ph--card { position: absolute; inset: 0; background: none; }
.ph--card .ph-stage { --u: 1.48cqw; --ph-sx: calc(-13 * var(--u)); }  /* tablet = 52u = 77% of the slot's width; the sheet starts 2u nearer so it stays inside the slot */
"""

CARD_JS = r"""
  // Procense card: rest on the final frame; replay the hero animation whenever the card becomes the active card
  (function () {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    document.querySelectorAll('[data-phc]').forEach(function (ph) {
      var shot = ph.closest('[data-active], .cx-img'); if (!shot) return;
      var imgs = [].slice.call(ph.querySelectorAll('img')).map(function (i) { return i.decode ? i.decode().catch(function () {}) : 0; });
      var ready = Promise.race([Promise.all(imgs.concat([document.fonts ? document.fonts.ready : 0])), new Promise(function (r) { setTimeout(r, 1500); })]);
      function active() { return shot.getAttribute('data-active') === 'true'; }
      function play() {
        ph.classList.remove('ph--anim', 'is-play'); void ph.offsetWidth; ph.classList.add('ph--anim');
        ready.then(function () { requestAnimationFrame(function () { if (active()) ph.classList.add('is-play'); }); });
      }
      function rest() { ph.classList.remove('ph--anim', 'is-play'); }
      new MutationObserver(function () { if (active()) { if (!ph.classList.contains('ph--anim')) play(); } else rest(); })
        .observe(shot, { attributes: true, attributeFilter: ['data-active'] });
      if (active()) play();
    });
  })();
"""
