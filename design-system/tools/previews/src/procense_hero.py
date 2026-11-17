"""Procense case-study hero: "handwriting becomes data".

A paper batch record on Procense's navy (the landing card's art). Handwritten date, time and initials write themselves
in, lift off the paper and land, typed, in auto-filled fields on a tablet, which ends on a tight, angled crop. Plays once
when the hero comes into view (about 4s), then holds the final frame. Without JS, or with reduced motion, it shows the
final frame. Everything is HTML/CSS, sized in --u (1% of the hero's width; larger on phones so the art stays legible).
Colours here are project art (Procense's navy, paper, pen ink and UI blue), like the landing cards and the mockups.
Values match the final QC tests screen: 04/02/2024, 14:36, J. Fischer.
"""
import re

HEAD = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&display=swap">'
        '<!-- Caveat: handwriting in the hero art only -->\n')

# (paper label, handwritten value, tablet label, typed value, auto-filled helper)
FIELDS = [('Date', '4/2/24', 'Date finished', '04/02/2024', True),
          ('Time', '2:36 pm', 'Time finished', '14:36', True),
          ('Initials', 'JF', 'Made by', 'J. Fischer', False)]

CHECK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>')


def html():
    paper_rows = ''.join(f'<div class="ph-pf"><span class="ph-pl">{pl}</span><span class="ph-hw" data-k="{k}">{hw}</span></div>'
                         for k, (pl, hw, tl, tv, auto) in enumerate(FIELDS))
    tab_fields = ''.join(f'<div class="ph-tf"><span class="ph-tl">{tl}</span><span class="ph-in"><span class="ph-tv" data-k="{k}">{tv}</span></span>'
                         + (f'<span class="ph-help">Auto-filled from line tracking</span>' if auto else '') + '</div>'
                         for k, (pl, hw, tl, tv, auto) in enumerate(FIELDS))
    return (
        '  <div class="pm-media pm-media--21x9 cs-hero-well ph" data-ph role="img" '
        'aria-label="Handwritten date, time and initials on a paper batch record lift off the page and land as auto-filled fields on a tablet.">'
        '<div class="ph-stage" aria-hidden="true">'
        # Paper: a fragment of the batch record, with blank lines either side of the three entries
        '<div class="ph-paper"><p class="ph-pt">QC Batch Performance</p>'
        '<div class="ph-lines"><i></i><i></i></div>'
        f'<div class="ph-prow">{paper_rows}</div>'
        '<div class="ph-lines"><i></i><i></i><i></i></div></div>'
        # Tablet: cropped by the hero's right and bottom edges
        '<div class="ph-tab"><div class="ph-scr">'
        '<p class="ph-crumb">Forms <b>›</b> <span>Dark Chocolate – Batch QC Form</span></p>'
        f'<p class="ph-h">QC tests <span class="ph-ok">{CHECK}</span></p>'
        f'<div class="ph-panel"><div class="ph-trow">{tab_fields}</div>'
        '<div class="ph-ghost"><i></i><i></i></div></div>'
        '</div></div>'
        '</div></div>\n')


_CSS = r"""
/* ===== Procense hero (procense_hero.py): handwriting becomes data ===== */
.ph { --u: 1cqw; container-type: inline-size; background: radial-gradient(120% 90% at 90% 100%, #2483FF 0%, rgb(36 131 255 / 0%) 60%), #1B2026; }
@container (max-width: 599px) { .ph-stage { --u: 1.3cqw; } }
.ph-stage { position: absolute; left: 50%; top: 50%; width: 100u; height: 42.857u; transform: translate(-50%, -50%); font-family: var(--font-sans); }
/* Paper */
.ph-paper { position: absolute; left: 7u; top: 8u; width: 38u; padding: 2.6u 3u; background: #FBFAF6; color: #2B2B2B; border-radius: .3u;
  box-shadow: 0 .3u .8u rgb(0 0 0 / 25%), 0 2u 5u rgb(0 0 0 / 30%); transform: rotate(-4deg); transform-origin: 50% 50%; }
.ph-pt { margin: 0 0 1.6u; font-size: 1.15u; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; }
.ph-lines { display: grid; gap: 2.1u; } .ph-lines i { display: block; height: .1u; background: #CFCAB8; }
.ph-lines i:nth-child(2) { width: 70%; } .ph-lines i:nth-child(3) { width: 85%; }
.ph-prow { display: grid; grid-template-columns: 1.1fr 1.1fr .8fr; gap: 2u; margin: 2.4u 0; }
.ph-pf { display: grid; gap: .5u; border-bottom: .1u solid #8E8A7C; padding-bottom: .4u; }
.ph-pl { font-size: 1u; color: #6B675C; }
.ph-hw { justify-self: start; font-family: Caveat, "Bradley Hand", cursive; font-weight: 600; font-size: 3.1u; line-height: 1; color: #22356F; white-space: nowrap; }
/* Tablet */
.ph-tab { position: absolute; left: 52u; top: 7u; width: 56u; height: 42u; padding: 1.3u; border-radius: 2.2u; background: #0D1117;
  box-shadow: 0 0 0 .15u rgb(255 255 255 / 8%), 0 3u 8u rgb(0 0 0 / 45%); transform: rotate(-2deg); transform-origin: 0 0; }
.ph-scr { height: 100%; border-radius: 1u; background: #FFFFFF; color: #1B2026; overflow: hidden; padding: 2u 2.6u; }
.ph-crumb { margin: 0 0 2u; padding-bottom: 1.4u; border-bottom: .1u solid #E5E7EB; font-size: 1.05u; color: #4B5563; }
.ph-crumb b { font-weight: 400; margin: 0 .4u; } .ph-crumb span { color: #3E5BD9; }
.ph-h { display: flex; align-items: center; gap: 1u; margin: 0 0 1.6u; font-size: 2.2u; font-weight: 600; }
.ph-ok { display: grid; place-items: center; width: 2.2u; height: 2.2u; border-radius: 50%; background: #3E5BD9; color: #FFFFFF; }
.ph-ok svg { width: 1.3u; height: 1.3u; }
.ph-panel { padding: 2u; border-radius: .8u; background: #F3F4F6; }
.ph-trow { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.6u; }
.ph-tf { display: grid; gap: .7u; align-content: start; }
.ph-tl { font-size: 1.15u; font-weight: 500; }
.ph-in { display: flex; align-items: center; height: 3.6u; padding: 0 1.1u; border: .1u solid #C9CED6; border-radius: .5u; background: #FFFFFF; }
.ph-tv { font-size: 1.35u; white-space: nowrap; }
.ph-help { font-size: .95u; color: #6B7280; }
.ph-ghost { display: grid; gap: 1.2u; margin-top: 2.4u; } .ph-ghost i { display: block; height: 3.6u; border-radius: .5u; background: #FFFFFF; box-shadow: inset 0 0 0 .1u #D9DDE3; }
.ph-ghost i:first-child { width: 62%; }
/* Flyers: a handwritten value in flight, cross-fading to its typed form (created by the script) */
.ph-fly { position: absolute; left: 0; top: 0; pointer-events: none; transform-origin: 0 0; white-space: nowrap; }
.ph-fly > span { position: absolute; left: 0; top: 0; }
.ph-fly .ph-hw { color: #22356F; }
.ph-fly .ph-tv { color: #1B2026; }
/* Armed (before playing): only the paper shows, its entries unwritten */
.ph.is-armed .ph-hw { clip-path: inset(0 100% 0 0); }
.ph.is-armed .ph-tab { opacity: 0; translate: 6u 0; }
.ph.is-armed .ph-tv, .ph.is-armed .ph-help, .ph.is-armed .ph-ok { opacity: 0; }
/* Final frame (also the static state): the paper steps back, the tablet holds */
.ph:not(.is-armed) .ph-paper { opacity: .6; translate: -2u .6u; scale: .96; }
.ph:not(.is-armed) .ph-paper .ph-hw { opacity: .45; }
"""
CSS = re.sub(r'(?<![\w.#-])(-?(?:\d+(?:\.\d+)?|\.\d+))u\b', lambda m: f'calc({m.group(1)} * var(--u))', _CSS)

JS = r"""
  // Procense hero: plays once when it comes into view; reduced motion or no IntersectionObserver keeps the final frame
  (function () {
    var hero = document.querySelector('[data-ph]');
    if (!hero || window.matchMedia('(prefers-reduced-motion: reduce)').matches || !hero.animate) return;
    var stage = hero.querySelector('.ph-stage'), paper = hero.querySelector('.ph-paper'), tab = hero.querySelector('.ph-tab');
    var hws = [].slice.call(hero.querySelectorAll('.ph-hw')), tvs = [].slice.call(hero.querySelectorAll('.ph-tv'));
    var helps = [].slice.call(hero.querySelectorAll('.ph-help')), ok = hero.querySelector('.ph-ok');
    var ease = 'cubic-bezier(.22,1,.36,1)';
    function rel(el) { var r = el.getBoundingClientRect(), s = stage.getBoundingClientRect(); return { x: r.left - s.left, y: r.top - s.top, w: r.width, h: r.height }; }
    function done() { hero.classList.remove('is-armed'); hero.querySelectorAll('.ph-fly').forEach(function (f) { f.remove(); }); }
    var started = false;
    function start() {
      if (started) return; started = true;
      hero.classList.add('is-armed');
      var fonts = document.fonts ? Promise.race([document.fonts.ready, new Promise(function (r) { setTimeout(r, 800); })]) : Promise.resolve();
      fonts.then(function () { requestAnimationFrame(play); });
    }
    function play() {
      // Runs on the first frame the page is actually shown (rAF waits while the tab is hidden).
      // Never strand the hero half-built: if anything stalls, show the final frame.
      setTimeout(function () { if (hero.classList.contains('is-armed')) { hero.getAnimations({ subtree: true }).forEach(function (an) { an.cancel(); }); tvs.forEach(function (tv) { tv.style.opacity = ''; }); done(); } }, 7000);
      // 1. Write: each entry is revealed left to right, as if by pen
      hws.forEach(function (hw, k) {
        hw.animate([{ clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0% 0 0)' }], { duration: 520, delay: 250 + k * 260, easing: 'ease-in-out', fill: 'forwards' });
      });
      // 2. The tablet slides in as the paper steps back
      tab.animate([{ opacity: 0, translate: 'calc(6 * var(--u)) 0' }, { opacity: 1, translate: '0 0' }], { duration: 900, delay: 1500, easing: ease, fill: 'forwards' });
      paper.animate([{ opacity: 1, translate: '0 0', scale: 1 }, { opacity: .6, translate: 'calc(-2 * var(--u)) calc(.6 * var(--u))', scale: .96 }], { duration: 1000, delay: 2300, easing: ease, fill: 'forwards' });
      // 3. Lift: each entry flies to its field, turning from handwriting into typed text
      setTimeout(function () {
        hws.forEach(function (hw, k) {
          var a = rel(hw), tv = tvs[k];
          tv.style.opacity = '0';
          var fly = document.createElement('div'); fly.className = 'ph-fly';
          var h = hw.cloneNode(true), t = tv.cloneNode(true); h.style.clipPath = 'none'; t.style.opacity = '0';
          fly.appendChild(h); fly.appendChild(t); stage.appendChild(fly);
          var b = rel(tv);
          var hwFont = parseFloat(getComputedStyle(hw).fontSize), tvFont = parseFloat(getComputedStyle(tv).fontSize);
          fly.style.translate = a.x + 'px ' + a.y + 'px';
          t.style.fontSize = tvFont + 'px'; h.style.fontSize = hwFont + 'px';
          hw.animate([{ opacity: 1 }, { opacity: .45 }], { duration: 400, delay: k * 140, fill: 'forwards' });
          var d = 950, dl = k * 140;
          fly.animate([{ translate: a.x + 'px ' + a.y + 'px', rotate: '-4deg' },
                       { translate: ((a.x + b.x) / 2) + 'px ' + (Math.min(a.y, b.y) - 0.06 * stage.offsetWidth) + 'px', rotate: '-3deg', offset: .5 },
                       { translate: b.x + 'px ' + b.y + 'px', rotate: '-2deg' }], { duration: d, delay: dl, easing: ease, fill: 'forwards' });
          h.animate([{ opacity: 1 }, { opacity: 0 }], { duration: d * .5, delay: dl + d * .3, fill: 'forwards' });
          t.animate([{ opacity: 0 }, { opacity: 1 }], { duration: d * .5, delay: dl + d * .35, fill: 'forwards' });
          setTimeout(function () { tv.style.opacity = '1'; fly.remove(); }, dl + d + 30);
        });
      }, 2200);
      // 4. Settle: helpers fade in, then the check
      setTimeout(function () { helps.forEach(function (e) { e.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, fill: 'forwards' }); }); }, 3450);
      setTimeout(function () { ok.animate([{ opacity: 0, scale: .4 }, { opacity: 1, scale: 1.15, offset: .7 }, { opacity: 1, scale: 1 }], { duration: 450, easing: 'ease-out', fill: 'forwards' }); }, 3800);
      setTimeout(function () {
        // Hand the final frame back to CSS and drop the animation fills
        hero.getAnimations({ subtree: true }).forEach(function (an) { an.cancel(); });
        tvs.forEach(function (tv) { tv.style.opacity = ''; });
        done();
      }, 4500);
    }
    hero.phReplay = function () { started = false; start(); };  // for checking the animation from the console
    // In view on load (the usual case: it's the top of the page)? Play now. Otherwise play when it scrolls into view.
    var r = hero.getBoundingClientRect();
    if (r.top < window.innerHeight * .75 && r.bottom > 0) { start(); return; }
    if (!('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (es) {
      if (es.some(function (e) { return e.isIntersecting; })) { io.disconnect(); start(); }
    }, { threshold: .5 });
    io.observe(hero);
  })();
"""
