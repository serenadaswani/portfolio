from lib import I, IMG, cell, h, frames
NAME = 'VideoControls'; GROUP = 'Media'; HEIGHT = 1700; WIDTH = 1100
SUB = 'Custom control bar for prototype videos: play/pause, seek, time, captions, mute, full screen; dark-scoped; compact on mobile.'

def player(state='paused', poster=True):
    playing = state == 'playing'
    big = (f'<button type="button" class="pm-btn pm-btn--primary pm-btn--lg pm-btn--icon pm-video__big-play" data-play aria-label="Play video: review queue walkthrough">{I["play"]}</button>' if poster and not playing else '')
    return (f'<div class="pm-video" data-theme="dark" data-video>'
            f'<div class="pm-media pm-media--16x9"><img src="{IMG["queue"]}" alt="Video poster: review queue walkthrough"></div>{big}'
            '<div class="pm-video__controls" role="group" aria-label="Video controls">'
            f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon" data-toggle aria-label="{"Pause" if playing else "Play"}">{I["pause"] if playing else I["play"]}</button>'
            '<span class="pm-video__time" data-cur>0:42</span>'
            '<input type="range" class="pm-video__scrub" min="0" max="190" value="42" step="1" aria-label="Seek" aria-valuetext="0:42 of 3:10" style="--pct:22%">'
            '<span class="pm-video__time"><span class="pm-video__duration-sep">/ </span><span class="pm-video__duration">3:10</span></span>'
            f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon" aria-pressed="true" aria-label="Captions" data-press>{I["cc"]}</button>'
            f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon pm-video__mute" aria-pressed="false" aria-label="Mute" data-press>{I["vol"]}</button>'
            f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon" aria-label="Full screen">{I["full"]}</button>'
            '</div></div>')

BODY = (h('Responsive · live: play, seek (arrow keys), captions, mute') + frames(player(), 1024, 375) +
        h('Control states (on scrim)') +
        '<div class="pm-spec__row" data-theme="dark" style="background:var(--color-overlay-scrim);padding:var(--space-4);border-radius:var(--radius-md);color:var(--color-text-on-image)">' +
        cell(f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon" aria-label="Play">{I["play"]}</button>', 'default') +
        cell(f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon is-hover" aria-label="Play">{I["play"]}</button>', 'hover') +
        cell(f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon is-focus" aria-label="Play">{I["play"]}</button>', 'focus-visible') +
        cell(f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon is-active" aria-label="Play">{I["play"]}</button>', 'active') +
        cell(f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon" aria-pressed="true" aria-label="Captions">{I["cc"]}</button>', 'selected · aria-pressed') +
        cell(f'<button type="button" class="pm-btn pm-btn--on-image pm-btn--icon" aria-disabled="true" aria-label="Captions (unavailable)">{I["cc"]}</button>', 'disabled') +
        '</div>' +
        h('Playing state') + '<div style="max-width:640px">' + player('playing').replace('data-video', 'data-video data-playing') + '</div>')
STYLE = '.pm-spec__row[data-theme] .pm-spec__cap{color:var(--color-text-secondary)}'
PAIRS_THEME = 'dark'
PAIRS = [('time / icons', '--color-text-on-image', '--color-overlay-scrim', 4.5), ('focus ring', '--color-focus-ring', '--color-overlay-scrim', 3),
         ('big play', '--color-text-on-accent', '--color-action-primary', 3)]
SCRIPT = r'''
function fmt(s){return Math.floor(s/60)+':'+String(s%%60).padStart(2,'0');}
var PLAY=%s, PAUSE=%s;
document.querySelectorAll('[data-video]').forEach(function(V){
  var t=V.querySelector('[data-toggle]'), r=V.querySelector('.pm-video__scrub'), cur=V.querySelector('[data-cur]'), big=V.querySelector('[data-play]'), timer=null;
  function upd(){var v=+r.value;cur.textContent=fmt(v);r.setAttribute('aria-valuetext',fmt(v)+' of 3:10');r.style.setProperty('--pct',(v/190*100)+'%%');}
  function set(p){t.setAttribute('aria-label',p?'Pause':'Play');t.innerHTML=p?PAUSE:PLAY;if(big)big.hidden=p;clearInterval(timer);
    if(p)timer=setInterval(function(){if(+r.value>=190){set(false);return;}r.value=+r.value+1;upd();},1000);}
  t.addEventListener('click',function(){set(t.getAttribute('aria-label')==='Play');});
  if(big)big.addEventListener('click',function(){set(true);t.focus();});
  r.addEventListener('input',upd);
  V.addEventListener('keydown',function(e){if((e.key===' '&&e.target===V)||e.key==='k'){e.preventDefault();t.click();}});
  V.querySelectorAll('[data-press]').forEach(function(b){b.addEventListener('click',function(){b.setAttribute('aria-pressed',b.getAttribute('aria-pressed')!=='true');});});
  upd();
});
pmCheck();
''' % ('`' + I['play'] + '`', '`' + I['pause'] + '`')
README = r'''
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
'''
