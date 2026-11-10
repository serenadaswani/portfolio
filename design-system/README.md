# Paper × Midnight design system (v1.8)

Editorial, analytical and quietly distinctive: Paper and Midnight surfaces, one cobalt accent, Instrument Sans throughout (metadata included), Lucide icons, and flat-but-dimensional depth. WCAG 2.2 AA in both themes, with Apple HIG behaviour.

Browse it (live previews and guidelines for every component): https://claude.ai/artifact/4Xae2JhSbDpb6tUHM1wuGL

## Folder map
```
design-system/
  tokens/design-tokens.json      SOURCE: every token (DTCG-style, light + dark, responsive, shadows, controls)
  css/tokens.css                 GENERATED from the JSON. Link this first on any page.
  css/components.css             Portable component styles. Link after tokens.css.
  docs/                          CHANGELOG, HIG-REVIEW, REFINEMENT-AUDIT
  published/                     Exact mirror of the Claude design-system artifact (README, audit, rationale,
                                 tokens.json, components/<Name>/{preview.html, README.md}, components/bundle.css)
  tools/
    build_tokens.py              JSON → css/tokens.css + published/tokens.json
    build_components_css.py      published/components/bundle.css → portable css/components.css
    usage.json                   Usage notes attached to tokens in the published system
    previews/
      src/comps/*.py             One module per component: preview markup, contrast pairs, guideline README
      src/build2.py              Builds every component preview + README into published/components/
      build_foundations.py       Builds the Colour/Surfaces and 375 / 768 / 1280 layout cards
      src/landing.py             Builds prototypes/landing.html from css/
      src/review.py, review2.py  Built the v1.6 and v1.8 review pages (records only; don't rebuild)
      src/lib.py, lucide.json    Lucide icons (lucide-static 0.460.0, ISC), placeholder imagery, helpers
      checks/*.js                Playwright checks: contrast + errors (shot3), overlaps, first-line alignment
```

## Use it on a page
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&display=swap">
<link rel="stylesheet" href="/design-system/css/tokens.css">
<link rel="stylesheet" href="/design-system/css/components.css">
<div class="pm-cq"> … pm-* components … </div>
```
Class names and markup for each component are in `published/components/<Name>/README.md` and its `preview.html`.

## Common tasks
- **Change a token:** edit `tokens/design-tokens.json`, then run `python3 design-system/tools/build_tokens.py`.
- **Change component styles:** edit `published/components/bundle.css`, then run `python3 design-system/tools/build_components_css.py` to refresh the portable `css/components.css`.
- **Change a component's preview or guideline:** edit `tools/previews/src/comps/<module>.py`, then run `python3 design-system/tools/previews/src/build2.py`.
- **Add a component:** add a module to `tools/previews/src/comps/` (copy an existing one: NAME, GROUP, HEIGHT, SUB, BODY, PAIRS, SCRIPT, README with the 8 sections) and its CSS to bundle.css. Then rebuild and run the checks.
- **Rebuild the landing prototype:** run `python3 design-system/tools/previews/src/landing.py`.
- **Run the checks:** see `CLAUDE.md` at the repo root.

## Version history
See `docs/CHANGELOG.md` (v1.1 audit fixes → v1.8 split layout and one type family).
