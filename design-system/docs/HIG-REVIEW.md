# HIG review (v1.5)

The whole system checked against Apple's Human Interface Guidelines, as they apply to a website. The goal is HIG-quality *behaviour* (clarity, deference to content, accessibility, predictable interaction) with Paper × Midnight's own visual language. It doesn't use SF Pro, translucent materials or Apple's component shapes.

| HIG area | Guidance | Status | How it's met |
|---|---|---|---|
| Layout · touch targets | 44×44pt minimum on touch | Met | `control-height-md|lg` and `control-min-target` grow to 44 / 52 / 44 under `pointer: coarse`. Rows and choices get a 44pt minimum height. |
| Layout · pointer controls | macOS controls are compact (about 22–28pt) | Met | xs 24, sm 32, md 40, lg 48 for mouse and trackpad, with `space-2` or more between small targets |
| Layout · safe areas | Keep content clear of notches and the home indicator | **Fixed** | Top nav, lightbox bars and the sheet footer pad with `env(safe-area-inset-*)`. Pages need `viewport-fit=cover`. |
| Layout · concentric corners | Inner radius = outer − padding | Met | Shape rule: segmented control 8 = 4 + 4, frame stage 12 → media 4 |
| Typography · Dynamic Type | Respect the user's text size | Met | rem sizes and unitless line heights. Containers have no fixed heights. |
| Typography · legibility | Body around 16–17pt; nothing essential below 11pt | Met | Body 16, UI 14, metadata 12, `micro` 11 for non-essential only |
| Color · contrast | 4.5:1 text, 3:1 UI | Met | Live contrast strip on every component, in both themes |
| Accessibility · Increase Contrast | Stronger separators and secondary text | **Fixed** | `prefers-contrast: more`: hairlines become 3:1 borders and tertiary text steps up a level, in both themes |
| Accessibility · Reduce Transparency | Replace translucent layers with opaque ones | **Fixed** | `prefers-reduced-transparency`: scrims and backdrops become opaque Ink |
| Accessibility · Reduce Motion | Remove non-essential motion | Met | All transitions, the shimmer and the sheet rise are gated on `prefers-reduced-motion` |
| Dark Mode | Elevated surfaces are lighter in dark | Met | Midnight → Deep blue → Night raised. Same hierarchy in both themes. |
| Interaction · feedback | Visible response on press; no hover-dependence on touch | **Fixed** | Hover rules live under `@media (hover: hover)` (no stuck hover after a tap). `:active` states on every control. `touch-action: manipulation` removes the double-tap delay. |
| Interaction · focus | Clear keyboard focus | Met | 3px ring at 3px offset; inset in dense groups; link focus as underline + tint |
| Buttons | One prominent button per view; clear hierarchy | Met | primary / secondary / tertiary / ghost; guidelines forbid two primaries |
| Modality · sheets | On compact width, present modals as sheets | **Fixed** | Dialog becomes a bottom sheet below 768px: full width, top corners, safe-area footer, stacked actions |
| Modality · alerts | Cancel and default actions are clearly ordered | Met | Cancel then primary on wide screens; primary on top when stacked |
| Popovers | Use for brief, non-modal content | Met | Non-modal, dismissed by Esc or outside click, focus returns |
| Help tags / tooltips | Never essential; not available on touch | Met | Shown on focus as well as hover. Icon buttons are named by `aria-labelledby`. |
| Segmented controls | Switch views of the same content | Met | `pm-tabs--segmented`, with tabs for distinct content |
| Text fields | Visible labels; placeholder isn't a label | Met | Always-visible labels, hints and errors linked by `aria-describedby` |
| Toggles | Use a switch for an instant on/off setting | n/a | No setting like that exists yet. Checkboxes are used for form consent. |
| Icons · SF Symbols | Use one consistent symbol set at matching weight | Met (Lucide) | One family, one stroke weight, sizes tied to text, centred on the first line |
| Materials | Translucency to show context | Deliberately not used | The brand calls for flat, opaque surfaces. Scrims are the only translucent layer, and they become opaque under Reduce Transparency. |

**Not verifiable here:** VoiceOver behaviour on a real device, Safari rendering of `prefers-reduced-transparency`, and the home-indicator inset. Test these on iPhone and iPad before launch.
