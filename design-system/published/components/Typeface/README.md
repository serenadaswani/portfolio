# Typeface

Instrument Sans is the only typeface. It became the primary face in v1.4, and from v1.8 it also sets metadata, replacing Geist Mono, which read as code. This card keeps the before and after on record, plus the full ramp with metrics read live from the rendered text.

## Anatomy
- **Primary**: Instrument Sans, variable: weights 400–700, width 75–100%, with italics. Loaded from Google Fonts. The fallback is system `sans-serif`.
- **Metadata voice** (`font-meta`): Instrument Sans 400 at `type-label` (13px), tertiary, with tabular figures. It sets years, dates, counts, versions, numbering, time codes and URL prefixes. Size, weight and colour set it apart from reading text; there is no second family.

## Why Instrument Sans
- **Distinctiveness.** Geist is strongly associated with Vercel, so a system set in it reads as a Vercel derivative. Instrument Sans is a slightly narrow grotesque with more editorial warmth, and it's recognisable without being decorative.
- **Editorial headlines.** The width axis allows condensed display type (`font-width-display` 90%), which is the Stripe-like headline character the brief asked for, without a second family.
- **One family.** v1.4–v1.7 paired it with Geist Mono for metadata. In v1.8 that was dropped: the mono read as code, and one family looks calmer and more modern. Tabular figures keep years and counts aligned.

## Variants
Weights in use: 400 (reading), 500 (names and actions), 600 (wordmark only). Width: 90% for `display-xl` and `display-lg`, 100% everywhere else. Italic is available for emphasis in prose.

## Sizes
The type scale is unchanged (same sizes and line heights). Tracking changed:

| Style | Before (Geist) | After (Instrument Sans) |
|---|---|---|
| display-xl / display-lg | −0.045em | −0.025em + 90% width |
| h1 / h2 | −0.03em | −0.015em |
| h3 | −0.02em | −0.01em |
| h4 | −0.015em | −0.005em |
| body, label, caption | 0 | 0 |

## States
n/a.

## Themes
Same in both. Instrument Sans at 400 holds up on midnight without needing a heavier weight.

## Responsive behavior
Display sizes step up at 768px and 1024px as before. The 90% width applies at every size, so long headlines wrap later on mobile.

## Accessibility
- UI labels stay at 500 (checked at 14px, where they render as firmly as Geist 500 did). No text in the system drops below 12px, except the non-essential `micro`.
- Condensed width is only for display sizes (≥36px). Reading text is never condensed.
- Sizes are rem and line heights are unitless, so user font settings and text-spacing overrides still work.

## Token dependencies
`font-sans` (Instrument Sans) · `font-meta` (Instrument Sans, metadata) · `font-width-display` `font-width-text` · `tracking-display|heading|h3|h4|body|label` · all `type-*` and `line-*` · `weight-regular|medium|semibold`
