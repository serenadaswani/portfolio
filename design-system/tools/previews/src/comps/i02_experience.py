from lib import cell, h, frames
NAME = 'ExperienceList'; GROUP = 'Page sections'; HEIGHT = 1300; WIDTH = 1100
SUB = 'Roles on hairlines: initials mark, organisation and role, years, one scope line. Plain variant without marks.'

ROLES = [('NW', 'Northwind AI', 'Lead product designer', '2023 – Now', True, 'Evaluation tooling for model reviewers; set up the product design system.'),
         ('LS', 'Lumen Systems', 'Senior product designer', '2020 – 2023', False, 'Internal platform: permissions, audit trails and operator workflows.'),
         ('FS', 'Fieldstone', 'Product designer', '2018 – 2020', False, 'B2B analytics; first design hire, built the component library.'),
         ('SP', 'Studio Parallel', 'Designer', '2016 – 2018', False, 'Brand and web for early-stage startups.')]

def lst(plain=False):
    rows = ''
    for m, org, role, yrs, now, scope in ROLES:
        mark = '' if plain else f'<span class="pm-experience__mark" aria-hidden="true">{m}</span>'
        dot = '<span class="pm-hero__dot" aria-hidden="true"></span>' if now else ''
        rows += (f'<li class="pm-experience__item">{mark}<div class="pm-experience__head"><h3 class="pm-experience__org">{org}</h3><span class="pm-experience__role">{role}</span></div>'
                 f'<span class="pm-experience__years">{dot}{yrs}</span><p class="pm-experience__scope">{scope}</p></li>')
    return f'<ol class="pm-experience{" pm-experience--plain" if plain else ""}" aria-label="Experience">{rows}</ol>'

BODY = (h('Default · with initials marks') + frames('<div style="padding:var(--space-6) var(--space-4)">' + lst() + '</div>', 1024, 375) +
        h('Plain') + '<div style="max-width:720px">' + lst(True) + '</div>')
PAIRS = [('organisation', '--color-text-primary', '--color-bg-canvas', 4.5), ('role / scope', '--color-text-secondary', '--color-bg-canvas', 4.5),
         ('years', '--color-text-tertiary', '--color-bg-canvas', 4.5), ('mark', '--color-text-secondary', '--color-bg-surface', 4.5)]
SCRIPT = 'pmCheck();'
README = r'''
# ExperienceList

A role history in rows, read top to bottom: organisation, role, years, and one line on what you did. It's the Dakota-style experience section in Paper × Midnight's spec-sheet language: hairlines, years, no cards.

## Anatomy
1. **List**: `<ol class="pm-experience">` (newest first), `color-border-subtle` hairline above and between rows.
2. **Mark** (optional): 40px `color-bg-surface` square, `radius-sm`, initials. A real logo can go here later.
3. **Head**: organisation (`<h3>`, `type-body-md` at 500) + role (`type-body-sm`, secondary), sharing a baseline and wrapping.
4. **Years**: metadata label, tertiary, tabular figures, right-aligned. The current role gets a 6px `color-state-success` dot.
5. **Scope**: one line, `type-body-sm`, secondary, max 60ch.

## Variants
Default (with marks) · `pm-experience--plain` (no marks: a denser list for case studies or résumés).

## Sizes
One size. Rows have `space-5` block padding.

## States
Static. If rows link to case studies later, make the organisation a link and add the Card hover pattern. Until then, rows aren't interactive.

## Themes
Hairlines and type carry it in both themes. The mark is surface-on-canvas in light and deep-blue on midnight in dark.

## Responsive behavior
Below 768px, the years move under the role (left-aligned). The scope stays aligned with the text column, not the mark.

## Accessibility
- An ordered list (the order is chronological). Each organisation is a heading, so screen-reader users can jump between roles.
- The mark is `aria-hidden` (the organisation name is right beside it). The "now" dot is decorative; the years read "2023 – Now".
- Contrast: organisation 17.92:1, role 7.66:1, years 5.55:1 on light canvas.

## Token dependencies
`color-border-subtle` `color-bg-surface` `color-text-primary|secondary|tertiary` `color-state-success` · `type-body-md|body-sm|caption` · `font-meta` · `weight-medium` · `radius-sm` · `space-1|2|4|5`
'''
