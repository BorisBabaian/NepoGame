# core/meters.rpy — the two persistent meters (scenario §3)
#
#   Reputation — what the firm thinks of the hero.
#   Composure  — what the hero has left.
#
# "Choices shift both, and every shift is shown as a handwritten margin note."
# The note is rendered by ui/screen_margin_note.rpy in the Caveat hand,
# matching .effect-note from styles.css.
#
# Story usage:
#     $ shift(reputation=1, composure=-2)

init python:

    METER_LABELS = {
        "reputation": _("Reputation"),
        "composure": _("Composure"),
    }

    def meter(name):
        return getattr(player, "meters", {}).get(name, 0)

    def shift(reputation=0, composure=0):
        """Adjust meters and show the handwritten margin note."""
        notes = []

        for key, amount in (("reputation", reputation), ("composure", composure)):
            if not amount:
                continue
            player.meters[key] = meter(key) + amount
            notes.append(u"{} {:+d}".format(METER_LABELS[key], amount))

        if notes:
            renpy.show_screen("margin_note", lines=notes)

        queue_sync()
