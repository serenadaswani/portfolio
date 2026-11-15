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
# Page background (one step darker) and card fill (the brand colour) per project, after the Philz app's tinted card on a
# tinted page. White text on the card: Mensio 5.24:1, Procense 14.5:1, Apple 17:1, OmniSynkAI 6.15:1; the card is
# 1.2-1.5x lighter than the page, so it lifts without leaving the palette. Literal hex is project art.
HERO = {
    'mensio':   {'page': '#0F47D1', 'card': '#175CFF', 'glow': '#3693F9'},
    'procense': {'page': '#12161B', 'card': '#232A33', 'glow': '#2483FF'},
    'apple':    {'page': '#000000', 'card': '#1C1C1E', 'glow': '#3A3A3C'},
    'omni':     {'page': '#3F3A9E', 'card': '#5B43E8', 'glow': '#9B94E0'},
}

def card(i, p, clone=False):
    """One project card: logo, title, description, tags, the floating screenshot, then 'View case study'.
    Clones (for the infinite loop) are hidden from assistive tech and out of the tab order."""
    k, title, sub, badges, _, href = p
    c = HERO[k]
    tags = ''.join(f'<li class="pm-badge">{b}</li>' for b in badges)
    a11y = ' aria-hidden="true" inert' if clone else f' role="group" aria-roledescription="slide" aria-label="{i + 1} of {len(PROJECTS)}: {title}"'
    return (f'<article class="cx-card" data-i="{i}"{a11y} style="--card:{c["card"]};--glow:{c["glow"]}">'
            f'{L.white_logo(k)}<h3 class="cx-title">{title}</h3><p class="cx-sub">{sub}</p>'
            f'<ul class="cx-tags" aria-label="Disciplines">{tags}</ul>'
            '<div class="cx-shot"><span class="cx-shot__img"></span></div>'
            f'<a class="cx-cta" href="{href}">View case study{I["arrow"]}</a></article>')

CSS = r"""
/* ===== Landing, carousel idea (after the Philz app) ===== */
body { margin: 0; font-family: var(--font-sans); background: var(--color-bg-canvas); color: var(--color-text-primary); }
.cxp { container-type: inline-size; }
.cx-nav .pm-topnav__brand { font-weight: var(--weight-medium); }
.cx-nav .pm-topnav__item .pm-icon { width: 14px; height: 14px; margin-left: var(--space-1); }

/* Hero: full width; the page background cross-fades to the active project's darker shade */
.cx { position: relative; isolation: isolate; overflow: hidden; color: var(--color-text-on-image); padding-top: var(--space-4); }
.cx-bg, .cx-bg > span { position: absolute; inset: 0; z-index: -1; }
.cx-bg > span { opacity: 0; background: var(--page); }
.cx-bg > span.is-active { opacity: 1; }

/* Track: infinite (three copies; the script recentres onto the middle copy), active card centred, a neighbour peeking
   on each side. Sized from the page width (cqw on .cxp). */
/* Wider card, bigger screenshot, more of each neighbour. The width is also capped by the window height so the whole
   centre card stays in view (below the 56px nav) on shorter screens. */
/* Geometry. --cx-side: how much of each neighbour's screenshot shows at the screen edge; --cx-over: how far it reaches
   into the centre card (on top of it, inside the card's side padding). The centre card spans the rest of the width; its
   screenshot keeps its own size (--cx-img, sized from the window height so the top of About shows below the hero), and
   the leftover becomes side padding. Every card and screenshot is the same size; side screenshots slide inward by
   --cx-pull so their inner edge lands exactly --cx-over inside the centre card. */
.cx-track { --cx-side: 168px; --cx-over: var(--space-8); --cx-gap: var(--space-6);
  --cx-w: calc(100cqw - 2 * (var(--cx-side) - var(--cx-over)));
  --cx-img: min(806px, calc(var(--cx-w) - 2 * var(--space-16)), calc((100svh - 560px) * 1.6));
  --cx-pull: calc(var(--cx-gap) + (var(--cx-w) - var(--cx-img)) / 2 + var(--cx-over));
  display: flex; align-items: center; gap: var(--cx-gap); overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x mandatory; scrollbar-width: none; padding: 0 calc((100cqw - var(--cx-w)) / 2) var(--space-4); }
.cx-track::-webkit-scrollbar { display: none; }
.cx-track:focus-visible { outline: 2px solid var(--color-text-on-image); outline-offset: -4px; border-radius: var(--radius-lg); }
@container (max-width: 767px) { .cx-track { --cx-side: 28px; --cx-over: var(--space-3); --cx-gap: var(--space-2); --cx-img: calc(var(--cx-w) - 2 * var(--space-6)); } }

/* Card (after Philz): the brand colour, a soft glow behind the screenshot, everything centred */
.cx-card { flex: 0 0 var(--cx-w); scroll-snap-align: center; position: relative; isolation: isolate; display: grid; justify-items: center; text-align: center; gap: var(--space-2);
  padding: var(--space-6) calc((var(--cx-w) - var(--cx-img)) / 2) var(--space-2); border-radius: var(--radius-lg); }
/* The card surface is a layer, so side cards can drop it: only their screenshot shows, like Philz's peeking drinks */
.cx-card::before { content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; opacity: 0;
  background: radial-gradient(70% 45% at 50% 62%, color-mix(in srgb, var(--glow) 55%, transparent) 0%, transparent 70%), var(--card);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--color-text-on-image) 10%, transparent), 0 var(--space-6) var(--space-12) calc(-1 * var(--space-4)) rgb(0 0 0 / 30%); }
.cx-card.is-active { z-index: 1; }
.cx-card.is-prev, .cx-card.is-next { z-index: 2; } /* their screenshots sit on top of the centre card's edge */
.cx-card.is-active::before { opacity: 1; }
.cx-card > :not(.cx-shot) { transition: opacity var(--motion-duration-base) var(--motion-ease); }
.cx-card:not(.is-active) > :not(.cx-shot) { opacity: 0; }
/* Side screenshots overflow their (invisible) cards toward the centre and tuck behind the centre card */
.cx-card.is-prev .cx-shot { transform: translateX(var(--cx-pull)); }
.cx-card.is-next .cx-shot { transform: translateX(calc(-1 * var(--cx-pull))); }
.cx-card .lp-card-logo { margin: 0 0 var(--space-2); color: var(--color-text-on-image); }
.cx-title { margin: 0; font-size: var(--type-h3); line-height: var(--line-h3); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h3); text-wrap: balance; }
.cx-sub { margin: 0; max-width: 34rem; font-size: var(--type-body-md); line-height: var(--line-body-md); text-wrap: pretty; }
.cx-tags { display: flex; flex-wrap: wrap; justify-content: center; gap: var(--space-1); list-style: none; margin: var(--space-2) 0 0; padding: 0; }
.cx .pm-badge { background: color-mix(in srgb, var(--color-text-on-image) 16%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--color-text-on-image) 30%, transparent); color: var(--color-text-on-image); }
.cx-shot { width: var(--cx-img); margin: var(--space-4) 0 var(--space-1); }
.cx-shot__img { position: relative; display: block; aspect-ratio: 16 / 10; border-radius: var(--radius-md); background: var(--color-text-on-image);
  box-shadow: 0 1px 2px rgb(0 0 0 / 6%), 0 var(--space-5) var(--space-10) calc(-1 * var(--space-2)) rgb(0 0 0 / 30%); }
.cx-shot__img::after { content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; box-shadow: inset 0 0 0 1px rgb(255 255 255 / 12%), inset 0 0 var(--space-6) rgb(0 0 0 / 7%); }
/* "View case study": a white text link with an arrow on every card (44px target) */
.cx-cta { display: inline-flex; align-items: center; justify-content: center; gap: var(--space-2); min-height: var(--control-min-target, 44px); padding: 0 var(--space-3); border-radius: var(--radius-sm); color: var(--color-text-on-image); font-weight: var(--weight-medium); text-decoration: none; }
.cx-cta .pm-icon { width: 16px; height: 16px; }
.cx-cta:focus-visible { outline: 2px solid var(--color-text-on-image); outline-offset: 3px; }
@media (hover: hover) { .cx-cta:hover { text-decoration: underline; text-underline-offset: 0.2em; } .cx-cta:hover .pm-icon { transform: translateX(2px); } }
.cx-cta .pm-icon { transition: transform var(--motion-duration-base) var(--motion-ease); }
/* A peeking card brings itself to the centre when clicked */
.cx-card:not(.is-active) { cursor: pointer; }
.cx-card:not(.is-active) .cx-cta { pointer-events: none; }

/* Controls: previous / dots / next (always enabled: the loop never ends) */
.cx-controls { display: flex; justify-content: center; align-items: center; gap: var(--space-3); padding-bottom: var(--space-6); }
.cx-controls .pm-btn { color: var(--color-text-on-image); background: transparent; }
@media (hover: hover) { .cx-controls .pm-btn:hover { background: color-mix(in srgb, var(--color-text-on-image) 16%, transparent); } }
.cx-controls .pm-btn:focus-visible { outline: 2px solid var(--color-text-on-image); outline-offset: 2px; }
.cx-dots { display: flex; gap: var(--space-2); list-style: none; margin: 0; padding: 0; }
.cx-dot { width: 24px; height: 24px; display: grid; place-items: center; padding: 0; border: 0; background: none; cursor: pointer; border-radius: var(--radius-sm); }
.cx-dot::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: color-mix(in srgb, var(--color-text-on-image) 45%, transparent); }
.cx-dot[aria-current="true"]::before { background: var(--color-text-on-image); }
.cx-dot:focus-visible { outline: 2px solid var(--color-text-on-image); outline-offset: 0; }
@media (pointer: coarse) { .cx-dot { width: 44px; height: 44px; } }

/* Motion: background cross-fade, card scale, a gentle float on the active screenshot. All off with reduced motion. */
@media (prefers-reduced-motion: no-preference) {
  .cx-bg > span { transition: opacity calc(var(--motion-duration-base) * 2.5) var(--motion-ease); }
  .cx-card, .cx-card .cx-shot { transition: transform calc(var(--motion-duration-base) * 2) var(--motion-ease); }
  .cx-card::before { transition: opacity calc(var(--motion-duration-base) * 2) var(--motion-ease); }
  .cx-card.is-active .cx-shot__img { animation: cx-float 6s ease-in-out infinite; }
  @keyframes cx-float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(calc(-1 * var(--space-2))); } }
}

/* Below the hero: About + Experience, reusing the section and timeline styles from landing.html */
.cx-main { max-width: var(--content-max-width); margin: 0 auto; padding: var(--space-10) var(--space-4) var(--space-16); container-type: inline-size; }
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

  // Carousel, infinite: three copies of the cards; the track always settles on the middle copy, so there is a card
  // on each side of the active one. Background, dots and the live label follow the active card.
  var hero = document.getElementById('work'), track = hero.querySelector('.cx-track');
  var cards = [].slice.call(track.querySelectorAll('.cx-card')), n = cards.length / 3;
  var bgs = [].slice.call(hero.querySelectorAll('.cx-bg > span')), dots = [].slice.call(hero.querySelectorAll('.cx-dot'));
  var live = document.getElementById('cx-live'), pos = n, settle;
  function centre(k) { var c = cards[k]; return c.offsetLeft - (track.clientWidth - c.offsetWidth) / 2; }
  function mark(k) {
    pos = k; var i = k % n;
    cards.forEach(function (c, j) { c.classList.toggle('is-active', j === k); c.classList.toggle('is-prev', j === k - 1); c.classList.toggle('is-next', j === k + 1); });
    bgs.forEach(function (b, j) { b.classList.toggle('is-active', j === i); });
    dots.forEach(function (d, j) { d.setAttribute('aria-current', String(j === i)); });
    var label = cards[n + i].getAttribute('aria-label'); if (live.textContent !== label) live.textContent = label;
  }
  function nearest() {
    var mid = track.scrollLeft + track.clientWidth / 2, best = 0, d = Infinity;
    cards.forEach(function (c, j) { var x = Math.abs(c.offsetLeft + c.offsetWidth / 2 - mid); if (x < d) { d = x; best = j; } });
    return best;
  }
  function recentre() { // jump, without animation, from a copy at either end to the same card in the middle copy
    var k = nearest(); if (k < n || k >= 2 * n) { var m = n + (k % n); track.style.scrollSnapType = 'none'; track.scrollLeft = centre(m); track.style.scrollSnapType = ''; mark(m); }
  }
  var ticking = false;
  track.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; var k = nearest(); if (k !== pos) mark(k); }); }
    clearTimeout(settle); settle = setTimeout(recentre, 160);
  }, { passive: true });
  if ('onscrollend' in window) track.addEventListener('scrollend', function () { clearTimeout(settle); recentre(); });
  function go(k) { track.scrollTo({ left: centre(k), behavior: reduce ? 'auto' : 'smooth' }); mark(k); }
  hero.querySelector('[data-cx="prev"]').addEventListener('click', function () { go(pos - 1); });
  hero.querySelector('[data-cx="next"]').addEventListener('click', function () { go(pos + 1); });
  dots.forEach(function (d, i) { d.addEventListener('click', function () { go(n + i); }); });
  track.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') { e.preventDefault(); go(pos + 1); } if (e.key === 'ArrowLeft') { e.preventDefault(); go(pos - 1); } });
  cards.forEach(function (c, j) { c.addEventListener('click', function (e) { if (j !== pos) { e.preventDefault(); go(j); } }); });
  // Start on the first project in the middle copy
  track.style.scrollSnapType = 'none'; track.scrollLeft = centre(n); track.style.scrollSnapType = ''; mark(n);
  addEventListener('resize', function () { track.scrollLeft = centre(pos); });

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
bgs = ''.join(f'<span class="{"is-active" if i == 0 else ""}" style="--page:{HERO[p[0]]["page"]}"></span>' for i, p in enumerate(PROJECTS))
dots = ''.join(f'<li><button type="button" class="cx-dot" aria-label="Show {p[1]}" aria-current="{"true" if i == 0 else "false"}"></button></li>' for i, p in enumerate(PROJECTS))
cards = (''.join(card(i, p, clone=True) for i, p in enumerate(PROJECTS)) + ''.join(card(i, p) for i, p in enumerate(PROJECTS))
         + ''.join(card(i, p, clone=True) for i, p in enumerate(PROJECTS)))
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
  <div class="cx-track" tabindex="0" aria-label="Projects. Use the left and right arrow keys to move between them.">{cards}</div>
  <div class="cx-controls">
    <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" data-cx="prev" aria-label="Previous project">{I["prev"]}</button>
    <ul class="cx-dots">{dots}</ul>
    <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" data-cx="next" aria-label="Next project">{I["next"]}</button>
  </div>
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
