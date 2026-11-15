"""Landing, carousel idea (after the Philz app): top nav, then a full-width project carousel whose background takes
each project's brand colour; the heading sits centred on top, the screenshot floats in the centre underneath, and the
neighbouring screenshots peek in from the edges. Then About + Experience.

An alternative to prototypes/landing.html, which stays as it is. Shares content, brand art, logos and the timeline
with landing.py (importing it also rebuilds landing.html, unchanged).
Run: python3 design-system/tools/previews/src/landing_carousel.py  ->  prototypes/landing-carousel.html
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import landing as L
from lib import I

PROJECTS = L.FEATURED + L.MORE
# Solid brand base under the centred text (white text: Mensio 5.24:1, Procense 16.4:1, Apple 21:1, OmniSynkAI 6.15:1)
# and a lighter brand glow behind the screenshot only. Literal hex is project art, as on landing.html.
HERO = {
    'mensio':   ('#175CFF', '#3693F9'),
    'procense': ('#1B2026', '#2483FF'),
    'apple':    ('#000000', '#3A3A3C'),
    'omni':     ('#5B43E8', '#9B94E0'),
}

def text(i, p):
    k, title, sub, badges, _, href = p
    tags = ''.join(f'<li class="pm-badge">{b}</li>' for b in badges)
    return (f'<div class="cx-text{" is-active" if i == 0 else ""}" data-i="{i}"{"" if i == 0 else " aria-hidden=\"true\""}>'
            f'{L.white_logo(k)}<h2 class="cx-title">{title}</h2><p class="cx-sub">{sub}</p>'
            f'<ul class="cx-tags" aria-label="Disciplines">{tags}</ul></div>')

def slide(i, p):
    k, title, _, _, _, href = p
    return (f'<div class="cx-slide{" is-active" if i == 0 else ""}" data-i="{i}" role="group" aria-roledescription="slide" aria-label="{i + 1} of {len(PROJECTS)}: {title}">'
            f'<a class="cx-shot" href="{href}" tabindex="-1" aria-hidden="true"><span class="cx-shot__img"></span></a></div>')

CSS = r"""
/* ===== Landing, carousel idea (after the Philz app) ===== */
body { margin: 0; font-family: var(--font-sans); background: var(--color-bg-canvas); color: var(--color-text-primary); }
.cxp { container-type: inline-size; }
.cx-nav .pm-topnav__brand { font-weight: var(--weight-medium); }
.cx-nav .pm-topnav__item .pm-icon { width: 14px; height: 14px; margin-left: var(--space-1); }

/* Hero: full width, background = the active project's brand colour (layers cross-fade; gradients can't transition) */
.cx { position: relative; isolation: isolate; overflow: hidden; color: var(--color-text-on-image); padding-top: var(--space-12); }
.cx-bg, .cx-bg > span { position: absolute; inset: 0; z-index: -1; }
.cx-bg > span { opacity: 0; background: radial-gradient(60% 55% at 50% 72%, var(--glow) 0%, transparent 70%), var(--base); }
.cx-bg > span.is-active { opacity: 1; }

/* Centred heading block: one per project, stacked in one cell, the active one shown */
.cx-copy { display: grid; justify-items: center; text-align: center; padding: 0 var(--space-4); }
.cx-text { grid-area: 1 / 1; display: grid; justify-items: center; gap: var(--space-2); max-width: 36rem; opacity: 0; visibility: hidden; transform: translateY(var(--space-2)); }
.cx-text.is-active { opacity: 1; visibility: visible; transform: none; }
.cx-text .lp-card-logo { margin: 0 0 var(--space-3); color: var(--color-text-on-image); }
.cx-title { margin: 0; font-size: var(--type-h1); line-height: var(--line-h1); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h1); text-wrap: balance; }
.cx-sub { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); text-wrap: pretty; }
.cx-tags { display: flex; flex-wrap: wrap; justify-content: center; gap: var(--space-1); list-style: none; margin: var(--space-2) 0 0; padding: 0; }
.cx .pm-badge { background: color-mix(in srgb, var(--color-text-on-image) 16%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--color-text-on-image) 30%, transparent); color: var(--color-text-on-image); }

/* Screenshot strip: the active one centred, neighbours smaller and peeking in from the edges */
/* Sized from the page width (cqw on .cxp): the active slide is centred, and each neighbour shows a slice of about --cx-peek */
.cx-track { --cx-w: min(600px, 60cqw); --cx-peek: 150px; display: flex; gap: calc((100cqw - var(--cx-w)) / 2 - var(--cx-peek)); overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x mandatory; scrollbar-width: none; padding: var(--space-10) calc((100cqw - var(--cx-w)) / 2) var(--space-12); }
.cx-track::-webkit-scrollbar { display: none; }
.cx-track:focus-visible { outline: 2px solid var(--color-text-on-image); outline-offset: -4px; border-radius: var(--radius-md); }
@container (max-width: 767px) { .cx-track { --cx-w: 76cqw; --cx-peek: var(--space-20); } }
.cx-slide { flex: 0 0 var(--cx-w); scroll-snap-align: center; display: grid; place-items: center; }
.cx-shot { display: block; width: 100%; border-radius: var(--radius-md); transform: scale(.82); opacity: .85; }
.cx-slide.is-active .cx-shot { transform: none; opacity: 1; }
.cx-shot__img { position: relative; display: block; aspect-ratio: 16 / 10; border-radius: var(--radius-md); background: var(--color-text-on-image);
  box-shadow: 0 1px 2px rgb(0 0 0 / 6%), 0 var(--space-6) var(--space-12) calc(-1 * var(--space-2)) rgb(0 0 0 / 28%); }
.cx-shot__img::after { content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; box-shadow: inset 0 0 0 1px rgb(255 255 255 / 12%), inset 0 0 var(--space-6) rgb(0 0 0 / 7%); }

/* Controls: previous / dots / next; then a darker band with the call to action (Philz's "I'll take it!") */
.cx-controls { display: flex; justify-content: center; align-items: center; gap: var(--space-3); padding-bottom: var(--space-8); }
.cx-controls .pm-btn { color: var(--color-text-on-image); background: transparent; }
@media (hover: hover) { .cx-controls .pm-btn:hover { background: color-mix(in srgb, var(--color-text-on-image) 16%, transparent); } }
.cx-controls .pm-btn:focus-visible { outline: 2px solid var(--color-text-on-image); outline-offset: 2px; }
.cx-dots { display: flex; gap: var(--space-2); list-style: none; margin: 0; padding: 0; }
.cx-dot { width: 24px; height: 24px; display: grid; place-items: center; padding: 0; border: 0; background: none; cursor: pointer; border-radius: var(--radius-sm); }
.cx-dot::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: color-mix(in srgb, var(--color-text-on-image) 45%, transparent); }
.cx-dot[aria-current="true"]::before { background: var(--color-text-on-image); }
.cx-dot:focus-visible { outline: 2px solid var(--color-text-on-image); outline-offset: 0; }
@media (pointer: coarse) { .cx-dot { width: 44px; height: 44px; } }
.cx-cta { display: flex; justify-content: center; padding: var(--space-5) var(--space-4); background: rgb(0 0 0 / 18%); }
.cx-cta a { display: inline-flex; align-items: center; gap: var(--space-2); min-height: var(--control-min-target); color: var(--color-text-on-image); font-weight: var(--weight-medium); text-decoration: none; border-radius: var(--radius-sm); }
.cx-cta a .pm-icon { width: 16px; height: 16px; }
.cx-cta a:focus-visible { outline: 2px solid var(--color-text-on-image); outline-offset: 4px; }
@media (hover: hover) { .cx-cta a:hover { text-decoration: underline; text-underline-offset: 0.2em; } }

/* Motion: cross-fades, the strip's scale, a gentle float on the active screenshot. All off with reduced motion. */
@media (prefers-reduced-motion: no-preference) {
  .cx-track { scroll-behavior: smooth; }
  .cx-bg > span { transition: opacity calc(var(--motion-duration-base) * 2.5) var(--motion-ease); }
  .cx-text { transition: opacity calc(var(--motion-duration-base) * 1.5) var(--motion-ease), transform calc(var(--motion-duration-base) * 1.5) var(--motion-ease), visibility 0s linear calc(var(--motion-duration-base) * 1.5); }
  .cx-text.is-active { transition-delay: 0s; }
  .cx-shot { transition: transform calc(var(--motion-duration-base) * 2) var(--motion-ease), opacity calc(var(--motion-duration-base) * 2) var(--motion-ease); }
  .cx-slide.is-active .cx-shot__img { animation: cx-float 6s ease-in-out infinite; }
  @keyframes cx-float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(calc(-1 * var(--space-2))); } }
}

/* Below the hero: About + Experience, reusing the section and timeline styles from landing.html */
.cx-main { max-width: var(--content-max-width); margin: 0 auto; padding: var(--space-16) var(--space-4) var(--space-16); container-type: inline-size; }
@container (min-width: 768px) { .cx-main { padding-inline: var(--space-10); } }
.cx-foot { display: flex; flex-wrap: wrap; justify-content: space-between; gap: var(--space-3); margin-top: var(--space-16); padding-top: var(--space-4); border-top: 1px solid var(--color-border-subtle); }
.cx-foot ul { display: flex; gap: var(--space-4); list-style: none; margin: 0; padding: 0; }
"""

SCRIPT = r"""
(function () {
  var root = document.documentElement, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Theme toggle
  var themeBtn = document.getElementById('cx-theme');
  function isDark() { var t = root.getAttribute('data-theme'); return t ? t === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; }
  function sync() { themeBtn.setAttribute('aria-pressed', String(isDark())); }
  themeBtn.addEventListener('click', function () { root.setAttribute('data-theme', isDark() ? 'light' : 'dark'); sync(); }); sync();
  // Mobile menu
  var nav = document.querySelector('.cx-nav'), menu = nav.querySelector('.pm-topnav__menu');
  menu.addEventListener('click', function () { var open = nav.getAttribute('data-open') !== 'true'; nav.setAttribute('data-open', String(open)); menu.setAttribute('aria-expanded', String(open)); });

  // Carousel: the slide nearest the centre is active; background, heading, dots and the call to action follow it
  var hero = document.getElementById('work'), track = hero.querySelector('.cx-track');
  var slides = [].slice.call(track.querySelectorAll('.cx-slide')), texts = [].slice.call(hero.querySelectorAll('.cx-text'));
  var bgs = [].slice.call(hero.querySelectorAll('.cx-bg > span')), dots = [].slice.call(hero.querySelectorAll('.cx-dot'));
  var cta = hero.querySelector('.cx-cta a'), live = document.getElementById('cx-live'), active = 0;
  function set(i) {
    if (i === active) return; active = i;
    [slides, texts, bgs].forEach(function (list) { list.forEach(function (el, j) { el.classList.toggle('is-active', j === i); }); });
    texts.forEach(function (el, j) { if (j === i) el.removeAttribute('aria-hidden'); else el.setAttribute('aria-hidden', 'true'); });
    dots.forEach(function (d, j) { d.setAttribute('aria-current', String(j === i)); });
    cta.href = slides[i].querySelector('.cx-shot').getAttribute('href');
    live.textContent = slides[i].getAttribute('aria-label');
  }
  function nearest() {
    var mid = track.getBoundingClientRect().left + track.clientWidth / 2, best = 0, d = Infinity;
    slides.forEach(function (s, j) { var r = s.getBoundingClientRect(), x = Math.abs(r.left + r.width / 2 - mid); if (x < d) { d = x; best = j; } });
    return best;
  }
  var ticking = false;
  track.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; set(nearest()); }); } }, { passive: true });
  function go(i) { i = Math.max(0, Math.min(slides.length - 1, i)); var s = slides[i]; track.scrollTo({ left: s.offsetLeft - (track.clientWidth - s.offsetWidth) / 2, behavior: reduce ? 'auto' : 'smooth' }); set(i); }
  hero.querySelector('[data-cx="prev"]').addEventListener('click', function () { go(active - 1); });
  hero.querySelector('[data-cx="next"]').addEventListener('click', function () { go(active + 1); });
  dots.forEach(function (d, j) { d.addEventListener('click', function () { go(j); }); });
  track.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') { e.preventDefault(); go(active + 1); } if (e.key === 'ArrowLeft') { e.preventDefault(); go(active - 1); } });
  // Clicking a peeking neighbour brings it to the centre instead of following its link
  slides.forEach(function (s, j) { s.querySelector('.cx-shot').addEventListener('click', function (e) { if (j !== active) { e.preventDefault(); go(j); } }); });

  // Timeline: same reveal as landing.html, replayed each time it comes into view
  var tl = document.querySelector('.lp-tl');
  if (tl && 'IntersectionObserver' in window && !reduce) {
    root.classList.add('lp-anim');
    new IntersectionObserver(function (es) { es.forEach(function (e) {
      if (e.intersectionRatio >= 0.35) tl.classList.add('is-in'); else if (!e.isIntersecting) tl.classList.remove('is-in');
    }); }, { threshold: [0, 0.35] }).observe(tl);
  }
  // Links to pages that aren't built yet stay put
  document.querySelectorAll('[data-soon]').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); }); });
})();
"""

n = len(PROJECTS)
bgs = ''.join(f'<span class="{"is-active" if i == 0 else ""}" style="--base:{HERO[p[0]][0]};--glow:{HERO[p[0]][1]}"></span>' for i, p in enumerate(PROJECTS))
dots = ''.join(f'<li><button type="button" class="cx-dot" aria-label="Show {p[1]}" aria-current="{"true" if i == 0 else "false"}"></button></li>' for i, p in enumerate(PROJECTS))
roles = ''.join(L.tl_item(len(L.ROLES) - 1 - j, len(L.ROLES), *r) for j, r in enumerate(L.ROLES))
socials = ''.join(f'<li><a class="pm-link pm-link--subtle" href="{h}" target="_blank" rel="noopener">{l}<span class="pm-sr"> (opens in a new tab)</span></a></li>' for l, h in L.SOCIAL)

page = f'''<title>Portfolio Carousel Idea</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&display=swap">
<style>
/* ===== Paper × Midnight {L.VER} · tokens.css (verbatim) ===== */
{L.tokens}
/* ===== Paper × Midnight {L.VER} · components.css (verbatim) ===== */
{L.comps}
/* ===== Shared with landing.html (sections, timeline, card art) ===== */
{L.PAGE_CSS}
{CSS}
</style>

<div class="cxp lp">
<header class="pm-topnav pm-topnav--sticky cx-nav" data-open="false">
  <div class="pm-topnav__bar">
    <a class="pm-topnav__brand" href="#work">{L.NAME}</a>
    <nav class="pm-topnav__nav" id="cx-nav" aria-label="Primary"><ul class="pm-topnav__list">
      <li><a class="pm-topnav__item" href="#work" aria-current="page">Work</a></li>
      <li><a class="pm-topnav__item" href="#about">About</a></li>
      <li><a class="pm-topnav__item" href="#resume" data-soon>Resume{I["ext"]}</a></li>
    </ul></nav>
    <div class="pm-topnav__actions">
      <span class="pm-tooltip-anchor">
        <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" id="cx-theme" aria-pressed="false" aria-labelledby="cx-theme-tip">{I["moon"]}</button>
        <span role="tooltip" id="cx-theme-tip" class="pm-tooltip pm-tooltip--bottom" style="left:auto;right:0;transform:none">Dark theme</span>
      </span>
    </div>
    <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-topnav__menu" aria-expanded="false" aria-controls="cx-nav" aria-label="Menu">{I["menu"]}</button>
  </div>
</header>

<section class="cx" id="work" aria-roledescription="carousel" aria-labelledby="cx-h">
  <h2 class="pm-sr" id="cx-h">Featured work</h2>
  <div class="cx-bg" aria-hidden="true">{bgs}</div>
  <div class="cx-copy">{''.join(text(i, p) for i, p in enumerate(PROJECTS))}</div>
  <div class="cx-track" tabindex="0" aria-label="Project screenshots. Use the left and right arrow keys to move between projects.">{''.join(slide(i, p) for i, p in enumerate(PROJECTS))}</div>
  <div class="cx-controls">
    <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" data-cx="prev" aria-label="Previous project">{I["prev"]}</button>
    <ul class="cx-dots">{dots}</ul>
    <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" data-cx="next" aria-label="Next project">{I["next"]}</button>
  </div>
  <div class="cx-cta"><a href="{PROJECTS[0][5]}">View case study{I["arrow"]}</a></div>
  <p class="pm-sr" aria-live="polite" id="cx-live"></p>
</section>

<main class="cx-main">
  <section class="pm-split__section lp-sec" id="about" aria-labelledby="lp-about-h">
    {L.sec_head(2, 'About', 'lp-about-h', 'About me', 'San Francisco')}
    <div class="lp-sec__body"><div class="lp-about" style="gap:var(--space-4)">{''.join(f'<p>{x}</p>' for x in L.BIO)}</div></div>
    <div class="lp-sec__head lp-sec__head--sub"><h3 class="lp-sec__h lp-sec__h--sub" id="lp-exp-h">Experience<span>2022 – 2026</span></h3></div>
    <div class="lp-sec__body lp-sec__body--sub"><ol class="lp-tl" aria-labelledby="lp-exp-h">{roles}</ol></div>
  </section>
  <footer class="cx-foot"><p class="pm-meta-text" style="margin:0">© 2026 {L.NAME} · Built on Paper × Midnight {L.VER}</p><ul aria-label="Elsewhere">{socials}</ul></footer>
</main>
</div>

<script>{SCRIPT}</script>
'''
out = os.path.join(L.REPO, 'prototypes', 'landing-carousel.html')
open(out, 'w').write(page)
print(len(page))
