# Typeface

Instrument Sans is the primary typeface from v1.4. Geist Mono stays as the secondary face, but only for metadata. This card keeps the before and after on record, plus the full ramp with metrics read live from the rendered text.

## Anatomy
- **Primary**: Instrument Sans, variable: weights 400–700, width 75–100%, with italics. Loaded from Google Fonts. The fallback is system `sans-serif`.
- **Secondary**: Geist Mono 400 and 500. It sets metadata only: years, dates, counts, versions, numbering, time codes, URL prefixes.

## Why Instrument Sans
- **Distinctiveness.** Geist is strongly associated with Vercel, so a system set in it reads as a Vercel derivative. Instrument Sans is a slightly narrow grotesque with more editorial warmth, and it's recognisable without being decorative.
- **Editorial headlines.** The width axis allows condensed display type (`font-width-display` 90%), which is the Stripe-like headline character the brief asked for, without a second family.
- **Pairing.** Geist Mono's geometric construction contrasts cleanly with Instrument's humanist proportions. One face reads as prose, the other as data.

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
`font-sans` (Instrument Sans) · `font-mono` (Geist Mono) · `font-width-display` `font-width-text` · `tracking-display|heading|h3|h4|body|label` · all `type-*` and `line-*` · `weight-regular|medium|semibold`
