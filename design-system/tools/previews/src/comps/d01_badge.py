from lib import S, cell, h
NAME = 'Badge'; GROUP = 'Feedback'; HEIGHT = 760
SUB = 'Square-cornered labels: outline tag (default), meta, accent, and four tonal statuses with shape glyphs. No pills.'

def st(k):
    return S[k].replace('class="pm-status__icon"', 'class="pm-icon"')

BODY = (h('Variants') + '<div class="pm-spec__row">' +
        cell('<span class="pm-badge">Research</span>', 'default · frosted tag') +
        cell('<span class="pm-badge pm-badge--meta">v2.1</span>', 'meta · versions, years, counts') +
        cell('<span class="pm-badge pm-badge--accent">Featured</span>', 'accent · one per view') +
        cell(f'<span class="pm-badge pm-badge--success">{st("success")}Shipped</span>', 'success') +
        cell(f'<span class="pm-badge pm-badge--warning">{st("warning")}Under NDA</span>', 'warning') +
        cell(f'<span class="pm-badge pm-badge--error">{st("error")}Discontinued</span>', 'error') +
        cell(f'<span class="pm-badge pm-badge--info">{st("info")}Pilot</span>', 'info') + '</div>' +
        h('Sizes') + '<div class="pm-spec__row" style="align-items:center">' +
        cell('<span class="pm-badge pm-badge--sm pm-badge--meta">2024</span>', 'sm · 20px') + cell('<span class="pm-badge">Interaction</span>', 'md · 24px') + '</div>' +
        h('On every surface') + '<div class="pm-spec__row">' +
        ''.join(cell(f'<span style="display:inline-flex;gap:var(--space-1);padding:var(--space-3);background:var(--color-bg-{s});border-radius:var(--radius-md)"><span class="pm-badge">Research</span><span class="pm-badge pm-badge--meta">2024</span><span class="pm-badge pm-badge--accent">Featured</span></span>', s) for s in ['canvas', 'surface', 'elevated', 'sunken']) +
        '</div>')
PAIRS = [('tag', '--color-text-secondary', '--color-bg-canvas', 4.5), ('tag/sunken', '--color-text-secondary', '--color-bg-sunken', 4.5),
         ('accent', '--color-action-selected-text', '--color-action-selected-bg', 4.5), ('success', '--color-state-success', '--color-state-success-bg', 4.5),
         ('warning', '--color-state-warning', '--color-state-warning-bg', 4.5), ('error', '--color-state-error', '--color-state-error-bg', 4.5),
         ('info', '--color-state-info', '--color-state-info-bg', 4.5)]
SCRIPT = 'pmCheck();'
README = r'''
# Badge

A small static label: a discipline tag, a version or year, "Featured", or a status. Shape and type tell them apart: a frosted tag for disciplines, meta for technical values, a tonal fill for status. All of them are square-cornered.

## Anatomy
1. **Container**: `<span>` or `<li>` (in a `<ul>` of tags), `radius-sm`, 24px tall.
2. **Glyph** (status only): a 12px Lucide icon (`circle-check`, `triangle-alert`, `octagon-x`, `info`), `aria-hidden`, centred on the text.
3. **Text**: `type-caption` (12px) at 500, sentence case, no tracking.

## Variants
| Variant | Class | Treatment | Use |
|---|---|---|---|
| Tag | default (`--outline` is an alias) | Frosted (v1.9): `color-badge-bg` (white at 55%; 6% in dark) + 1px `color-badge-border` (ink at 8%; white at 10% in dark), secondary text. No blur. | Disciplines on cards |
| Meta | `pm-badge--meta` | Metadata voice at 400, tabular | Years, versions, counts |
| Accent | `pm-badge--accent` | `color-action-selected-bg` / `-text` | One per view |
| Status | `--success` `--warning` `--error` `--info` | tonal state fill + glyph + word | Project or content status |

Pills were removed in v1.3. Status is distinguished by fill and glyph, not by a rounder shape. v1.9 replaced the tag's silver outline with the frosted fill so tags sit quietly on project washes; it stays flat (no backdrop blur).

## Sizes
md 24px with `space-2` padding · `pm-badge--sm` 20px with `space-1` padding.

## States
None. Badges aren't interactive. A clickable filter is a chip (not yet in the system).

## Themes
The tag fill is translucent, so it takes on the surface beneath it. Its text is secondary on any surface (≥6.45:1 light, ≥8.64:1 dark); the fill only lightens light surfaces and barely shifts dark ones. With `prefers-contrast: more` the edge becomes `color-border-default`. Status pairs are ≥5.75:1 (light) and ≥6.12:1 (dark).

## Responsive behavior
Rows wrap with a `space-1` gap. Badges never truncate.

## Accessibility
Plain text · status glyphs are decorative and the word carries the meaning · wrap live-changing badges in `role="status"`.

## Token dependencies
`color-badge-bg|border` `color-border-default` (high contrast) `color-text-secondary` `color-action-selected-bg|text` `color-state-*` and `-bg` · `space-1|2` · `radius-sm` · `type-caption` · `font-meta` · `weight-medium|regular`
'''
