"""Procense Digital Forms application case study, on the same structure as the revised Mensio case study (casestudy.render).
Content: Serena's Framer case study (project-detail-procense-digital-forms-application, read 2026-11-16), rewritten in
this site's voice. Media: first-pass mockups drawn in HTML (no Framer images were available): the paper QC form and
three tablet screens. They are labelled as reconstructed and use Procense's navy and blue only as project art.
Run: python3 design-system/tools/previews/src/casestudy_procense.py  ->  prototypes/procense.html
"""
import casestudy as C
from casestudy import I, S, section, lede, panel, points, stats
from lib import _l

# ---------- media: paper form (before) ----------
PAIN = [  # from Serena's Framer case study
    ('Critical checks didn’t stand out', 'Only red, bold text marked a must-pass test, which is easy to miss when you’re working fast.', 3.4, 35.0),
    ('The same fields, over and over', 'Every row asked for the date and time again: slow to fill in, and an easy place to slip up.', 3.4, 56.0)]
def paper_form():
    head = ['Date', 'Time', 'Test', 'Spec', 'Result', 'Initials']
    rows = [('pH', '6.5 – 7.5'), ('Viscosity (cP)', '1,200 – 1,500'), ('Specific gravity', '1.02 – 1.06'), ('Appearance', 'Clear, no particulates'),
            ('Moisture (%)', '≤ 0.5'), ('Odor', 'Characteristic')]
    tr = ''.join(f'<tr><td>__/__/__</td><td>__:__</td><td{" class=crit" if i in (0, 2) else ""}>{t}</td><td>{sp}</td><td></td><td></td></tr>' for i, (t, sp) in enumerate(rows))
    pins = ''.join(f'<button type="button" class="pr-pin" style="left:{x}%;top:{y}%" data-pain="{n}" aria-pressed="false" aria-label="Pain point {n + 1}: {t}">{n + 1}</button>'
                   for n, (t, d, x, y) in enumerate(PAIN))
    notes = ''.join(f'<template data-pain-note="{n}">{t}|{d}</template>' for n, (t, d, x, y) in enumerate(PAIN))
    return ('<div class="pr-pain" data-pains>'
            '<div class="pr-paper" data-active="">'
            '<div aria-hidden="true"><p class="pr-paper__t">QC BATCH PERFORMANCE</p>'
            '<p class="pr-paper__m">Batch No. ________ &nbsp; MO No. ________ &nbsp; Product ______________</p>'
            '<table><colgroup><col style="width:15%"><col style="width:11%"><col style="width:23%"><col style="width:23%"><col style="width:14%"><col style="width:14%"></colgroup><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + f'</tr></thead><tbody>{tr}</tbody></table>'
            '<p class="pr-paper__m">Reviewed by ____________ &nbsp; Date __/__/__ &nbsp; Signature ____________</p>'
            f'</div>{pins}</div>{notes}'
            '<div class="pr-note" aria-live="polite"><p class="pr-note__t" data-note-t>Two pain points</p><p class="pr-note__d" data-note-d>Hover over or tap a number on the form to see what slowed operators down.</p></div>'
            '</div>')

# ---------- media: tablet screens (after) ----------
STEPS = ['Batch information', 'SOPs & ingredients', 'QC tests']
def tablet(active, body, label):
    step = ''.join(f'<li class="{"is-on" if i == active else ("is-done" if i < active else "")}"><span>{"✓" if i < active else i + 1}</span>{t}</li>' for i, t in enumerate(STEPS))
    return (f'<div class="pr-tab" role="img" aria-label="{label}"><div class="pr-scr" aria-hidden="true">'
            '<div class="pr-bar"><b>Procense</b><span>Digital Forms</span><i>Batch A-2291 · Line 2</i></div>'
            f'<ol class="pr-steps">{step}</ol><div class="pr-body">{body}</div></div></div>')

def field(label, value, tag='', icon='', wide=False):
    return (f'<div class="pr-f{" pr-f--wide" if wide else ""}"><span class="pr-f__l">{label}</span>'
            f'<span class="pr-f__v">{icon}{value}{f"<em>{tag}</em>" if tag else ""}</span></div>')

CAL = '<svg viewBox="0 0 24 24"><path d="M8 2v4M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/></svg>'
CLK = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
PEN = '<svg viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.4 3.6a2.1 2.1 0 1 1 3 3L7 19l-4 1 1-4Z"/></svg>'

def screen1():
    body = ('<p class="pr-h">Batch information</p><div class="pr-grid">'
            + field('Batch number', 'A-2291') + field('MO number', 'MO-10482') + field('Product', 'Surfactant blend 40')
            + field('Sample type', 'Finished product ▾') + field('Date', '06/14/2023', 'Auto', CAL) + field('Time', '09:42', 'Auto', CLK)
            + field('Operator', 'Signed as J. Rivera', 'Auto', PEN, True) + '</div><div class="pr-foot"><span class="pr-btn">Next</span></div>')
    return tablet(0, body, 'Reconstructed tablet screen, Batch information: batch and MO numbers typed in, date, time and operator signature filled in automatically')

def screen2():
    sop = ('<div class="pr-sop"><p class="pr-sop__n">SOP 3.2 · Charge the reactor</p><ol><li>Confirm the vessel is clean and dry.</li>'
           '<li>Add water, then start agitation at low speed.</li><li><b>Keep the temperature below 40 °C while adding the surfactant.</b></li>'
           '<li>Add the preservative once the blend is uniform.</li><li>Hold for 15 minutes, then pull a sample for QC.</li></ol></div>')
    ing = ('<div class="pr-ing"><p class="pr-ing__h">Ingredients</p>' + ''.join(
        f'<div class="pr-ing__r"><span>{n}</span><span>{t}</span><span class="pr-in">{a}</span><span class="pr-ok">{"✓" if a else ""}</span></div>'
        for n, t, a in [('Deionized water', '420.0 kg', '420.2'), ('Surfactant LAS-96', '180.0 kg', '179.8'), ('Preservative P-2', '2.5 kg', ''), ('Fragrance F-11', '1.2 kg', ''), ('Citric acid (50%)', 'As needed', '')]) + '</div>')
    return tablet(1, f'<div class="pr-two">{sop}{ing}</div><div class="pr-foot"><span class="pr-btn pr-btn--2">Back</span><span class="pr-btn">Next</span></div>',
                  'Reconstructed tablet screen, SOPs and ingredients: the SOP step in a blue block with the critical instruction in bold, and an ingredients list in grey with target and actual weights')

def screen3():
    rows = [('pH', '6.5 – 7.5', '7.1', 'Pass'), ('Viscosity (cP)', '1,200 – 1,500', '1,340', 'Pass'), ('Specific gravity', '1.02 – 1.06', '1.07', 'Fail'), ('Appearance', 'Clear', 'Clear', 'Pass'), ('Moisture (%)', '≤ 0.5', '0.3', 'Pass'), ('Odor', 'Characteristic', 'Characteristic', 'Pass')]
    tb = ''.join(f'<div class="pr-qc__r"><span>{t}</span><span>{sp}</span><span class="pr-in">{r}</span><span class="pr-pf pr-pf--{st.lower()}">{st}</span></div>' for t, sp, r, st in rows)
    body = ('<p class="pr-h">QC tests</p><div class="pr-qc"><div class="pr-qc__r pr-qc__hd"><span>Test</span><span>Spec</span><span>Result</span><span></span></div>' + tb + '</div>'
            '<div class="pr-foot"><span class="pr-sign">' + PEN + 'Approved by M. Chen · 11:18 · Auto</span><span class="pr-btn">Submit batch</span></div>')
    return tablet(2, body, 'Reconstructed tablet screen, QC tests: each test with its spec, the result and a pass or fail flag, and the approval signed automatically')

# Small thumbnails for the solution cards: close-ups of the reconstructed tablet UI (project art)
THUMBS = {
    # A complete three-step wizard: each step goes active, then done, and the line fills between them
    'flow': ('<div class="pr-th pr-th--flow">'
             + '<i class="pr-l pr-l1"><u></u></i><i class="pr-l pr-l2"><u></u></i>'
             + ''.join(f'<span class="pr-c pr-c{n}"><em>{n}</em><strong>✓</strong></span>' for n in (1, 2, 3))
             + '<b class="pr-t1">Batch details</b><b class="pr-t2">SOP</b><b class="pr-t3">QA checks</b></div>'),
    # Values appear on their own: date and time from the clock, the verifier from the operator's login
    'auto': ('<div class="pr-th pr-th--auto">'
             '<div class="pr-af"><span class="pr-lbl">Date</span><div class="pr-th__f"><span class="pr-v pr-v1">06/14/2023</span></div></div>'
             '<div class="pr-af"><span class="pr-lbl">Time</span><div class="pr-th__f"><span class="pr-v pr-v2">09:42</span></div></div>'
             '<div class="pr-af pr-af--w"><span class="pr-lbl">Verified by</span><div class="pr-th__f"><span class="pr-v pr-v3">J. Rivera, Operator</span><em class="pr-v pr-v3">Auto</em></div></div>'
             '</div>'),
    # The SOP's requirements get ticked off one by one
    'sop': ('<div class="pr-th pr-th--sop"><p>SOP 3.2 · Charge the reactor</p>'
            '<span class="pr-ck pr-k1"><i></i>Vessel clean and dry</span>'
            '<span class="pr-ck pr-k2"><i></i>Water added, mixing</span>'
            '<span class="pr-ck pr-k3"><i></i><b>Kept below 40 °C</b></span></div>'),
}

def feature_cards(rows, cols=3):
    """Solution features as design-system cards (Card --outlined), lifted so they stand out. rows: (icon or '', title, text)."""
    anim = any(ic for ic, t, d in rows)
    return (f'<div class="pr-cards-wrap"{" data-anim" if anim else ""}><ul class="pr-cards pr-cards--{cols}">' + ''.join(
        f'<li><article class="pm-card pm-card--outlined pr-card">'
        + (f'<div class="pr-card__thumb" aria-hidden="true">{THUMBS[ic]}</div>' if ic else '')
        + f'<h4 class="pm-card__title">{t}</h4><p class="pm-card__summary">{d}</p></article></li>' for ic, t, d in rows) + '</ul>'
        + (f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--xs pr-anim-btn" aria-pressed="false" data-anim-toggle>{I["pause"]}<span>Pause animations</span></button>' if anim else '')
        + '</div>')

def items(rows, grid=False):
    """Title + description list, no numbering (Serena, 2026-11-16)."""
    return (f'<ul class="cs-points cs-points--plain{" cs-points--grid" if grid else ""}">'
            + ''.join(f'<li><div><h4>{t}</h4><p>{d}</p></div></li>' for t, d in rows) + '</ul>')

# Interview insights. DRAFT: written to fill out the section (Serena asked for illustrative insights, 2026-11-16);
# replace with real interview notes before publishing. Each one links to the design goal it shaped.
# Interview insights (DRAFT, written at Serena's request; replace with real notes) and the goal each one set.
INSIGHT_GOALS = [  # insight title, insight, goal title, goal
    ('Forms get filled in mid-task', 'Operators record values while they weigh ingredients, mix and take samples, often wearing gloves.',
     'Fewer taps', 'Every tap removed is one less chance to make a mistake.'),
    ('The same values are written again and again', 'Date, time and initials go on every row. Most errors were copying slips that only surfaced in review.',
     'Built-in guardrails', 'Fields fill themselves in where they can, and the same parts repeat across forms.'),
    ('The platform already knows the batch', 'Batch numbers, products and operators already live in Procense, yet operators copied them onto paper by hand.',
     'At home in Procense', 'The forms draw on what the platform already knows and work like the rest of it.'),
    ('Every record has to survive an audit', 'Auditors check critical limits and sign-offs first. Every value needs a who and a when.',
     'Faster, not looser', 'Speed can’t come at the cost of the checks the forms exist for.'),
]
def insight_goals():
    """One graphic: each interview insight on the left, the design goal it set on the right."""
    arrow = f'<span class="pr-ig__arrow" aria-hidden="true">{_l("arrow-right")}</span>'
    rows = ''.join(
        f'<li class="pr-ig__row"><div class="pr-ig__in"><p class="pr-ig__k">What I learned</p><h4>{it}</h4><p>{idesc}</p></div>{arrow}'
        f'<div class="pm-card pm-card--outlined pr-ig__goal"><p class="pr-ig__k">Design goal</p><h4 class="pm-card__title">{gt}</h4><p class="pm-card__summary">{gd}</p></div></li>'
        for it, idesc, gt, gd in INSIGHT_GOALS)
    return (f'<figure class="pr-ig"><div class="pr-ig__head" aria-hidden="true"><span>What I learned</span><span></span><span>Design goal</span></div>'
            f'<ol class="pr-ig__list">{rows}</ol>'
            '<figcaption class="pm-meta-text">Draft insights, to replace with interview notes.</figcaption></figure>')

# The paper batch workflow, with the points where errors creep in (Serena, 2026-11-16).
FLOW = [  # title, who, what happens, error risk
    ('Weigh ingredients', 'Operator', 'Weighs each ingredient and writes the actual amount next to the target.', 'Misread scales and transposed digits'),
    ('Follow the steps', 'Operator', 'Works through the instructions in a separate binder, initialling each step.', 'Skipped or out-of-order steps'),
    ('Record conditions', 'Operator', 'Writes down temperatures, times and mixing speeds as the batch runs.', 'Out-of-range values go unnoticed'),
    ('Run quality tests', 'Operator', 'Tests samples and copies each result onto the quality form.', 'Results copied wrong or left blank'),
    ('Hand off the forms', 'Operator to QA', 'Carries the signed paper forms to QA and engineering.', 'Lost pages and missing signatures'),
    ('Review and approve', 'QA and engineers', 'Checks every entry by hand and sends mistakes back to the floor.', 'Corrections restart the loop and delay release'),
]
def flow():
    """Fig. 1: plays through the six steps on its own; any step can be picked. The note shows the step on the left
    and its risk, in a filled and outlined box, on the right. Phones get a list with every step's details."""
    kind = lambda i: 'Delay risk' if i == len(FLOW) - 1 else 'Error risk'
    risk = lambda label, text, attrs='': (f'<div class="pr-flow__risk"{attrs}><span class="pr-flow__rl">{S["warning"]}<span data-fn-rl>{label}</span></span>'
                                          f'<span class="pr-flow__rt" data-fn-rt>{text}</span></div>')
    steps = ''.join(
        f'<li class="pr-flow__s"><button type="button" class="pr-flow__b" data-step="{i}" aria-pressed="{"true" if i == 0 else "false"}">'
        f'<span class="pr-flow__n" aria-hidden="true"><em>{i + 1}</em><strong>✓</strong></span><span class="pr-flow__t">{t}</span></button>'
        f'<div class="pr-flow__d"><p class="pm-meta-text">{who}</p><p>{d}</p>{risk(kind(i), r)}</div></li>'
        for i, (t, who, d, r) in enumerate(FLOW))
    notes = ''.join(f'<template data-step-note="{i}">{t}|{who}|{d}|{r}|{kind(i)}</template>' for i, (t, who, d, r) in enumerate(FLOW))
    t0, who0, d0, r0 = FLOW[0]
    return ('<div class="pr-flow" data-flow>'
            f'<ol class="pr-flow__list" aria-label="A paper batch, step by step"><span class="pr-flow__prog" aria-hidden="true"></span>{steps}</ol>{notes}'
            '<div class="pr-flow__note" aria-live="off" data-fn-live>'
            f'<div class="pr-flow__txt"><p class="pm-meta-text" data-fn-w>Step 1 of {len(FLOW)} · {who0}</p><p class="pr-note__t" data-fn-t>{t0}</p><p class="pr-note__d" data-fn-d>{d0}</p></div>'
            f'{risk(kind(0), r0, " data-fn-r")}</div>'
            f'<div class="pr-flow__bar"><button type="button" class="pm-btn pm-btn--ghost pm-btn--xs" aria-pressed="false" data-flow-toggle>{I["pause"]}<span>Pause</span></button></div>'
            '</div>')

def shot(art, cap, n):
    return (f'<figure class="pm-frame"><div class="pm-frame__stage pr-stage">{art}</div>'
            f'<figcaption class="pm-frame__caption"><span class="pm-frame__index">Fig. {n:02d}</span><span>{cap}</span></figcaption></figure>')

# ---------- content ----------
SECTIONS = [('overview', 'Overview'), ('problem', 'The problem'), ('discovery', 'Approach'), ('goals', 'Design goals'), ('ideation', 'Ideation'),
            ('tablet', 'Tablet-first'), ('solution', 'The solution'), ('feedback', 'User feedback'), ('reflection', 'Impact &amp; reflection')]

STATS_FULL = [('10%', 'Faster batch execution, from weighing ingredients to quality sign-off'), ('100%', 'Automated traceability, so audits take less digging'), ('100%', 'Data accuracy, with nothing copied over from paper')]

BODY = ''.join([
    section('overview', 'Overview', 'We replaced paper batch records with one guided tablet flow.',
        lede('Procense’s integrated platform helps chemical manufacturers run and monitor production, but every batch was still recorded on paper. I designed the Digital Forms application to change that, moving quality checks and manufacturing steps onto the tablets operators already carry.',
             'Batches now run 10% faster, every record is traceable and accurate, and operators spend their time on the batch instead of the paperwork.')
        + stats(STATS_FULL, ' pm-stats--sm cs-stats')),

    section('problem', 'The problem', 'Every batch was recorded by hand, then checked on paper.',
        lede('In many chemical plants, each batch is recorded on two paper forms: one for the manufacturing steps and one for the quality checks. Once complete, the forms go to directors and engineers, who decide whether the batch meets the standard. The process is slow, invites human error and holds up decisions on the floor.')
        + shot(flow(), 'A paper batch, step by step. Five of the six steps are written by hand, and each is a chance for error.', 1)
        + stats([('~150', 'Handwritten entries in one batch record'), ('1–4%', 'Chance any handwritten entry is inaccurate'), ('1–3 days', 'From the end of a batch to its approval')], ' pm-stats--sm cs-stats')
        + '<p class="pm-meta-text pr-draft">Estimates for a typical paper batch record, for illustration.</p>'
        + lede('One North Star kept product, design and business aligned.')
        + f'<section class="pr-ns" aria-labelledby="p-ns"><p class="pr-ns__label" id="p-ns">{_l("compass")}Our North Star</p>'
          '<p class="pr-ns__text">Streamline batch manufacturing by digitizing its forms, while keeping them intuitive for operators used to filling them in by hand.</p></section>'
        + '<h3 class="cs-h3">The solution, in short</h3>'
        + lede('A guided tablet flow, built into the Procense platform. It gives operators a faster, more reliable way to record each batch, and still feels as familiar as paper.')
        + feature_cards([('flow', 'Two forms, one flow', 'Batch details, the SOP and QA checks in three steps, in the order operators work.'),
                         ('auto', 'Fields that fill themselves', 'Dates, times and signatures fill in automatically, so there’s less to write and less to get wrong.'),
                         ('sop', 'Instructions in the form', 'Each step’s instructions and critical limits sit right where the data is entered.')])),

    section('discovery', 'Approach', 'I started by taking the paper forms apart.',
        lede('The forms captured a great deal of data, but made it hard to spot what mattered and slow to fill in.')
        + shot(paper_form(), 'The paper quality form, reconstructed. Hover over or tap a number to see each pain point.', 2)
        + '<h3 class="cs-h3">Then I learned how the forms are used on the floor.</h3>'
        + lede('I interviewed Procense’s co-founder, a former process engineer who has both written and filled in these forms. Four insights stood out, and each one set a design goal.')),

    section('goals', 'Design goals', 'Four things I learned became four goals.',
        lede('Each insight from the floor set one goal for the Digital Forms application, so every design decision traced back to how operators really work.')
        + insight_goals()),

    section('ideation', 'Ideation', 'I explored how crowded tables could become simple steps.',
        lede('I studied how other products turn paper forms into software and organise large tables, then sketched layouts and noted what each form needed.')
        + shot(f'<div class="pm-media pm-media--16x10 pr-well" role="img" aria-label="Image to come: annotated layout sketches"><div class="pm-media__fallback">{I["image"]}<span>Image to come</span><span>Annotated layout sketches</span></div></div>', 'Early sketches of the digital quality and manufacturing forms.', 3)),

    section('tablet', 'Tablet-first', 'We designed for desktop. The floor ran on tablets.',
        '<div class="cs-pair">'
        + panel('What we assumed', '<p>Operators would use desktops or laptops, like the rest of Procense’s web-first platform.</p>', ' pm-panel--tonal', 'p-assumed')
        + panel('What we found', '<p>Operators carry tablets as they work through each step and run quality tests on the floor.</p>', '', 'p-found')
        + '</div>'
        + lede('That discovery reshaped the project. We moved to a tablet-first design with new layouts and a new flow. The smaller screen meant breaking long forms into steps, which adds a tap or two, but in return operators got larger text, cleaner sections and a flow that matches how they actually work.')),

    section('solution', 'The solution', 'Two paper forms became one guided flow.',
        lede('The final design merges both forms into three steps: batch details, then the manufacturing steps and ingredients, then the quality tests. Each screen shows only what that step needs, so operators can keep their attention on the batch.')
        + shot(screen1(), 'Batch information, the first step. Date, time and signature fill in on their own.', 4)
        + shot(screen2(), 'Manufacturing steps and ingredients. Instructions in blue, ingredients in grey, critical conditions in bold.', 5)
        + shot(screen3(), 'Quality tests, the last step. Each result is checked against its target range as it’s entered.', 6)
        + feature_cards([('', 'Fields that fill themselves', 'Date and time fill in automatically, and signatures come from the operator’s login.'),
                         ('', 'The same patterns everywhere', 'Buttons and layouts behave the same at every step.'),
                         ('', 'Clear sections', 'Colour sets them apart: blue for instructions, grey for ingredients.'),
                         ('', 'Familiar icons', 'Icons like date and time mark the inputs that are required.'),
                         ('', 'Built for dense data', 'One left-aligned column that’s easy to read and move through.'),
                         ('', 'Instructions in the form', 'The steps for each stage sit right inside the form, so there’s no binder to check.'),
                         ('', 'Critical steps stand out', 'Conditions that can ruin a batch are bold and hard to miss.')], cols=2)),

    section('feedback', 'User feedback', 'A QA manager’s review cut even more typing.',
        lede('We reviewed the first design of the quality test form with a QA manager, section by section, and their feedback led to two changes.')
        + '<div class="cs-pair">'
        + panel('What we heard', '<p>Operators still typed too much, and choosing batch and order numbers from a list added unnecessary steps.</p>', ' pm-panel--tonal', 'p-heard')
        + panel('What we changed', '<p>More fields now fill in automatically from the sample type, and batch and order numbers are typed in directly.</p>', '', 'p-changed')
        + '</div>'),

    section('reflection', 'Impact &amp; reflection', 'Operators now record each batch as they work.',
        lede('Moving from paper to the Digital Forms application streamlined the whole batch process. Operators record data as they go instead of copying it later, reviewers see it as soon as it’s entered, and every value carries who entered it and when. With the paperwork out of the way, teams can focus on running safe, consistent batches.')
        + stats(STATS_FULL, ' pm-stats--sm cs-stats')
        + '<h3 class="cs-h3">What I learned</h3>'
        + '<div class="cs-pair">'
        + panel('Design for the device in their hands', '<p>Learning that operators carry tablets changed every layout decision, and made the forms easier to use, not harder.</p>', ' pm-panel--tonal', 'p-l1')
        + panel('Modernize what people already know', '<p>Keeping the forms familiar, rather than reinventing them, let the plants move faster without losing the checks that keep every batch safe.</p>', ' pm-panel--tonal', 'p-l2')
        + '</div>'),
])

HEADER = f'''  <header class="cs-head">
    <ul class="cs-badges" aria-label="Status and disciplines"><li class="pm-badge pm-badge--success">{S["success"]}Shipped</li><li class="pm-badge">Product design</li><li class="pm-badge">End-to-end</li><li class="pm-badge">Tablet</li></ul>
    <h1 class="cs-title">Digitizing manufacturing QA forms to increase batch execution speed by 10%</h1>
  </header>

  <section class="cs-facts" aria-label="Project details"><dl class="cs-facts__list">
    <div><dt>Role</dt><dd>Product designer</dd></div>
    <div><dt>Team</dt><dd>1 PM</dd><dd>1 designer</dd><dd>3 engineers</dd></div>
    <div><dt>Timeline</dt><dd>2023</dd></div>
    <div><dt>Skills</dt><dd>User research</dd><dd>Product design</dd><dd>Prototyping</dd></div>
  </dl></section>'''

TLDR = f'''      <dl class="cs-tldr__rows">
        <div class="cs-tldr__row"><dt>Background</dt><dd>Chemical plants record every batch on paper forms that managers then review by hand.</dd></div>
        <div class="cs-tldr__row"><dt>Problem</dt><dd>Paper slowed decisions on the floor, and crowded, repetitive forms made mistakes easy.</dd></div>
        <div class="cs-tldr__row"><dt>Approach</dt><dd>I studied the forms and how operators work, then designed the Digital Forms application for the tablets they carry.</dd></div>
        <div class="cs-tldr__row"><dt>Outcome</dt><dd>Two paper forms became one tablet flow, so plants move faster and teams can focus on the work on the floor.</dd></div>
      </dl>
      {stats([('10%', 'Faster batch execution'), ('100%', 'Automated traceability'), ('100%', 'Data accuracy')], ' pm-stats--sm cs-tldr__stats')}'''

JS = r"""
  // Solution card animations loop; the button pauses them (WCAG 2.2.2), and they also rest while off screen
  document.querySelectorAll('[data-anim]').forEach(function (w) {
    var btn = w.querySelector('[data-anim-toggle]'), user = false, PAUSE = '<svg class="pm-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="14" y="4" width="4" height="16" rx="1"/><rect x="6" y="4" width="4" height="16" rx="1"/></svg>', PLAY = '<svg class="pm-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><polygon points="6 3 20 12 6 21 6 3"/></svg>';
    function sync() { btn.setAttribute('aria-pressed', String(user)); btn.innerHTML = (user ? PLAY : PAUSE) + '<span>' + (user ? 'Play animations' : 'Pause animations') + '</span>'; }
    btn.addEventListener('click', function () { user = !user; w.classList.toggle('is-paused', user); sync(); });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { if (!user) w.classList.toggle('is-paused', !es[0].isIntersecting); }).observe(w);
    sync();
  });

  // Fig. 1 batch workflow: plays through the steps on its own (not with reduced motion, and only in the six-across layout).
  // Hover, focus or click a step to see it: hovering and focus pause the tour, a click stops it on that step.
  // The button pauses and resumes (WCAG 2.2.2); it also rests while off screen. Announcements start once someone interacts.
  document.querySelectorAll('[data-flow]').forEach(function (w) {
    var btns = [].slice.call(w.querySelectorAll('[data-step]')), wEl = w.querySelector('[data-fn-w]'), t = w.querySelector('[data-fn-t]'), d = w.querySelector('[data-fn-d]');
    var r = w.querySelector('[data-fn-r]'), live = w.querySelector('[data-fn-live]'), tog = w.querySelector('[data-flow-toggle]');
    var notes = [].map.call(w.querySelectorAll('template[data-step-note]'), function (x) { return x.innerHTML.split('|'); });
    var cur = 0, stopped = false, hold = false, offscreen = false, timer = null, STEP = 3500, PAUSE = '<svg class="pm-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="14" y="4" width="4" height="16" rx="1"/><rect x="6" y="4" width="4" height="16" rx="1"/></svg>', PLAY = '<svg class="pm-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><polygon points="6 3 20 12 6 21 6 3"/></svg>';
    var prog = w.querySelector('.pr-flow__prog'), body = [w.querySelector('.pr-flow__txt'), r], N = notes.length;
    // The line runs from step 1's centre; at step i it reaches step i's centre (i / N of the list's width)
    function line(frac, ms, ease) { prog.style.transition = reduce ? 'none' : 'width ' + ms + 'ms ' + ease; prog.style.width = (frac / N * 100) + '%'; }
    function show(i, fill) {
      var changed = i !== cur; cur = i;
      btns.forEach(function (b, j) { b.setAttribute('aria-pressed', String(j === i)); b.classList.toggle('is-done', j < i); });
      var n = notes[i]; wEl.textContent = 'Step ' + (i + 1) + ' of ' + N + ' · ' + n[1]; t.textContent = n[0]; d.textContent = n[2];
      r.querySelector('[data-fn-rl]').textContent = n[4]; r.querySelector('[data-fn-rt]').textContent = n[3];
      line(i, 450, 'cubic-bezier(.22,1,.36,1)');
      if (changed && !reduce && body[0].animate) body.forEach(function (el, k) { el.animate([{ opacity: 0, transform: 'translateY(6px)' }, { opacity: 1, transform: 'none' }], { duration: 380, delay: k * 60, easing: 'cubic-bezier(.22,1,.36,1)', fill: 'backwards' }); });
      // While the tour runs, the line keeps creeping toward the next step, arriving just as it opens
      if (fill && i < N - 1) setTimeout(function () { if (cur === i && canRun()) line(i + 1, STEP - 500, 'linear'); }, 460);
    }
    function wide() { return w.querySelector('.pr-flow__note').offsetParent !== null; }
    function canRun() { return !reduce && !stopped && !hold && !offscreen && wide(); }
    function tick() { clearTimeout(timer); if (!canRun()) { line(cur, 300, 'ease-out'); return; } if (cur < N - 1) setTimeout(function () { if (canRun()) line(cur + 1, STEP - 500, 'linear'); }, 460); timer = setTimeout(function () { if (canRun()) show((cur + 1) % N); tick(); }, STEP); }
    function syncBtn() { tog.setAttribute('aria-pressed', String(stopped)); tog.innerHTML = (stopped ? PLAY : PAUSE) + '<span>' + (stopped ? 'Play' : 'Pause') + '</span>'; }
    function interact() { live.setAttribute('aria-live', 'polite'); }
    btns.forEach(function (b, i) {
      b.addEventListener('mouseenter', function () { hold = true; show(i); tick(); });
      b.addEventListener('focus', function () { hold = true; interact(); show(i); tick(); });
      b.addEventListener('click', function () { stopped = true; interact(); show(i); syncBtn(); tick(); });
    });
    w.querySelector('.pr-flow__list').addEventListener('mouseleave', function () { hold = false; tick(); });
    w.addEventListener('focusout', function (e) { if (!w.contains(e.relatedTarget)) { hold = false; tick(); } });
    tog.addEventListener('click', function () { stopped = !stopped; interact(); syncBtn(); tick(); });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { offscreen = !es[0].isIntersecting; tick(); }).observe(w);
    window.addEventListener('resize', tick);
    if (reduce) tog.hidden = true;
    syncBtn(); tick();
  });

  // Fig. 1 pain points: hover, focus or tap a number to show its note under the form and highlight that part of the form
  document.querySelectorAll('[data-pains]').forEach(function (w) {
    var paper = w.querySelector('.pr-paper'), pins = [].slice.call(w.querySelectorAll('[data-pain]')), t = w.querySelector('[data-note-t]'), d = w.querySelector('[data-note-d]');
    var notes = [].map.call(w.querySelectorAll('template[data-pain-note]'), function (x) { return x.innerHTML.split('|'); });
    var base = [t.textContent, d.textContent], pinned = -1;
    function show(i) {
      pins.forEach(function (p, j) { p.setAttribute('aria-pressed', String(j === i)); });
      paper.setAttribute('data-active', i < 0 ? '' : String(i + 1));
      t.textContent = i < 0 ? base[0] : notes[i][0]; d.textContent = i < 0 ? base[1] : notes[i][1];
    }
    pins.forEach(function (p, i) {
      p.addEventListener('mouseenter', function () { show(i); });
      p.addEventListener('focus', function () { show(i); });
      p.addEventListener('click', function () { pinned = pinned === i ? -1 : i; show(pinned < 0 ? i : pinned); });
    });
    paper.addEventListener('mouseleave', function () { show(pinned); });
    w.addEventListener('focusout', function (e) { if (!w.contains(e.relatedTarget)) show(pinned); });
  });
"""

CSS = r"""
/* Body numbers share a top line even when a label wraps (as in the TL;DR) */
.cs-stats .pm-stats__item { justify-content: flex-end; }
/* Figure stages a step lighter on this page (surface instead of sunken) */
.pm-frame__stage { background: var(--color-bg-surface); }
.pr-flow__n { --ring: var(--color-bg-surface); }
/* Feature cards: Card --outlined, lifted (shadow-sm) so they stand out; static, so no hover change */
.pr-cards { container-type: inline-size; list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-4); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 600px) { .pr-cards--3 { grid-template-columns: repeat(3, minmax(0, 1fr)); } .pr-cards--2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.pr-cards > li { display: flex; }
.pr-card.pm-card--outlined, .pr-card.pm-card--outlined:hover { flex: 1; padding: var(--space-5); gap: var(--space-2); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); }
.pr-card .pm-card__title { font-size: var(--type-body-md); line-height: var(--line-body-md); letter-spacing: 0; }
.pr-card .pm-card__summary { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); text-wrap: pretty; }
.pr-card.pm-card--outlined, .pr-card.pm-card--outlined:hover { padding: var(--space-3) var(--space-3) var(--space-5); }
.pr-card .pm-card__title, .pr-card .pm-card__summary { padding-inline: var(--space-2); }
/* Thumbnail: a close-up of the tablet UI on the app's own light background in both themes (project art; nested radius = outer - padding) */
.pr-card__thumb { aspect-ratio: 16 / 10; margin-bottom: var(--space-3); border-radius: var(--radius-sm); background: #F6F7F9; box-shadow: inset 0 0 0 1px var(--color-border-subtle); container-type: inline-size; overflow: hidden; display: grid; place-items: center; }
.pr-th { width: 84%; font-family: var(--font-sans); font-size: 4.6cqw; line-height: 1.3; color: #1B2026; }
/* Default styles are the finished state (also what reduced motion shows); the loops run only without reduced motion */
/* Stepper */
.pr-th--flow { position: relative; display: grid; grid-template-columns: repeat(3, 1fr); row-gap: 3cqw; justify-items: center; }
.pr-c { position: relative; z-index: 1; display: grid; place-items: center; width: 11cqw; height: 11cqw; border-radius: 50%; background: #E6F0FF; color: #2483FF; font-size: 4.6cqw; font-weight: 600; }
.pr-c em, .pr-c strong { grid-area: 1 / 1; font-style: normal; }
.pr-c em { opacity: 0; } .pr-c strong { opacity: 1; }
.pr-l { position: absolute; top: 5.5cqw; height: 1px; width: calc(33.33% - 11cqw); background: #C9CED6; }
.pr-l1 { left: calc(16.67% + 5.5cqw); } .pr-l2 { left: calc(50% + 5.5cqw); }
.pr-l u { display: block; height: 100%; width: 100%; background: #2483FF; }
.pr-th--flow b { font-weight: 400; color: #4B5563; text-align: center; white-space: nowrap; }
.pr-c1 { grid-column: 1; } .pr-c2 { grid-column: 2; } .pr-c3 { grid-column: 3; }
.pr-t1 { grid-column: 1; } .pr-t2 { grid-column: 2; } .pr-t3 { grid-column: 3; }
/* Auto-filled fields */
.pr-th--auto { display: grid; grid-template-columns: 1fr 1fr; gap: 2.6cqw 3cqw; }
.pr-af { display: grid; gap: 1cqw; min-width: 0; } .pr-af--w { grid-column: 1 / -1; }
.pr-lbl { font-size: 3.8cqw; color: #4B5563; }
.pr-th__f { display: flex; align-items: center; gap: 2cqw; min-height: 9cqw; padding: 0 3cqw; border-radius: 1.6cqw; background: #FFFFFF; box-shadow: inset 0 0 0 1px #D6DAE1; white-space: nowrap; overflow: hidden; }
.pr-th__f em { margin-left: auto; font-style: normal; font-size: 3.8cqw; padding: .4cqw 2cqw; border-radius: 1.2cqw; background: #E6F0FF; color: #1559C9; }
/* SOP checklist */
.pr-th--sop { display: grid; gap: 2.2cqw; padding: 4cqw; border-radius: 2cqw; background: #E6F0FF; border-left: 1.4cqw solid #2483FF; }
.pr-th--sop p { margin: 0 0 .6cqw; font-weight: 600; color: #1559C9; }
.pr-ck { display: flex; align-items: center; gap: 2.4cqw; }
.pr-ck b { font-weight: 600; }
.pr-ck i { flex: none; display: grid; place-items: center; width: 6cqw; height: 6cqw; border-radius: 1.2cqw; background: #2483FF; box-shadow: inset 0 0 0 1px #2483FF; }
.pr-ck i::after { content: ""; width: 1.6cqw; height: 3cqw; margin-top: -.6cqw; border: solid #FFFFFF; border-width: 0 .7cqw .7cqw 0; transform: rotate(45deg); }
@media (prefers-reduced-motion: no-preference) {
  .pr-c1 { animation: pr-c1 7s infinite; } .pr-c2 { animation: pr-c2 7s infinite; } .pr-c3 { animation: pr-c3 7s infinite; }
  .pr-c1 em { animation: pr-n1 7s infinite; } .pr-c1 strong { animation: pr-d1 7s infinite; }
  .pr-c2 em { animation: pr-n2 7s infinite; } .pr-c2 strong { animation: pr-d2 7s infinite; }
  .pr-c3 em { animation: pr-n3 7s infinite; } .pr-c3 strong { animation: pr-d3 7s infinite; }
  .pr-l1 u { animation: pr-l1 7s infinite; } .pr-l2 u { animation: pr-l2 7s infinite; }
  .pr-t1 { animation: pr-t1 7s infinite; } .pr-t2 { animation: pr-t2 7s infinite; } .pr-t3 { animation: pr-t3 7s infinite; }
  .pr-v1 { animation: pr-v1 6s infinite; } .pr-v2 { animation: pr-v2 6s infinite; } .pr-v3 { animation: pr-v3 6s infinite; }
  .pr-k1 i { animation: pr-k1 6s infinite; } .pr-k2 i { animation: pr-k2 6s infinite; } .pr-k3 i { animation: pr-k3 6s infinite; }
  .pr-k1 i::after { animation: pr-m1 6s infinite; } .pr-k2 i::after { animation: pr-m2 6s infinite; } .pr-k3 i::after { animation: pr-m3 6s infinite; }
  .pr-cards-wrap.is-paused .pr-th, .pr-cards-wrap.is-paused .pr-th *, .pr-cards-wrap.is-paused .pr-th *::after { animation-play-state: paused !important; }
}
@media (prefers-reduced-motion: reduce) { .pr-anim-btn { display: none; } }
/* step states: idle (white, grey ring) · active (blue, number) · done (pale blue, check) */
@keyframes pr-c1 { 0%, 28% { background: #2483FF; color: #FFFFFF; } 32%, 100% { background: #E6F0FF; color: #2483FF; } }
@keyframes pr-c2 { 0%, 28% { background: #FFFFFF; color: #6B7280; box-shadow: inset 0 0 0 1px #C9CED6; } 32%, 58% { background: #2483FF; color: #FFFFFF; box-shadow: none; } 62%, 100% { background: #E6F0FF; color: #2483FF; box-shadow: none; } }
@keyframes pr-c3 { 0%, 58% { background: #FFFFFF; color: #6B7280; box-shadow: inset 0 0 0 1px #C9CED6; } 62%, 84% { background: #2483FF; color: #FFFFFF; box-shadow: none; } 88%, 100% { background: #E6F0FF; color: #2483FF; box-shadow: none; } }
@keyframes pr-n1 { 0%, 28% { opacity: 1; } 32%, 100% { opacity: 0; } } @keyframes pr-d1 { 0%, 28% { opacity: 0; } 32%, 100% { opacity: 1; } }
@keyframes pr-n2 { 0%, 58% { opacity: 1; } 62%, 100% { opacity: 0; } } @keyframes pr-d2 { 0%, 58% { opacity: 0; } 62%, 100% { opacity: 1; } }
@keyframes pr-n3 { 0%, 84% { opacity: 1; } 88%, 100% { opacity: 0; } } @keyframes pr-d3 { 0%, 84% { opacity: 0; } 88%, 100% { opacity: 1; } }
@keyframes pr-l1 { 0%, 22% { width: 0; } 30%, 100% { width: 100%; } }
@keyframes pr-l2 { 0%, 52% { width: 0; } 60%, 100% { width: 100%; } }
@keyframes pr-t1 { 0%, 28% { color: #1B2026; font-weight: 600; } 32%, 100% { color: #4B5563; font-weight: 400; } }
@keyframes pr-t2 { 0%, 28% { color: #6B7280; } 32%, 58% { color: #1B2026; font-weight: 600; } 62%, 100% { color: #4B5563; font-weight: 400; } }
@keyframes pr-t3 { 0%, 58% { color: #6B7280; } 62%, 84% { color: #1B2026; font-weight: 600; } 88%, 100% { color: #4B5563; font-weight: 400; } }
/* fields fill in one after another, hold, then clear for the next loop */
@keyframes pr-v1 { 0%, 10% { opacity: 0; transform: translateY(2cqw); } 18%, 88% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; } }
@keyframes pr-v2 { 0%, 26% { opacity: 0; transform: translateY(2cqw); } 34%, 88% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; } }
@keyframes pr-v3 { 0%, 44% { opacity: 0; transform: translateY(2cqw); } 52%, 88% { opacity: 1; transform: none; } 96%, 100% { opacity: 0; } }
/* boxes tick in order, hold, then clear */
@keyframes pr-k1 { 0%, 14% { background: #FFFFFF; box-shadow: inset 0 0 0 1px #9AA3AF; } 18%, 90% { background: #2483FF; box-shadow: inset 0 0 0 1px #2483FF; } 95%, 100% { background: #FFFFFF; box-shadow: inset 0 0 0 1px #9AA3AF; } }
@keyframes pr-k2 { 0%, 34% { background: #FFFFFF; box-shadow: inset 0 0 0 1px #9AA3AF; } 38%, 90% { background: #2483FF; box-shadow: inset 0 0 0 1px #2483FF; } 95%, 100% { background: #FFFFFF; box-shadow: inset 0 0 0 1px #9AA3AF; } }
@keyframes pr-k3 { 0%, 54% { background: #FFFFFF; box-shadow: inset 0 0 0 1px #9AA3AF; } 58%, 90% { background: #2483FF; box-shadow: inset 0 0 0 1px #2483FF; } 95%, 100% { background: #FFFFFF; box-shadow: inset 0 0 0 1px #9AA3AF; } }
@keyframes pr-m1 { 0%, 14% { opacity: 0; } 18%, 90% { opacity: 1; } 95%, 100% { opacity: 0; } }
@keyframes pr-m2 { 0%, 34% { opacity: 0; } 38%, 90% { opacity: 1; } 95%, 100% { opacity: 0; } }
@keyframes pr-m3 { 0%, 54% { opacity: 0; } 58%, 90% { opacity: 1; } 95%, 100% { opacity: 0; } }
.pr-cards-wrap { display: grid; gap: var(--space-3); justify-items: end; }
.pr-cards-wrap > .pr-cards { justify-self: stretch; }
/* North Star: the one accent-tinted surface on the page, so it reads first */
.pr-ns { display: grid; gap: var(--space-2); padding: var(--space-6); border-radius: var(--radius-md); background: var(--color-action-selected-bg); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); }
@container (min-width: 768px) { .pr-ns { padding: var(--space-8); } }
.pr-ns__label { margin: 0; display: flex; align-items: center; gap: var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-action-selected-text); }
.pr-ns__label .pm-icon { width: 16px; height: 16px; flex: none; }
.pr-ns__text { margin: 0; font-size: var(--type-h3); line-height: var(--line-h3); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h3); color: var(--color-text-primary); text-wrap: balance; }

/* Batch workflow (Fig. 1): six steps in a row from a 620px container, a list with details below that */
.pr-flow { container: pr-flow / inline-size; width: 100%; display: grid; gap: var(--space-5); }
.pr-flow template { display: none; }
.pr-flow__list { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-4); }
.pr-flow__b { all: unset; box-sizing: border-box; display: grid; grid-template-columns: auto minmax(0, 1fr); align-items: center; gap: var(--space-1) var(--space-3); cursor: pointer; border-radius: var(--radius-sm); }
.pr-flow__b:focus-visible { outline: var(--focus-ring-width) solid var(--color-focus-ring); outline-offset: var(--focus-ring-offset); }
.pr-flow__n { display: grid; place-items: center; width: 32px; height: 32px; border-radius: 50%; background: var(--color-bg-elevated); color: var(--color-text-primary); box-shadow: inset 0 0 0 1px var(--color-border-default); font: var(--weight-medium) var(--type-label) / 1 var(--font-sans); font-variant-numeric: tabular-nums; }
.pr-flow__b[aria-pressed="true"] .pr-flow__n { background: var(--color-action-primary); color: var(--color-text-on-accent); box-shadow: 0 0 0 4px var(--ring, var(--color-bg-sunken)); }
/* Number for upcoming and current steps, a check once a step is behind the tour (like the solution stepper) */
.pr-flow__n em, .pr-flow__n strong { grid-area: 1 / 1; font-style: normal; }
.pr-flow__n strong { opacity: 0; }
.pr-flow__b.is-done .pr-flow__n { background: var(--color-action-selected-bg); color: var(--color-action-selected-text); box-shadow: 0 0 0 4px var(--ring, var(--color-bg-sunken)); }
.pr-flow__b.is-done .pr-flow__n em { opacity: 0; } .pr-flow__b.is-done .pr-flow__n strong { opacity: 1; }
.pr-flow__prog { display: none; }
@media (prefers-reduced-motion: no-preference) {
  .pr-flow__n, .pr-flow__n em, .pr-flow__n strong, .pr-flow__t { transition: background-color .35s ease, color .35s ease, box-shadow .35s ease, opacity .25s ease; }
}
.pr-flow__t { font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.pr-flow__d p { margin: var(--space-1) 0 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
/* Risk: a filled, outlined box (warning tint + warning ring) with the label and icon, then the risk itself */
.pr-flow__risk { display: grid; gap: var(--space-1); align-content: start; padding: var(--space-3) var(--space-4); border-radius: var(--radius-sm); background: var(--color-state-warning-bg); box-shadow: inset 0 0 0 1px var(--color-state-warning); }
.pr-flow__d .pr-flow__risk { margin-top: var(--space-3); }
.pr-flow__rl { display: inline-flex; align-items: center; gap: var(--space-1); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-state-warning); }
.pr-flow__rl .pm-status__icon { width: 16px; height: 16px; margin: 0; flex: none; }
.pr-flow__rt { font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-primary); text-wrap: pretty; }
.pr-flow__d .pr-flow__rt { margin: 0; }
.pr-flow__bar { display: none; justify-content: flex-end; }
.pr-flow__d { padding-left: calc(32px + var(--space-3)); }

.pr-flow__note { display: none; }
@container pr-flow (min-width: 620px) {
  .pr-flow__list { grid-template-columns: repeat(6, minmax(0, 1fr)); gap: var(--space-2); position: relative; }
  .pr-flow__prog { display: block; position: absolute; z-index: 0; left: calc(100% / 12); top: 15.5px; width: 0; height: 2px; border-radius: 1px; background: var(--color-action-primary); pointer-events: none; }
  .pr-flow__s { z-index: 1; }
  .pr-flow__list::before { content: ""; position: absolute; left: calc(100% / 12); right: calc(100% / 12); top: 16px; height: 1px; background: var(--color-border-default); }
  .pr-flow__s { position: relative; }
  .pr-flow__b { grid-template-columns: minmax(0, 1fr); justify-items: center; text-align: center; width: 100%; padding: 0 var(--space-1); }
  .pr-flow__n { grid-row: auto; box-shadow: inset 0 0 0 1px var(--color-border-default), 0 0 0 4px var(--ring, var(--color-bg-sunken)); }
  .pr-flow__d { display: none; }
  .pr-flow__bar { display: flex; margin-top: calc(-1 * var(--space-2)); }
  .pr-flow__note { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 15rem); gap: var(--space-6); align-items: start; min-height: 7rem; padding: var(--space-4) var(--space-5); border-radius: var(--radius-md); background: var(--color-bg-elevated); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); }
  .pr-flow__note .pm-meta-text { margin: 0 0 var(--space-1); display: flex; align-items: center; gap: var(--space-1); }
}

/* Lists without numbers */
.cs-points--plain li { grid-template-columns: minmax(0, 1fr); }
/* Fig. 1: pain points with a note under the form */
.pr-pain { width: 100%; max-width: 640px; display: grid; gap: var(--space-5); justify-items: center; }
.pr-pain template { display: none; }
.pr-note { justify-self: stretch; min-height: 5.5rem; padding: var(--space-4) var(--space-5); border-radius: var(--radius-md); background: var(--color-bg-elevated); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); }
.pr-note__t { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.pr-note__d { margin: var(--space-1) 0 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); text-wrap: pretty; }
.pr-paper[data-active="1"] .crit { background: rgb(36 131 255 / 14%); box-shadow: inset 0 0 0 2px #2483FF; }
.pr-paper[data-active="2"] td:nth-child(-n+2), .pr-paper[data-active="2"] th:nth-child(-n+2) { background: rgb(36 131 255 / 14%); }
.pr-pin:focus-visible { outline: var(--focus-ring-width) solid var(--color-focus-ring); outline-offset: var(--focus-ring-offset); }
.pr-pin[aria-pressed="true"] { background: var(--color-action-primary); color: var(--color-text-on-accent); }
@media (pointer: coarse) { .pr-pin::after { content: ""; position: absolute; inset: -10px; } }
/* Insights -> goals: one row per pair, the insight on a tint, an arrow, then the goal as a lifted card */
.pr-ig { container: pr-ig / inline-size; margin: var(--space-2) 0; display: grid; gap: var(--space-3); }
.pr-ig__head { display: none; }
.pr-ig__list { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-4); }
.pr-ig__row { display: grid; gap: var(--space-2); justify-items: center; }
.pr-ig__row > div { justify-self: stretch; }
.pr-ig__in { padding: var(--space-5); border-radius: var(--radius-md); background: var(--color-bg-surface); display: grid; gap: var(--space-1); align-content: start; }
.pr-ig h4 { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); letter-spacing: 0; color: var(--color-text-primary); }
.pr-ig__in p:not(.pr-ig__k), .pr-ig__goal .pm-card__summary { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); text-wrap: pretty; }
.pr-ig__goal.pm-card--outlined, .pr-ig__goal.pm-card--outlined:hover { padding: var(--space-5); gap: var(--space-1); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); }
.pr-ig__k { margin: 0 0 var(--space-1); font-family: var(--font-meta); font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-tertiary); }
.pr-ig__arrow { color: var(--color-text-tertiary); transform: rotate(90deg); }
.pr-ig__arrow .pm-icon { width: 20px; height: 20px; }
@container pr-ig (min-width: 600px) {
  .pr-ig__head { display: grid; grid-template-columns: minmax(0, 1fr) 40px minmax(0, 1fr); font-family: var(--font-meta); font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-tertiary); }
  .pr-ig__row { grid-template-columns: minmax(0, 1fr) 40px minmax(0, 1fr); align-items: stretch; gap: 0; }
  .pr-ig__arrow { align-self: center; transform: none; }
  .pr-ig__k { display: none; }
}

/* ===== Procense media: first-pass reconstructions (project art: Procense navy #1B2026 and blue #2483FF) ===== */
.pr-stage { display: grid; place-items: center; }
.pr-well { width: 100%; }
/* Paper form */
.pr-paper { position: relative; width: 100%; max-width: 640px; aspect-ratio: 8.5 / 6; container-type: inline-size; background: #FBFAF6; color: #2B2B2B; box-shadow: 0 1px 2px rgb(0 0 0 / 10%), 0 12px 32px rgb(0 0 0 / 10%); transform: rotate(-0.6deg); overflow: hidden; }
.pr-paper > div { position: absolute; inset: 0; padding: 5cqw; font-family: var(--font-sans); font-size: 2.1cqw; }
.pr-paper__t { margin: 0 0 2cqw; text-align: center; font-weight: 700; font-size: 3cqw; letter-spacing: .06em; }
.pr-paper__m { margin: 2cqw 0; }
.pr-paper table { width: 100%; border-collapse: collapse; table-layout: fixed; font-size: inherit; }
.pr-paper td, .pr-paper th { overflow-wrap: break-word; }
.pr-paper th, .pr-paper td { border: 1px solid #8A8A8A; padding: 1.1cqw 1cqw; text-align: left; font-weight: 400; height: 3.4cqw; }
.pr-paper th { background: #EFEDE6; }
.pr-paper th, .pr-paper td { color: #2B2B2B; }
.pr-paper .crit { color: #C62828; font-weight: 700; }
.pr-paper td { position: relative; }
.pr-pin { position: absolute; z-index: 1; transform: translate(-50%, -50%); padding: 0; border: 0; cursor: pointer; display: grid; place-items: center; width: 5cqw; height: 5cqw; border-radius: 50%; background: var(--color-bg-inverse); color: var(--color-text-inverse); font: var(--weight-medium) 2.6cqw / 1 var(--font-sans); box-shadow: 0 0 0 0.6cqw #FBFAF6; }
/* Tablet */
.pr-tab { container-type: inline-size; width: 100%; max-width: 720px; padding: 2.2%; border-radius: 4.5% / 6.4%; background: #1B2026; box-shadow: 0 2px 4px rgb(0 0 0 / 14%), 0 18px 40px rgb(0 0 0 / 16%); }
.pr-scr { aspect-ratio: 4 / 3; overflow: hidden; border-radius: 2.4% / 3.2%; background: #F6F7F9; color: #1B2026; font-family: var(--font-sans); font-size: 1.9cqw; line-height: 1.35; display: flex; flex-direction: column; }
.pr-bar { display: flex; align-items: center; gap: 1.6cqw; padding: 1.6cqw 2.6cqw; background: #1B2026; color: #FFFFFF; }
.pr-bar span { opacity: .7; } .pr-bar i { margin-left: auto; font-style: normal; opacity: .7; }
.pr-steps { list-style: none; margin: 0; padding: 1.8cqw 2.6cqw; display: flex; gap: 2.6cqw; background: #FFFFFF; border-bottom: 1px solid #E3E6EB; color: #6B7280; }
.pr-steps li { display: flex; align-items: center; gap: 1cqw; }
.pr-steps span { display: grid; place-items: center; width: 3cqw; height: 3cqw; border-radius: 50%; border: 1px solid #C9CED6; font-size: 1.6cqw; }
.pr-steps .is-on { color: #1B2026; font-weight: 600; } .pr-steps .is-on span { background: #2483FF; border-color: #2483FF; color: #FFFFFF; }
.pr-steps .is-done span { background: #E6F0FF; border-color: #E6F0FF; color: #2483FF; }
.pr-body { flex: 1; padding: 2.4cqw 2.6cqw; display: flex; flex-direction: column; gap: 1.8cqw; min-height: 0; }
.pr-h { margin: 0; font-size: 2.6cqw; font-weight: 600; }
.pr-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.6cqw 2cqw; }
.pr-f { display: grid; gap: .6cqw; } .pr-f--wide { grid-column: 1 / -1; }
.pr-f__l { color: #4B5563; font-size: 1.7cqw; }
.pr-f__v { display: flex; align-items: center; gap: 1cqw; padding: 1.3cqw 1.4cqw; border: 1px solid #D6DAE1; border-radius: .8cqw; background: #FFFFFF; }
.pr-f__v svg, .pr-sign svg { width: 2.2cqw; height: 2.2cqw; fill: none; stroke: #2483FF; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; flex: none; }
.pr-f__v em { margin-left: auto; font-style: normal; font-size: 1.5cqw; padding: .2cqw .9cqw; border-radius: .6cqw; background: #E6F0FF; color: #1559C9; }
.pr-foot { margin-top: auto; display: flex; align-items: center; justify-content: flex-end; gap: 1.4cqw; }
.pr-btn { padding: 1.2cqw 3cqw; border-radius: .8cqw; background: #2483FF; color: #FFFFFF; font-weight: 600; }
.pr-btn--2 { background: #FFFFFF; color: #1B2026; box-shadow: inset 0 0 0 1px #C9CED6; }
.pr-two { display: grid; grid-template-columns: 1.15fr 1fr; gap: 2cqw; }
.pr-sop { padding: 2cqw; border-radius: 1cqw; background: #E6F0FF; border-left: .6cqw solid #2483FF; }
.pr-sop__n { margin: 0 0 1.2cqw; font-weight: 600; color: #1559C9; }
.pr-sop ol { margin: 0; padding-left: 2.6cqw; display: grid; gap: 1cqw; }
.pr-sop b { color: #1B2026; }
.pr-ing { padding: 2cqw; border-radius: 1cqw; background: #EEF0F3; display: grid; gap: 1.1cqw; align-content: start; }
.pr-ing__h { margin: 0; font-weight: 600; }
.pr-ing__r, .pr-qc__r { display: grid; grid-template-columns: 1.6fr 1fr 1fr auto; gap: 1.2cqw; align-items: center; }
.pr-in { padding: .8cqw 1cqw; border: 1px solid #D6DAE1; border-radius: .6cqw; background: #FFFFFF; min-height: 2.4cqw; }
.pr-ok { color: #1E8E5A; font-weight: 700; width: 2cqw; }
.pr-qc { display: grid; gap: 1.2cqw; padding: 2cqw; border-radius: 1cqw; background: #FFFFFF; border: 1px solid #E3E6EB; }
.pr-qc__r { grid-template-columns: 1.6fr 1.2fr 1fr 6cqw; }
.pr-qc__hd { color: #6B7280; font-size: 1.6cqw; }
.pr-pf { text-align: center; padding: .4cqw 0; border-radius: .6cqw; font-size: 1.5cqw; font-weight: 600; }
.pr-pf--pass { background: #E3F4EA; color: #1E7A4C; } .pr-pf--fail { background: #FDE7E7; color: #B42318; }
.pr-sign { margin-right: auto; display: flex; align-items: center; gap: 1cqw; color: #4B5563; }
"""

PROCENSE = dict(page_title='Procense Case Study', out='procense.html', sections=SECTIONS, body=BODY, header=HEADER, tldr=TLDR, css=CSS, js=JS)

if __name__ == '__main__':
    print(len(C.render(PROCENSE)))
