import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import I, S, IMG
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
tokens = open(os.path.join(REPO, 'design-system', 'css', 'tokens.css')).read()
comps = open(os.path.join(REPO, 'design-system', 'css', 'components.css')).read()
check = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check.js')).read()

PROPOSED_CSS = r"""
/* ================= PROPOSED · not yet in the design system ================= */
/* 1. TopNavigation --floating: centred, sticky, floating bar. No current-page indicator. */
.pm-topnav--floating { position: sticky; top: calc(var(--space-3) + env(safe-area-inset-top, 0px)); z-index: 20; background: transparent; border-bottom: 0; padding-inline: var(--space-4); pointer-events: none; }
.pm-topnav--floating .pm-topnav__bar { pointer-events: auto; width: max-content; max-width: 100%; min-height: 48px; margin: 0 auto; padding: 0 var(--space-1) 0 var(--space-4); gap: var(--space-1); align-items: center; background: var(--color-bg-elevated); border-radius: var(--radius-md); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); }
.pm-topnav--floating.is-scrolled .pm-topnav__bar { box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-md); }
.pm-topnav--floating .pm-topnav__brand { margin-right: var(--space-2); font-size: var(--type-body-sm); }
.pm-topnav--floating .pm-topnav__nav { display: flex; }
.pm-topnav--floating .pm-topnav__list { margin: 0; gap: 2px; align-items: center; }
.pm-topnav--floating .pm-topnav__item { min-height: var(--control-height-sm); padding: 0 var(--space-3); border-radius: var(--radius-sm); box-shadow: none; }
.pm-topnav--floating .pm-topnav__item.is-hover { color: var(--color-text-primary); background: var(--color-bg-surface); box-shadow: none; }
@media (hover: hover) { .pm-topnav--floating .pm-topnav__item:hover { color: var(--color-text-primary); background: var(--color-bg-surface); box-shadow: none; } }
.pm-topnav__sep { width: 1px; height: 16px; margin: 0 var(--space-1); background: var(--color-border-subtle); flex: none; }
@media (prefers-reduced-motion: no-preference) { .pm-topnav--floating .pm-topnav__bar { transition: box-shadow var(--motion-duration-base) var(--motion-ease); } }
@container (max-width: 767px) {
  .pm-topnav--floating .pm-topnav__bar { flex-wrap: nowrap; padding-left: var(--space-1); }
  .pm-topnav--floating .pm-topnav__nav { display: flex; order: 0; flex-basis: auto; padding: 0; border: 0; }
  .pm-topnav--floating .pm-topnav__list { flex-direction: row; }
  .pm-topnav--floating .pm-topnav__brand, .pm-topnav--floating .pm-topnav__sep--brand { display: none; }
  .pm-topnav--floating .pm-topnav__item { width: auto; padding: 0 var(--space-2); box-shadow: none; }
  .pm-topnav--floating .pm-topnav__actions { order: 0; }
}

/* 2. Hero: centred, sentence-sized, with a "currently" chip and two quiet actions */
.pm-hero { display: grid; justify-items: center; text-align: center; gap: var(--space-6); padding-block: var(--space-20) var(--space-16); }
.pm-hero__title { margin: 0; max-width: 30ch; font-size: var(--type-h3); line-height: var(--line-h3); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h3); color: var(--color-text-secondary); text-wrap: balance; }
.pm-hero__title b { font-weight: var(--weight-medium); color: var(--color-text-primary); }
.pm-hero__now { display: grid; justify-items: center; gap: var(--space-2); }
.pm-hero__now-label { display: inline-flex; align-items: center; gap: var(--space-1); }
.pm-hero__now-label .pm-icon { width: 12px; height: 12px; }
.pm-hero__chip { display: inline-flex; align-items: center; gap: var(--space-2); min-height: 28px; padding: 0 var(--space-3); border-radius: var(--radius-sm); background: var(--color-bg-elevated); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); font-size: var(--type-label); line-height: var(--line-label); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.pm-hero__dot { width: 6px; height: 6px; border-radius: 50%; background: var(--color-state-success); }
@media (prefers-reduced-motion: no-preference) { .pm-hero__dot { animation: pm-pulse 2.4s var(--motion-ease) infinite; } }
@keyframes pm-pulse { 50% { opacity: .35; } }
.pm-hero__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: var(--space-2); }

/* 3. Card --tile: neutral stage, artwork rising from the bottom edge, whole-card hover */
.pm-card--tile .pm-card__stage { position: relative; aspect-ratio: 4 / 3; max-width: 100%; margin-bottom: var(--space-4); background: var(--color-bg-surface); border-radius: var(--radius-md); overflow: hidden; }
.pm-card--tile .pm-card__stage > img { position: absolute; left: var(--space-8); top: var(--space-12); width: calc(100% - 2 * var(--space-8)); max-width: none; aspect-ratio: 4 / 3; object-fit: cover; object-position: top left; border-radius: var(--radius-sm) var(--radius-sm) 0 0; box-shadow: 0 0 0 1px var(--color-border-subtle), var(--shadow-md); }
.pm-card__go { position: absolute; top: var(--space-3); right: var(--space-3); display: grid; place-items: center; width: var(--control-height-sm); height: var(--control-height-sm); border-radius: var(--radius-sm); background: var(--color-bg-elevated); color: var(--color-text-primary); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); opacity: 0; }
.pm-card__row { display: flex; align-items: baseline; justify-content: space-between; gap: var(--space-4); }
.pm-card--tile .pm-card__title { font-size: var(--type-body-lg); line-height: var(--line-body-lg); letter-spacing: 0; }
.pm-card--tile .pm-card__sub { margin: var(--space-1) 0 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.pm-card--tile.is-hover .pm-card__stage, .pm-card--tile:focus-within .pm-card__stage { background: var(--color-bg-sunken); }
.pm-card--tile.is-hover .pm-card__go, .pm-card--tile:focus-within .pm-card__go { opacity: 1; }
.pm-card--tile.is-hover .pm-card__stage > img { transform: translateY(calc(-1 * var(--space-2))); }
.pm-card--tile .pm-card__title a { text-decoration: none !important; }
@media (hover: hover) {
  .pm-card--tile:hover .pm-card__stage { background: var(--color-bg-sunken); }
  .pm-card--tile:hover .pm-card__go { opacity: 1; }
  .pm-card--tile:hover .pm-card__stage > img { transform: translateY(calc(-1 * var(--space-2))); }
}
.pm-card--tile:active .pm-card__stage > img { transform: translateY(0); }
@media (prefers-reduced-motion: no-preference) { .pm-card--tile .pm-card__stage, .pm-card--tile .pm-card__stage > img, .pm-card__go { transition: background-color var(--motion-duration-base) var(--motion-ease), transform var(--motion-duration-base) var(--motion-ease), opacity var(--motion-duration-base) var(--motion-ease); } }
@media (prefers-reduced-motion: reduce) { .pm-card--tile .pm-card__stage > img { transform: none !important; } }
/* staggered two-column work grid */
.pm-work-grid { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-12) var(--space-6); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .pm-work-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } .pm-work-grid > li:nth-child(even) { margin-top: var(--space-24); } }
"""

PAGE_CSS = r"""
/* Review page scaffolding (not part of the system).
   Layout: a single 1200px column; each proposal is a compare row (current | proposed) above its rationale. */
body { font-family: var(--font-sans); }
.rv { container-type: inline-size; }
.rv-wrap { max-width: var(--content-max-width); margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
@container (min-width: 768px) { .rv-wrap { padding-left: max(var(--space-6), env(safe-area-inset-left, 0px)); padding-right: max(var(--space-6), env(safe-area-inset-right, 0px)); } }
.rv-head { padding-block: var(--space-16) var(--space-10); display: grid; gap: var(--space-4); }
.rv-head h1 { margin: 0; font-size: var(--type-h1); line-height: var(--line-h1); font-weight: var(--weight-medium); letter-spacing: var(--tracking-heading); }
.rv-head p { margin: 0; max-width: 62ch; color: var(--color-text-secondary); font-size: var(--type-body-md); line-height: var(--line-body-md); }
.rv-head__bar { display: flex; flex-wrap: wrap; gap: var(--space-2) var(--space-6); align-items: center; justify-content: space-between; margin-top: var(--space-2); }
.rv-jump { display: flex; flex-wrap: wrap; gap: var(--space-1) var(--space-4); }
.rv-sec { padding-block: var(--space-10) var(--space-16); border-top: 1px solid var(--color-border-subtle); scroll-margin-top: var(--space-6); }
.rv-sec__head { display: grid; gap: var(--space-2); margin-bottom: var(--space-8); max-width: 72ch; }
.rv-sec__head h2 { margin: 0; font-size: var(--type-h2); line-height: var(--line-h2); font-weight: var(--weight-medium); letter-spacing: var(--tracking-heading); }
.rv-sec__head p { margin: 0; color: var(--color-text-secondary); font-size: var(--type-body-md); line-height: var(--line-body-md); }
.rv-compare { display: grid; gap: var(--space-6); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 1024px) { .rv-compare { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.rv-pane { min-width: 0; display: grid; gap: var(--space-3); align-content: start; }
.rv-pane__label { display: flex; align-items: center; gap: var(--space-2); }
.rv-stage { position: relative; min-width: 0; border-radius: var(--radius-md); background: var(--color-bg-canvas); box-shadow: inset 0 0 0 1px var(--color-border-default); overflow: hidden; container-type: inline-size; }
.rv-stage--pad { padding: var(--space-6); }
.rv-scroll { height: 360px; overflow-y: auto; overscroll-behavior: contain; }
.rv-filler { display: grid; gap: var(--space-3); padding: var(--space-10) var(--space-6) var(--space-16); }
.rv-filler span { display: block; height: 12px; border-radius: var(--radius-sm); background: var(--color-bg-sunken); }
.rv-notes { display: grid; gap: var(--space-6); margin-top: var(--space-8); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .rv-notes { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.rv-notes h3 { margin: 0 0 var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); }
.rv-notes ul { margin: 0; padding-left: var(--space-4); display: grid; gap: var(--space-1); font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.rv-notes code, .rv-table code { font-family: var(--font-mono); font-size: 0.857em; color: var(--color-text-primary); }
/* current hero (from the landing page) */
.cur-hero { padding: var(--space-10) var(--space-6); display: grid; gap: var(--space-6); }
.cur-hero h1 { margin: 0; font-size: var(--type-display-lg); line-height: var(--line-display-lg); font-weight: var(--weight-medium); letter-spacing: var(--tracking-display); font-stretch: var(--font-width-display); text-wrap: balance; max-width: 14ch; }
.cur-hero h1 span { color: var(--color-text-tertiary); }
.cur-hero p { margin: 0; color: var(--color-text-secondary); max-width: 44ch; font-size: var(--type-body-md); line-height: var(--line-body-md); }
.cur-hero__actions { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.rv-cards { display: grid; gap: var(--space-6); grid-template-columns: repeat(2, minmax(0, 1fr)); }
@container (max-width: 440px) { .rv-cards { grid-template-columns: minmax(0, 1fr); } }
/* flow schematics */
.rv-flows { display: grid; gap: var(--space-10); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 1024px) { .rv-flows { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.rv-flow h3 { margin: 0 0 var(--space-1); font-size: var(--type-h4); line-height: var(--line-h4); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h4); }
.rv-flow > p { margin: 0 0 var(--space-5); color: var(--color-text-secondary); font-size: var(--type-body-sm); line-height: var(--line-body-sm); }
.rv-steps { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-2); counter-reset: step; }
.rv-step { counter-increment: step; display: grid; grid-template-columns: 28px minmax(0, 1fr); gap: var(--space-1) var(--space-3); align-items: baseline; padding: var(--space-3) var(--space-4); background: var(--color-bg-elevated); border-radius: var(--radius-md); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); }
.rv-step::before { content: counter(step, decimal-leading-zero); font-family: var(--font-mono); font-size: var(--type-caption); color: var(--color-text-tertiary); }
.rv-step__top { display: flex; align-items: center; justify-content: space-between; gap: var(--space-3); min-width: 0; }
.rv-step__top b { font-weight: var(--weight-medium); font-size: var(--type-body-sm); line-height: var(--line-body-sm); }
.rv-step__desc { grid-column: 2; font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-secondary); }
.rv-step--split { background: var(--color-bg-surface); box-shadow: none; }
.rv-table-wrap { overflow-x: auto; border-radius: var(--radius-md); box-shadow: inset 0 0 0 1px var(--color-border-subtle); }
.rv-table { width: 100%; border-collapse: collapse; font-size: var(--type-body-sm); line-height: var(--line-body-sm); min-width: 640px; }
.rv-table th, .rv-table td { text-align: left; padding: var(--space-3) var(--space-4); border-bottom: 1px solid var(--color-border-subtle); vertical-align: top; }
.rv-table th { font-weight: var(--weight-medium); color: var(--color-text-tertiary); font-size: var(--type-label); }
.rv-table tr:last-child td { border-bottom: 0; }
.rv-table td:first-child { font-family: var(--font-mono); font-size: var(--type-caption); color: var(--color-text-tertiary); white-space: nowrap; }
.rv-a11y { display: flex; flex-wrap: wrap; gap: var(--space-1) var(--space-4); margin-top: var(--space-4); }
.pm-ratio { font-family: var(--font-mono); font-size: var(--type-caption); color: var(--color-text-secondary); }
.pm-pass::before { content: "✓ "; } .pm-fail { font-family: var(--font-mono); font-size: var(--type-caption); color: var(--color-state-error); } .pm-fail::before { content: "✕ "; }
"""

def badge(kind, text):
    cls = {'cur': 'pm-badge', 'prop': 'pm-badge pm-badge--accent', 'new': 'pm-badge pm-badge--info', 'var': 'pm-badge pm-badge--accent', 'keep': 'pm-badge'}[kind]
    return f'<span class="{cls}">{text}</span>'

def notes(what, why, a11y):
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    return f'<div class="rv-notes"><div><h3>What changes</h3><ul>{li(what)}</ul></div><div><h3>Why</h3><ul>{li(why)}</ul></div><div><h3>Accessibility and tokens</h3><ul>{li(a11y)}</ul></div></div>'

def pane(label_badge, label, body):
    return f'<div class="rv-pane"><div class="rv-pane__label">{label_badge}<span class="pm-mono">{label}</span></div>{body}</div>'

# ---------- 1. Nav ----------
CUR_NAV = (f'<div class="rv-stage">'
  '<header class="pm-topnav" data-open="false"><div class="pm-topnav__bar">'
  '<a class="pm-topnav__brand" href="#rv-nav">Your Name</a>'
  '<nav class="pm-topnav__nav" aria-label="Current navigation example"><ul class="pm-topnav__list">'
  '<li><a class="pm-topnav__item" href="#rv-nav" aria-current="page">Work</a></li><li><a class="pm-topnav__item" href="#rv-nav">About</a></li><li><a class="pm-topnav__item" href="#rv-nav">Writing</a></li></ul></nav>'
  f'<div class="pm-topnav__actions"><a class="pm-btn pm-btn--secondary pm-btn--sm pm-topnav__desktop-only" href="#rv-nav">Résumé</a></div>'
  f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-topnav__menu" aria-label="Menu" aria-expanded="false">{I["menu"]}</button>'
  '</div></header><div class="rv-filler" aria-hidden="true">' + '<span style="width:70%"></span><span style="width:90%"></span><span style="width:55%"></span>' * 2 + '</div></div>')
PROP_NAV = ('<div class="rv-stage rv-scroll" id="rv-navdemo" tabindex="0" aria-label="Scrollable preview of the floating navigation">'
  '<header class="pm-topnav pm-topnav--floating" id="rv-floating"><div class="pm-topnav__bar">'
  '<a class="pm-topnav__brand" href="#rv-nav">Your Name</a><span class="pm-topnav__sep pm-topnav__sep--brand" aria-hidden="true"></span>'
  '<nav class="pm-topnav__nav" aria-label="Proposed navigation example"><ul class="pm-topnav__list">'
  '<li><a class="pm-topnav__item" href="#rv-nav">Work</a></li><li><a class="pm-topnav__item is-hover" href="#rv-nav">About</a></li><li><a class="pm-topnav__item" href="#rv-nav">Experience</a></li><li><a class="pm-topnav__item" href="#rv-nav">Contact</a></li></ul></nav>'
  '<span class="pm-topnav__sep" aria-hidden="true"></span>'
  f'<div class="pm-topnav__actions"><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--sm" aria-label="Dark theme" aria-pressed="false" data-theme-toggle>{I["moon"]}</button></div>'
  '</div></header><div class="rv-filler" aria-hidden="true">' + '<span style="width:70%"></span><span style="width:90%"></span><span style="width:55%"></span><span style="width:80%"></span>' * 5 + '</div></div>')

# ---------- 2. Hero ----------
CUR_HERO = ('<div class="rv-stage"><div class="cur-hero">'
  f'<span class="pm-status pm-status--success">{S["success"]}<span class="pm-status__text"><span class="pm-status__label">Open to senior and staff roles</span></span></span>'
  '<h1>I design calm tools for <span>complicated work.</span></h1>'
  '<p>I’m a product designer working where enterprise software, AI tooling and design systems meet.</p>'
  f'<div class="cur-hero__actions"><a class="pm-btn pm-btn--primary" href="#rv-hero">View selected work{I["arrow"]}</a><a class="pm-btn pm-btn--secondary" href="#rv-hero">Get in touch</a></div>'
  '</div></div>')
PROP_HERO = ('<div class="rv-stage"><section class="pm-hero" aria-labelledby="rv-hero-h">'
  '<h2 class="pm-hero__title" id="rv-hero-h"><b>Hi, I’m Your Name,</b> a product designer building calm tools for complicated work in AI and enterprise software.</h2>'
  f'<div class="pm-hero__now"><span class="pm-mono pm-hero__now-label">Currently designing {I["arrow"]}</span>'
  '<span class="pm-hero__chip"><span class="pm-hero__dot" aria-hidden="true"></span>Review queue v3, in pilot</span></div>'
  f'<div class="pm-hero__actions"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" id="rv-copy" data-email="hello@yourname.design">{I["copy"]}<span>Copy email</span></button>'
  f'<a class="pm-btn pm-btn--ghost pm-btn--sm" href="#rv-hero">Résumé{I["ext"]}</a></div>'
  '<p class="pm-sr" aria-live="polite" id="rv-copy-live"></p>'
  '</section></div>')

# ---------- 3. Cards ----------
P = [('queue', 'Review queue for model evaluations', 'Product design · AI tooling', '2024'),
     ('grid', 'One token source for four teams', 'Design systems · Web', '2023'),
     ('form', 'Permissions console for operators', 'Product design · Internal platform', '2022'),
     ('chart', 'Evaluation dashboards reviewers trust', 'Product design · Data viz', '2025')]
def cur_card(k, t, sub, y, state=''):
    return (f'<article class="pm-card{state}"><div class="pm-media pm-card__media"><img src="{IMG[k]}" alt="" width="1600" height="1000"></div>'
            f'<p class="pm-card__eyebrow">{y} · {sub.split(" · ")[1]}</p><h3 class="pm-card__title"><a href="#rv-cards">{t}</a></h3>'
            '<p class="pm-card__summary">Turned an ad-hoc list into a ranked, explainable queue.</p>'
            '<ul class="pm-card__meta"><li class="pm-badge">Research</li><li class="pm-badge">Interaction</li></ul></article>')
def tile(k, t, sub, y, state=''):
    return (f'<article class="pm-card pm-card--tile{state}"><div class="pm-card__stage"><img src="{IMG[k]}" alt="" width="1600" height="1000">'
            f'<span class="pm-card__go" aria-hidden="true">{I["arrow"]}</span></div>'
            f'<div class="pm-card__row"><h3 class="pm-card__title"><a href="#rv-cards">{t}</a></h3><span class="pm-mono">{y}</span></div>'
            f'<p class="pm-card__sub">{sub}</p></article>')
CUR_CARDS = '<div class="rv-stage rv-stage--pad"><div class="rv-cards">' + cur_card(*P[0]) + cur_card(*P[1], state=' is-hover') + '</div></div>'
PROP_CARDS = '<div class="rv-stage rv-stage--pad"><div class="rv-cards">' + tile(*P[0]) + tile(*P[1], state=' is-hover') + '</div></div>'
GRID = ('<div class="rv-stage rv-stage--pad" style="margin-top:var(--space-6)"><ul class="pm-work-grid" aria-label="Proposed work grid">' +
        ''.join(f'<li>{tile(*p)}</li>' for p in P) + '</ul></div>')

# ---------- 4. Flow ----------
def step(title, comp, kind, label, split=False):
    return f'<li class="rv-step{" rv-step--split" if split else ""}"><div class="rv-step__top"><b>{title}</b>{badge(kind, label)}</div><span class="rv-step__desc">{comp}</span></li>'
LANDING = ''.join([
  step('Floating nav', 'TopNavigation <code>--floating</code>: Work · About · Experience · Contact, anchors on one page', 'var', 'Variant'),
  step('Hero', 'Hero (new pattern): one sentence, “Currently designing” chip, Copy email, Résumé', 'new', 'New'),
  step('Selected work', 'Card <code>--tile</code> in a staggered two-column grid; each opens a case study', 'var', 'Variant'),
  step('About', 'Panel (tonal) + metadata rows + a short first-person bio and one photo', 'keep', 'Existing'),
  step('What I do', 'Bento: 3–5 tiles for strengths (systems, AI tooling, research, accessibility)', 'keep', 'Existing'),
  step('Experience', 'Experience list (new): organisation, role, mono years, one-line scope per row', 'new', 'New'),
  step('Contact', 'Closing statement + Copy email + Résumé, the same actions as the hero', 'keep', 'Existing'),
])
CASE = ''.join([
  step('Back + eyebrow', 'Link (standalone, ←) + mono eyebrow “Case study · AI tooling”', 'keep', 'Existing'),
  step('Title + chips', 'Display title + Badges: status, timeline, role, tools', 'keep', 'Existing'),
  step('TL;DR', 'Panel + metadata rows: Background · Problem · Approach · Outcome', 'keep', 'Existing'),
  step('Impact numbers', 'Stat row (new): 3 big numbers with mono labels, reusing the Bento stat style', 'new', 'New'),
  step('Story body', 'Sticky InPageNavigation beside sections: mono label → statement heading → prose → ImageFrame', 'keep', 'Existing', True),
  step('Evidence', 'ImageFrame (annotated, before/after), quotes in a tonal Panel', 'keep', 'Existing', True),
  step('Learnings', 'Statement heading + short list', 'keep', 'Existing'),
  step('More case studies', 'Two Card <code>--tile</code> items', 'var', 'Variant'),
])

ROWS = [
  ('01', 'TopNavigation <code>--floating</code>', 'Variant of an existing component', 'Centred, sticky, floating bar; no current-page indicator; shadow deepens on scroll', 'Adopt. Keep the current header for case-study pages.'),
  ('02', 'Hero', 'New pattern', 'Centred sentence hero with “Currently designing” chip and Copy email', 'Adopt for the landing page'),
  ('03', 'Card <code>--tile</code>', 'Variant of an existing component', 'Neutral stage, artwork rising from the bottom edge, whole-card hover', 'Adopt as the default for selected work'),
  ('04', 'Work grid (staggered)', 'Layout pattern', 'Two columns, right column offset by <code>space-24</code>', 'Adopt; keep the carousel for “More case studies”'),
  ('05', 'Experience list', 'New component', 'Rows: org, role, mono years, scope line', 'Build next, after 01–04 are approved'),
  ('06', 'Stat row', 'New pattern', 'Bento stat styling without the tile, for case-study headers', 'Build with the case-study template'),
]
TABLE = ('<div class="rv-table-wrap"><table class="rv-table"><thead><tr><th>#</th><th>Change</th><th>Type</th><th>What it does</th><th>My recommendation</th></tr></thead><tbody>' +
         ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in ROWS) + '</tbody></table></div>')

def checks(pairs):
    return '<div class="rv-a11y">' + ''.join(f'<span class="pm-mono">{l} <span data-fg="{f}" data-bg="{b}" data-min="{m}"></span></span>' for l, f, b, m in pairs) + '</div>'

page = f'''<title>Portfolio Component Proposals</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&family=Geist+Mono:wght@400;500&display=swap">
<style>
/* Paper × Midnight v1.6 tokens.css + components.css, verbatim */
{tokens}
{comps}
{PROPOSED_CSS}
{PAGE_CSS}
</style>
<div class="rv">
<header class="rv-wrap rv-head">
  <p class="pm-mono" style="margin:0">Paper × Midnight v1.6 · review</p>
  <h1>Component proposals</h1>
  <p>Each change is shown live beside what exists today, using the real system CSS. Nothing here is in the design system yet. Approve, adjust or reject each one, and I’ll fold the approved ones into the system and the landing page.</p>
  <div class="rv-head__bar">
    <nav class="rv-jump" aria-label="Proposals">
      <a class="pm-link" href="#rv-nav">01 Navigation</a><a class="pm-link" href="#rv-hero">02 Hero</a><a class="pm-link" href="#rv-cards">03 Work cards</a><a class="pm-link" href="#rv-flow">04 Page flow</a><a class="pm-link" href="#rv-sum">Summary</a>
    </nav>
    <button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-theme-toggle aria-pressed="false">{I["moon"]}<span>Compare in dark</span></button>
  </div>
</header>

<section class="rv-wrap rv-sec" id="rv-nav" aria-labelledby="rv-nav-h">
  <div class="rv-sec__head"><p class="pm-mono" style="margin:0">01 · Navigation</p><h2 id="rv-nav-h">A centred, floating header</h2>
  <p>Scroll inside the proposed preview: the bar stays pinned and its shadow deepens once content passes underneath.</p></div>
  <div class="rv-compare">{pane(badge('cur','Current'), 'TopNavigation · full-width bar', CUR_NAV)}{pane(badge('prop','Proposed'), 'TopNavigation --floating', PROP_NAV)}</div>
  {notes(['Bar is centred, sized to its content, and floats <code>space-3</code> below the top edge on a 1px <code>border-subtle</code> ring.',
          'Sticky, with <code>shadow-xs</code> at rest and <code>shadow-md</code> once the page scrolls.',
          'No current-page indicator: on a one-page site every link is an anchor, so there’s no “current page” to mark. Hover is a <code>color-bg-surface</code> wash.',
          'Links fit inline on phones (the name hides), so there’s no menu button on the landing page.'],
         ['Matches itti’s quiet centred nav while keeping your brand mark and theme toggle.',
          'Floating keeps the header present without a full-width band competing with the hero.',
          'The current full-width header stays for case-study pages, where “Back to work” matters more.'],
         ['Keyboard focus stays visible (WCAG 2.4.7 requires it). I removed the <em>selected</em> state, not the focus ring. The ring is drawn inside each item.',
          'Items are 32px with a pointer and 44px on touch.',
          'Tokens: <code>color-bg-elevated</code>, <code>color-border-subtle</code>, <code>shadow-xs/md</code>, <code>radius-md</code> bar, <code>radius-sm</code> items. Radius stays md, not a pill, to keep the shape rule.'])}
</section>

<section class="rv-wrap rv-sec" id="rv-hero" aria-labelledby="rv-hero-sh">
  <div class="rv-sec__head"><p class="pm-mono" style="margin:0">02 · Hero</p><h2 id="rv-hero-sh">A standard, centred hero</h2>
  <p>The proposed hero says who you are in one sentence and points at what you’re working on now. It leaves the work to do the talking.</p></div>
  <div class="rv-compare">{pane(badge('cur','Current'), 'About header · display statement', CUR_HERO)}{pane(badge('prop','Proposed'), 'Hero (new pattern)', PROP_HERO)}</div>
  {notes(['Centred stack: one sentence at <code>type-h3</code> (24px). Your name is in primary text, the rest in secondary.',
          '“Currently designing →” in mono, plus a chip with a live dot (the itti pattern, in system shapes).',
          'Two quiet actions: <b>Copy email</b> (copies, then shows “Copied”) and Résumé. The big blue button goes; the work grid becomes the call to action.'],
         ['A smaller headline reads as confident rather than loud, and the cards below become the first visual.',
          'Copy email avoids <code>mailto:</code>, which often fails for people without a mail app set up.',
          'The spec-sheet panel moves down into About, where it supports the bio.'],
         ['One <code>h1</code> per page (it’s an <code>h2</code> here only because this review page has its own h1).',
          'The copy result is announced through a polite live region. The dot pulses only without reduced motion.',
          'Tokens: <code>type-h3</code>, <code>text-primary/secondary</code>, <code>font-mono</code>, <code>state-success</code>, <code>shadow-xs</code>, <code>space-6/16/20</code>.'])}
  {checks([('name','--color-text-primary','--color-bg-canvas',4.5),('sentence','--color-text-secondary','--color-bg-canvas',4.5),('label','--color-text-tertiary','--color-bg-canvas',4.5)])}
</section>

<section class="rv-wrap rv-sec" id="rv-cards" aria-labelledby="rv-cards-h">
  <div class="rv-sec__head"><p class="pm-mono" style="margin:0">03 · Work cards</p><h2 id="rv-cards-h">Grey stage, whole-card hover</h2>
  <p>The right-hand card in each pair is shown in its hover state. Hover the others to compare.</p></div>
  <div class="rv-compare">{pane(badge('cur','Current'), 'Card · frameless, hairline edge', CUR_CARDS)}{pane(badge('prop','Proposed'), 'Card --tile', PROP_CARDS)}</div>
  {GRID}
  {notes(['No outline. The artwork sits on a neutral stage (<code>color-bg-surface</code>), rising from the bottom edge like a screen on a desk.',
          'Hover works on the whole card: the stage deepens to <code>color-bg-sunken</code>, the artwork lifts 8px, and a ↗ chip appears. The title no longer underlines.',
          'Text is simplified to title + mono year on one line, then a single “Discipline · Area” line. Summary and tags move into the case study.',
          'Staggered two-column grid, with the right column offset 96px (the itti rhythm).'],
         ['The stage makes every project read as a curated artifact, even when screenshots vary in colour.',
          'Hover on the image is the clearest signal that the whole card is clickable.',
          'Less text per card makes the grid scannable.'],
         ['The whole card remains one link (one tab stop). Focus shows the ring around the card and reveals the ↗ chip.',
          'The lift turns off with reduced motion; the tone change remains.',
          'Tokens: <code>color-bg-surface/sunken</code>, <code>shadow-md</code> on the artwork, <code>radius-md</code> stage, <code>radius-sm</code> screen, <code>space-8/12</code> insets.'])}
  {checks([('title','--color-text-primary','--color-bg-canvas',4.5),('meta','--color-text-secondary','--color-bg-canvas',4.5),('year','--color-text-tertiary','--color-bg-canvas',4.5)])}
</section>

<section class="rv-wrap rv-sec" id="rv-flow" aria-labelledby="rv-flow-h">
  <div class="rv-sec__head"><p class="pm-mono" style="margin:0">04 · Page flow</p><h2 id="rv-flow-h">One narrative page, and a case-study template</h2>
  <p>The landing page follows Dakota’s one-page narrative. Case studies follow Leah’s structure: summary first, then the story beside a sticky index. Each block maps to a component you already have, or to one I’d add.</p></div>
  <div class="rv-flows">
    <div class="rv-flow"><h3>Landing page</h3><p>Seven blocks, top to bottom. The nav anchors to each.</p><ol class="rv-steps">{LANDING}</ol></div>
    <div class="rv-flow"><h3>Case-study page</h3><p>Grey rows sit in the two-column body beside the sticky index.</p><ol class="rv-steps">{CASE}</ol></div>
  </div>
</section>

<section class="rv-wrap rv-sec" id="rv-sum" aria-labelledby="rv-sum-h">
  <div class="rv-sec__head"><p class="pm-mono" style="margin:0">Summary</p><h2 id="rv-sum-h">What I’d change, and in what order</h2>
  <p>Reply with the numbers you approve, plus any adjustments. Approved items go into the design system (tokens, components, guidelines) and then into the landing page.</p></div>
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
  // floating nav: deepen the shadow once content scrolls under it
  var demo = document.getElementById('rv-navdemo'), fl = document.getElementById('rv-floating');
  demo.addEventListener('scroll', function () {{ fl.classList.toggle('is-scrolled', demo.scrollTop > 8); }}, {{ passive: true }});
  // copy email
  var cp = document.getElementById('rv-copy'), live = document.getElementById('rv-copy-live'), label = cp.querySelector('span');
  cp.addEventListener('click', function () {{
    var email = cp.getAttribute('data-email');
    function done(ok) {{ label.textContent = ok ? 'Copied' : email; live.textContent = ok ? 'Email address copied' : 'Copy failed. The address is ' + email; setTimeout(function () {{ label.textContent = 'Copy email'; }}, 2000); }}
    try {{ navigator.clipboard.writeText(email).then(function () {{ done(true); }}, function () {{ done(false); }}); }} catch (e) {{ done(false); }}
  }});
  // preview links stay put
  document.querySelectorAll('.rv-stage a[href^="#"]').forEach(function (a) {{ a.addEventListener('click', function (e) {{ e.preventDefault(); }}); }});
}})();
</script>
'''
open(os.path.join(REPO, 'prototypes/proposals.html'), 'w').write(page)
print(len(page))
