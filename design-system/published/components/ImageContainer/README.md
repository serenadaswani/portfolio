# ImageContainer

`pm-media` is the ratio-locked box every image and video sits in. It reserves space before the image loads (no layout shift), crops consistently, and handles the loading and failure states.

## Anatomy
1. **Box**: `<figure class="pm-media">` (or `<div>` inside a figure), `aspect-ratio: var(--pm-ratio)`, `color-bg-sunken` fill, overflow hidden.
2. **Media**: `<img>` / `<video>` / `<svg>`, absolutely filling the box, `object-fit: cover`.
3. **Fallback** (error): `.pm-media__fallback`, an icon plus "Image unavailable" plus the alt text.
4. **Caption** (optional): a `<figcaption>`, usually supplied by ImageFrame.

## Variants
| Variant | Class |
|---|---|
| Ratios | `--1x1` `--4x3` `--3x4` `--16x10` (default) `--16x9` `--21x9`, or set `--pm-ratio` |
| Fit | cover (default) · `--contain` (letterboxed on sunken with `space-4` inset, for UI screenshots that mustn't be cropped) |
| Shape | `radius-md` (default) · `--square` (full-bleed). Inside an ImageFrame stage it becomes `radius-sm` (nested radius). |

## Sizes
Fluid: the box is 100% of its column and height comes from the ratio. Supply `width`/`height` attributes on `<img>` and a `srcset` + `sizes` that match the grid (for example `sizes="(min-width:1024px) 33vw, (min-width:768px) 50vw, 100vw"` for a card grid).

## States
| State | Treatment |
|---|---|
| Loading | `color-bg-sunken` box (optionally a Skeleton shimmer), `aria-busy="true"` |
| Loaded | image fills the box |
| Error | `.pm-media__fallback`: broken-image icon, "Image unavailable", then the alt text, so the information survives |
| Interactive | not this component. Wrap it in a Thumbnail button or an ImageFrame expand control. |

## Themes
The sunken fill is `mist` / `ink`. Imagery is never re-tinted for dark mode. If a screenshot is very bright in dark mode, present it in an ImageFrame (the well gives it a ground).

## Responsive behavior
`--21x9` falls back to 16:9 below a 768px container (cinematic crops are too short on phones). Swap art direction with `<picture>` when the crop changes meaning.

## Accessibility
- Alt text describes what the image shows that matters to the story ("Review queue: a ranked list of six evaluations, the top one flagged high risk"). Use `alt=""` when the image is decorative or fully described in adjacent text.
- Complex images (diagrams, charts) need a text equivalent nearby or in the caption, not in a long alt.
- Lazy-load below-the-fold images (`loading="lazy"`), but never the first meaningful image.
- In the error state, the fallback exposes the alt via `role="img"` + `aria-label`.

## Token dependencies
`color-bg-sunken` `color-text-secondary` `color-text-tertiary` · `radius-md` · `space-2|4` · `type-caption`
