"""OmniSynkAI AI autofill case study, on the same structure as the Procense and Mensio pages (casestudy.render).
Content: Serena's case study presentation (OSAI_Case Study Presentation.pdf, 22 slides, read 2026-11-19: Discover ->
Conceptualize -> Design, research findings, early concept, final highlights, roadmap) and her Framer case study
(project-detail-omnisynkai-ai-autofill-feature), reworded in this site's voice. Media: stills from the approved prototype
video (omnisynkai/figma/, PNG; assets/screens/, JPEG 1600px), used with her PM's permission, design team credited.
Graphics still to supply are "Graphic needed" slots (need()); the process strip, findings -> priorities and the autofill
flow are drawn in HTML with design-system tokens.
Run: python3 design-system/tools/previews/src/casestudy_omnisynkai.py  ->  omnisynkai/index.html
"""
import casestudy as C
from casestudy import I, section, lede, panel
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
    n = _num()
    return (f'<figure class="pm-frame"><div class="pm-frame__stage om-stage"><img class="om-shot" src="assets/screens/{f}" width="1600" height="1183" loading="lazy" alt="{alt}"></div>'
            + _cap(n, cap) + '</figure>')
def pair(a, b):
    return f'<div class="om-pair">{a}{b}</div>'

def need(cap, what, ratio='16x10'):
    """A slot for a graphic Serena still needs to supply: says what goes there."""
    n = _num()
    return (f'<figure class="pm-frame om-need"><div class="pm-frame__stage"><div class="pm-media pm-media--{ratio}" role="img" aria-label="Graphic to come: {what}">'
            f'<div class="pm-media__fallback">{I["image"]}<span>Graphic needed</span><span>{what}</span></div></div></div>' + _cap(n, cap) + '</figure>')

def framed(art, cap):
    return f'<figure class="pm-frame"><div class="pm-frame__stage om-stage">{art}</div>' + _cap(_num(), cap) + '</figure>'

# Discover -> Conceptualize -> Design (slides 5–15)
PHASES = [
    ('Discover', 'Where can AI help sellers most?', ['Past research with UX research', 'AI’s strengths and limits with engineering and product', 'Desk research', 'SWOT of Shopify and Trustana']),
    ('Conceptualize', 'What should autofill do, and when?', ['Initial user flows', 'Interactions and triggers', 'Feedback loops to rate and tweak AI output']),
    ('Design', 'Where does AI live on the page?', ['New vs. returning seller flows', 'Listing page layouts in the design system', 'Final MVP prototype']),
]
def process():
    return ('<ol class="om-proc">' + ''.join(
        f'<li class="om-proc__step"><p class="om-proc__k"><span class="pm-meta-text">{i + 1:02d}</span>{name}</p><h4>{q}</h4>'
        '<ul>' + ''.join(f'<li>{o}</li>' for o in outs) + '</ul></li>'
        for i, (name, q, outs) in enumerate(PHASES)) + '</ol>')

# Research findings (slides 8–9) and the design priority each one set (Framer "Design Priorities")
FINDINGS = [
    ('Ease of use comes first', 'Desk research: sellers expect AI tools to feel intuitive from the first click.',
     'Easy to find', 'Make autofill discoverable and simple to start, for new and experienced sellers alike.'),
    ('Sellers need to see what changed', 'Desk research: visual cues help people tell AI content from their own.',
     'Clearly marked', 'Highlight everything AI wrote, so sellers know what to check.'),
    ('Time is of the essence', 'Desk research: sellers list in volume, so every extra step costs them.',
     'Right place, right time', 'Bring AI into the key moments of the listing flow, without adding friction.'),
    ('Feedback makes the model better', 'Competitors: feedback loops improve the AI and keep sellers engaged.',
     'Learns from feedback', 'Let sellers react to what AI writes, and use that to improve it.'),
    ('Sellers still want control', 'Competitors: even with AI, sellers can always list by hand.',
     'Seller in control', 'Every field stays editable, and sellers can regenerate, clear or retone at any time.'),
]
def findings():
    arrow = f'<span class="pr-ig__arrow" aria-hidden="true">{_l("arrow-right")}</span>'
    rows = ''.join(
        f'<li class="pr-ig__row"><div class="pr-ig__in"><p class="pr-ig__k">Finding</p><h4>{ft}</h4><p>{fd}</p></div>{arrow}'
        f'<div class="pm-card pm-card--outlined pr-ig__goal"><p class="pr-ig__k">Design priority</p><h4 class="pm-card__title">{gt}</h4><p class="pm-card__summary">{gd}</p></div></li>'
        for ft, fd, gt, gd in FINDINGS)
    return (f'<figure class="pr-ig"><div class="pr-ig__head" aria-hidden="true"><span>Finding</span><span></span><span>Design priority</span></div>'
            f'<ol class="pr-ig__list">{rows}</ol></figure>')

# The final autofill flow, from the prototype
FLOW = [('Add a title and category', 'The two required fields'), ('Autofill', 'One click on the sparkle'), ('Review', 'AI content highlighted'),
        ('Adjust', 'Regenerate, retone or clear'), ('Pick platforms', 'Where to list'), ('Preview and post', 'One last check')]
def flow():
    return ('<ol class="om-flow">' + ''.join(
        f'<li><span class="om-flow__n" aria-hidden="true">{i + 1}</span><div><p class="om-flow__t">{t}</p><p class="om-flow__d">{d}</p></div></li>'
        for i, (t, d) in enumerate(FLOW)) + '</ol>')

# ---------- content ----------
SECTIONS = [('overview', 'Overview'), ('problem', 'The problem'), ('discover', 'Discover'), ('priorities', 'Design priorities'),
            ('conceptualize', 'Conceptualize'), ('design', 'Design'), ('solution', 'The solution'), ('accessibility', 'Accessibility'),
            ('reflection', 'Reflection')]

BODY = ''.join([
    section('overview', 'Overview', 'AI autofill turned inventory listing from data entry into a quick review.',
        lede('OmniSynkAI is a B2B SaaS platform that helps e-commerce sellers list and manage inventory across marketplaces. Sellers create every listing on its Inventory Listing page, filling in product-specific fields by hand, one product and one platform at a time.',
             'As a product design intern, I designed AI autofill for that page, end to end and ahead of the MVP launch. Sellers now enter a title and a category, and AI drafts the rest: description, media, brand and tags. They review what it wrote, refine it with regenerate, tone and clear controls, then publish to every platform they sell on from one flow.')
        + shot('filled', 'A listing drafted by AI autofill. Everything AI wrote is highlighted in purple for the seller to review.')),

    section('problem', 'The problem', 'Listing by hand was slow, error-prone and hard to find in search.',
        lede('Sellers spent too much time entering product-specific fields for every item they listed. The more they listed, the more errors and inconsistencies crept in, and listings written in a hurry rarely did well in search.')
        + need('The Inventory Listing page before autofill: every field filled in by hand.', 'The original listing page, before AI (a screenshot or a simple redraw)')
        + f'<section class="om-ns" aria-labelledby="om-ns-h"><p class="om-ns__label" id="om-ns-h">{_l("sparkles")}The opportunity</p>'
          '<p class="om-ns__text">Design an autofill feature that brings AI into the listing flow, helping sellers quickly create compelling, search-friendly listings and raising listing quality across the platform.</p></section>'
        + '<div class="cs-pair">'
        + panel('For sellers', '<p>Listings that are faster to create and easier to find, so they can grow with more confidence.</p>', ' pm-panel--tonal', 'p-sellers')
        + panel('For OmniSynkAI', '<p>A reason for sellers to stay: better retention, less churn and more listings that succeed.</p>', ' pm-panel--tonal', 'p-business')
        + '</div>'
        + '<h3 class="cs-h3">I worked in three phases.</h3>'
        + lede('Each phase answered one question, and each answer shaped the next.')
        + framed(process(), 'Discover, conceptualize, design: the question each phase answered and what came out of it.')),

    section('discover', '01 · Discover', 'I started with what we already knew, and what AI could really do.',
        lede('Before designing anything, I wanted to know where AI could help sellers most, and where it couldn’t. I partnered with UX research to gather past findings on seller needs and pain points and to spot the gaps, and huddled with engineers and product managers to map the AI’s strengths and its limits.')
        + '<h3 class="cs-h3">Desk research showed what sellers expect from AI tools.</h3>'
        + items([('Ease of use', 'AI has to feel intuitive from the first click, or sellers won’t trust it.'),
                 ('Visual cues', 'People need to see which content AI wrote and which they wrote.'),
                 ('Speed', 'Time is of the essence: sellers list in volume, and every extra step adds up.')], grid=True)
        + '<h3 class="cs-h3">Then I studied AI in action on other platforms.</h3>'
        + lede('I mapped a SWOT analysis of Shopify’s and Trustana’s AI features, asking two questions: where can AI help sellers most, and how can we guide them to a listing they’re happy with?')
        + need('SWOT analysis of Shopify’s and Trustana’s AI listing features.', 'Your SWOT diagram for Shopify and Trustana (from Miro)', '16x9')
        + '<div class="cs-pair">'
        + panel('Shopify', '<p>Interactive feedback loops let sellers react to what AI writes and steer the next version.</p>', '', 'p-shopify')
        + panel('Trustana', '<p>AI-assisted enrichment fills out product data to improve search, discoverability and conversion.</p>', '', 'p-trustana')
        + '</div>'
        + lede('Three recommendations came out of it: build in feedback loops so the model keeps improving, let sellers keep control of listing by hand, and focus on the AI features sellers need most, built as one end-to-end flow.')),

    section('priorities', 'Design priorities', 'Five findings became five design priorities.',
        lede('Every priority traces back to something research showed, so each design decision had a reason behind it.')
        + findings()),

    section('conceptualize', '02 · Conceptualize', 'I defined the flow before designing a single screen.',
        lede('With priorities set, I mapped how autofill should work: the initial user flows, the interactions and triggers that start and update it, and feedback loops that let sellers rate and tweak what AI suggests.')
        + need('Early user flows for autofill: entry points, triggers and feedback loops.', 'Your initial user flow diagram or wireframes', '16x9')
        + '<h3 class="cs-h3">Three qualities guided every choice.</h3>'
        + items([('Simplicity', 'Sellers should understand how to start autofill at a glance.'),
                 ('Flexibility', 'Work around what the AI can’t do, and still give sellers an experience that feels effortless.'),
                 ('AI magic', 'Results that get better as sellers give feedback.')], grid=True)
        + lede('The result was one flow that starts with two fields and ends with a published listing.')
        + framed(flow(), 'The autofill flow, from two required fields to a published listing.')),

    section('design', '03 · Design', 'With the MVP close, the question was where AI lives on the page.',
        lede('Launch was coming up fast, so I focused on three questions: how sellers learn to start autofill and keep using it, how the experience differs for new and returning sellers, and where AI controls belong on a page that already held a lot.')
        + '<h3 class="cs-h3">The first concept put AI in a sidebar.</h3>'
        + lede('Working within OmniSynkAI’s design system, I explored layouts for the listing page. The first concept invited sellers to “Try listing with Autofill” from a card in the sidebar, with per-platform publishing toggles below it. Each AI-written field had its own controls to browse versions, give a thumbs up or down, and regenerate, and a message after autofill invited sellers to compare versions.')
        + need('First concept vs. final design.', 'Your early concept export, shown against the final screen in a before/after slider', '16x10')
        + '<h3 class="cs-h3">Three things shaped the final design.</h3>'
        + items([('A home for AI at the top of the page', 'Autofill moved into a title bar beside the two fields it needs, so sellers see where to start and the controls stay in reach as they scroll.'),
                 ('Feedback that fits the model', 'We adjusted to what the AI model could reliably do. Regenerate, change tone and clear fields gathered under one More options menu, giving sellers flexible ways to steer the result.'),
                 ('Room for more platforms', 'Per-platform toggles became a step for choosing platforms at publish time, so sellers can list across more than a few marketplaces.')])),

    section('solution', 'The solution', 'Autofill fits into the listing flow sellers already know.',
        lede('A grid layout separates the listing into clear sections and puts key information first. Purple highlights mark everything AI wrote, and short dialogs handle each step, from autofill to publishing, without leaving the page.')
        + '<h3 class="cs-h3">Two fields are all it takes to start.</h3>'
        + lede('The title bar invites sellers to save time with autofill. Once they add a title and a category, the sparkle button starts it, and a short dialog shows the AI at work.')
        + pair(shot('empty', 'Before autofill: a title and a category unlock the sparkle button.'),
               shot('filling', 'While the AI works, a dialog shows progress and lets sellers cancel.'))
        + '<h3 class="cs-h3">AI-written content is easy to spot.</h3>'
        + lede('The title bar confirms the listing was autofilled and invites edits. Brand and tags written by AI are highlighted in purple, so sellers know exactly what to check. The bar stays fixed as they scroll, keeping the title, category and AI controls in reach.')
        + shot('filled', 'The autofilled listing, with AI-written fields marked.')
        + '<h3 class="cs-h3">Sellers stay in control of what AI writes.</h3>'
        + lede('More options holds three ways to adjust the result: regenerate it, clear the fields, or change the tone so the listing matches the seller’s brand voice. Clearing asks for confirmation first, since it can’t be undone.')
        + pair(shot('menu', 'More options: regenerate, clear fields or change tone.'),
               shot('tone', 'Seven tones, from formal to playful.'))
        + pair(shot('retoned', 'After a tone change, only the new tags are highlighted.'),
               shot('clear', 'Clearing autofilled content asks for confirmation.'))
        + '<h3 class="cs-h3">One listing, published everywhere.</h3>'
        + lede('Publishing asks which marketplaces to list on, then shows a final check with a preview of the listing on each platform before it goes live.')
        + pair(shot('platforms', 'Choose the marketplaces to list on.'),
               shot('confirm', 'A last check, with a preview, before posting.'))
        + shot('done', 'Done: the listing goes live across the chosen platforms in a few minutes.')),

    section('accessibility', 'Accessibility', 'I reviewed the designs with an accessibility designer.',
        lede('I worked closely with an accessibility designer at OmniSynkAI to make sure the designs met accessibility standards. Together we reviewed the existing interface and checked it supported a wide range of needs, so the listing experience works for every seller.')),

    section('reflection', 'Reflection', 'AI works best when sellers stay in charge of it.',
        lede('By pairing AI with user-centered design, autofill makes listing easy and helps sellers publish high-quality listings. The listing page has kept evolving since my internship, but the goals behind it stayed the same.')
        + '<h3 class="cs-h3">What I learned</h3>'
        + '<div class="cs-pair">'
        + panel('Design around the model’s limits', '<p>Knowing what the AI could and couldn’t do early kept the design honest, and shaped simpler controls.</p>', ' pm-panel--tonal', 'p-l1')
        + panel('Lead your own research', '<p>Pulling together past research, desk research and competitors gave me the evidence for every decision.</p>', ' pm-panel--tonal', 'p-l2')
        + '</div>'
        + '<h3 class="cs-h3">What’s next</h3>'
        + items([('Usability testing', 'Test autofill with sellers to measure how well it works and where it falls short.'),
                 ('Richer feedback', 'Decide how detailed feedback should be, and give sellers more ways to share it.'),
                 ('A guided first run', 'A short tutorial that shows new sellers how to start autofill and what it can do.')])
        + need('A concept for the guided first run: a coach mark pointing sellers to autofill.', 'Your tutorial concept (the “Click Autofill my listing” coach mark)', '4x3')
        + '<p class="pm-meta-text om-credit">Designed with the product design team at OmniSynkAI. Screens from the approved prototype, shared with permission.</p>'),
])

HEADER = '''  <header class="cs-head">
    <ul class="cs-badges" aria-label="Disciplines"><li class="pm-badge">Product design</li><li class="pm-badge">AI</li><li class="pm-badge">Web</li></ul>
    <h1 class="cs-title">Introducing AI autofill to reduce e-commerce listing input by 50%</h1>
  </header>

  <section class="cs-facts" aria-label="Project details"><dl class="cs-facts__list">
    <div><dt>Role</dt><dd>Product design intern</dd></div>
    <div><dt>Team</dt><dd>Product designers</dd><dd>UX researchers</dd><dd>PMs and engineers</dd></div>
    <div><dt>Timeline</dt><dd>July – September 2024</dd></div>
    <div><dt>Skills</dt><dd>Competitive analysis</dd><dd>Interaction design</dd><dd>Prototyping</dd></div>
  </dl></section>'''

TLDR = '''      <dl class="cs-tldr__rows">
        <div class="cs-tldr__row"><dt>Background</dt><dd>OmniSynkAI helps e-commerce sellers list inventory across marketplaces, one product-specific form at a time.</dd></div>
        <div class="cs-tldr__row"><dt>Problem</dt><dd>Filling in every field by hand was slow and led to errors, inconsistent listings and poor search performance.</dd></div>
        <div class="cs-tldr__row"><dt>Approach</dt><dd>Past research, desk research and a SWOT of Shopify and Trustana set five design priorities; I mapped the flow, then found AI a home on the page.</dd></div>
        <div class="cs-tldr__row"><dt>Outcome</dt><dd>An MVP where two fields start autofill, AI content is clearly marked, and sellers regenerate, retone or edit before publishing everywhere.</dd></div>
      </dl>'''

CSS = r"""
/* Prototype stills: the screen on the grey figure stage, lifted slightly */
.om-stage { padding: var(--space-4); }
.om-shot { display: block; width: 100%; height: auto; border-radius: var(--radius-sm); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); }
.om-pair { display: grid; gap: var(--space-6); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .om-pair { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-5); } }
.cs-section > .om-pair, .cs-section > .pr-ig { margin-block: var(--space-2); }
.cs-points--plain li { grid-template-columns: minmax(0, 1fr); }
.om-credit { margin: 0; }
/* Slots for graphics still to supply */
.om-need .pm-media__fallback span:last-child { max-width: 36ch; text-align: center; }

/* Process: three phases, side by side from a 640px stage */
.om-stage:has(.om-proc), .om-stage:has(.om-flow) { container-type: inline-size; padding: var(--space-5); }
.om-proc { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-3); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 640px) { .om-proc { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.om-proc__step { padding: var(--space-5); border-radius: var(--radius-md); background: var(--color-bg-elevated); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); display: grid; gap: var(--space-2); align-content: start; }
.om-proc__k { margin: 0; display: flex; gap: var(--space-2); align-items: baseline; font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-proc__step h4 { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); letter-spacing: 0; color: var(--color-text-primary); }
.om-proc__step ul { margin: 0; padding-left: 1.1em; display: grid; gap: var(--space-1); font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }

/* The opportunity: the page's one accent-tinted surface, like Procense's North Star */
.om-ns { margin: var(--space-2) 0; padding: var(--space-6); border-radius: var(--radius-md); background: var(--color-action-selected-bg); box-shadow: var(--shadow-sm); display: grid; gap: var(--space-3); }
.om-ns__label { margin: 0; display: flex; align-items: center; gap: var(--space-2); font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-ns__label .pm-icon { width: 16px; height: 16px; }
.om-ns__text { margin: 0; font-size: var(--type-h3); line-height: var(--line-h3); font-weight: var(--weight-medium); color: var(--color-text-primary); text-wrap: balance; }

/* Autofill flow: six numbered steps, three across from 520px, six across from 900px */
.om-flow { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--space-3); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 520px) { .om-flow { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@container (min-width: 900px) { .om-flow { grid-template-columns: repeat(6, minmax(0, 1fr)); } }
.om-flow li { display: flex; gap: var(--space-3); align-items: flex-start; padding: var(--space-4); border-radius: var(--radius-md); background: var(--color-bg-elevated); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-xs); }
@container (min-width: 900px) { .om-flow li { flex-direction: column; } }
.om-flow__n { flex: none; width: 24px; height: 24px; display: grid; place-items: center; border-radius: 50%; background: var(--color-action-primary); color: var(--color-text-on-accent); font-size: var(--type-label); line-height: 1; font-variant-numeric: tabular-nums; }
.om-flow__t { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); font-weight: var(--weight-medium); color: var(--color-text-primary); }
.om-flow__d { margin: 0; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
"""

OMNI = dict(page_title='OmniSynkAI Case Study', out='omnisynkai/index.html', sections=SECTIONS, body=BODY, header=HEADER, tldr=TLDR, css=IG_CSS + CSS)

if __name__ == '__main__':
    print(len(C.render(OMNI)))
