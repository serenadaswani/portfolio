from lib import I, cell, h, frames, img
NAME = 'ImageFrame'; GROUP = 'Media'; HEIGHT = 2900; WIDTH = 1100
SUB = 'Artifact presentation for case studies: well, browser, device, annotated and bleed frames with captions.'

def fr(cls, inner, cap, idx='Fig. 01', extra=''):
    return (f'<figure class="pm-frame{cls}"><div class="pm-frame__stage">{inner}{extra}</div>'
            f'<figcaption class="pm-frame__caption"><span class="pm-frame__index">{idx}</span><span>{cap}</span></figcaption></figure>')

def media(key, cls=' pm-media--16x10'):
    return f'<div class="pm-media{cls}">{img(key)}</div>'

EXPAND = f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-btn--sm pm-frame__expand" aria-label="Expand figure 1">{I["expand"]}</button>'
ANN = (fr(' pm-frame--annotated', media('queue') +
          '<span class="pm-frame__marker" style="left:38%;top:30%" aria-hidden="true">1</span><span class="pm-frame__marker" style="left:83%;top:24%" aria-hidden="true">2</span>',
          'Annotated: the ranked queue.', 'Fig. 03') +
       '<ol class="pm-frame__notes"><li>Risk rank, with the reason shown inline: reviewers can argue with it.</li><li>The single primary action per row keeps triage to one decision.</li></ol>')

BODY = (h('Variants') + '<div class="pm-spec__grid" style="grid-template-columns:repeat(auto-fill,minmax(420px,1fr))">' +
        cell(fr('', media('queue'), 'Well (default): the ranked queue, after triage rules.'), 'well') +
        cell(fr(' pm-frame--browser', '<div class="pm-frame__chrome" aria-hidden="true"><b></b></div>' + f'<div class="pm-media pm-media--16x10">{img("form")}</div>', 'Browser: role templates replaced a 40-field form.', 'Fig. 02'), 'browser chrome') +
        cell(fr(' pm-frame--device', f'<div class="pm-media pm-media--3x4">{img("mobile")}</div>', 'Device: the mobile review queue.', 'Fig. 04'), 'device') +
        cell(ANN, 'annotated · numbered markers + ordered notes') +
        cell(fr('', media('chart'), 'Interactive: opens in the lightbox.', 'Fig. 05', EXPAND), 'with expand control') +
        '</div>' +
        h('Sizes · stage padding') + '<div class="pm-spec__grid" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">' +
        cell(fr(' pm-frame--sm', media('grid'), 'sm · space-4'), 'sm') + cell(fr('', media('grid'), 'md · space-6'), 'md') + cell(fr(' pm-frame--lg', media('grid'), 'lg · space-10'), 'lg') + '</div>' +
        h('Responsive · bleed goes edge-to-edge below 768px; padding drops to space-4') +
        frames('<div style="padding:var(--space-4)">' + fr(' pm-frame--bleed pm-frame--lg', media('chart', ' pm-media--16x9'), 'Bleed: triage time over ten weeks.', 'Fig. 06') + '</div>', 820, 375))
STYLE = '.pm-spec__grid .pm-spec__cell{align-items:stretch}'
PAIRS = [('caption', '--color-text-tertiary', '--color-bg-canvas', 4.5), ('index', '--color-text-secondary', '--color-bg-canvas', 4.5),
         ('marker', '--color-text-on-accent', '--color-action-primary', 4.5), ('well vs canvas', '--color-bg-sunken', '--color-bg-canvas', 0),
         ('notes', '--color-text-secondary', '--color-bg-canvas', 4.5)]
SCRIPT = 'pmCheck();'
README = r'''
# ImageFrame

How project artifacts are presented in case studies. The frame is the shared, branded part. The image inside keeps its own palette, which is how every project stays different within one system (consistency with purposeful variation).

## Anatomy
1. **Figure**: `<figure class="pm-frame">`.
2. **Stage**: `.pm-frame__stage`, a `color-bg-sunken` well with `radius-lg` and padding. It gives any screenshot a neutral ground (figure–ground).
3. **Image container**: `.pm-media` inside, `radius-sm` (nested: 12 outer, 4 inner), with a 1px `color-border-default` edge so white screenshots don't melt into light wells.
4. **Chrome** (browser variant): a 28px elevated bar with a centred address placeholder, `aria-hidden`. The traffic-light dots were removed in v1.3 as decoration.
5. **Markers** (annotated): 20px discs with numerals, `color-action-primary` with `color-text-on-accent` and a 2px canvas halo.
6. **Caption**: `<figcaption>` with a index ("Fig. 03", tertiary, tabular) and text (`type-label`, secondary), baseline-aligned.
7. **Notes** (annotated): an `<ol>` on hairlines with `01` counters that match the markers.
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
'''
