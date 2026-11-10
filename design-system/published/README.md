Paper × Midnight is the identity for a product-design portfolio covering enterprise products, AI tooling, internal platforms and design systems. It reads as editorial, analytical and quietly distinctive: warm paper surfaces, mineral neutrals, midnight-ink blues and one controlled cobalt accent. The personality comes from type, composition and art direction, not from decoration.

> **Version 1.8.** One type family: metadata moves from Geist Mono to Instrument Sans (`font-meta`, 13px regular, tertiary, tabular figures), so the site reads calmer and less like code. New Split layout (sticky intro and vertical nav beside the work, with scroll-spy) and Card `--showcase` (one large container per project; strongest work full width, the rest two-up). **v1.7** One-page portfolio patterns: floating centred nav, centred hero, tile cards in a staggered work grid, experience list and stat row. **v1.6** Softer, layered, Midnight-tinted shadows (new `shadow-lg`), Vercel-style light borders with a whisper of depth on containers, and a new Bento component for feature highlights. **v1.5** Lucide icons (shadcn/ui's set), first-line icon alignment checked to 1px, 8px choice spacing, and an Apple HIG pass (hover only on hover-capable devices, Increase Contrast, Reduce Transparency, sheets on compact width, safe areas). **v1.4** Primary typeface is now Instrument Sans, with Geist Mono for metadata, loosened heading tracking and condensed display width. **v1.3** refined every component: shape roles, flat depth, a mono metadata voice. **v1.2** Adds x-small controls, compact pointer sizes with touch overrides, hover-only shadows, a lighter secondary-button border, text-only links, and a no-overlap spacing rule. Built on **v1.1**: The approved audit fixes are applied to `design-tokens.json` and `tokens.css`, and to the tokens here. The component previews are built on them. Contrast is checked in every preview, live, in both themes. This is still not a WCAG certification: test the rendered site with a keyboard and a screen reader.

## Content fundamentals

- Write in the first person ("I mapped…", "we shipped…"). Name the designer's own contribution separately from the team's.
- Lead each case study with role, team, timeline and outcome, then the problem, the decisions and the trade-offs. Recruiters scan; senior designers read the decisions.
- Use sentence case everywhere: headings, buttons, nav, labels. There is **no uppercase or tracked-out label style** in the system. Small supporting text is a label or the metadata voice, both Instrument Sans.
- Be plain and specific. Use numbers only when they are real and sourced. No superlatives, no emoji, no exclamation marks.
- Link text must say where it goes ("Read the evaluation write-up"), never "click here".

## Color

- Build on semantic roles only: `color-bg-*`, `color-text-*`, `color-border-*`, `color-action-*`, `color-focus-ring`, `color-state-*`. Primitives (`paper`, `cobalt-500`, …) feed the roles and never appear in components.
- Surfaces step by lightness: `color-bg-canvas` is the page, `color-bg-surface` groups content (cards, metadata asides), `color-bg-elevated` lifts menus and artifact frames, and `color-bg-sunken` holds wells and placeholders.
- Text: `color-text-primary` for headings and body, `color-text-secondary` for supporting copy and metadata values, `color-text-tertiary` for captions and labels. All three pass 4.5:1 on all four surfaces in both themes.
- Cobalt is the only accent. Spend it on actions, links, the selected indicator and focus, and nowhere else. No gradients, no second hue for decoration.
- Status colors (`color-state-success|warning|error|info`) always come with an icon and a word ("Error:", "Shipped."). `color-state-info` shares the link/focus hue, so the icon is mandatory there.
- `color-border-subtle` and `color-border-default` are decorative (under 3:1). Mark every region with a surface change too. Secondary buttons use the lighter `color-border-button` (silver in light): the label identifies the button. Inputs, thumbnails and toggles keep `color-border-control` (≥3:1).
- Link text is `color-text-link` (cobalt-600 in light), never `color-action-primary`. Cobalt-500 is a fill and the selection indicator; as small text it fails on sunken.
- Selection is always `color-selected-indicator` (bar or ring) plus `aria-current` or `aria-pressed`, never the selected fill alone.
- Tooltips use `color-bg-inverse` / `color-text-inverse`. The lightbox and video player are always dark-scoped (`data-theme="dark"`) over `color-overlay-backdrop` or `color-overlay-scrim`.

## Type

- Primary family **Instrument Sans** (`--font-sans`, variable: weight 400–700, width 75–100%). Display styles run condensed at `font-width-display` (90%) for editorial headlines, and everything else at 100%. **The metadata voice is `--font-meta`** (Instrument Sans, v1.8; it replaced Geist Mono): years, dates, counts, versions, numbering (`01`, `Fig. 03`), time codes and URL prefixes, at `type-label` (13px), weight 400, tertiary, with tabular figures. Size, weight and colour set it apart, not a second family. Load Instrument Sans from Google Fonts; the fallback is system `sans-serif`.
- Hierarchy: `display-xl` once per page (homepage statement), `display-lg` for case-study titles, then `h1`–`h4`. Use exactly one H1 per page, whichever style it wears, and keep heading levels in order.
- Sizes are rem (16px base) and line heights unitless, so browser font-size settings and text-spacing overrides work.
- Reading text is `body-md` at a 680px measure (`reading-max-width`). The case-study lede is `body-lg`. Card summaries are `body-sm`.
- Text roles, so no two kinds of text look interchangeable: **names** (titles, labels, nav, buttons) sans 500 · **reading** (body, summaries, hints) sans 400 in secondary · **metadata** sans 400 at 13px in tertiary, tabular · **captions** sans 13 in secondary. `label` (13px) is for hints, metadata keys and sm buttons, and isn't tracked or uppercased. `micro` is for non-essential metadata only.
- Display, H1–H3 and `body-lg` step up at 768px and 1024px using the `responsiveType` tokens. All other styles stay fixed.
- Weight 500 is not bold for WCAG purposes, so only text 24px and larger counts as "large". Every text color already meets 4.5:1, so this matters only for future colors.

## Spacing, layout and shape

- 4px base: `space-1` … `space-24`. Inside a card use `space-3`/`space-4`; between related blocks `space-6`/`space-8`; between case-study sections `space-12` (mobile) and `space-16` (tablet and up).
- Grid: 4 columns at mobile (≤767px), 8 at tablet (768–1023px), 12 at desktop (≥1024px), with a `space-6` gutter and a `content-max-width` of 1200px. Page gutter: `space-4` mobile, `space-10` tablet and desktop.
- Project cards span 4 columns: one per row on mobile, two on tablet, three on desktop. On desktop, a case study puts its metadata aside in columns 1–3 and its prose in columns 5–12.
- **Shape language:** `radius-sm` (4) for controls and labels (buttons, inputs, tabs, nav items, badges, tooltips, thumbnails) · `radius-md` (8) for containers (panels, popovers, dialogs, card image wells, messages) · `radius-lg` (12) only for artifact stages (ImageFrame, inline lightbox). Nested radius = outer − padding. `radius-pill` isn't used by any component: status is told by fill and glyph, not by roundness.
- **Depth: flat but dimensional** (Vercel's light borders, Stripe's soft layered shadows). Containers rest with a light `color-border-subtle` ring + `shadow-xs`. Interactive surfaces go to `color-border-default` + `shadow-sm` on hover, with no translate or scale. Popover `shadow-md`, Dialog `shadow-lg`. Shadows are Midnight-tinted (not black), use negative spread so they hug the element, and are never the only edge. Tonal steps (Paper → Mineral → Mist; Midnight → Deep blue → Ink) still carry grouping. No gradients, blur or glass. Flat by design: nav, links, badges, inputs, frameless cards.

## States and interaction

- Every interactive component documents the same seven states: default, hover, focus-visible, active, selected, disabled and error (or n/a, with the reason). Specimens force states with `.is-hover`, `.is-active`, `.is-focus` and `.is-selected`; real pseudo-classes work too.
- Links are text only: `color-text-link` at `weight-medium` (body is 400, so weight is the non-colour cue), with an underline on hover. Visited = default. Link focus has **no outline**: a 2px `color-focus-ring` underline on a `color-action-selected-bg` tint.
- Focus on every other control: `focus-ring-width` 3px solid `color-focus-ring` at `focus-ring-offset` 3px. Never set the offset to 0 on filled controls (1.36:1 against the fill), and never clip the ring with `overflow: hidden`.
- **Spacing rule (no overlapping atoms):** inside a molecule, atoms keep at least `space-2` between them. Where items sit closer than 12px (nav lists, toolbars, the video bar), the focus ring draws inset (`outline-offset: -3px`), so it never covers a neighbour. Headers wrap their actions under the title before they can collide, and metadata wraps under labels. Every preview is machine-checked for overlapping boxes and rings.
- Disabled controls use `aria-disabled="true"` (they stay focusable) with `color-disabled-text`, `color-disabled-bg` and `color-disabled-border`. Unavailable content (NDA work) is explained in words, not greyed out.
- Sizes: `control-height-xs` 24 · `sm` 32 · `md` 40 · `lg` 48px for mouse and trackpad. Under `pointer: coarse`, md becomes 44 and lg 52 (Apple HIG touch targets), and `control-min-target` goes from 24 to 44. Use xs and sm for inline, table and toolbar actions only, with `space-2` or more between targets.
- Motion: `motion-duration-fast` 120ms for colour, `motion-duration-base` 200ms for overlays, both on `motion-ease`, and only under `prefers-reduced-motion: no-preference`.
- Responsive components use **container queries** at 768px and 1024px. Put `container-type: inline-size` (`.pm-cq`) on the layout region.

## Imagery and artifacts

- Present project work in an ImageFrame (sunken well, `radius-lg`) around an ImageContainer (`pm-media`, ratio-locked). Give every image meaningful alt text, or `alt=""` with a caption when the figure is described in the prose.
- Text over imagery sits on `color-overlay-scrim` (ink at 72%). That gives 7.6:1 even over a pure-white image.

## Iconography and logo

- No logo was supplied. Set the name in plain Instrument Sans (weight 600, `tracking-heading`).
- **Icons are Lucide**, the set shadcn/ui ships (`lucide-react` in code; this system embeds `lucide-static` 0.460.0 geometry, ISC licence). Use them unmodified: 24px grid, `stroke-width` 2, round caps and joins, `currentColor`, `aria-hidden` (the control carries the name). Sizes: 16px in UI (shadcn `size-4`) · 14px in xs buttons, status indicators and field errors · 12px in badges and thumbnail checks · 20px in empty states. Never mix icon families, change stroke widths, or fill outline icons.
- **Status shapes:** `circle-check` success · `circle-dot` in progress · `circle-dashed` neutral · `info` info · `triangle-alert` warning · `octagon-x` error. Each status has its own shape, so colour is never the only cue.
- **Alignment:** an icon next to text centres on the text's *first* line: margin-top = (line-height × font-size − icon size) / 2, computed from tokens, so it stays aligned when the text wraps. Inline icons are bound to the last word (`pm-nowrap`). Every preview is checked to 1px.

## Apple HIG alignment

The system follows Apple's Human Interface Guidelines where they apply on the web. It takes HIG's behaviour and clarity, not Apple's visual styling: no SF fonts, no translucent materials, no copied components. See the "HIG review" page for each item.
- Touch targets of 44pt via `pointer: coarse`; compact 24–40px controls for pointers, in line with macOS control sizes.
- Hover effects only on devices that can hover (`@media (hover: hover)`), so a tapped control never keeps a stuck hover state. Press states (`:active`) give immediate feedback on touch.
- Supports Increase Contrast (`prefers-contrast: more`), Reduce Transparency (`prefers-reduced-transparency`), Reduce Motion and Dark Mode. Text sizes are rem, so they follow the browser's text-size setting, much like Dynamic Type.
- Concentric corners (nested radius = outer − padding), one prominent action per view, sheets on compact width, safe-area insets on edge-anchored UI.

## Influences

| Source | What this system borrows | Where |
|---|---|---|
| Stripe (marketing) | Editorial hierarchy, confident type contrast, deliberate whitespace between groups | Card rhythm, Panel, type roles |
| Apple (marketing + HIG) | Simplicity, proportion, one clear action; HIG behaviour: touch targets, sheets, accessibility settings, concentric corners | Button proportions, Dialog, control sizes, every component |
| Megan Yap, Dakota Sumner | Split home page: sticky intro and vertical nav beside the work; one large container per project | Split layout, Card `--showcase` |
| xAI | Restraint and high contrast; a single precise accent cue instead of fills | Top navigation rule, Tabs, side-nav tick |
| Vercel | Monochrome surfaces, 1px borders, geometric radii | Shape language, Badge, Input, metadata |
| Linear | Compact rows, flat hover fills, inset focus in dense lists | Side navigation, toolbars |
| Polaris | Component anatomy and states documented the same way for every component | Each component's guidelines |
