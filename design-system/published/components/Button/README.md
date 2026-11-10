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
