# Component library (v1.7)

27 components, each with a live preview in both themes and a guideline page covering anatomy, variants, sizes, states, themes, responsive behaviour, accessibility and token dependencies.

| Group | Components |
|---|---|
| Actions | Button (primary, secondary, tertiary, ghost, on-image) · Link |
| Navigation | TopNavigation (incl. `--floating`) · SideNavigation · InPageNavigation · Tabs |
| Containers | Card (incl. `--tile` + work grid) · Bento · Panel · Divider |
| Feedback | Badge · StatusIndicator · Skeleton · Tooltip |
| Media | ImageContainer · ImageFrame · Thumbnail · Lightbox · VideoControls |
| Forms | Input (text, textarea, select) · CheckboxRadio |
| Overlays | Popover · Dialog |
| Page sections | Hero · ExperienceList · StatRow |

## Shared conventions
- **CSS only, class-based** (`pm-` prefix, BEM-style `__part` and `--variant`). Use it from `components/bundle.css` together with the tokens. There's no framework dependency. Behaviour (menus, disclosures, lightbox, video) is a few lines of vanilla JS, shown in each preview.
- **Semantic tokens only.** The single literal colour is the video player's `ink` letterbox.
- **States model:** default → hover → focus-visible → active → selected → disabled → error. Selection is always indicator + ARIA state. Disabled is `aria-disabled`. Error is word + shape + colour.
- **Responsive:** container queries at 768px and 1024px, so a component adapts to its column, not the window.
- **Themes:** every component reads the same role tokens. Lightbox and VideoControls are dark-scoped by design.
- **Depth:** flat but dimensional: light ring + `shadow-xs` at rest, `border-default` + `shadow-sm` on hover, `shadow-md` popover, `shadow-lg` dialog.
- **Shape:** sm controls · md containers · lg artifact stages.
- **Type roles:** names Instrument Sans 500 · reading Instrument Sans 400 · metadata Geist Mono 12. No uppercase.
- **Sizes:** xs 24 · sm 32 · md 40 · lg 48px, growing to 44/52px under `pointer: coarse`.
- **Spacing:** atoms in a molecule keep ≥`space-2`. Dense groups use inset focus rings. Each preview is checked for overlapping boxes and focus rings.
- **Previews:** each card's footer recomputes the WCAG ratios for that component's real pairs from the live tokens. Edit a token on this page and the checks update.

## Not built yet
Filter chips, a standalone metadata component (currently `pm-meta` inside Panel), menus and dropdowns, toast, footer and breadcrumbs.
