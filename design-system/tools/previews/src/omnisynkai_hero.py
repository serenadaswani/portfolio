"""OmniSynkAI case-study hero: from v3 to one-click AI autofill, as a short loop.

On OmniSynkAI's brand gradient (the landing card's art), the listing page sits in a window on the right; the left column
holds the logo, a headline and a caption that follows the story. One CSS timeline (10s, looped):
  1. v3: the old listing page, with AI spread across the page (caption "Before: v3").
  2. It gives way to the launch version (v4): the title and category type themselves in.
  3. A cursor moves to the AI autofill icon and clicks it (a ripple).
  4. The "Filling out your listing" dialog appears and a progress bar fills.
  5. The autofilled listing is revealed from top to bottom behind a soft scan line, and the AI-written brand and tags
     glow purple, then it loops back to v3.
Every position is a % of the 2000x1480 screen exports (measured from Serena's Figma exports). The window is its own
container, so typed text is sized in cqw and stays proportional at any width.

Motion rules: starts when in view, the tab is visible and the screens have decoded; pauses off screen; a Pause/Play
button (WCAG 2.2.2, the loop runs longer than 5s). Reduced motion or no JS: the final frame (autofilled listing) and
no button. The gradient, cursor and glow colours are project art (OmniSynkAI's own palette), like the Procense hero.
"""
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
V = '?v=2'

def _logo():
    svg = open(os.path.join(REPO, 'landing', 'logos', 'omnisynkai.svg')).read().strip()
    return svg.replace('<svg ', '<svg class="oh-logo" aria-hidden="true" focusable="false" ', 1)

CAPTIONS = [  # (step label, line)
    ('Before: v3', 'AI was spread across the page, and easy to miss.'),
    ('Launch: v4', 'Start with a title and a category.'),
    ('One click', 'The AI autofill icon drafts the rest.'),
    ('Ready to review', 'Everything AI wrote is clearly marked.'),
]

CURSOR = ('<svg class="oh-cursor" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
          '<path d="M4 2.5 L4 19.5 L8.6 15.4 L11.4 21.6 L14.2 20.4 L11.5 14.3 L17.6 14.1 Z" fill="#FFFFFF" stroke="#111827" stroke-width="1.4" stroke-linejoin="round"/></svg>')

def html(base='assets/screens', I=None):
    """The hero well. I: the page's icon map (pause/play). The animated stage is role=img; the button sits outside it."""
    caps = ''.join(f'<p class="oh-cap oh-cap--{i + 1}"><span class="oh-cap__k">{k}</span><span class="oh-cap__t">{t}</span></p>'
                   for i, (k, t) in enumerate(CAPTIONS))
    img = lambda f, cls: f'<img class="oh-scr {cls}" src="{base}/{f}{V}" width="2000" height="1480" alt="" loading="eager" decoding="async">'
    win = ('<div class="oh-win">'
           + img('01-empty-listing.jpg', 'oh-s1')
           + '<span class="oh-type oh-type--title">Vitamin C Serum</span><span class="oh-type oh-type--cat">Skincare</span>'
           + img('02-autofill-in-progress.jpg', 'oh-s2')
           + '<span class="oh-bar" aria-hidden="true"></span>'
           + img('03-listing-autofilled.jpg', 'oh-s3')
           + '<span class="oh-scan" aria-hidden="true"></span>'
           + '<span class="oh-glow oh-glow--brand" aria-hidden="true"></span><span class="oh-glow oh-glow--tags" aria-hidden="true"></span>'
           + img('00-v3-listing-page-match.jpg', 'oh-v3')
           + '<span class="oh-ripple" aria-hidden="true"></span>' + CURSOR + '</div>')
    pause = I['pause'] if I else ''
    play = I['play'] if I else ''
    return ('  <div class="cs-hero-well oh-wrap">'
            '<div class="pm-media pm-media--21x9 oh" data-oh role="img" '
            'aria-label="OmniSynkAI AI autofill: the old v3 listing page gives way to the launch version; a seller types a title and a category, '
            'clicks the AI autofill icon, a dialog shows autofill at work, and the listing fills in with the AI-written brand and tags highlighted.">'
            f'<div class="oh-stage"><div class="oh-copy" aria-hidden="true">{_logo()}<p class="oh-h">AI autofill for inventory listings</p>'
            f'<div class="oh-caps">{caps}</div></div>{win}</div></div>'
            '<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-btn--sm oh-toggle" aria-pressed="false" aria-label="Pause animation" data-oh-toggle hidden>'
            f'<span class="oh-ic oh-ic--pause">{pause}</span><span class="oh-ic oh-ic--play" hidden>{play}</span></button></div>\n'
            # Start frame before first paint (no JS or reduced motion: the final frame stays)
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("oh--anim")})(document.querySelector("[data-oh]"))</script>\n')

CSS = r"""
/* ===== OmniSynkAI hero (omnisynkai_hero.py): v3 -> v4, then one-click autofill, looped ===== */
.oh-wrap { position: relative; }
.oh { container-type: inline-size; background: linear-gradient(160deg, #4745B0 0%, #5B43E8 40%, #755CFB 75%, #9B94E0 100%); }
.oh-stage { position: absolute; inset: 0; }
.oh-copy { position: absolute; left: 5cqw; top: 50%; width: 31cqw; transform: translateY(-50%); display: grid; gap: 2.2cqw; color: #FFFFFF; }
.oh-logo { width: 15cqw; height: auto; color: #FFFFFF; }
.oh-h { margin: 0; font-size: clamp(20px, 3.1cqw, 40px); line-height: 1.12; font-weight: var(--weight-medium); letter-spacing: -0.02em; font-stretch: var(--font-width-display); text-wrap: balance; }
.oh-caps { position: relative; min-height: 4.6em; font-size: clamp(13px, 1.3cqw, 17px); line-height: 1.4; }
.oh-cap { position: absolute; inset: 0 auto auto 0; margin: 0; display: grid; gap: .25em; opacity: 0; }
.oh-cap--4 { opacity: 1; }  /* final frame */
.oh-cap__k { font-weight: var(--weight-medium); color: #FFFFFF; }
.oh-cap__t { color: rgb(255 255 255 / 86%); }

/* The window: the listing page, its own container so typed text scales with it */
.oh-win { position: absolute; right: 5cqw; top: 50%; width: 52cqw; aspect-ratio: 2000 / 1480; transform: translateY(-50%); container-type: inline-size;
  border-radius: 1cqw; overflow: hidden; background: #FFFFFF; box-shadow: 0 2cqw 5cqw rgb(20 12 70 / 35%), 0 0 0 1px rgb(255 255 255 / 25%); isolation: isolate; }
.oh-scr { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }
.oh-s2, .oh-v3 { opacity: 0; }
.oh-type { position: absolute; top: 21.9%; transform: translateY(-50%); font-family: var(--font-sans); font-size: 1.3cqw; line-height: 1; color: #1F2430; white-space: nowrap; opacity: 0; }
.oh-type--title { left: 27.3%; }
.oh-type--cat { left: 49.1%; }
.oh-bar { position: absolute; left: 34.9%; top: 43.9%; width: 30.2%; height: .35cqw; background: linear-gradient(90deg, #7C5CFA, #A78BFA); transform-origin: left; transform: scaleX(0); opacity: 0; }
.oh-scan { position: absolute; left: 0; right: 0; top: 0; height: 6%; background: linear-gradient(to bottom, rgb(124 92 250 / 0%), rgb(124 92 250 / 22%)); opacity: 0; pointer-events: none; }
.oh-glow { position: absolute; top: 92.6%; height: 2.9%; border-radius: .5cqw; box-shadow: 0 0 0 .35cqw rgb(124 92 250 / 55%), 0 0 2cqw rgb(124 92 250 / 45%); opacity: 0; }
.oh-glow--brand { left: 11.2%; width: 5.6%; }
.oh-glow--tags { left: 43.5%; width: 11.9%; }
.oh-cursor { position: absolute; left: 92%; top: 80%; width: 2.6cqw; height: 2.6cqw; opacity: 0; filter: drop-shadow(0 .2cqw .4cqw rgb(0 0 0 / 25%)); transform-origin: 15% 10%; }
.oh-ripple { position: absolute; left: 81.8%; top: 20.5%; width: 4cqw; height: 4cqw; margin: -2cqw 0 0 -2cqw; border-radius: 50%; background: rgb(124 92 250 / 35%); opacity: 0; }

/* Pause / Play, outside the image role */
.oh-toggle { position: absolute; right: var(--space-3); bottom: var(--space-3); z-index: 2; }
.oh-toggle[hidden], .oh-ic[hidden] { display: none; }
.oh-ic { display: contents; }

/* Phones: the window alone, centred; the copy is in the aria-label */
@container (max-width: 599px) {
  .oh-copy { display: none; }
  .oh-win { right: auto; left: 50%; width: 66cqw; transform: translate(-50%, -50%); }
}

/* ---- The loop (10s). Default styles above are the final frame. ---- */
.oh--anim .oh-v3 { opacity: 1; }
.oh--anim .oh-s3 { clip-path: inset(0 0 100% 0); }
.oh--anim .oh-cap--4 { opacity: 0; }
.oh--anim.is-play * { animation-duration: 10s; animation-iteration-count: infinite; animation-fill-mode: both; animation-timing-function: ease-in-out; }
.oh--anim.is-paused * { animation-play-state: paused; }
.oh--anim.is-play .oh-v3 { animation-name: oh-v3; }
.oh--anim.is-play .oh-type--title { animation-name: oh-title; }
.oh--anim.is-play .oh-type--cat { animation-name: oh-cat; }
.oh--anim.is-play .oh-cursor { animation-name: oh-cursor; }
.oh--anim.is-play .oh-ripple { animation-name: oh-ripple; }
.oh--anim.is-play .oh-s2 { animation-name: oh-s2; }
.oh--anim.is-play .oh-bar { animation-name: oh-bar; }
.oh--anim.is-play .oh-s3 { animation-name: oh-s3; }
.oh--anim.is-play .oh-scan { animation-name: oh-scan; }
.oh--anim.is-play .oh-glow { animation-name: oh-glow; }
.oh--anim.is-play .oh-cap--1 { animation-name: oh-c1; }
.oh--anim.is-play .oh-cap--2 { animation-name: oh-c2; }
.oh--anim.is-play .oh-cap--3 { animation-name: oh-c3; }
.oh--anim.is-play .oh-cap--4 { animation-name: oh-c4; }
@keyframes oh-v3 { 0%, 15% { opacity: 1; } 21%, 94% { opacity: 0; } 100% { opacity: 1; } }
@keyframes oh-title { 0% { opacity: 1; clip-path: inset(-40% 100% -40% 0); } 24% { opacity: 1; clip-path: inset(-40% 100% -40% 0); animation-timing-function: steps(15, end); }
  32% { clip-path: inset(-40% 0 -40% 0); } 46% { opacity: 1; clip-path: inset(-40% 0 -40% 0); } 48%, 100% { opacity: 0; clip-path: inset(-40% 0 -40% 0); } }
@keyframes oh-cat { 0%, 33% { opacity: 0; } 35%, 46% { opacity: 1; } 48%, 100% { opacity: 0; } }
@keyframes oh-cursor { 0%, 32% { opacity: 0; left: 92%; top: 80%; transform: scale(1); } 35% { opacity: 1; left: 90%; top: 72%; }
  43% { left: 81.2%; top: 19.6%; transform: scale(1); } 44.5% { transform: scale(.82); } 46% { opacity: 1; transform: scale(1); left: 81.2%; top: 19.6%; }
  50%, 100% { opacity: 0; left: 81.2%; top: 19.6%; transform: scale(1); } }
@keyframes oh-ripple { 0%, 44% { opacity: 0; transform: scale(.3); } 44.5% { opacity: .9; transform: scale(.4); } 51%, 100% { opacity: 0; transform: scale(2.4); } }
@keyframes oh-s2 { 0%, 46% { opacity: 0; } 49%, 70% { opacity: 1; } 72%, 100% { opacity: 0; } }
@keyframes oh-bar { 0%, 49% { opacity: 0; transform: scaleX(0); } 50% { opacity: 1; transform: scaleX(0); } 62% { opacity: 1; transform: scaleX(1); } 64%, 100% { opacity: 0; transform: scaleX(1); } }
@keyframes oh-s3 { 0%, 63% { clip-path: inset(0 0 100% 0); } 72%, 100% { clip-path: inset(0 0 0 0); } }
@keyframes oh-scan { 0%, 62% { opacity: 0; top: -6%; } 63% { opacity: 1; top: -6%; } 72% { opacity: 1; top: 100%; } 74%, 100% { opacity: 0; top: 100%; } }
@keyframes oh-glow { 0%, 73% { opacity: 0; transform: scale(1); } 77% { opacity: 1; transform: scale(1.08); } 81% { opacity: 1; transform: scale(1); } 85% { opacity: 1; transform: scale(1.06); } 90% { opacity: 1; transform: scale(1); } 94%, 100% { opacity: 0; } }
@keyframes oh-c1 { 0%, 16% { opacity: 1; } 19%, 96% { opacity: 0; } 100% { opacity: 1; } }
@keyframes oh-c2 { 0%, 19% { opacity: 0; } 22%, 38% { opacity: 1; } 41%, 100% { opacity: 0; } }
@keyframes oh-c3 { 0%, 40% { opacity: 0; } 43%, 61% { opacity: 1; } 64%, 100% { opacity: 0; } }
@keyframes oh-c4 { 0%, 63% { opacity: 0; } 66%, 93% { opacity: 1; } 96%, 100% { opacity: 0; } }
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
    var imgs = [].map.call(hero.querySelectorAll('img'), function (i) { return i.decode ? i.decode().catch(function () {}) : 0; });
    Promise.race([Promise.all(imgs), new Promise(function (r) { setTimeout(r, 2000); })]).then(function () { ready = true; sync(); });
  })();
"""
