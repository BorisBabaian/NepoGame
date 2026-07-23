# Nepo The Game — Art Prompts (full-screen visual novel)

The game is now a full-screen VN. Each beat is a **16:9 background that fills the
screen**, with the dialogue bar and namebox overlaid on the lower third. So the art
brief changed from framed 4:3 panels to full-bleed 1920x1080 illustrations.

## Where files go

- Backgrounds: `game/images/bg/<name>.png` — 1920x1080 (or 2x: 3840x2160), 16:9.
  Names the engine already looks for (prologue): `wake, mirror, hall, card, monday,
  office, coffee, badge, descent`. Drop a file in and it replaces the placeholder.
- Character sprites (optional, for extra life): `game/images/sprites/<name>.png` —
  transparent PNG, full-height figure. Layer over a room background with
  `show <name>` in the script.
- Mirror portraits (character creation): `game/images/portraits/p1..p6.png` — 3:4.

## STYLE PREFIX (prepend to every prompt)

> Hand-drawn black ink line illustration on warm off-white paper (#fcfbf7),
> editorial New Yorker cartoon style, single-weight pen line with slight hand wobble,
> sparse parallel hatching for shadows only, no grayscale fills, no color, elegant
> satirical high-society mood, wide cinematic 16:9 composition. Leave the lower third
> calmer and less detailed so an overlaid text box stays readable. No drawn frame,
> full-bleed to the edges.

## NEGATIVE

> color, grayscale shading, gradients, screentone, photorealism, 3D render, text,
> lettering, speech bubbles, watermark, signature, frame, border, busy bottom third,
> dark heavy backgrounds

## Composition rule for VN backgrounds

Keep the subject in the upper two thirds. The bottom ~28% of the frame is where the
dialogue bar sits, so leave it as open floor, table surface, water, sky, or light
hatching. Never place a face or key detail in the bottom center.

---

## Backgrounds — Prologue (file name → prompt)

**wake** — A vast bedroom late morning. Canopy bed with rumpled silk sheets upper
left, tall windows with heavy velvet curtains letting in one blade of light, a
decorative alarm clock reading 10:47 on a nightstand. Camera wide, room recedes to the
right. Lower third: empty carpet and a discarded dinner jacket.

**mirror** — A palatial marble bathroom. An enormous gilded rococo mirror dominates
the upper center, its glass an empty oval of light. A shelf of identical unopened soap
bottles to one side. Lower third: the clean marble vanity surface, mostly empty.

**hall** — A grand breakfast hall. A table for forty seen in dramatic perspective,
set for only two at opposite ends. Chandeliers above. At the far end a figure hidden
behind a raised broadsheet newspaper whose front page shows a yacht and a harbour
crane. Lower third: the long empty tablecloth running toward the viewer.

**card** — Close, quiet composition. A small open velvet box held in white-gloved
butler's hands upper center, a platinum credit card lying inside like a body in state.
Soft focus on the surrounding desk. Lower third: the polished table surface.

**monday** — Exterior office-tower forecourt at 8:58 AM. A glass skyscraper soars up
and out of the top of the frame. A convertible parked diagonally across two marked
parking bays, one stencilled CFO. A small confident figure walking away from it toward
glass doors. Lower third: empty pavement with parking-line markings.

**office** — A corner office on a high floor. Two floor-to-ceiling windows with clouds
BELOW the horizon line (very high up), an oversized office plant, a designer desk with
a laptop. Cartoon grandeur, slightly absurd emptiness. Lower third: the open desk
surface and floor.

**coffee** — An office coffee point. A tall bistro table with two tiny espresso cups
upper center, a sleek espresso machine behind. Two implied conversation positions.
Wide, airy. Lower third: the floor and the base of the table.

**badge** — Close on a bureaucratic badge printer on a side table, one small blinking
light, a blank white badge sliding out of its slot. Faint dramatic hatching radiating
behind it like a small guillotine. Lower third: the tabletop, empty.

**descent** — Interior of a glass elevator descending. The floor indicator shows 3.
Through the glass wall, far below, an open-plan office floor with rows of identical
desks and one tiny lone desk beside a photocopier. A single small figure inside the
lift. Lower third: the lift floor.

## Character sprites (optional, transparent PNG, full height)

Generate on a plain white or transparent background, full standing figure, same ink
style, so they can be layered over room backgrounds. Consistent faces via a character
reference image.

- **father** — man in his sixties, iron grey hair, heavy glasses, double breasted
  suit, holding a folded newspaper, expression of permanent judgement.
- **nestor** — tall gaunt ancient butler, white gloves, tailcoat, perfect posture,
  professionally unsurprised.
- **vergeau** — woman ~60, severe silver bob, thin angular glasses, floor-length
  column gown, holds a champagne flute she never drinks from, mild permanent
  disappointment.

## Mirror portraits — character creation (`portraits/p1..p6.png`, 3:4)

Head-and-shoulders in an ornate gilded oval mirror frame, young person in silk
pyjamas, morning light, slightly too pleased with themselves. Vary across the six:
different hair, build, and gender presentation so players can pick.

## Production notes

- Order: 3 character references (father, nestor, vergeau) → 9 prologue backgrounds
  → 6 mirror portraits. That is a complete, playable prologue.
- Generate at 3840x2160 if the tool allows, then downscale to 1920x1080 for the game,
  keeps lines crisp.
- Attach your "Jaded Euro" reference pages as the style image on every generation.
- Convert finals to PNG (or WebP) and drop into the folders above. No code changes
  needed, the engine swaps placeholders for real files automatically.
