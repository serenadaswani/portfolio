# Mensio case study: handoff

Everything from the Mensio case study redesign (Nov 2026), so it can be rebuilt in the Paper x Midnight design system.

- Live page: `projects/mensio.html` (served at `/portfolio/projects/mensio.html`)
- Styles: `projects/mensio.css` (scoped to `body.mensio`, nothing leaks to other pages)
- Interactions: `projects/mensio.js` (vanilla JS, no dependencies)
- Reference snapshots of every component: `docs/mensio/components/` (2x, WebP)
- Build scripts: `tools/mensio/` (see "Rebuilding" below)

## Page structure

| Section (`id`) | Heading | Asset |
|---|---|---|
| header | Redesigning Mensio's Data Explorer for self-serve analysis | Pills (Shipped, Product Design, Redesign), wide blue hero with looping video, TL;DR rows, 3 stats |
| `overview` | Mensio is a powerful tool… / …but customers couldn't get the data out | Before/after slider |
| `assumption` | We assumed customers were our primary users. We were wrong. | Two-column takeaways |
| `problem` | Every custom chart went through an analyst. | Custom request timeline, customer emails, session clip (placeholder), analyst stats, business-impact cards |
| `insight` | The process lived in analysts' heads. | Design goal callout |
| `interviews` | We studied the analyst workflow to rebuild it for customers. | Sticky-note affinity map, quote, Insight callout |
| `roadmap` | We merged stakeholder requests and research findings into one roadmap. | Six-step wizard animation, wishlist → evidence → built table, customer 2×2 map |
| `exploration` | Three flow variations led to our final wizard. | Three Explored/Final wireframes |
| `solution` | Six design decisions shaped Guided Setup. | Bento grid (7 cards), Select screens carousel |
| `engineering` | We designed within the backend's rules. | Design QA board |
| `reflection` | Customers now build their own charts. | Scatterplot + heatmap (illustrative data), two lessons |

## Visual decisions (carry these into the new system)

- Accent: Mensio blue `#206cfd` (darker `#1550d6`, tints `#f1f5ff`, `#e0eaff`, `#c4d7ff`). Blue only on what matters (the "5" in 8 → 5, "85%", current step, links).
- Page background white, no film grain. Ink `#32404f` with 45/55/80% tints for secondary text.
- Type: Geist for the page; Inter only inside rebuilt product UI (matches Figma). Title ~48px, all h2 24px, medium weight, tight tracking. Section labels 15px grey.
- No highlighted text in body copy.
- Bento cards: white, 1px `#e5e7eb` outline, no hover. Screenshots inside: 10px top-left radius, `0 0 0 1px #e4e6f2`, soft purple shadow `0 10px 28px -6px rgba(124,108,255,.22), 0 2px 6px rgba(124,108,255,.08)`, bleed off right/bottom edge.
- Spacing: ~40px between copy and media, 72px between sections.
- Side nav: top-level sections only, fades in at Overview, out above it.

## Components to rebuild (all code-built, see snapshots)

| # | Component | Behaviour | Snapshot |
|---|---|---|---|
| 1 | TL;DR + stats | Rows: Background / Problem / Approach / Outcome. Stats: 8 → 5 steps, 6 presets, 14 wks | `01-tldr-stats` |
| 2 | Before/after slider | Drag divider; Before/After buttons above each half animate to full view, click again returns to split; nudges once on scroll-in; keyboard via range input | `02-before-after-slider` |
| 3 | Custom request timeline | 8 numbered dots across Customer / Analyst / Manager rows, curved path, dashed "1 in 3 come back" loop. Hover/tap/arrow keys fill path to that step and update detail panel (eyebrow "STEP n OF 8 · ROLE", step name, description). Summary row: 8 steps, 3 roles, 3 tools, ~1 day. Below ~500px it becomes a vertical list | `03-custom-request-timeline` |
| 4 | Customer emails | Two anonymized cards, filter pills in Mensio chip colours (purple metric, pink date, orange grouping, green filter) | `04-customer-emails` |
| 5 | Business-impact cards | 3 cards, Lucide icons (trending-down, calendar-x, lock) | `05-business-impact-cards` |
| 6 | Callouts | "Design goal" and "Insight", light grey box, blue label | `06-design-goal-callout` |
| 7 | Affinity map | 4 colour clusters of stacked sticky notes; click a note to bring to front | `07-affinity-map` |
| 8 | Wizard animation | 6-step stepper (Data type → Date range), neutral skeleton per step, auto-advances ~2s, Next → Submit → "Chart ready", loops; pauses off screen | `08-wishlist-wizard-animation` |
| 9 | Wishlist roadmap | 3 rows: stakeholder wish → interview evidence → what we built | `09-wishlist-roadmap` |
| 10 | Customer 2×2 | Frequency vs trust; tooltip placed per dot (Super/Power users: left; others: above). Phones: numbered dots + key | `10-customer-map` |
| 11–13 | Explored/Final wireframes | Hover/tap crossfades two states. Three flows → two doors; full-page wizard (numbered top stepper) → modal (numbered vertical stepper); six steps with Schedule → five ending on Review + Schedule Report in chart bar | `11`–`13` |
| 14 | Bento grid | 01 segmented stepper (auto-fills, Review & Fetch); 02 Presets (hero, 3 cols × 2 rows); 03 Smart defaults + 04 Duplicate (2 cols, stacked); 05 Guardrails (full strip); 06 Chart types (3 cols) + 07 Seasons (2 cols). Each image is a cropped region that fills its frame | `14-solution-bento` |
| 15 | Select screens carousel | 5 UX moments, numbered segments 01–05 with progress bars synced to a 4.8s timer, zooms into each screen, pause on hover, click to jump | `15-select-screens-carousel` |
| 16 | Design QA board | To fix / In review / Done, P0–P4 tags with legend. Items are illustrative | `16-design-qa-board` |
| 17 | Impact charts | Scatterplot (legend filters) and heatmap with hover tooltips. Illustrative data | `17-impact-charts` |

Bento crop regions (source px, `x0,y0 → x1,y1`) are in `tools/mensio/build_page.py`, function `region(...)`.

## Asset files

`assets/mensio/`
- `01-hero.mp4` + poster: Guided Setup run-through (~14s, cross-fades, click rings)
- `02-session.mp4` + poster: **draft** frustrated-session edit (~20s, 6 captioned zooms, username masked). Not on the page yet; work was paused
- `screens/`: Figma screen exports (1440×1024, 1x only because of the Figma Starter MCP limit). Used by the slider and carousel
- `bento/screen-*.webp`: your full component exports used in the bento
- `bento/presets|defaults|seasons|charts|guardrails.webp`: your tighter snippet exports (only `guardrails` is used now)

## Sources

- Figma: `Mensio-Data-Explorer-Revamp` (file key `EzPty7WLJWIRoeTM3qMZ2d`). Page "Revamped Data Explorer Screens" `2:47969`; the shadcn section `2:77916` is the final UI. Old explorer is on the Handoff page, section `2:7504`. Higher-res (2x) exports would sharpen the slider and carousel.
- Google Drive, shared "Mensio" folder: Case Study Story (analyst Q&A), Case Study Narrative, Product Spec / Rules, Tech Specs, Data Explorer Selection Menu.

## Open items

1. Session clip: finish or drop `02-session.mp4` (draft exists; placeholder still on page).
2. Design QA board: replace illustrative items with real ones from the QA doc.
3. Wishlist table: "in the same order" in the first evidence cell isn't in the interview notes. Confirm or remove.
4. Analyst numbers: Amanda (~3 requests/day) vs Will (3–4/week) still unreconciled.
5. Re-export Figma screens at 2x.
6. Confidentiality: client names are removed from the page; confirm Deploy is fine with screens and figures being shown.
7. landing-b quick-view summaries come from the resume; confirm OK to show (Apple NDA).

## Rebuilding this page

`tools/mensio/build_page.py` generates `projects/mensio.html`:

```bash
python3 tools/mensio/build_page.py projects/mensio.html
```

Edit copy and markup there, not in the HTML. The video scripts (`make_hero_video.py`, `edit_session_video.py`) were run from a scratch folder with raw Figma PNGs and the raw session recording, which are not in the repo; they're kept as a reference for timings, crops and captions.
