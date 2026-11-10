from lib import I, cell, h
NAME = 'Tooltip'; GROUP = 'Feedback'; HEIGHT = 820
SUB = 'Inverse, arrowless, label-sized bubble on hover and focus; optional shortcut; Esc dismisses.'

BODY = (h('Variants (shown open)') +
        '<div class="pm-spec__row" style="padding-top:var(--space-12);gap:var(--space-12) var(--space-16)">' +
        cell(f'<span class="pm-tooltip-anchor"><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-labelledby="tt1-{{T}}">{I["copy"]}</button><span role="tooltip" id="tt1-{{T}}" class="pm-tooltip is-open">Copy link<kbd>⌘C</kbd></span></span>', 'label · top (default)') +
        cell(f'<span class="pm-tooltip-anchor"><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-labelledby="tt2-{{T}}">{I["download"]}</button><span role="tooltip" id="tt2-{{T}}" class="pm-tooltip pm-tooltip--end is-open">Download PDF</span></span>', 'label · end') +
        '</div><div class="pm-spec__row" style="padding-bottom:var(--space-24);gap:var(--space-12) var(--space-16);margin-top:var(--space-6)">' +
        cell(f'<span class="pm-tooltip-anchor"><button type="button" class="pm-btn pm-btn--tertiary pm-btn--sm" aria-describedby="tt3-{{T}}">Median triage time {I["info"]}</button><span role="tooltip" id="tt3-{{T}}" class="pm-tooltip pm-tooltip--rich pm-tooltip--bottom is-open"><strong>Median triage time</strong>Time from an evaluation landing to a reviewer opening it, pilot cohort only.</span></span>', 'description · rich · bottom') +
        '</div>' +
        h('Live · hover or Tab to the buttons, Esc to dismiss') + '<div class="pm-spec__row" style="padding-top:var(--space-10)">' +
        f'<span class="pm-tooltip-anchor"><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-labelledby="tl1-{{T}}">{I["copy"]}</button><span role="tooltip" id="tl1-{{T}}" class="pm-tooltip">Copy link</span></span>' +
        f'<span class="pm-tooltip-anchor"><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-labelledby="tl2-{{T}}">{I["full"]}</button><span role="tooltip" id="tl2-{{T}}" class="pm-tooltip">Full screen</span></span>' +
        f'<span class="pm-tooltip-anchor"><button type="button" class="pm-btn pm-btn--ghost pm-btn--icon" aria-labelledby="tl3-{{T}}" aria-disabled="true">{I["edit"]}</button><span role="tooltip" id="tl3-{{T}}" class="pm-tooltip">Edit (unavailable in preview)</span></span>' +
        '</div>')
PAIRS = [('text', '--color-text-inverse', '--color-bg-inverse', 4.5), ('bubble vs canvas', '--color-bg-inverse', '--color-bg-canvas', 3),
         ('bubble vs surface', '--color-bg-inverse', '--color-bg-surface', 3)]
SCRIPT = r'''
document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.pm-tooltip-anchor:hover, .pm-tooltip-anchor:focus-within').forEach(function(a){a.classList.add('is-dismissed');});}});
document.querySelectorAll('.pm-tooltip-anchor').forEach(function(a){a.addEventListener('mouseleave',function(){a.classList.remove('is-dismissed');});a.addEventListener('focusout',function(){a.classList.remove('is-dismissed');});});
document.querySelectorAll('[aria-disabled="true"]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();});});
pmCheck();
'''
README = r'''
# Tooltip

A short text bubble that names an icon-only control or adds a one-line explanation. It appears on hover and keyboard focus. A tooltip never holds anything a person needs to complete a task.

## Anatomy
1. **Anchor**: `.pm-tooltip-anchor` wraps the trigger and the bubble (so the bubble is hoverable).
2. **Trigger**: a focusable control (button or link). Never a plain `span`.
3. **Bubble**: `<span role="tooltip" id>`, `color-bg-inverse` / `color-text-inverse`, `radius-sm`, `type-caption` at 500. There's no arrow: the `space-2` offset and inverse contrast make the link to the trigger clear, and an arrow is decoration.
4. **Shortcut** (optional): `<kbd>` in the metadata voice at 72% opacity ("⌘C").
5. **Hover bridge**: an invisible `::before` covering the gap, so moving the pointer onto the bubble doesn't close it.

## Variants
| Variant | Wiring | Use |
|---|---|---|
| Label | trigger `aria-labelledby="tip-id"` | Names an icon-only button (the tooltip is its accessible name). |
| Description | trigger `aria-describedby="tip-id"` | Supplementary detail for a control that already has a name. |
| Rich | `pm-tooltip--rich` | Title + one sentence, max 280px. No links or buttons inside (that would make it a popover). |
| Placement | default top · `--bottom` · `--end` | Pick the side with room. Flip near viewport edges. |

## Sizes
Label: `type-caption` at 500, padding `space-1` `space-2`, max 240px. Rich: `type-body-sm`, padding `space-2` `space-3`, max 280px. Both are capped at viewport minus `space-8`. Offset from the trigger: `space-2`.

## States
| State | Behaviour |
|---|---|
| Hidden | default |
| Shown | trigger `:hover` or `:focus-within`, fading in over `motion-duration-fast` (no fade with reduced motion) |
| Dismissed | Esc hides it without moving focus (WCAG 1.4.13). It resets on pointer leave or blur. |
| Persistent | Stays while the pointer is over the trigger or the bubble. No timeout. |
| Disabled trigger | Use `aria-disabled` (not `disabled`), so the tooltip can still explain why. |

## Themes
Inverse in both: ink on paper (17.92:1) in light, paper-white on midnight (17.30:1) in dark. The bubble is ≥14.58:1 against any surface, so it needs no border. A soft `shadow-sm` separates it from busy content below.

## Responsive behavior
No hover on touch: tooltips show on focus only. Every icon button keeps its name through `aria-labelledby`, so nothing is lost. Width is capped at the viewport. On narrow containers, prefer `--bottom` or `--end` placement so the bubble isn't clipped by the top bar.

## Accessibility
- WCAG 1.4.13: dismissible (Esc), hoverable (bridge), persistent (no timeout).
- Triggers must be focusable. Tooltips on non-interactive text aren't reachable by keyboard; use visible text instead.
- Only the label or the description, never both with the same text (avoid "Copy link, Copy link").
- No interactive content inside. If you need a link, use a popover or dialog.

## Token dependencies
`color-bg-inverse` `color-text-inverse` · `space-1|2|3|8` · `radius-sm` · `type-caption` `type-body-sm` · `font-meta` · `weight-regular` `weight-medium` · `motion-duration-fast` `motion-ease`
'''
