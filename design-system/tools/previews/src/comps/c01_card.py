from lib import I, cell, h, frames, img
NAME = 'Card'; GROUP = 'Containers'; HEIGHT = 2400; WIDTH = 1100
SUB = 'Frameless editorial card: hairline image well, mono metadata, title, summary. Outlined, featured, horizontal, compact, locked.'

def card(cls='', key='queue', title='Review queue for model evaluations', eyebrow='2024 · AI tooling', state='', current=False, badges=True, media=True,
         summary='Cut median triage time by turning ad-hoc review into a ranked, explainable queue.'):
    cur = ' aria-current="page"' if current else ''
    return (f'<article class="pm-card{cls}{state}">' +
            (f'<div class="pm-media pm-card__media">{img(key, alt="")}</div>' if media else '') +
            f'<p class="pm-card__eyebrow">{eyebrow}</p>'
            f'<h3 class="pm-card__title"><a href="#c"{cur}>{title}</a></h3>'
            f'<p class="pm-card__summary">{summary}</p>' +
            ('<ul class="pm-card__meta" aria-label="Disciplines"><li class="pm-badge">Research</li><li class="pm-badge">Interaction</li></ul>' if badges else '') +
            '</article>')

GRID = ('<div style="padding:var(--space-6) var(--space-4)"><ul class="card-grid" role="list">' +
        '<li>' + card() + '</li>' +
        '<li>' + card(key='grid', title='One token source for four product teams', eyebrow='2023 · Design systems', summary='A semantic token layer that let teams theme without forking components.') + '</li>' +
        '<li>' + card(key='form', title='Permissions console for operators', eyebrow='2022 · Internal platform', summary='Replaced a 40-field form with role templates and an audit trail.') + '</li>' +
        '</ul></div>')
LOCKED = ('<article class="pm-card pm-card--locked"><div class="pm-media pm-card__media" role="img" aria-label="Image withheld"><div class="pm-media__fallback">' + I['lock'] + '<span>Visuals withheld under NDA</span></div></div>'
          '<p class="pm-card__eyebrow">2021 · Fintech</p><h3 class="pm-card__title">Payments platform</h3>'
          '<p class="pm-card__summary">Case study available on request.</p><ul class="pm-card__meta"><li class="pm-badge pm-badge--warning">Under NDA</li></ul></article>')
ERROR = ('<article class="pm-card"><div class="pm-media pm-card__media" role="img" aria-label="Image failed to load"><div class="pm-media__fallback">' + I['broken'] + '<span>Image unavailable</span></div></div>'
         '<p class="pm-card__eyebrow">2024 · AI tooling</p><h3 class="pm-card__title"><a href="#c">Review queue for model evaluations</a></h3><p class="pm-card__summary">The card still works when the image fails.</p></article>')

BODY = (h('Grid · 3 / 2 / 1 per row by container width') + frames(GRID, 1024, 375) +
        h('States') + '<div class="pm-spec__grid">' +
        cell(card(), 'default') + cell(card(state=' is-hover'), 'hover · well edge darkens, title underlines') +
        cell(card(state=' is-focus'), 'focus-visible') + cell(card(state=' is-active'), 'active') +
        cell(card(current=True), 'selected · aria-current') + cell(ERROR, 'error · image failed') + cell(LOCKED, 'locked · not a link') + '</div>' +
        h('Outlined · contained, for dense grids') + '<div class="pm-spec__grid">' +
        cell(card(' pm-card--outlined'), 'default') + cell(card(' pm-card--outlined', state=' is-hover'), 'hover · border-strong') +
        cell(card(' pm-card--outlined pm-card--compact', media=False, badges=False, title='Token system', eyebrow='Next project · 03', summary='A semantic token layer for four teams.'), 'compact · related / next') + '</div>' +
        h('Featured + horizontal (≥768px container)') + '<div class="pm-cq">' + card(' pm-card--featured pm-card--horizontal', key='chart', title='Evaluation dashboards that reviewers trust', eyebrow='2025 · AI tooling · Featured') + '</div>')
STYLE = ('.card-grid{list-style:none;margin:0;padding:0;display:grid;gap:var(--space-10) var(--space-6);grid-template-columns:1fr}'
         '@container (min-width:768px){.card-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}'
         '@container (min-width:1024px){.card-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}'
         '.pm-spec__grid .pm-spec__cell{align-items:stretch}')
PAIRS = [('title', '--color-text-primary', '--color-bg-canvas', 4.5), ('summary', '--color-text-secondary', '--color-bg-canvas', 4.5),
         ('eyebrow (mono)', '--color-text-tertiary', '--color-bg-canvas', 4.5), ('hover well edge', '--color-border-strong', '--color-bg-canvas', 3),
         ('outlined hover', '--color-border-strong', '--color-bg-elevated', 3), ('selected ring', '--color-selected-indicator', '--color-bg-canvas', 3),
         ('focus ring', '--color-focus-ring', '--color-bg-canvas', 3)]
SCRIPT = "document.querySelectorAll('a[href=\"#c\"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();});});pmCheck();"
README = r'''
# Card

The project card. By default it's frameless: an image well with a hairline edge, then type. Hierarchy comes from typography and alignment, not from a filled container, and the work itself is the figure.

## Anatomy
1. **Card**: `<article class="pm-card">`, no fill, `radius-md` (used only for the focus ring's shape).
2. **Image well**: `.pm-media.pm-card__media`, 16:10, `radius-md`, 1px `color-border-subtle` edge. `color-bg-sunken` shows while loading.
3. **Eyebrow**: Geist Mono caption, tertiary, year first ("2024 · AI tooling"). It's metadata, so it's set as metadata.
4. **Title**: `<h3>` + stretched link, `type-h4` at 500, `tracking-h4`, balanced wrapping.
5. **Summary**: `type-body-sm`, `color-text-secondary`, max 48ch.
6. **Tags**: Badges, 1px outline, `space-1` apart.

Rhythm: well → `space-4` → eyebrow → `space-1` → title → `space-2` → summary → `space-4` → tags. Tight inside each group, more space between groups.

Removed in v1.3: the surface fill and the "Read case study →" line (the whole card is the link, so the line added nothing).

## Variants
| Variant | Class | Use |
|---|---|---|
| Frameless | default | Work grids, the main index. |
| Outlined | `pm-card--outlined` | Dense grids and related lists. Elevated paper, 1px `color-border-subtle` ring + `shadow-xs`, image flush to the frame with a hairline under it. |
| Compact | `+ pm-card--compact` | Next and related project, no image: `space-3`/`space-4` padding, `body-md` title. |
| Featured | `pm-card--featured` | One lead project: 16:9, `type-h3` title, `body-md` summary. |
| Horizontal | `pm-card--horizontal` | At ≥768px container: image 7/12, text 5/12. Deliberately asymmetric. |
| Locked | `pm-card--locked` | NDA work: no link, lock fallback, warning badge. |

## Sizes
One size. Width comes from the grid (each card spans 4 columns). Grid gaps are `space-6` horizontal and `space-10` vertical: rows need more air than columns, because the eye reads down a card.

## States
| State | Frameless | Outlined |
|---|---|---|
| Hover | well edge → `color-border-default` + soft `shadow-sm`; title underlines | ring → `color-border-default`, `shadow-xs` → `shadow-sm` |
| Focus-visible | 3px ring around the card (via `:has()`) | same |
| Active | title → `color-text-secondary` | `color-bg-surface` |
| Selected | `aria-current` → 2px cobalt ring on the well | same |
| Disabled | Use Locked: unavailable work is explained, not dimmed | same |
| Error | well fallback + "Image unavailable"; text is unaffected | same |

## Themes
In dark, the well edge is `dark-border-subtle`, hover `dark-border-strong` (3.67:1). The text colours hold hierarchy the same way in both themes: title 15.98:1, summary 10.46:1, eyebrow 7.86:1 on midnight.

## Responsive behavior
The grid goes 1 → 2 → 3 per row, and Horizontal stacks below 768px. Titles wrap with `text-wrap: balance` and never truncate.

## Accessibility
- One link per card (the title), stretched over the card, so there's one tab stop.
- Card images are `alt=""` when the title says it all.
- Heading level follows the outline. Don't nest other interactive controls inside a stretched card.
- Contrast: title ≥15.07:1, summary ≥6.45:1, eyebrow ≥4.67:1 on every light surface.

## Token dependencies
`color-text-primary|secondary|tertiary` `color-border-subtle|default|strong` `color-bg-elevated|surface|sunken` `color-selected-indicator` `color-focus-ring` · `shadow-xs|sm` · `space-1|2|3|4|5|6|8|10` · `radius-md` · `type-h4|h3|body-sm|body-md|caption` · `font-mono` · `weight-medium` · `tracking-h4|h3` · `link-underline-*` · Badge, ImageContainer
'''

# ---- v1.7: tile variant + staggered work grid ----
from lib import IMG
TP = [('queue', 'Review queue for model evaluations', 'Product design · AI tooling', '2024'), ('grid', 'One token source for four teams', 'Design systems · Web', '2023'),
      ('form', 'Permissions console for operators', 'Product design · Internal platform', '2022'), ('chart', 'Evaluation dashboards reviewers trust', 'Product design · Data viz', '2025')]
def tile(k, t, sub, y, state=''):
    return (f'<article class="pm-card pm-card--tile{state}"><div class="pm-card__stage"><img src="{IMG[k]}" alt="" width="1600" height="1000">'
            f'<span class="pm-card__go" aria-hidden="true">{I["arrow"]}</span></div>'
            f'<div class="pm-card__row"><h3 class="pm-card__title"><a href="#c">{t}</a></h3><span class="pm-mono">{y}</span></div><p class="pm-card__sub">{sub}</p></article>')
BODY = (h('Tile · default for selected work (v1.7)') + '<div class="pm-spec__grid">' +
        cell(tile(*TP[0]), 'default') + cell(tile(*TP[1], state=' is-hover'), 'hover · stage deepens, artwork lifts, ↗ appears') +
        cell(tile(*TP[2], state=' is-focus'), 'focus-visible') + cell(tile(*TP[3], state=' is-active'), 'active') + '</div>' +
        h('Staggered work grid · 2 columns from 768px, right column offset space-24') +
        frames('<div style="padding:var(--space-6) var(--space-4)"><ul class="pm-work-grid">' + ''.join(f'<li>{tile(*p)}</li>' for p in TP) + '</ul></div>', 1024, 375) + BODY)
PAIRS = PAIRS + [('tile stage', '--color-bg-surface', '--color-bg-canvas', 0)]
SUB = 'Tile (default for selected work): neutral stage with whole-card hover. Also frameless, outlined, featured, horizontal, compact and locked.'
README = README.replace("## Variants\n| Variant | Class | Use |\n|---|---|---|", """## Variants
| Variant | Class | Use |
|---|---|---|
| **Tile** (v1.7) | `pm-card--tile` | **Default for selected work.** No outline. The artwork sits on a `color-bg-surface` stage (`radius-md`) and rises flush from its bottom edge: the stage is padded `space-12` top and `space-8` sides (`space-8`/`space-5` below 768px), and the full 16:10 screenshot gets top-only `radius-sm` and `shadow-md`, never cropped. Below it are the title (`type-body-lg` at 500) with a mono year on the same baseline, then one "Discipline · Area" line. Hover covers the whole card: the stage goes to `color-bg-sunken`, the artwork lifts `space-2` (no lift with reduced motion), and a ↗ chip appears. Focus shows the card ring and the chip. Lay tiles out in `pm-work-grid`: two columns from 768px, with the right column offset `space-24`. |""",1)
