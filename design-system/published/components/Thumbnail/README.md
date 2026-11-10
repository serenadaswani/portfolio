# Thumbnail

A small image button that selects or opens one image in a set: gallery strips, lightbox navigation, and "more screens" rows in case studies.

## Anatomy
1. **Button**: `<button type="button" class="pm-thumb">`, `radius-sm` (a thumbnail is a control), `color-bg-sunken` behind the image.
2. **Image**: `<img alt="">` cropped with `object-fit: cover`. The button carries the name.
3. **Edge**: an inset 1px `color-border-default` ring (`::after`). It defines light screenshots on light pages.
4. **Selected mark**: a 2px `color-selected-indicator` inset ring, a canvas gap, and a 20px check disc.
5. **List**: `<ul class="pm-thumbs" aria-label="Gallery">`.

## Variants
- **Square** (default) and **wide** `pm-thumb--wide` (4:3).
- **Strip**: `pm-thumbs` wraps. `pm-thumbs--scroll` becomes a single scrolling row below 768px.
- **In lightbox**: the same component on the dark backdrop.

## Sizes
| Size | Edge | Radius |
|---|---|---|
| `pm-thumb--sm` | 56px | `radius-sm` |
| md (default) | 80px | `radius-sm` |
| `pm-thumb--lg` | 112px | `radius-sm` |
Every size is ≥44px (`control-min-target`). Strip gap `space-3`, so a focused thumbnail's ring (6px out) never touches its neighbour.

## States
| State | Treatment |
|---|---|
| Default | 1px `color-border-default` inset |
| Hover | 1px `color-border-strong` inset + soft `shadow-sm` lift |
| Focus-visible | 3px `color-focus-ring` outline at 3px offset (outside, so it's distinct from selection) |
| Active | 2px `color-border-strong` inset |
| Selected | `aria-current="true"` + 2px indicator ring + check disc: two cues besides colour |
| Disabled | `aria-disabled="true"`, greyscale image at 45% opacity, not-allowed cursor |
| Error | sunken tile with a broken-image icon. The name says "failed to load". |

## Themes
Same tokens. The selection ring is `cobalt-500` (light, ≥4.56:1) or `dark-accent` (dark, ≥5.68:1). The check is white on cobalt (5.17:1) or ink on dark accent (7.45:1).

## Responsive behavior
A `pm-thumbs--scroll` strip turns into a horizontal scroller below a 768px container (padding keeps focus rings visible). Inside the Lightbox, thumbnails hide below 768px in favour of previous/next buttons.

## Accessibility
- Name the button, not the image: "Image 2 of 5: Token library". The `<img>` is `alt=""` to avoid double announcement.
- Selection: `aria-current="true"` for "the one being shown". Use `aria-pressed` only for multi-select toggles.
- Tab reaches every thumbnail. In large galleries (more than 12), consider a roving tabindex with arrow keys.
- The focus ring (outside, 3px) and the selection ring (inside, 2px plus gap) never look alike.

## Token dependencies
`color-bg-sunken` `color-bg-canvas` `color-border-default` `color-border-control` `color-border-strong` `color-selected-indicator` `color-action-primary` `color-text-on-accent` `color-text-tertiary` `color-focus-ring` · `control-min-target` · `space-1|2` · `radius-sm` `radius-md`
