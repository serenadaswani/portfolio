"""Procense case-study hero: from a handwritten batch form to the shipped tablet screens.

On Procense's navy (the landing card's art), a paper QC batch form, styled like Fig. 2, fills itself in by hand: the
same date, time and initials on every row. Then Serena's real production screen rises in front of it in a tablet
frame: the landscape QC tests screen (date and time auto-filled), cropped
by the hero's edges so the flow stays for later. The paper steps back, staying fully opaque (a translucent paper read as a grey card).

One CSS timeline, transforms and opacity only, long expo-out easing: about 4.5s, played once when the hero is in view
and the tab is visible, then it holds. No JS, or reduced motion: the final frame. Sized in --u (1% of the hero's width;
larger on phones so the scene crops in and stays legible). Colours are project art (navy, paper, pen ink), like the
landing cards and the mockups. The form's tests come from the shipped QC tests screen.
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
    rows, i = '', 0
    for k, (test, spec, time, result) in enumerate(ROWS):
        rows += (f'<tr><td>{_hw("4/2/24", i)}</td><td>{_hw(time, i + 1)}</td><td>{test}</td><td>{spec}</td>'
                 f'<td>{_hw(result, i + 2)}</td><td>{_hw("JF" if result else "", i + 3)}</td></tr>')
        i += 4
    paper = ('<div class="ph-paper"><p class="ph-pt">QC Batch Performance</p>'
             f'<p class="ph-pm"><span>Batch No. {_hw("32000102", 0)}</span><span>Product {_hw("Dark Chocolate", 1)}</span></p>'
             '<table><colgroup><col style="width:13%"><col style="width:10%"><col style="width:25%"><col style="width:28%"><col style="width:12%"><col style="width:12%"></colgroup>'
             '<thead><tr><th>Date</th><th>Time</th><th>Test</th><th>Standard</th><th>Result</th><th>Initials</th></tr></thead>'
             f'<tbody>{rows}</tbody></table>'
             '<p class="ph-pm ph-pf">Reviewed by ____________ &nbsp; Date __/__/__ &nbsp; Signature ____________</p></div>')
    dev = lambda cls, src, w, h: (f'<div class="ph-dev {cls}"><img src="assets/screens/{src}" width="{w}" height="{h}" alt="" decoding="async"></div>')
    return ('  <div class="pm-media pm-media--21x9 cs-hero-well ph" data-ph role="img" '
            'aria-label="A paper batch quality form, filled in by hand with the same date, time and initials on every row, steps back as a tablet screen from the shipped Digital Forms application rises in front of it.">'
            '<div class="ph-stage" aria-hidden="true">'
            + paper
            + dev('ph-dev--ls', 'landscape-qc-tests.webp', 1536, 1152)
            + '</div></div>\n'
            # Set the start frame before first paint, so the final frame never flashes (no JS: the final frame stays)
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("ph--anim")})(document.querySelector("[data-ph]"))</script>\n')


_CSS = r"""
/* ===== Procense hero (procense_hero.py): handwritten form -> shipped tablet screens ===== */
.ph { --u: 1cqw; container-type: inline-size; background: radial-gradient(120% 90% at 90% 100%, #2483FF 0%, rgb(36 131 255 / 0%) 60%), #1B2026; }
.ph-stage { position: absolute; left: 50%; top: 50%; width: 100u; height: 42.857u; transform: translate(-50%, -50%); }
@container (max-width: 599px) { .ph-stage { --u: 1.45cqw; } }
/* Paper: the Fig. 2 form, filled in by hand (final frame: stepped back) */
.ph-paper { position: absolute; left: 4u; top: 5.5u; width: 45u; padding: 2.4u 2.6u 2u; background: #FBFAF6; color: #2B2B2B;
  font-family: var(--font-sans); border-radius: .25u; box-shadow: 0 .3u .8u rgb(0 0 0 / 25%), 0 2.4u 6u rgb(0 0 0 / 35%);
  transform: translate(-2u, .8u) rotate(-4deg) scale(.97); }
.ph-pt { margin: 0 0 1.1u; text-align: center; font-size: 1.35u; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }
.ph-pm { display: flex; justify-content: space-between; align-items: baseline; margin: 0 0 1u; font-size: .9u; color: #4A473F; }
.ph-pm > span { display: flex; align-items: baseline; gap: .6u; }
.ph-pf { margin: 1.3u 0 0; justify-content: flex-start; }
.ph-paper table { width: 100%; border-collapse: collapse; table-layout: fixed; font-size: .82u; }
.ph-paper th, .ph-paper td { border: .08u solid #8E8A7C; padding: .55u .6u; text-align: left; vertical-align: middle; height: 3u; overflow: hidden; white-space: nowrap; }
.ph-paper th { background: #EFEDE4; font-weight: 600; font-size: .78u; }
.ph-hw { display: inline-block; font-family: Caveat, "Bradley Hand", cursive; font-weight: 600; font-size: 1.75u; line-height: .9; color: #22356F; white-space: nowrap; }
.ph-pm .ph-hw { font-size: 1.9u; }
/* Devices: Serena's production screens in tablet frames, cropped by the hero's edges */
.ph-dev { position: absolute; padding: 1.1u; border-radius: 2.2u; background: #0D1117; box-shadow: 0 0 0 .12u rgb(255 255 255 / 9%), 0 3u 8u rgb(0 0 0 / 45%); }
.ph-dev img { display: block; width: 100%; height: auto; border-radius: 1.1u; }
.ph-dev--ls { left: 52u; top: 3.5u; width: 56u; transform: rotate(-3deg); }

/* The timeline (start frame set before first paint by the inline script; runs once .is-play is added) */
.ph--anim .ph-paper { animation: ph-paper 4.6s cubic-bezier(.45,0,.2,1) both paused; }
.ph--anim .ph-hw { animation: ph-write .5s cubic-bezier(.4,0,.2,1) both paused; animation-delay: calc(.55s + var(--i, 0) * 70ms); }
.ph--anim .ph-dev--ls { animation: ph-rise-ls 1.7s cubic-bezier(.16,1,.3,1) 2.05s both paused; }
.ph--anim.is-play .ph-paper, .ph--anim.is-play .ph-hw, .ph--anim.is-play .ph-dev { animation-play-state: running; }
@keyframes ph-paper {
  0% { opacity: 0; transform: translate(4u, 2u) rotate(-2deg) scale(1); }
  12% { opacity: 1; transform: translate(4u, 0) rotate(-2.5deg) scale(1); }
  46% { opacity: 1; transform: translate(4u, 0) rotate(-2.5deg) scale(1); }
  100% { opacity: 1; transform: translate(-2u, .8u) rotate(-4deg) scale(.97); }
}
@keyframes ph-write { from { clip-path: inset(-20% 100% -20% 0); } to { clip-path: inset(-20% -5% -20% 0); } }
@keyframes ph-rise-ls { from { opacity: 0; transform: translate(6u, 26u) rotate(4deg); } to { opacity: 1; transform: rotate(-3deg); } }
"""
CSS = re.sub(r'(?<![\w.#-])(-?(?:\d+(?:\.\d+)?|\.\d+))u\b', lambda m: f'calc({m.group(1)} * var(--u))', _CSS)

JS = r"""
  // Procense hero: start the timeline once, when the hero is in view and the tab is visible
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
    var fonts = document.fonts ? Promise.race([document.fonts.ready, new Promise(function (res) { setTimeout(res, 700); })]) : Promise.resolve();
    fonts.then(function () { ready = true; go(); });
    // For checking from the console: restart the timeline
    hero.phReplay = function () {
      hero.querySelectorAll('.ph-paper, .ph-hw, .ph-dev').forEach(function (e) { e.style.animation = 'none'; void e.offsetWidth; e.style.animation = ''; });
      hero.classList.add('is-play');
    };
  })();
"""
