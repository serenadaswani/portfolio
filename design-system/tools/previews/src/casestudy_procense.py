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

def items(rows, grid=False):
    """Title + description list, no numbering (Serena, 2026-11-16)."""
    return (f'<ul class="cs-points cs-points--plain{" cs-points--grid" if grid else ""}">'
            + ''.join(f'<li><div><h4>{t}</h4><p>{d}</p></div></li>' for t, d in rows) + '</ul>')

# Interview insights. DRAFT: written to fill out the section (Serena asked for illustrative insights, 2026-11-16);
# replace with real interview notes before publishing. Each one links to the design goal it shaped.
INSIGHTS = [
    ('Forms get filled in mid-task', 'Operators record values while they weigh ingredients, mix and take samples, often wearing gloves. Every extra tap is time away from the batch.', 'Fewer taps'),
    ('The same values are written again and again', 'Date, time and initials go on every row. Most errors weren’t bad readings, they were copying slips that only surfaced in review.', 'Built-in guardrails'),
    ('The instructions live in a binder', 'Operators flip between the step-by-step instructions and the form to check limits. That’s where steps get missed.', 'At home in Procense'),
    ('Every record has to survive an audit', 'Auditors check critical limits and sign-offs first. Every value needs a who and a when, so speed can’t cost traceability.', 'Faster, not looser'),
]
def insights():
    return ('<div class="pr-ins-wrap"><p class="pm-meta-text pr-draft">Draft insights, to replace with interview notes</p><ul class="pr-ins">' + ''.join(
        f'<li class="pm-panel pr-ins__c"><h4>{t}</h4><p>{d}</p><p class="pr-ins__g"><span class="pm-meta-text">Shaped the goal</span><span class="pm-badge">{g}</span></p></li>'
        for t, d, g in INSIGHTS) + '</ul></div>')

def shot(art, cap, n):
    return (f'<figure class="pm-frame"><div class="pm-frame__stage pr-stage">{art}</div>'
            f'<figcaption class="pm-frame__caption"><span class="pm-frame__index">Fig. {n:02d}</span><span>{cap}</span></figcaption></figure>')

# ---------- content ----------
SECTIONS = [('overview', 'Overview'), ('challenge', 'The challenge'), ('discovery', 'Discovery'), ('goals', 'Design goals'), ('ideation', 'Ideation'),
            ('tablet', 'Tablet-first'), ('solution', 'The solution'), ('feedback', 'User feedback'), ('impact', 'Impact'), ('reflection', 'Reflection')]

BODY = ''.join([
    section('overview', 'Overview', 'Going digital let the floor move faster and focus on what matters.',
        lede('Procense gives chemical manufacturers an integrated platform for running and monitoring production. Even so, the plants it served still recorded every batch on paper forms.',
             'I designed the Digital Forms application, a module within that platform that replaces those forms with a single tablet flow. It streamlined and modernized how plants record each batch: batches run 10% faster, every record is accurate and traceable from the start, and operators spend less time on paperwork and more on the work in front of them.')
        + stats([('10%', 'Faster batch execution, from weighing ingredients to quality sign-off'), ('100%', 'Automated traceability, so audits take less digging'), ('100%', 'Data accuracy, with nothing copied over from paper')], ' pm-stats--sm cs-stats')),

    section('challenge', 'The challenge', 'Every batch was tracked on paper.',
        lede('Chemical plants make products in batches, combining set amounts of ingredients and testing them step by step. In many plants, each batch is recorded by hand on two paper forms: one for the manufacturing steps and one for the quality checks.',
             'Once complete, the forms go to directors and engineers, who decide whether the batch meets the standard. Every handwritten value is a chance for error, and decisions on the floor stall while the paperwork moves.',
             'Digitizing the forms was a chance to give frontline workers a faster, more reliable way to record production data, tailored to each client’s workflow. It also had to feel familiar to operators who had filled in these forms by hand for years, which led to our guiding question.')
        + panel('How might we', '<p class="cs-goal">How might we streamline batch manufacturing by digitizing its forms, while keeping them intuitive for operators used to filling them in by hand?</p>', ' pm-panel--tonal', 'p-hmw')),

    section('discovery', 'Discovery', 'The forms hid what mattered most.',
        lede('I started by taking the paper forms apart. They captured a great deal of data, but made it hard to spot what mattered and slow to fill in.')
        + shot(paper_form(), 'The paper QC form, reconstructed. Hover over or tap a number to see each pain point.', 1)
        + '<h3 class="cs-h3">What I learned about the floor</h3>'
        + lede('To understand how the forms are used on the floor, I interviewed Procense’s co-founder, a former process engineer who has both written and filled in these forms. Four insights stood out, and each became a design goal.')
        + insights()),

    section('goals', 'Design goals', 'Faster, without cutting corners.',
        lede('Together, the pain points and interviews gave the Digital Forms application four goals.')
        + items([('Fewer taps', 'Every tap removed is one less chance to make a mistake.'),
               ('Built-in guardrails', 'Fields fill themselves in where they can, and the same parts repeat across forms.'),
               ('At home in Procense', 'The forms work like the rest of the platform, so there’s nothing new to learn.'),
               ('Faster, not looser', 'Speed can’t come at the cost of the checks the forms exist for.')], grid=True)),

    section('ideation', 'Ideation', 'I sketched how crowded tables could become simple steps.',
        lede('I studied how other products turn paper forms into software and organise large tables, then sketched layouts and noted what each form needed.')
        + shot(f'<div class="pm-media pm-media--16x10 pr-well" role="img" aria-label="Image to come: annotated layout sketches"><div class="pm-media__fallback">{I["image"]}<span>Image to come</span><span>Annotated layout sketches</span></div></div>', 'Early sketches of the digitized QC and SOP forms.', 2)),

    section('tablet', 'Shifting gears', 'We designed for desktop. The floor ran on tablets.',
        '<div class="cs-pair">'
        + panel('What we assumed', '<p>Operators would use desktops or laptops, like the rest of Procense’s web-first platform.</p>', ' pm-panel--tonal', 'p-assumed')
        + panel('What we found', '<p>Operators carry tablets as they work through each step and run quality tests on the floor.</p>', '', 'p-found')
        + '</div>'
        + lede('That discovery reshaped the project. We moved to a tablet-first design with new layouts and a new flow. The smaller screen meant breaking long forms into steps, which adds a tap or two, but in return operators got larger text, cleaner sections and a flow that matches how they actually work.')),

    section('solution', 'The solution', 'Two paper forms became one simple flow.',
        lede('The final design merges both forms into one flow of three steps: batch details, then the manufacturing steps and ingredients, then the quality tests. Each screen shows only what that step needs, so operators can keep their attention on the batch.')
        + shot(screen1(), 'Batch information, the first step. Date, time and signature fill in on their own.', 3)
        + shot(screen2(), 'Manufacturing steps and ingredients. Instructions in blue, ingredients in grey, critical conditions in bold.', 4)
        + shot(screen3(), 'Quality tests, the last step. Each result is checked against its target range as it’s entered.', 5)
        + items([('Fields that fill themselves', 'Date and time fill in automatically, and signatures come from the operator’s login.'),
                  ('The same patterns everywhere', 'Buttons and layouts behave the same at every step.'),
                  ('Clear sections', 'Colour sets them apart: blue for instructions, grey for ingredients.'),
                  ('Familiar icons', 'Icons like date and time mark the inputs that are required.'),
                  ('Built for dense data', 'One left-aligned column that’s easy to read and move through.'),
                  ('Instructions in the form', 'The steps for each stage sit right inside the form, so there’s no binder to check.'),
                  ('Critical steps stand out', 'Conditions that can ruin a batch are bold and hard to miss.')], grid=True)),

    section('feedback', 'User feedback', 'A QA manager walked us through every section.',
        lede('We reviewed the first design of the quality test form with a QA manager, section by section, and their feedback led to two changes.')
        + '<div class="cs-pair">'
        + panel('What we heard', '<p>Operators still typed too much, and choosing batch and order numbers from a list added unnecessary steps.</p>', ' pm-panel--tonal', 'p-heard')
        + panel('What we changed', '<p>More fields now fill in automatically from the sample type, and batch and order numbers are typed in directly.</p>', '', 'p-changed')
        + '</div>'),

    section('impact', 'Impact', 'Faster batches, and more time for what matters.',
        lede('Moving from paper to the Digital Forms application streamlined the whole batch process. Operators record data as they work instead of copying it later, reviewers see it as soon as it’s entered, and every value carries who entered it and when. With the paperwork out of the way, teams can focus on running safe, consistent batches.')
        + stats([('10%', 'Faster batch execution, from weighing ingredients to quality sign-off'), ('100%', 'Automated traceability, so audits take less digging'), ('100%', 'Data accuracy, so frontline teams can focus on key insights')], ' pm-stats--sm cs-stats')),

    section('reflection', 'Reflection', 'Designing without direct access to operators.',
        lede('The hardest part was researching without access to operators on the floor. I relied on the team and Procense’s in-house experts, and learned manufacturing forms from scratch.',
             'The project showed how much a well-designed form can change. By modernizing a process operators already knew, rather than replacing it with something unfamiliar, the plants moved faster without losing the checks that keep every batch safe.')
        + '<h3 class="cs-h3">What I’d do next</h3>'
        + items([('Observe operators on the floor', 'Watch the forms in use to find the next steps worth removing.'),
                 ('Bring more forms over', 'Apply the same patterns to the other paper processes in the plant.')])),
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
/* Interview insights */
.pr-ins-wrap { container-type: inline-size; display: grid; gap: var(--space-3); }
.pr-draft { margin: 0; }
.pr-ins { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-4); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 600px) { .pr-ins { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.pr-ins__c { padding: var(--space-5); display: grid; gap: var(--space-2); align-content: start; }
.pr-ins__c h4 { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); }
.pr-ins__c p { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); text-wrap: pretty; }
.pr-ins__c .pr-ins__g { margin-top: var(--space-2); display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-2); }

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
