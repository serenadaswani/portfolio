# Refinement audit (v1.3)

A craft pass over existing components. **No token values changed.** Only how components use the tokens changed, plus usage notes. Tabs, Input, CheckboxRadio, Popover and Dialog were missing, so they were added in the same language.

## Highest-impact issues found
1. **Everything sat in a filled box.** Cards and panels relied on Mineral fills, so hierarchy came from containers rather than type.
2. **One small-text style for everything.** Eyebrows, nav headings, metadata keys and divider labels all shared 13px uppercase tracked text, the most obvious "generated UI" tell.
3. **No shape logic.** Buttons, inputs, cards and media all sat at 8–12px, and status badges were pills.
4. **Floating treatments.** v1.2 hover shadows lifted cards, buttons and thumbnails off the page.
5. **Over-signalled selection.** Fill + colour + bar + border at once.
6. **Icon drift.** Sizes from 14 to 20px, strokes thinning when scaled, and decorative extras (card CTA line, tooltip arrows, browser-chrome dots).

## System rules introduced
| Rule | Detail |
|---|---|
| Type roles | names sans 500 · reading sans 400 · metadata Geist Mono 12, tertiary, tabular · no uppercase anywhere |
| Shape | sm = controls and labels · md = containers · lg = artifact stages · nested radius = outer − padding |
| Depth | tone + 1px at rest and on hover · `shadow-md` only for Popover and Dialog |
| Cobalt | primary fill, focus, and one precise selection cue (2px rule or tick). Tertiary hover is neutral. |
| Proportion | button padding-x ≈ 0.4 × height · icon side −`space-1` (optical) · rows 32 (pointer) / 44 (touch) |
| Icons | Lucide (shadcn/ui's set) since v1.5: 16px in UI, 14 at xs and in status, 12 in badges, 20 in empty states; stroke 2; only where they add meaning |
| Rhythm | tight inside a group (`space-1`–`space-2`), wider between groups (`space-4`+), and card grids have more vertical than horizontal gap (40 / 24) |

## Component by component
| Component | What felt generic | Change |
|---|---|---|
| Button | 8px radius; hover shadows; tertiary hovered in cobalt tint; inconsistent padding | `radius-sm`; no shadows; secondary hover darkens the border only; tertiary and ghost hover use a neutral wash; padding-x ≈ 0.4h; optical icon padding; ghost rests in secondary text |
| Link | — (already text-only) | subtle variant gets a quiet `border-strong` underline |
| Top nav | filled selected tab with a bar; 64px bar; fill hover | 56px bar; full-height items; current page = one 2px cobalt rule on the hairline; text-only hover |
| Side nav | 40–44px rows; selected fill + bar; uppercase heading | 32px rows (44 touch); selection = primary text + 500 + cobalt tick, no fill; sentence-case caption heading; mono counts |
| In-page nav | uppercase heading | caption heading; baseline-aligned mono numbers |
| Card | filled container; hover lift + shadow; uppercase eyebrow; redundant CTA line | frameless: hairline image well + type; mono eyebrow, year first; hover darkens the well edge and underlines the title; CTA removed; outlined variant with flush media for dense grids; 7/5 asymmetric horizontal layout |
| Panel | Mineral fill by default; uppercase dt; big padding | default = 1px border on elevated paper; tonal variant for asides; spec-sheet metadata rows on hairlines; mono dates; tonal footer strip |
| Badge | pills for status; 13px tracked uppercase feel | `radius-sm` everywhere; outline tags; mono variant for technical values; 12px glyphs |
| Tooltip | arrow; label-weight body | no arrow; caption 500; optional mono `<kbd>` shortcut |
| Divider | uppercase tracked label | mono caption label, left-aligned |
| Image frame | dots in browser chrome; sans "Figure 3" | chrome reduced to an address bar; mono `Fig. 03`; notes as hairline rows with mono counters; nested radius |
| Thumbnail | hover shadow; 8px radius | `radius-sm` (it's a control); hover = `border-strong` edge |
| Video | 6px track, 16px thumb | 4px track, 12px thumb, mono timecodes |
| Tabs (new) | — | underline tabs on a hairline with a cobalt rule; segmented control with nested radii for view switches |
| Input (new) | — | always-visible label; 3:1 border; 2px focus edge (no glow); mono prefix; hint and error under the field; 16px text on touch |
| CheckboxRadio (new) | — | native controls, accent-tinted, aligned to the first line |
| Popover / Dialog (new) | — | elevated + hairline + `shadow-md` (the only shadows); tonal footer; stacked actions on mobile |

## Kept on purpose
Palette, semantic tokens, type scale, spacing scale, radii values, focus treatment (3px at 3px offset; inset in dense groups), link treatment, the dark-scoped lightbox and video, and every accessibility behaviour from v1.1 and v1.2.
