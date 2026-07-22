## Nepo The Game — design code (mirrors bm-game/src/styles.css).
## Paper white ground, ink black line work, serif narration, handwritten notes.

init python:
    gui.init(1920, 1080)

    ## Fonts. Drop CormorantGaramond-Medium.ttf, CormorantGaramond-Bold.ttf and
    ## Caveat-Regular.ttf into game/fonts/ for the exact web look.
    ## Until then the bundled DejaVu Serif is the stand in.
    def nepo_font(preferred, fallback):
        return preferred if renpy.loadable(preferred) else fallback

define nepo.serif = nepo_font("fonts/CormorantGaramond-Medium.ttf", "fonts/DejaVuSerif.ttf")
define nepo.serif_bold = nepo_font("fonts/CormorantGaramond-Bold.ttf", "fonts/DejaVuSerif-Bold.ttf")
define nepo.hand = nepo_font("fonts/Caveat-Regular.ttf", "fonts/DejaVuSerif-Italic.ttf")

## Palette (styles.css :root).
define nepo.paper = "#fcfbf7"
define nepo.ink = "#141414"
define nepo.ink_soft = "#3a3a3a"
define nepo.ink_faint = "#8a8781"

define gui.text_color = nepo.ink
define gui.interface_text_color = nepo.ink
define gui.idle_color = nepo.ink_faint
define gui.hover_color = nepo.ink
define gui.selected_color = nepo.ink
define gui.insensitive_color = "#8a878180"
define gui.accent_color = nepo.ink

define gui.text_font = nepo.serif
define gui.name_text_font = nepo.serif_bold
define gui.interface_text_font = nepo.serif

define gui.text_size = 40
define gui.name_text_size = 30
define gui.interface_text_size = 36
define gui.notify_text_size = 40

define gui.main_menu_background = "images/bg_paper.png"
define gui.game_menu_background = "images/bg_paper.png"

## Dialogue window geometry.
define gui.textbox_height = 300
define gui.textbox_yalign = 1.0

define gui.name_xpos = 0.5
define gui.name_xalign = 0.5
define gui.name_ypos = -26

define gui.dialogue_xpos = 360
define gui.dialogue_width = 1200
define gui.dialogue_ypos = 78
define gui.dialogue_text_xalign = 0.5
