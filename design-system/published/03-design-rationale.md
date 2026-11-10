# Design rationale

## Gestalt

- **Common region.** A project card is a `color-bg-surface` field, not a bordered box. The surface step (1.10:1 light) is quiet, so every card also groups its content by **proximity**: frame → kicker → title → summary → tags, with spacing of `space-3` inside and `space-6` between cards. Grouping still reads when the region is barely visible, for example in high-contrast mode, on a poor screen, or for low-vision users.
- **Proximity over lines.** Metadata (`dt`/`dd`) sits in a tight `space-1`/`space-4` grid, so keys bind to values without rules. Hairlines (`border-default`) appear only to set off a decision pull-quote, where separation is the meaning.
- **Similarity.** Everything interactive shares one hue: links, primary buttons, the selected indicator, focus. Everything static stays neutral. So cobalt means "you can act here", and is never decoration. That's also why visited links don't get purple, and why info status needs an icon to avoid being taken for a link.
- **Figure–ground.** Paper and midnight are low-chroma grounds. The cobalt figure and the high-contrast ink type carry the eye. Elevation is a lightness step (sunken → canvas → surface → elevated), not a shadow, which keeps the editorial flatness.
- **Continuity.** The 4/8/12 grid and a shared left edge run from the header through the hero, cards and case study, so a scanning eye follows one vertical line. On desktop the metadata aside runs alongside the prose instead of interrupting it.

## Hierarchy and scanning

- **Role → project → contribution → decisions → outcome.** The card answers what and when (kicker), the problem (title) and the result (summary). The case study opens with Role, Team, Timeline and Outcome before any prose, because hiring managers decide in seconds. Decisions get a ruled pull-quote so senior readers can find the trade-offs.
- **Type does the work.** Weight stays at 500 across headings, and hierarchy comes from size and negative tracking. That's quieter than bold, and it's where the "intellectual" character comes from. The label style (13px, tracked, uppercase in CSS) creates a second, smaller voice for metadata without adding a color.
- **Measure.** Prose caps at 680px (about 70 characters at `body-md`), even on a 1280px canvas. The page stays wide; the reading column doesn't.

## Consistency with purposeful variation

The shared parts are the type ramp, color roles, the grid, nav and the metadata block. The variable part is the **artifact frame** (`radius-lg` on `color-bg-sunken`), which can hold any project's imagery, diagrams or UI at any aspect ratio. A project's own palette lives inside the frame and never leaks into the chrome. That unifies the portfolio without forcing identical layouts.

## Usability

- **Recognition over recall:** the nav shows the current section with three cues (fill, indicator bar, `aria-current`) and the same labels on every page.
- **Visible states:** every control has distinct default, hover, pressed, focus and disabled states. Pressed darkens in light and lightens in dark, so it always moves away from the ground.
- **Error prevention and recovery:** status messages lead with a word ("Error:"), not just a hue.
- **Keyboard:** each card has one tab stop (the title link stretches over the whole card), and the focus ring moves to the card so the visible target matches the clickable one.

## Trade-offs

- **Cobalt-600 for text links instead of 500.** This costs a little vibrancy in body copy but passes on every surface. Cobalt-500 keeps its role as the hero fill, where it's most visible.
- **Underlined links.** This costs a little visual cleanliness, but it's the only way dark-theme links meet 1.4.1. The underline is thin and offset to stay editorial.
- **Decorative borders stay sub-3:1.** Raising them would make the system feel boxed-in and corporate. The rule instead: a border never carries meaning alone, and controls get the 3:1 `border-control`.
- **No shadows.** This keeps the paper flatness. The cost is that elevated surfaces rely on lightness steps, so menus and dialogs will need a `border-default` edge when components are built.
