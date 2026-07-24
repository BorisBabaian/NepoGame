# core/state.rpy — Player state foundation (see docs/TECHNICAL_PLAN.md §2)
#
# All per-playthrough state lives in one PlayerState object declared with
# `default`, so it is saved in save slots and participates in rollback.
# RULE: only ADD fields to this class; never rename/remove (save compat).

init -10 python:

    class PlayerState(object):

        def __init__(self):
            # Identity (set during the prologue)
            self.first_name = "P."       # replaced at the badge printer
            self.portrait = None         # portrait id chosen at the mirror
            self.gender = "m"            # see core/pronouns.rpy

            # Progression
            self.chapter = "ep00"        # current stage of the game
            self.level = 1
            self.xp = 0

            # The two persistent meters (scenario §3):
            #   reputation — what the firm thinks of the hero
            #   composure  — what the hero has left
            self.meters = {"reputation": 0, "composure": 0}

            # Mechanics
            self.abilities = set()       # Field Manual framework cards
            self.stats = {}              # misc relationship points
            self.flags = set()           # story event flags

        # -- flags ------------------------------------------------------

        def set_flag(self, name):
            self.flags.add(name)

        def has_flag(self, name):
            return name in self.flags

        # -- sync -------------------------------------------------------

        def to_dict(self):
            """Flat summary for server sync / debugging. One source of truth."""
            return {
                "first_name": self.first_name,
                "portrait": self.portrait,
                "gender": self.gender,
                "chapter": self.chapter,
                "level": self.level,
                "xp": self.xp,
                "meters": dict(self.meters),
                "abilities": sorted(self.abilities),
                "stats": dict(self.stats),
                "flags": sorted(self.flags),
            }


default player = PlayerState()


# Save migration (TECHNICAL_PLAN.md §2): fields are only ever ADDED, and
# saves made before a field existed are healed here on load. This is what
# keeps "add a feature now" from breaking "load an old save later".
init python:

    def _migrate_player(*args):
        defaults = {
            "gender": "m",
            "meters": {"reputation": 0, "composure": 0},
            "abilities": set(),
            "stats": {},
            "flags": set(),
        }

        changed = False
        for field, value in defaults.items():
            if not hasattr(player, field):
                setattr(player, field, value)
                changed = True

        if changed:
            # Required by the docs: without this, rolling back past the load
            # point would revert the migration and reintroduce the missing field.
            renpy.block_rollback()

    config.after_load_callbacks.append(_migrate_player)

# Dynamic display name for the hero character (see characters.rpy).
# "P. VAULMONT" until the badge printer; the chosen first name after.
default hero_name = "P. Vaulmont"
