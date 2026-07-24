# gui.rpy — design code "The Jaded Euro" (from styles.css)
#
# Paper-white ground, hand-ink black line work, elegant serif narration,
# handwritten annotations. No color except ink; emphasis via weight & space.

init offset = -2

init python:
    gui.init(1920, 1080)

## Palette (styles.css :root) ------------------------------------------------

define gui.paper     = "#fcfbf7"   # --paper
define gui.ink       = "#141414"   # --ink / --line
define gui.ink_soft  = "#3a3a3a"   # --ink-soft
define gui.ink_faint = "#8a8781"   # --ink-faint
define gui.white     = "#ffffff"

## Fonts ----------------------------------------------------------------------
## Drop the real fonts into game/fonts/ (free on Google Fonts):
##   CormorantGaramond-Regular.ttf  — --font-serif
##   Caveat-Regular.ttf             — --font-hand
## Until then, Ren'Py's bundled font is used as a fallback.

define gui.serif = ("fonts/CormorantGaramond-Regular.ttf"
    if renpy.loadable("fonts/CormorantGaramond-Regular.ttf") else "DejaVuSans.ttf")

define gui.hand = ("fonts/Caveat-Regular.ttf"
    if renpy.loadable("fonts/Caveat-Regular.ttf") else gui.serif)

## Ink frames (.ink-frame: 2.5px border, offset shadow feel) -------------------

define gui.panel       = Frame("gui/ink/panel.png", 10, 10)        # white + ink border
define gui.panel_hover = Frame("gui/ink/panel_hover.png", 10, 10)  # inverted (hover)
define gui.panel_paper = Frame("gui/ink/panel_paper.png", 10, 10)  # paper + ink border

## Type scale (1920x1080; CSS clamp values scaled from the 680px page) ---------

define gui.text_size      = 33    # .narration / .dialogue .line
define gui.name_size      = 26    # .dialogue .speaker
define gui.interface_size = 26
define gui.label_size     = 30
