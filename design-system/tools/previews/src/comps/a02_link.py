from lib import I, cell, h
NAME = 'Link'; GROUP = 'Actions'; HEIGHT = 900
SUB = 'Text-only links (weight 500, no underline): inline, standalone, subtle, external and on-image, with every state.'

BODY = (
 h('Inline · link text only; weight 500 marks it, underline on hover') +
 '<p class="body-md" style="max-width:var(--reading-max-width);margin:0">The triage rules cut review time. See <a class="pm-link" href="#m">the evaluation write-up</a> for the method, or the <a class="pm-link pm-link--external" href="#m" target="_blank" rel="noopener">pilot <span class="pm-nowrap">data<span class="pm-sr"> (opens in a new tab)</span>' + I['ext'].replace('class="pm-icon"', 'class="pm-icon pm-icon--inline"') + '</span></a>.</p>' +
 h('States') + '<div class="pm-spec__row">' +
   cell('<a class="pm-link" href="#m">Evaluation write-up</a>', 'default') +
   cell('<a class="pm-link is-hover" href="#m">Evaluation write-up</a>', 'hover · underline') +
   cell('<a class="pm-link is-focus" href="#m">Evaluation write-up</a>', 'focus · no outline: tint + 2px line') +
   cell('<a class="pm-link is-active" href="#m">Evaluation write-up</a>', 'active') +
   cell('<a class="pm-link" href="#m">Evaluation write-up</a>', 'visited = default') +
   cell('<a class="pm-link" href="#m" aria-current="page">Work</a>', 'selected · aria-current') +
   cell('<span class="pm-link-unavailable">Under NDA</span>', 'unavailable (not a link)') +
 '</div>' +
 h('Variants') + '<div class="pm-spec__row">' +
   cell(f'<a class="pm-link pm-link--standalone" href="#m">Read case study{I["arrow"]}</a>', 'standalone') +
   cell(f'<a class="pm-link pm-link--standalone is-hover" href="#m">Read case study{I["arrow"]}</a>', 'standalone hover') +
   cell('<a class="pm-link pm-link--subtle" href="#m">Colophon</a>', 'subtle · footer, metadata') +
   cell(f'<a class="pm-link pm-link--standalone" href="#m" target="_blank" rel="noopener">GitHub<span class="pm-sr"> (opens in a new tab)</span>{I["ext"]}</a>', 'external') +
   cell('<span style="display:inline-block;padding:var(--space-3) var(--space-4);background:var(--color-overlay-scrim);border-radius:var(--radius-md)"><a class="pm-link pm-link--on-image" href="#m">View full image</a></span>', 'on image · on scrim') +
 '</div>' +
 h('On every surface') + '<div class="pm-spec__row">' +
   ''.join(cell(f'<span style="display:inline-block;padding:var(--space-3) var(--space-4);background:var(--color-bg-{s});border-radius:var(--radius-md)"><a class="pm-link" href="#m">Read more</a></span>', s) for s in ['canvas', 'surface', 'elevated', 'sunken']) +
 '</div>'
)
PAIRS = [
 ('link/canvas', '--color-text-link', '--color-bg-canvas', 4.5), ('link/surface', '--color-text-link', '--color-bg-surface', 4.5),
 ('link/elevated', '--color-text-link', '--color-bg-elevated', 4.5), ('link/sunken', '--color-text-link', '--color-bg-sunken', 4.5),
 ('hover/sunken', '--color-text-link-hover', '--color-bg-sunken', 4.5), ('subtle', '--color-text-secondary', '--color-bg-canvas', 4.5),
 ('link vs body text (weight 500 carries it)', '--color-text-link', '--color-text-primary', 0),
 ('focus line', '--color-focus-ring', '--color-action-selected-bg', 3),
]
SCRIPT = "document.querySelectorAll('a[href^=\"#\"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();});});pmCheck();"
README = r'''
# Link

Links go somewhere: another page, a section, a file or an external site. A link is just its text, in the link colour at weight 500. If the element does something on the current page, it's a Button.

## Anatomy
1. **Anchor**: `<a href>`.
2. **Text**: says where it goes ("the evaluation write-up", not "here"). `color-text-link`, `weight-medium`.
3. **Underline** (hover and focus only): 1px at 0.2em on hover. On focus it's 2px in `color-focus-ring`.
4. **Focus tint**: a `color-action-selected-bg` wash with a 2px spread, replacing the outline.
5. **Icon** (standalone/external): arrow → or external ↗, `aria-hidden`.
6. **Hidden text** (external): `<span class="pm-sr"> (opens in a new tab)</span>`.

## Variants
| Variant | Class | Use |
|---|---|---|
| Inline | `pm-link` | Inside paragraphs, lists, captions. Text only, weight 500. |
| Standalone | `pm-link--standalone` | Alone on a line ("Read case study →"). Adds the arrow and a `control-min-target` height. |
| Subtle | `pm-link--subtle` | Footers, metadata, colophon. `color-text-secondary` at weight 400 with a quiet 1px `color-border-strong` underline (its non-colour cue), which turns `currentColor` on hover. |
| External | ↗ icon + hidden text | Off-site destinations. |
| On image | `pm-link--on-image` | Only over `color-overlay-scrim`. |

## Sizes
Links inherit the size of their text. Standalone links keep a `control-min-target` height (24px pointer, 44px touch).

## States
| State | Treatment |
|---|---|
| Default | `color-text-link`, weight 500, no underline |
| Hover | `color-text-link-hover` + 1px underline |
| Focus-visible | **No outline.** 2px `color-focus-ring` underline + `color-action-selected-bg` tint |
| Active | `color-action-pressed` |
| Visited | `color-text-link-visited` (= default: one accent, no purple) |
| Selected | `aria-current="page"`: `color-text-primary` + 2px `color-selected-indicator` underline |
| Disabled | Links can't be disabled. Use plain text with `pm-link-unavailable` and a reason ("Under NDA"). |
| Error | n/a |

## Themes
Light: `cobalt-600` (5.65–7.02:1 on every surface), hover `cobalt-700`. Dark: `dark-accent` (5.68–7.45:1), hover `dark-accent-hover`. The focus line on its tint is 6.27:1 (light) and 6.12:1 (dark).

## Responsive behavior
None. Standalone links wrap. Inline icons are bound to the last word with `<span class="pm-nowrap">`, so an icon never wraps onto a line by itself.

## Accessibility
- **The non-colour cue is weight.** Body text is 400 and links are 500, plus an underline on hover and focus. That keeps WCAG 1.4.1 met without an underline at rest: the dark link is only 2.32:1 against body text, so colour alone wouldn't be enough. Don't set links in prose at weight 400, and don't put them inside text that's already 500.
- **Focus without an outline still meets 2.4.7**: the 2px focus-colour line plus the tint is a clearly visible indicator, at ≥6.12:1. Don't remove both.
- Link text must make sense out of context. Never "click here" alone.
- External: say "(opens in a new tab)" in hidden text, and use `rel="noopener"`.
- Keyboard: Tab to focus, Enter to follow.

## Token dependencies
`color-text-link` `color-text-link-hover` `color-text-link-visited` `color-action-pressed` `color-action-selected-bg` `color-focus-ring` `color-text-primary` `color-text-secondary` `color-text-on-image` `color-selected-indicator` `color-disabled-text` `color-overlay-scrim` · `weight-medium` `weight-regular` · `link-underline-thickness` `link-underline-thickness-hover` `link-underline-offset` · `control-min-target` · `space-1`
'''
