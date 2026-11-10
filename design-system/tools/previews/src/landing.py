import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import I, S, IMG
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
tokens = open(os.path.join(REPO, 'design-system', 'css', 'tokens.css')).read()
comps = open(os.path.join(REPO, 'design-system', 'css', 'components.css')).read()
NAME = 'Serena Daswani'
EMAIL = 'hello@serenadaswani.com'  # placeholder address

WORK = [('queue', 'Review queue for model evaluations', 'Product design · AI tooling', '2024'),
        ('grid', 'One token source for four product teams', 'Design systems · Web', '2023'),
        ('form', 'Permissions console for operators', 'Product design · Internal platform', '2022'),
        ('chart', 'Evaluation dashboards reviewers trust', 'Product design · Data viz', '2025')]
ROLES = [('NW', 'Northwind AI', 'Lead product designer', '2023 – Now', True, 'Evaluation tooling for model reviewers; set up the product design system.'),
         ('LS', 'Lumen Systems', 'Senior product designer', '2020 – 2023', False, 'Internal platform: permissions, audit trails and operator workflows.'),
         ('FS', 'Fieldstone', 'Product designer', '2018 – 2020', False, 'B2B analytics; first design hire, built the component library.'),
         ('SP', 'Studio Parallel', 'Designer', '2016 – 2018', False, 'Brand and web for early-stage startups.')]

def tile(k, t, sub, y, i):
    return (f'<li><article class="pm-card pm-card--tile"><div class="pm-card__stage">'
            f'<img src="{IMG[k]}" alt="" width="1600" height="1000" loading="{"eager" if i < 2 else "lazy"}" decoding="async">'
            f'<span class="pm-card__go" aria-hidden="true">{I["arrow"]}</span></div>'
            f'<div class="pm-card__row"><h3 class="pm-card__title"><a href="#work" data-soon>{t}</a></h3><span class="pm-mono">{y}</span></div>'
            f'<p class="pm-card__sub">{sub}</p></article></li>')

def role(m, org, r, yrs, now, scope):
    dot = '<span class="pm-hero__dot" aria-hidden="true"></span>' if now else ''
    return (f'<li class="pm-experience__item"><span class="pm-experience__mark" aria-hidden="true">{m}</span>'
            f'<div class="pm-experience__head"><h3 class="pm-experience__org">{org}</h3><span class="pm-experience__role">{r}</span></div>'
            f'<span class="pm-experience__years">{dot}{yrs}</span><p class="pm-experience__scope">{scope}</p></li>')

def btile(cls, eyebrow, title, text='', extra='', visual='', theme=''):
    th = f' data-theme="{theme}"' if theme else ''
    return (f'<article class="pm-bento__tile{cls}"{th}><div class="pm-bento__body"><p class="pm-bento__eyebrow">{eyebrow}</p>'
            + (f'<h3 class="pm-bento__title">{title}</h3>' if title else '') + (f'<p class="pm-bento__text">{text}</p>' if text else '') + extra + '</div>' + visual + '</article>')
def vis(k, bleed=False):
    return f'<div class="pm-bento__visual{" pm-bento__visual--bleed" if bleed else ""}"><div class="pm-media pm-media--16x10"><img src="{IMG[k]}" alt="" loading="lazy"></div></div>'
CHECKS = '<ul class="pm-bento__list">' + ''.join(f'<li>{I["check"]}<span>{x}</span></li>' for x in ['WCAG 2.2 AA contrast, checked as I design', 'Keyboard paths for every flow', 'Reduced motion and contrast settings respected']) + '</ul>'
BENTO = ('<div class="pm-bento">' +
  btile(' pm-bento__tile--featured pm-bento__tile--wide pm-bento__tile--tall', 'Systems', 'Design systems that scale across teams', 'Semantic tokens and a component library four product teams theme without forking.', visual=vis('queue')) +
  btile('', 'Outcome', '', '', '<p class="pm-bento__stat">−52%</p><p class="pm-bento__stat-label">median triage time, pilot cohort</p>') +
  btile(' pm-bento__tile--midnight', 'AI tooling', 'Interfaces for model evaluation', 'Ranked, explainable queues reviewers can argue with.', visual=vis('grid', True), theme='dark') +
  btile(' pm-bento__tile--half', 'Research', 'From interviews to roadmap', 'Contextual interviews turned into three bets and one deliberate cut.', visual=vis('chart')) +
  btile(' pm-bento__tile--half pm-bento__tile--tonal', 'Accessibility', 'Inclusive by default', '', CHECKS) + '</div>')

def copy_btn(i):
    return f'<button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-copy="{EMAIL}" id="copy-{i}">{I["copy"]}<span>Copy email</span></button>'

PAGE_CSS = r"""
/* ===== Landing composition (v1.7 components) =====
   Layout: one narrative column (1200px); floating centred nav; centred hero; staggered work grid;
   about = 7/12 bio + 4/12 spec sheet; bento; experience rows; closing contact. */
html { scroll-padding-top: calc(var(--space-20) + env(safe-area-inset-top, 0px)); }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
body { font-family: var(--font-sans); }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 21; background: var(--color-bg-canvas); }
.lp { container-type: inline-size; }
.lp .pm-topnav--floating { margin-top: var(--space-3); }
.lp-wrap { max-width: var(--content-max-width); margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
@container (min-width: 768px) { .lp-wrap { padding-left: max(var(--space-6), env(safe-area-inset-left, 0px)); padding-right: max(var(--space-6), env(safe-area-inset-right, 0px)); } }
.lp-sec { padding-block: var(--space-16); }
@container (min-width: 1024px) { .lp-sec { padding-block: var(--space-20); } }
.lp-sec__head { display: flex; align-items: baseline; justify-content: space-between; gap: var(--space-4); flex-wrap: wrap; padding-top: var(--space-4); margin-bottom: var(--space-10); border-top: 1px solid var(--color-border-subtle); }
.lp-sec__head h2 { margin: 0; font-size: var(--type-h3); line-height: var(--line-h3); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h3); }
.lp-hero { padding-top: var(--space-8); }
/* about */
.lp-about { display: grid; gap: var(--space-10); }
@container (min-width: 1024px) { .lp-about { grid-template-columns: repeat(12, minmax(0, 1fr)); gap: var(--space-6); } .lp-about__bio { grid-column: 1 / span 7; } .lp-about__spec { grid-column: 9 / span 4; align-self: start; } }
.lp-about__bio { min-width: 0; display: grid; gap: var(--space-5); }
.lp-about__bio p { margin: 0; max-width: 60ch; font-size: var(--type-body-md); line-height: var(--line-body-md); color: var(--color-text-secondary); text-wrap: pretty; }
.lp-about__bio p:first-child { font-size: var(--type-body-lg); line-height: var(--line-body-lg); color: var(--color-text-primary); }
.lp-clock { display: inline-flex; align-items: center; gap: var(--space-2); }
/* contact */
.lp-contact { display: grid; justify-items: center; text-align: center; gap: var(--space-6); padding-block: var(--space-20) var(--space-16); }
.lp-contact h2 { margin: 0; max-width: 22ch; font-size: var(--type-h2); line-height: var(--line-h2); font-weight: var(--weight-medium); letter-spacing: var(--tracking-heading); text-wrap: balance; }
.lp-contact h2 span { color: var(--color-text-tertiary); }
.lp-contact__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: var(--space-2); }
.lp-foot { display: flex; flex-wrap: wrap; gap: var(--space-2) var(--space-6); justify-content: space-between; align-items: baseline; padding-block: var(--space-5) var(--space-8); border-top: 1px solid var(--color-border-subtle); }
.lp-foot nav { display: flex; gap: var(--space-5); flex-wrap: wrap; }
"""

page = f'''<title>Serena Daswani Portfolio</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&family=Geist+Mono:wght@400;500&display=swap">
<style>
/* ===== Paper × Midnight v1.7 · tokens.css (verbatim) ===== */
{tokens}
/* ===== Paper × Midnight v1.7 · components.css (verbatim) ===== */
{comps}
{PAGE_CSS}
</style>

<div class="lp" id="top">
<header class="pm-topnav pm-topnav--floating" id="lp-nav">
  <div class="pm-topnav__bar">
    <a class="pm-topnav__brand" href="#top">{NAME}</a>
    <span class="pm-topnav__sep pm-topnav__sep--brand" aria-hidden="true"></span>
    <nav class="pm-topnav__nav" aria-label="Primary">
      <ul class="pm-topnav__list">
        <li><a class="pm-topnav__item" href="#work">Work</a></li>
        <li><a class="pm-topnav__item" href="#about">About</a></li>
        <li><a class="pm-topnav__item" href="#experience">Experience</a></li>
        <li><a class="pm-topnav__item" href="#contact">Contact</a></li>
      </ul>
    </nav>
    <span class="pm-topnav__sep" aria-hidden="true"></span>
    <div class="pm-topnav__actions">
      <span class="pm-tooltip-anchor">
        <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--sm" id="lp-theme" aria-pressed="false" aria-labelledby="lp-theme-tip">{I["moon"]}</button>
        <span role="tooltip" id="lp-theme-tip" class="pm-tooltip pm-tooltip--bottom">Dark theme</span>
      </span>
    </div>
  </div>
</header>

<main>
  <div class="lp-wrap lp-hero">
    <section class="pm-hero" aria-labelledby="lp-h1">
      <h1 class="pm-hero__title" id="lp-h1"><b>Hi, I’m {NAME},</b> a product designer building calm tools for complicated work in AI and enterprise software.</h1>
      <div class="pm-hero__now"><span class="pm-mono pm-hero__now-label">Currently designing {I["arrow"]}</span>
        <span class="pm-hero__chip"><span class="pm-hero__dot" aria-hidden="true"></span>Review queue v3, in pilot</span></div>
      <div class="pm-hero__actions">{copy_btn('hero')}<a class="pm-btn pm-btn--ghost pm-btn--sm" href="#resume" data-soon>Résumé{I["ext"]}</a></div>
    </section>
  </div>

  <section class="lp-wrap lp-sec" id="work" aria-labelledby="lp-work-h">
    <div class="lp-sec__head"><h2 id="lp-work-h">Selected work</h2><span class="pm-mono">04 projects · 2022–2025</span></div>
    <ul class="pm-work-grid">{''.join(tile(*w, i) for i, w in enumerate(WORK))}</ul>
  </section>

  <section class="lp-wrap lp-sec" id="about" aria-labelledby="lp-about-h">
    <div class="lp-sec__head"><h2 id="lp-about-h">About</h2><span class="pm-mono">Product designer since 2016</span></div>
    <div class="lp-about">
      <div class="lp-about__bio">
        <p>I design the parts of software people use all day: review queues, permission models, dashboards and the systems behind them.</p>
        <p>My work sits where enterprise software, AI tooling and design systems meet. I start with the hardest real case, prototype in code when it helps, and stay with a problem through launch, because the details only show up once people use the thing.</p>
        <p>Outside work I write about design systems and editorial interfaces, and I mentor early-career designers.</p>
      </div>
      <aside class="pm-panel pm-panel--tonal lp-about__spec" aria-labelledby="lp-spec-h">
        <div class="pm-panel__header"><h3 class="pm-panel__title" id="lp-spec-h">At a glance</h3></div>
        <div class="pm-panel__body">
          <dl class="pm-meta">
            <dt>Role</dt><dd>Lead product designer</dd>
            <dt>Focus</dt><dd>AI tooling, design systems, internal platforms</dd>
            <dt>Experience</dt><dd><span class="pm-mono">10 yrs</span></dd>
            <dt>Based in</dt><dd><span class="lp-clock"><span>New York</span><span class="pm-hero__dot" aria-hidden="true"></span><span class="pm-mono" id="lp-time" aria-label="Local time">--:--</span></span></dd>
          </dl>
        </div>
      </aside>
    </div>
  </section>

  <section class="lp-wrap lp-sec" id="what" aria-labelledby="lp-what-h">
    <div class="lp-sec__head"><h2 id="lp-what-h">What I bring</h2><span class="pm-mono">Systems · AI · Research · Access</span></div>
    {BENTO}
  </section>

  <section class="lp-wrap lp-sec" id="experience" aria-labelledby="lp-exp-h">
    <div class="lp-sec__head"><h2 id="lp-exp-h">Experience</h2><span class="pm-mono">2016 – Now</span></div>
    <ol class="pm-experience" aria-labelledby="lp-exp-h">{''.join(role(*r) for r in ROLES)}</ol>
  </section>

  <section class="lp-wrap lp-contact" id="contact" aria-labelledby="lp-contact-h">
    <h2 id="lp-contact-h">Building something people have to trust? <span>Let’s talk.</span></h2>
    <div class="lp-contact__actions">{copy_btn('contact')}<a class="pm-btn pm-btn--ghost pm-btn--sm" href="#resume" data-soon>Résumé{I["ext"]}</a></div>
    <p class="pm-mono" style="margin:0">{EMAIL}</p>
  </section>
</main>

<footer class="lp-wrap">
  <div class="lp-foot">
    <p class="pm-mono" style="margin:0">© 2026 {NAME} · Built on Paper × Midnight v1.7</p>
    <nav aria-label="Elsewhere">
      <a class="pm-link pm-link--subtle" href="https://www.linkedin.com/" target="_blank" rel="noopener">LinkedIn<span class="pm-sr"> (opens in a new tab)</span></a>
      <a class="pm-link pm-link--subtle" href="#resume" data-soon>Résumé</a>
    </nav>
  </div>
</footer>
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

  // Floating nav deepens its shadow once content scrolls under it
  var nav = document.getElementById('lp-nav');
  function onScroll() {{ nav.classList.toggle('is-scrolled', (window.scrollY || document.documentElement.scrollTop) > 8); }}
  window.addEventListener('scroll', onScroll, {{ passive: true }}); onScroll();

  // Copy email (falls back to showing the address)
  var live = document.getElementById('lp-live');
  document.querySelectorAll('[data-copy]').forEach(function (b) {{
    var label = b.querySelector('span');
    b.addEventListener('click', function () {{
      var e = b.getAttribute('data-copy');
      function done(ok) {{ label.textContent = ok ? 'Copied' : e; live.textContent = ok ? 'Email address copied' : 'Copy failed. The address is ' + e; setTimeout(function () {{ label.textContent = 'Copy email'; }}, 2000); }}
      try {{ navigator.clipboard.writeText(e).then(function () {{ done(true); }}, function () {{ done(false); }}); }} catch (x) {{ done(false); }}
    }});
  }});

  // Live local time (sample: New York)
  var t = document.getElementById('lp-time');
  function tick() {{ try {{ t.textContent = new Intl.DateTimeFormat('en-GB', {{ hour: '2-digit', minute: '2-digit', timeZone: 'America/New_York' }}).format(new Date()); }} catch (e) {{ t.textContent = ''; }} }}
  tick(); setInterval(tick, 15000);

  // Links to pages that don't exist yet stay put
  document.querySelectorAll('[data-soon]').forEach(function (a) {{ a.addEventListener('click', function (e) {{ e.preventDefault(); }}); }});
}})();
</script>
'''
open(os.path.join(REPO, 'prototypes/landing.html'), 'w').write(page)
print(len(page))
