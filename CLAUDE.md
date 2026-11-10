# Serena Daswani · portfolio

Static site (plain HTML, CSS and JS, with no build step and no package manager). Two things live here:

| Path | What it is | Status |
|---|---|---|
| `index.html`, `about.html`, `landing-a.html`, `landing-b.html`, `projects/`, `styles.css`, `site.js` | The **current site** (Inter + Libre Baskerville, orange accent, sidebar layout). `site.js` holds the real content in `SITE`. | Live version. Don't restyle it in place. |
| `design-system/` | **Paper × Midnight v1.9** (v1.9: frosted badge, see `docs/CHANGELOG.md`), the new design system: tokens, component CSS, docs, the published Claude design-system source, and the build and check tools. | Source of truth for the redesign |
| `prototypes/landing.html` | One-page landing built only from the design system, on the Split layout with Card `--showcase`. **The starting point for the redesign.** | v2 (split) |
| `prototypes/mensio.html` | Case-study template, first instance (Mensio). Built by `design-system/tools/previews/src/casestudy.py`; edit that, not the HTML. | Draft |
| `prototypes/review-v1.8.html` | The v1.7 → v1.8 review (metadata font, split layout options). A record; don't rebuild it. | Archive |
| `prototypes/review-badges.html` | The v1.8 → v1.9 badge review (current vs frosted vs glass; frosted chosen). Built by `review_badges.py`. A record. | Archive |
| `prototypes/proposals.html` | Snapshot of the v1.6 → v1.7 side-by-side review. A record; don't rebuild it. | Archive |

Start every session by reading `NEXT-SESSION.md` for the current agenda.

## Source of truth: never edit generated files by hand
- **Tokens:** edit `design-system/tokens/design-tokens.json`, then run `python3 design-system/tools/build_tokens.py`. That regenerates `design-system/css/tokens.css` and `design-system/published/tokens.json`. Never hand-edit those two files.
- **Component CSS:** `design-system/published/components/bundle.css` is the authored source (it adds a responsive re-point block and specimen scaffolding). `design-system/css/components.css` is the portable copy for sites: bundle.css minus section 0, the HIG preference block and section 22. When you change bundle.css, run `python3 design-system/tools/build_components_css.py` to regenerate components.css.
- **Component previews and guidelines:** each component is one Python module in `design-system/tools/previews/src/comps/` (markup, contrast pairs, README). Run `python3 design-system/tools/previews/src/build2.py` to write `published/components/<Name>/{preview.html,README.md}`. Foundation cards: `python3 design-system/tools/previews/build_foundations.py`.
- **Landing prototype:** `python3 design-system/tools/previews/src/landing.py` rebuilds `prototypes/landing.html` from the CSS. Edit content and structure in `landing.py`, not in the HTML.

## Design rules (keep the system cohesive)
- Use **semantic tokens only** (`--color-*`, `--space-*`, `--radius-*`, `--type-*`, `--shadow-*`). No literal colours, no new accent hues. Cobalt is for the primary action, focus and one precise selection cue only.
- **Type roles:** one family, Instrument Sans. 500 = names and actions · 400 = reading text · metadata (years, counts, numbering, time) = `--font-meta` at `type-label` (13px), 400, tertiary, tabular figures (`.pm-meta-text`). No Geist Mono or other second family. No uppercase or tracked labels. Display styles use `--font-width-display` (90%).
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
- From the Framer portfolio (read 2026-11-10): based in **San Francisco**. Experience dates (confirmed by Serena): Deploy Jan 2026 – Present; Apple, UI/UX designer (contract), Aug 2024 – Dec 2025; OmniSynkAI, product design intern, Jul – Sep 2024; Procense (formerly Empiric, Inc), UI/UX designer (contract), Jan 2022 – Aug 2024. Projects: Procense Digital Forms (2023), Apple internal QA reporting tool (2025, confidential), OmniSynkAI AI autofill (2024), Procense website redesign (2022), a freelance grocery delivery app. Framer has no email or résumé link.
- Landing page: white page background in light (page CSS only; the `--color-bg-canvas` token stays paper), sidebar on `--paper` at ≥1024px (surface in dark), "Resume" without accents, no "Read case study" line on showcase cards. Work is "Featured work" with no intro text. Cards: no date/company eyebrow; the title is the project name on one line (Mensio Data Explorer, Procense Digital Forms, Apple QA Reporting, OmniSynkAI Autofill) with the longer description underneath; text column 2fr, asset 3fr, offset right and cropped by the card's right and bottom edges (Apple keeps its centred logo). Showcase cards use a soft project wash (`TINT` in `landing.py`: Mensio #206CFD, Procense #1B2026, Apple #B6BAC6 with a transparent Apple logo SVG (current text colour) instead of a placeholder, OmniSynkAI #755CFB → #9B94E0) rising from the bottom to white, with an 8px-rounded placeholder where the screenshot goes. No border at rest; hover and keyboard focus add a soft shadow (0 3px 12px, grey at 10%). This is a page-level exception to "no gradients / no literal colours": the hex values are project art, not UI chrome.
- Company logos: `assets/logos/{deploy,apple,omnisynkai,procense}.svg`, used in the Experience list (replacing the initials mark and name; the name stays as screen-reader text). Experience is a vertical timeline (`.lp-tl` in `landing.py`, page-level for now): dates (right-aligned) · rail with a dot per role · logo with the role underneath, centred on each row. Rail and unfilled dots use `color-border-default` (soft, decorative); the current role's dot is the selection colour. Each time the section comes into view (it resets once fully off screen), the line grows from the oldest role up through the others and lands on the present role with a small pulse; it is a timed animation, not tied to scroll position; each row appears as the line reaches it. No animation with reduced motion or without JS. On narrow columns the dates wrap as 'Jan 2026 –' / 'Present'.
- Sections follow ericsin.com: a header row with microcopy (`01 · Work`, meta text, sentence case), the heading at h3 size (primary) and a second line in `color-border-strong` from 768px up (h3 is 24px there, WCAG large text, so 3:1 is allowed: 3.77:1 light, 3.67:1 dark) and tertiary below 768px or with `prefers-contrast: more`, on the left, content on the right (≥768px main column); Work's card grid spans full width under it. Draft copy to confirm: the card titles and descriptions, "About me / San Francisco", "4+ years of experience / 2022 – 2026", "Want to work together? / Say hello." Sources: deploy.com header SVG; procense.ai header SVG; OmniSynkAI's own site header (sites.google.com/view/omnisynkai), a 1047px PNG traced to SVG; Apple: the mark + "Apple" lockup Serena supplied, traced to SVG (24px tall so its cap height matches Deploy's). Text parts use `currentColor` so they flip in dark mode. The right Deploy is **deploy.com** (not deploy.co).
- Still placeholders in the landing prototype: the public email (Copy email says "Email TBC") and the Résumé link.
