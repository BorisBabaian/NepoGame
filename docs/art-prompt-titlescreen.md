# Title Screen Background — prompt

The menu background is `game/images/menu_bg.png`. Replace the generated
placeholder with your own art.

**Export at 3840x2400** (2x of the 1920x1200 window) and save the full-res file —
this is what keeps the menu crisp on a Retina screen. If the tool only gives 16:9,
generate 3840x2160 and add a little paper at top/bottom to reach 16:10, or just let
it sit letterboxed (the bars are paper-white now).

## Composition (important — this is a menu, art must not fight the text)

- **Top ~30% stays calm and near-empty:** the title "Nepo The Game", the tagline,
  and the "BUSINESS AND MANAGEMENT IN A GLOBAL CONTEXT" line sit there.
- **Center vertical strip stays open too:** the four chapter cards and Quit stack
  down the middle. Keep a clear, uncluttered gutter through the center.
- Put all the detail in the **left margin, right margin, and bottom edge.**

## STYLE PREFIX (paste before the scene text)

> Hand-drawn black ink line illustration on warm off-white paper (#fcfbf7),
> editorial New Yorker cartoon style, single-weight pen line with slight hand wobble,
> sparse cross-hatching for shadow only, no grey fills, no color, elegant and
> satirical, full-bleed to the edges, no border or frame.

## NEGATIVE

> color, grey shading, gradients, screentone, photorealism, 3D render, text,
> lettering, numbers, logos, brand names, watermark, signature, busy center,
> heavy dark areas at the top

## Primary prompt — "The Desk: two lives, top-down"

A satirical top-down flat-lay of a single desk surface, drawn in fine black ink on
warm paper, split by contrast down the middle. The **left half is the old life**: a
careless spill of expensive things — a heavy Swiss luxury wristwatch, an open bottle
of vintage champagne tipped beside a single coupe glass, a fanned stack of banknotes,
a fat cigar in a crystal ashtray, a signet ring, sports-car keys on a leather fob, a
platinum credit card. Everything overlapping, extravagant, a little decadent. The
**right half is the new life**: one plain white dress shirt, neatly folded, with a
cheap plastic employee ID badge clipped to the collar (badge blank, no legible text),
a single ballpoint pen and a paper coffee cup beside it. Nothing else. Between the two
halves runs a bare, empty stretch of desk. The upper area of the desk is clear, open
paper. Objects cluster toward the left edge, the right edge, and the bottom. Elegant,
absurd, quietly expensive on one side and austere on the other. Flat overhead view.

## Alternative A — "Wardrobe rail, left to right"

A top-down or straight-on ink drawing of a wardrobe rail. From the left hang several
pieces of obviously expensive designer clothing — a tailored dinner jacket, a fur
collar, a silk robe, a garment bag — drawn rich and heavy. They thin out toward the
right, and at the far right hangs one plain white analyst's shirt with a small ID
badge clipped to it (blank, no text). The contrast is the whole point: opulence on the
left dissolving into a single humble shirt on the right. Warm paper, open space above
the rail for the title.

## Alternative B — "Skyline" (the earlier idea, kept)

> A satirical establishing view of high finance and old money in fine black ink on
> warm paper. A grand glass skyscraper on the right, an ornate members-club facade on
> the left with columns and a striped awning, a lone convertible parked across two
> spaces between them, a doorman in a top hat. A faint champagne coupe and a few
> bubbles float above the skyline. The upper third is open sky with light cloud
> hatching, kept airy for the title.

## After generating

Save as `game/images/menu_bg.png`. Reload the game — the menu picks it up
automatically. If the title or cards are hard to read over the art, tell me and I
will drop a soft paper scrim behind them.
