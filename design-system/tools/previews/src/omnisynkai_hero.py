"""OmniSynkAI case-study hero: a close-up of one-click AI autofill, as a short loop.

No copy and no full screens: on OmniSynkAI's brand gradient (the landing card's art), the listing page is rebuilt large in
HTML components with the shipped UI's own look (title bar; Description, Media, Brand & Tags cards in their empty state).
One CSS timeline (10s, looped):
  1. The title and category type in; the AI autofill icon starts to pulse.
  2. A cursor clicks it (a press and a ripple). The bar's status becomes "Filling out your listing", the icon spins and a
     shimmer sweeps across the empty cards.
  3. The AI content arrives in a stagger: the description writes in line by line, product photos pop into the media grid
     (cropped from Serena's final export), and the brand and tags chips land with their purple highlight and a glow.
  4. The bar flips to "Listing Autofilled", More options appears and Publish turns on. Hold, then a quick reset.
Sized in u (1cqw of the hero; converted by the regex below, as in procense_hero.py). Colours are project art (the
shipped UI's greys, purple and blue). Starts when in view, the tab is visible and the image has decoded; pauses off
screen and on Pause (WCAG 2.2.2); reduced motion or no JS show the final frame and no button.
"""
import re

V = '?v=2'

SPARK = ('<svg class="oh-spark" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><defs><linearGradient id="ohg" x1="0" y1="0" x2="1" y2="1">'
         '<stop offset="0" stop-color="#A78BFA"/><stop offset="1" stop-color="#6D4AF0"/></linearGradient></defs>'
         '<path fill="url(#ohg)" d="M10 3 C10.6 7.4 12.6 9.4 17 10 C12.6 10.6 10.6 12.6 10 17 C9.4 12.6 7.4 10.6 3 10 C7.4 9.4 9.4 7.4 10 3 Z"/>'
         '<path fill="url(#ohg)" d="M18 13 C18.3 15.3 19.2 16.2 21.5 16.5 C19.2 16.8 18.3 17.7 18 20 C17.7 17.7 16.8 16.8 14.5 16.5 C16.8 16.2 17.7 15.3 18 13 Z"/></svg>')
CURSOR = ('<svg class="oh-cursor" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
          '<path d="M4 2.5 L4 19.5 L8.6 15.4 L11.4 21.6 L14.2 20.4 L11.5 14.3 L17.6 14.1 Z" fill="#FFFFFF" stroke="#111827" stroke-width="1.4" stroke-linejoin="round"/></svg>')
CHEV = '<svg class="oh-chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

DESC = ['Give your skin a radiant boost with our potent Vitamin C Serum!',
        'Packed with antioxidants, this lightweight formula helps:',
        '•  Brighten and even skin tone for a luminous complexion.',
        '•  Reduce the appearance of fine lines and wrinkles.']
# Photo crops from the final export (03, 1000 x 740 preview px): x, y, w, h
THUMBS = [(104, 460, 163, 163), (274, 460, 79, 79), (360, 460, 79, 79), (274, 545, 79, 79), (360, 545, 79, 79)]

def _thumb(i, x, y, w, h, base):
    bs = 1000 / w * 100
    px = x / (1000 - w) * 100
    py = y / (740 - h) * 100
    return (f'<span class="oh-ph oh-ph--{i}" style="background-image:url({base}/03-listing-autofilled.jpg{V});'
            f'background-size:{bs:.1f}% auto;background-position:{px:.2f}% {py:.2f}%"></span>')

def html(base='assets/screens', I=None):
    lines = ''.join(f'<span class="oh-line oh-line--{i + 1}">{t}</span>' for i, t in enumerate(DESC))
    thumbs = ''.join(_thumb(i + 1, *t, base) for i, t in enumerate(THUMBS))
    slots = ''.join(f'<span class="oh-slot oh-slot--{i + 1}"></span>' for i in range(len(THUMBS)))
    bar = ('<div class="oh-bar">'
           '<div class="oh-status">'
           '<p class="oh-st oh-st--idle"><b>Save time with Autofill</b><span>Fill out required details and click the stars to begin.</span></p>'
           '<p class="oh-st oh-st--busy"><b>Filling out your listing</b><span>This takes a few seconds.</span></p>'
           f'<p class="oh-st oh-st--done"><b>{SPARK}Listing Autofilled</b><span>Feel free to edit details</span></p></div>'
           '<span class="oh-div oh-div--1"></span>'
           '<div class="oh-field oh-field--title"><span class="oh-lbl">Title</span><span class="oh-in"><span class="oh-val oh-val--title">Vitamin C Serum</span></span></div>'
           f'<div class="oh-field oh-field--cat"><span class="oh-lbl">Product category</span><span class="oh-in"><span class="oh-val oh-val--cat">Skincare</span>{CHEV}</span></div>'
           f'<span class="oh-ai">{SPARK}<span class="oh-pulse"></span><span class="oh-ripple"></span></span>'
           f'<span class="oh-more">More options{CHEV}</span>'
           '<span class="oh-div oh-div--2"></span>'
           '<span class="oh-pub">Publish listing</span></div>')
    cards = ('<div class="oh-card oh-desc"><span class="oh-h">Description</span><span class="oh-tools"></span>'
             f'<div class="oh-lines">{lines}</div></div>'
             f'<div class="oh-card oh-media"><span class="oh-h">Media</span><div class="oh-grid">{slots}{thumbs}</div></div>'
             '<div class="oh-card oh-meta"><div class="oh-mf"><span class="oh-h">Brand</span><span class="oh-in"><span class="oh-chip oh-chip--1">By Rituals</span></span></div>'
             '<div class="oh-mf"><span class="oh-h">Tags</span><span class="oh-in"><span class="oh-chip oh-chip--2">#skincare</span><span class="oh-chip oh-chip--3">#vitaminC</span></span></div></div>'
             '<span class="oh-shimmer" aria-hidden="true"></span>')
    pause = I['pause'] if I else ''
    play = I['play'] if I else ''
    return ('  <div class="cs-hero-well oh-wrap">'
            '<div class="pm-media pm-media--21x9 oh" data-oh role="img" '
            'aria-label="OmniSynkAI AI autofill, close up: a seller types a title and a category, clicks the AI autofill icon, and the listing fills in by itself: '
            'a description writes in, product photos appear, and the brand and tags arrive highlighted in purple as AI-written. The bar then reads Listing Autofilled and Publish turns on.">'
            f'<div class="oh-stage"><div class="oh-app">{bar}{cards}{CURSOR}</div></div></div>'
            '<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-btn--sm oh-toggle" aria-pressed="false" aria-label="Pause animation" data-oh-toggle hidden>'
            f'<span class="oh-ic oh-ic--pause">{pause}</span><span class="oh-ic oh-ic--play" hidden>{play}</span></button></div>\n'
            '  <script>(function(h){if(h&&!matchMedia("(prefers-reduced-motion: reduce)").matches)h.classList.add("oh--anim")})(document.querySelector("[data-oh]"))</script>\n')

_CSS = r"""
/* ===== OmniSynkAI hero (omnisynkai_hero.py): one-click AI autofill, close up, looped ===== */
.oh-wrap { position: relative; }
.oh { --u: 1cqw; container-type: inline-size; background: radial-gradient(90% 120% at 50% 110%, rgb(255 255 255 / 22%) 0%, rgb(255 255 255 / 0%) 60%), linear-gradient(160deg, #4745B0 0%, #5B43E8 40%, #755CFB 75%, #9B94E0 100%); }
@container (max-width: 599px) { .oh { --u: 1.18cqw; } }
.oh-stage { position: absolute; inset: 0; display: grid; place-items: center; }
.oh-app { position: relative; width: 78u; height: 35.5u; border-radius: 1.6u; background: #F5F5F7; box-shadow: 0 2u 5u rgb(20 12 70 / 35%), 0 0 0 1px rgb(255 255 255 / 30%);
  font-family: var(--font-sans); color: #1F2430; font-size: 1.05u; line-height: 1.3; }
.oh-app * { box-sizing: border-box; }

/* Title bar */
.oh-bar { position: absolute; left: 1.5u; top: 1.5u; width: 75u; height: 7.6u; border-radius: 1u; background: #FFFFFF; box-shadow: 0 0 0 1px #E3E6EC; }
.oh-status { position: absolute; left: 1.6u; top: 50%; width: 13.4u; transform: translateY(-50%); height: 4.4u; }
.oh-st { position: absolute; inset: 0; margin: 0; display: grid; align-content: center; gap: .3u; }
.oh-st b { display: flex; align-items: center; gap: .5u; font-weight: 500; font-size: 1.15u; }
.oh-st span { font-size: .85u; color: #6B7280; line-height: 1.25; }
.oh-st--idle, .oh-st--busy { opacity: 0; }
.oh-st .oh-spark { width: 1.4u; height: 1.4u; }
.oh-div { position: absolute; top: 1.5u; bottom: 1.5u; width: 1px; background: #E3E6EC; }
.oh-div--1 { left: 15.8u; } .oh-div--2 { left: 66.2u; }
.oh-field { position: absolute; top: 1.15u; width: 18u; display: grid; gap: .45u; }
.oh-field--title { left: 17.2u; } .oh-field--cat { left: 36.6u; }
.oh-lbl { font-size: .85u; color: #4B5563; }
.oh-in { position: relative; display: flex; align-items: center; gap: .6u; height: 3.5u; padding: 0 1u; border-radius: .6u; background: #FFFFFF; box-shadow: inset 0 0 0 1px #CBD2DC; overflow: hidden; }
.oh-val { font-size: 1.05u; white-space: nowrap; }
.oh-chev { width: 1.3u; height: 1.3u; margin-left: auto; color: #4B5563; flex: none; }
.oh-ai { position: absolute; left: 60.2u; top: 50%; width: 3.6u; height: 3.6u; transform: translateY(-50%); display: grid; place-items: center; opacity: 0; }
.oh-ai .oh-spark { width: 2.6u; height: 2.6u; position: relative; z-index: 1; }
.oh-pulse, .oh-ripple { position: absolute; inset: 0; border-radius: 50%; }
.oh-pulse { box-shadow: 0 0 0 .3u rgb(124 92 250 / 45%); opacity: 0; }
.oh-ripple { background: rgb(124 92 250 / 30%); opacity: 0; }
.oh-more { position: absolute; left: 56.6u; top: 50%; transform: translateY(-50%); display: flex; align-items: center; gap: .4u; font-size: 1.05u; white-space: nowrap; }
.oh-more .oh-chev { margin: 0; }
.oh-pub { position: absolute; left: 67.6u; top: 50%; width: 6.4u; height: 3.4u; transform: translateY(-50%); display: grid; place-items: center; border-radius: .6u; background: #4461DC; color: #FFFFFF; font-size: .85u; font-weight: 500; white-space: nowrap; }

/* Cards */
.oh-card { position: absolute; border-radius: 1u; background: #FFFFFF; box-shadow: 0 0 0 1px #E3E6EC; overflow: hidden; }
.oh-h { font-size: .95u; color: #374151; }
.oh-desc { left: 1.5u; top: 10.6u; width: 45.5u; height: 12.6u; padding: 1u 1.4u; }
.oh-tools { display: block; height: .5u; margin: .8u 0 .9u; border-radius: .25u; background: repeating-linear-gradient(90deg, #D9DDE4 0 1.3u, transparent 1.3u 2.4u); width: 22u; }
.oh-lines { display: grid; gap: .35u; }
.oh-line { display: block; white-space: nowrap; font-size: .98u; color: #1F2430; }
.oh-media { left: 48.6u; top: 10.6u; width: 27.9u; height: 23.4u; padding: 1u 1.2u; }
.oh-grid { position: relative; margin-top: 1u; height: 17u; }
.oh-slot, .oh-ph { position: absolute; border-radius: .5u; }
.oh-slot { border: 1px dashed #B9BFCC; }
.oh-ph { background-repeat: no-repeat; }
.oh-slot--1, .oh-ph--1 { left: 0; top: 0; width: 12.4u; height: 12.4u; }
.oh-slot--2, .oh-ph--2 { left: 13.2u; top: 0; width: 6u; height: 6u; }
.oh-slot--3, .oh-ph--3 { left: 19.8u; top: 0; width: 6u; height: 6u; }
.oh-slot--4, .oh-ph--4 { left: 13.2u; top: 6.4u; width: 6u; height: 6u; }
.oh-slot--5, .oh-ph--5 { left: 19.8u; top: 6.4u; width: 6u; height: 6u; }
.oh-meta { left: 1.5u; top: 24.6u; width: 45.5u; height: 9.4u; padding: 1u 1.4u; display: grid; grid-template-columns: 1fr 1fr; gap: 1.4u; }
.oh-mf { display: grid; gap: .5u; align-content: start; }
.oh-chip { display: inline-block; padding: .2u .5u; border-radius: .4u; background: #EDE7FB; color: #6D3FD0; font-size: .95u; white-space: nowrap; box-shadow: 0 0 0 0 rgb(124 92 250 / 0%); }
.oh-shimmer { position: absolute; left: 1.5u; top: 10.6u; width: 75u; height: 23.4u; border-radius: 1u; pointer-events: none; opacity: 0;
  background: linear-gradient(100deg, rgb(167 139 250 / 0%) 30%, rgb(167 139 250 / 30%) 50%, rgb(167 139 250 / 0%) 70%); background-size: 250% 100%; background-position: 120% 0; }
.oh-cursor { position: absolute; left: 70u; top: 30u; width: 2.6u; height: 2.6u; opacity: 0; filter: drop-shadow(0 .2u .4u rgb(0 0 0 / 25%)); transform-origin: 15% 10%; pointer-events: none; }

/* Pause / Play, outside the image role */
.oh-toggle { position: absolute; right: var(--space-3); bottom: var(--space-3); z-index: 2; }
.oh-toggle[hidden], .oh-ic[hidden] { display: none; }
.oh-ic { display: contents; }

/* ---- The loop (10s). The rules above are the final frame; with motion, every layer runs from its 0% frame,
   held paused until the hero is ready and in view. ---- */
.oh--anim * { animation-duration: 10s; animation-iteration-count: infinite; animation-fill-mode: both; animation-timing-function: ease-in-out; animation-play-state: paused; }
.oh--anim.is-play:not(.is-paused) * { animation-play-state: running; }
.oh--anim .oh-val--title { animation-name: oh-title; }
.oh--anim .oh-val--cat { animation-name: oh-cat; }
.oh--anim .oh-st--idle { animation-name: oh-idle; }
.oh--anim .oh-st--busy { animation-name: oh-busy; }
.oh--anim .oh-st--done { animation-name: oh-done; }
.oh--anim .oh-ai { animation-name: oh-ai; }
.oh--anim .oh-ai .oh-spark { animation-name: oh-spin; }
.oh--anim .oh-pulse { animation-name: oh-pulse; }
.oh--anim .oh-ripple { animation-name: oh-ripple; }
.oh--anim .oh-more { animation-name: oh-more; }
.oh--anim .oh-pub { animation-name: oh-pub; }
.oh--anim .oh-cursor { animation-name: oh-cursor; }
.oh--anim .oh-shimmer { animation-name: oh-shimmer; }
.oh--anim .oh-line { animation-name: oh-line; }
.oh--anim .oh-line--2 { animation-name: oh-line2; } .oh--anim .oh-line--3 { animation-name: oh-line3; } .oh--anim .oh-line--4 { animation-name: oh-line4; }
.oh--anim .oh-ph { animation-name: oh-ph1; }
.oh--anim .oh-ph--2 { animation-name: oh-ph2; } .oh--anim .oh-ph--3 { animation-name: oh-ph3; } .oh--anim .oh-ph--4 { animation-name: oh-ph4; } .oh--anim .oh-ph--5 { animation-name: oh-ph5; }
.oh--anim .oh-slot { animation-name: oh-slot; }
.oh--anim .oh-chip { animation-name: oh-chip1; }
.oh--anim .oh-chip--2 { animation-name: oh-chip2; } .oh--anim .oh-chip--3 { animation-name: oh-chip3; }

/* typing and the empty bar */
@keyframes oh-title { 0%, 5% { clip-path: inset(-40% 100% -40% 0); animation-timing-function: steps(15, end); } 17%, 94% { clip-path: inset(-40% 0 -40% 0); opacity: 1; } 97%, 100% { clip-path: inset(-40% 0 -40% 0); opacity: 0; } }
@keyframes oh-cat { 0%, 18% { opacity: 0; } 21%, 94% { opacity: 1; } 97%, 100% { opacity: 0; } }
@keyframes oh-idle { 0%, 29% { opacity: 1; } 32%, 96% { opacity: 0; } 100% { opacity: 1; } }
@keyframes oh-busy { 0%, 30% { opacity: 0; } 33%, 46% { opacity: 1; } 49%, 100% { opacity: 0; } }
@keyframes oh-done { 0%, 47% { opacity: 0; } 50%, 94% { opacity: 1; } 97%, 100% { opacity: 0; } }
/* the AI autofill icon: appears with the fields filled, pulses, is clicked, spins while it works, then gives way to More options */
@keyframes oh-ai { 0%, 19% { opacity: .35; } 22% { opacity: 1; } 47% { opacity: 1; } 50%, 96% { opacity: 0; } 100% { opacity: .35; } }
@keyframes oh-spin { 0%, 31% { transform: rotate(0) scale(1); } 29.5% { transform: scale(1); } 30.5% { transform: scale(.8); } 46% { transform: rotate(540deg) scale(1); } 100% { transform: rotate(540deg) scale(1); } }
@keyframes oh-pulse { 0%, 22% { opacity: 0; transform: scale(1); } 24% { opacity: 1; transform: scale(1); } 27% { opacity: 0; transform: scale(1.7); } 27.1% { opacity: 1; transform: scale(1); } 30% { opacity: 0; transform: scale(1.7); } 100% { opacity: 0; } }
@keyframes oh-ripple { 0%, 30.4% { opacity: 0; transform: scale(.4); } 30.6% { opacity: 1; transform: scale(.5); } 36%, 100% { opacity: 0; transform: scale(2.6); } }
@keyframes oh-cursor { 0%, 21% { opacity: 0; left: 70u; top: 30u; transform: scale(1); } 23% { opacity: 1; } 29.5% { left: 63.1u; top: 5u; transform: scale(1); }
  30.5% { transform: scale(.82); } 31.5% { opacity: 1; transform: scale(1); left: 63.1u; top: 5u; } 38%, 100% { opacity: 0; left: 64u; top: 12u; } }
@keyframes oh-more { 0%, 48% { opacity: 0; transform: translateY(-50%) translateX(1u); } 51%, 94% { opacity: 1; transform: translateY(-50%); } 97%, 100% { opacity: 0; transform: translateY(-50%); } }
@keyframes oh-pub { 0%, 48% { background: #B5C0EF; } 51%, 94% { background: #4461DC; } 97%, 100% { background: #B5C0EF; } }
/* loading: a shimmer sweeps across the empty cards */
@keyframes oh-shimmer { 0%, 32% { opacity: 0; background-position: 120% 0; } 34% { opacity: 1; background-position: 120% 0; } 40% { background-position: -20% 0; } 40.1% { background-position: 120% 0; } 46% { opacity: 1; background-position: -20% 0; } 48%, 100% { opacity: 0; background-position: -20% 0; } }
/* AI content arrives in a stagger: description lines write in, photos pop, chips land with a glow */
@keyframes oh-line { 0%, 48% { clip-path: inset(-20% 100% -20% 0); } 54%, 94% { clip-path: inset(-20% 0 -20% 0); opacity: 1; } 97%, 100% { opacity: 0; clip-path: inset(-20% 0 -20% 0); } }
@keyframes oh-line2 { 0%, 51% { clip-path: inset(-20% 100% -20% 0); } 57%, 94% { clip-path: inset(-20% 0 -20% 0); opacity: 1; } 97%, 100% { opacity: 0; clip-path: inset(-20% 0 -20% 0); } }
@keyframes oh-line3 { 0%, 54% { clip-path: inset(-20% 100% -20% 0); } 59%, 94% { clip-path: inset(-20% 0 -20% 0); opacity: 1; } 97%, 100% { opacity: 0; clip-path: inset(-20% 0 -20% 0); } }
@keyframes oh-line4 { 0%, 56% { clip-path: inset(-20% 100% -20% 0); } 61%, 94% { clip-path: inset(-20% 0 -20% 0); opacity: 1; } 97%, 100% { opacity: 0; clip-path: inset(-20% 0 -20% 0); } }
@keyframes oh-ph1 { 0%, 50% { opacity: 0; transform: scale(.85); } 54%, 94% { opacity: 1; transform: scale(1); } 97%, 100% { opacity: 0; } }
@keyframes oh-ph2 { 0%, 52% { opacity: 0; transform: scale(.8); } 56%, 94% { opacity: 1; transform: scale(1); } 97%, 100% { opacity: 0; } }
@keyframes oh-ph3 { 0%, 54% { opacity: 0; transform: scale(.8); } 58%, 94% { opacity: 1; transform: scale(1); } 97%, 100% { opacity: 0; } }
@keyframes oh-ph4 { 0%, 56% { opacity: 0; transform: scale(.8); } 60%, 94% { opacity: 1; transform: scale(1); } 97%, 100% { opacity: 0; } }
@keyframes oh-ph5 { 0%, 58% { opacity: 0; transform: scale(.8); } 62%, 94% { opacity: 1; transform: scale(1); } 97%, 100% { opacity: 0; } }
@keyframes oh-slot { 0%, 52% { opacity: 1; } 60%, 94% { opacity: 0; } 98%, 100% { opacity: 1; } }
@keyframes oh-chip1 { 0%, 61% { opacity: 0; transform: translateY(.6u) scale(.9); } 64% { opacity: 1; transform: none; box-shadow: 0 0 0 .3u rgb(124 92 250 / 45%); } 72% { box-shadow: 0 0 0 0 rgb(124 92 250 / 0%); } 94% { opacity: 1; transform: none; } 97%, 100% { opacity: 0; } }
@keyframes oh-chip2 { 0%, 63% { opacity: 0; transform: translateY(.6u) scale(.9); } 66% { opacity: 1; transform: none; box-shadow: 0 0 0 .3u rgb(124 92 250 / 45%); } 74% { box-shadow: 0 0 0 0 rgb(124 92 250 / 0%); } 94% { opacity: 1; transform: none; } 97%, 100% { opacity: 0; } }
@keyframes oh-chip3 { 0%, 65% { opacity: 0; transform: translateY(.6u) scale(.9); } 68% { opacity: 1; transform: none; box-shadow: 0 0 0 .3u rgb(124 92 250 / 45%); } 76% { box-shadow: 0 0 0 0 rgb(124 92 250 / 0%); } 94% { opacity: 1; transform: none; } 97%, 100% { opacity: 0; } }
"""
# "Nu" -> calc(N * var(--u)), as in procense_hero.py (inside keyframes too)
CSS = re.sub(r'(?<![\w.#-])(-?(?:\d+(?:\.\d+)?|\.\d+))u\b', lambda m: f'calc({m.group(1)} * var(--u))', _CSS)

JS = r"""
  // OmniSynkAI hero: loops while in view and the tab is visible, once the photos have decoded; Pause/Play (WCAG 2.2.2)
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
    var img = new Image(); img.src = (hero.querySelector('.oh-ph').style.backgroundImage.match(/url\(["']?(.*?)["']?\)/) || [])[1] || '';
    Promise.race([img.decode ? img.decode().catch(function () {}) : Promise.resolve(), new Promise(function (r) { setTimeout(r, 2000); })]).then(function () { ready = true; sync(); });
  })();
"""
