# VideoControls

A custom control bar for short prototype and walkthrough videos in case studies. It replaces the browser's default chrome so videos match the system, and it's always dark-scoped over the footage.

## Anatomy
1. **Player**: `.pm-video` with `data-theme="dark"`, `radius-md`, containing a 16:9 `pm-media` with the `<video>` (poster first).
2. **Big play** (poster state): a primary lg icon button, centred, named "Play video: <title>".
3. **Control bar**: `role="group" aria-label="Video controls"` on `color-overlay-scrim`.
4. **Play/Pause**: on-image icon button whose `aria-label` swaps (the action, not the state).
5. **Current time**: metadata label.
6. **Seek**: `<input type="range">` with `aria-label="Seek"` and `aria-valuetext="0:42 of 3:10"`. 4px outlined track, solid fill, 12px thumb.
7. **Duration**.
8. **Captions**: toggle, `aria-pressed`.
9. **Mute**: toggle, `aria-pressed`.
10. **Full screen**.

## Variants
- **Poster** (paused, not started): big play visible.
- **Playing**: big play hidden. Controls stay visible while paused, focused or hovered. Auto-hide while playing only after 3s without activity, and never while any control has focus.
- **Minimal** (loops under 15s): play/pause + captions only, and no autoplay.

## Sizes
Control buttons: `control-height-md` icon buttons (40px, 44px on touch). The seek input's hit area is 44px tall even though the visible track is 6px. Bar padding `space-2` `space-3`. Big play: `control-height-lg` 52px.

## States
| Control | States |
|---|---|
| Buttons | default · hover (1px inset ring) · focus-visible (3px ring drawn inset, so adjacent controls never overlap, ≥3.88:1 on the scrim) · active · selected (`aria-pressed="true"`: inset ring + 2px indicator underline) · disabled (`aria-disabled`, for example "Captions (unavailable)") |
| Seek | default · focus-visible (ring) · dragging · disabled (live streams) |
| Player | poster · playing · paused · ended (returns to poster with "Replay") · error (ImageContainer fallback with "Video unavailable" and a transcript link) |

## Themes
Always dark-scoped. The scrim is fixed (ink at 72%), so text and icons are 7.03:1+ even over white footage, and the focus ring is 3.88:1. The page theme doesn't change the player.

## Responsive behavior
Below a 768px container: Mute hides (devices have hardware volume), the duration collapses to the current time only, and gaps tighten. Play, seek, captions and full screen always remain, because captions are an accessibility control and are never dropped.

## Accessibility
- Never autoplay with sound. Respect `prefers-reduced-motion` by not autoplaying at all.
- Captions (WCAG 1.2.2) for every video with speech, and a transcript link next to the player. Captions default to on for silent-first portfolios.
- Keyboard: Tab through the controls. Space or K toggles play when the player has focus. Left/Right on the seek control step 1s (native range). Use Page Up/Down for 10s steps.
- Names describe actions ("Play", "Pause"), and toggles keep constant names with `aria-pressed`.
- The seek control announces time, not a number (`aria-valuetext`).
- If you use native `<video controls>` instead, these styles don't apply, and that's an acceptable fallback.

## Token dependencies
`color-overlay-scrim` `color-text-on-image` `color-text-secondary` `color-focus-ring` `color-selected-indicator` `color-action-primary` `color-text-on-accent` (all dark scope) · `ink` (player letterbox) · `control-height-md|lg` `control-min-target` · `space-1|2|3` · `radius-sm` `radius-lg` · `type-caption` · `font-meta` · Button (on-image, primary), ImageContainer
