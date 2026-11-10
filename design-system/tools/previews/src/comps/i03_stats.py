from lib import cell, h, frames
NAME = 'StatRow'; GROUP = 'Page sections'; HEIGHT = 700; WIDTH = 1100
SUB = 'Two to four big numbers with mono labels for case-study headers and outcomes; the Bento stat style without the tile.'

def stats(items, cls=''):
    return f'<dl class="pm-stats{cls}">' + ''.join(f'<div class="pm-stats__item"><dt class="pm-stats__label">{l}</dt><dd class="pm-stats__value">{v}</dd></div>' for v, l in items) + '</dl>'

A = [('−52%', 'median triage time'), ('14', 'review teams live'), ('3', 'bets shipped, 1 cut')]
B = [('11 → 1', 'tables unified'), ('8', 'Storybook stories'), ('0', 'one-off styles left')]
BODY = (h('Default · display-lg at 90% width') + frames('<div style="padding:var(--space-6) var(--space-4)">' + stats(A) + '</div>', 1024, 375) +
        h('Small · h2 size, for the outcome section') + '<div style="max-width:720px">' + stats(B, ' pm-stats--sm') + '</div>')
PAIRS = [('value', '--color-text-primary', '--color-bg-canvas', 4.5), ('label', '--color-text-tertiary', '--color-bg-canvas', 4.5)]
SCRIPT = 'pmCheck();'
README = r'''
# StatRow

Big numbers with short mono labels. Use it in a case-study header (after the summary) and in the outcome section. It's the Bento stat typography without the tile, so impact reads in a second, as on Leah Kim's case studies.

## Anatomy
1. **Row**: `<dl class="pm-stats">`, an auto-fit grid (min 160px), `space-6` gap, with a `color-border-subtle` hairline and `space-5` above.
2. **Item**: `<div>` containing `<dt>` (label) then `<dd>` (value), visually reversed so the number sits on top while the source order stays label-then-value.
3. **Value**: `type-display-lg` at 500, `font-width-display` (90%), `tracking-display`, tabular figures.
4. **Label**: mono caption, tertiary, lower case, 2–5 words.

## Variants
Default · `pm-stats--sm` (value at `type-h2`, for the outcome section deeper in a case study).

## Sizes
Two to four items. More than four stops being glanceable, so put the rest in prose.

## States
Static.

## Themes
Primary value and tertiary label in both themes (17.92 / 5.55:1 light, 15.98 / 7.86:1 dark).

## Responsive behavior
The auto-fit grid goes 3 or 4 across on desktop, then 2, then 1, keeping a 160px minimum so numbers never squeeze.

## Accessibility
- Description list semantics: screen readers announce "median triage time: −52%". Never show a number without its label.
- Use real values with their units in the text ("−52%", "11 → 1"). Don't encode meaning in colour.

## Token dependencies
`type-display-lg|h2` `line-*` `tracking-display|heading` `font-width-display` · `font-mono` `type-caption` · `color-text-primary|tertiary` `color-border-subtle` · `space-1|5|6`
'''
