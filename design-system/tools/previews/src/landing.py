import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import I, S, IMG, showcase
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
tokens = open(os.path.join(REPO, 'design-system', 'css', 'tokens.css')).read()
comps = open(os.path.join(REPO, 'design-system', 'css', 'components.css')).read()
NAME = 'Serena Daswani'
VER = 'v1.9'
# Real content comes from site.js (see CLAUDE.md). Anything marked Placeholder or TBC is still to replace.
FEATURED = [  # strongest first: full width
    ('mensio', 'Redesigning Mensio’s Data Explorer for self-serve analysis', 'Turning analysts’ follow-up questions into a guided chart builder.', ['Product design', 'Analytics'], '2026 · Mensio', 'mensio.html'),
    ('procense', 'Modernizing manufacturing QA with digital forms', 'A tablet-first replacement for paper batch and SOP forms in chemical manufacturing.', ['Product design', 'Manufacturing'], '2023 · Procense', 'https://serenadaswani.framer.website/project-detail-procense-digital-forms-application')]
MORE = [  # two-up below
    ('apple', 'Rethinking an internal QA reporting tool', 'Sole designer on an internal tool for QA workflows.', ['Product design'], '2025 · Apple', 'https://serenadaswani.framer.website/project-detail-apple-internal-reporting-tool'),
    ('omni', 'AI autofill for inventory listings', 'Generated listing content with regeneration, feedback and tone options.', ['Product design', 'AI'], '2024 · OmniSynkAI', 'https://serenadaswani.framer.website/project-detail-omnisynkai-ai-autofill-feature')]
ROLES = [('D', 'Deploy', 'Product designer', 'Jan 2026 – Present', True, 'Product design for Mensio, and a design system adopted across Deploy’s products.'),
         ('A', 'Apple', 'UI/UX designer, contract', 'Aug 2024 – Dec 2025', False, 'Sole designer on an internal QA reporting tool.'),
         ('O', 'OmniSynkAI', 'Product design intern', 'Jul – Sep 2024', False, 'Designed an AI autofill feature for inventory listings.'),
         ('P', 'Procense', 'UI/UX designer, contract', 'Jan 2022 – Aug 2024', False, 'Sole designer for a B2B enterprise platform for manufacturing QA.')]
SOCIAL = [('LinkedIn', 'https://www.linkedin.com/in/serena-daswani'), ('GitHub', 'https://github.com/serenadaswani'), ('Framer', 'https://serenadaswani.framer.website/')]
SECTIONS = ['Work', 'About', 'Experience', 'Contact']

# Project art: a soft wash rising from the bottom (where the asset sits) and fading to white, like Anthropic's
# curated-collection cards. Literal hex is project art (content), not UI chrome. (bottom colour, mid colour, strength)
TINT = {
    'mensio':   ('#206CFD', '#206CFD', '16%'),
    'procense': ('#1B2026', '#1B2026', '11%'),
    'apple':    ('#B6BAC6', '#B6BAC6', '45%'),
    'omni':     ('#755CFB', '#9B94E0', '16%'),   # the sparkle purples from the Framer asset
}
# Apple logo, transparent, filled with the primary text colour (black in light, white in dark)
APPLE_LOGO = '<svg class="lp-shot__logo" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></svg>'

def card(p):
    k, t, sub, badges, eyebrow, href = p
    a, b, amt = TINT[k]
    html = showcase('white', t, sub, badges, eyebrow, href=href or '#work', more='')
    html = html.replace('class="pm-card pm-card--showcase"', f'class="pm-card pm-card--showcase lp-tint" style="--lp-a:{a};--lp-b:{b};--lp-amt:{amt}"', 1)
    # Placeholder asset: a plain 8px-rounded rectangle until the real screenshot exists. Apple keeps its logo centred.
    inner = APPLE_LOGO if k == 'apple' else ''
    shot = f'<div class="lp-shot{" lp-shot--apple" if k == "apple" else ""}" aria-hidden="true">{inner}</div>'
    i = html.index('<div class="pm-card__shot">'); j = html.index('</div></div></article>')
    return html[:i] + f'<div class="pm-card__shot">{shot}' + html[j:]

# Company logos (official artwork, saved in assets/logos/). Text parts use currentColor so they flip with the theme;
# brand accents keep their colour. Heights are optically balanced: all-caps and wide wordmarks sit smaller.
LOGO_H = {'Deploy': 22, 'Apple': 24, 'OmniSynkAI': 17, 'Procense': 13}
def logo(org):
    svg = open(os.path.join(REPO, 'assets', 'logos', org.lower() + '.svg')).read().strip()
    return svg.replace('<svg ', f'<svg class="lp-logo" style="height:{LOGO_H[org]}px" aria-hidden="true" focusable="false" ', 1)

def role(m, org, r, yrs, now, scope=''):
    dot = '<span class="pm-hero__dot" aria-hidden="true"></span>' if now else ''
    return (f'<li class="pm-experience__item">'
            f'<div class="pm-experience__head"><h3 class="pm-experience__org">{logo(org)}' + f'<span class="pm-sr">{org}</span>' + f'</h3><span class="pm-experience__role">{r}</span></div>'
            f'<span class="pm-experience__years">{dot}{yrs}</span>' + '</li>')  # no scope line: logo, role and dates only

def sec_head(n, label, hid, title, sub):
    """Section header (after ericsin.com): microcopy, then the heading with a quiet second line."""
    return (f'<div class="lp-sec__head"><p class="lp-sec__micro pm-meta-text">{n:02d} · {label}</p>'
            f'<h2 class="lp-sec__h" id="{hid}">{title}<span>{sub}</span></h2></div>')

def date_nb(yrs):
    """Keep each date whole and the dash with the start date, so a narrow column breaks as 'Jan 2026 –' / 'Present'."""
    a, _, b = yrs.partition(' – ')
    nb = lambda t: t.replace(' ', '\u00a0')
    return f'{nb(a)}\u00a0– {nb(b)}' if b else nb(a)

def tl_item(i, n, m, org, r, yrs, now, scope=''):
    """Timeline row: dates · dot on the rail · logo with the role underneath, centred on the row."""
    p = i / (n - 1) if n > 1 else 1
    return (f'<li class="lp-tl__item{" is-current" if now else ""}" style="--p:{p:.4f}">'
            f'<span class="lp-tl__date pm-meta-text">{date_nb(yrs)}</span>'
            '<span class="lp-tl__dot" aria-hidden="true"></span>'
            f'<div class="lp-tl__body"><h3 class="lp-tl__org">{logo(org)}<span class="pm-sr">{org}</span></h3>'
            f'<span class="lp-tl__role">{r}</span></div></li>')

def copy_btn(i):
    # No public address yet: the button says so instead of copying a placeholder.
    return f'<button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-copy="" id="copy-{i}">{I["copy"]}<span>Copy email</span></button>'

def ext(label, href):
    return f'<a class="pm-link pm-link--subtle" href="{href}" target="_blank" rel="noopener">{label}<span class="pm-sr"> (opens in a new tab)</span></a>'

PAGE_CSS = r"""
/* Page background: white in light (the system's canvas token stays paper); dark is unchanged */
@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) { --color-bg-canvas: var(--white); } }
[data-theme="light"] { --color-bg-canvas: var(--white); }
body { background: var(--color-bg-canvas); }
/* Side column on paper where it is a sidebar (>=1024px); dark keeps the surface step */
.lp { --lp-aside-bg: var(--paper); }
[data-theme="dark"] .lp { --lp-aside-bg: var(--color-bg-surface); }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .lp { --lp-aside-bg: var(--color-bg-surface); } }
@container (min-width: 1024px) { .pm-split__aside { background: var(--lp-aside-bg); } }

/* Sections (after ericsin.com): microcopy + heading on the left, content on the right (>=768px main column).
   Work keeps its grid full width under the header row. */
.lp-sec { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--space-6); }
@container (min-width: 768px) {
  .lp-sec { grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); column-gap: var(--space-10); row-gap: var(--space-10); align-items: start; }
  .lp-sec__full { grid-column: 1 / -1; }
}
.lp-sec__head { display: grid; gap: var(--space-3); align-content: start; }
.lp-sec__micro { margin: 0; }
/* Heading pair (after ericsin.com): same size and weight, primary vs a lighter grey.
   h3 is 24px from 768px up, which is WCAG large text, so there the sub-line may use the 3:1 grey
   (color-border-strong: 3.77:1 light, 3.67:1 dark). Below 768px h3 is 23px, so it stays tertiary (4.5:1+).
   prefers-contrast: more keeps tertiary everywhere. */
.lp-sec__h { margin: 0; display: grid; font-size: var(--type-h3); line-height: var(--line-h3); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h3); color: var(--color-text-primary); text-wrap: balance; }
.lp-sec__h span { color: var(--color-text-tertiary); }
@media (min-width: 768px) and (prefers-contrast: no-preference) { .lp-sec__h span { color: var(--color-border-strong); } }
.lp-sec__body { container: lp-body / inline-size; min-width: 0; }
.lp-sec__intro { margin: 0; max-width: 48ch; font-size: var(--type-body-md); line-height: var(--line-body-md); color: var(--color-text-secondary); text-wrap: pretty; }
/* Right-hand content starts level with the heading, not the microcopy above it */
@container (min-width: 768px) { .lp-sec__body { padding-top: calc(var(--type-label) * var(--line-label) + var(--space-3)); } }

/* Timeline: dates · rail with one dot per role · logo with the role underneath, each row centred.
   The rail and soft dots use color-border-default (decorative); the current role's dot is the selection colour.
   Animation (once, when the section comes into view): the line grows from the oldest role up to the present one,
   each row and dot appearing as the line reaches it, and lands on the current role with a small pulse.
   Static with reduced motion or without JS. */
.lp-tl { --lp-row: 76px; --lp-date: 9.5rem; --lp-gap: var(--space-5); --lp-dur: calc(var(--motion-duration-base) * 7);
  position: relative; list-style: none; margin: 0; padding: 0; }
.lp-tl::before { content: ""; position: absolute; left: calc(var(--lp-date) + var(--lp-gap) + 5px); top: calc(var(--lp-row) / 2); bottom: calc(var(--lp-row) / 2); width: 2px; border-radius: 1px; background: var(--color-border-default); transform-origin: 50% 100%; }
.lp-tl__item { display: grid; grid-template-columns: var(--lp-date) 12px minmax(0, 1fr); column-gap: var(--lp-gap); align-items: center; height: var(--lp-row); }
.lp-tl__date { text-align: right; text-wrap: balance; }
.lp-tl__item.is-current .lp-tl__date { color: var(--color-text-primary); }
.lp-tl__dot { position: relative; width: 12px; height: 12px; border-radius: 50%; background: var(--color-bg-canvas); box-shadow: inset 0 0 0 2px var(--color-border-default); }
.lp-tl__item.is-current .lp-tl__dot { background: var(--color-selected-indicator); box-shadow: 0 0 0 3px var(--color-action-selected-bg); }
.lp-tl__body { display: grid; gap: var(--space-1); justify-items: start; min-width: 0; }
.lp-tl__org { margin: 0; display: flex; align-items: center; min-height: 26px; }
.lp-tl .lp-logo { display: block; width: auto; color: var(--color-text-primary); }
.lp-tl__role { font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
@container lp-body (max-width: 479px) { .lp-tl { --lp-date: 6.5rem; --lp-gap: var(--space-4); } }

.lp-anim .lp-tl::before { transform: scaleY(0); }
.lp-anim .lp-tl__dot { transform: scale(0); }
.lp-anim .lp-tl__date, .lp-anim .lp-tl__body { opacity: 0; transform: translateY(var(--space-1)); }
.lp-anim .lp-tl.is-in::before { transform: scaleY(1); transition: transform var(--lp-dur) linear; }
.lp-anim .lp-tl.is-in .lp-tl__dot { transform: none; transition: transform var(--motion-duration-base) var(--motion-ease) calc(var(--p) * var(--lp-dur)); }
.lp-anim .lp-tl.is-in .lp-tl__date, .lp-anim .lp-tl.is-in .lp-tl__body { opacity: 1; transform: none; transition: opacity calc(var(--motion-duration-base) * 2) var(--motion-ease) calc(var(--p) * var(--lp-dur)), transform calc(var(--motion-duration-base) * 2) var(--motion-ease) calc(var(--p) * var(--lp-dur)); }
.lp-anim .lp-tl.is-in .is-current .lp-tl__dot::after { content: ""; position: absolute; inset: -3px; border-radius: 50%; box-shadow: 0 0 0 2px var(--color-selected-indicator); opacity: 0; animation: lp-land calc(var(--motion-duration-base) * 4) var(--motion-ease) var(--lp-dur) 1; }
@keyframes lp-land { from { opacity: .6; transform: scale(1); } to { opacity: 0; transform: scale(2.2); } }

/* Tinted showcase cards: copy on top, the wash and asset rise from the bottom */
.pm-card--showcase.lp-tint, .pm-card--showcase.lp-tint:hover, .pm-card--showcase.lp-tint:focus-within {
  background: linear-gradient(to top,
    color-mix(in srgb, var(--lp-a) var(--lp-amt), var(--color-bg-elevated)) 0%,
    color-mix(in srgb, var(--lp-b) calc(var(--lp-amt) * 0.45), var(--color-bg-elevated)) 45%,
    var(--color-bg-elevated) 90%);
  box-shadow: none; /* no border at rest */
}
/* Hover (and keyboard focus): a soft grey shadow, x 0 · y 3 · blur 12 · grey at 10% */
.pm-card--showcase.lp-tint:focus-within { box-shadow: 0 3px 12px rgb(27 32 38 / 10%); }
@media (hover: hover) { .pm-card--showcase.lp-tint:hover { box-shadow: 0 3px 12px rgb(27 32 38 / 10%); } }
@container pm-showcase (min-width: 768px) { .lp-tint .pm-card__copy { align-self: start !important; } }
.lp-tint .pm-card__shot { padding: var(--space-8) var(--space-8) var(--space-8) !important; align-self: end; }
@container pm-showcase (min-width: 768px) { .lp-tint .pm-card__shot { padding: var(--space-12) var(--space-10) var(--space-10) var(--space-2) !important; } }
@container pm-showcase (max-width: 479px) { .lp-tint .pm-card__shot { padding: var(--space-6) var(--space-5) var(--space-5) !important; } }
.lp-shot { aspect-ratio: 16 / 10; border-radius: var(--radius-md); background: var(--color-bg-elevated); box-shadow: 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); display: grid; place-items: center; }
.lp-shot--apple { background: none; box-shadow: none; color: var(--color-text-primary); }
.lp-shot__logo { width: 16%; min-width: 48px; height: auto; }
@media (prefers-reduced-motion: no-preference) {
  .pm-card--showcase.lp-tint { transition: box-shadow var(--motion-duration-base) var(--motion-ease); }
  .lp-shot { transition: transform var(--motion-duration-base) var(--motion-ease); }
}
@media (hover: hover) and (prefers-reduced-motion: no-preference) { .pm-card--showcase.lp-tint:hover .lp-shot { transform: translateY(calc(-1 * var(--space-1))); } }
/* ===== Landing composition (v1.8) =====
   Layout: split. Sticky 360px intro + vertical nav on the left (≥1024px); work, about, experience, contact on the right.
   Work = Card --showcase: strongest projects full width, then two-up. */
html { scroll-padding-top: var(--space-6); }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
body { font-family: var(--font-sans); }
.lp { container-type: inline-size; padding-left: env(safe-area-inset-left, 0px); padding-right: env(safe-area-inset-right, 0px); }
.lp-tools { display: flex; align-items: center; gap: var(--space-2); }
.lp-tip { left: auto; right: 0; transform: none; } /* the toggle sits at the right edge: open the tip leftwards */
.lp-about { display: grid; gap: var(--space-8); }
.lp-about p { margin: 0; max-width: 60ch; font-size: var(--type-body-md); line-height: var(--line-body-md); color: var(--color-text-secondary); text-wrap: pretty; }
.lp-about p:first-child { font-size: var(--type-body-lg); line-height: var(--line-body-lg); color: var(--color-text-primary); }
.lp-contact__actions { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.lp-colophon { margin: var(--space-16) 0 0; padding-top: var(--space-4); border-top: 1px solid var(--color-border-subtle); }
"""

NAV = ''.join(f'<li><a class="pm-sidenav__item" href="#{s.lower()}"{" aria-current=\"location\"" if j == 0 else ""} data-spy>{s}</a></li>' for j, s in enumerate(SECTIONS))

page = f'''<title>Serena Daswani Portfolio</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&display=swap">
<style>
/* ===== Paper × Midnight {VER} · tokens.css (verbatim) ===== */
{tokens}
/* ===== Paper × Midnight {VER} · components.css (verbatim) ===== */
{comps}
{PAGE_CSS}
</style>

<div class="lp" id="top">
<div class="pm-split">
  <aside class="pm-split__aside" aria-label="Introduction">
    <div class="pm-intro">
      <span class="pm-intro__photo pm-intro__photo--empty" aria-hidden="true">{I["user"]}</span>
      <h1 class="pm-intro__name">{NAME} <span>is a product designer who builds for fun.</span></h1>
      <p class="pm-intro__text">Currently designing at Deploy. Previously at Apple and Procense.</p>
      <span class="pm-intro__status"><span class="pm-hero__dot" aria-hidden="true"></span>Designing at Deploy</span>
      <div class="pm-intro__actions">{copy_btn('intro')}<a class="pm-btn pm-btn--ghost pm-btn--sm" href="#resume" data-soon>Resume{I["ext"]}</a></div>
    </div>
    <nav class="pm-sidenav pm-split__nav" aria-label="Sections"><ul class="pm-sidenav__list">{NAV}</ul></nav>
    <div class="pm-split__foot">
      <ul aria-label="Elsewhere">{''.join(f'<li>{ext(l, h)}</li>' for l, h in SOCIAL)}</ul>
      <div class="lp-tools">
        <span class="pm-meta-text" id="lp-time" aria-label="Local time in San Francisco">--:-- PT</span>
        <span class="pm-tooltip-anchor">
          <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--xs" id="lp-theme" aria-pressed="false" aria-labelledby="lp-theme-tip">{I["moon"]}</button>
          <span role="tooltip" id="lp-theme-tip" class="pm-tooltip lp-tip">Dark theme</span>
        </span>
      </div>
    </div>
  </aside>

  <main class="pm-split__main">
    <section class="pm-split__section lp-sec" id="work" aria-labelledby="lp-work-h">
      {sec_head(1, 'Work', 'lp-work-h', 'Selected work', '2022 – 2026')}
      <div class="lp-sec__body"><p class="lp-sec__intro">Product design for data-heavy tools: analytics, manufacturing QA, internal reporting and AI features.</p></div>
      <ul class="pm-showcase-grid lp-sec__full">{''.join(f'<li class="pm-showcase-grid__wide">{card(p)}</li>' for p in FEATURED)}{''.join(f'<li>{card(p)}</li>' for p in MORE)}</ul>
    </section>

    <section class="pm-split__section lp-sec" id="about" aria-labelledby="lp-about-h">
      {sec_head(2, 'About', 'lp-about-h', 'About me', 'San Francisco')}
      <div class="lp-sec__body lp-about">
        <div class="lp-about" style="gap:var(--space-4)">
          <p>I’m a product designer in San Francisco who turns complexity into clarity. I’m designing at Deploy; before that I designed at Apple and Procense, and interned at OmniSynkAI.</p>
          <p>My background is enterprise design: data-heavy tools for testing, QA and engineering. I’m hands-on from research and prototyping through to UI polish.</p><p>Off the clock, you’ll find me people-watching at my local Philz, or watching Bay Area sports from the couch.</p>
        </div>
      </div>
    </section>

    <section class="pm-split__section lp-sec" id="experience" aria-labelledby="lp-exp-h">
      {sec_head(3, 'Experience', 'lp-exp-h', '4+ years of experience', '2022 – 2026')}
      <div class="lp-sec__body"><ol class="lp-tl" aria-labelledby="lp-exp-h">{''.join(tl_item(len(ROLES) - 1 - j, len(ROLES), *r) for j, r in enumerate(ROLES))}</ol></div>
    </section>

    <section class="pm-split__section lp-sec" id="contact" aria-labelledby="lp-contact-h">
      {sec_head(4, 'Contact', 'lp-contact-h', 'Want to work together?', 'Say hello.')}
      <div class="lp-sec__body"><div class="lp-contact__actions">{copy_btn('contact')}{''.join(f'<a class="pm-btn pm-btn--ghost pm-btn--sm" href="{h}" target="_blank" rel="noopener">{l}{I["ext"]}<span class="pm-sr"> (opens in a new tab)</span></a>' for l, h in SOCIAL[:1])}</div></div>
    </section>

    <p class="pm-meta-text lp-colophon">© 2026 {NAME} · Built on Paper × Midnight {VER}</p>
  </main>
</div>
<p class="pm-sr" aria-live="polite" id="lp-live"></p>
</div>

<script>
(function () {{
  var root = document.documentElement;
  var themeBtn = document.getElementById('lp-theme');
  function isDark() {{ var t = root.getAttribute('data-theme'); return t ? t === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; }}
  function sync() {{ themeBtn.setAttribute('aria-pressed', String(isDark())); }}
  themeBtn.addEventListener('click', function () {{ root.setAttribute('data-theme', isDark() ? 'light' : 'dark'); sync(); }});
  sync();

  // Timeline: play bottom to top each time it comes into view; reset once it has fully left the screen,
  // so the next visit replays it. Not tied to scroll position. Skipped with reduced motion.
  var tl = document.querySelector('.lp-tl');
  if (tl && 'IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {{
    document.documentElement.classList.add('lp-anim');
    new IntersectionObserver(function (es) {{ es.forEach(function (e) {{
      if (e.intersectionRatio >= 0.35) tl.classList.add('is-in');
      else if (!e.isIntersecting) tl.classList.remove('is-in');
    }}); }}, {{ threshold: [0, 0.35] }}).observe(tl);
  }}

  // Scroll-spy: mark the section in view with aria-current="location"
  var links = [].slice.call(document.querySelectorAll('[data-spy]'));
  function spy() {{
    var cur = links[0], line = window.innerHeight * 0.35;
    links.forEach(function (a) {{ var s = document.querySelector(a.getAttribute('href')); if (s && s.getBoundingClientRect().top < line) cur = a; }});
    if ((window.innerHeight + window.scrollY) >= document.documentElement.scrollHeight - 2) cur = links[links.length - 1];
    links.forEach(function (a) {{ if (a === cur) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); }});
  }}
  window.addEventListener('scroll', spy, {{ passive: true }}); window.addEventListener('resize', spy); spy();

  // Copy email: no public address yet, so say that
  var live = document.getElementById('lp-live');
  document.querySelectorAll('[data-copy]').forEach(function (b) {{
    var label = b.querySelector('span');
    b.addEventListener('click', function () {{
      var e = b.getAttribute('data-copy');
      function done(ok, msg) {{ label.textContent = msg; live.textContent = ok ? 'Email address copied' : msg; setTimeout(function () {{ label.textContent = 'Copy email'; }}, 2000); }}
      if (!e) {{ done(false, 'Email TBC'); return; }}
      try {{ navigator.clipboard.writeText(e).then(function () {{ done(true, 'Copied'); }}, function () {{ done(false, e); }}); }} catch (x) {{ done(false, e); }}
    }});
  }});

  // Live local time, San Francisco (Pacific)
  var t = document.getElementById('lp-time');
  function tick() {{ try {{ t.textContent = new Intl.DateTimeFormat('en-US', {{ hour: 'numeric', minute: '2-digit', timeZone: 'America/Los_Angeles' }}).format(new Date()) + ' PT'; }} catch (e) {{ t.textContent = ''; }} }}
  tick(); setInterval(tick, 15000);

  // Links to pages that aren't in this prototype stay put
  document.querySelectorAll('[data-soon], a[href="#work"]:not([data-spy])').forEach(function (a) {{ a.addEventListener('click', function (e) {{ e.preventDefault(); }}); }});
}})();
</script>
'''
open(os.path.join(REPO, 'prototypes/landing.html'), 'w').write(page)
print(len(page))
