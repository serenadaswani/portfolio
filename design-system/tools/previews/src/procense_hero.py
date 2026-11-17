"""Procense case-study hero: the paper becomes the tablet.

One object, start to finish. On Procense's navy (the landing card's art), a paper QC batch form, styled like Fig. 2,
fills itself in by hand: batch number, product, then the same date, time and initials on every row of the shipped QC
tests. The sheet then lifts, flattens and turns as it glides right into the tablet's place. A thin blue scan line sweeps
across it, and behind the line the paper becomes Serena's real QC tests screen (date and time auto-filled) while the
bezel grows in around it. It holds on the tablet, cropped by the hero's right and bottom edges.

One CSS timeline (transforms, opacity and clip-path only; soft easing): about 4.7s, played once when the hero is in
view and the tab is visible. An inline script sets the start frame before first paint; no JS or reduced motion show the
final frame. Sized in --u (1% of the hero's width; a little larger on phones). Colours are project art (navy, paper,
pen ink, the scan line's Procense blue), like the landing cards and the mockups.
"""
import re

HEAD = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&display=swap">'
        '<!-- Caveat: handwriting in the hero art only -->\n')

# Test, standard (from the shipped QC tests screen), handwritten time and result
ROWS = [('Visual inspection', 'No bloom or air bubbles', '2:31', 'Pass'),
        ('Snap test', 'Clean, crisp break', '2:33', 'Pass'),
        ('Taste test', 'Balanced, not bitter', '2:34', 'Pass'),
        ('Set test', 'Set within 2 hours', '2:36', 'OK'),
        ('Packaging', 'Sealed and labeled', '2:38', '')]


def _hw(text, i):
    return f'<span class="ph-hw" style="--i:{i}">{text}</span>' if text else ''


def html():
    rows, i = '', 2
    for test, spec, time, result in ROWS:
        rows += (f'<tr><td>{_hw("4/2/24", i)}</td><td>{_hw(time, i + 1)}</td><td>{test}</td><td>{spec}</td>'
                 f'<td>{_hw(result, i + 2)}</td><td>{_hw("JF" if result else "", i + 3)}</td></tr>')
        i += 4
    paper = ('<div class="ph-paper"><p class="ph-pt">QC Batch Performance</p>'
             f'<p class="ph-pm"><span>Batch No. {_hw("32000102", 0)}</span><span>Product {_hw("Dark Chocolate", 1)}</span></p>'
             '<table><colgroup><col style="width:13%"><col style="width:10%"><col style="width:24%"><col style="width:29%"><col style="width:12%"><col style="width:12%"></colgroup>'
             '<thead><tr><th>Date</th><th>Time</th><th>Test</th><th>Standard</th><th>Result</th><th>Initials</th></tr></thead>'
             f'<tbody>{rows}</tbody></table>'
             '<p class="ph-pm ph-pf">Reviewed by ____________ &nbsp; Date __/__/__ &nbsp; Signature ____________</p></div>')
    return ('  <div class="pm-media pm-media--21x9 cs-hero-well ph" data-ph role="img" '
            'aria-label="A paper batch quality form, filled in by hand with the same date, time and initials on every row, glides into place and turns into the shipped Digital Forms tablet screen, where the date and time are filled in automatically.">'
            '<div class="ph-stage" aria-hidden="true"><div class="ph-in"><div class="ph-obj">'
            '<div class="ph-bezel"></div>'
            '<div class="ph-screen">' + paper
            + '<img class="ph-shot" src="assets/screens/landscape-qc-tests.webp" width="1536" height="1152" alt="" decoding="async">'
            '<div class="ph-scanw"><i class="ph-scan"></i></div>'
            '</div></div></div></div></div>\n'
            # Set the start frame before first paint, so the final frame never flashes (no JS: the final frame stays)
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("ph--anim")})(document.querySelector("[data-ph]"))</script>\n')


_CSS = r"""
/* ===== Procense hero (procense_hero.py): the paper becomes the tablet ===== */
.ph { --u: 1cqw; container-type: inline-size; background: radial-gradient(120% 90% at 90% 100%, #2483FF 0%, rgb(36 131 255 / 0%) 60%), #1B2026; }
.ph-stage { position: absolute; left: 50%; top: 50%; width: 100u; height: 42.857u; transform: translate(-50%, -50%); }
@container (max-width: 599px) { .ph-stage { --u: 1.15cqw; } }
/* The object, in its final place: a tablet, cropped by the hero's right and bottom edges */
.ph-in { position: absolute; left: 26u; top: -9u; width: 72u; height: 54.55u; }  /* screen area 69.8 x 52.35u = 4:3, like the screen image; cropped at the top so the auto-filled fields show */
.ph-obj { position: absolute; inset: 0; transform: rotate(-3deg); transform-origin: 50% 50%; }
.ph-bezel { position: absolute; inset: 0; border-radius: 2.8u; background: #0D1117; box-shadow: 0 0 0 .12u rgb(255 255 255 / 9%), 0 3u 8u rgb(0 0 0 / 45%); }
.ph-screen { position: absolute; inset: 1.1u; overflow: hidden; border-radius: 1.4u; background: #FBFAF6; }
.ph-shot { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }
.ph-scanw { position: absolute; inset: 0; pointer-events: none; opacity: 0; }
.ph-scan { position: absolute; top: 0; bottom: 0; right: 0; width: .3u; background: #6EA2FF; box-shadow: 0 0 1.4u .4u rgb(36 131 255 / 70%), 0 0 4u 1u rgb(36 131 255 / 35%); }
/* Paper: the Fig. 2 form, filled in by hand, filling the screen area */
.ph-paper { position: absolute; inset: 0; padding: 3.4u 4.2u 2.6u; background: #FBFAF6; color: #2B2B2B; font-family: var(--font-sans); }
.ph-pt { margin: 0 0 1.8u; text-align: center; font-size: 2.2u; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }
.ph-pm { display: flex; justify-content: space-between; align-items: baseline; margin: 0 0 1.7u; font-size: 1.4u; color: #4A473F; }
.ph-pm > span { display: flex; align-items: baseline; gap: .7u; }
.ph-pf { margin: 2u 0 0; justify-content: flex-start; }
.ph-paper table { width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 1.3u; }
.ph-paper th, .ph-paper td { border: .1u solid #8E8A7C; padding: .9u 1u; text-align: left; vertical-align: middle; height: 5.3u; overflow: hidden; white-space: nowrap; }
.ph-paper th { height: 4.1u; background: #EFEDE4; font-weight: 600; font-size: 1.22u; }
.ph-hw { display: inline-block; font-family: Caveat, "Bradley Hand", cursive; font-weight: 600; font-size: 2.85u; line-height: .9; color: #22356F; white-space: nowrap; }
.ph-pm .ph-hw { font-size: 3u; }

/* The timeline: write (0.5-2.1s), glide (2.1-3.6s), scan and bezel (3.3-4.7s). Start frame comes from the 0% keyframes. */
.ph--anim .ph-in { animation: ph-in .7s cubic-bezier(.2,0,0,1) .1s both paused; }
.ph--anim .ph-hw { animation: ph-write .42s cubic-bezier(.4,0,.2,1) both paused; animation-delay: calc(.5s + var(--i, 0) * 50ms); }
.ph--anim .ph-obj { animation: ph-glide 1.5s cubic-bezier(.65,0,.35,1) 2.1s both paused; }
.ph--anim .ph-screen { animation: ph-sheet 1.5s cubic-bezier(.65,0,.35,1) 2.1s both paused; }
.ph--anim .ph-bezel { animation: ph-bezel .9s cubic-bezier(.2,0,0,1) 3.35s both paused; }
.ph--anim .ph-shot { animation: ph-reveal 1.25s cubic-bezier(.45,0,.25,1) 3.4s both paused; }
.ph--anim .ph-scanw { animation: ph-scan 1.25s cubic-bezier(.45,0,.25,1) 3.4s both paused; }
.ph--anim.is-play .ph-in, .ph--anim.is-play .ph-hw, .ph--anim.is-play .ph-obj, .ph--anim.is-play .ph-screen,
.ph--anim.is-play .ph-bezel, .ph--anim.is-play .ph-shot, .ph--anim.is-play .ph-scanw { animation-play-state: running; }
@keyframes ph-in { from { opacity: 0; translate: 0 1.5u; } to { opacity: 1; translate: 0 0; } }
@keyframes ph-write { from { clip-path: inset(-25% 100% -25% 0); } to { clip-path: inset(-25% -5% -25% 0); } }
/* From a sheet lying on the left (smaller, tilted the other way) to the tablet's place */
@keyframes ph-glide { from { transform: translate(-35u, 3u) rotate(-7deg) scale(.6); } to { transform: rotate(-3deg); } }
@keyframes ph-sheet { from { border-radius: .4u; box-shadow: 0 .3u .8u rgb(0 0 0 / 25%), 0 2.4u 6u rgb(0 0 0 / 35%); }
                      to { border-radius: 1.4u; box-shadow: 0 0 0 rgb(0 0 0 / 0%), 0 0 0 rgb(0 0 0 / 0%); } }
@keyframes ph-bezel { from { opacity: 0; transform: scale(.965); } to { opacity: 1; transform: scale(1); } }
@keyframes ph-reveal { from { clip-path: inset(0 100% 0 0); } to { clip-path: inset(0 0 0 0); } }
@keyframes ph-scan { 0% { opacity: 0; transform: translateX(-100%); } 8% { opacity: 1; } 88% { opacity: 1; } 100% { opacity: 0; transform: translateX(0); } }
"""
CSS = re.sub(r'(?<![\w.#-])(-?(?:\d+(?:\.\d+)?|\.\d+))u\b', lambda m: f'calc({m.group(1)} * var(--u))', _CSS)

JS = r"""
  // Procense hero: start the timeline once, when the hero is in view, the tab is visible and the handwriting font is ready
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
    var shot = hero.querySelector('.ph-shot');
    var imgReady = shot.decode ? shot.decode().catch(function () {}) : Promise.resolve();
    var fonts = document.fonts ? document.fonts.ready : Promise.resolve();
    Promise.race([Promise.all([fonts, imgReady]), new Promise(function (res) { setTimeout(res, 1200); })]).then(function () { ready = true; go(); });
    // For checking from the console: restart the timeline
    hero.phReplay = function () {
      hero.querySelectorAll('.ph-in, .ph-hw, .ph-obj, .ph-screen, .ph-bezel, .ph-shot, .ph-scanw').forEach(function (e) { e.style.animation = 'none'; void e.offsetWidth; e.style.animation = ''; });
      hero.classList.add('is-play');
    };
  })();
"""
