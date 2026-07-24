# options.rpy — project configuration

define config.name = _("BMGC")
define config.version = "0.1.0"

## Save files location (unique id, do not change after release)
define config.save_directory = "NepoGame-BMGC"

define config.has_autosave = True
define config.has_quicksave = True
define config.has_music = True
define config.has_sound = True

## Saves ---------------------------------------------------------------------
## Autosave runs roughly every N interactions. Ren'Py's default (200) is very
## sparse for a story-heavy game; 40 keeps the automatic page genuinely useful
## without noticeable hitching.
define config.autosave_frequency = 40

## How many slots the automatic rotation cycles through.
define config.autosave_slots = 6

## Save-on-exit uses the documented `_quit_slot` store variable, set in
## scripts.rpy. See that file for why it isn't defined here.

## Dialogue history depth (History screen)
define config.history_length = 250

## Save slot thumbnails
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Menu transitions — quiet, paper-like
define config.enter_transition = Dissolve(0.15)
define config.exit_transition = Dissolve(0.15)
define config.intra_transition = Dissolve(0.15)
define config.after_load_transition = None
define config.end_game_transition = None

## Build rules
define build.name = "BMGC"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
