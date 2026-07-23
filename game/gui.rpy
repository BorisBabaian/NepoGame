## Nepo The Game — design code (mirrors bm-game/src/styles.css).
## Paper white ground, ink black line work, elegant serif, full-screen VN.

init python:
    gui.init(1920, 1080)

    ## Fonts. Lora ships with the project (elegant serif, close to the web mock).
    ## Drop CormorantGaramond / Caveat into game/fonts/ to match the web exactly.
    def nepo_font(preferred, fallback):
        return preferred if renpy.loadable(preferred) else fallback

define nepo.serif = nepo_font("fonts/CormorantGaramond-Medium.ttf", "fonts/Lora.ttf")
define nepo.serif_bold = nepo_font("fonts/CormorantGaramond-Bold.ttf", "fonts/Lora.ttf")
define nepo.serif_italic = nepo_font("fonts/Lora-Italic.ttf", "fonts/Lora-Italic.ttf")
define nepo.hand = nepo_font("fonts/Caveat-Regular.ttf", "fonts/Lora-Italic.ttf")

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

## A touch bigger for a proper serif; Lora runs small.
define gui.text_size = 44
define gui.name_text_size = 30
define gui.interface_text_size = 38
define gui.notify_text_size = 42

define gui.main_menu_background = "images/bg_paper.png"
define gui.game_menu_background = "images/bg_paper.png"

## Dialogue window (bottom VN bar).
define gui.textbox_height = 320
define gui.textbox_yalign = 1.0

define gui.dialogue_width = 1360
define gui.dialogue_ypos = 96
define gui.dialogue_text_xalign = 0.5

## Namebox — dark pill sitting on top edge of the textbox.
define gui.name_xpos = 0.5
define gui.name_xalign = 0.5
define gui.name_ypos = -34

## Choice buttons.
define gui.choice_button_width = 1100
define gui.choice_button_text_size = 38
define gui.choice_spacing = 24
