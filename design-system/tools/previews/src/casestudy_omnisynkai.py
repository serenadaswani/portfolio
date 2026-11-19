"""OmniSynkAI AI autofill case study, on the same structure as the Procense and Mensio pages (casestudy.render).
Content: Serena's Framer case study (project-detail-omnisynkai-ai-autofill-feature, read 2026-11-19), reworded in this
site's voice. Media: stills from the approved prototype video (omnisynkai/figma/, PNG; assets/screens/, JPEG 1600px),
used with her PM's permission, design team credited. First pass, to be revised section by section with Serena.
Run: python3 design-system/tools/previews/src/casestudy_omnisynkai.py  ->  omnisynkai/index.html
"""
import casestudy as C
from casestudy import I, section, lede, panel, stats

def items(rows, grid=False):
    """Title + description list, no numbering (same as Procense)."""
    return (f'<ul class="cs-points cs-points--plain{" cs-points--grid" if grid else ""}">'
            + ''.join(f'<li><div><h4>{t}</h4><p>{d}</p></div></li>' for t, d in rows) + '</ul>')

# Prototype stills: file in assets/screens/, alt text
SHOTS = {
    'empty': ('01-empty-listing.jpg', 'Create a new listing page before autofill: a bar at the top reads “Save time with Autofill” beside empty Title and Product category fields and a sparkle button; Publish listing is disabled.'),
    'filling': ('02-autofill-in-progress.jpg', 'A “Filling out your listing” dialog over the page, with a tip that autofill saves businesses over 58 hours a year and a Cancel Autofill button.'),
    'filled': ('03-listing-autofilled.jpg', 'The listing after autofill: a Vitamin C Serum description, nine product photos, and the brand and tags highlighted in purple. The top bar reads “Listing Autofilled, feel free to edit details” with More options and Publish listing.'),
    'tone': ('04-change-tone.jpg', 'A Change Tone dialog with tone options: Formal, Persuasive, Humorous, Playful, Informative, Conversational and Informal, and a Confirm button.'),
    'retoned': ('05-tone-changed-new-tags.jpg', 'The listing after a tone change: the earlier tags are now plain and two new tags, #toning and #brightening, are highlighted in purple.'),
    'clear': ('06-clear-listing-confirmation.jpg', 'A confirmation dialog: “Are you sure you’d like to clear this listing? Clearing this form will remove all autofilled content. You won’t be able to undo this action.” with Cancel and Clear listing.'),
    'menu': ('07-more-options-menu.jpg', 'The More options menu open under the top bar, with Regenerate, Clear fields and Change tone.'),
    'platforms': ('08-select-platforms.jpg', 'A Select Platforms dialog with eBay, Depop, Amazon, TikTok, Mercari and Etsy, a “Why can’t I see all platforms?” hint and a Confirm button.'),
    'confirm': ('09-confirm-and-publish.jpg', 'A Confirm and publish dialog showing the listing will be posted on eBay and Amazon, with Preview listing and “Looks good, post” buttons.'),
    'done': ('10-listing-complete.jpg', 'A Listing Complete dialog: “Nice work, you just listed your first product with OmniSynkAI,” with Dashboard and List Another buttons.'),
}
_n = [0]
def shot(key, cap):
    _n[0] += 1
    f, alt = SHOTS[key]
    return (f'<figure class="pm-frame"><div class="pm-frame__stage om-stage"><img class="om-shot" src="assets/screens/{f}" width="1600" height="1183" loading="lazy" alt="{alt}"></div>'
            f'<figcaption class="pm-frame__caption"><span class="pm-frame__index">Fig. {_n[0]:02d}</span><span>{cap}</span></figcaption></figure>')
def pair(a, b):
    return f'<div class="om-pair">{a}{b}</div>'

SECTIONS = [('overview', 'Overview'), ('problem', 'The problem'), ('approach', 'Approach'), ('goals', 'Design goals'),
            ('solution', 'The solution'), ('accessibility', 'Accessibility'), ('reflection', 'Reflection')]

BODY = ''.join([
    section('overview', 'Overview', 'I brought AI autofill into the listing page sellers already used.',
        lede('OmniSynkAI is a B2B SaaS platform that helps e-commerce sellers manage their inventory across marketplaces. As a product design intern, I worked with product designers, UX researchers, product managers and engineers to add an AI autofill feature to its Inventory Listing page.',
             'Sellers enter a title and a category, and AI drafts the rest of the listing: the description, media, brand and tags. They can then regenerate it, change its tone or edit any field before publishing to the marketplaces they sell on.')
        + shot('filled', 'A listing drafted by AI autofill. AI-written brand and tags are highlighted in purple.')),

    section('problem', 'The problem', 'Sellers filled in every listing by hand, field by field.',
        lede('E-commerce sellers manage large inventories across several platforms, and each product needs a detailed listing. Filling in every field by hand is slow, and it invites errors, inconsistencies and missed chances to show up in search.',
             'That was an opportunity for OmniSynkAI, whose mission is to simplify complex e-commerce workflows: let AI do the first draft, so sellers spend their time checking a listing instead of writing it.')
        + '<div class="cs-pair">'
        + panel('For sellers', '<p>Listings that are faster to create and easier to find, so they can grow their business with more confidence.</p>', ' pm-panel--tonal', 'p-sellers')
        + panel('For OmniSynkAI', '<p>A reason for sellers to stay: better retention, less churn and more listings that succeed.</p>', ' pm-panel--tonal', 'p-business')
        + '</div>'),

    section('approach', 'Approach', 'I started with what we knew and what competitors were doing.',
        lede('I worked with UX researchers to pull common needs and pain points from existing research, and met with engineers and product managers to learn what the AI could and couldn’t do. Knowing its limits early kept the design honest.')
        + '<h3 class="cs-h3">Competitors showed where AI helps most.</h3>'
        + lede('To find where AI would add the most value in the listing flow, I studied the AI features of Shopify and Trustana.')
        + '<div class="cs-pair">'
        + panel('Shopify', '<p>Interactive feedback loops let sellers react to what the AI writes and steer the next version.</p>', '', 'p-shopify')
        + panel('Trustana', '<p>AI-assisted enrichment fills out product data to improve search, discoverability and conversion.</p>', '', 'p-trustana')
        + '</div>'
        + lede('Both pointed the same way: AI works best when sellers can react to it in real time and it’s tuned for how listings get found.')),

    section('goals', 'Design goals', 'Five priorities kept the AI helpful and out of the way.',
        lede('What I learned from research became the priorities for the design.')
        + items([('Easy to find', 'Make AI features intuitive and discoverable for sellers at every level of experience.'),
                 ('Clearly marked', 'Use visual cues to separate what AI wrote from what the seller entered.'),
                 ('Learns from feedback', 'Build in feedback loops that improve the model and keep sellers engaged.'),
                 ('Right place, right time', 'Bring AI into the key moments of the listing flow, without adding friction.'),
                 ('Seller in control', 'Let sellers edit and enter their own details at every step.')], grid=True)),

    section('solution', 'The solution', 'Autofill fits into the listing flow sellers already know.',
        lede('Working within OmniSynkAI’s design system, I redesigned the Inventory Listing page for new and existing sellers. It explains the value of autofill up front, shows progress while the AI works, marks what the AI wrote, and keeps the seller in control with options to regenerate, clear and change the tone.')
        + '<h3 class="cs-h3">Two fields are all it takes to start.</h3>'
        + lede('A bar at the top of the page invites sellers to save time with autofill. Once they add a title and a category, the sparkle button starts it, and a short dialog shows the AI at work.')
        + pair(shot('empty', 'Before autofill: a title and a category unlock the sparkle button.'),
               shot('filling', 'While the AI works, a dialog shows progress and lets sellers cancel.'))
        + '<h3 class="cs-h3">AI-written content is easy to spot.</h3>'
        + lede('The title bar confirms the listing was autofilled and invites edits. Brand and tags written by the AI are highlighted in purple, so sellers know what to check before they publish. The bar stays fixed as sellers scroll, keeping the title, category and autofill controls in reach.')
        + shot('filled', 'The autofilled listing, with AI-written fields marked.')
        + '<h3 class="cs-h3">Sellers stay in control of what the AI writes.</h3>'
        + lede('More options holds three ways to adjust the result: regenerate it, clear the fields, or change the tone so the listing matches the seller’s brand voice. Clearing asks for confirmation first, since it can’t be undone.')
        + pair(shot('menu', 'More options: regenerate, clear fields or change tone.'),
               shot('tone', 'Seven tones, from formal to playful.'))
        + pair(shot('retoned', 'After a tone change, only the new tags are highlighted.'),
               shot('clear', 'Clearing autofilled content asks for confirmation.'))
        + '<h3 class="cs-h3">One listing, published everywhere.</h3>'
        + lede('Publishing asks which marketplaces to list on, then shows a final check with a preview before the listing goes live.')
        + pair(shot('platforms', 'Choose the marketplaces to list on.'),
               shot('confirm', 'A last check, with a preview, before posting.'))
        + shot('done', 'Done: the listing goes live across the chosen platforms in a few minutes.')),

    section('accessibility', 'Accessibility', 'I reviewed the designs with an accessibility designer.',
        lede('I worked closely with an accessibility designer at OmniSynkAI to make sure the designs met accessibility standards. Together we reviewed the existing interface and checked it supported a wide range of needs, so the listing experience works for every seller.')),

    section('reflection', 'Reflection', 'Every AI feature has to earn its place.',
        lede('OmniSynkAI’s listing page and autofill have kept evolving since my internship, but the core of what we designed, and the goals behind it, stayed the same.')
        + '<h3 class="cs-h3">What I learned</h3>'
        + '<div class="cs-pair">'
        + panel('Balance innovation with intention', '<p>Every AI feature should serve a real seller need, and stay clear about what it did.</p>', ' pm-panel--tonal', 'p-l1')
        + panel('Keep people in control', '<p>Regenerate, clear and change tone let sellers shape the result instead of accepting it as is.</p>', ' pm-panel--tonal', 'p-l2')
        + '</div>'
        + '<h3 class="cs-h3">What’s next</h3>'
        + items([('Richer feedback', 'More ways for sellers to tell the AI what worked and what didn’t.'),
                 ('A guided tutorial', 'A walkthrough for sellers using autofill for the first time.'),
                 ('Smarter tools', 'New ways for AI to help sellers list faster and more confidently.')])
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
    <div><dt>Tools</dt><dd>Figma</dd><dd>Jira</dd><dd>Miro</dd></div>
  </dl></section>'''

TLDR = '''      <dl class="cs-tldr__rows">
        <div class="cs-tldr__row"><dt>Background</dt><dd>OmniSynkAI helps e-commerce sellers manage inventory across marketplaces like eBay, Amazon and TikTok Shop.</dd></div>
        <div class="cs-tldr__row"><dt>Problem</dt><dd>Sellers filled in every listing by hand: slow, inconsistent and easy to miss in search.</dd></div>
        <div class="cs-tldr__row"><dt>Approach</dt><dd>I drew on existing research, the AI’s real limits and competitors like Shopify and Trustana to set five design priorities.</dd></div>
        <div class="cs-tldr__row"><dt>Outcome</dt><dd>AI autofill drafts a listing from a title and a category, marks what it wrote, and lets sellers regenerate, retone or edit it.</dd></div>
      </dl>'''

CSS = r"""
/* Prototype stills: the screen on the grey figure stage, lifted slightly */
.om-stage { padding: var(--space-4); }
.om-shot { display: block; width: 100%; height: auto; border-radius: var(--radius-sm); box-shadow: inset 0 0 0 1px var(--color-border-subtle), var(--shadow-sm); }
.om-pair { display: grid; gap: var(--space-6); grid-template-columns: minmax(0, 1fr); }
@container (min-width: 768px) { .om-pair { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-5); } }
.cs-section > .om-pair { margin-block: var(--space-2); }
.cs-points--plain li { grid-template-columns: minmax(0, 1fr); }
.om-credit { margin: 0; }
"""

OMNI = dict(page_title='OmniSynkAI Case Study', out='omnisynkai/index.html', sections=SECTIONS, body=BODY, header=HEADER, tldr=TLDR, css=CSS)

if __name__ == '__main__':
    print(len(C.render(OMNI)))
