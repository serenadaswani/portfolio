"""Case-study components, rebuilt from the Mensio handoff (docs/mensio/HANDOFF.md) in Paper × Midnight.

Everything here uses semantic tokens and existing components (Panel, Badge, Button, StatRow, ImageFrame).
Brand colour appears only in project media (the hero's Mensio-blue stage and the Figma screens), as on the landing.
Each builder returns markup; CSS and JS for all of them are in PARTS_CSS and PARTS_JS.
Once a part is used on a second case study, promote it to a design-system component.
"""
from lib import I, _l

A = '../assets/mensio/'  # media, relative to prototypes/

# ---------- Hero: looping product video on a Mensio-blue stage (project art), with a pause control ----------
def hero(src, poster, label):
    return (f'<figure class="cs-hero"><div class="cs-hero__stage">'
            f'<video class="cs-hero__video" muted loop playsinline preload="metadata" poster="{poster}" aria-label="{label}" data-autoplay>'
            f'<source src="{src}" type="video/mp4"></video>'
            f'<button type="button" class="pm-btn pm-btn--secondary pm-btn--icon pm-btn--sm cs-hero__toggle" aria-label="Pause video" data-video-toggle>{I["pause"]}</button>'
            f'</div></figure>')

# ---------- Before/after slider ----------
def before_after(before, before_alt, after, after_alt, before_note, after_note, w=1440, h=1024):
    return ('<div class="cs-ba" data-ba>'
            '<div class="cs-ba__head">'
            f'<div class="cs-ba__side"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-go="100" aria-pressed="false">{_l("arrow-left")}Before</button><p>{before_note}</p></div>'
            f'<div class="cs-ba__side cs-ba__side--r"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" data-go="0" aria-pressed="false">After{_l("arrow-right")}</button><p>{after_note}</p></div>'
            '</div>'
            f'<div class="cs-ba__frame" style="--pos:50%;--ar:{w} / {h}">'
            f'<img class="cs-ba__img" src="{after}" alt="{after_alt}" loading="lazy" width="{w}" height="{h}">'
            f'<div class="cs-ba__before"><img class="cs-ba__img" src="{before}" alt="{before_alt}" loading="lazy" width="{w}" height="{h}"></div>'
            f'<div class="cs-ba__line" aria-hidden="true"><span class="cs-ba__knob">{_l("chevrons-left-right")}</span></div>'
            '<input class="cs-ba__range" type="range" min="0" max="100" value="50" step="0.5" aria-label="Compare before and after: drag left to show more of the redesign">'
            '</div></div>')

# ---------- Custom request timeline ----------
LANES = ['Customer', 'Analyst', 'Manager']
STEPS8 = [
 (0, ['Emails a', 'request'], 'above', 'The customer emails one line, usually just a metric and a brand or program.'),
 (1, ['Asks', 'follow-ups'], 'below', 'The analyst asks for the date range, live or replay, verbal or social, competitors and an asset breakdown.'),
 (0, ['Gets on', 'a call'], 'above', 'If email isn’t enough, the analyst and customer get on a call to pin the request down.'),
 (1, ['Builds', 'the pull'], 'below-left', 'About 10 minutes in Mensio. Analysts pulled extra data so nothing would be missed.'),
 (2, ['Reviews', 'the pull'], 'below', 'A manager checks the pull before it can be saved and exported.'),
 (1, ['Exports,', 'cleans in Excel'], 'above-left', 'The analyst exports to Excel and filters out what the customer didn’t ask for. This took about 35% of an analyst’s day.'),
 (0, ['Receives', 'a file'], 'above', 'The customer gets an Excel file, not a chart they can change themselves.'),
 (1, ['Revises', 'the pull'], 'above-right', 'About 1 in 3 requests come back, often a month later, for roughly an hour of rework.'),
]

def timeline():
    VW, LT, LH = 680, 0, 120
    xs = [134 + i * 68 for i in range(8)]
    yc = [LT + LH * k + LH / 2 for k in range(3)]
    pts = [(xs[i], yc[s[0]]) for i, s in enumerate(STEPS8)]
    VH = LH * 3
    svg = f'<svg class="cs-tl__svg" viewBox="0 0 {VW} {VH}" aria-hidden="true" focusable="false">'
    svg += ('<defs><marker id="cs-tl-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path class="cs-tl__arrowhead" d="M1,1 L9,5 L1,9" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>')
    for k, name in enumerate(LANES):
        y = LT + LH * k
        if k % 2 == 0: svg += f'<rect class="cs-tl__band" x="0" y="{y}" width="{VW}" height="{LH}" rx="8"/>'
        svg += f'<text class="cs-tl__lane" x="16" y="{y + LH / 2 + 4}">{name}</text>'
    (x7, y7), (x3, y3) = pts[7], pts[3]
    dip = yc[1] + LH * 0.6
    svg += f'<path class="cs-tl__loop" d="M{x7},{y7 + 16} C{x7 + 8},{dip + 10} {x3 + 40},{dip + 10} {x3 + 10},{y3 + 16}" marker-end="url(#cs-tl-arrow)"/>'
    svg += f'<text class="cs-tl__loop-t" x="{(xs[5] + xs[7]) / 2 + 10}" y="{dip + 24}" text-anchor="middle">1 in 3 come back</text>'
    for i in range(7):
        (ax, ay), (bx, by) = pts[i], pts[i + 1]
        kk = (bx - ax) * 0.8
        svg += f'<path class="cs-tl__seg" data-seg="{i + 1}" d="M{ax},{ay} C{ax + kk},{ay} {bx - kk},{by} {bx},{by}"/>'
    for i, ((x, y), (lane, lab, pos, desc)) in enumerate(zip(pts, STEPS8)):
        below = pos.startswith('below')
        anchor = 'end' if pos.endswith('left') else ('start' if pos.endswith('right') else 'middle')
        tx = x - 12 if anchor == 'end' else (x + 12 if anchor == 'start' else x)
        y1 = y + 36 if below else y - 38
        svg += (f'<text class="cs-tl__lbl" data-lbl="{i}" x="{tx}" y="{y1}" text-anchor="{anchor}">'
                f'<tspan x="{tx}">{lab[0]}</tspan><tspan x="{tx}" dy="16">{lab[1]}</tspan></text>')
    svg += '</svg>'
    # Real buttons sit over the dots, positioned in % of the drawing, so the steps are focusable and keyboard-driven
    btns = ''.join(
        f'<button type="button" class="cs-tl__dot" data-i="{i}" style="left:{x / VW * 100:.3f}%;top:{y / VH * 100:.3f}%" '
        f'aria-label="Step {i + 1} of 8, {LANES[s[0]]}: {" ".join(s[1])}" aria-pressed="false">{i + 1}</button>'
        for i, ((x, y), s) in enumerate(zip(pts, STEPS8)))
    data = ''.join(f'<template data-step="{i}">{LANES[s[0]]}|{" ".join(s[1])}|{s[3]}</template>' for i, s in enumerate(STEPS8))
    vert = '<ol class="cs-tl__list">' + ''.join(
        f'<li><span class="cs-tl__num" aria-hidden="true">{i + 1}</span><div><p class="cs-tl__who">{LANES[s[0]]}</p>'
        f'<p class="cs-tl__t">{" ".join(s[1])}</p><p class="cs-tl__d">{s[3]}</p></div></li>' for i, s in enumerate(STEPS8)) + '</ol>'
    facts = ('<dl class="cs-tl__facts">' + ''.join(f'<div><dd>{v}</dd><dt>{k}</dt></div>' for v, k in
             [('8', 'steps'), ('3', 'roles'), ('3', 'tools'), ('~1 day', 'end to end')]) + '</dl>')
    return ('<div class="cs-tl" data-tl>' + facts + data +
            f'<div class="cs-tl__wide"><div class="cs-tl__stage">{svg}{btns}</div>'
            '<div class="cs-tl__detail" aria-live="polite"><span class="cs-tl__num cs-tl__num--lg" data-n>8</span><div>'
            '<p class="cs-tl__who" data-who>The whole request</p><p class="cs-tl__t" data-t>8 steps and 7 handoffs for one chart</p>'
            '<p class="cs-tl__d" data-d>About a day end to end. Hover, tap or use the arrow keys on a step to see what happened there.</p></div></div></div>'
            f'<div class="cs-tl__narrow">{vert}<p class="cs-tl__sum">8 steps and 7 handoffs for one chart, about a day end to end. About 1 in 3 come back for rework.</p></div>'
            '</div>')

# ---------- Customer emails ----------
def _chip(icon, text): return f'<li class="pm-badge">{_l(icon, "pm-icon")}{text}</li>'
def _mail(who, subject, body):
    return (f'<article class="pm-panel cs-mail"><header class="cs-mail__head"><span class="cs-mail__av" aria-hidden="true">{I["user"]}</span>'
            f'<div><p class="cs-mail__from">{who}</p><p class="cs-mail__to">To: Mensio analytics team</p></div></header>'
            f'<p class="cs-mail__subj">{subject}</p>{body}</article>')
def emails():
    e1 = _mail('Client, media agency', 'Sponsorship value by team',
               '<p class="cs-mail__body">We filtered to home games to avoid double counting. <strong>Is this right?</strong></p>')
    e2 = _mail('Client, brand team', 'Checking my pull',
               '<ul class="cs-mail__chips" aria-label="Their pull">' + _chip('ruler', 'Equivalent Media Value') + _chip('calendar', 'Last 12 months')
               + _chip('funnel', 'Home Games') + '<li class="pm-badge pm-badge--meta">+6 filters</li></ul>'
               '<p class="cs-mail__body"><strong>Can you check the numbers look right?</strong></p>')
    return f'<div class="cs-mails">{e1}{e2}</div><p class="pm-meta-text cs-note">Names, companies and brands removed.</p>'

# ---------- Icon cards (business impact) ----------
def icon_cards(items):
    return '<ul class="cs-icards">' + ''.join(
        f'<li class="pm-panel cs-icard"><span class="cs-icard__ic" aria-hidden="true">{_l(ic)}</span><h4>{t}</h4><p>{d}</p></li>'
        for ic, t, d in items) + '</ul>'

# ---------- Callout (Design goal, Insight) ----------
def callout(label, text):
    return f'<aside class="pm-panel pm-panel--tonal cs-callout"><p class="cs-callout__label">{label}</p><p class="cs-callout__text">{text}</p></aside>'

# ---------- Wishlist → evidence → built ----------
COLS3 = ['Stakeholder wish', 'Interview evidence', 'What we built']
def roadmap(rows):
    arrow = f'<span class="cs-rm__arrow" aria-hidden="true">{_l("arrow-right")}</span>'
    head = ('<div class="cs-rm__row cs-rm__head" aria-hidden="true">'
            f'<span class="pm-badge">{COLS3[0]}</span><span></span><span class="pm-badge">{COLS3[1]}</span><span></span>'
            f'<span class="pm-badge pm-badge--accent">{COLS3[2]}</span></div>')
    body = ''
    for r in rows:
        cells = [f'<div class="pm-panel pm-panel--sm cs-rm__cell"><p class="cs-rm__col pm-meta-text">{COLS3[j]}</p>'
                 f'<p class="cs-rm__t">{r[j * 2]}</p><p class="cs-rm__d">{r[j * 2 + 1]}</p></div>' for j in range(3)]
        body += f'<li class="cs-rm__row">{cells[0]}{arrow}{cells[1]}{arrow}{cells[2]}</li>'
    return f'<div class="cs-rm">{head}<ol class="cs-rm__list" aria-label="Wishlist to roadmap">{body}</ol></div>'

# ---------- Design QA board ----------
PRI = {'P0': 'pm-badge--error', 'P1': 'pm-badge--warning', 'P2': 'pm-badge--info', 'P3': 'pm-badge--meta', 'P4': 'pm-badge--meta'}
LEG = [('P0', 'Blocks launch'), ('P1', 'Must fix'), ('P2', 'Should fix'), ('P3', 'Polish'), ('P4', 'Nice to have')]
def qa_board(cols):
    out = ('<div class="cs-qa"><div class="cs-qa__head"><h4>Design QA</h4><span class="pm-badge pm-badge--meta">Illustrative</span></div>'
           '<div class="cs-qa__cols">')
    for name, items in cols:
        done = name == 'Done'
        out += (f'<section class="cs-qa__col" aria-label="{name}, {len(items)} items"><h5>{name}<span class="pm-meta-text">{len(items)}</span></h5><ul>'
                + ''.join(f'<li class="pm-panel pm-panel--sm cs-qa__tk{" is-done" if done else ""}"><span class="pm-badge pm-badge--sm {PRI[p]}">{p}</span>'
                          f'<p>{"<s>" if done else ""}{t}{"</s>" if done else ""}</p><small class="pm-meta-text">{area}</small></li>' for p, t, area in items)
                + '</ul></section>')
    out += '</div><ul class="cs-qa__key" aria-label="Priority key">' + ''.join(
        f'<li><span class="pm-badge pm-badge--sm {PRI[k]}">{k}</span>{v}</li>' for k, v in LEG) + '</ul></div>'
    return out

# ---------- Placeholder for a component still to rebuild ----------
def todo(title, what):
    return (f'<figure class="pm-frame"><div class="pm-frame__stage"><div class="pm-media pm-media--16x9" role="img" aria-label="Component to come: {title}">'
            f'<div class="pm-media__fallback">{I["image"]}<span>Component to come: {title}</span><span>{what}</span></div></div></div></figure>')


PARTS_CSS = r"""
/* ===== Case-study parts (Mensio handoff, rebuilt on tokens) ===== */
.cs-note { margin: 0; }

/* Hero: project art. The Mensio-blue stage is brand colour, like the landing card; the video docks to the bottom edge */
.cs-hero { margin: var(--space-10) 0 0; }
.cs-hero__stage { position: relative; overflow: hidden; border-radius: var(--radius-lg); padding: var(--space-10) var(--space-6) 0;
  background: radial-gradient(120% 90% at 85% 100%, #3693F9 0%, rgb(54 147 249 / 0) 60%), linear-gradient(160deg, #175CFF 0%, #206CFD 55%, #2A78FB 100%); }
@container (min-width: 768px) { .cs-hero__stage { padding: var(--space-16) var(--space-16) 0; } }
.cs-hero__video { display: block; width: 100%; max-width: 960px; margin: 0 auto; aspect-ratio: 1440 / 900; object-fit: cover; object-position: top;
  border-radius: var(--radius-md) var(--radius-md) 0 0; background: var(--white); box-shadow: 0 -2px 24px rgb(0 0 0 / 18%); }
.cs-hero__toggle { position: absolute; right: var(--space-3); bottom: var(--space-3); }

/* Before/after slider */
.cs-ba { display: grid; gap: var(--space-4); }
.cs-ba__head { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: var(--space-4); }
.cs-ba__side { display: grid; gap: var(--space-2); justify-items: start; align-content: start; }
.cs-ba__side--r { justify-items: end; text-align: right; }
.cs-ba__side p { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); text-wrap: pretty; }
.cs-ba__side .pm-btn[aria-pressed="true"] { background: var(--color-action-selected-bg); color: var(--color-action-selected-text); }
.cs-ba__frame { --pos: 50%; position: relative; overflow: hidden; aspect-ratio: var(--ar, 1440 / 1024); border-radius: var(--radius-lg); box-shadow: 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); background: var(--color-bg-sunken); touch-action: pan-y; }
.cs-ba__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: left top; user-select: none; -webkit-user-drag: none; }
.cs-ba__before { position: absolute; inset: 0; clip-path: inset(0 calc(100% - var(--pos)) 0 0); }
.cs-ba__line { position: absolute; top: 0; bottom: 0; left: var(--pos); width: 2px; margin-left: -1px; background: var(--color-bg-elevated); box-shadow: 0 0 0 1px var(--color-border-default); pointer-events: none; }
.cs-ba__knob { position: absolute; top: 50%; left: 50%; display: grid; place-items: center; width: 40px; height: 40px; transform: translate(-50%, -50%);
  border-radius: var(--radius-sm); background: var(--color-bg-elevated); color: var(--color-text-primary); box-shadow: 0 0 0 1px var(--color-border-default), var(--shadow-sm); }
.cs-ba__knob .pm-icon { width: 16px; height: 16px; }
.cs-ba__range { position: absolute; inset: 0; width: 100%; height: 100%; margin: 0; opacity: 0; cursor: ew-resize; }
.cs-ba__frame:has(.cs-ba__range:focus-visible) .cs-ba__knob { outline: var(--focus-ring-width) solid var(--color-focus-ring); outline-offset: var(--focus-ring-offset); }

/* Request timeline: horizontal from a 560px container, a vertical list below */
.cs-tl { container: cs-tl / inline-size; display: grid; gap: var(--space-5); }
.cs-tl template { display: none; }
.cs-tl__facts { margin: 0; display: flex; flex-wrap: wrap; justify-content: flex-end; gap: var(--space-2) 0; }
.cs-tl__facts > div { display: flex; align-items: baseline; gap: var(--space-1); padding: 0 var(--space-4); border-left: 1px solid var(--color-border-subtle); }
.cs-tl__facts > div:first-child { border-left: 0; }
.cs-tl__facts > div:last-child { padding-right: 0; }
.cs-tl__facts dd { margin: 0; font-size: var(--type-h4); line-height: var(--line-h4); font-weight: var(--weight-medium); color: var(--color-text-primary); font-variant-numeric: tabular-nums; }
.cs-tl__facts dt { font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-tertiary); }
.cs-tl__wide { display: none; }
.cs-tl__stage { position: relative; }
.cs-tl__svg { display: block; width: 100%; height: auto; overflow: visible; }
.cs-tl__band { fill: var(--color-bg-surface); }
.cs-tl__lane { fill: var(--color-text-tertiary); font-family: var(--font-sans); font-size: 13px; }
.cs-tl__lbl { fill: var(--color-text-secondary); font-family: var(--font-sans); font-size: 13px; }
.cs-tl__lbl.is-on { fill: var(--color-text-primary); font-weight: var(--weight-medium); }
.cs-tl__seg { fill: none; stroke: var(--color-border-default); stroke-width: 2; }
.cs-tl__seg.is-on { stroke: var(--color-text-primary); }
.cs-tl__loop { fill: none; stroke: var(--color-text-tertiary); stroke-width: 1.5; stroke-dasharray: 5 5; }
.cs-tl__arrowhead { stroke: var(--color-text-tertiary); }
.cs-tl__loop-t { fill: var(--color-text-secondary); font-family: var(--font-sans); font-size: 13px; }
.cs-tl__dot { position: absolute; width: 28px; height: 28px; transform: translate(-50%, -50%); display: grid; place-items: center; padding: 0; border: 0; border-radius: 50%;
  background: var(--color-bg-inverse); color: var(--color-text-inverse); font: var(--weight-medium) var(--type-label) / 1 var(--font-sans); font-variant-numeric: tabular-nums; cursor: pointer; box-shadow: 0 0 0 3px var(--color-bg-canvas); }
.cs-tl__dot[aria-pressed="true"] { background: var(--color-action-primary); color: var(--color-text-on-accent); }
.cs-tl__dot:focus-visible { outline: var(--focus-ring-width) solid var(--color-focus-ring); outline-offset: var(--focus-ring-offset); }
@media (pointer: coarse) { .cs-tl__dot::after { content: ""; position: absolute; inset: -8px; } }
.cs-tl__detail, .cs-tl__list li { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: var(--space-4); align-items: start; }
.cs-tl__detail { margin-top: var(--space-5); padding: var(--space-5); border-radius: var(--radius-md); background: var(--color-bg-surface); min-height: 7.5rem; }
.cs-tl__num { display: grid; place-items: center; width: 28px; height: 28px; border-radius: 50%; background: var(--color-bg-inverse); color: var(--color-text-inverse); font: var(--weight-medium) var(--type-label) / 1 var(--font-sans); font-variant-numeric: tabular-nums; }
.cs-tl__num--lg { width: 40px; height: 40px; font-size: var(--type-body-md); }
.cs-tl__who { margin: 0; font-family: var(--font-meta); font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-tertiary); }
.cs-tl__t { margin: var(--space-1) 0 0; font-size: var(--type-body-lg); line-height: var(--line-body-lg); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.cs-tl__d { margin: var(--space-1) 0 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); text-wrap: pretty; }
.cs-tl__list { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-4); }
.cs-tl__list .cs-tl__t { font-size: var(--type-body-md); line-height: var(--line-body-md); }
.cs-tl__sum { margin: 0; padding: var(--space-4); border-radius: var(--radius-md); background: var(--color-bg-surface); font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.cs-tl__narrow { display: grid; gap: var(--space-5); }
@container cs-tl (min-width: 560px) { .cs-tl__wide { display: block; } .cs-tl__narrow { display: none; } }
@container cs-tl (max-width: 559px) { .cs-tl__facts { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-2) var(--space-4); } .cs-tl__facts > div { padding: 0; border-left: 0; } }

/* Customer emails */
.cs-mails { container-type: inline-size; display: grid; gap: var(--space-4); grid-template-columns: minmax(0, 1fr); align-items: start; }
@container (min-width: 560px) { .cs-mails { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.cs-mail { padding: var(--space-5); display: grid; gap: var(--space-3); }
.cs-mail__head { display: flex; align-items: center; gap: var(--space-3); padding-bottom: var(--space-3); border-bottom: 1px solid var(--color-border-subtle); }
.cs-mail__av { display: grid; place-items: center; flex: none; width: 32px; height: 32px; border-radius: var(--radius-sm); background: var(--color-bg-sunken); color: var(--color-text-tertiary); }
.cs-mail__av .pm-icon { width: 16px; height: 16px; }
.cs-mail__from { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); }
.cs-mail__to { margin: 0; font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-tertiary); }
.cs-mail__subj { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); }
.cs-mail__body { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.cs-mail__body strong { font-weight: var(--weight-medium); color: var(--color-text-primary); }
.cs-mail__chips { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: var(--space-2); }
.cs-mail__chips .pm-icon { width: 12px; height: 12px; }

/* Icon cards */
.cs-icards { container-type: inline-size; list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-4); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 600px) { .cs-icards { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.cs-icard { padding: var(--space-5); display: grid; gap: var(--space-2); align-content: start; }
.cs-icard__ic { display: grid; place-items: center; width: 32px; height: 32px; margin-bottom: var(--space-2); border-radius: var(--radius-sm); background: var(--color-bg-surface); color: var(--color-text-primary); }
.cs-icard__ic .pm-icon { width: 16px; height: 16px; }
.cs-icard h4 { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); }
.cs-icard p { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); text-wrap: pretty; }

/* Callout */
.cs-callout { padding: var(--space-5) var(--space-6); display: grid; gap: var(--space-1); }
.cs-callout__label { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-secondary); }
.cs-callout__text { margin: 0; font-size: var(--type-h4); line-height: var(--line-h4); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h4); color: var(--color-text-primary); text-wrap: balance; }

/* Wishlist → evidence → built: three columns with arrows from 640px; stacked cells with column labels below */
.cs-rm { container: cs-rm / inline-size; display: grid; gap: var(--space-3); }
.cs-rm__list { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-3); }
.cs-rm__row { display: grid; gap: var(--space-2); grid-template-columns: minmax(0, 1fr); }
.cs-rm__head { display: none; }
.cs-rm__arrow { display: none; color: var(--color-text-tertiary); }
.cs-rm__arrow .pm-icon { width: 16px; height: 16px; }
.cs-rm__cell { padding: var(--space-4); display: grid; gap: var(--space-1); align-content: start; }
.cs-rm__col { margin: 0 0 var(--space-1); }
.cs-rm__t { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); }
.cs-rm__d { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); text-wrap: pretty; }
.cs-rm__row > .cs-rm__cell:last-child { background: var(--color-action-selected-bg); box-shadow: none; }
.cs-rm__row > .cs-rm__cell:last-child .cs-rm__t { color: var(--color-action-selected-text); }
.cs-rm__list > .cs-rm__row { padding-bottom: var(--space-3); border-bottom: 1px solid var(--color-border-subtle); }
.cs-rm__list > .cs-rm__row:last-child { padding-bottom: 0; border-bottom: 0; }
@container cs-rm (min-width: 640px) {
  .cs-rm__row { grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr) auto minmax(0, 1fr); align-items: stretch; gap: var(--space-2); }
  .cs-rm__head { display: grid; justify-items: start; }
  .cs-rm__arrow { display: grid; place-items: center; }
  .cs-rm__col { display: none; }
  .cs-rm__list > .cs-rm__row { padding-bottom: 0; border-bottom: 0; }
}

/* Design QA board */
.cs-qa { container: cs-qa / inline-size; display: grid; gap: var(--space-4); }
.cs-qa__head { display: flex; align-items: center; justify-content: space-between; gap: var(--space-3); }
.cs-qa__head h4 { margin: 0; font-size: var(--type-body-lg); line-height: var(--line-body-lg); font-weight: var(--weight-medium); }
.cs-qa__cols { display: grid; gap: var(--space-3); grid-template-columns: minmax(0, 1fr); }
@container cs-qa (min-width: 600px) { .cs-qa__cols { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.cs-qa__col { padding: var(--space-3); border-radius: var(--radius-md); background: var(--color-bg-surface); display: grid; gap: var(--space-3); align-content: start; }
.cs-qa__col h5 { margin: 0; display: flex; align-items: baseline; gap: var(--space-2); padding: var(--space-1) var(--space-1) 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); }
.cs-qa__col ul { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-2); }
.cs-qa__tk { padding: var(--space-3); display: grid; gap: var(--space-2); justify-items: start; }
.cs-qa__tk p { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-primary); }
.cs-qa__tk.is-done p { color: var(--color-text-tertiary); }
.cs-qa__key { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: var(--space-2) var(--space-5); font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.cs-qa__key li { display: inline-flex; align-items: center; gap: var(--space-2); }
"""

PARTS_JS = r"""
  // Hero video: autoplay only without reduced motion; the button pauses and resumes (WCAG 2.2.2)
  document.querySelectorAll('[data-autoplay]').forEach(function (v) {
    var btn = v.parentNode.querySelector('[data-video-toggle]'), ICON_PLAY = __PLAY__, ICON_PAUSE = __PAUSE__;
    function sync() { var p = v.paused; btn.innerHTML = p ? ICON_PLAY : ICON_PAUSE; btn.setAttribute('aria-label', p ? 'Play video' : 'Pause video'); }
    if (!reduce) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); }
    btn.addEventListener('click', function () { if (v.paused) v.play(); else v.pause(); });
    v.addEventListener('play', sync); v.addEventListener('pause', sync); sync();
  });

  // Before/after slider
  document.querySelectorAll('[data-ba]').forEach(function (ba) {
    var frame = ba.querySelector('.cs-ba__frame'), range = ba.querySelector('.cs-ba__range'), btns = ba.querySelectorAll('[data-go]'), raf = null;
    function set(v) { frame.style.setProperty('--pos', v + '%'); range.value = v; btns.forEach(function (b) { b.setAttribute('aria-pressed', String(+b.dataset.go === +v)); }); }
    function animate(to, dur) {
      cancelAnimationFrame(raf); var from = +range.value;
      if (reduce) { set(to); return; }
      var t0 = performance.now(); dur = dur || 500;
      (function step(now) { var t = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - t, 3); set(from + (to - from) * e); if (t < 1) raf = requestAnimationFrame(step); })(t0);
    }
    range.addEventListener('input', function () { cancelAnimationFrame(raf); set(+range.value); });
    // Before shows the old screen in full, After the new one; pressing the same button again returns to the split
    btns.forEach(function (b) { b.addEventListener('click', function () { animate(b.getAttribute('aria-pressed') === 'true' ? 50 : +b.dataset.go); }); });
    // A small nudge the first time it scrolls into view, so the divider reads as draggable
    if (!reduce && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); animate(58, 450); setTimeout(function () { animate(50, 450); }, 500); } }, { threshold: 0.6 });
      io.observe(frame);
    }
  });

  // Request timeline: hover, focus, tap or arrow keys pick a step; the path fills up to it and the panel explains it
  document.querySelectorAll('[data-tl]').forEach(function (tl) {
    var dots = [].slice.call(tl.querySelectorAll('.cs-tl__dot')), segs = tl.querySelectorAll('.cs-tl__seg'), lbls = tl.querySelectorAll('.cs-tl__lbl');
    var steps = [].map.call(tl.querySelectorAll('template[data-step]'), function (t) { return t.innerHTML.split('|'); });
    var n = tl.querySelector('[data-n]'), who = tl.querySelector('[data-who]'), tt = tl.querySelector('[data-t]'), dd = tl.querySelector('[data-d]');
    var base = [n.textContent, who.textContent, tt.textContent, dd.textContent], pinned = -1;
    function show(i) {
      dots.forEach(function (d, j) { d.setAttribute('aria-pressed', String(j === i)); });
      segs.forEach(function (s) { s.classList.toggle('is-on', i >= 0 && +s.dataset.seg <= i); });
      lbls.forEach(function (l) { l.classList.toggle('is-on', +l.dataset.lbl === i); });
      if (i < 0) { n.textContent = base[0]; who.textContent = base[1]; tt.textContent = base[2]; dd.textContent = base[3]; return; }
      var s = steps[i]; n.textContent = i + 1; who.textContent = 'Step ' + (i + 1) + ' of 8 · ' + s[0]; tt.textContent = s[1]; dd.textContent = s[2];
    }
    dots.forEach(function (d, i) {
      d.addEventListener('mouseenter', function () { show(i); });
      d.addEventListener('focus', function () { show(i); });
      d.addEventListener('click', function () { pinned = pinned === i ? -1 : i; show(pinned < 0 ? i : pinned); });
      d.addEventListener('keydown', function (e) {
        var k = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key]; if (!k) return;
        e.preventDefault(); dots[(i + k + dots.length) % dots.length].focus();
      });
    });
    tl.querySelector('.cs-tl__stage').addEventListener('mouseleave', function () { show(pinned); });
    tl.addEventListener('focusout', function (e) { if (!tl.contains(e.relatedTarget)) show(pinned); });
  });
"""
PARTS_JS = PARTS_JS.replace('__PLAY__', repr(I['play'])).replace('__PAUSE__', repr(I['pause']))
