# core/pronouns.rpy — hero pronouns
#
# The scenario allows choosing the hero's gender. For now the text is male
# (as written in the final scenario), but EVERY pronoun in the narration goes
# through these variables. Turning the choice on later = calling set_gender()
# from the mirror; not a single line of story text has to be rewritten.
#
# Usage in story text (Ren'Py interpolation flags):
#     "[pr_he!c] opens Excel."      -> "He opens Excel."
#     "the cells beat [pr_him]"     -> "the cells beat him"

default hero_gender = "m"

default pr_he      = "he"
default pr_him     = "him"
default pr_his     = "his"
default pr_himself = "himself"
default pr_man     = "man"
default pr_son     = "son"

init python:

    PRONOUN_SETS = {
        "m": {"pr_he": "he",   "pr_him": "him",  "pr_his": "his",
            "pr_himself": "himself",  "pr_man": "man",    "pr_son": "son"},
        "f": {"pr_he": "she",  "pr_him": "her",  "pr_his": "her",
            "pr_himself": "herself",  "pr_man": "woman",  "pr_son": "daughter"},
    }

    def set_gender(code):
        """Switch every pronoun at once. Call from the mirror when the
        gender choice is enabled."""
        store.hero_gender = code
        for key, value in PRONOUN_SETS.get(code, PRONOUN_SETS["m"]).items():
            setattr(store, key, value)
        player.gender = code
