# characters.rpy — the season's cast (scenario §2)
#
# Style note (styles.css .dialogue): speaker names in tracked caps,
# spoken lines italic; narration stays upright.

## The hero ------------------------------------------------------------------
# The speaker label is always "You" — the player is the hero, and the whole
# point of the season is that the name on the badge is not yet worth much.
# The typed first name still lives in `hero_name` / player.first_name and is
# used on the badge itself, in telemetry, and by other characters.
define hero = Character("You", what_italic=True)

## The estate ----------------------------------------------------------------
define father = Character("FATHER", what_italic=True)
define nestor = Character("NESTOR", what_italic=True)

## McQuinsey & Company -------------------------------------------------------
define vergeau = Character("MME VERGEAU", what_italic=True)
define prov    = Character("PROV", what_italic=True)       # theory, Module 1+
define piedad  = Character("MS PIEDAD", what_italic=True)  # HR, Interlude

## The season's society ------------------------------------------------------
define maxi     = Character("MAXI GELDMANN", what_italic=True)
define tanaka   = Character("TANAKA SAN", what_italic=True)
define chairman = Character("THE CHAIRMAN", what_italic=True)
define waiter   = Character("THE WAITER", what_italic=True)
