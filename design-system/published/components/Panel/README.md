# Panel

A titled region for grouped content: project details, an aside, a form or an error summary. It's separated by a light 1px ring with a whisper of `shadow-xs` (flat but dimensional), or by a tonal step.

## Anatomy
1. **Region**: `<section>` or `<aside>`, `aria-labelledby` its title, `radius-md`.
2. **Header**: title (`type-body-md` at 500; `type-h4` at lg) + optional sm action, pulled to the right edge by `space-2` so its label aligns with the padding. An optional description (secondary) wraps under the title.
3. **Body**: `type-body-sm`, `color-text-secondary`, `space-3` under the header.
4. **Metadata rows** (`pm-meta`): key (`type-label`, tertiary) and value (`type-body-sm`, primary) on `color-border-subtle` hairlines, like a spec sheet. Dates and numbers are Geist Mono.
5. **Footer**: tonal `color-bg-surface` strip under a `color-border-default` hairline, actions right-aligned.

## Variants
| Variant | Class | Use |
|---|---|---|
| Default | — | Elevated paper + 1px `color-border-subtle` ring + `shadow-xs`. Forms, contact, details. |
| Tonal | `pm-panel--tonal` | Mineral fill, no border. Asides beside prose. |
| Sunken | `pm-panel--sunken` | Code, raw data, quotes. |
| Collapsible | `pm-panel--collapsible` | Optional depth (methods, appendices). |
| Error | `pm-panel--error` | `color-state-error` edge, shape icon, sentence starting "Error:". |

`--elevated`, `--outlined` and `--surface` from v1.2 are kept as aliases (default, default, tonal), so nothing breaks.

## Sizes
`pm-panel--sm` `space-4` · md `space-5` · `pm-panel--lg` `space-8` with an h4 title. All drop to `space-4` below a 768px container.

## States
Static panels have no states. Collapsible header: hover (the chevron gets a `color-bg-surface` square), focus-visible (3px ring), expanded/collapsed (`aria-expanded`, chevron rotates). Error is a variant. Selected and disabled: n/a.

## Themes
Default is white + silver hairline in light, and night-raised + `dark-border-default` in dark. Tonal is mineral / deep-blue. Same structure, same hierarchy.

## Responsive behavior
Padding compresses below 768px. The header wraps its action under the title before they can collide. Metadata stays two-column (keys are short).

## Accessibility
- Label regions you want people to jump to. Not every panel needs to be a landmark.
- Collapsible: a button inside the heading, `aria-controls` → body `role="region"`. Collapsed content is `display: none`.
- Error: word + shape + colour. Move focus to the summary after a failed submit.
- Contrast: body 8.01 / 8.64:1 on elevated, keys 5.80 / 6.49:1.

## Token dependencies
`color-bg-elevated|surface|sunken` `color-border-default|subtle` `shadow-xs` `color-text-primary|secondary|tertiary` `color-state-error` `color-focus-ring` · `space-2|3|4|5|6|8` · `radius-sm|md` · `type-body-md|body-sm|label|h4|caption` · `font-mono` · `weight-medium` · `control-height-sm`
