# Next session: start here

## Where we left off (Paper × Midnight v1.8)
- **Design system:** 28 components with live previews and guidelines (light and dark), Instrument Sans only (metadata moved off Geist Mono in v1.8), Lucide icons, an Apple HIG pass, and soft dimensional depth. Browse it: https://claude.ai/artifact/4Xae2JhSbDpb6tUHM1wuGL
- **Landing prototype v2 (split layout):** sticky left column (intro, Copy email, Résumé, vertical nav with scroll-spy, socials, LA clock) → right column: showcase work (two full width, two side by side) → about → experience → contact. The v1 bento and floating nav are not on this page any more. https://claude.ai/artifact/XM7Noz2dHb3rfzVEtTnGRb (source: `prototypes/landing.html`, built by `design-system/tools/previews/src/landing.py`)
- **References we agreed on:** itti (nav, hero, work grid), Dakota Sumner (one-page narrative), Leah Kim (case-study layout). Stripe and Vercel inform depth; Apple HIG informs behaviour.
- Everything is on branch `paper-midnight-design-system`. The current site files are untouched.

## How to start
1. Open a Claude Code session on `serenadaswani/portfolio`, on branch `paper-midnight-design-system`. `CLAUDE.md` loads automatically.
2. Paste something like:
   > Read NEXT-SESSION.md and CLAUDE.md. Let's work on the agenda, starting with item 1. Show me side-by-side comparisons before changing components.
3. Bring the new portfolios you found, with a note on what you like in each (information architecture, layout or interactions).

## Agenda
1. **Information architecture.** Confirm the section list and order for the one-page landing, and decide what stays from the current site's nav (Work · Fun · Notes · About). Do Fun and Notes become sections, separate pages, or go?
2. **Real content.** Replace the prototype's placeholders with real content from `site.js` (see "Real content" in `CLAUDE.md`): Deploy, Apple, Procense, OmniSynkAI, Mensio, the LA time zone, socials. Decide the email for Copy email.
3. **Case-study template (Leah Kim structure).** Build it from existing components: back link + eyebrow → title + badges → summary panel (Background / Problem / Approach / Outcome) → StatRow → sticky InPageNavigation + sections with ImageFrame → learnings → more case studies (Card `--tile`). Use Mensio as the first real case study.
4. **Interactions.** Review hover and scroll behaviour against the new references: floating-nav shadow on scroll, tile hover, any page-load moment. Keep the reduced-motion fallbacks.
5. **Ship path.** Decide how the redesign replaces the current site: move `prototypes/landing.html` → `index.html` once approved, port `projects/mensio.html` to the template, then retire `styles.css` and the `landing-a`/`landing-b` experiments.

## Open decisions
- Which project is the second full-width card, and which two go side by side?
- Intro mark: initials now; a photo like Dakota's?
- Bring back the Bento ("What I bring") as a section, or leave it out?
- Floating nav: keep the container, or switch to `pm-topnav--bare` (links only)?
- Real project imagery: screenshots, device mockups, or both on the tile stage?
- Résumé: PDF link, or a résumé page built from ExperienceList?

## Working agreement
- Propose component changes as a side-by-side (Current | Proposed) before editing the system; approved changes go into tokens, CSS and guidelines, then the pages.
- Run the checks in `CLAUDE.md` after every visual change, and fix anything they flag.
- Republish the Claude design system after component changes, so the browsable reference stays in sync with the repo.
