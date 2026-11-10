# Builds prototypes/review-v1.8.html: side-by-side review for (A) metadata typeface and (B) split layout.
# Usage (from the repo root):  python3 design-system/tools/previews/src/review2.py
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import I, S, IMG
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
tokens = open(os.path.join(REPO, 'design-system', 'css', 'tokens.css')).read()
comps = open(os.path.join(REPO, 'design-system', 'css', 'components.css')).read()
check = open(os.path.join(HERE, 'check.js')).read()

META_SELECTORS = ('.pm-mono, .pm-card__eyebrow, .pm-bento__eyebrow, .pm-bento__stat-label, .pm-experience__mark, .pm-experience__years, '
                  '.pm-stats__label, .pm-badge--mono, .pm-divider-label, .pm-sidenav__count, .pm-toc__num, .pm-tabs__count, .pm-field__count, '
                  '.pm-input-group__addon, .pm-frame__index, .pm-lightbox__count, .pm-video__time')
scoped = ', '.join('.v-sans ' + s.strip() for s in META_SELECTORS.split(','))

PROPOSED = r"""
/* ================= PROPOSED v1.8 · not yet in the design system ================= */
/* A. Metadata voice: Instrument Sans 13px regular, tertiary, tabular figures (one switch: --font-meta) */
""" + scoped + r""" { font-family: var(--font-sans); font-size: var(--type-label); line-height: var(--line-label); letter-spacing: 0; font-variant-numeric: tabular-nums; }
.v-sans .pm-experience__mark { font-weight: var(--weight-medium); }

/* B. Split layout: sticky intro + vertical nav on the left, work on the right */
.pm-split { display: grid; grid-template-columns: minmax(0, 1fr); min-height: 100%; }
@container (min-width: 1024px) { .pm-split { grid-template-columns: 360px minmax(0, 1fr); } }
.pm-split__aside { display: flex; flex-direction: column; gap: var(--space-6); padding: var(--space-10) var(--space-6) var(--space-6); }
@container (min-width: 1024px) {
  .pm-split__aside { position: sticky; top: 0; height: var(--pm-split-h, 100vh); padding: var(--space-12) var(--space-8) var(--space-8); border-right: 1px solid var(--color-border-subtle); overflow-y: auto; }
}
.pm-split__main { min-width: 0; padding: var(--space-6) var(--space-4) var(--space-16); }
@container (min-width: 1024px) { .pm-split__main { padding: var(--space-12) var(--space-10) var(--space-24); } }
.pm-intro { display: grid; gap: var(--space-4); }
.pm-intro__mark { width: 40px; height: 40px; border-radius: var(--radius-sm); display: grid; place-items: center; background: var(--color-bg-surface); box-shadow: inset 0 0 0 1px var(--color-border-subtle); font-size: var(--type-label); font-weight: var(--weight-medium); color: var(--color-text-secondary); }
.pm-intro__name { margin: var(--space-2) 0 0; font-size: var(--type-h2); line-height: var(--line-h2); font-weight: var(--weight-medium); letter-spacing: var(--tracking-heading); text-wrap: balance; }
.pm-intro__name span { color: var(--color-text-tertiary); }
.pm-intro__text { margin: 0; max-width: 36ch; font-size: var(--type-body-md); line-height: var(--line-body-md); color: var(--color-text-secondary); }
.pm-intro__status { display: inline-flex; align-items: center; gap: var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-primary); }
.pm-intro__actions { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.pm-split__nav { margin-top: var(--space-4); }
@container (min-width: 1024px) { .pm-split__nav { margin-top: auto; } }
.pm-sidenav__item[aria-current="location"] { color: var(--color-text-primary); font-weight: var(--weight-medium); }
.pm-sidenav__item[aria-current="location"]::before { content: ""; position: absolute; left: 0; top: var(--space-2); bottom: var(--space-2); width: 2px; border-radius: 1px; background: var(--color-selected-indicator); }
@container (max-width: 1023px) {
  .pm-split__nav .pm-sidenav__list { flex-direction: row; flex-wrap: wrap; gap: var(--space-1); }
  .pm-split__nav .pm-sidenav__item { width: auto; }
  .pm-split__nav .pm-sidenav__item[aria-current="location"]::before { left: var(--space-3); right: var(--space-3); top: auto; bottom: 0; width: auto; height: 2px; }
}
.pm-split__foot { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); flex-wrap: wrap; padding-top: var(--space-4); border-top: 1px solid var(--color-border-subtle); }
.pm-split__foot nav { display: flex; gap: var(--space-4); flex-wrap: wrap; }
.pm-split__section { scroll-margin-top: var(--space-6); }
.pm-split__section + .pm-split__section { margin-top: var(--space-20); }
.pm-split__h { margin: 0 0 var(--space-6); font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); color: var(--color-text-secondary); }
/* even two-column grid (no stagger) for the narrower split column */
.pm-work-grid--even > li:nth-child(even) { margin-top: 0 !important; }
.pm-work-grid--even { gap: var(--space-10) var(--space-6); }
/* Card --showcase: one large container per project (Dakota), copy left, screen right */
.pm-card--showcase { display: grid; grid-template-columns: minmax(0, 1fr); overflow: hidden; background: var(--color-bg-surface); border-radius: var(--radius-md); min-height: 0; }
@container (min-width: 1024px) { .pm-card--showcase { grid-template-columns: 5fr 7fr; min-height: 420px; } }
.pm-card--showcase .pm-card__copy { display: flex; flex-direction: column; gap: var(--space-2); padding: var(--space-8); align-self: end; }
.pm-card--showcase .pm-card__title { font-size: var(--type-h3); line-height: var(--line-h3); letter-spacing: var(--tracking-h3); }
.pm-card--showcase .pm-card__sub { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); max-width: 40ch; }
.pm-card--showcase .pm-card__meta { margin-top: var(--space-2); }
.pm-card--showcase .pm-card__more { margin-top: var(--space-4); display: inline-flex; align-items: center; gap: var(--space-1); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.pm-card--showcase .pm-card__shot { position: relative; align-self: end; padding: var(--space-8) 0 0 var(--space-8); }
@container (min-width: 1024px) { .pm-card--showcase .pm-card__shot { padding: var(--space-12) 0 0 0; } }
.pm-card--showcase .pm-card__shot img { display: block; width: 100%; aspect-ratio: 16 / 10; object-fit: cover; object-position: top left; border-radius: var(--radius-sm) 0 0 0; box-shadow: 0 0 0 1px var(--color-border-subtle), var(--shadow-md); }
.pm-card--showcase .pm-card__title a::after { border-radius: var(--radius-md); }
.pm-card--showcase.is-hover, .pm-card--showcase:focus-within { background: var(--color-bg-sunken); }
.pm-card--showcase.is-hover .pm-card__shot img { transform: translateY(calc(-1 * var(--space-2))); }
@media (hover: hover) { .pm-card--showcase:hover { background: var(--color-bg-sunken); } .pm-card--showcase:hover .pm-card__shot img { transform: translateY(calc(-1 * var(--space-2))); } .pm-card--showcase:hover .pm-card__more .pm-icon { transform: translateX(2px); } }
@media (prefers-reduced-motion: no-preference) { .pm-card--showcase, .pm-card--showcase .pm-card__shot img, .pm-card__more .pm-icon { transition: background-color var(--motion-duration-base) var(--motion-ease), transform var(--motion-duration-base) var(--motion-ease); } }
@media (prefers-reduced-motion: reduce) { .pm-card--showcase .pm-card__shot img { transform: none !important; } }
.pm-showcase-list { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-4); }
"""

PAGE_CSS = r"""
/* Review scaffolding. Layout: single 1200px column; compare rows; device frames scaled to fit. */
body { font-family: var(--font-sans); }
.rv { container-type: inline-size; }
.rv-wrap { max-width: var(--content-max-width); margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
@container (min-width: 768px) { .rv-wrap { padding-left: max(var(--space-6), env(safe-area-inset-left, 0px)); padding-right: max(var(--space-6), env(safe-area-inset-right, 0px)); } }
.rv-head { padding-block: var(--space-16) var(--space-10); display: grid; gap: var(--space-4); }
.rv-head h1 { margin: 0; font-size: var(--type-h1); line-height: var(--line-h1); font-weight: var(--weight-medium); letter-spacing: var(--tracking-heading); }
.rv-head p { margin: 0; max-width: 64ch; color: var(--color-text-secondary); font-size: var(--type-body-md); line-height: var(--line-body-md); }
.rv-bar { display: flex; flex-wrap: wrap; gap: var(--space-2) var(--space-6); align-items: center; justify-content: space-between; }
.rv-jump { display: flex; flex-wrap: wrap; gap: var(--space-1) var(--space-4); }
.rv-sec { padding-block: var(--space-10) var(--space-16); border-top: 1px solid var(--color-border-subtle); }
.rv-sec__head { display: grid; gap: var(--space-2); margin-bottom: var(--space-8); max-width: 72ch; }
.rv-sec__head h2 { margin: 0; font-size: var(--type-h2); line-height: var(--line-h2); font-weight: var(--weight-medium); letter-spacing: var(--tracking-heading); }
.rv-sec__head p, .rv-eyebrow { margin: 0; color: var(--color-text-secondary); font-size: var(--type-body-md); line-height: var(--line-body-md); }
.rv-eyebrow { font-size: var(--type-label); color: var(--color-text-tertiary); }
.rv-compare { display: grid; gap: var(--space-6); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 1024px) { .rv-compare { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.rv-pane { min-width: 0; display: grid; gap: var(--space-3); align-content: start; }
.rv-label { display: flex; align-items: center; gap: var(--space-2); font-size: var(--type-label); color: var(--color-text-tertiary); }
.rv-stage { border-radius: var(--radius-md); background: var(--color-bg-canvas); box-shadow: inset 0 0 0 1px var(--color-border-default); padding: var(--space-6); display: grid; gap: var(--space-8); container-type: inline-size; min-width: 0; }
.rv-spec { display: grid; gap: var(--space-2); }
.rv-spec > .rv-eyebrow { margin-bottom: var(--space-1); }
.rv-notes { display: grid; gap: var(--space-6); margin-top: var(--space-8); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .rv-notes { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.rv-notes h3 { margin: 0 0 var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); }
.rv-notes ul { margin: 0; padding-left: var(--space-4); display: grid; gap: var(--space-1); font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.rv-notes code { font-family: var(--font-mono); font-size: .857em; color: var(--color-text-primary); }
/* device frames */
.rv-devices { display: grid; gap: var(--space-10); }
.rv-device-wrap { display: grid; gap: var(--space-3); }
.rv-device-wrap > div:first-child { display: flex; justify-content: space-between; gap: var(--space-4); flex-wrap: wrap; align-items: baseline; }
.rv-viewport { position: relative; width: 100%; overflow: hidden; border-radius: var(--radius-md); box-shadow: inset 0 0 0 1px var(--color-border-default), var(--shadow-sm); background: var(--color-bg-canvas); }
.rv-device { position: absolute; top: 0; left: 0; transform-origin: top left; overflow-y: auto; overscroll-behavior: contain; container-type: inline-size; background: var(--color-bg-canvas); }
.rv-phones { display: grid; gap: var(--space-6); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .rv-phones { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.rv-table-wrap { overflow-x: auto; border-radius: var(--radius-md); box-shadow: inset 0 0 0 1px var(--color-border-subtle); }
.rv-table { width: 100%; border-collapse: collapse; min-width: 640px; font-size: var(--type-body-sm); line-height: var(--line-body-sm); }
.rv-table th, .rv-table td { text-align: left; padding: var(--space-3) var(--space-4); border-bottom: 1px solid var(--color-border-subtle); vertical-align: top; }
.rv-table th { font-weight: var(--weight-medium); color: var(--color-text-tertiary); font-size: var(--type-label); }
.rv-table tr:last-child td { border-bottom: 0; }
.rv-table code { font-family: var(--font-mono); font-size: .857em; }
.pm-ratio { font-size: var(--type-label); color: var(--color-text-secondary); } .pm-pass::before { content: "✓ "; } .pm-fail { color: var(--color-state-error); font-size: var(--type-label); } .pm-fail::before { content: "✕ "; }
.rv-a11y { display: flex; flex-wrap: wrap; gap: var(--space-1) var(--space-4); }
"""

# ---------- content (real where it exists) ----------
PROJ = [('form', 'Mensio Data Explorer', 'Redesigning the data explorer for self-serve analysis', 'Product design · Analytics', '2026', True),
        ('queue', 'Review queue', 'Placeholder project', 'Product design · AI tooling', '2025', False),
        ('grid', 'Token system', 'Placeholder project', 'Design systems · Web', '2024', False),
        ('chart', 'Dashboards', 'Placeholder project', 'Product design · Data viz', '2024', False)]

def tile(p, i):
    k, t, s, sub, y, real = p
    return (f'<li><article class="pm-card pm-card--tile"><div class="pm-card__stage"><img src="{IMG[k]}" alt="" loading="lazy">'
            f'<span class="pm-card__go" aria-hidden="true">{I["arrow"]}</span></div>'
            f'<div class="pm-card__row"><h3 class="pm-card__title"><a href="#w">{t}</a></h3><span class="pm-mono">{y}</span></div>'
            f'<p class="pm-card__sub">{sub}</p></article></li>')

def showcase(p, i):
    k, t, s, sub, y, real = p
    return (f'<li><article class="pm-card pm-card--showcase"><div class="pm-card__copy">'
            f'<p class="pm-card__eyebrow">{y} · {sub.split(" · ")[1]}</p>'
            f'<h3 class="pm-card__title"><a href="#w">{t if not real else "Redesigning Mensio’s Data Explorer for self-serve analysis"}</a></h3>'
            + (f'<p class="pm-card__sub">{s}</p>' if not real else '<p class="pm-card__sub">Shipped 2026.</p>') +
            f'<ul class="pm-card__meta" aria-label="Disciplines"><li class="pm-badge">{sub.split(" · ")[0]}</li><li class="pm-badge">{sub.split(" · ")[1]}</li></ul>'
            f'<span class="pm-card__more" aria-hidden="true">Read case study{I["arrow"]}</span></div>'
            f'<div class="pm-card__shot"><img src="{IMG[k]}" alt="" loading="lazy"></div></article></li>')

EXP = [('D', 'Deploy', 'Product designer', 'Now', True), ('A', 'Apple', 'Product designer', '', False), ('P', 'Procense', 'Product designer', '', False), ('O', 'OmniSynkAI', 'Design intern', '', False)]
def exp_list():
    rows = ''
    for m, org, role, yrs, now in EXP:
        dot = '<span class="pm-hero__dot" aria-hidden="true"></span>' if now else ''
        rows += (f'<li class="pm-experience__item"><span class="pm-experience__mark" aria-hidden="true">{m}</span><div class="pm-experience__head"><h3 class="pm-experience__org">{org}</h3>'
                 f'<span class="pm-experience__role">{role}</span></div><span class="pm-experience__years">{dot}{yrs or "Years TBC"}</span></li>')
    return f'<ol class="pm-experience">{rows}</ol>'

def split_page(variant, uid):
    nav = ''.join(f'<li><a class="pm-sidenav__item" href="#{uid}-{s.lower()}"{" aria-current=\"location\"" if j == 0 else ""} data-spy>{s}</a></li>'
                  for j, s in enumerate(['Work', 'About', 'Experience', 'Contact']))
    work = (f'<ul class="pm-work-grid pm-work-grid--even">{"".join(tile(p, i) for i, p in enumerate(PROJ))}</ul>' if variant == 'grid'
            else f'<ul class="pm-showcase-list">{"".join(showcase(p, i) for i, p in enumerate(PROJ))}</ul>')
    return f'''<div class="pm-split v-sans">
  <aside class="pm-split__aside" aria-label="Introduction">
    <div class="pm-intro">
      <span class="pm-intro__mark" aria-hidden="true">SD</span>
      <h2 class="pm-intro__name">Serena Daswani <span>is a product designer who builds for fun.</span></h2>
      <p class="pm-intro__text">Designing calm tools for complicated work. Currently at Deploy; previously Apple and Procense.</p>
      <span class="pm-intro__status"><span class="pm-hero__dot" aria-hidden="true"></span>Designing at Deploy</span>
      <div class="pm-intro__actions"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-copy>{I["copy"]}<span>Copy email</span></button><a class="pm-btn pm-btn--ghost pm-btn--sm" href="#w">Résumé{I["ext"]}</a></div>
    </div>
    <nav class="pm-sidenav pm-split__nav" aria-label="Sections ({variant})"><ul class="pm-sidenav__list">{nav}</ul></nav>
    <div class="pm-split__foot"><nav aria-label="Elsewhere ({variant})"><a class="pm-link pm-link--subtle" href="#w">LinkedIn</a><a class="pm-link pm-link--subtle" href="#w">GitHub</a></nav><span class="pm-mono" data-clock>--:-- PT</span></div>
  </aside>
  <main class="pm-split__main">
    <section class="pm-split__section" id="{uid}-work" aria-label="Work"><h2 class="pm-split__h">Selected work</h2>{work}</section>
    <section class="pm-split__section" id="{uid}-about" aria-label="About"><h2 class="pm-split__h">About</h2><p class="pm-intro__text" style="max-width:60ch">A short first-person bio goes here: how you work, what you care about, one personal detail.</p></section>
    <section class="pm-split__section" id="{uid}-experience" aria-label="Experience"><h2 class="pm-split__h">Experience</h2>{exp_list()}</section>
    <section class="pm-split__section" id="{uid}-contact" aria-label="Contact" style="padding-bottom:40vh"><h2 class="pm-split__h">Contact</h2><p class="pm-intro__text">Closing line and Copy email.</p></section>
  </main>
</div>'''

def device(label, sub, inner, w, h, uid):
    return (f'<div class="rv-device-wrap"><div><span class="rv-label">{label}</span><span class="rv-eyebrow">{sub}</span></div>'
            f'<div class="rv-viewport" data-w="{w}" data-h="{h}"><div class="rv-device" style="width:{w}px;height:{h}px;--pm-split-h:{h}px" tabindex="0" aria-label="{label}, scrollable preview" id="{uid}">{inner}</div></div></div>')

def badge(kind, text):
    return f'<span class="pm-badge{" pm-badge--accent" if kind == "prop" else ""}">{text}</span>'

# ---------- A. metadata comparison ----------
def meta_block():
    return (f'<div class="rv-spec"><span class="rv-eyebrow">Work card</span><ul class="pm-work-grid" style="grid-template-columns:minmax(0,1fr)">{tile(PROJ[0], 0)}</ul></div>'
            f'<div class="rv-spec"><span class="rv-eyebrow">Hero chip label</span><div class="pm-hero__now" style="justify-items:start"><span class="pm-mono pm-hero__now-label">Currently designing {I["arrow"]}</span><span class="pm-hero__chip"><span class="pm-hero__dot" aria-hidden="true"></span>Data explorer, at Deploy</span></div></div>'
            f'<div class="rv-spec"><span class="rv-eyebrow">Spec sheet + stats</span><dl class="pm-meta"><dt>Role</dt><dd>Product designer</dd><dt>Since</dt><dd><span class="pm-mono">2022</span></dd><dt>Local time</dt><dd><span class="pm-mono" data-clock>--:-- PT</span></dd></dl>'
            '<dl class="pm-stats pm-stats--sm"><div class="pm-stats__item"><dt class="pm-stats__label">tables unified</dt><dd class="pm-stats__value">11 → 1</dd></div><div class="pm-stats__item"><dt class="pm-stats__label">teams onboarded</dt><dd class="pm-stats__value">4</dd></div></dl></div>'
            f'<div class="rv-spec"><span class="rv-eyebrow">Experience row</span>{exp_list()}</div>')

def notes(what, why, a11y):
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    return f'<div class="rv-notes"><div><h3>What changes</h3><ul>{li(what)}</ul></div><div><h3>Why</h3><ul>{li(why)}</ul></div><div><h3>Accessibility and tokens</h3><ul>{li(a11y)}</ul></div></div>'

ROWS = [('A', 'Metadata in Instrument Sans', 'Token + type role', 'New <code>--font-meta</code> role = Instrument Sans 13px regular, tertiary, tabular. 20 selectors switch from <code>--font-mono</code>. Geist Mono is dropped from the site.'),
        ('B', 'Split layout <code>pm-split</code>', 'New page layout', '360px sticky left column (intro, status, actions, vertical nav, socials, clock) + right content column. Stacks below 1024px.'),
        ('B1', 'Two-per-row tiles', 'Variant of Card <code>--tile</code> grid', '<code>pm-work-grid--even</code>: no stagger in the narrower right column.'),
        ('B2', 'Card <code>--showcase</code>', 'New card variant', 'One large container per project: copy bottom-left, screen right, whole-card hover.'),
        ('B3', 'Scroll-spy in the vertical nav', 'Behaviour', 'The current section is marked with weight + a cobalt tick (<code>aria-current="location"</code>). In a side nav, location is useful, unlike the floating top nav.')]
TABLE = ('<div class="rv-table-wrap"><table class="rv-table"><thead><tr><th>#</th><th>Change</th><th>Type</th><th>What it does</th></tr></thead><tbody>' +
         ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in ROWS) + '</tbody></table></div>')

page = f'''<title>Portfolio Layout Review</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&family=Geist+Mono:wght@400;500&display=swap">
<style>
{tokens}
{comps}
{PROPOSED}
{PAGE_CSS}
</style>
<div class="rv">
<header class="rv-wrap rv-head">
  <p class="rv-eyebrow">Paper × Midnight v1.7 → v1.8 · review</p>
  <h1>Metadata type and split layout</h1>
  <p>Two proposals, shown live with the real system CSS. Nothing here is in the design system yet. Content uses your real details where they exist (Mensio, Deploy, Apple, Procense, OmniSynkAI, Pacific time); everything marked “Placeholder” is a stand-in.</p>
  <div class="rv-bar"><nav class="rv-jump" aria-label="Proposals"><a class="pm-link" href="#rv-a">A · Metadata type</a><a class="pm-link" href="#rv-b">B · Split layout</a><a class="pm-link" href="#rv-sum">Summary</a></nav>
  <button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-theme-toggle aria-pressed="false">{I["moon"]}<span>Compare in dark</span></button></div>
</header>

<section class="rv-wrap rv-sec" id="rv-a" aria-labelledby="rv-a-h">
  <div class="rv-sec__head"><p class="rv-eyebrow">A · Metadata type</p><h2 id="rv-a-h">Drop the code font</h2>
  <p>Years, labels, counts and times move from Geist Mono into Instrument Sans: smaller and lighter rather than a different typeface, the way itti, Leah and Dakota do it.</p></div>
  <div class="rv-compare">
    <div class="rv-pane"><span class="rv-label">{badge("cur", "Current")} Geist Mono 12px</span><div class="rv-stage">{meta_block()}</div></div>
    <div class="rv-pane"><span class="rv-label">{badge("prop", "Proposed")} Instrument Sans 13px, tertiary, tabular</span><div class="rv-stage v-sans">{meta_block()}</div></div>
  </div>
  {notes(['One new role, <code>--font-meta</code>, set to Instrument Sans. The 20 metadata selectors point at it instead of <code>--font-mono</code>.',
          'Size goes from 12px to 13px (<code>type-label</code>) at weight 400 in <code>color-text-tertiary</code>. Tabular figures keep years and times aligned.',
          'Geist Mono stops loading on the site: one fewer font file, faster first paint.'],
         ['Hierarchy now comes from size, weight and grey within one family. That reads as quieter and more modern than switching typeface.',
          'Matches every reference you picked. None of them sets metadata in a code font.',
          'Keeps a single path to bring a mono back later (one token) if you ever want it for a specific detail.'],
         ['Tertiary text stays at ≥4.67:1 (light) and ≥6.49:1 (dark), and 13px is more legible than 12px.',
          'The type-role rule in <code>CLAUDE.md</code> changes to: names 500 · reading 400 · metadata 13px 400 tertiary, all Instrument Sans.',
          'Tokens: new <code>typography.fontFamily.meta</code>; <code>--font-mono</code> kept for code samples only.'])}
  <div class="rv-a11y">{''.join(f'<span class="rv-eyebrow">{l} <span data-fg="{f}" data-bg="{b}" data-min="4.5"></span></span>' for l, f, b in [('metadata on canvas', '--color-text-tertiary', '--color-bg-canvas'), ('on surface', '--color-text-tertiary', '--color-bg-surface'), ('on elevated', '--color-text-tertiary', '--color-bg-elevated')])}</div>
</section>

<section class="rv-wrap rv-sec" id="rv-b" aria-labelledby="rv-b-h">
  <div class="rv-sec__head"><p class="rv-eyebrow">B · Split layout (Megan Yap + Dakota Sumner)</p><h2 id="rv-b-h">Intro and nav on the left, work on the right</h2>
  <p>Both frames are live: scroll inside them. The left column stays put, and the vertical nav marks the section you’re in. Both use the proposed metadata type from A.</p></div>
  <div class="rv-devices">
    {device("B1 · Two per row", "Card --tile in an even two-column grid", split_page("grid", "g"), 1280, 800, "dev-g")}
    {device("B2 · One large container per project", "New Card --showcase, Dakota-style", split_page("showcase", "s"), 1280, 800, "dev-s")}
    <div class="rv-phones">
      {device("Phone · B1", "Below 1024px the left column becomes the top intro; nav turns into a row", split_page("grid", "gm"), 390, 760, "dev-gm")}
      {device("Phone · B2", "Showcase cards stack: copy, then screen", split_page("showcase", "sm"), 390, 760, "dev-sm")}
    </div>
  </div>
  {notes(['New page layout <code>pm-split</code>: a 360px sticky left column (mark, name as the headline, one-line intro, status, Copy email + Résumé, vertical nav pinned to the bottom, socials + Pacific clock) and a right column for content.',
          'The vertical nav reuses SideNavigation. Scroll-spy marks the current section with weight + the cobalt tick (<code>aria-current="location"</code>).',
          'B1 keeps Card <code>--tile</code> in an even (unstaggered) grid. B2 adds Card <code>--showcase</code>: one large neutral container per project, copy bottom-left, screen rising on the right, whole-card hover.'],
         ['The intro and nav stay visible the whole time, so the page reads like a calm app shell (Megan) while the work gets the wide column (Dakota).',
          'B1 shows more projects at once, and suits having 4+ projects of similar weight.',
          'B2 gives each project a moment, and suits 2–4 strong projects (you have Mensio plus the ones you’ll add).'],
         ['Below 1024px nothing is sticky: the intro comes first, then the nav as a wrapping row, then the content. There’s no hidden menu.',
          'Scroll-spy only updates <code>aria-current</code>; the links are plain anchors, so it works without JS.',
          'Tokens: <code>space-6/8/10/12</code>, <code>color-border-subtle</code> divider, <code>color-bg-surface/sunken</code> for showcase, <code>shadow-md</code> on screens, <code>radius-md</code> containers.'])}
</section>

<section class="rv-wrap rv-sec" id="rv-sum" aria-labelledby="rv-sum-h">
  <div class="rv-sec__head"><p class="rv-eyebrow">Summary</p><h2 id="rv-sum-h">Decide</h2>
  <p>Approve A on its own, and pick B1 or B2 (or both: B2 for featured work, B1 for the rest). I’ll then put them into the system with guidelines, rebuild the landing page, and republish.</p></div>
  {TABLE}
</section>
</div>

<script>
{check}
(function () {{
  var root = document.documentElement;
  function isDark() {{ var t = root.getAttribute('data-theme'); return t ? t === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; }}
  function sync() {{ document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {{ b.setAttribute('aria-pressed', String(isDark())); var s = b.querySelector('span'); if (s) s.textContent = isDark() ? 'Compare in light' : 'Compare in dark'; }}); if (window.pmCheck) pmCheck(); }}
  document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {{ b.addEventListener('click', function () {{ root.setAttribute('data-theme', isDark() ? 'light' : 'dark'); sync(); }}); }});
  sync();
  // scale device frames to fit
  function fit() {{ document.querySelectorAll('.rv-viewport').forEach(function (v) {{ var w = +v.dataset.w, h = +v.dataset.h, s = Math.min(1, v.clientWidth / w); var d = v.firstElementChild; d.style.transform = 'scale(' + s + ')'; v.style.height = (h * s) + 'px'; }}); }}
  fit(); window.addEventListener('resize', fit);
  // scroll-spy inside each frame
  document.querySelectorAll('.rv-device').forEach(function (dev) {{
    var links = [].slice.call(dev.querySelectorAll('[data-spy]'));
    function spy() {{ var top = dev.scrollTop + 120, cur = links[0]; links.forEach(function (a) {{ var s = dev.querySelector(a.getAttribute('href')); if (s && s.offsetTop <= top) cur = a; }}); links.forEach(function (a) {{ if (a === cur) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); }}); }}
    dev.addEventListener('scroll', spy, {{ passive: true }});
    links.forEach(function (a) {{ a.addEventListener('click', function (e) {{ e.preventDefault(); var s = dev.querySelector(a.getAttribute('href')); dev.scrollTo({{ top: s.offsetTop - 24, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }}); }}); }});
  }});
  // Pacific clock
  function tick() {{ var t = ''; try {{ t = new Intl.DateTimeFormat('en-US', {{ hour: 'numeric', minute: '2-digit', timeZone: 'America/Los_Angeles' }}).format(new Date()) + ' PT'; }} catch (e) {{}} document.querySelectorAll('[data-clock]').forEach(function (c) {{ c.textContent = t; }}); }}
  tick(); setInterval(tick, 15000);
  document.querySelectorAll('[data-copy]').forEach(function (b) {{ b.addEventListener('click', function () {{ var l = b.querySelector('span'); l.textContent = 'Email TBC'; setTimeout(function () {{ l.textContent = 'Copy email'; }}, 1500); }}); }});
  document.querySelectorAll('a[href="#w"]').forEach(function (a) {{ a.addEventListener('click', function (e) {{ e.preventDefault(); }}); }});
}})();
</script>
'''
out = os.path.join(REPO, 'prototypes', 'review-v1.8.html')
open(out, 'w').write(page)
print('wrote', out, len(page))
