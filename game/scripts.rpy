# scripts.rpy — entry point. Story lives in story/, mechanics in core/.

## Save-on-exit -----------------------------------------------------------
## `_quit_slot` is a Ren'Py store variable: if it holds a slot name, the game
## is saved into that slot when the player quits. It must be assigned at
## runtime (not with `default`, since Ren'Py already defines it as None), so
## it is set here at the start of a new game and re-applied after every load.

init python:

    QUIT_SLOT = "auto-1"

    def _arm_quit_save(*args):
        store._quit_slot = QUIT_SLOT

    # Re-arm after loading an older save that predates this feature.
    config.after_load_callbacks.append(_arm_quit_save)


label start:
    $ _arm_quit_save()
    jump ep00_prologue
