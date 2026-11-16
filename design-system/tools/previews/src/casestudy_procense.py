"""Procense Digital Forms case study, on the same structure as the revised Mensio case study (casestudy.render).
Content: Serena's Framer case study (project-detail-procense-digital-forms-application, read 2026-11-16), rewritten in
this site's voice. Media: first-pass mockups drawn in HTML (no Framer images were available): the paper QC form and
three tablet screens. They are labelled as reconstructed and use Procense's navy and blue only as project art.
Run: python3 design-system/tools/previews/src/casestudy_procense.py  ->  prototypes/procense.html
"""
import casestudy as C
from casestudy import I, S, section, lede, panel, points, stats
from lib import _l

# ---------- media: paper form (before) ----------
def paper_form():
    head = ['Date', 'Time', 'Test', 'Spec', 'Result', 'Initials']
    rows = [('pH', '6.5 – 7.5'), ('Viscosity (cP)', '1,200 – 1,500'), ('Specific gravity', '1.02 – 1.06'), ('Appearance', 'Clear, no particulates'),
            ('Moisture (%)', '≤ 0.5'), ('Odor', 'Characteristic')]
    PIN = lambda n: f'<span class="pr-pin">{n}</span>'
    tr = ''.join(f'<tr><td>__/__/__</td><td>__:__</td><td{" class=crit" if i in (0, 2) else ""}>{t}</td><td>{sp}</td><td>{PIN(1) if i == 2 else ""}</td><td></td></tr>' for i, (t, sp) in enumerate(rows))
    return ('<div class="pr-paper" role="img" aria-label="Reconstructed paper QC form: a dense table where only red bold text marks critical tests, and every row repeats date and time fields">'
            '<div aria-hidden="true"><p class="pr-paper__t">QC BATCH PERFORMANCE</p>'
            '<p class="pr-paper__m">Batch No. ________ &nbsp; MO No. ________ &nbsp; Product ______________</p>'
            '<table><colgroup><col style="width:15%"><col style="width:11%"><col style="width:23%"><col style="width:23%"><col style="width:14%"><col style="width:14%"></colgroup><thead><tr>' + ''.join(f'<th>{h}{PIN(2) if h == "Date" else ""}</th>' for h in head) + f'</tr></thead><tbody>{tr}</tbody></table>'
            '<p class="pr-paper__m">Reviewed by ____________ &nbsp; Date __/__/__ &nbsp; Signature ____________</p>'
            '</div></div>')

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

def shot(art, cap, n):
    return (f'<figure class="pm-frame"><div class="pm-frame__stage pr-stage">{art}</div>'
            f'<figcaption class="pm-frame__caption"><span class="pm-frame__index">Fig. {n:02d}</span><span>{cap}</span></figcaption></figure>')

# ---------- content ----------
SECTIONS = [('challenge', 'The challenge'), ('discovery', 'Discovery'), ('goals', 'Design goals'), ('ideation', 'Ideation'),
            ('tablet', 'Tablet-first'), ('solution', 'The solution'), ('feedback', 'User feedback'), ('impact', 'Projected impact'), ('reflection', 'Reflection')]

BODY = ''.join([
    section('challenge', 'The challenge', 'Chemical plants still ran quality checks on paper.',
        lede('Many Tier 2 and Tier 3 chemical plants record batch performance on two paper forms: the QC Batch Performance form and the Crude Manufacturing SOP form.',
             'Those checklists go to directors and engineers, who use them to judge product quality. Paper slows decisions on the floor and leaves room for human error.')
        + shot(paper_form(), 'The paper QC form, reconstructed. Numbers mark the pain points below.', 1)
        + panel('How might we', '<p class="cs-goal">How might we get the most out of moving from paper forms to digital ones inside Procense’s platform?</p>', ' pm-panel--tonal', 'p-hmw')
        + lede('Procense’s answer was Digital Forms, a cloud module of its manufacturing platform. Each client gets its own forms, designed to cut cognitive load and errors.')),

    section('discovery', 'Discovery', 'The paper forms buried what mattered.',
        lede('I started with the forms themselves, looking for pain points and inconsistencies. The aim was a clearer hierarchy and layout for a lot of data, and faster entry.')
        + points([('Limited visual hierarchy', 'Only red, bold text set critical fields apart, which made the form hard to scan under time pressure.'),
                  ('Repetitive, disjointed data', 'Dense tables repeated fields like date and time on every row, slowing entry and inviting mistakes.')])
        + '<h3 class="cs-h3">Interviews</h3>'
        + lede('I interviewed Procense’s co-founder, a former process engineer, about how SOPs and batch forms are designed and used, to learn the input patterns and the usability problems on the floor.')),

    section('goals', 'Design goals', 'Four goals kept the forms fast and safe.',
        points([('Fewer clicks and actions', 'Every step removed is one less chance for human error.'),
                ('Guardrails', 'Auto-filled fields and reusable components.'),
                ('Native to the platform', 'The form’s structure follows how Procense already works.'),
                ('Faster, not looser', 'Efficiency without losing what the form means operationally.')], 'cs-points cs-points--grid')),

    section('ideation', 'Ideation', 'I sketched how dense paper tables could become steps.',
        lede('I studied common ways paper forms get digitized and common patterns for tabular data, then sketched layouts and labelled the features each form needed.')
        + shot(f'<div class="pm-media pm-media--16x10 pr-well" role="img" aria-label="Image to come: annotated layout sketches"><div class="pm-media__fallback">{I["image"]}<span>Image to come</span><span>Annotated layout sketches</span></div></div>', 'Early sketches of the digitized QC and SOP forms.', 2)),

    section('tablet', 'Shifting gears', 'Operators worked on tablets, so we went tablet-first.',
        '<div class="cs-pair">'
        + panel('What we assumed', '<p>Operators would use desktops or laptops, like the rest of Procense’s web-first platform.</p>', ' pm-panel--tonal', 'p-assumed')
        + panel('What we found', '<p>Operators carry tablets as they move through SOPs and run QA tests on the floor.</p>', '', 'p-found')
        + '</div>'
        + lede('We switched to a tablet-first, responsive approach, with new layouts, interactions and information flow. Limited screen space meant splitting long forms into steps, which adds some navigation. In return: larger, readable text, cleaner sections, and a flow closer to how operators already work.')),

    section('solution', 'The solution', 'Two paper forms became one tablet flow.',
        lede('The flow starts with Batch information from the QC form, moves through the SOPs and ingredients from the manufacturing form, and ends with the QC tests.')
        + shot(screen1(), 'Batch information, the first step. Date, time and signature fill in on their own.', 3)
        + shot(screen2(), 'SOPs and ingredients. SOP steps in blue, ingredients in grey, critical conditions in bold.', 4)
        + shot(screen3(), 'QC tests, the last step. Results are checked against the spec as they’re entered.', 5)
        + points([('Smart field automation', 'Date and time fill in automatically, and signatures come from the user’s credentials.'),
                  ('Consistent interaction patterns', 'The same buttons and layouts at every step.'),
                  ('Clear visual hierarchy', 'Colour-coded sections: blue for SOPs, grey for ingredients.'),
                  ('Recognisable icons', 'Icons like date and time mark required inputs.'),
                  ('A layout for dense data', 'One vertical, left-aligned column that’s easy to read and move through.'),
                  ('In-line SOPs', 'The relevant SOP steps sit inside the form, with no switching documents.'),
                  ('Highlighted instructions', 'Critical process conditions are bold and hard to miss.')], 'cs-points cs-points--grid')),

    section('feedback', 'User feedback', 'A QA manager walked us through every section.',
        lede('We reviewed the first mockup of the QC test form with an operational QA manager, section by section.')
        + '<div class="cs-pair">'
        + panel('What we heard', '<p>Operators still typed too much, and picking batch and MO numbers from a list added steps.</p>', ' pm-panel--tonal', 'p-heard')
        + panel('What we changed', '<p>More fields fill in from the selected sample type, and batch and MO numbers became free text.</p>', '', 'p-changed')
        + '</div>'),

    section('impact', 'Projected impact', 'What Procense expects Digital Forms to change.',
        lede('These are Procense’s projections. The module hasn’t been built yet, so none of them is measured.')
        + stats([('10%', 'Faster batch execution: pre-weigh, compounding and QA approvals'), ('100%', 'Automated traceability, for simpler audits'), ('100%', 'Digital data accuracy, so teams can focus on insights')], ' pm-stats--sm cs-stats')),

    section('reflection', 'Reflection', 'Designing without direct access to operators.',
        lede('The hardest part was research without the people on the floor. I leaned on the team and Procense’s internal experts, and learned SOP forms from scratch.',
             'Procense is raising funding to build Digital Forms. The designs validated user needs, shaped the product direction, and have drawn interest from other potential clients.')
        + '<h3 class="cs-h3">Next steps</h3>'
        + points([('Test with operators', 'Put the prototype in front of factory operators.'),
                  ('Build the front end', 'A working version with real interactions.')])),
])

HEADER = f'''  <header class="cs-head">
    <ul class="cs-badges" aria-label="Status and disciplines"><li class="pm-badge pm-badge--info">{S["info"]}Concept</li><li class="pm-badge">Product design</li><li class="pm-badge">End-to-end</li><li class="pm-badge">Tablet</li></ul>
    <h1 class="cs-title">Digitizing manufacturing QA forms to increase batch execution speed by 10%</h1>
  </header>

  <section class="cs-facts" aria-label="Project details"><dl class="cs-facts__list">
    <div><dt>Role</dt><dd>UI/UX designer</dd><dd>Contract</dd></div>
    <div><dt>Team</dt><dd>To confirm</dd></div>
    <div><dt>Timeline</dt><dd>2023</dd></div>
    <div><dt>Skills</dt><dd>User research</dd><dd>Product design</dd><dd>Prototyping</dd></div>
  </dl></section>'''

TLDR = f'''      <dl class="cs-tldr__rows">
        <div class="cs-tldr__row"><dt>Background</dt><dd>Chemical plants record batch quality on paper QC and SOP forms that directors and engineers review by hand.</dd></div>
        <div class="cs-tldr__row"><dt>Problem</dt><dd>Paper slowed decisions on the floor, and dense, repetitive tables made errors easy.</dd></div>
        <div class="cs-tldr__row"><dt>Approach</dt><dd>I studied the forms, interviewed Procense’s co-founder, and redesigned tablet-first when we learned operators work on tablets.</dd></div>
        <div class="cs-tldr__row"><dt>Outcome</dt><dd>Two paper forms became one tablet flow. The designs are helping Procense raise funding to build it.</dd></div>
      </dl>
      {stats([('2 → 1', 'Paper forms merged into one tablet flow'), ('10%', 'Projected faster batch execution'), ('7', 'Patterns to cut clicks and errors')], ' pm-stats--sm cs-tldr__stats')}'''

CSS = r"""
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
.pr-paper .crit { color: #C62828; font-weight: 700; }
.pr-paper td { position: relative; }
.pr-paper th { position: relative; }
.pr-paper th .pr-pin { left: auto; right: 1cqw; }
.pr-pin { position: absolute; left: 1cqw; top: 50%; transform: translateY(-50%); display: grid; place-items: center; width: 5cqw; height: 5cqw; border-radius: 50%; background: var(--color-bg-inverse); color: var(--color-text-inverse); font: var(--weight-medium) 2.6cqw / 1 var(--font-sans); box-shadow: 0 0 0 0.6cqw #FBFAF6; }
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

PROCENSE = dict(page_title='Procense Case Study', out='procense.html', sections=SECTIONS, body=BODY, header=HEADER, tldr=TLDR, css=CSS)

if __name__ == '__main__':
    print(len(C.render(PROCENSE)))
