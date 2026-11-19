I'm rebuilding screens from an approved prototype I designed during my OmniSynkAI internship (my PM approved using it in my portfolio). I've attached 10 reference PNGs (2252×1666, exported from the prototype video). Rebuild them as editable frames in a new Figma file called "OmniSynkAI – Case study screens". Accuracy matters more than speed.

## How to work
1. Build ONE screen first: "03 · Listing autofilled" (it has the most UI). Don't start any other screen until it matches.
2. Before drawing anything, place the reference PNG on the canvas in its own frame, scaled to 1440×1064, locked, on a layer named "REF". Build the new frame directly on top of it.
3. Check your work by setting the REF layer to 50% opacity and taking a screenshot. Anything that doesn't line up (edges, text baselines, icon positions) is a bug: fix it before moving on. Do this at least twice per screen and tell me what you fixed each round.
4. Once 03 matches, turn its shared parts into components (side nav, page header, autofill bar, card, input, select, tag chip, primary/secondary button, modal shell). Build every other screen by duplicating 03 (or 01 for the empty states) and changing only what differs. Never rebuild a screen from scratch.
5. Modals: same component for all of them (white, rounded, header row with optional back chevron, divider, body, divider, footer buttons). The page behind a modal is the same screen with a dark overlay, not a redraw.
6. Don't invent anything. If text is hard to read, zoom into the reference; if it's still unclear, leave a "?" and list it for me.
7. Hide the REF layers when finished (don't delete them), and give me a list of anything you couldn't match.

## Measurements (taken from the screenshots, at 1440 wide; treat as ±2px)
- Frame: 1440×1064, page background #F5F5F7
- Side nav: 108px wide, #1B181C. Logo at the top, then a white rounded-square "+" button and a settings gear; logout icon at the bottom
- Page header: white strip, 0–132px tall. Breadcrumb "Main menu › Modules › Finance" (~13px), title "Create a new listing" (~24px, semibold) below it. Content starts 24px right of the nav
- Gutters: 24px from the nav, ~23px from the right edge, ~12px between cards
- Cards: white, ~8px radius, 1px light grey border
  - Autofill bar: y 156–278, full content width
  - Left column (~946px wide): Description y 291–485, Media y 498–910, Brand + Tags y 923–1040
  - Right column (~325px wide): Listing status y 291–396, Product organization y 409–644
- Primary button: #4461DC, white text, ~150×43, ~6px radius. Disabled: #B5C0EF
- Secondary button: white, 1px light border, dark text
- AI-generated content (brand, tags): chip with background #ECE4F5 and purple text (~#7E3CD8). When the tone changes, the previous tags turn plain and only the new ones are highlighted
- Sparkle / Autofill icon: purple (~#A599D9 to #7E3CD8 gradient)
- Empty media slots: 1px dashed border #B4B3C9 with an "add image" icon
- Modal: ~440px wide, white, ~10px radius, title ~20px semibold, overlay behind it darkens the page (page background reads as #BDBCC1)
- Font: a geometric sans (it looks like Plus Jakarta Sans). Before building, open the original Figma file I can view, click a text layer, and use the exact font family, sizes and weights shown in its properties panel. Read colours from there too if they're visible, and use those instead of my sampled values. Only read values; don't try to copy or export from that file.

## Screens (same order as the PNGs)
01 Empty listing · 02 Autofill in progress (modal) · 03 Listing autofilled · 04 Change tone (modal) · 05 Tone changed (new tags highlighted) · 06 Clear listing confirmation (modal) · 07 More options menu (dropdown: Regenerate, Clear fields, Change tone) · 08 Select platforms (modal) · 09 Confirm and publish (modal) · 10 Listing complete (modal)

- Product photos: grey rectangles, same sizes and positions. I'll drop the images in myself
- Leave out the mouse cursor
- Name the frames exactly as the PNG file names
