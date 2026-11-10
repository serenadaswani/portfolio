from lib import I, cell, h, frames, img
NAME = 'Bento'; GROUP = 'Containers'; HEIGHT = 2600; WIDTH = 1100
SUB = 'Feature-highlight grid: featured, stat, Midnight, tonal and link tiles; copy on top, visual on the bottom edge; 6 / 2 / 1 columns.'

def tile(cls='', eyebrow='', title='', text='', body_extra='', visual='', link=False, theme=''):
    t = f'<a href="#b">{title}</a>' if link else title
    th = f' data-theme="{theme}"' if theme else ''
    return (f'<article class="pm-bento__tile{cls}"{th}><div class="pm-bento__body">'
            + (f'<p class="pm-bento__eyebrow">{eyebrow}</p>' if eyebrow else '')
            + (f'<h3 class="pm-bento__title">{t}</h3>' if title else '')
            + (f'<p class="pm-bento__text">{text}</p>' if text else '') + body_extra + '</div>' + visual + '</article>')

def vis(key, bleed=False, ratio='16x10'):
    return f'<div class="pm-bento__visual{" pm-bento__visual--bleed" if bleed else ""}"><div class="pm-media pm-media--{ratio}">{img(key, alt="")}</div></div>'

CHECK = I['check']
LIST = ('<ul class="pm-bento__list">' + ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in
        ['WCAG 2.2 AA contrast, checked live', 'Keyboard paths for every flow', 'Respects reduced motion and contrast settings']) + '</ul>')

GRID = ('<div class="pm-bento">' +
        tile(' pm-bento__tile--featured pm-bento__tile--wide pm-bento__tile--tall', '01 · Systems', 'Design systems that scale across teams',
             'A semantic token layer and a component library four product teams theme without forking.', visual=vis('queue')) +
        tile('', '02 · Outcome', '', '', '<p class="pm-bento__stat">−52%</p><p class="pm-bento__stat-label">median triage time, pilot cohort</p>') +
        tile(' pm-bento__tile--midnight', '03 · AI tooling', 'Interfaces for model evaluation', 'Ranked, explainable queues reviewers can argue with.', visual=vis('grid', bleed=True), theme='dark') +
        tile(' pm-bento__tile--half', '04 · Research', 'From interviews to roadmap', 'Twelve contextual interviews turned into three bets and one cut.', visual=vis('chart')) +
        tile(' pm-bento__tile--half pm-bento__tile--tonal', '05 · Accessibility', 'Inclusive by default', '', LIST) +
        tile(' pm-bento__tile--full', '06 · Writing', 'Essays on systems and craft', 'Notes on tokens, editorial UI and designing for review work.', link=True) +
        '</div>')

STATES = ('<div class="pm-bento" style="grid-template-columns:repeat(auto-fill,minmax(220px,1fr))">' +
          cell(tile('', '06 · Writing', 'Essays on systems', 'Default', link=True), 'link tile · default') +
          cell(tile(' is-hover', '06 · Writing', 'Essays on systems', 'Hover: ring + shadow-sm', link=True), 'hover') +
          cell(tile(' is-focus', '06 · Writing', 'Essays on systems', 'Focus-visible ring', link=True), 'focus-visible') +
          cell(tile(' is-active', '06 · Writing', 'Essays on systems', 'Pressed: surface tone', link=True), 'active') + '</div>')

BODY = (h('Composition · 6 / 2 / 1 columns by container width') + frames('<div style="padding:var(--space-5)">' + GRID + '</div>', 1024, 375) +
        h('Interactive tile states') + STATES)
STYLE = '.pm-spec__cell > .pm-bento__tile{width:100%;min-height:180px}'
PAIRS = [('title', '--color-text-primary', '--color-bg-elevated', 4.5), ('text', '--color-text-secondary', '--color-bg-elevated', 4.5),
         ('eyebrow', '--color-text-tertiary', '--color-bg-elevated', 4.5), ('text/tonal', '--color-text-secondary', '--color-bg-surface', 4.5),
         ('ring', '--color-border-subtle', '--color-bg-canvas', 0)]
SCRIPT = "document.querySelectorAll('a[href=\"#b\"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();});});pmCheck();"
README = r'''
# Bento

A grid of feature-highlight tiles for showing what you do at a glance: capabilities, outcomes, principles. It takes the good parts of Stripe's bento: copy on top, the visual anchored to the bottom edge, one large number when a metric is the story, and soft layered depth. It keeps Paper × Midnight's language: mono eyebrows, hairline rings, a single accent, `radius-md` containers.

## Anatomy
1. **Grid**: `.pm-bento`, dense auto-flow, `space-4` gap (`space-5` at ≥1024px).
2. **Tile**: `<article class="pm-bento__tile">`, `color-bg-elevated`, `radius-md`, 1px `color-border-subtle` ring + `shadow-xs`. Flat but dimensional.
3. **Body**: `space-5` padding (`space-8` on featured), `space-2` rhythm.
4. **Eyebrow**: mono caption, numbered and named ("01 · Systems").
5. **Title**: `type-h4` (h3 on featured), balanced wrapping. Optionally a stretched link, which makes the tile interactive.
6. **Text**: `type-body-sm` (body-md on featured), secondary, max 42ch.
7. **Stat** (optional): `type-display-lg` at 90% width, tabular figures, + mono label. Use one per grid at most.
8. **Visual** (optional): `pm-media` set into the bottom edge, inset by the body padding, top corners only (`radius-sm`, nested in `radius-md`), with its own `shadow-sm`. `--bleed` runs edge to edge.
9. **List** (optional): Lucide `check` + text, icons centred on the first line.

## Variants
| Variant | Class | Use |
|---|---|---|
| Default | — | Most tiles |
| Featured | `--featured` | One per grid: larger type and padding, `shadow-md` |
| Midnight | `--midnight` + `data-theme="dark"` | A brand moment: dark-scoped Ink surface (`color-bg-sunken` in dark) with a `color-border-default` ring, so it holds its edge on Paper and Midnight pages alike. Max one per grid. |
| Tonal | `--tonal` | Quiet supporting tiles (Mineral, no ring or shadow) |
| Link tile | title contains `<a>` | Whole tile navigates |

## Sizes
Spans on the 6-column desktop grid: default 2 (a third) · `--half` 3 · `--wide` 4 · `--full` 6 · `--tall` adds a second row. Minimum height 240px on tablet and up, so short tiles still read as tiles. At 2 columns, `--wide` and `--full` span both, and everything else takes one.

## States
Static tiles have none. Link tiles:
| State | Treatment |
|---|---|
| Hover | ring → `color-border-default`, shadow → `shadow-sm`, title underlines. No translate, no scale. |
| Focus-visible | 3px ring around the tile |
| Active | `color-bg-surface` |
| Disabled / selected / error | n/a |

## Themes
Light: paper-white tiles with a mist ring and a Midnight-tinted soft shadow. Dark: night-raised tiles with deeper black shadows. The Midnight tile always renders dark-scoped on Ink. On a dark page it sits one step deeper than Midnight and is defined by its `border-default` ring.

## Responsive behavior
6 → 2 → 1 columns by container. Below 768px, featured padding drops to `space-5`, minimum heights are removed, and tiles stack in source order. Put the most important tile first.

## Accessibility
- Each tile is an `<article>` with a heading. Visuals are decorative (`alt=""`) unless they carry information the text doesn't.
- Stats need their label: "−52%" alone is meaningless to a screen reader. Keep the label adjacent.
- Link tiles have one link (the title), stretched over the tile.
- Contrast: title ≥15.07:1, text ≥7.07:1 (tonal), eyebrow ≥5.12:1 on the light surfaces.

## Token dependencies
`color-bg-elevated|surface|sunken` `color-border-subtle|default` `color-text-primary|secondary|tertiary` `color-focus-ring` · `shadow-xs|sm|md` · `space-2|3|4|5|8` · `radius-sm|md` · `type-h4|h3|body-sm|body-md|display-lg|caption` · `font-mono` · `font-width-display` · `tracking-h4|h3|display` · `weight-medium` · ImageContainer
'''
