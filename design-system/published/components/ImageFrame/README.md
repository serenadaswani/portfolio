# ImageFrame

How project artifacts are presented in case studies. The frame is the shared, branded part. The image inside keeps its own palette, which is how every project stays different within one system (consistency with purposeful variation).

## Anatomy
1. **Figure**: `<figure class="pm-frame">`.
2. **Stage**: `.pm-frame__stage`, a `color-bg-sunken` well with `radius-lg` and padding. It gives any screenshot a neutral ground (figure–ground).
3. **Image container**: `.pm-media` inside, `radius-sm` (nested: 12 outer, 4 inner), with a 1px `color-border-default` edge so white screenshots don't melt into light wells.
4. **Chrome** (browser variant): a 28px elevated bar with a centred address placeholder, `aria-hidden`. The traffic-light dots were removed in v1.3 as decoration.
5. **Markers** (annotated): 20px discs with mono numerals, `color-action-primary` with `color-text-on-accent` and a 2px canvas halo.
6. **Caption**: `<figcaption>` with a mono index ("Fig. 03", tertiary, tabular) and text (`type-label`, secondary), baseline-aligned.
7. **Notes** (annotated): an `<ol>` on hairlines with mono `01` counters that match the markers.
8. **Expand** (optional): an on-image icon button on `color-overlay-scrim` that opens the Lightbox.

## Variants
| Variant | Class | Use |
|---|---|---|
| Well | default | Most screenshots and diagrams. |
| Browser | `pm-frame--browser` | Web product screens, where context helps. |
| Device | `pm-frame--device` | Mobile screens. Inverse bezel `space-2`. |
| Annotated | `pm-frame--annotated` + `pm-frame__notes` | Explaining decisions on an artifact. |
| Bleed | `pm-frame--bleed` | Hero artifacts. Full width on narrow screens. |

## Sizes
Stage padding: `pm-frame--sm` `space-4` · md `space-6` · `pm-frame--lg` `space-10`. All drop to `space-4` below a 768px container. Width follows the grid: the prose column (8/12) for most figures, full content width for heroes.

## States
Static by default. With the expand control: the button has hover (1px inset ring), focus-visible (ring, ≥3.88:1 on the scrim) and active states. The frame itself never takes hover effects or shadows, and there's no zoom-on-hover motion.

## Themes
The well is `mist` / `ink`, and the edge is `silver` / `dark-border-default`. Markers stay the accent in both themes (5.17:1 light, ink on dark-accent 7.45:1 dark). Device bezels use `color-bg-inverse`, so they flip with the theme.

## Responsive behavior
Below 768px: padding becomes `space-4`, `--bleed` drops its radius and extends into the page gutter, and captions stay within `reading-max-width`. Annotated markers are positioned in percentages, so they track the image as it scales.

## Accessibility
- `<figure>` + `<figcaption>`: the caption is associated automatically. Give the image real alt text even when there's a caption (alt describes, caption interprets).
- Markers are `aria-hidden`. The numbered `<ol>` is the accessible version of the annotations, so never put information only in the markers.
- The expand button's name includes the figure ("Expand figure 1") and opens a Lightbox dialog.
- Contrast: caption 5.55 / 7.86:1, index 7.66 / 10.46:1, marker 5.17 / 7.45:1.

## Token dependencies
`color-bg-sunken` `color-bg-elevated` `color-bg-inverse` `color-bg-canvas` `color-border-default` `color-text-secondary` `color-text-tertiary` `color-action-primary` `color-text-on-accent` `color-overlay-scrim` · `space-2|3|4|6|10` · `radius-sm` `radius-md` `radius-lg` · `type-caption` `type-body-sm` · `weight-medium` · `reading-max-width` · ImageContainer, Button
