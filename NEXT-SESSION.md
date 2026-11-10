# Next session: start here

## Where we left off (Paper × Midnight v1.8)
- **Design system:** 28 components with live previews and guidelines (light and dark), Instrument Sans only (metadata moved off Geist Mono in v1.8), Lucide icons, an Apple HIG pass, and soft dimensional depth. Browse it: https://claude.ai/artifact/4Xae2JhSbDpb6tUHM1wuGL
- **Landing prototype v2 (split layout):** sticky left column (intro, Copy email, Résumé, vertical nav with scroll-spy, socials, LA clock) → right column: showcase work (two full width, two side by side) → about → experience → contact. The v1 bento and floating nav are not on this page any more. https://claude.ai/artifact/XM7Noz2dHb3rfzVEtTnGRb (source: `prototypes/landing.html`, built by `design-system/tools/previews/src/landing.py`)
- **References we agreed on:** Megan Yap and Dakota Sumner (split layout, showcase cards, one-page narrative), itti (minimal tone), Leah Kim (case-study layout). Stripe and Vercel inform depth; Apple HIG informs behaviour.
- Everything is on branch `paper-midnight-design-system`. The current site files are untouched.

## How to start
1. Open a Claude Code session on `serenadaswani/portfolio`, on branch `paper-midnight-design-system`. `CLAUDE.md` loads automatically.
2. Paste something like:
   > Read NEXT-SESSION.md and CLAUDE.md. Let's work on the agenda, starting with item 1. Show me side-by-side comparisons before changing components.
3. Attach or commit the material under "Bring with you". Any new reference portfolios are welcome too, with a note on what you like in each.

## Agenda
1. **Real content and images.** Swap the landing placeholders for real material (see "Bring with you" below). Put images in `assets/` at the repo root (photo, project screenshots at 16:10, about 1600×1000) and reference them from `landing.py`; the prototype currently embeds generated placeholder art.
2. **Case-study template (Leah Kim structure), starting with Mensio.** Build it from existing components: back link + eyebrow → title + badges → summary panel (Background / Problem / Approach / Outcome) → StatRow → sticky InPageNavigation + sections with ImageFrame → learnings → more case studies (Card `--showcase`). Port the copy from `projects/mensio.html`.
3. **The rest of the IA.** The current site's nav has Work · Fun · Notes · About. Do Fun and Notes become sections in the right column, separate pages, or go?
4. **Interactions.** Showcase hover, scroll-spy feel, any page-load moment. Keep the reduced-motion fallbacks.
5. **Ship path.** Move the prototype to `index.html` once approved, link `design-system/css/` instead of inlining it, port the case studies, then retire `styles.css` and the `landing-a`/`landing-b` experiments.

## Bring with you
- A photo for the intro (square crop, at least 256×256).
- Your four featured projects in order, strongest first. For each: title, one-line summary, year, client, 1–2 discipline tags, and one 16:10 screenshot.
- About bio (2–3 short paragraphs), years for each role, the public email for Copy email, and a résumé PDF or a decision to build a résumé page.

## Decided (v1.8)
- Metadata in Instrument Sans; Geist Mono dropped.
- Split layout with Card `--showcase`: strongest work full width, two more side by side.
- Scroll-spy marker in the vertical nav stays.
- Intro gets a photo. A placeholder (`.pm-intro__photo--empty`) holds the slot until there's a real image: drop an `<img alt="">` inside `.pm-intro__photo`.
- No Bento section on the home page (the showcase cards already do that job). The component stays in the system.

## Open decisions
- Which project is the second full-width card, and which two go side by side?
- Real project imagery: plain screenshots, or device mockups, on the showcase cards?
- Résumé: PDF link, or a résumé page built from ExperienceList?

## Working agreement
- Propose component changes as a side-by-side (Current | Proposed) before editing the system; approved changes go into tokens, CSS and guidelines, then the pages.
- Run the checks in `CLAUDE.md` after every visual change, and fix anything they flag.
- Republish the Claude design system after component changes, so the browsable reference stays in sync with the repo.
