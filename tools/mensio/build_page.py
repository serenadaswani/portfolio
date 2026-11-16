import re, sys
OUT = sys.argv[1]
P = {
 'check': '<path d="M20 6 9 17l-5-5"/>',
 'info': '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
 'lock': '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 'calendar': '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
 'chevron': '<path d="m6 9 6 6 6-6"/>',
 'plus': '<path d="M5 12h14"/><path d="M12 5v14"/>',
 'x': '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
 'arrow': '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
 'copy': '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>',
 'dash': '<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
 'eye': '<path d="M2.06 12.35a1 1 0 0 1 0-.7 10.75 10.75 0 0 1 19.88 0 1 1 0 0 1 0 .7 10.75 10.75 0 0 1-19.88 0"/><circle cx="12" cy="12" r="3"/>',
 'pin': '<path d="M12 17v5"/><path d="M9 10.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24V16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V7a1 1 0 0 1 1-1 2 2 0 0 0 0-4H8a2 2 0 0 0 0 4 1 1 0 0 1 1 1z"/>',
 'trend': '<path d="M16 17h6v-6"/><path d="m22 17-8.5-8.5-5 5L2 7"/>',
 'calx': '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="m14 14-4 4"/><path d="m10 14 4 4"/>',
 'ruler': '<path d="M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.41 2.41 0 0 1 0-3.4l2.6-2.6a2.41 2.41 0 0 1 3.4 0Z"/><path d="m14.5 12.5 2-2"/><path d="m11.5 9.5 2-2"/><path d="m8.5 6.5 2-2"/><path d="m17.5 15.5 2-2"/>',
}
def ic(m):
    name, size = m.group(1), m.group(2) or '14'
    col = m.group(3) or 'currentColor'
    w = '3' if name == 'check' else '2'
    return f'<svg class="lucide lucide-{name}" xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>'
A = '../assets/mensio/'
ARROW = '<span class="rm-arrow" aria-hidden="true">[[arrow:19]]</span>'

def rm_row(w1, w2, e1, e2, b1, b2):
    return (f'<div class="rm-row"><div class="rm-cell" data-col="Stakeholder wish"><p class="rm-title">{w1}</p><p class="rm-sub">{w2}</p></div>{ARROW}'
            f'<div class="rm-cell" data-col="Interview evidence"><p class="rm-title">{e1}</p><p class="rm-sub">{e2}</p></div>{ARROW}'
            f'<div class="rm-cell" data-col="What we built"><p class="rm-title">{b1}</p><p class="rm-sub">{b2}</p></div></div>')

# ---------- request timeline: horizontal with hover detail; vertical on narrow screens ----------
LANES = ['Customer', 'Analyst', 'Manager']
steps8 = [
 (0, ['Emails a', 'request'], 'above', 'The customer emails one line, usually just a metric and a brand or program.'),
 (1, ['Asks', 'follow-ups'], 'below', 'The analyst asks for the date range, live or replay, verbal or social, competitors and an asset breakdown.'),
 (0, ['Gets on', 'a call'], 'above', 'If email isn’t enough, the analyst and customer get on a call to pin the request down.'),
 (1, ['Builds', 'the pull'], 'below-left', 'About 10 minutes in Mensio. Analysts pulled extra data so nothing would be missed.'),
 (2, ['Reviews', 'the pull'], 'below', 'A manager checks the pull before it can be saved and exported.'),
 (1, ['Exports,', 'cleans in Excel'], 'above-left', 'The analyst exports to Excel and filters out what the customer didn’t ask for. This took about 35% of an analyst’s day.'),
 (0, ['Receives', 'a file'], 'above', 'The customer gets an Excel file, not a chart they can change themselves.'),
 (1, ['Revises', 'the pull'], 'above-right', 'About 1 in 3 requests come back, often a month later, for roughly an hour of rework.'),
]
VW, LT, LH = 680, 4, 120
xs = [114 + i * 68 for i in range(8)]
yc = [LT + LH * k + LH / 2 for k in range(3)]
pts = [(xs[i], yc[st[0]]) for i, st in enumerate(steps8)]
H = LT + LH * 3 + 8
PADX, PADY = 28, 20
svg = f'<svg class="mx-tl-svg" viewBox="0 {LT} {VW} {LH * 3}" aria-hidden="true">'
svg += '<defs><marker id="mx-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1,1 L9,5 L1,9" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>'
for k, name in enumerate(LANES):
    y = LT + LH * k
    svg += f'<rect class="band{k % 2}" x="0" y="{y}" width="{VW}" height="{LH}" rx="10"/>'
    svg += f'<text class="lane" x="16" y="{y + LH / 2 + 4}">{name}</text>'
(x7, y7), (x3, y3) = pts[7], pts[3]
dip = yc[1] + LH * 0.62
svg += f'<path class="loop" d="M{x7},{y7 + 13} C{x7 + 8},{dip + 10} {x3 + 40},{dip + 10} {x3 + 9},{y3 + 12}" marker-end="url(#mx-arrow)"/>'
svg += f'<text class="loop-t" x="{(xs[5] + xs[7]) / 2 + 10}" y="{dip + 20}" text-anchor="middle">1 in 3 come back</text>'
for i in range(7):
    (ax, ay), (bx, by) = pts[i], pts[i + 1]
    k = (bx - ax) * 0.8
    svg += f'<path class="seg" data-i="{i + 1}" d="M{ax},{ay} C{ax + k},{ay} {bx - k},{by} {bx},{by}"/>'
for i, ((x, y), (lane, lab, pos, desc)) in enumerate(zip(pts, steps8)):
    vy = -1 if pos.startswith('above') else 1
    anchor = 'end' if pos.endswith('left') else ('start' if pos.endswith('right') else 'middle')
    tx = x - 9 if anchor == 'end' else (x + 9 if anchor == 'start' else x)
    y1 = y + 31 if vy > 0 else y - 34
    # generous hit area covering the dot and its label
    hx = tx - 62 if anchor == 'end' else (tx - 4 if anchor == 'start' else tx - 40)
    hy = min(y - 16, y1 - 14) if vy < 0 else y - 16
    hh = (y + 16 - hy) if vy < 0 else (y1 + 20 - hy)
    hx = min(hx, x - 18); hw = max(80, (x + 18) - hx) if anchor == 'end' else 80
    svg += (f'<g class="dot" data-i="{i}"><rect class="hit" x="{hx:.0f}" y="{hy:.0f}" width="{hw:.0f}" height="{hh:.0f}" rx="8"/>'
            f'<circle cx="{x}" cy="{y}" r="13"/><text class="num" x="{x}" y="{y + 4.5}" text-anchor="middle">{i + 1}</text>'
            f'<text class="lbl" x="{tx}" y="{y1}" text-anchor="{anchor}"><tspan x="{tx}">{lab[0]}</tspan><tspan x="{tx}" dy="16">{lab[1]}</tspan></text></g>')
svg += '</svg>'
btns = ''.join(f'<button type="button" class="mx-tl-btn" data-i="{i}">Step {i + 1}: {LANES[st[0]]} {" ".join(st[1]).lower()}</button>' for i, st in enumerate(steps8))
data = ' '.join(f'data-s{i}="{LANES[st[0]]}|{" ".join(st[1])}|{st[3]}"' for i, st in enumerate(steps8))
vert = '<div class="mx-tlv-wrap"><svg class="mx-tlv-svg" aria-hidden="true"></svg><ol class="mx-tlv">' + ''.join(
    f'<li data-lane="{st[0]}"><span class="mx-tlv-dot">{i + 1}</span><div><p class="w">{LANES[st[0]]}</p><p class="t">{" ".join(st[1])}</p><p class="d">{st[3]}</p></div></li>'
    for i, st in enumerate(steps8)) + '</ol></div>'
sw = (f'<div class="mx-tl" {data}>'
      '<dl class="mx-tl-facts"><div><dt>steps</dt><dd>8</dd></div><div><dt>roles</dt><dd>3</dd></div><div><dt>tools</dt><dd>3</dd></div><div><dt>end to end</dt><dd>~1 day</dd></div></dl>'
      f'<div class="mx-tl-h"><div class="mx-tl-stage">{svg}<div class="mx-tl-keys">{btns}</div></div>'
      '<div class="mx-tl-detail" aria-live="polite"><span class="n">8</span><div><p class="w">The whole request</p><p class="t">8 steps and 7 handoffs for one chart</p><p class="d">About a day end to end. Hover or tap a step to see what happened there.</p></div></div></div>'
      f'<div class="mx-tl-v">{vert}<p class="mx-tl-sum"><b>8 steps and 7 handoffs</b> for one chart, about a day end to end. About 1 in 3 come back for rework.</p></div>'
      '</div>')

# ---------- affinity ----------
cols = [
 ('Follow-up questions were consistent', [('“Customers would email us with a one sentence that usually just included the metric and TV program or brand.”', 'Analyst'), ('“We then have to follow up and ask for the date range… whether they want live events…”', 'Analyst'), ('“0–2 [clarifications], depending how specific they are in the original ask.”', 'Senior analyst')]),
 ('Analysts over-pulled data', [('“We pull way more data than required… because we are afraid to miss something.”', 'Analyst'), ('“We export more data than we need and manually filter out what we don’t need in Excel.”', 'Analyst'), ('35% of the day went to exporting and cleaning up data.', 'Analyst estimate')]),
 ('Errors surfaced a month later', [('“The bulk of the time is when we have to go back and add a metric about a month later.”', 'Analyst'), ('About 1 in 3 requests needed rework.', 'Analyst estimate'), ('Finding the missing filter took about an hour, plus explaining the change.', 'Analyst')]),
 ('Customers didn’t understand the data model', [('Customers relied on analysts to explain Brands, Programs, Episodes and Asset Types.', 'Senior analyst'), ('“Users often don’t understand how to interpret the data when segmented in different ways.”', 'Senior analyst'), ('Clients didn’t know where exclusion filters were, or why they mattered.', 'Analyst')]),
]
AFF_DESC = ['Date range, live vs. replay, competitors, asset breakdown. Customers rarely specified these upfront.', 'To avoid missing something, they pulled extra and filtered it in Excel.', 'Finding a missing filter took about an hour, plus explaining the change to the customer.', 'Groupings and filters, such as programs vs. episodes, caused the most confusion.']
PAPER = ['#fdf1a8', '#fbd9e1', '#d6e5ff', '#d4f1dc']
ROT = [[-2.2, 1.6, -0.8], [1.8, -1.4, 0.9], [-1.5, 2.0, -0.6], [2.1, -1.2, 1.1]]
aff = '<div class="mx-sticky">'
for i, (h, ns) in enumerate(cols):
    aff += f'<section class="mx-cluster" style="--paper:{PAPER[i]}"><header><span class="num">0{i + 1}</span><h3>{h}</h3><p>{AFF_DESC[i]}</p></header><div class="mx-stack">'
    for k, (t, w) in enumerate(ns):
        aff += (f'<button type="button" class="mx-sn" style="--i:{k};--r:{ROT[i][k]}deg;z-index:{k + 1}" '
                f'aria-label="Note {k + 1} of {len(ns)}: bring to front"><span class="q">{t}</span><span class="w">{w}</span></button>')
    aff += '</div></section>'
aff += '</div><p class="mx-sticky-hint">Click a note to bring it to the front.</p>' 

# ---------- customer map ----------
groups = [('Super users', '5–10 people, about 5%', 'Live in Data Explorer, but still make mistakes they don’t know about.', 70, 12, ' left'),
          ('Power users', 'Tweak dashboards', 'Tweak custom dashboards, but wouldn’t build a chart from scratch.', 57, 30, ' left'),
          ('High-involvement users', 'About 20 people', 'Settle for core modules and email the team every couple of weeks.', 55, 78, ' above'),
          ('New users &amp; requesters', 'Often the budget owners', 'Need the most guidance, and are often the people who renew the contract.', 7, 88, ' key above')]
mp = '<div class="mx-map"><div class="mx-map-plot">'
for n, sub, d, x, y, k in groups:
    k0 = k; place = 'left' if 'left' in k else 'above'; k = ' key' if 'key' in k else ''
    mp += f'<button type="button" data-place="{place}" data-n="{groups.index((n, sub, d, x, y, k0)) + 1}" class="mx-dot{k}" style="left:{x}%;top:{y}%" data-who="{n}" data-desc="{d}"><span><b>{n}</b><small>{sub}</small></span></button>'
mp += ('<div class="mx-dot-card" role="tooltip"></div></div>'
       '<span class="mx-axis" style="left:44px;bottom:20px">Rarely</span><span class="mx-axis" style="right:0;bottom:20px">Daily</span>'
       '<span class="mx-axis title" style="left:44px;right:0;bottom:0;text-align:center">How often they use Mensio</span>'
       '<span class="mx-axis" style="left:0;top:0">High</span><span class="mx-axis" style="left:0;bottom:44px">Low</span>'
       '<span class="mx-axis title" style="left:14px;top:50%;transform:translate(-50%,-50%) rotate(-90deg);white-space:nowrap">Trust in themselves</span></div>')
mp += '<ol class="mx-map-key">' + ''.join(f'<li class="{"key" if "key" in g[5] else ""}"><span>{i + 1}</span><div><b>{g[0]}</b><small>{g[1]}</small></div></li>' for i, g in enumerate(groups)) + '</ol>'

# ---------- wireframes: two layers (explored / final) that crossfade inside a 380x285 canvas ----------
WFH = '<span class="mx-wf-state"><span>Explored</span><span>Final</span></span><span class="badge">Reconstructed</span>'
def lay(cls, inner): return f'<div class="lay {cls}">{inner}</div>'
def bars(*ws, gap=7): return ''.join(f'<span class="br" style="width:{w};margin-bottom:{gap}px"></span>' for w in ws)
def card(t, sub, on=False, hi=False, style=''):
    return (f'<div class="bx{" hi" if hi else ""}" style="padding:9px 10px;display:flex;gap:7px;{style}">'
            f'<span class="r{" on" if on else ""}"></span><div style="min-width:0"><div class="t">{t}</div><div class="s">{sub}</div></div></div>')
def dlg_head(t, sub): return f'<div class="t" style="font-size:11.5px">{t}</div><div class="s" style="margin-bottom:10px">{sub}</div>'

# 1. three entry points -> two
q = '<div class="t" style="margin-bottom:7px">How would you like to create this chart?</div>'
two = (f'<div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:7px">'
       f'{card("Guided Setup", "Step-by-step guidance", True)}{card("Preset Templates", "Start from a common question")}</div>')
wf7 = ('<div class="mx-wf">' + WFH
       + lay('ex', f'<div class="w dlg">{dlg_head("Create New Chart", "Chart setup")}{q}{two}'
               + card('Custom Build', 'Pick any metrics, groupings and filters', hi=True, style='margin-top:7px') + '</div>')
       + lay('fin', f'<div class="w dlg">{dlg_head("Create New Chart", "Chart setup")}{q}{two}'
               '<div style="margin-top:12px">' + bars('70%', '52%') + '</div></div>')
       + '</div>')

# 2. full-page wizard with a top stepper -> modal with a vertical stepper
STEP5 = ['Metrics', 'Date range', 'Grouping', 'Filters', 'Review']
hstep = '<div class="hstep">' + ''.join(
    f'<span class="hs{" on" if i == 0 else ""}"><span class="nd{" on" if i == 0 else ""}">{i + 1}</span><span class="t">{n}</span></span>' for i, n in enumerate(STEP5)) + '</div>'
pagebar = '<div class="pbar"><span class="t" style="font-weight:600">mensio</span><span class="br" style="width:26px;margin:0"></span><span class="br" style="width:26px;margin:0"></span></div>'
skel_blocks = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">' + ''.join(f'<div class="bx" style="padding:9px">{bars("60%", "85%", gap=5)}</div>' for _ in range(4)) + '</div>'
vstep = '<div class="vstep">' + ''.join(f'<div class="vs{" on" if i == 0 else ""}"><span class="nd{" on" if i == 0 else ""}">{i + 1}</span><span class="t">{n}</span></div>' for i, n in enumerate(STEP5)) + '</div>'
wf8 = ('<div class="mx-wf">' + WFH
       + lay('ex', f'<div class="w page">{pagebar}<div style="padding:10px 12px">'
               f'<div class="t" style="font-size:11.5px;margin-bottom:8px">New chart</div>{hstep}{skel_blocks}</div></div>')
       + lay('fin', f'<div class="w page dim">{pagebar}</div>'
               f'<div class="w modal">{dlg_head("Create New Chart", "Guided Setup · Table")}'
               f'<div style="display:flex;gap:12px">{vstep}<div style="flex:1;min-width:0;border-left:1px solid var(--border);padding-left:10px">'
               + bars('55%', '90%', '75%', '82%', '40%') + '</div></div></div>')
       + '</div>')

# 3. six steps with Schedule -> five steps ending on Review
def vlist(names, cur):
    return '<div class="vstep">' + ''.join(
        f'<div class="vs{" on" if i == cur else ""}"><span class="nd{" on" if i == cur else ""}{" done" if i < cur else ""}">{i + 1}</span><span class="t">{n}</span></div>'
        for i, n in enumerate(names)) + '</div>'
def modal9(names, cur, title, cls='dlg'):
    return (f'<div class="w {cls}">{dlg_head("Create New Chart", "Guided Setup · Table")}'
            f'<div style="display:flex;gap:12px">{vlist(names, cur)}'
            f'<div style="flex:1;min-width:0;border-left:1px solid var(--border);padding-left:10px">'
            f'<div class="t" style="margin-bottom:8px">{title}</div>'
            + bars('80%', '64%', '88%', '50%', '72%') + '</div></div></div>')
wf9 = ('<div class="mx-wf">' + WFH
       + lay('ex', modal9(['Metrics', 'Date range', 'Data grouping', 'Filters', 'Schedule', 'Review'], 4, 'Schedule'))
       + lay('fin', '<div class="w cbar"><span class="br" style="width:54px;margin:0 auto 0 0"></span>'
               '<span class="sl">[[calendar:9]] Schedule Report</span><span class="br" style="width:34px;margin:0"></span></div>'
               + modal9(['Metrics', 'Date range', 'Data grouping', 'Filters', 'Review'], 4, 'Review', 'dlg low'))
       + '</div>')

def explore(label, wf, turn, t, d):
    return (f'<div class="project-content-media"><div class="explore-row"><div class="panel explore-panel"><p class="panel-label">{label}</p><div class="panel-card">{wf}</div></div>'
            f'<div class="explore-caption"><span class="mx-label">{turn}</span><p>{t}</p><p>{d}</p></div></div></div>')

# ---------- solution flow ----------
info = {
 'Metrics': 'Pick a metric group. Its usual metrics are pre-selected, and you can add or remove any.',
 'Date range': 'Choose a quick range, a league season, or several ranges to compare.',
 'Data grouping': 'Choose how the data is split, such as by brand, network, program or episode.',
 'Filters': 'Optional. Narrow by team or program, add exclusion filters, or use advanced filters.',
 'Review': 'See every choice in one place and edit any step before Save & Fetch.',
}
def lane2(door, sub, kinds):
    h = f'<div class="mx-lane2"><div class="mx-door">{door}<small>{sub}</small></div><span class="ar">[[arrow:12]]</span>'
    for i, (nm, k) in enumerate(zip(info, kinds)):
        em = '<em>Defaults selected</em>' if k == 'def' else ('<em>Optional</em>' if k == 'opt' else '')
        d = 'Set by the preset, so it can’t be changed.' if k == 'lock' else info[nm]
        h += f'<button type="button" class="mx-step{" lock" if k=="lock" else ""}" data-n="{i+1}" data-t="{door}: {nm}" data-d="{d}"><i>{i+1}</i>{nm}{em}</button>'
    return h + '<span class="ar">[[arrow:12]]</span><div class="mx-end"><span class="mx-pill">Save &amp; Fetch</span><small>Chart is ready</small></div></div>'
flow2 = ('<div class="mx-scroll"><div class="mx-flow2">' + lane2('Preset', 'Common questions', ['lock', 'req', 'lock', 'opt', 'lock'])
         + lane2('Guided Setup', 'Everything else', ['def', 'req', 'req', 'opt', 'req'])
         + '<div class="mx-key"><div><span style="background:color-mix(in srgb,var(--foreground) 7%,transparent)"></span>You choose</div><div><span style="background:repeating-linear-gradient(135deg,color-mix(in srgb,var(--foreground) 12%,transparent) 0 3px,transparent 3px 6px)"></span>Set by the preset</div></div></div></div>'
         + '<div class="mx-detail" aria-live="polite"><span class="n">5</span><span class="t">steps at most, in one direction</span><span class="d">Hover or tap a step to see what it asks.</span></div>')

# ---------- select screens: UX moments, timed carousel with numbered progress segments ----------
tour_steps = [
 ('One decision per step', 'metrics-expanded', (208, 24, 900, 600), 'A fixed order, metrics to review, so customers never face every option at once.'),
 ('Your choices stay visible', 'review', (430, 118, 1232, 344), 'Every selection becomes a pill at the top, so the chart’s recipe is always in view.'),
 ('Review before you fetch', 'review', (430, 360, 1240, 992), 'One summary of every step, each with an Edit link, before any data is pulled.'),
 ('A chart you can keep changing', 'viewchart', (20, 190, 1420, 700), 'The result is a live chart with its own filters, not a one-off Excel export.'),
 ('Edit from any selection', 'editchart', (10, 76, 1100, 256), 'Clicking a pill on the chart opens Guided Setup at that exact step.'),
]
SHORT = ['Step by step', 'Choices in view', 'Review first', 'Live results', 'Edit in place']
imgs = sorted({st[1] for st in tour_steps}, key=[st[1] for st in tour_steps].index)
segs = ''.join(
    f'<button type="button" class="mx-ind" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-img="{k}" data-r="{",".join(map(str, r))}" data-t="{t}" data-d="{d}">'
    f'<span class="num">{i + 1:02d}</span><span class="lab">{SHORT[i]}</span><span class="trk"><i></i></span></button>'
    for i, (t, k, r, d) in enumerate(tour_steps))
tour = ('<div class="mx-stage mx-tour" aria-roledescription="carousel" aria-label="Select screens">'
        f'<div class="mx-tour-head" aria-live="polite"><p>{tour_steps[0][0]}</p><p>{tour_steps[0][3]}</p></div>'
        f'<div class="mx-inds" role="tablist">{segs}</div>'
        '<div class="mx-tour-frame"><div class="mx-tour-layer">' + ''.join(f'<img src="{A}screens/{k}.webp" alt="" data-k="{k}" loading="lazy">' for k in imgs) + '<div class="mx-ring"></div></div></div></div>')

# ---------- bento: features, each shown as a clean, rebuilt product component ----------
def cell(n, t, d, vis, cls=''):
    return f'<article class="mx-cell {cls}"><header><i>{n:02d}</i><h3>{t}</h3><p>{d}</p></header><div class="mx-vis">{vis}</div></article>'
def radio(on=False): return f'<span class="rd{" on" if on else ""}"></span>'
def opt(title, sub, on=False, extra=''):
    return f'<div class="o{" on" if on else ""}">{radio(on)}<div class="tx"><p class="ot">{title}</p><p class="os">{sub}</p></div>{extra}</div>'
TAG = lambda t: f'<span class="tag">{t}</span>'
CHEV = '[[chevron:12:#64748b]]'
CAL = '[[calendar:12:#64748b]]'

c1 = ('<div class="cmp">'
      '<p class="h">How would you like to create this chart?</p>'
      '<div class="two">' + opt('Guided Setup', 'Follow step-by-step guidance to build your chart.', extra='<span class="rec">Recommended</span>')
      + opt('Preset Templates', 'Start with a predefined chart configuration.', True) + '</div>'
      '<p class="h sm">Select a Preset</p>'
      '<div class="two">' + opt('Total Brand Exposures Across a Season', 'TV Sponsorship [Visual]', extra=TAG('Table'))
      + opt('Duration vs Equivalency for a Program', 'TV Sponsorship [Visual]', extra=TAG('Scatterplot')) + '</div></div>')

CH = ['Avg. Equivalency (%)', 'Duration (HH:MM:SS)', 'Equivalent 30s Units', 'Equivalent Media Value [Visual]']
c2 = ('<div class="cmp">'
      + opt('TV Sponsorship [Visual]', 'Do you want data on TV sponsorship [visual] exposures?', True) +
      '<p class="lbl">Pre-selected metrics</p><div class="chips">'
      + ''.join(f'<span class="chip">[[ruler:10:#64748b]]{x}</span>' for x in CH) + '<span class="chip more">+3 more</span></div></div>')

QR = ['Last 30 days', 'Year to Date', 'Seasons']
c3 = ('<div class="cmp seasons"><div class="qr">' + ''.join(f'<span class="{"on" if q == "Seasons" else ""}">{q}</span>' for q in QR) + '</div>'
      '<div class="sf"><div class="pair"><div><p class="lbl">League / Season</p><div class="fld">NFL / Regular' + CHEV + '</div></div>'
      '<div><p class="lbl">Year</p><div class="fld">2025' + CHEV + '</div></div></div>'
      '<div class="pair"><div><p class="lbl">Start Date</p><div class="fld auto">09-04-2025' + CAL + '</div></div>'
      '<div><p class="lbl">End Date</p><div class="fld auto">01-04-2026' + CAL + '</div></div></div></div></div>')

c4 = ('<div class="cmp guard"><div class="gcol">'
      + opt('TV Sponsorship [Visual &amp; Verbal] <span class="ii">[[info:12:#64748b]]</span>', 'Data on both visual exposures and brand mentions.') +
      '<div class="tip">Note that selecting this will limit access to certain visual and verbal metrics.</div></div>'
      '<div class="gcol"><p class="lbl">Chart style: <b>Heatmap</b></p>'
      '<div class="o off">' + radio() + '<div class="tx"><p class="ot">TV Sponsorship [Visual &amp; Verbal]</p><p class="os">Not available for this chart style.</p></div><span class="tag lock">[[lock:10:#64748b]] Table only</span></div></div></div>')

CT = [('Table', 'tbl'), ('Stacked Bar', 'stk'), ('Horizontal Bar', 'hbar'), ('Trend Line', 'line'), ('Scatterplot', 'dots'), ('Heatmap', 'heat')]
GLY = {
 'tbl': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M3 15h18M9 4v16"/>',
 'stk': '<path d="M5 20V10M12 20V4M19 20v-7"/><path d="M3 20h18"/>',
 'hbar': '<path d="M4 6h12M4 12h16M4 18h8"/>',
 'line': '<path d="M3 17l6-6 4 4 8-8"/>',
 'dots': '<circle cx="7" cy="15" r="1.6"/><circle cx="12" cy="9" r="1.6"/><circle cx="17" cy="13" r="1.6"/><circle cx="9" cy="7" r="1.6"/><circle cx="18" cy="6" r="1.6"/>',
 'heat': '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>',
}
c5 = ('<div class="cmp"><p class="h sm">Chart Style</p><div class="ct">' + ''.join(
      f'<div class="o{" on" if k == "dots" else ""}">{radio(k == "dots")}<span class="ot">{n}</span><svg viewBox="0 0 24 24" aria-hidden="true">{GLY[k]}</svg></div>' for n, k in CT)
      + '</div></div>')

c6 = ('<div class="cmp dup"><div class="tb"><span class="ot">Chart Title</span><span class="b">[[dash:12]] Add to Dashboard</span><span class="b on">[[copy:12]] Duplicate</span></div>'
      '<div class="dlg"><p class="h">Duplicate Chart</p><p class="lbl">Chart name</p><div class="fld">Chart Title Copy</div>'
      '<div class="act"><span class="btn o2">Cancel</span><span class="btn p">Create</span></div></div></div>')

# Each card: copy on top, then a real screen that starts inset at a chosen point and bleeds off the right and bottom edges.
# (src, source w, source h, anchor x, anchor y, image width as % of the frame)
def region(k, sw, sh, x0, y0, x1, y1, alt):
    rw, rh = x1 - x0, y1 - y0
    return (f'<div class="bleed rg" role="img" aria-label="{alt}"><div class="fr" style="aspect-ratio:{rw}/{rh}">'
            f'<img src="{A}bento/{k}.webp" alt="" decoding="async" '
            f'style="--iw:{sw / rw * 100:.3f}%;--t:translate({-x0 / sw * 100:.3f}%,{-y0 / sh * 100:.3f}%)"></div></div>')
def bleed(k, sw, sh, fx, fy, wpct, alt): return region(k, sw, sh, fx, fy, sw, sh, alt)
def bcell(n, t, d, vis, cls=''):
    return f'<article class="mx-cell v5 {cls}"><header><i>{n:02d}</i><h3>{t}</h3><p>{d}</p></header>{vis}</article>'
PSTEPS = ['Preset or Guided Setup', 'Metrics', 'Date Range', 'Data Grouping', 'Filters', 'Review & Fetch']
progression = ('<ol class="mx-seg-steps" aria-label="Six steps: ' + ', '.join(PSTEPS) + '">' + ''.join(
    f'<li><span class="bar"><i></i></span><span class="lab">{t.replace("&", "&amp;")}</span></li>' for t in PSTEPS) + '</ol>')
bento = ('<div class="mx-bento-wrap"><div class="mx-bento v5">'
         + bcell(1, 'One path from question to chart', 'Every chart follows the same six steps, ending in one review before the data is fetched.', progression, 'wide progcard')
         + bcell(2, 'Presets for common questions', 'Six presets answer the requests analysts got most, from season totals to scatterplots.',
                 region('screen-presets', 1395, 2000, 0, 500, 1000, 1500, 'Create New Chart with Preset Templates selected and the list of presets'), 'hero white')
         + bcell(3, 'Smart defaults', 'Picking a metric group pre-selects its most-used metrics.',
                 region('screen-metrics', 1542, 2000, 252, 142, 912, 557, 'Guided Setup Metrics step with pre-selected metric pills and TV Sponsorship [Visual] selected'), 'side white')
         + bcell(4, 'Duplicate and Add to Dashboard', 'Copy a chart or add it to a dashboard from the chart bar.',
                 region('screen-edit', 2000, 1422, 1158, 0, 1768, 384, 'Chart bar with Add to Dashboard, Schedule Report and Duplicate'), 'side zoom')
         + bcell(5, 'Guardrails in the copy', 'Tooltips explain the trade-off before customers make a choice.',
                 region('guardrails', 1536, 428, 12, 12, 1524, 416, 'Tooltip on TV Sponsorship [Visual and Verbal] noting it limits access to certain visual and verbal metrics'), 'strip')
         + bcell(6, 'Chart types beyond tables', 'Scatterplots and heatmaps, which analysts had never built for clients.',
                 region('screen-charts', 2000, 1737, 680, 1080, 1990, 1528, 'Chart Style options including Stacked Bar, Horizontal Bar, Scatterplot and Heatmap'), 'pair-w white')
         + bcell(7, 'A Seasons date picker', 'Pick a league and a year, and the start and end dates fill in.',
                 region('screen-seasons', 2000, 1512, 488, 24, 1500, 594, 'League and Season dropdown with the start date filled in'), 'pair-n')
         + '</div></div>')

# ---------- before/after ----------
ba = ('<div class="mx-cmp">'
      '<div class="mx-cmp-head">'
      '<div class="side l"><button type="button" class="mx-cmp-btn" data-go="100" aria-pressed="false">Before</button><p>Every metric in one dialog, with no order and no guidance.</p></div>'
      '<div class="side r"><button type="button" class="mx-cmp-btn" data-go="0" aria-pressed="false">After</button><p>Five steps in a fixed order, with the usual metrics pre-selected.</p></div>'
      '</div>'
      '<div class="mx-cmp-frame" style="--pos:50%">'
      f'<img class="mx-cmp-img" src="{A}screens/metrics-expanded.webp" alt="After: Guided Setup on the Metrics step, with a metric group chosen and its usual metrics pre-selected" loading="lazy">'
      f'<div class="mx-cmp-before"><img class="mx-cmp-img" src="{A}screens/old-addmetric.webp" alt="Before: the Add Metric dialog listing every metric at once" loading="lazy"></div>'
      '<div class="mx-cmp-line" aria-hidden="true"><span class="mx-cmp-knob">[[chevron:14]][[chevron:14]]</span></div>'
      '<input class="mx-cmp-range" type="range" min="0" max="100" value="50" step="0.5" aria-label="Drag to compare the old and new Data Explorer">'
      '</div>'
      '</div>')


# ---------- stakeholders' vision: animated 6-step wizard with skeleton content ----------
WSTEPS = ['Data type', 'Visualization', 'Metrics', 'Groupings', 'Filters', 'Date range']
def sk(w, h=8, cls=''):
    return f'<i class="sk {cls}" style="width:{w};height:{h}px"></i>'
panes = []
opt = lambda w: f'<div class="card">{sk(w, 8)}</div>'
dd = lambda w: f'<div class="dd">{sk(w, 8)}<span class="chev"></span></div>'
panes.append(f'<div class="g2">{opt("58%")}{opt("46%")}</div>')                                   # data type: two option cards
panes.append('<div class="g3">' + ''.join('<div class="tile"></div>' for _ in range(6)) + '</div>')  # visualization: blank tiles
panes.append(f'<div class="g2">{opt("52%")}{opt("64%")}</div>')                                   # metrics: same option pattern
panes.append('<div class="rows">' + ''.join(f'<div class="row">{sk(w, 8)}</div>' for w in ['44%', '58%', '36%']) + '</div>')  # groupings: plain rows
panes.append(f'<div class="fields">{dd("40%")}{dd("54%")}</div>')                                 # filters: dropdowns
panes.append(f'<div class="g2">{dd("46%")}{dd("52%")}</div>')                                     # date range: two selectors
stepper = ''.join(
    f'<li data-i="{i}"><span class="dot"><b>{i + 1}</b><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></span><span class="lab">{n}</span></li>'
    for i, n in enumerate(WSTEPS))
wiz = (f'<div class="mx-wiz" data-step="0" role="img" aria-label="Animation of a six-step wizard: Data type, Visualization, Metrics, Groupings, Filters and Date range, with Back and Next buttons and a final Submit">'
       '<div class="win">'
       '<div class="bar"><span class="t"></span><span class="x"></span></div>'
       f'<ol class="steps">{stepper}<span class="track"><span class="fill"></span></span></ol>'
       '<div class="body">' + ''.join(f'<div class="pane" data-i="{i}">{p}</div>' for i, p in enumerate(panes)) +
       '<div class="done"><span class="ok"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></span><span class="msg">Chart ready</span></div></div>'
       '<div class="foot"><span class="btn back">Back</span><span class="btn next"><span class="l1">Next</span><span class="l2">Submit</span></span></div>'
       '</div></div>')


# ---------- Design QA: a simple board ----------
QA = [
 ('To fix', [('P0', 'Save & Fetch stays enabled with no date range', 'Guided Setup'),
             ('P1', 'Tooltip covers the Next button on small screens', 'Metrics')]),
 ('In review', [('P1', 'Seasons dates don’t fill in after picking a year', 'Date range'),
                ('P2', 'Selection pills overflow without Show less', 'Edit chart')]),
 ('Done', [('P2', 'Stepper spacing differs between steps', 'Guided Setup'),
           ('P3', 'Preset tags use the wrong text style', 'Presets'),
           ('P4', 'Icon size in the chart bar', 'Chart bar')]),
]
LEG = [('P0', 'Blocks launch'), ('P1', 'Must fix'), ('P2', 'Should fix'), ('P3', 'Polish'), ('P4', 'Nice to have')]
qa = ('<div class="mx-qa"><div class="mx-qa-head"><p>Design QA</p><span class="mx-qa-ill">Illustrative</span></div>'
      '<div class="mx-qa-cols">' + ''.join(
          f'<section class="col"><h4>{name}<span>{len(items)}</span></h4>' + ''.join(
              f'<article class="tk{" done" if name == "Done" else ""}"><span class="pr {pr.lower()}">{pr}</span><p>{t}</p><small>{area}</small></article>'
              for pr, t, area in items) + '</section>' for name, items in QA)
      + '</div><ul class="mx-qa-key">' + ''.join(f'<li><span class="pr {k.lower()}">{k}</span>{v}</li>' for k, v in LEG) + '</ul></div>')


# ---------- anonymized customer emails ----------
def pill(kind, text):
    ico = {'m': '[[ruler:10]]', 'd': '[[calendar:10]]', 'g': '[[x:10]]', 'f': '<svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 5h18l-7 8v6l-4 2v-8z"/></svg>'}[kind]
    return f'<span class="ep {kind}">{ico}<span>{text}</span></span>'
mail = lambda who, sub, body, cls='': (
    f'<article class="em {cls}"><header><span class="av"></span><div><p class="fr">{who}</p><p class="to">To: Mensio analytics team</p></div></header>'
    f'<p class="sj">{sub}</p><div class="bd">{body}</div></article>')
e1 = mail('Client, media agency', 'Sponsorship value by team',
    '<p>We filtered to home games to avoid double counting. <mark>Is this right?</mark></p>')
e2 = mail('Client, brand team', 'Checking my pull',
    '<div class="pills">' + pill('m', 'Equivalent Media Value') + pill('d', 'Last 12 months') + pill('f', 'Home Games') + '<span class="ep more">+6 filters</span></div>'
    '<p><mark>Can you check the numbers look right?</mark></p>', 'b')
emails = f'<div class="mx-emails">{e1}{e2}<p class="mx-emails-note">Names, companies and brands removed.</p></div>'

# ---------- charts ----------
charts = ('<div class="figure-grid cols-2">'
          '<figure><div class="mx-chart" id="mx-scatter"><h4>Duration vs. Equivalency</h4><p>Bubble size is media value · Illustrative data</p><div class="plot"></div><div class="mx-legend"></div></div><figcaption>Scatterplot preset</figcaption></figure>'
          '<figure><div class="mx-chart" id="mx-heatmap"><h4>Total Brand Exposures by Asset</h4><p>Visual occurrence count · Illustrative data</p><div class="plot"></div></div><figcaption>Heatmap preset</figcaption></figure></div>')

page = open(OUT.replace('mensio.html', 'mensio.template.html')).read() if False else None

HTML = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mensio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
  <link rel="stylesheet" href="mensio.css">
</head>
<body class="mensio" data-root="../" data-page="project" data-title="Mensio">
  <div class="shell">
    <div class="page-margin" style="flex:1;display:flex;flex-direction:column">
      <div class="grid-12" style="flex:1">
        <main class="content">
          <article class="case-study fade-in d1">
            <header class="project-measure mx-head">
              <h1 class="project-title">Redesigning Mensio's Data Explorer for self-serve analysis</h1>
              <ul class="mx-pills">
                <li class="on">Shipped</li><li>Product Design</li><li>Redesign</li>
              </ul>
            </header>

            <div class="project-hero mx-stage"><div class="mx-hero-screen"><video autoplay muted loop playsinline preload="metadata" poster="{A}01-hero-poster.jpg" aria-label="A chart being built in Guided Setup, from Create to the finished table"><source src="{A}01-hero.mp4" type="video/mp4"></video></div></div>

            <div class="project-measure">
              <p class="project-section-label mx-tldr-label">TL;DR</p>
              <dl class="mx-tldr">
                <div><dt>Background</dt><dd>Mensio tracks brand exposure across 185 TV networks and 2,000+ social handles.</dd></div>
                <div><dt>Problem</dt><dd>Customers couldn't build charts on their own, so every custom request went through an analyst.</dd></div>
                <div><dt>Approach</dt><dd>We studied the analysts' workflow and built their follow-up questions into a guided chart builder.</dd></div>
                <div><dt>Outcome</dt><dd>Guided Setup shipped in 14 weeks. Customers now build their own charts.</dd></div>
              </dl>
              <div class="mx-stats">
                <div class="mx-stat"><b>8 → <span class="mx-accent">5</span></b><span>Steps to a custom chart</span></div>
                <div class="mx-stat"><b>6</b><span>Presets for common requests</span></div>
                <div class="mx-stat"><b>14 wks</b><span>From research to ship</span></div>
              </div>
            </div>

            <div class="project-sections">

              <section id="overview" data-toc="Overview" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">Overview</p>
                <div class="project-content-text"><h2>Mensio is a powerful tool that tracks brand exposure across TV and social…</h2></div>
                <div class="project-content-text"><p>Brands, teams and networks use it for sponsorship and ad intelligence. It watches every second of 185 TV networks and 2,000+ social handles, and catches 13,000+ brand logos at 99%+ accuracy.</p></div>
                <div class="project-content-text"><h2>…but customers couldn't get the data out on their own.</h2></div>
                <div class="project-content-text"><p>Data Explorer showed every metric, grouping and filter at once. Customers didn't know which combination answered their question, so they leaned on Mensio's analysts to pull the data for them.</p><p>We redesigned chart building into <span class="mx-hl">Guided Setup, a step-by-step wizard with presets</span>, and shipped it in 14 weeks.</p></div>
                <div class="project-content-media">{ba}</div>
              </section>

              <section id="assumption" data-toc="Starting assumption" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">Starting assumption</p>
                <div class="project-content-text"><h2>We assumed customers were our primary users. We were wrong.</h2></div>
                <div class="project-content-text"><p>New to Mensio, we planned to start with customer pain points. Our first stakeholder conversations changed that.</p></div>
                <div class="project-content-text">
                  <div class="takeaways">
                    <div><p>What we assumed</p><p>Customers built their own charts, and their pain points would show us what to fix.</p></div>
                    <div><p>What we found</p><p>There were no documented customer pain points. <span class="mx-hl">Analysts were doing the work</span>, so their workflow was what we needed to study.</p></div>
                  </div>
                </div>
              </section>

              <section id="problem" data-toc="The problem" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">The problem</p>
                <div class="project-content-text"><h2>Every custom chart went through an analyst.</h2></div>
                <div class="project-content-text"><p>A one-line customer email became <span class="mx-hl">an eight-step process across two people and three tools</span>.</p></div>
                <div class="project-content-media">
                  <div class="panel" style="background:#2b3a6714">
                    <p class="panel-label">A custom request, step by step</p>
                    <div class="panel-card" style="display:block">{sw}</div>
                  </div>
                </div>
                <div class="project-content-media"><div class="panel" style="background:#2b3a6714"><p class="panel-label">Customers asked analysts to check their own pulls</p><div class="panel-card" style="display:block">{emails}</div></div></div>
                <div class="project-content-media"><div class="figure-grid cols-2"><figure><div class="figure-media" style="aspect-ratio:4 / 3"><span class="asset-note">Anonymized session clip</span></div><figcaption>A frustrated session in the old explorer</figcaption></figure></div></div>

                <div id="analysts" data-toc="Impact on analysts" class="project-subsection project-content-text">
                  <p class="project-subsection-label">Impact on analysts</p>
                  <h2>Analysts spent most of their day fulfilling requests.</h2>
                </div>
                <div class="project-content-text">
                  <div class="mx-stats">
                    <div class="mx-stat"><b>~1 day</b><span>End to end, per request</span></div>
                    <div class="mx-stat key"><b>85%</b><span>Of an analyst's day on requests, exports and cleanup</span></div>
                    <div class="mx-stat"><b>1 in 3</b><span>Requests came back for rework</span></div>
                  </div>
                </div>

                <div id="renewal" data-toc="Impact on the business" class="project-subsection project-content-text">
                  <p class="project-subsection-label">Impact on the business</p>
                  <h2>Customers couldn't see Mensio's value or potential unless they used it themselves.</h2>
                </div>
                <div class="project-content-text">
                  <ul class="mx-cards">
                    <li><span class="mx-ic">[[trend:18]]</span><p class="t">Low adoption</p><p class="d">Customers stopped using Mensio or relied on analysts.</p></li>
                    <li><span class="mx-ic">[[calx:18]]</span><p class="t">Weak renewals</p><p class="d">Buyers rarely used the product after the demo, so they couldn't speak to its value at renewal.</p></li>
                    <li><span class="mx-ic">[[lock:18]]</span><p class="t">Capped value</p><p class="d">Mensio's full value was only reachable through the analytics team.</p></li>
                  </ul>
                </div>
              </section>

              <section id="insight" data-toc="The insight" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">The insight</p>
                <div class="project-content-text"><h2>The process lived in analysts' heads.</h2></div>
                <div class="project-content-text"><p>Accurate pulls depend on knowing which filters and exclusions go together. Adding teams, for example, requires home, neutral and non-game filters to avoid double-counting. <span class="mx-hl">None of it was documented.</span></p></div>
                <div class="project-content-text"><p class="mission"><span>Design goal</span>Have the product ask the questions an analyst would.</p></div>
              </section>

              <section id="interviews" data-toc="Analyst interviews" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">Analyst interviews</p>
                <div class="project-content-text"><h2>We studied the analyst workflow to rebuild it for customers.</h2></div>
                <div class="project-content-text"><p>Since analysts were doing the work, we studied their workflow to understand what customers actually received. We used Mensio daily and interviewed the media analysts who handled customer requests.</p></div>
                <div class="project-content-media">
                  <div class="panel" style="background:#2b3a6714">
                    <p class="panel-label">What analysts told us</p>
                    <div class="panel-card" style="display:block">{aff}</div>
                  </div>
                </div>
                <div class="project-content-text"><blockquote>“There is no checklist, so you are trying to remember off the top of your head…”</blockquote></div>
                <div class="project-content-text"><div class="mx-callout"><span class="mx-label">Insight</span><p>The analysts' follow-up questions became the structure of the wizard.</p></div></div>
              </section>

              <section id="roadmap" data-toc="Wishlist to roadmap" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">Wishlist to roadmap</p>
                <div class="project-content-text"><h2>We merged stakeholder requests and research findings into one roadmap.</h2></div>
                <div class="project-content-text"><p>Stakeholders brought a wishlist, led by a left-to-right flow. We validated each item against the interviews and prioritized what to build.</p></div>
                <div class="project-content-media">
                  <div class="panel" style="background:#2b3a6714">
                    <p class="panel-label">The stakeholders' left-to-right vision</p>
                    <div class="panel-card" style="display:block">{wiz}</div>
                  </div>
                </div>
                <div class="project-content-media">
                  <div class="roadmap">
                    <div class="rm-row rm-head"><span class="rm-pill">Stakeholder wish</span><span></span><span class="rm-pill">Interview evidence</span><span></span><span class="rm-pill rm-pill--accent">What we built</span></div>
                    {rm_row('Streamlined left-to-right flow', 'Build a chart in sequence, not all at once', 'Same questions, every request', 'Analysts asked the same follow-ups, in the same order', 'Guided Setup', 'Five sequential steps, from metrics to review')}
                    {rm_row("Show only what's relevant", 'Guide customers through filter choices', 'Hidden nuances in data', 'Filters confused customers; 1 in 3 requests needed rework', 'Progressive options', 'Each step shows only what fits, with tooltips and guardrails')}
                    {rm_row('Offer pre-set views', 'Answers to the questions customers ask most', 'Repeated requests', 'Most were a metric plus a brand or program', 'Six presets', 'Based on the most common use cases')}
                  </div>
                </div>
                <div class="project-content-text"><p>We chose a wizard as the core pattern. It matched the stakeholders' left-to-right vision and mirrored how analysts already worked.</p></div>

                <div id="customers" data-toc="Customer groups" class="project-subsection project-content-text">
                  <p class="project-subsection-label">Customer groups</p>
                  <h2>Customer groups shaped the wizard's two branches.</h2>
                </div>
                <div class="project-content-text"><p>Usage and common requests varied by group. From one entry point, people choose how to build a chart: a preset for recurring questions, or Guided Setup for everything else.</p></div>
                <div class="project-content-media">
                  <div class="panel" style="background:#2b3a6714">
                    <p class="panel-label">How often they use Mensio vs. how much they trust themselves</p>
                    <div class="panel-card" style="display:block">{mp}</div>
                  </div>
                </div>
              </section>

              <section id="exploration" data-toc="Navigating the mess" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">Navigating the mess</p>
                <div class="project-content-text"><h2>Three flow variations led to our final wizard.</h2></div>
                <div class="project-content-text"><p>Feedback from analysts, engineers and stakeholders shaped each version. Hover a design to see what it became.</p></div>
                {explore('Three separate flows', wf7, 'Key turn 1', 'Three paths became two', 'Presets, Guided and Custom confused the analytics team. We folded Custom into Guided Setup as “Frequently Selected Options.”')}
                {explore('Full-page wizard', wf8, 'Key turn 2', 'A full-page wizard became a modal', 'Backend constraints required a modal, so we redesigned the micro-interactions to avoid modal-on-modal.')}
                {explore('Six-step flow', wf9, 'Key turn 3', 'Six steps became five', 'We moved scheduling to the nav bar to keep the modal focused on building a chart.')}
              </section>

              <section id="solution" data-toc="The solution" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">The solution</p>
                <div class="project-content-text"><h2>Six design decisions shaped Guided Setup.</h2></div>
                <div class="project-content-media">{bento}</div>
                <div id="screens" data-toc="Select screens" class="project-subsection project-content-text">
                  <p class="project-subsection-label">Select screens</p>
                  <h2>Building a chart, from first click to the finished table.</h2>
                </div>
                <div class="project-content-media">{tour}</div>
              </section>

              <section id="engineering" data-toc="Design x Engineering" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">Design x Engineering</p>
                <div class="project-content-text"><h2>We designed within the backend's rules.</h2></div>
                <div class="project-content-text"><p>We acted as our own PMs, worked within the rules for valid chart combinations, asked for a Seasons API, and triaged QA by priority across a 14-week build.</p><p>In parallel, we built a new design system now adopted across all Deploy products, and mapped its components to Mensio's production screens.</p><p>Along the way, we found capabilities, like multiple date ranges, that <span class="mx-hl">neither the analytics team nor the engineers knew existed</span>, and turned them into features.</p></div>
                <div class="project-content-media">
                  <div class="panel" style="background:color-mix(in srgb, var(--foreground) 6%, transparent)">
                    <p class="panel-label">Design QA, triaged P0–P4</p>
                    <div class="panel-card" style="display:block">{qa}</div>
                  </div>
                </div>
              </section>

              <section id="reflection" data-toc="Impact &amp; reflection" class="project-content-grid">
                <div class="project-content-text"><div class="divider"></div></div>
                <p class="project-section-label project-content-text">Impact &amp; reflection</p>
                <div class="project-content-text"><h2>Customers now build their own charts.</h2></div>
                <div class="project-content-text">
                  <ul class="bullets">
                    <li>Clients now use <span class="mx-hl">scatterplots and heatmaps</span> the team never built for them before.</li>
                    <li>Multiple date ranges replace stitching several charts together in Excel.</li>
                    <li>Customers know where the exclusion filters are, and why they matter.</li>
                  </ul>
                </div>
                <div class="project-content-media">{charts}</div>
                <div class="project-content-text">
                  <div class="takeaways">
                    <div><p>Encode expert knowledge into the product</p><p>Presets, defaults and tooltips now ask what analysts used to ask over email.</p></div>
                    <div><p>Design with constraints, not against them</p><p>Working within the backend's rules shaped a simpler flow.</p></div>
                  </div>
                </div>
              </section>

            </div>
          </article>
        </main>
      </div>
    </div>
  </div>
  <script src="../site.js"></script>
  <script src="mensio.js" defer></script>
</body>
</html>
'''
HTML = re.sub(r'<span class="mx-hl">(.*?)</span>', r'\1', HTML)
HTML = re.sub(r'\[\[(\w+):?(\d+)?:?([#\w]+)?\]\]', ic, HTML)
open(OUT, 'w').write(HTML)
print('wrote', len(HTML))
