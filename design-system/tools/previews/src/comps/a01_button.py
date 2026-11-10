from lib import I, cell, h, frames
NAME = 'Button'; GROUP = 'Actions'; HEIGHT = 1700; WIDTH = 1100
SUB = 'Primary, secondary, tertiary and ghost; xs/sm/md/lg with one proportion rule; flat states; radius-sm.'

def row(v, label='View project'):
    st = [('', 'default'), (' is-hover', 'hover'), (' is-focus', 'focus-visible'), (' is-active', 'active'), ('" aria-pressed="true', 'selected'), ('" aria-disabled="true', 'disabled')]
    if v == 'primary':
        st = [s for s in st if s[1] != 'selected']
    return '<div class="pm-spec__row">' + ''.join(
        cell(f'<button type="button" class="pm-btn pm-btn--{v}{c}">{label}</button>', cap) for c, cap in st) + '</div>'

BODY = (
 h('Primary · one per view') + row('primary') +
 h('Secondary · neutral, outlined') + row('secondary', 'Download PDF') +
 h('Tertiary · accent text, low emphasis') + row('tertiary', 'View all work') +
 h('Ghost · neutral, toolbars and icon buttons') + row('ghost', 'Share') +
 h('Sizes') + '<div class="pm-spec__row" style="align-items:center">' +
   cell('<button type="button" class="pm-btn pm-btn--primary pm-btn--xs">X-small</button>', 'xs · 24 · px 8 · caption') +
   cell('<button type="button" class="pm-btn pm-btn--primary pm-btn--sm">Small</button>', 'sm · 32 · px 12 · label') +
   cell('<button type="button" class="pm-btn pm-btn--primary">Medium</button>', 'md · 40 · px 16 · body-sm') +
   cell('<button type="button" class="pm-btn pm-btn--primary pm-btn--lg">Large</button>', 'lg · 48 · px 20 · body-md') +
   cell(f'<button type="button" class="pm-btn pm-btn--secondary">{I["download"]}Download PDF</button>', 'leading icon') +
   cell(f'<button type="button" class="pm-btn pm-btn--tertiary">Continue{I["arrow"]}</button>', 'trailing icon') +
   cell(f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-label="Copy link">{I["copy"]}</button>', 'icon-only md · aria-label') +
   cell(f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--sm" aria-label="Edit">{I["edit"]}</button>', 'icon-only sm') +
   cell(f'<button type="button" class="pm-btn pm-btn--ghost pm-btn--icon pm-btn--xs" aria-label="Copy">{I["copy"]}</button>', 'icon-only xs') +
 '</div>' +
 h('X-small in all variants · inline and table actions') + '<div class="pm-spec__row" style="align-items:center;gap:var(--space-2) var(--space-4)">' +
   ''.join(cell(f'<button type="button" class="pm-btn pm-btn--{v} pm-btn--xs{c}">{l}</button>', cap) for v,l,c,cap in [('primary','Publish','','primary'),('secondary',I['copy']+'Copy','','secondary + icon'),('secondary','Copy',' is-hover','secondary hover'),('tertiary','Edit','','tertiary'),('ghost','Share','','ghost'),('secondary','Copy','" aria-disabled="true','disabled')]) +
 '</div>' +
 h('Responsive · block below 768px') +
 frames('<div style="padding:var(--space-4);display:flex;gap:var(--space-2);flex-wrap:wrap"><button type="button" class="pm-btn pm-btn--primary pm-btn--lg pm-btn--block-mobile">Get in touch</button><button type="button" class="pm-btn pm-btn--secondary pm-btn--lg pm-btn--block-mobile">Download résumé</button></div>', 820, 375)
)
PAIRS = [
 ('primary label', '--color-text-on-accent', '--color-action-primary', 4.5),
 ('hover', '--color-text-on-accent', '--color-action-hover', 4.5),
 ('pressed', '--color-text-on-accent', '--color-action-pressed', 4.5),
 ('secondary border (label identifies)', '--color-border-button', '--color-bg-canvas', 0),
 ('tertiary', '--color-text-link', '--color-bg-canvas', 4.5),
 ('tertiary hover', '--color-text-link-hover', '--color-bg-surface', 4.5),
 ('secondary hover border', '--color-border-strong', '--color-bg-canvas', 3),
 ('ghost', '--color-text-secondary', '--color-bg-canvas', 4.5),
 ('selected', '--color-action-selected-text', '--color-action-selected-bg', 4.5),
 ('focus ring', '--color-focus-ring', '--color-bg-canvas', 3),
 ('disabled', '--color-disabled-text', '--color-disabled-bg', 0),
]
SCRIPT = "pmCheck();"
README = r'''
# Button

Buttons act on the current page. If it navigates, it's a Link, even when styled as a button (`<a class="pm-btn">`).

## Anatomy
1. **Container**: `<button type="button">`, `radius-sm` (controls are crisp; containers are `radius-md`), 1px border slot.
2. **Label**: sentence case, verb first, `type-body-sm` at 500.
3. **Icon** (optional): a Lucide icon at 16px (14px at xs), stroke 2, exactly as shadcn/ui sizes it (`size-4`). It's centred on the label by flex alignment. On the icon side, padding loses `space-1`, so the visual margins balance. Only use an icon when it adds meaning (download, external, direction).
4. **Focus ring**: 3px `color-focus-ring` at a 3px offset. Inset inside toolbars.

## Variants
| Variant | Use | Rest | Hover |
|---|---|---|---|
| `pm-btn--primary` | The one main action per view | cobalt fill, `color-text-on-accent` | `color-action-hover` |
| `pm-btn--secondary` | Alternatives | 1px `color-border-button` + `shadow-xs`, no fill | border goes to `color-border-strong` |
| `pm-btn--tertiary` | Low-emphasis action in content | `color-text-link` text | `color-bg-surface` wash |
| `pm-btn--ghost` | Toolbars and icon buttons | `color-text-secondary` | `color-text-primary` on `color-bg-surface` |
| `pm-btn--on-image` | Over `color-overlay-scrim` | `color-text-on-image` | 1px currentColor border |

Cobalt appears on primary only (tertiary uses the link colour as text). Two primaries side by side is a hierarchy bug.

## Sizes
Padding x ≈ 0.4 × height, so every size keeps the same proportions.
| Size | Height | Padding x | Label | Icon |
|---|---|---|---|---|
| `pm-btn--xs` | `control-height-xs` 24 | `space-2` | `type-caption` | 14 |
| `pm-btn--sm` | `control-height-sm` 32 | `space-3` | `type-label` | 16 |
| md (default) | `control-height-md` 40 (44 touch) | `space-4` | `type-body-sm` | 16 |
| `pm-btn--lg` | `control-height-lg` 48 (52 touch) | `space-5` | `type-body-md` | 16 |
| `pm-btn--icon` | square at the size | 0 | — | 16 |

## States
| State | Primary | Secondary | Tertiary | Ghost |
|---|---|---|---|---|
| Hover | `action-hover` | border `border-strong` | surface wash, `link-hover` | surface wash, text primary |
| Focus-visible | 3px ring, 3px offset | same | same | same (inset in toolbars) |
| Active | `action-pressed` | `bg-sunken` + `border-strong` | `bg-sunken`, `action-pressed` text | `bg-sunken` |
| Selected (`aria-pressed`) | n/a | `selected-bg` + `selected-text` + cobalt border | same | same |
| Disabled (`aria-disabled`) | `disabled-bg` / `disabled-text` | same, border removed | `disabled-text` | `disabled-text` |
| Error | n/a. Errors belong to fields and messages. | | | |

Secondary buttons rest with `shadow-xs` (flat but dimensional, Vercel-style) and lose it when pressed. Primary, tertiary and ghost stay flat. Changes are tone, border or text, over `motion-duration-fast`.

## Themes
Dark primary is `dark-accent` with an **ink** label (7.45:1). Pressed lightens in dark (`cobalt-200`) and darkens in light (`cobalt-700`). The dark secondary border is `dark-border-strong` (3.03:1+).

## Responsive behavior
`pm-btn--block-mobile` goes full width below a 768px container. md and lg grow to 44 and 52px under `pointer: coarse`.

## Accessibility
- Real `<button>` or `<a>`. Icon-only buttons need `aria-label` (or a Tooltip via `aria-labelledby`).
- Toggles: `aria-pressed`, with a constant label.
- Prefer `aria-disabled="true"` over `disabled`, so the control stays discoverable.
- Contrast: labels 5.17–11.26:1, focus ring ≥5.65:1. The light secondary border (silver, 1.53:1) is deliberate: WCAG 1.4.11 doesn't require a boundary when the text label identifies the button.
- xs and sm need at least `space-2` between targets (WCAG 2.5.8 spacing exception).

## Token dependencies
`color-action-primary|hover|pressed` `color-text-on-accent` `color-text-primary|secondary` `color-text-link|link-hover` `color-text-on-image` `color-border-button` `color-border-strong` `color-bg-surface|sunken` `color-action-selected-bg|selected-text` `color-selected-indicator` `color-disabled-bg|text` `color-focus-ring` · `shadow-xs` · `control-height-xs|sm|md|lg` · `space-1|2|3|4|5` · `radius-sm` · `type-caption|label|body-sm|body-md` · `weight-medium` · `focus-ring-width|offset` · `motion-duration-fast` `motion-ease`
'''
