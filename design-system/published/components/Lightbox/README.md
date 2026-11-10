# Lightbox

A modal viewer for looking closely at project artifacts. It's always rendered in the dark scope, because imagery reads best on a dark ground, whatever the page theme.

## Anatomy
1. **Dialog**: native `<dialog class="pm-lightbox" data-theme="dark">` opened with `showModal()`, labelled by the caption (`aria-labelledby`).
2. **Backdrop**: `color-overlay-backdrop` (ink at 92%).
3. **Top bar**: counter "2 of 5" (`aria-live="polite"`, metadata voice, `color-text-secondary`) and a Close icon button.
4. **Stage**: Previous button · figure (`pm-media--contain`, never cropped) · Next button.
5. **Footer**: caption (`color-text-on-image`, `reading-max-width`), a mobile previous/next pair, and a thumbnail strip.

## Variants
- **Gallery** (default): counter, previous/next and thumbnails.
- **Single image**: omit the counter, previous/next and thumbnails. Close and caption only.
- **Inline** (`pm-lightbox--inline`): specimen and documentation only. Never use it as a real viewer.

## Sizes
Full viewport. The image is constrained to `content-max-width` (1200px) and contained in the remaining height. Bars use `space-2`/`space-4` padding. Controls are `control-height-md` 44px icon buttons. Thumbnails are sm (56px).

## States
| Element | States |
|---|---|
| Dialog | closed → open (fade over `motion-duration-base`, none with reduced motion) → closed |
| Prev / Next / Close | default · hover (1px inset ring) · focus-visible (3px ring, ≥7.83:1 on the backdrop) · active · disabled (at the ends of a non-looping set: `aria-disabled`) |
| Thumbnails | Thumbnail states. The current image is `aria-current="true"`. |
| Image | loading (sunken) · loaded · error (ImageContainer fallback with alt text) |

## Themes
Always dark-scoped, so light and dark pages show an identical viewer. That's deliberate: in light, the focus ring (`cobalt-600`) would be only about 2.3:1 on the backdrop. In the dark scope the ring is `dark-accent-hover`, at 7.83:1 even over white imagery. Caption text: 14.18:1.

## Responsive behavior
- **≥768px container:** side previous/next buttons and a thumbnail strip.
- **<768px:** the image goes full-bleed, side arrows and thumbnails hide, and "Previous / Next" text buttons appear under the caption (larger, labelled targets). Support swipe as an addition, never as the only way.

## Accessibility
- Native `<dialog>` + `showModal()` handles focus containment, Esc to close and inert background. Focus moves to Close on open and **returns to the trigger** on close.
- Left/Right arrows navigate. Tab cycles through the controls. The counter is a polite live region, so changes are announced.
- Each image keeps real alt text, and the caption labels the dialog.
- Clicking the backdrop closes it, but there's always a visible Close button.
- Don't autoplay slideshows.

## Token dependencies
`color-overlay-backdrop` `color-text-on-image` `color-text-secondary` `color-focus-ring` (dark scope) `color-selected-indicator` · `content-max-width` `reading-max-width` · `control-height-md` · `space-2|3|4` · `radius-md` `radius-lg` · `type-body-sm` `type-caption` · `font-meta` · `motion-duration-base` `motion-ease` · Button (on-image), Thumbnail, ImageContainer
