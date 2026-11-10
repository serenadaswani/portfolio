import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import I, S, IMG, showcase
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
tokens = open(os.path.join(REPO, 'design-system', 'css', 'tokens.css')).read()
comps = open(os.path.join(REPO, 'design-system', 'css', 'components.css')).read()
NAME = 'Serena Daswani'
VER = 'v1.8'
# Real content comes from site.js (see CLAUDE.md). Anything marked Placeholder or TBC is still to replace.
FEATURED = [  # strongest first: full width
    ('form', 'Redesigning Mensio’s Data Explorer for self-serve analysis', 'Shipped 2026.', ['Product design', 'Analytics'], '2026 · Mensio', 'projects/mensio.html'),
    ('chart', 'Placeholder project', 'Your second strongest project.', ['Product design'], 'Placeholder', None)]
MORE = [  # two-up below
    ('queue', 'Placeholder project', 'A supporting project.', ['Product design'], 'Placeholder', None),
    ('grid', 'Placeholder project', 'A supporting project.', ['Design systems'], 'Placeholder', None)]
ROLES = [('D', 'Deploy', 'Product designer', 'Now', True), ('A', 'Apple', 'Product designer', 'Years TBC', False),
         ('P', 'Procense', 'Product designer', 'Years TBC', False), ('O', 'OmniSynkAI', 'Design intern', 'Years TBC', False)]
SOCIAL = [('LinkedIn', 'https://www.linkedin.com/in/serena-daswani'), ('GitHub', 'https://github.com/serenadaswani'), ('Framer', 'https://serenadaswani.framer.website/')]
SECTIONS = ['Work', 'About', 'Experience', 'Contact']

def card(p):
    k, t, sub, badges, eyebrow, href = p
    return showcase(k, t, sub, badges, eyebrow, href=href or '#work')

def role(m, org, r, yrs, now):
    dot = '<span class="pm-hero__dot" aria-hidden="true"></span>' if now else ''
    return (f'<li class="pm-experience__item"><span class="pm-experience__mark" aria-hidden="true">{m}</span>'
            f'<div class="pm-experience__head"><h3 class="pm-experience__org">{org}</h3><span class="pm-experience__role">{r}</span></div>'
            f'<span class="pm-experience__years">{dot}{yrs}</span></li>')

def copy_btn(i):
    # No public address yet: the button says so instead of copying a placeholder.
    return f'<button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-copy="" id="copy-{i}">{I["copy"]}<span>Copy email</span></button>'

def ext(label, href):
    return f'<a class="pm-link pm-link--subtle" href="{href}" target="_blank" rel="noopener">{label}<span class="pm-sr"> (opens in a new tab)</span></a>'

PAGE_CSS = r"""
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
.lp-about .pm-meta { max-width: 480px; }
.lp-contact { display: grid; justify-items: start; gap: var(--space-5); }
.lp-contact h3 { margin: 0; max-width: 22ch; font-size: var(--type-h2); line-height: var(--line-h2); font-weight: var(--weight-medium); letter-spacing: var(--tracking-heading); text-wrap: balance; }
.lp-contact h3 span { color: var(--color-text-tertiary); }
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
      <span class="pm-intro__mark" aria-hidden="true">SD</span>
      <h1 class="pm-intro__name">{NAME} <span>is a product designer who builds for fun.</span></h1>
      <p class="pm-intro__text">Currently designing at Deploy. Previously at Apple and Procense.</p>
      <span class="pm-intro__status"><span class="pm-hero__dot" aria-hidden="true"></span>Designing at Deploy</span>
      <div class="pm-intro__actions">{copy_btn('intro')}<a class="pm-btn pm-btn--ghost pm-btn--sm" href="#resume" data-soon>Résumé{I["ext"]}</a></div>
    </div>
    <nav class="pm-sidenav pm-split__nav" aria-label="Sections"><ul class="pm-sidenav__list">{NAV}</ul></nav>
    <div class="pm-split__foot">
      <ul aria-label="Elsewhere">{''.join(f'<li>{ext(l, h)}</li>' for l, h in SOCIAL)}</ul>
      <div class="lp-tools">
        <span class="pm-meta-text" id="lp-time" aria-label="Local time in Los Angeles">--:-- PT</span>
        <span class="pm-tooltip-anchor">
          <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--xs" id="lp-theme" aria-pressed="false" aria-labelledby="lp-theme-tip">{I["moon"]}</button>
          <span role="tooltip" id="lp-theme-tip" class="pm-tooltip lp-tip">Dark theme</span>
        </span>
      </div>
    </div>
  </aside>

  <main class="pm-split__main">
    <section class="pm-split__section" id="work" aria-labelledby="lp-work-h">
      <h2 class="pm-split__h" id="lp-work-h">Selected work</h2>
      <ul class="pm-showcase-grid">{''.join(f'<li class="pm-showcase-grid__wide">{card(p)}</li>' for p in FEATURED)}{''.join(f'<li>{card(p)}</li>' for p in MORE)}</ul>
    </section>

    <section class="pm-split__section" id="about" aria-labelledby="lp-about-h">
      <h2 class="pm-split__h" id="lp-about-h">About</h2>
      <div class="lp-about">
        <div class="lp-about" style="gap:var(--space-4)">
          <p>I’m a product designer at Deploy. Before that I designed at Apple and Procense, and interned at OmniSynkAI.</p>
          <p>Placeholder bio: how you work, what you care about, and one personal detail. Two or three short paragraphs.</p>
        </div>
        <dl class="pm-meta">
          <dt>Now</dt><dd>Product designer, Deploy</dd>
          <dt>Before</dt><dd>Apple, Procense, OmniSynkAI</dd>
          <dt>Based in</dt><dd>Los Angeles</dd>
        </dl>
      </div>
    </section>

    <section class="pm-split__section" id="experience" aria-labelledby="lp-exp-h">
      <h2 class="pm-split__h" id="lp-exp-h">Experience</h2>
      <ol class="pm-experience" aria-labelledby="lp-exp-h">{''.join(role(*r) for r in ROLES)}</ol>
    </section>

    <section class="pm-split__section lp-contact" id="contact" aria-labelledby="lp-contact-h">
      <h2 class="pm-split__h" id="lp-contact-h" style="margin:0">Contact</h2>
      <h3>Want to work together? <span>Say hello.</span></h3>
      <div class="lp-contact__actions">{copy_btn('contact')}{''.join(f'<a class="pm-btn pm-btn--ghost pm-btn--sm" href="{h}" target="_blank" rel="noopener">{l}{I["ext"]}<span class="pm-sr"> (opens in a new tab)</span></a>' for l, h in SOCIAL[:1])}</div>
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

  // Live local time, Los Angeles
  var t = document.getElementById('lp-time');
  function tick() {{ try {{ t.textContent = new Intl.DateTimeFormat('en-US', {{ hour: 'numeric', minute: '2-digit', timeZone: 'America/Los_Angeles' }}).format(new Date()) + ' PT'; }} catch (e) {{ t.textContent = ''; }} }}
  tick(); setInterval(tick, 15000);

  // Links to pages that aren't in this prototype stay put
  document.querySelectorAll('[data-soon], a[href="#work"]:not([data-spy]), a[href="projects/mensio.html"]').forEach(function (a) {{ a.addEventListener('click', function (e) {{ e.preventDefault(); }}); }});
}})();
</script>
'''
open(os.path.join(REPO, 'prototypes/landing.html'), 'w').write(page)
print(len(page))
