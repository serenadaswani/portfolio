from lib import h
NAME = 'Typeface'; GROUP = 'Foundations'; HEIGHT = 2000; WIDTH = 1100
SUB = 'Instrument Sans for everything, metadata included (v1.8): before/after against Geist, and the full ramp with live metrics.'

def col(cls, tag):
    return (f'<div class="tf-col {cls}"><p class="pm-spec__cap tf-tag">{tag}</p>'
            '<p class="tf-d">Making complex systems legible</p>'
            '<p class="tf-h2">The problem</p>'
            '<p class="tf-h4">Review queue for model evaluations</p>'
            '<p class="tf-b">Reviewers spent most of their time deciding what to look at, not reviewing it. 0123456789</p>'
            '<div class="tf-ui"><span class="pm-btn pm-btn--primary pm-btn--sm">View project</span><span class="pm-btn pm-btn--secondary pm-btn--sm">Download PDF</span></div>'
            '<p class="pm-meta-text" style="margin:var(--space-3) 0 0">2024 · AI tooling · Fig. 03</p></div>')

RAMP = [('display-xl', 'Making complex systems legible'), ('display-lg', 'Designing the review queue'), ('h1', 'Selected work'), ('h2', 'The problem'),
        ('h3', 'What we tried first'), ('h4', 'Constraints'), ('body-lg', 'Reviewers spent most of their time triaging, not reviewing.'),
        ('body-md', 'We shipped the queue in three stages, starting with the riskiest assumption.'), ('body-sm', 'Enterprise platform, lead designer.'),
        ('label', 'Where you’re hiring for.'), ('caption', 'Figure caption and supporting notes.')]

BODY = (h('Before / after · same content, same sizes') +
        '<div class="tf-grid">' + col('tf-geist', 'Before · Geist, −0.045 / −0.03em') + col('tf-inst', 'After · Instrument Sans, −0.025 / −0.015em, display 90% width') + '</div>' +
        h('Ramp · Instrument Sans, with the metadata voice (metrics read live)') +
        '<div class="tf-ramp">' + ''.join(f'<div class="tf-row"><span class="pm-meta-text tf-spec" data-s="{n}">{n}</span><p class="{n}">{t}</p></div>' for n, t in RAMP) +
        '<div class="tf-row"><span class="pm-meta-text tf-spec">meta · label 400</span><p class="pm-meta-text" style="margin:0">2024.02 – 2024.11 · v2.1 · 01 02 03 · 0:42 / 3:10</p></div></div>')
STYLE = ('@import url("https://fonts.googleapis.com/css2?family=Geist:wght@400;500&display=swap");'
         '.tf-grid{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-10)}'
         '.tf-col{border-top:1px solid var(--color-border-default);padding-top:var(--space-3)}'
         '.tf-tag{margin:0 0 var(--space-5)}'
         '.tf-col p{margin:0}'
         '.tf-d{font-size:56px;line-height:1.07;font-weight:500;margin-bottom:var(--space-5)!important}'
         '.tf-h2{font-size:var(--type-h2);line-height:var(--line-h2);font-weight:500;margin-bottom:var(--space-3)!important}'
         '.tf-h4{font-size:var(--type-h4);line-height:var(--line-h4);font-weight:500;margin-bottom:var(--space-2)!important}'
         '.tf-b{font-size:var(--type-body-md);line-height:var(--line-body-md);color:var(--color-text-secondary);max-width:40ch}'
         '.tf-ui{display:flex;gap:var(--space-2);margin-top:var(--space-4)}'
         '.tf-geist,.tf-geist .pm-btn{font-family:"Geist",sans-serif}'
         '.tf-geist .tf-d{letter-spacing:-0.045em}.tf-geist .tf-h2{letter-spacing:-0.03em}.tf-geist .tf-h4{letter-spacing:-0.015em}'
         '.tf-inst .tf-d{letter-spacing:var(--tracking-display);font-stretch:var(--font-width-display)}.tf-inst .tf-h2{letter-spacing:var(--tracking-heading)}.tf-inst .tf-h4{letter-spacing:var(--tracking-h4)}'
         '.tf-ramp{display:grid;gap:var(--space-4)}'
         '.tf-row{display:grid;grid-template-columns:200px 1fr;gap:var(--space-6);align-items:baseline;padding-top:var(--space-3);border-top:1px solid var(--color-border-subtle)}'
         '.tf-row p{margin:0}'
         '@media (max-width:720px){.tf-grid{grid-template-columns:1fr}.tf-row{grid-template-columns:1fr;gap:var(--space-1)}}')
PAIRS = [('heading', '--color-text-primary', '--color-bg-canvas', 4.5), ('body', '--color-text-secondary', '--color-bg-canvas', 4.5), ('meta', '--color-text-tertiary', '--color-bg-canvas', 4.5)]
SCRIPT = r'''
function tf(){document.querySelectorAll('[data-s]').forEach(function(e){var p=e.nextElementSibling,c=getComputedStyle(p);
  e.textContent=e.dataset.s+' · '+parseFloat(c.fontSize)+'/'+Math.round(parseFloat(c.lineHeight))+' · '+c.fontWeight+' · '+(c.letterSpacing==='normal'?'0':(parseFloat(c.letterSpacing)/parseFloat(c.fontSize)).toFixed(3)+'em')+(c.fontStretch&&c.fontStretch!=='100%'&&c.fontStretch!=='normal'?' · '+c.fontStretch:'');});}
tf(); if(document.fonts)document.fonts.ready.then(tf); pmCheck();
'''
README = r'''
# Typeface

Instrument Sans is the only typeface. It became the primary face in v1.4, and from v1.8 it also sets metadata, replacing Geist Mono, which read as code. This card keeps the before and after on record, plus the full ramp with metrics read live from the rendered text.

## Anatomy
- **Primary**: Instrument Sans, variable: weights 400–700, width 75–100%, with italics. Loaded from Google Fonts. The fallback is system `sans-serif`.
- **Metadata voice** (`font-meta`): Instrument Sans 400 at `type-label` (13px), tertiary, with tabular figures. It sets years, dates, counts, versions, numbering, time codes and URL prefixes. Size, weight and colour set it apart from reading text; there is no second family.

## Why Instrument Sans
- **Distinctiveness.** Geist is strongly associated with Vercel, so a system set in it reads as a Vercel derivative. Instrument Sans is a slightly narrow grotesque with more editorial warmth, and it's recognisable without being decorative.
- **Editorial headlines.** The width axis allows condensed display type (`font-width-display` 90%), which is the Stripe-like headline character the brief asked for, without a second family.
- **One family.** v1.4–v1.7 paired it with Geist Mono for metadata. In v1.8 that was dropped: the mono read as code, and one family looks calmer and more modern. Tabular figures keep years and counts aligned.

## Variants
Weights in use: 400 (reading), 500 (names and actions), 600 (wordmark only). Width: 90% for `display-xl` and `display-lg`, 100% everywhere else. Italic is available for emphasis in prose.

## Sizes
The type scale is unchanged (same sizes and line heights). Tracking changed:

| Style | Before (Geist) | After (Instrument Sans) |
|---|---|---|
| display-xl / display-lg | −0.045em | −0.025em + 90% width |
| h1 / h2 | −0.03em | −0.015em |
| h3 | −0.02em | −0.01em |
| h4 | −0.015em | −0.005em |
| body, label, caption | 0 | 0 |

## States
n/a.

## Themes
Same in both. Instrument Sans at 400 holds up on midnight without needing a heavier weight.

## Responsive behavior
Display sizes step up at 768px and 1024px as before. The 90% width applies at every size, so long headlines wrap later on mobile.

## Accessibility
- UI labels stay at 500 (checked at 14px, where they render as firmly as Geist 500 did). No text in the system drops below 12px, except the non-essential `micro`.
- Condensed width is only for display sizes (≥36px). Reading text is never condensed.
- Sizes are rem and line heights are unitless, so user font settings and text-spacing overrides still work.

## Token dependencies
`font-sans` (Instrument Sans) · `font-meta` (Instrument Sans, metadata) · `font-width-display` `font-width-text` · `tracking-display|heading|h3|h4|body|label` · all `type-*` and `line-*` · `weight-regular|medium|semibold`
'''
