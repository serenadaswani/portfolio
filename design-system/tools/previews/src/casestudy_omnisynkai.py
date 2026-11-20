"""OmniSynkAI AI autofill case study, on the same structure as the Procense and Mensio pages (casestudy.render).
Story (2026-11-19, Serena): she joined for v4 of the listing flow, working with the lead designer while the listing
page itself was being enhanced in parallel. Her focus: where autofill lives on the page, telling AI from manual content, and
the feedback loop. The page summarizes the team's research and earlier versions, then shows how her work built on them.
Sources: Serena's presentation (OSAI_Case Study Presentation.pdf) and Framer case study; teammates' published case studies
for team context and results, cited as team results by role only, no names or links (Serena, 2026-11-19). Media: stills from the approved prototype video (PM's permission, team credited).
Run: python3 design-system/tools/previews/src/casestudy_omnisynkai.py  ->  omnisynkai/index.html
"""
import casestudy as C
from casestudy import I, section, lede, panel, stats
from lib import _l
import casestudy_procense as CP

IG_CSS = CP._between(CP.CSS, '/* Insights -> goals', '/* ===== Procense media')  # same findings -> goals graphic as Procense

def items(rows, grid=False):
    """Title + description list, no numbering (same as Procense)."""
    return (f'<ul class="cs-points cs-points--plain{" cs-points--grid" if grid else ""}">'
            + ''.join(f'<li><div><h4>{t}</h4><p>{d}</p></div></li>' for t, d in rows) + '</ul>')

# ---------- figures ----------
_n = [0]
def _num():
    _n[0] += 1
    return f'{_n[0]:02d}'
def _cap(n, cap):
    return f'<figcaption class="pm-frame__caption"><span class="pm-frame__index">Fig. {n}</span><span>{cap}</span></figcaption>'

# Prototype stills: file in assets/screens/, alt text
SHOTS = {
    'empty': ('01-empty-listing.jpg', 'Create a new listing page before autofill: a bar at the top reads “Save time with Autofill” beside empty Title and Product category fields and a sparkle button; Publish listing is disabled.'),
    'filling': ('02-autofill-in-progress.jpg', 'A “Filling out your listing” dialog over the page, with a tip about time saved and a Cancel Autofill button.'),
    'filled': ('03-listing-autofilled.jpg', 'The listing after autofill: a Vitamin C Serum description, nine product photos, and the brand and tags highlighted in purple. The top bar reads “Listing Autofilled, feel free to edit details” with More options and Publish listing.'),
    'tone': ('04-change-tone.jpg', 'A Change Tone dialog with tone options: Formal, Persuasive, Humorous, Playful, Informative, Conversational and Informal, and a Confirm button.'),
    'retoned': ('05-tone-changed-new-tags.jpg', 'The listing after a tone change: the earlier tags are now plain and two new tags, #toning and #brightening, are highlighted in purple.'),
    'clear': ('06-clear-listing-confirmation.jpg', 'A confirmation dialog: “Are you sure you’d like to clear this listing? Clearing this form will remove all autofilled content. You won’t be able to undo this action.” with Cancel and Clear listing.'),
    'menu': ('07-more-options-menu.jpg', 'The More options menu open under the top bar, with Regenerate, Clear fields and Change tone.'),
    'platforms': ('08-select-platforms.jpg', 'A Select Platforms dialog with eBay, Depop, Amazon, TikTok, Mercari and Etsy, a “Why can’t I see all platforms?” hint and a Confirm button.'),
    'confirm': ('09-confirm-and-publish.jpg', 'A Confirm and publish dialog showing the listing will be posted on eBay and Amazon, with Preview listing and “Looks good, post” buttons.'),
    'done': ('10-listing-complete.jpg', 'A Listing Complete dialog: “Nice work, you just listed your first product with OmniSynkAI,” with Dashboard and List Another buttons.'),
}
def shot(key, cap):
    f, alt = SHOTS[key]
    return (f'<figure class="pm-frame"><div class="pm-frame__stage om-stage"><img class="om-shot" src="assets/screens/{f}" width="1600" height="1183" loading="lazy" alt="{alt}"></div>'
            + _cap(_num(), cap) + '</figure>')
def pair(a, b):
    return f'<div class="om-pair">{a}{b}</div>'

def need(cap, what, ratio='16x10'):
    """A slot for a graphic Serena still needs to supply: says what goes there."""
    n = _num()
    return (f'<figure class="pm-frame om-need"><div class="pm-frame__stage"><div class="pm-media pm-media--{ratio}" role="img" aria-label="Graphic to come: {what}">'
            f'<div class="pm-media__fallback">{I["image"]}<span>Graphic needed</span><span>{what}</span></div></div></div>' + _cap(n, cap) + '</figure>')

def framed(art, cap):
    return f'<figure class="pm-frame"><div class="pm-frame__stage om-stage">{art}</div>' + _cap(_num(), cap) + '</figure>'

def team_source():
    return ('<p class="pm-meta-text om-source">Team results for the whole listing flow: listing time and accuracy from testing after the September 2024 soft launch; '
            'autofill satisfaction from pre-launch usability testing.</p>')

# How the listing flow evolved before and while I joined (the lead designer's case study), with what each version taught the team
VERSIONS = [
    ('v1', 'Cross-listing', 'Grouped actions in a bento layout, with a separate price optimizer.', 'Cluttered, and couldn’t scale to data-heavy fields.', False),
    ('v2', 'Autosynk', 'Sellers chose AI or manual listing; AI drafted from a few core details.', 'Sellers wanted more control over what AI wrote.', False),
    ('v3', 'Autofill tiles', 'Autofill buttons, form steppers and feedback on each suggestion.', 'Many sellers didn’t realize autofill existed.', False),
    ('v4', 'Autofill for launch', 'Autofill became a core launch feature, with a clear place on the page, cues for AI content and simple controls.', 'Make it findable, clearly marked and easy to steer.', True),
]
def versions():
    return ('<ol class="om-ver">' + ''.join(
        f'<li class="om-ver__v{" is-mine" if mine else ""}"><p class="om-ver__k"><span class="pm-meta-text">{v}</span>{name}'
        + '</p>' + ('<span class="pm-badge om-ver__me">Where I joined</span>' if mine else '')
        + f'<p class="om-ver__d">{d}</p><p class="om-ver__l"><span>{"Goal" if mine else "Learned"}</span>{l}</p></li>'
        for v, name, d, l, mine in VERSIONS) + '</ol>')

# My three areas: the open problem, the evidence behind it, what I designed
FOCUS = [
    ('Placement', 'Where does autofill live?', 'Sellers couldn’t find the autofill button, and many didn’t know the feature existed.'),
    ('Clarity', 'What did AI write, and what did I?', 'Autofilled text looked like manual text, and sellers weren’t sure which fields they had to fill in.'),
    ('Control', 'How do sellers steer the result?', 'AI helped, but sellers wanted more say in what it generated.'),
]
def focus():
    return ('<ul class="om-focus">' + ''.join(
        f'<li class="pm-card pm-card--outlined om-focus__c"><p class="om-focus__k">{k}</p><h4 class="pm-card__title">{q}</h4><p class="pm-card__summary">{d}</p></li>'
        for k, q, d in FOCUS) + '</ul>')

# My research (slides 6–9) and the design priority each finding set
FINDINGS = [
    ('Ease of use comes first', 'Desk research', 'Sellers expect AI tools to feel intuitive from the first click.',
     'Easy to find', 'Make autofill discoverable and simple to start, for new and returning sellers alike.'),
    ('Sellers need to see what changed', 'Desk research', 'Visual cues help people tell AI content from their own.',
     'Clearly marked', 'Highlight everything AI wrote, so sellers know what to check.'),
    ('Time is of the essence', 'Desk research', 'Sellers list in volume, so every extra step costs them.',
     'Right place, right time', 'Bring AI into the key moments of the listing flow, without adding friction.'),
    ('Feedback makes the model better', 'Competitors', 'Feedback loops improve the AI and keep sellers engaged.',
     'Learns from feedback', 'Let sellers react to what AI writes, and use that to improve it.'),
    ('Sellers still want control', 'Competitors', 'Even with AI, sellers can always list by hand.',
     'Seller in control', 'Every field stays editable, and sellers can regenerate, clear or retone at any time.'),
]
def findings():
    arrow = f'<span class="pr-ig__arrow" aria-hidden="true">{_l("arrow-right")}</span>'
    rows = ''.join(
        f'<li class="pr-ig__row"><div class="pr-ig__in"><p class="pr-ig__k">Finding</p><div class="om-fd__h"><h4>{ft}</h4><span class="pm-badge">{src}</span></div><p>{fd}</p></div>{arrow}'
        f'<div class="pm-card pm-card--outlined pr-ig__goal"><p class="pr-ig__k">Design priority</p><h4 class="pm-card__title">{gt}</h4><p class="pm-card__summary">{gd}</p></div></li>'
        for ft, src, fd, gt, gd in FINDINGS)
    return (f'<figure class="pr-ig"><div class="pr-ig__head" aria-hidden="true"><span>Finding</span><span></span><span>Design priority</span></div>'
            f'<ol class="pr-ig__list">{rows}</ol></figure>')

# Discover -> Conceptualize -> Design, for my part
PHASES = [
    ('Discover', 'Where can AI help?', 'I pulled past research, mapped the AI’s limits with engineering, and studied how Shopify and Trustana use AI.'),
    ('Conceptualize', 'What should it do?', 'I mapped the flow for new and returning sellers, starting from the two fields AI needs, with feedback built in.'),
    ('Design', 'How does it fit?', 'I designed where autofill lives, how AI content is marked, and how sellers steer it.'),
]
def process():
    arrow = f'<span class="om-proc__arrow" aria-hidden="true">{_l("arrow-right")}</span>'
    return ('<ol class="om-proc">' + arrow.join(
        f'<li class="om-proc__step"><p class="om-proc__k">{name}</p><h4>{q}</h4><p class="om-proc__d">{d}</p></li>'
        for name, q, d in PHASES) + '</ol>')

# The final autofill flow, from the prototype
FLOW = [('Add a title and category', 'The two required fields'), ('Autofill', 'One click on the sparkle'), ('Review', 'AI content highlighted'),
        ('Adjust', 'Regenerate, retone or clear'), ('Pick platforms', 'Where to list'), ('Preview and post', 'One last check')]
def flow():
    return ('<ol class="om-flow">' + ''.join(
        f'<li><span class="om-flow__n" aria-hidden="true">{i + 1}</span><div><p class="om-flow__t">{t}</p><p class="om-flow__d">{d}</p></div></li>'
        for i, (t, d) in enumerate(FLOW)) + '</ol>')


# v3 (the team's listing page before I joined; image from the lead designer's published case study) against the final design
CHANGES = [  # area, v3, my design
    ('Placement', 'A small Autofill link above the title, a sparkle in the description toolbar and an AI Generator button under the images: AI in three places.',
     'One entry point in a title bar, beside the two fields autofill needs, fixed as sellers scroll.'),
    ('Clarity', 'AI-written text looked the same as anything the seller typed.',
     'Purple highlights on everything AI writes, and a status that invites edits.'),
    ('Control', 'Feedback on each suggestion, spread across the page.',
     'Regenerate, change tone and clear fields, together under More options.'),
]
def compare():
    n = _num()
    imgs = ('<div class="om-cmp__imgs">'
            '<div><p class="om-cmp__k">Before: v3</p><img class="om-shot" src="assets/screens/00-v3-listing-page.jpg" width="1600" height="1139" loading="lazy" '
            'alt="The v3 listing page: tabs for general information, product details, pricing, shipping and platform integrations; a small Autofill link above the listing title, a sparkle in the description toolbar, and an AI Generator button under the product photos."></div>'
            f'<div><p class="om-cmp__k">After: v4</p><img class="om-shot" src="assets/screens/{SHOTS["filled"][0]}" width="1600" height="1183" loading="lazy" alt="{SHOTS["filled"][1]}"></div>'
            '</div>')
    rows = ('<dl class="om-cmp__rows">' + ''.join(
        f'<div class="om-cmp__row"><dt>{a}</dt><dd><span class="om-cmp__tag">v3</span>{b}</dd><dd><span class="om-cmp__tag om-cmp__tag--me">v4</span>{c}</dd></div>'
        for a, b, c in CHANGES) + '</dl>')
    return (f'<figure class="pm-frame"><div class="pm-frame__stage om-stage om-cmp">{imgs}{rows}</div>'
            + _cap(n, 'The v3 listing page (left) and the launch version (right): what changed in placement, clarity and control.') + '</figure>')

STATS_TEAM = [('60%', 'Less time to create a listing, on average'), ('20%', 'More accurate listings'),
              ('78%', 'Of testers satisfied with autofill')]

def impact_box():
    """Team results in their own container, so they read first."""
    return f'<section class="om-impact" aria-label="Results">{stats(STATS_TEAM, " pm-stats--sm cs-stats")}{team_source()}</section>'

def callout(label, text):
    """A key insight, set large on a surface panel (the opportunity keeps the accent tint)."""
    return f'<div class="om-callout"><p class="om-callout__k">{label}</p><p class="om-callout__t">{text}</p></div>'

# ---------- content ----------
SECTIONS = [('overview', 'Overview'), ('problem', 'The problem'), ('role', 'My role'), ('discover', 'Research'), ('concept', 'Concept'),
            ('placement', 'Placement'), ('clarity', 'Clarity'), ('control', 'Control'), ('publish', 'Publishing'), ('impact', 'Impact &amp; reflection')]

BODY = ''.join([
    section('overview', 'Overview', 'I designed how AI fits into the moment sellers create a listing.',
        lede('OmniSynkAI helped small and mid-sized sellers list products across marketplaces like Amazon, eBay and Etsy. Its listing page made them fill in every field by hand.',
             'I joined the design team as AI autofill became a launch feature, and focused on three things: where autofill lives on the page, how sellers tell AI content from their own, and how they steer what it writes.')
        + shot('filled', 'The listing after autofill: the title bar, purple highlights for AI content, and More options for steering it.')
        + impact_box()),

    section('problem', 'The problem', 'Sellers were spending their time, or their money, just to list products.',
        lede('Small businesses grow by selling on as many platforms as they can, which means listing the same product again and again, each time with different requirements. Our UX research team’s survey of 456 sellers showed what that costs.')
        + stats([('25%', 'Called syncing listings across platforms a nightmare'), ('27.9%', 'Of multi-platform sellers hired virtual assistants to keep up'),
                 ('25.2%', 'Outsourced listing management to third parties')], ' pm-stats--sm cs-stats')
        + '<p class="pm-meta-text om-source">From the team’s seller survey (456 responses), led by UX research.</p>'
        + callout('What the data showed', 'Listing by hand was slow, led to errors and inconsistencies, and left listings hard to find in search.')
        + f'<section class="om-ns" aria-labelledby="om-ns-h"><p class="om-ns__label" id="om-ns-h">{_l("sparkles")}The opportunity</p>'
          '<p class="om-ns__text">Design an autofill feature that brings AI into the listing flow, helping sellers quickly create compelling, search-friendly listings and raising listing quality across the platform.</p></section>'),

    section('role', 'My role', 'I made autofill findable, clear and easy to steer.',
        lede('The team had already explored three versions of the listing flow. The same three gaps came up in all of them, and closing them became my focus.')
        + framed(versions(), 'How the listing flow evolved, and where I joined.')
        + callout('Three gaps', 'Sellers missed autofill, couldn’t tell what it wrote, and wanted more say in the result.')
        + focus()
        + '<h3 class="cs-h3">I tackled them in three phases.</h3>'
        + framed(process(), 'Discover, conceptualize, design.')),

    section('discover', 'Research', 'I started by asking where AI could actually help.',
        lede('Before designing anything, I needed to uncover where AI could help sellers most, and how we could guide them to a listing they’re happy with.',
             'I partnered with UX research to pull the survey and interview findings and spot the gaps, and collaborated with engineers and product managers to map the AI’s constraints and feasibility. Knowing its limits early kept the design honest.',
             'To fill the gaps, I ran desk research on how people use AI tools, and mapped a SWOT analysis of two competitors’ AI listing features.')
        + items([('Shopify', 'Interactive feedback loops let sellers react to what AI writes and steer the next version.'),
                 ('Trustana', 'AI enrichment fills out product data to improve search and conversion.')], grid=True)
        + need('SWOT analysis of Shopify’s and Trustana’s AI listing features.', 'Your SWOT diagram for Shopify and Trustana, redrawn', '16x9')
        + '<h3 class="cs-h3">I turned five findings into five design priorities.</h3>'
        + lede('Every priority traces back to a finding, so each decision that followed had a reason behind it.')
        + findings()),

    section('concept', 'Concept', 'I mapped the flow before designing a screen.',
        lede('With priorities set, I defined how autofill should work: the flows for new and returning sellers, the triggers that start it, and a feedback loop for refining what it writes. Three qualities guided every choice.')
        + items([('Simplicity', 'Sellers understand how to start at a glance.'),
                 ('Flexibility', 'The experience feels effortless, even within the AI’s limits.'),
                 ('Better with feedback', 'Results improve as sellers react to them.')], grid=True)
        + lede('The key trigger came from the data: AI needs only a title and a category to draft a listing. So I built the flow around those two fields, from the first click to a published listing.')
        + framed(flow(), 'The flow I designed, from two required fields to a published listing.')
        + '<h3 class="cs-h3">My first concept, and what it taught me.</h3>'
        + lede('I built my first layout within OmniSynkAI’s design system:')
        + items([('A sidebar card', 'Invited sellers to “Try listing with Autofill,” with per-platform publishing toggles below it.'),
                 ('Feedback on every field', 'Each AI-written field had controls to browse versions, rate them and regenerate.'),
                 ('A compare message', 'After autofill, a message invited sellers to compare versions.')])
        + lede('Reviewing it against my priorities, the AI’s limits and the team’s plans, I took three lessons into the final design, one for each gap. Here’s how the launch version compares with v3.')
        + compare()),

    section('placement', 'Placement', 'I moved autofill to where every listing starts.',
        lede('In v3, autofill was a small link above the title, with more AI buttons elsewhere on the page; in my first concept, it sat in a sidebar card. Either way, it was apart from the fields it needed. Mapping it against the flow showed why sellers missed it: they start a listing at the top, with a title and a category, which is exactly what autofill needs.',
             'So I moved autofill into a title bar, right beside those two fields. This became the entry point in the final design.')
        + items([('Unlocks when ready', 'The sparkle button lights up once the title and category are filled in.'),
                 ('Explains itself', 'One line tells sellers what autofill does for them.'),
                 ('Always in reach', 'The bar stays fixed as sellers scroll, keeping the AI controls close.')], grid=True)
        + pair(shot('empty', 'Autofill sits beside the two fields it needs, and unlocks once both are filled in.'),
               shot('filling', 'A short dialog shows the AI at work, and lets sellers cancel.'))),

    section('clarity', 'Clarity', 'I created a visual language for AI content.',
        lede('Earlier versions didn’t separate AI content from manual input, so sellers couldn’t tell what to double-check, or which fields they still had to fill in. I designed three cues that carried into the final design:')
        + items([('Purple highlights', 'Everything AI writes, like the brand and tags, is highlighted, so sellers know exactly what to review.'),
                 ('A clear status', 'After autofill, the title bar reads “Listing Autofilled, feel free to edit details,” inviting edits instead of blind trust.'),
                 ('Only what’s new', 'When AI rewrites part of a listing, only the new content is highlighted; what sellers already reviewed goes back to plain text.')])
        + pair(shot('filled', 'After autofill: AI content highlighted, and a status that invites edits.'),
               shot('retoned', 'After a change, only the new tags are highlighted.'))),

    section('control', 'Control', 'I fit the feedback loop to what the AI could do.',
        lede('My first concept put feedback on every field: browse versions, thumbs up or down, regenerate. It was more than our AI model could reliably support, and more than sellers needed on every field. I simplified it to the three actions sellers actually reach for, and gathered them under one More options menu in the title bar, where they’re always in reach. We refined the options together as a team, and this became how sellers steer AI in the final design.')
        + items([('Regenerate', 'Not quite right? Ask the AI for a new draft.'),
                 ('Change tone', 'Pick from seven tones, from formal to playful, to match the seller’s brand voice.'),
                 ('Clear fields', 'Start over by hand, with a confirmation first, since it can’t be undone.')], grid=True)
        + pair(shot('menu', 'More options: regenerate, change tone or clear fields.'),
               shot('tone', 'Seven tones, from formal to playful.'))
        + shot('clear', 'Clearing autofilled content asks for confirmation first.')),

    section('publish', 'Publishing', 'One listing, published everywhere.',
        lede('Autofill hands off to our publishing flow. Instead of the per-platform toggles in my first concept, sellers choose their marketplaces when they publish, which leaves room for more platforms, then preview the listing on each and post to all of them at once.')
        + pair(shot('platforms', 'Choose the marketplaces to list on.'),
               shot('confirm', 'A last check, with a preview, before posting.'))),

    section('impact', 'Impact &amp; reflection', 'Sellers found autofill, and liked using it.',
        lede('Autofill shipped in the September 2024 soft launch with the title bar entry point, purple AI cues and the More options menu in place. In pre-launch testing, 78% of testers were satisfied with autofill, and after launch, average listing time fell by 60% across the listing flow.')
        + impact_box()
        + lede('OmniSynkAI has since wound down, but the work showed me how AI can take on the tedious parts of selling while sellers keep ownership of their listings.')
        + '<h3 class="cs-h3">What I learned</h3>'
        + '<div class="cs-pair om-trio">'
        + panel('Start from what’s still open', '<p>Studying three earlier versions first meant I could focus on the problems no one had solved yet.</p>', ' pm-panel--tonal', 'p-l1')
        + panel('Design around the model’s limits', '<p>Knowing what the AI could reliably do turned a busy feedback system into three clear actions.</p>', ' pm-panel--tonal', 'p-l2')
        + panel('Make AI visible, not magic', '<p>Sellers trust AI more when they can see what it wrote and change it easily.</p>', ' pm-panel--tonal', 'p-l3')
        + '</div>'
        + '<p class="pm-meta-text om-credit">Designed with the OmniSynkAI team: the lead designer, a fellow product designer, UX research, product and engineering. Screens from the approved prototype, shared with permission.</p>'),
])

HEADER = '''  <header class="cs-head">
    <ul class="cs-badges" aria-label="Disciplines"><li class="pm-badge">Product design</li><li class="pm-badge">AI</li><li class="pm-badge">Web</li></ul>
    <h1 class="cs-title">Introducing AI autofill to cut e-commerce listing time by 60%</h1>
  </header>

  <section class="cs-facts" aria-label="Project details"><dl class="cs-facts__list">
    <div><dt>Role</dt><dd>Product design intern</dd></div>
    <div><dt>Team</dt><dd>3 product designers</dd><dd>1 UX researcher</dd><dd>1 PM</dd><dd>3 engineers</dd></div>
    <div><dt>Timeline</dt><dd>July – September 2024</dd></div>
    <div><dt>Skills</dt><dd>AI interaction design</dd><dd>Competitive analysis</dd><dd>Prototyping</dd></div>
  </dl></section>'''

TLDR = f'''      <dl class="cs-tldr__rows">
        <div class="cs-tldr__row"><dt>Background</dt><dd>OmniSynkAI helped sellers list products across marketplaces. Its listing page made them fill in every field by hand.</dd></div>
        <div class="cs-tldr__row"><dt>Problem</dt><dd>In a survey of 456 sellers, a quarter called cross-platform listing a nightmare, and many paid assistants to keep up.</dd></div>
        <div class="cs-tldr__row"><dt>My role</dt><dd>I joined the team on the launch version of AI autofill, focusing on where it lives on the page, how AI content is marked, and how sellers steer it.</dd></div>
        <div class="cs-tldr__row"><dt>Outcome</dt><dd>Autofill shipped beside the fields it needs, with purple cues for AI content and a More options menu to steer it. Listing time fell 60%.</dd></div>
      </dl>
      {stats(STATS_TEAM, ' pm-stats--sm cs-tldr__stats')}
      {team_source()}'''

CSS = r"""
/* Prototype stills: the screen on the grey figure stage, lifted slightly */
.om-stage { padding: var(--space-4); }
.om-shot { display: block; width: 100%; height: auto; border-radius: var(--radius-sm); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); }
.om-pair { display: grid; gap: var(--space-6); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .om-pair { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-5); } }
.cs-section > .om-pair, .cs-section > .pr-ig, .cs-section > .om-focus { margin-block: var(--space-2); }
.cs-points--plain li { grid-template-columns: minmax(0, 1fr); }
.cs-stats .pm-stats__item { justify-content: flex-end; }
.om-source { margin: var(--space-3) 0 0; max-width: 60ch; }
.cs-section > .pm-stats + .om-source { margin-top: calc(var(--space-3) - var(--space-6)); }
.om-credit { margin: 0; }
.om-need .pm-media__fallback span:last-child { max-width: 36ch; text-align: center; }
@container (min-width: 768px) { .om-trio { grid-template-columns: repeat(3, minmax(0, 1fr)); } }

/* Shared inner-card look for the HTML graphics */
.om-stage:has(.om-proc), .om-stage:has(.om-flow), .om-stage:has(.om-ver) { container-type: inline-size; padding: var(--space-5); }
.om-proc__step, .om-flow li, .om-ver__v { border-radius: var(--radius-md); background: var(--color-bg-elevated); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); }

/* Process: three phases, side by side from a 640px stage */
.om-proc { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-3); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 640px) { .om-proc { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.om-proc__step { padding: var(--space-5); display: grid; gap: var(--space-2); align-content: start; }
.om-proc__k { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-proc__step h4 { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); letter-spacing: 0; color: var(--color-text-primary); }
.om-proc__step ul { margin: 0; padding-left: 1.1em; display: grid; gap: var(--space-1); font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }

/* Versions: four across from a 720px stage, two across from 440px; mine gets the selection ring */
.om-ver { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-3); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 440px) { .om-ver { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@container (min-width: 720px) { .om-ver { grid-template-columns: repeat(4, minmax(0, 1fr)); } }
.om-ver__v { padding: var(--space-4); display: grid; gap: var(--space-2); align-content: start; }
.om-ver__v.is-mine { background: var(--color-action-selected-bg); box-shadow: inset 0 0 0 2px var(--color-action-primary), var(--shadow-sm); }
.om-ver__k { margin: 0; display: flex; flex-wrap: wrap; align-items: baseline; gap: var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-ver__me { margin-left: auto; }
.om-ver__d { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.om-ver__l { margin: 0; padding-top: var(--space-2); border-top: 1px solid var(--color-border-subtle); display: grid; gap: 2px; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-primary); }
.om-ver__l span { font-family: var(--font-meta); font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-tertiary); }

/* Focus areas: three cards across from a 768px column */
.om-focus { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-3); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .om-focus { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.om-focus__c.pm-card--outlined, .om-focus__c.pm-card--outlined:hover { padding: var(--space-5); gap: var(--space-1); cursor: default; box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); }
.om-focus__c .pm-card__title, .om-focus__c .pm-card__summary { padding-inline: 0; }
.om-focus__k { margin: 0 0 var(--space-1); font-family: var(--font-meta); font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-tertiary); }

/* The opportunity: the page's one accent-tinted statement, like Procense's North Star */
.om-ns { margin: var(--space-2) 0; padding: var(--space-6); border-radius: var(--radius-md); background: var(--color-action-selected-bg); box-shadow: var(--shadow-sm); display: grid; gap: var(--space-3); }
.om-ns__label { margin: 0; display: flex; align-items: center; gap: var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-ns__label .pm-icon { width: 16px; height: 16px; }
.om-ns__text { margin: 0; font-size: var(--type-h3); line-height: var(--line-h3); font-weight: var(--weight-medium); color: var(--color-text-primary); text-wrap: balance; }

/* Autofill flow: six numbered steps, three across from 520px, six across from 900px */
.om-flow { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-3); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 520px) { .om-flow { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@container (min-width: 900px) { .om-flow { grid-template-columns: repeat(6, minmax(0, 1fr)); } }
.om-flow li { display: flex; gap: var(--space-3); align-items: flex-start; padding: var(--space-4); }
@container (min-width: 900px) { .om-flow li { flex-direction: column; } }
.om-flow__n { flex: none; width: 24px; height: 24px; display: grid; place-items: center; border-radius: 50%; background: var(--color-action-primary); color: var(--color-text-on-accent); font-size: var(--type-label); line-height: 1; font-variant-numeric: tabular-nums; }
.om-flow__t { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-flow__d { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }

/* v3 vs my design: two screens, then one row per area (side by side from 768px) */
.om-cmp { container-type: inline-size; display: grid; gap: var(--space-5); padding: var(--space-5); }
.om-cmp__imgs { display: grid; gap: var(--space-4); grid-template-columns: minmax(0, 1fr); align-items: start; }
@container (min-width: 640px) { .om-cmp__imgs { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.om-cmp__k { margin: 0 0 var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-cmp__rows { margin: 0; display: grid; gap: var(--space-3); }
.om-cmp__row { padding: var(--space-4); border-radius: var(--radius-md); background: var(--color-bg-elevated); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); display: grid; gap: var(--space-2); }
@container (min-width: 640px) { .om-cmp__row { grid-template-columns: 7rem minmax(0, 1fr) minmax(0, 1fr); gap: var(--space-4); } }
.om-cmp__row dt { font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-cmp__row dd { margin: 0; display: grid; gap: var(--space-1); align-content: start; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.om-cmp__row dd:last-child { color: var(--color-text-primary); }
.om-cmp__tag { justify-self: start; font-family: var(--font-meta); font-size: var(--type-label); line-height: var(--line-label); color: var(--color-text-tertiary); }
.om-cmp__tag--me { color: var(--color-text-link); font-weight: var(--weight-medium); }

/* Results: a container so the numbers stand out */
.om-impact { margin: var(--space-2) 0; padding: var(--space-6); border-radius: var(--radius-md); background: var(--color-bg-surface); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); }
.om-impact .pm-stats { margin: 0; padding-top: 0; border-top: 0; }
.om-impact .om-source { margin-top: var(--space-4); }
/* Key insight: large text on a surface panel with a cobalt rule */
.om-callout { margin: var(--space-2) 0; padding: var(--space-5) var(--space-6); border-radius: var(--radius-md); background: var(--color-bg-surface); box-shadow: inset 3px 0 0 var(--color-action-primary), inset 0 0 0 1px var(--color-border-subtle); display: grid; gap: var(--space-2); }
.om-callout__k { margin: 0; display: flex; align-items: center; gap: var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-secondary); }
.om-callout__k .pm-icon { width: 16px; height: 16px; }
.om-callout__t { margin: 0; font-size: var(--type-h4, var(--type-body-lg)); line-height: var(--line-h4, var(--line-body-lg)); font-weight: var(--weight-medium); color: var(--color-text-primary); text-wrap: balance; }
/* Versions: the badge sits on the card's top-right edge */
.om-ver__v { position: relative; }
.om-ver__me { position: absolute; top: 0; right: var(--space-3); transform: translateY(-50%); margin: 0; background: var(--color-bg-elevated); box-shadow: inset 0 0 0 1px var(--color-action-primary), var(--shadow-xs); }
.om-stage:has(.om-ver) { padding-top: var(--space-6); }
/* Phases: short question and tags, with arrows between from 640px */
.om-proc__d { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.om-proc__arrow { display: none; color: var(--color-text-tertiary); align-self: center; justify-self: center; }
.om-proc__arrow .pm-icon { width: 20px; height: 20px; }
@container (min-width: 640px) { .om-proc { grid-template-columns: minmax(0, 1fr) 24px minmax(0, 1fr) 24px minmax(0, 1fr); gap: var(--space-2); } .om-proc__arrow { display: block; } }
/* Findings: the source as a badge, top right of each finding */
.om-fd__h { display: flex; align-items: flex-start; justify-content: space-between; gap: var(--space-3); }
.om-fd__h .pm-badge { flex: none; margin-top: 1px; }
"""

OMNI = dict(page_title='OmniSynkAI Case Study', out='omnisynkai/index.html', sections=SECTIONS, body=BODY, header=HEADER, tldr=TLDR, css=IG_CSS + CSS)

if __name__ == '__main__':
    print(len(C.render(OMNI)))
