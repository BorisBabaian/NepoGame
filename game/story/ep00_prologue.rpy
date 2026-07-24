# story/ep00_prologue.rpy — PROLOGUE: "How the Money Ends"
#
# Follows the final scenario §5. Four player interactions, exactly as listed:
#   1. Face selection in the mirror
#   2. One low-stakes dialogue choice at breakfast
#   3. One deliberately unwinnable professional question
#   4. Name entry at the badge printer
#
# No grading, no theory. Pronouns go through core/pronouns.rpy.

label ep00_prologue:

    $ player.chapter = "ep00"

    ## The estate. 10:47. --------------------------------------------------

    scene black
    with fade

    "{i}10:47. The family estate.{/i}"

    scene bg bedroom
    with dissolve
    # play music "audio/theme_estate.ogg" fadein 2.0

    "Silk sheets. A canopy bed. A bedroom the size of a branch office."
    "The alarm has been set to 'decorative' since 2019."

    ## The mirror — CHARACTER CREATION -------------------------------------

    scene bg bathroom
    with dissolve

    "[pr_he!c] pads to the bathroom and meets [pr_his] own reflection in a gilded mirror."
    "The mirror, like everyone else in this house, is on the payroll."

    call screen mirror_portraits

    $ player.portrait = _return
    $ queue_sync()

    "The mirror approves. The mirror is paid to approve."

    ## Nestor ---------------------------------------------------------------

    show nestor
    with dissolve

    nestor "Your father requests your presence at breakfast."
    nestor "He used the word 'requests' loosely."

    hide nestor
    with dissolve

    ## The breakfast hall ---------------------------------------------------

    scene bg breakfast_hall
    with fade

    "A table for forty, set for two."

    show father
    with dissolve

    "Father sits at the far end, behind a financial newspaper."

    show cg newspaper
    with dissolve

    "The front page reports an incident involving a yacht, a harbour and a crane in Portofino."

    hide cg newspaper
    with dissolve

    father "Do you know what a margin is?"

    "The question is not rhetorical. It is worse. It is patient."

    father "It is what your yacht did to the harbour master's boat in Portofino."
    father "The fine has six digits. I have paid it."
    father "That was the last time."

    ## THE ONE LOW-STAKES CHOICE (scenario §5) ------------------------------
    ## Nothing is at stake but Composure — the firm does not exist yet.

    menu:
        "The correct answer does not exist. Several incorrect ones present themselves."

        "\"In fairness, the harbour master's boat was moored provocatively.\"":
            hero "In fairness, the harbour master's boat was moored provocatively."
            "Father does not look up. The newspaper does not move. Somewhere, a clock decides not to tick."
            father "Provocatively."
            hero "...it was very close to my yacht."
            $ shift(composure=1)
            "[pr_he!c] survives [pr_his] own sentence. Barely. It counts as a win."

        "\"I'm sorry. Genuinely.\"":
            hero "I'm sorry. Genuinely."
            father "You are sorry the way weather is sorry. It happens, and then it happens again."
            $ shift(composure=-1)
            "The apology lands somewhere on the table and is not picked up."

        "Say nothing. Let the newspaper speak.":
            "[pr_he!c] says nothing."
            "It is, statistically, the best thing [pr_he] has said all year."
            father "Good. You are learning the value of silence. It costs nothing, which is now your budget."

    ## The Ceremony of the Card ---------------------------------------------

    "Nestor approaches with a small velvet box, carrying it with the solemnity of a state funeral."

    show cg velvet_box
    with dissolve

    "The card is placed inside. The box clicks shut."

    # Epilogue hook: the box unlocks only if all four Members' Edition
    # cards are collected across the season.
    $ player.set_flag("velvet_box_locked")

    hide cg velvet_box
    with dissolve

    ## The assignment --------------------------------------------------------

    father "You start Monday. Vice Head of Special Projects at McQuinsey and Company."

    hero "What happened to the previous Vice Head?"

    father "There has never been one. Kristof owed me a favour."
    father "No allowance. No accounts. No calls to my office."
    father "You will live on a salary. Look the word up."
    father "The card returns when you have earned something that is not a reservation."

    hide father
    with dissolve

    "The newspaper rises again. The audience is over."

    ## The weekend -----------------------------------------------------------

    scene black
    with fade

    "The weekend passes in quiet despair, at a standard of comfort most people would describe as a holiday."

    scene bg estate_night
    with dissolve

    "On Sunday night, Nestor lays out a suit for the first working Monday of [pr_his] life."

    show nestor
    with dissolve

    nestor "Charcoal, sir. It photographs as competence."

    hide nestor
    with dissolve

    ## Monday. The arrival. ---------------------------------------------------

    scene bg driveway
    with fade
    # play music "audio/theme_firm.ogg" fadein 2.0

    "{i}Monday. 8:58 AM.{/i}"

    "The convertible comes to rest across two parking spaces."
    "One of them belongs to the CFO. This will matter later, though not to [pr_him]."

    scene bg lobby
    with dissolve

    "Beautifully dressed and radiantly smug, [pr_he] rides the glass lift to floor 67."

    scene bg floor67
    with dissolve

    "Corner office. Two windows. A plant taller than [pr_his] career."

    ## The Excel incident ------------------------------------------------------

    show cg excel
    with dissolve

    "[pr_he!c] opens a spreadsheet."
    "A full screen of cells stares back. [pr_he!c] stares. The cells win."

    hide cg excel
    with dissolve

    "Some battles choose you. This one [pr_he] declined."
    "[pr_he!c] closes the laptop and opens a dating app instead, where [pr_his] performance is historically stronger."

    ## Enter Mme Vergeau --------------------------------------------------------

    show vergeau
    with dissolve

    vergeau "Oh, you are the new one. Come. Coffee."
    vergeau "It is not optional here, like breathing."

    hide vergeau
    with dissolve

    ## The coffee point ----------------------------------------------------------

    scene bg coffee_point
    with fade

    show vergeau
    with dissolve

    "The small talk goes beautifully."
    "Weather, architecture, the criminal underrating of the view from 67. This is [pr_his] arena, and [pr_he] holds an unearned doctorate in it."
    "For four and a half minutes, [pr_he] is the most charming [pr_man] on the floor."

    "Then, mid-sip, the pivot."

    vergeau "So. Our client's margin is collapsing in the DACH region."
    vergeau "Your read?"

    ## THE UNWINNABLE QUESTION (scenario §5) --------------------------------------
    ## All three answers are equally poor by design: at this moment the hero
    ## knows exactly as much as the student playing him.

    "Somewhere inside [pr_his] head, a single slide bearing the word SYNERGY rotates slowly, and alone."

    menu:
        "Three answers present themselves. They are, without exception, terrible."

        "\"We should leverage cross-vertical synergies to re-platform the value narrative.\"":
            hero "We should leverage cross-vertical synergies to re-platform the value narrative."
            vergeau "..."
            vergeau "That sentence contained no information. It was structurally a sentence."

        "\"Have you tried marketing? More of it?\"":
            hero "Have you tried marketing? More of it? Visibly more?"
            vergeau "More marketing. On a collapsing margin."
            vergeau "You wish to spend your way out of not earning."

        "\"Margins are down four point seven percent. Classic. Textbook.\"":
            hero "Margins are down four point seven percent. Classic. Textbook, really."
            vergeau "They are down twelve point three."
            vergeau "You have invented a number, in front of me, at speed. That is almost a skill."

    $ shift(composure=-2)

    ## The badge -------------------------------------------------------------------

    "The temperature of the coffee point drops several degrees."

    vergeau "How does a person who cannot read a P&L become Vice Head of Special—"

    "Her eyes drop to the badge."

    show cg badge_old
    with dissolve

    "{b}P. VAULMONT{/b}"

    "A pause. The kind of pause that has its own line item."

    vergeau "Ah. Now I understand."

    hide cg badge_old
    with dissolve

    ## The sentence -----------------------------------------------------------------

    vergeau "Under my leadership, no nepotism."
    vergeau "Out of respect for your father, you are not fired."
    vergeau "Out of respect for the firm, you are no longer Vice Head of anything."

    "She takes the badge. It does not take long."

    $ shift(reputation=-3)

    ## The badge printer — NAME ENTRY -------------------------------------------------

    "A badge printer wakes up somewhere behind her. It sounds distinctly judgemental."

    python:
        new_name = renpy.input(
            _("The printer requires a first name. Only a first name."),
            default="Paul", length=14, exclude="{}[]%<>")
        new_name = new_name.strip() or "Paul"
        player.first_name = new_name
        hero_name = new_name
        queue_sync()

    show cg badge_new
    with dissolve

    "{b}[player.first_name]{/b}\n{i}Junior Analyst, probationary{/i}"

    hide cg badge_new
    with dissolve

    vergeau "Here you have no surname."
    vergeau "You will earn one back, or you will not."

    hide vergeau
    with dissolve

    ## The descent ---------------------------------------------------------------------

    scene bg lift
    with fade
    # play sound "audio/lift_hum.ogg"

    "The lift descends from 67 to 3."
    "The floor numbers tick down in silence, which is a language [pr_he] is only now beginning to learn."

    scene bg floor3
    with dissolve

    "The smallest desk on the open floor. Directly beside the office printer."

    "And here, at the printer desk, the game begins."

    # Prologue is ungraded by design — we log completion and the choices
    # that define the character (docs/TELEMETRY_AND_ADMIN_PANEL.md).
    $ record_episode_result("ep00", artifact={
        "portrait": player.portrait,
        "first_name": player.first_name,
        "meters": dict(player.meters),
        })

    $ player.chapter = "interlude_application"
    $ record_progress()

    jump interlude_application


## Next up — Interlude: The Application (scenario §6) --------------------------

label interlude_application:

    scene black
    with fade

    "{i}INTERLUDE — \"The Application.\" Coming soon.{/i}"

    return
