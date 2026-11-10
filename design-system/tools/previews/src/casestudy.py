"""Case-study template (v1.8), first instance: Mensio.
Structure (Leah Kim): back link + eyebrow -> title + badges -> summary panel -> StatRow ->
sticky InPageNavigation + sections with ImageFrame -> learnings -> more case studies (Card --showcase).
Built only from design-system components; page CSS composes them with semantic tokens.
Copy is ported from projects/mensio.html. Images are still placeholders there, so figures show an
"Image to come" slot with the planned content as text.
Run: python3 design-system/tools/previews/src/casestudy.py  ->  prototypes/mensio.html
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import I, showcase
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
tokens = open(os.path.join(REPO, 'design-system', 'css', 'tokens.css')).read()
comps = open(os.path.join(REPO, 'design-system', 'css', 'components.css')).read()
VER = 'v1.9'
NAME = 'Serena Daswani'

_fig = [0]
def fig(caption, planned, ratio='16x10', variant=''):
    """ImageFrame with an empty slot. Swap the fallback div for <img alt="..."> once the asset exists."""
    _fig[0] += 1
    n = f'{_fig[0]:02d}'
    return (f'<figure class="pm-frame{variant}"><div class="pm-frame__stage">'
            + ('<div class="pm-frame__chrome" aria-hidden="true"><b></b></div>' if 'browser' in variant else '') +
            f'<div class="pm-media pm-media--{ratio}" role="img" aria-label="Image to come: {planned}">'
            f'<div class="pm-media__fallback">{I["image"]}<span>Image to come</span><span>{planned}</span></div></div></div>'
            f'<figcaption class="pm-frame__caption"><span class="pm-frame__index">Fig. {n}</span><span>{caption}</span></figcaption></figure>')

def stats(items, cls=''):
    return f'<dl class="pm-stats{cls}">' + ''.join(f'<div class="pm-stats__item"><dt class="pm-stats__label">{l}</dt><dd class="pm-stats__value">{v}</dd></div>' for v, l in items) + '</dl>'

def meta(rows):
    return '<dl class="pm-meta">' + ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in rows) + '</dl>'

def points(items, cls='cs-points'):
    """Numbered title + description list."""
    return f'<ol class="{cls}">' + ''.join(f'<li><span class="pm-meta-text" aria-hidden="true">{i+1:02d}</span><div><h4>{t}</h4><p>{d}</p></div></li>' for i, (t, d) in enumerate(items)) + '</ol>'

def panel(title, body, cls='', pid=''):
    return (f'<section class="pm-panel{cls}" aria-labelledby="{pid}"><div class="pm-panel__header"><h4 class="pm-panel__title" id="{pid}">{title}</h4></div>'
            f'<div class="pm-panel__body">{body}</div></section>')

SECTIONS = [  # id, TOC label
    ('overview', 'Overview'), ('problem', 'The problem'), ('research', 'Research'), ('roadmap', 'Roadmap'),
    ('iterations', 'Iterations'), ('solution', 'The solution'), ('engineering', 'Design × engineering'), ('impact', 'Impact')]

def section(sid, eyebrow, title, body):
    return (f'<section class="cs-section" id="{sid}" aria-labelledby="h-{sid}">'
            f'<p class="cs-eyebrow">{eyebrow}</p><h2 class="cs-h2" id="h-{sid}">{title}</h2>{body}</section>')

def lede(*ps):
    return '<div class="cs-prose">' + ''.join(f'<p>{p}</p>' for p in ps) + '</div>'

STEPS = ['Client emails one line', 'Analyst follows up', 'Call if too complex', 'Analyst builds the pull',
         'Manager reviews', 'Export, clean in Excel', 'Send to client', 'Revise']

BODY = ''.join([
    section('overview', 'Overview', 'Mensio tracks brand exposure across TV and social…',
        lede('Brands, teams and networks use it for sponsorship and ad intelligence. It watches every second of 185 TV networks and 2,000+ social handles, and catches 13,000+ brand logos at 99%+ accuracy.')
        + fig('Mensio Data Explorer, before the redesign.', 'Screenshot of the old Data Explorer', variant=' pm-frame--browser')
        + '<h3 class="cs-h3">…but customers couldn’t get the data out on their own.</h3>'
        + lede('Data Explorer showed every metric, grouping and filter at once. Customers didn’t know which combination answered their question, so they leaned on Mensio’s analysts to pull the data for them. We redesigned chart building into Guided Setup, a step-by-step wizard with presets, and shipped it in 14 weeks.')
        + '<h3 class="cs-h3">We assumed customers were our primary users. We were wrong.</h3>'
        + lede('New to Mensio, we planned to start with customer pain points. Our first stakeholder conversations changed that.')
        + '<div class="cs-pair">'
        + panel('What we assumed', '<p>Customers built their own charts, and their pain points would show us what to fix.</p>', ' pm-panel--tonal', 'p-assumed')
        + panel('What we found', '<p>There were no documented customer pain points. Analysts were doing the work, so their workflow was what we needed to study.</p>', '', 'p-found')
        + '</div>'),

    section('problem', 'The problem', 'Every custom chart went through an analyst.',
        lede('A one-line customer email became an eight-step process across two people and three tools.')
        + '<figure class="pm-frame"><div class="pm-frame__stage"><ol class="cs-steps">'
        + ''.join(f'<li><span class="pm-meta-text">{i+1:02d}</span>{s}</li>' for i, s in enumerate(STEPS))
        + '</ol></div><figcaption class="pm-frame__caption"><span class="pm-frame__index">Process</span><span>A custom request: 8 steps, 2 people, 3 tools.</span></figcaption></figure>'
        + '<div class="cs-pair">' + fig('Customer emails asking for one-off pulls.', 'Collage of anonymized customer emails', '4x3')
        + fig('A frustrated session in the old explorer.', 'Anonymized session clip', '4x3') + '</div>'
        + '<h3 class="cs-h3">Analysts spent most of their day fulfilling requests.</h3>'
        + stats([('~1 day', 'end-to-end per request'), ('85%', 'of an analyst’s day on requests, exports and cleanup'), ('1 in 3', 'requests came back for rework')], ' pm-stats--sm')
        + '<h3 class="cs-h3">Customers couldn’t see Mensio’s value unless they used it themselves.</h3>'
        + points([('Low adoption', 'Customers stopped using Mensio or relied on analysts.'),
                  ('Weak renewals', 'Buyers rarely used the product after the demo, so they couldn’t speak to its value at renewal.'),
                  ('Capped value', 'Mensio’s full value was only reachable through the analytics team.')])),

    section('research', 'The insight', 'The process lived in analysts’ heads.',
        lede('Accurate pulls depend on knowing which filters and exclusions go together. Adding teams, for example, requires home, neutral and non-game filters to avoid double-counting. None of it was documented.')
        + panel('Design goal', '<p class="cs-goal">Have the product ask the questions an analyst would.</p>', ' pm-panel--tonal', 'p-goal')
        + '<h3 class="cs-h3">We studied the analyst workflow to rebuild it for customers.</h3>'
        + lede('We used Mensio daily and interviewed the media analysts who handled customer requests.')
        + fig('What analysts told us.', 'Interview synthesis: affinity map or key quotes')
        + points([('Follow-up questions were consistent', 'Date range, live vs. replay, competitors, asset breakdown. Customers rarely specified these upfront.'),
                  ('Analysts over-pulled data', 'To avoid missing something, they pulled extra and filtered it in Excel.'),
                  ('Errors surfaced a month later', 'Finding a missing filter took about an hour, plus explaining the change to the customer.'),
                  ('Customers didn’t understand the data model', 'Groupings and filters, such as programs vs. episodes, caused the most confusion.')])
        + '<figure class="cs-quote"><blockquote><p>“There is no checklist, so you are trying to remember off the top of your head…”</p></blockquote>'
          '<figcaption>The analysts’ follow-up questions became the structure of the wizard.</figcaption></figure>'),

    section('roadmap', 'Wishlist to roadmap', 'We merged stakeholder requests and research findings into one roadmap.',
        lede('Stakeholders brought a wishlist, led by a left-to-right flow: data type, visualization, metrics, groupings, filters, date range. We validated each item against the interviews and prioritized what to build.')
        + '<div class="cs-table-wrap" tabindex="0" role="region" aria-labelledby="t-roadmap"><table class="cs-table"><caption id="t-roadmap" class="pm-sr">Stakeholder wishes, interview evidence and what we built</caption>'
          '<thead><tr><th scope="col">Stakeholder wish</th><th scope="col">Interview evidence</th><th scope="col">What we built</th></tr></thead><tbody>'
        + ''.join(f'<tr><td><b>{a}</b>{a2}</td><td><b>{b}</b>{b2}</td><td><b>{c}</b>{c2}</td></tr>' for a, a2, b, b2, c, c2 in [
            ('Streamlined left-to-right flow', 'Build a chart in sequence, not all at once', 'Same questions, every request', 'Analysts asked the same follow-ups, in the same order', 'Guided Setup', 'Five sequential steps, from metrics to review'),
            ('Show only what’s relevant', 'Guide customers through filter choices', 'Hidden nuances in data', 'Filters confused customers; 1 in 3 requests needed rework', 'Progressive options', 'Each step shows only what fits, with tooltips and guardrails'),
            ('Offer pre-set views', 'Answers to the questions customers ask most', 'Repeated requests', 'Most were a metric plus a brand or program', 'Six presets', 'Based on the most common use cases')])
        + '</tbody></table></div>'
        + lede('We chose a wizard as the core pattern. It matched the stakeholders’ left-to-right vision and mirrored how analysts already worked.')
        + '<h3 class="cs-h3">Customer groups shaped the wizard’s two branches.</h3>'
        + lede('From one entry point, people choose how to build a chart: a preset for recurring questions, or Guided Setup for everything else.')
        + fig('How often they use Mensio vs. how much they trust themselves.', 'Customer map: four groups plotted on a 2×2', '4x3')
        + meta([('Super users', 'Live in Data Explorer, still make mistakes they don’t know about'),
                ('Power users', 'Tweak custom dashboards, wouldn’t build from scratch'),
                ('High-involvement', 'Settle for core modules, email the team every couple of weeks'),
                ('New users', 'Need the most guidance, and are often the budget owners')])),

    section('iterations', 'Navigating the mess', 'Three flow variations led to our final wizard.',
        lede('Feedback from analysts, engineers and stakeholders shaped each version.')
        + ''.join('<div class="cs-iter">' + fig(cap, planned) + f'<div><h3 class="cs-h4">{t}</h3><p>{d}</p></div></div>' for cap, planned, t, d in [
            ('Three separate flows.', 'Discarded design: three entry points', 'Three paths became two', 'Presets, Guided and Custom confused the analytics team. We folded Custom into Guided Setup as “Frequently Selected Options.”'),
            ('Full-page wizard.', 'Discarded design: full-page wizard', 'A full-page wizard became a modal', 'Backend constraints required a modal, so we redesigned the micro-interactions to avoid modal-on-modal.'),
            ('Six-step flow.', 'Discarded design: six steps with scheduling', 'Six steps became five', 'We moved scheduling to the nav bar to keep the modal focused on building a chart.')])),

    section('solution', 'The solution', 'Six design decisions shaped Guided Setup.',
        fig('After: the customer builds it.', 'Diagram: preset or Guided Setup → 5 steps with defaults → Save &amp; Fetch')
        + fig('Building a chart with Guided Setup.', 'Prototype video: the guided flow and a preset', '16x9', ' pm-frame--browser')
        + points([('One entry, two paths', 'Six presets for common questions; Guided Setup for everything else.'),
                  ('A linear flow', 'Metrics → Date range → Grouping → Filters → Review, showing only options that fit.'),
                  ('Smart defaults', 'Picking a metric group pre-selects the usual metrics.'),
                  ('Built-in guardrails', 'Tooltips explain exclusion and double-counting rules; invalid combinations are blocked.'),
                  ('Advanced features, surfaced', 'Multiple date ranges, a Seasons date picker, scatterplot and heatmap presets.'),
                  ('Shortcuts for power users', 'Duplicate Chart, Add to Dashboard and Pin cut repeated work.')], 'cs-points cs-points--grid')),

    section('engineering', 'Design × engineering', 'We designed within the backend’s rules.',
        lede('We acted as our own PMs, worked within the rules for valid chart combinations, asked for a Seasons API, and triaged QA by priority across a 14-week build.',
             'In parallel, we built a new design system now adopted across all Deploy products, and mapped its components to Mensio’s production screens. Along the way, we found capabilities, like multiple date ranges, that neither the analytics team nor the engineers knew existed, and turned them into features.')
        + fig('Design QA, triaged P0–P4.', 'Screenshot of the QA tracker', variant=' pm-frame--browser')),

    section('impact', 'Impact &amp; reflection', 'Customers now build their own charts.',
        points([('New chart types', 'Clients now use scatterplots and heatmaps the team never built for them before.'),
                ('No more stitching', 'Multiple date ranges replace stitching several charts together in Excel.'),
                ('Filters understood', 'Customers know where the exclusion filters are, and why they matter.')])
        + '<div class="cs-pair">' + fig('Scatterplot preset.', 'Customer-built scatterplot', '4x3') + fig('Heatmap preset.', 'Customer-built heatmap', '4x3') + '</div>'
        + '<h3 class="cs-h3">What I learned</h3>'
        + '<div class="cs-pair">'
        + panel('Encode expert knowledge into the product', '<p>Presets, defaults and tooltips now ask what analysts used to ask over email.</p>', ' pm-panel--tonal', 'p-l1')
        + panel('Design with constraints, not against them', '<p>Working within the backend’s rules shaped a simpler flow.</p>', ' pm-panel--tonal', 'p-l2')
        + '</div>'),
])

TOC = ''.join(f'<li><a class="pm-toc__item" href="#{sid}"{" aria-current=\"location\"" if i == 0 else ""} data-spy><span class="pm-toc__num">{i+1:02d}</span>{label}</a></li>' for i, (sid, label) in enumerate(SECTIONS))

MORE = [('chart', 'Placeholder project', 'Your second strongest project.', ['Product design'], 'Placeholder'),
        ('queue', 'Placeholder project', 'A supporting project.', ['Product design'], 'Placeholder')]

PAGE_CSS = r"""
/* Page background: white in light (the system's canvas token stays paper); dark is unchanged */
@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) { --color-bg-canvas: var(--white); } }
[data-theme="light"] { --color-bg-canvas: var(--white); }
body { background: var(--color-bg-canvas); }
/* ===== Case-study composition (v1.8) =====
   Header (back link, eyebrow, title, badges, summary panel, StatRow) -> 220px sticky InPageNavigation + reading column
   (>=1024px container; a horizontal strip above the content below that) -> more case studies (Card --showcase, two-up). */
html { scroll-padding-top: var(--space-16); }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
body { margin: 0; font-family: var(--font-sans); background: var(--color-bg-canvas); color: var(--color-text-primary); }
.cs { container-type: inline-size; padding-left: env(safe-area-inset-left, 0px); padding-right: env(safe-area-inset-right, 0px); }
.cs-wrap { max-width: var(--content-max-width); margin: 0 auto; padding: var(--space-6) var(--space-4) var(--space-16); }
@container (min-width: 768px) { .cs-wrap { padding: var(--space-10) var(--space-10) var(--space-24); } }

.cs-bar { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); margin-bottom: var(--space-12); }
.cs-back { display: inline-flex; align-items: center; gap: var(--space-1); }
.cs-back .pm-icon { flex: none; width: 16px; height: 16px; }

.cs-head { display: grid; gap: var(--space-5); max-width: 880px; }
.cs-head .pm-card__eyebrow { margin: 0; }
.cs-title { margin: 0; font-size: var(--type-display-lg); line-height: var(--line-display-lg); font-weight: var(--weight-display-lg); letter-spacing: var(--tracking-display-lg); font-stretch: var(--font-width-display); text-wrap: balance; }
.cs-badges { display: flex; flex-wrap: wrap; gap: var(--space-1); list-style: none; margin: 0; padding: 0; }
.cs-summary { margin-top: var(--space-10); }
.cs-summary__body { display: grid; gap: var(--space-8); }
.cs-summary + .pm-stats { margin-top: var(--space-8); }
.cs-summary__grid { display: grid; gap: var(--space-5); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .cs-summary__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-6) var(--space-8); } }
.cs-summary__grid h3 { margin: 0 0 var(--space-1); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.cs-summary__grid p { margin: 0; }
.cs-summary .pm-stats { margin-top: var(--space-2); }

.cs-body { display: grid; gap: var(--space-8); margin-top: var(--space-16); grid-template-columns: minmax(0, 1fr); }
.cs-toc { position: sticky; top: 0; z-index: 1; background: var(--color-bg-canvas); padding-block: var(--space-2); margin-inline: calc(var(--space-4) * -1); padding-inline: var(--space-4); }
@container (min-width: 1024px) {
  .cs-body { grid-template-columns: 220px minmax(0, 1fr); gap: var(--space-16); }
  .cs-toc { top: var(--space-10); align-self: start; margin: 0; padding: 0; background: none; }
}
.cs-main { min-width: 0; display: grid; gap: var(--space-24); max-width: 760px; }

.cs-section { display: grid; gap: var(--space-6); }
.cs-section > .pm-frame, .cs-section > .cs-pair, .cs-section > .cs-table-wrap { margin-block: var(--space-2); }
.cs-eyebrow { margin: 0 0 calc(var(--space-4) * -1); font-family: var(--font-meta); font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-tertiary); }
.cs-h2 { margin: 0; font-size: var(--type-h2); line-height: var(--line-h2); font-weight: var(--weight-h2); letter-spacing: var(--tracking-h2); text-wrap: balance; }
.cs-h3 { margin: var(--space-6) 0 calc(var(--space-2) * -1); font-size: var(--type-h4); line-height: var(--line-h4); font-weight: var(--weight-h4); letter-spacing: var(--tracking-h4); text-wrap: balance; }
.cs-h4 { margin: 0 0 var(--space-1); font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); }
.cs-prose { display: grid; gap: var(--space-4); max-width: var(--reading-max-width); }
.cs-prose p, .cs-iter p { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); color: var(--color-text-secondary); text-wrap: pretty; }
.cs-section .pm-panel__body p { margin: 0; }
.cs-goal { font-size: var(--type-h4) !important; line-height: var(--line-h4) !important; color: var(--color-text-primary); }

.cs-pair { display: grid; gap: var(--space-4); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .cs-pair { grid-template-columns: repeat(2, minmax(0, 1fr)); } }

.cs-steps { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-2); grid-template-columns: repeat(2, minmax(0, 1fr)); }
@container (min-width: 768px) { .cs-steps { grid-template-columns: repeat(4, minmax(0, 1fr)); } }
.cs-steps li { display: grid; gap: var(--space-2); align-content: start; padding: var(--space-3); border-radius: var(--radius-sm); background: var(--color-bg-elevated); box-shadow: 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); font-size: var(--type-body-sm); line-height: var(--line-body-sm); }

.cs-points { list-style: none; margin: 0; padding: 0; display: grid; }
.cs-points li { display: grid; grid-template-columns: var(--space-8) minmax(0, 1fr); gap: var(--space-2); padding: var(--space-4) 0; border-top: 1px solid var(--color-border-subtle); }
.cs-points li > .pm-meta-text { line-height: var(--line-body-md); }
.cs-points h4 { margin: 0 0 var(--space-1); font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); }
.cs-points p { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
@container (min-width: 768px) { .cs-points--grid { grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: var(--space-8); } }

.cs-quote { margin: var(--space-4) 0; padding-left: var(--space-6); border-left: 2px solid var(--color-border-strong); display: grid; gap: var(--space-3); }
.cs-quote blockquote { margin: 0; }
.cs-quote blockquote p { margin: 0; font-size: var(--type-h3); line-height: var(--line-h3); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h3); text-wrap: balance; }
.cs-quote figcaption { font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }

.cs-table-wrap { overflow-x: auto; border-radius: var(--radius-md); box-shadow: 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); background: var(--color-bg-elevated); }
.cs-table { width: 100%; min-width: 600px; border-collapse: collapse; font-size: var(--type-body-sm); line-height: var(--line-body-sm); }
.cs-table th { text-align: left; padding: var(--space-3) var(--space-4); font-size: var(--type-label); line-height: var(--line-label); font-weight: var(--weight-regular); color: var(--color-text-tertiary); background: var(--color-bg-surface); }
.cs-table td { vertical-align: top; padding: var(--space-4); border-top: 1px solid var(--color-border-subtle); color: var(--color-text-secondary); }
.cs-table td b { display: block; margin-bottom: var(--space-1); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.cs-table td:last-child { background: var(--color-action-selected-bg); }
.cs-table td:last-child b { color: var(--color-action-selected-text); }

.cs-iter { display: grid; gap: var(--space-4); grid-template-columns: minmax(0, 1fr); align-items: center; }
@container (min-width: 768px) { .cs-iter { grid-template-columns: minmax(0, 3fr) minmax(0, 2fr); gap: var(--space-8); } }

.cs-more { margin-top: var(--space-24); padding-top: var(--space-10); border-top: 1px solid var(--color-border-subtle); display: grid; gap: var(--space-6); }
.cs-more .cs-h2 { font-size: var(--type-h3); line-height: var(--line-h3); }
.cs-colophon { margin: var(--space-16) 0 0; }
"""

page = f'''<title>Mensio Case Study</title>
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

<div class="cs" id="top">
<div class="cs-wrap">
  <div class="cs-bar">
    <a class="pm-link cs-back" href="landing.html#work">{I["prev"]}All work</a>
    <span class="pm-tooltip-anchor">
      <button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--xs" id="cs-theme" aria-pressed="false" aria-labelledby="cs-theme-tip">{I["moon"]}</button>
      <span role="tooltip" id="cs-theme-tip" class="pm-tooltip" style="left:auto;right:0;transform:none">Dark theme</span>
    </span>
  </div>

  <header class="cs-head">
    <p class="pm-card__eyebrow"><span class="pm-meta-text">2026</span> · Mensio</p>
    <h1 class="cs-title">Redesigning Mensio’s Data Explorer for self-serve analysis</h1>
    <ul class="cs-badges" aria-label="Disciplines"><li class="pm-badge">Product design</li><li class="pm-badge">User research</li><li class="pm-badge">Analytics</li></ul>
  </header>

  <section class="pm-panel pm-panel--lg cs-summary" aria-labelledby="cs-sum-h">
    <div class="pm-panel__header"><h2 class="pm-panel__title" id="cs-sum-h">Summary</h2></div>
    <div class="pm-panel__body cs-summary__body"><div class="cs-summary__grid">
      <div><h3>Background</h3><p>Mensio tracks brand exposure across 185 TV networks and 2,000+ social handles. Data Explorer is where customers pull that data into charts.</p></div>
      <div><h3>Problem</h3><p>Data Explorer showed every metric, grouping and filter at once, so customers relied on analysts for every custom chart.</p></div>
      <div><h3>Approach</h3><p>We studied the analysts’ workflow and turned their follow-up questions into Guided Setup, a step-by-step wizard with presets.</p></div>
      <div><h3>Outcome</h3><p>Shipped in 14 weeks. Customers now build their own charts, including chart types the team never built for them before.</p></div>
    </div>
    {meta([('Collaborators', 'Enterprise Analytics team, frontend and backend engineers'), ('Timeline', '<span class="pm-meta-text">June – September 2026</span>'), ('Scope', 'User research, product design, design QA, acting PM')])}
    </div>
  </section>

  {stats([('14 wks', 'from research to ship'), ('8 → 5', 'steps from question to chart'), ('6', 'presets for common questions')])}

  <div class="cs-body">
    <nav class="pm-toc cs-toc" aria-labelledby="cs-toc-h"><p class="pm-toc__heading" id="cs-toc-h">On this page</p><ol class="pm-toc__list">{TOC}</ol></nav>
    <main class="cs-main">{BODY}</main>
  </div>

  <section class="cs-more" aria-labelledby="cs-more-h">
    <h2 class="cs-h2" id="cs-more-h">More case studies</h2>
    <ul class="pm-showcase-grid">{''.join(f'<li>{showcase(k, t, s, b, e, href="landing.html#work", more="")}</li>' for k, t, s, b, e in MORE)}</ul>
  </section>

  <p class="pm-meta-text cs-colophon">© 2026 {NAME} · Built on Paper × Midnight {VER}</p>
</div>
</div>

<script>
(function () {{
  var root = document.documentElement, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var themeBtn = document.getElementById('cs-theme');
  function isDark() {{ var t = root.getAttribute('data-theme'); return t ? t === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; }}
  function sync() {{ themeBtn.setAttribute('aria-pressed', String(isDark())); }}
  themeBtn.addEventListener('click', function () {{ root.setAttribute('data-theme', isDark() ? 'light' : 'dark'); sync(); }});
  sync();

  // Scroll-spy on the "On this page" index; the current item scrolls into view in the narrow strip
  var links = [].slice.call(document.querySelectorAll('[data-spy]')), last = null;
  function spy() {{
    var cur = links[0], line = window.innerHeight * 0.3;
    links.forEach(function (a) {{ var s = document.querySelector(a.getAttribute('href')); if (s && s.getBoundingClientRect().top < line) cur = a; }});
    if ((window.innerHeight + window.scrollY) >= document.documentElement.scrollHeight - 2) cur = links[links.length - 1];
    links.forEach(function (a) {{ if (a === cur) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); }});
    if (cur !== last) {{ last = cur; var list = cur.closest('ol'); if (list.scrollWidth > list.clientWidth) list.scrollTo({{ left: cur.offsetLeft - 16, behavior: reduce ? 'auto' : 'smooth' }}); }}
  }}
  window.addEventListener('scroll', spy, {{ passive: true }}); window.addEventListener('resize', spy); spy();
  // Focus moves to the section after a jump
  links.forEach(function (a) {{ a.addEventListener('click', function () {{ var s = document.querySelector(a.getAttribute('href')); if (s) {{ s.setAttribute('tabindex', '-1'); setTimeout(function () {{ s.focus({{ preventScroll: true }}); }}, 0); }} }}); }});
  // Other pages aren't in this prototype yet
  document.querySelectorAll(".cs-more .pm-card__title a").forEach(function (a) {{ a.addEventListener('click', function (e) {{ e.preventDefault(); }}); }});
}})();
</script>
'''
open(os.path.join(REPO, 'prototypes/mensio.html'), 'w').write(page)
print(len(page))
