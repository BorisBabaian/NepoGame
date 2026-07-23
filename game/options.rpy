## Nepo The Game — project options.

define config.name = _("Nepo The Game")
define config.version = "0.1"
define gui.about = _("A satirical career simulation.\nDesign code: black ink on paper white.")

define build.name = "NepoGame"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

## Always show our own compact menu button (top-right), nothing else.
define config.overlay_screens = ["nepo_menu_button"]

## Escape / right-click open our minimal pause menu instead of the full game menu.
define config.game_menu_action = ShowMenu("pause_menu")

## Transitions.
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.window_hide_transition = Dissolve(0.2)
define config.window_show_transition = Dissolve(0.2)

define config.window = "auto"

## Letterbox bars (shown on aspect ratios other than 16:10) are paper white,
## not black, so they read as an intentional margin rather than a defect.
define config.gl_clear_color = "#fcfbf7"

define config.save_directory = "NepoGame-1"
define config.window_icon = None
