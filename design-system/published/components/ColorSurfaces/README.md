# ColorSurfaces

Foundation specimen, not a component: every text, link, focus and border role on all four surfaces, in both themes, with WCAG ratios computed live from the current tokens.

- v1.1 tokens: `color-text-link`, `color-border-control` and `color-selected-indicator` replace the v1.0 failures. Every required row passes in both themes.
- `action-primary` is shown as decorative: it's a fill. Its text use was retired in favour of `color-text-link`. "Decorative" rows aren't required to pass, and must never be the only cue for a region.
- Edit a color token on the page and the ratios update.
