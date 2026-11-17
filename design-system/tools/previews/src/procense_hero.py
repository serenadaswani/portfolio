"""Procense case-study hero: the paper form's elements become the shipped screen's elements.

On Procense's navy (the landing card's art), a paper QC tests form fills in by hand (batch number, product, then the
date and time finished). The sheet settles level into a tablet's place, and each part of it glides and reshapes into
its counterpart on Serena's real QC tests screen: the printed title into the "QC tests" heading, the bordered section
into the grey panel, each ruled field into its input box (the handwritten date and time become the auto-filled
04/02/2024 and 14:36), and the printed table into the test table. The bezel fades in, then the real screen fades in
over the morphed layout so the final frame is pixel-exact: the whole tablet, level (0deg), fully in frame.

Screen-element rects (MORPH, % of the screen) were measured on the shipped base image plus the matching slice of the
scroll export (content box 80, 56, 944, 631 in 1x px; slice from y = 540 of the 1.5x export).

One CSS timeline: the morph animates left/top/width/height of ten absolutely positioned boxes inside the tablet
(through custom properties), everything else is transform, opacity and clip-path; soft easing; about 4.8s, played once
when in view and the tab is visible. An inline script sets the start frame before first paint; no JS or reduced motion
show the final frame. Sized in --u (1% of the hero's width; a little larger on phones). Colours are project art.
"""
import re

HEAD = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&display=swap">'
        '<!-- Caveat: handwriting in the hero art only -->\n')

SCROLL_Y, SCROLL_H = 540, 2337  # slice start and height of the scroll export (1.5x px)

# name, kind, paper rect, screen rect (left, top, width, height in % of the screen), paper label, screen label,
# paper value (handwritten), screen value (typed; a leading ~ marks placeholder text)
MORPH = [
    ('title', 'title', (30, 4.5, 40, 6), (12.63, 7.64, 10.42, 3.56), '', '', 'QC Tests', 'QC tests'),
    ('panel', 'panel', (5, 16.5, 90, 46), (12.63, 18.75, 82.68, 57.03), '', '', '', ''),
    ('yield', 'field', (9, 24, 25, 5.5), (14.97, 26.04, 24.67, 6.16), 'Actual yield', 'Actual yield', '', '~Add number…'),
    ('date', 'field', (38, 24, 25, 5.5), (41.6, 26.04, 24.74, 6.16), 'Date finished', 'Date finished', '4/2/24', '04/02/2024'),
    ('time', 'field', (67, 24, 24, 5.5), (68.29, 26.04, 24.67, 6.16), 'Time finished', 'Time finished', '2:36 pm', '14:36'),
    ('made', 'field', (9, 36, 40, 5.5), (14.97, 42.97, 38.02, 6.25), 'Made by', 'Made by', '', '~Select operator'),
    ('pack', 'field', (51, 36, 40, 5.5), (54.95, 42.97, 38.02, 6.25), 'Packaged by', 'Packaged by', '', '~Select operator'),
    ('comments', 'field', (9, 48, 82, 10), (14.97, 55.99, 77.99, 16.67), 'Misc. comments', 'Misc. comments', '', '~Add comments here…'),
    ('table', 'table', (5, 66, 90, 27), (12.63, 78.91, 82.68, 29.08), '', '', '', ''),
]
TESTS = [('QA-10', 'Visual inspection', 'Smooth surface, no bloom or air bubbles'),
         ('QA-11', 'Snap test', 'Clean, crisp break when snapped'),
         ('QA-12', 'Taste test', 'Balanced flavor, not overly bitter')]


def _morph_el(k, item):
    name, kind, p, s, pl, sl, pv, sv = item
    style = ';'.join(f'--{a}:{v}%' for a, v in zip(('pl', 'pt', 'pw', 'ph', 'sl', 'st', 'sw', 'sh'), p + s)) + f';--d:{k}'
    inner = ''
    if kind == 'title':
        inner = f'<span class="ph-p ph-tp">{pv}</span><span class="ph-s ph-ts">{sv}</span>'
    elif kind == 'field':
        inner = (f'<span class="ph-lab ph-p">{pl}</span><span class="ph-lab ph-s">{sl}</span>'
                 + (f'<span class="ph-p ph-hw ph-val" style="--i:{k}">{pv}</span>' if pv else '')
                 + f'<span class="ph-s ph-val{" ph-val--ph" if sv.startswith("~") else ""}">{sv.lstrip("~")}</span>')
    elif kind == 'table':
        rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td></td><td></td></tr>' for a, b, c in TESTS)
        inner = ('<table class="ph-p"><colgroup><col style="width:11%"><col style="width:22%"><col style="width:41%"><col style="width:13%"><col style="width:13%"></colgroup>'
                 '<thead><tr><th>Test ID</th><th>Test name</th><th>Standard</th><th>Result</th><th>Initials</th></tr></thead>'
                 f'<tbody>{rows}</tbody></table>'
                 '<div class="ph-s ph-th"><span>Test ID</span><span>Test name</span><span>Standard</span><span>Result</span></div>')
    return f'<div class="ph-m ph-m--{kind} ph-m--{name}" style="{style}">{inner}</div>'


def html():
    morph = ''.join(_morph_el(k, it) for k, it in enumerate(MORPH))
    paper_only = ('<p class="ph-po ph-meta">Batch No. <span class="ph-hw" style="--i:-2">32000102</span>'
                  '<span>Product <span class="ph-hw" style="--i:-1">Dark Chocolate</span></span></p>'
                  '<p class="ph-po ph-foot">Reviewed by ____________ &nbsp; Date __/__/__ &nbsp; Signature ____________</p>')
    slice_top = -SCROLL_Y / SCROLL_H * 100
    shot = ('<div class="ph-shot"><img src="assets/screens/landscape-qc-tests.webp" width="1536" height="1152" alt="" decoding="async">'
            f'<div class="ph-view"><img src="assets/screens/landscape-qc-tests-scroll.webp" width="1416" height="{SCROLL_H}" alt="" decoding="async" style="transform:translateY({slice_top:.4f}%)"></div></div>')
    return ('  <div class="pm-media pm-media--21x9 cs-hero-well ph" data-ph role="img" '
            'aria-label="A paper quality form for a Dark Chocolate batch, filled in by hand, settles into a tablet; its title, fields and test table glide into the shipped Digital Forms screen for the same form, where the date and time are filled in automatically.">'
            '<div class="ph-stage" aria-hidden="true"><div class="ph-in"><div class="ph-obj">'
            '<div class="ph-bezel"></div><div class="ph-screen">' + paper_only + morph + shot + '</div>'
            '</div></div></div></div>\n'
            # Set the start frame before first paint, so the final frame never flashes (no JS: the final frame stays)
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("ph--anim")})(document.querySelector("[data-ph]"))</script>\n')


_CSS = r"""
/* ===== Procense hero (procense_hero.py): paper elements -> shipped screen elements ===== */
.ph { --u: 1cqw; container-type: inline-size; background: radial-gradient(120% 90% at 90% 100%, #2483FF 0%, rgb(36 131 255 / 0%) 60%), #1B2026; }
.ph-stage { position: absolute; left: 50%; top: 50%; width: 100u; height: 42.857u; transform: translate(-50%, -50%); }
@container (max-width: 599px) { .ph-stage { --u: 1.25cqw; } }
/* Final place: the whole tablet, level and centred (screen area 49.8 x 37.35u = 4:3, like the screen image) */
.ph-in { position: absolute; left: 24u; top: 1.65u; width: 52u; height: 39.55u; }
.ph-obj { position: absolute; inset: 0; transform-origin: 50% 50%; }
.ph-bezel { position: absolute; inset: 0; border-radius: 2.4u; background: #0D1117; box-shadow: 0 0 0 .12u rgb(255 255 255 / 9%), 0 2.6u 7u rgb(0 0 0 / 45%); }
.ph-screen { position: absolute; inset: 1.1u; overflow: hidden; border-radius: 1.3u; background: #F3F4F6; font-family: var(--font-sans); color: #1B2026; }
/* The shipped screen, faded in over the morphed layout at the end */
.ph-shot { position: absolute; inset: 0; z-index: 2; }
.ph-shot > img { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }
.ph-view { position: absolute; left: 7.8125%; top: 7.2917%; width: 92.1875%; height: 82.1615%; overflow: hidden; background: #FFFFFF; }
.ph-view img { display: block; width: 100%; height: auto; }
/* Morphing boxes: placed at their screen rects; the animation brings them in from their paper rects */
.ph-m { position: absolute; left: var(--sl); top: var(--st); width: var(--sw); height: var(--sh); box-sizing: border-box; }
.ph-p { opacity: 0; } .ph-s { opacity: 1; }
.ph-m--title { display: grid; align-items: center; }
.ph-tp, .ph-ts { grid-area: 1 / 1; white-space: nowrap; }
.ph-tp { justify-self: center; font-size: 1.9u; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: #2B2B2B; }
.ph-ts { font-size: 1.45u; font-weight: 600; }
.ph-m--panel { border-radius: .45u; background: #E9EBEF; }
.ph-m--field { display: flex; align-items: center; padding: 0 .55u; border: .1u solid #C9CED6; border-radius: .35u; background: #FFFFFF; }
.ph-m--comments { align-items: flex-start; padding-top: .5u; }
.ph-lab { position: absolute; left: 0; bottom: 100%; margin-bottom: .45u; white-space: nowrap; }
.ph-lab.ph-p { font-size: .78u; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; color: #4A473F; }
.ph-lab.ph-s { font-size: .86u; font-weight: 500; }
.ph-val { position: absolute; left: .6u; white-space: nowrap; font-size: .82u; }
.ph-val.ph-s { top: 50%; translate: 0 -50%; } .ph-val--ph { color: #6B7280; }
.ph-m--comments .ph-val.ph-s { top: .7u; translate: none; }
.ph-val.ph-hw { bottom: .1u; font-size: 2u; }
.ph-m--table { overflow: hidden; border: .1u solid #D9DDE3; border-radius: .45u; background: #FFFFFF; }
.ph-m--table table { width: 100%; height: 100%; border-collapse: collapse; table-layout: fixed; font-size: .82u; color: #2B2B2B; }
.ph-m--table th, .ph-m--table td { border: .1u solid #8E8A7C; padding: .4u .6u; text-align: left; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
.ph-m--table th { background: #EFEDE4; font-weight: 600; font-size: .75u; }
.ph-th { position: absolute; inset: 0 0 auto; display: grid; grid-template-columns: 11% 18% 39% 32%; align-items: center; height: 2.4u; padding: 0 .7u; background: #F6F7F9; border-bottom: .1u solid #E5E7EB; font-size: .72u; color: #4B5563; }
/* Paper-only parts (header line, footer) */
.ph-po { position: absolute; margin: 0; font-size: .9u; color: #4A473F; opacity: 0; }
.ph-meta { left: 5%; right: 5%; top: 11%; display: flex; justify-content: space-between; align-items: baseline; }
.ph-meta .ph-hw { font-size: 1.9u; margin-left: .4u; }
.ph-foot { left: 5%; top: 95%; }
.ph-hw { display: inline-block; font-family: Caveat, "Bradley Hand", cursive; font-weight: 600; line-height: 1; color: #22356F; white-space: nowrap; }

/* ---- The timeline: write (0.7-2.0s), settle (1.9-3.1s), morph (2.7-4.3s), bezel (3.3s), real screen (4.1-4.8s) ---- */
.ph--anim .ph-in { animation: ph-in .7s cubic-bezier(.2,0,0,1) .1s both; }
.ph--anim .ph-obj { animation: ph-settle 1.2s cubic-bezier(.65,0,.35,1) 1.9s both; }
.ph--anim .ph-screen { animation: ph-sheet 1.2s cubic-bezier(.65,0,.35,1) 2.5s both; }
.ph--anim .ph-po { animation: ph-out .5s ease-in 2.6s both; }
.ph--anim .ph-po .ph-hw, .ph--anim .ph-p.ph-hw { animation: ph-write .5s cubic-bezier(.4,0,.2,1) both; animation-delay: calc(1.05s + var(--i, 0) * 220ms); }
.ph--anim .ph-m { animation: ph-geo 1.3s cubic-bezier(.65,0,.35,1) both; animation-delay: calc(2.7s + var(--d) * 45ms); }
.ph--anim .ph-m--field { animation-name: ph-geo, ph-field; }
.ph--anim .ph-m--panel { animation-name: ph-geo, ph-panel; }
.ph--anim .ph-m--table { animation-name: ph-geo, ph-table; }
.ph--anim .ph-m .ph-p:not(.ph-hw) { animation: ph-out-p 1.3s linear both; animation-delay: calc(2.7s + var(--d) * 45ms); }
.ph--anim .ph-m .ph-p.ph-hw { animation: ph-write .5s cubic-bezier(.4,0,.2,1) both, ph-out-p 1.3s linear both;
  animation-delay: calc(1.05s + var(--i, 0) * 220ms), calc(2.7s + var(--d) * 45ms); }
.ph--anim .ph-m .ph-s { animation: ph-in-s 1.3s linear both; animation-delay: calc(2.7s + var(--d) * 45ms); }
.ph--anim .ph-bezel { animation: ph-bezel 1s cubic-bezier(.2,0,0,1) 3.3s both; }
.ph--anim .ph-shot { animation: ph-shot .7s ease-in-out 4.1s both; }
/* Held at the start frame until the script says go */
.ph--anim:not(.is-play) *, .ph--anim:not(.is-play) { animation-play-state: paused !important; }

@keyframes ph-in { from { opacity: 0; translate: 0 1.5u; } to { opacity: 1; translate: 0 0; } }
@keyframes ph-settle { from { transform: translate(-15u, 1u) rotate(-5deg) scale(.8); } to { transform: none; } }
@keyframes ph-sheet { from { background: #FBFAF6; border-radius: .4u; } to { background: #F3F4F6; border-radius: 1.3u; } }
@keyframes ph-write { from { clip-path: inset(-25% 100% -25% 0); } to { clip-path: inset(-25% -5% -25% 0); } }
@keyframes ph-out { from { opacity: 1; } to { opacity: 0; } }
@keyframes ph-geo { from { left: var(--pl); top: var(--pt); width: var(--pw); height: var(--ph); } to { left: var(--sl); top: var(--st); width: var(--sw); height: var(--sh); } }
@keyframes ph-field { from { border-color: transparent transparent #8E8A7C; border-radius: 0; background: rgb(255 255 255 / 0%); } to { border-color: #C9CED6; border-radius: .35u; background: #FFFFFF; } }
@keyframes ph-panel { from { background: rgb(233 235 239 / 0%); box-shadow: inset 0 0 0 .1u #8E8A7C; border-radius: 0; } to { background: #E9EBEF; box-shadow: inset 0 0 0 0 rgb(142 138 124 / 0%); border-radius: .45u; } }
@keyframes ph-table { from { border-color: transparent; background: rgb(255 255 255 / 0%); border-radius: 0; } to { border-color: #D9DDE3; background: #FFFFFF; border-radius: .45u; } }
/* Overlapping cross-fade, so the elements never go pale mid-morph */
@keyframes ph-out-p { 0%, 25% { opacity: 1; } 62% { opacity: 0; } 100% { opacity: 0; } }
@keyframes ph-in-s { 0%, 30% { opacity: 0; } 62% { opacity: 1; } 100% { opacity: 1; } }
@keyframes ph-bezel { from { opacity: 0; transform: scale(.97); } to { opacity: 1; transform: scale(1); } }
@keyframes ph-shot { from { opacity: 0; } to { opacity: 1; } }
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
    hero.phReplay = function () {
      hero.getAnimations({ subtree: true }).forEach(function (a) { a.cancel(); a.play(); });
    };
  })();
"""
