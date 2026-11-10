# Serena Daswani · portfolio

Static site (plain HTML, CSS and JS, with no build step and no package manager). Two things live here:

| Path | What it is | Status |
|---|---|---|
| `index.html`, `about.html`, `landing-a.html`, `landing-b.html`, `projects/`, `styles.css`, `site.js` | The **current site** (Inter + Libre Baskerville, orange accent, sidebar layout). `site.js` holds the real content in `SITE`. | Live version. Don't restyle it in place. |
| `design-system/` | **Paper × Midnight v1.7**, the new design system: tokens, component CSS, docs, the published Claude design-system source, and the build and check tools. | Source of truth for the redesign |
| `prototypes/landing.html` | One-page landing built only from the design system. **The starting point for the redesign.** | v1 |
| `prototypes/proposals.html` | Snapshot of the v1.6 → v1.7 side-by-side review. A record; don't rebuild it. | Archive |

Start every session by reading `NEXT-SESSION.md` for the current agenda.

## Source of truth: never edit generated files by hand
- **Tokens:** edit `design-system/tokens/design-tokens.json`, then run `python3 design-system/tools/build_tokens.py`. That regenerates `design-system/css/tokens.css` and `design-system/published/tokens.json`. Never hand-edit those two files.
- **Component CSS:** `design-system/published/components/bundle.css` is the authored source (it adds a responsive re-point block and specimen scaffolding). `design-system/css/components.css` is the portable copy for sites: bundle.css minus section 0, the HIG preference block and section 22. When you change bundle.css, run `python3 design-system/tools/build_components_css.py` to regenerate components.css.
- **Component previews and guidelines:** each component is one Python module in `design-system/tools/previews/src/comps/` (markup, contrast pairs, README). Run `python3 design-system/tools/previews/src/build2.py` to write `published/components/<Name>/{preview.html,README.md}`. Foundation cards: `python3 design-system/tools/previews/build_foundations.py`.
- **Landing prototype:** `python3 design-system/tools/previews/src/landing.py` rebuilds `prototypes/landing.html` from the CSS. Edit content and structure in `landing.py`, not in the HTML.

## Design rules (keep the system cohesive)
- Use **semantic tokens only** (`--color-*`, `--space-*`, `--radius-*`, `--type-*`, `--shadow-*`). No literal colours, no new accent hues. Cobalt is for the primary action, focus and one precise selection cue only.
- **Type roles:** Instrument Sans 500 = names and actions · 400 = reading text · Geist Mono 12px = metadata (years, counts, numbering, time). No uppercase or tracked labels. Display styles use `--font-width-display` (90%).
- **Shape:** `radius-sm` (4) for controls and labels · `radius-md` (8) for containers, including the floating nav · `radius-lg` (12) for artifact stages only. No pills. Nested radius = outer − padding.
- **Depth, flat but dimensional:** containers rest on a `--color-border-subtle` ring + `--shadow-xs`; interactive surfaces go to `--color-border-default` + `--shadow-sm` on hover. Popover `--shadow-md`, dialog `--shadow-lg`. No gradients, blur or glass.
- **Icons:** Lucide only (the set shadcn/ui uses; geometry in `design-system/tools/previews/src/lucide.json`), stroke 2. Sizes 16 / 14 / 12 / 20. Centre text-adjacent icons on the first line: margin-top = (line-height × font-size − icon) / 2.
- **Spacing:** 4/8 grid. Atoms inside a molecule keep at least `space-2` apart. Where items sit closer than 12px, focus rings draw inset.
- **Apple HIG behaviour:** hover styles only inside `@media (hover: hover)`; 44px targets under `pointer: coarse`; respect `prefers-reduced-motion`, `prefers-contrast: more` and `prefers-reduced-transparency`; dialogs become bottom sheets below 768px; use safe-area insets on edge-anchored UI.
- **Accessibility floor:** WCAG 2.2 AA. Text 4.5:1, UI boundaries and focus 3:1, in **both** themes. Never remove focus indicators.
- **Responsive:** components use container queries at 768px and 1024px. Put `.pm-cq` (container-type: inline-size) on the layout region.

## Checks to run after any visual change
Playwright and Chromium are preinstalled in Claude Code cloud sessions.
```bash
python3 design-system/tools/previews/src/localcss.py design-system/published/tokens.json > design-system/tools/previews/.local/tokens.compiled.css
python3 design-system/tools/previews/src/mklocal.py
node design-system/tools/previews/checks/shot3.js Button Card Hero        # contrast failures, script errors, overflow, screenshots
node design-system/tools/previews/checks/overlap.js Button Card Hero      # overlapping atoms and focus rings
node design-system/tools/previews/checks/align.js CheckboxRadio Badge     # icon and control centred within 1px of the text's first line
```
Pass component names (the folder names in `published/components/`). Append `:375` for a phone-width viewport. `.local/` is git-ignored.

## Publishing the Claude design system
The browsable system is a Claude Design System artifact: https://claude.ai/artifact/4Xae2JhSbDpb6tUHM1wuGL (private to Serena). `design-system/published/` mirrors its `project/` folder exactly. To publish, use the Artifact tool with that `url`, `root` = a folder holding `project/…` (copy `published/` to `<tmp>/project/`), `file_path` = `project/design-system.json`, and `files` = every other changed `project/...` path. Read `project/design-system.json` from the artifact right before publishing and update only its `lastChange`.

Landing prototype artifact: https://claude.ai/artifact/XM7Noz2dHb3rfzVEtTnGRb

## Real content (from `site.js`). Use this, not the prototype's samples
- Name: Serena Daswani. Time zone: America/Los_Angeles.
- Currently designing at Deploy. Previously designed at Apple and Procense; interned at OmniSynkAI.
- Project: **Mensio**, “Redesigning Mensio's Data Explorer for self-serve analysis” (shipped 2026, `projects/mensio.html`).
- Socials: LinkedIn https://www.linkedin.com/in/serena-daswani · GitHub https://github.com/serenadaswani · Framer https://serenadaswani.framer.website/ · Résumé (no link yet).
- The prototype's Northwind AI / Lumen Systems / Fieldstone / Studio Parallel roles, the "New York" clock, "10 yrs", `hello@serenadaswani.com`, the −52% stat and the four sample projects are **placeholders** to replace.
