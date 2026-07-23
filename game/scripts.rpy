## Nepo The Game — Prologue. Full-screen visual novel.
## Backgrounds fill the screen; the dialogue bar and namebox overlay the bottom.
## Content follows docs/scenario.tex. Mechanics come later.

## ── Characters (the name appears in the namebox) ─────────────────────────────
define narrator = Character(None)
define nestor = Character("Nestor")
define father = Character("Father")
define vergeau = Character("Mme Vergeau")
define you = Character("[player_name]")

default portrait_id = 1
default player_name = "Analyst"
default reputation = 5
default composure = 5

## ── Backgrounds ──────────────────────────────────────────────────────────────
## Each resolves to images/bg/<name>.png (full 1920x1080). Until the art exists,
## a labelled paper placeholder is shown so the scene still plays.
init python:
    import os
    def bg(name, label):
        path = "images/bg/%s.png" % name
        if renpy.loadable(path):
            renpy.image("bg " + name, path)
        else:
            renpy.image("bg " + name, Fixed(
                "images/bg_paper.png",
                Text("{i}" + label + "{/i}", size=48, color="#8a8781",
                     xalign=0.5, yalign=0.4, text_align=0.5, xsize=1300,
                     substitute=False),
                xysize=(1920, 1200),
            ))

    for n, lbl in [
        ("wake", "bedroom, silk sheets, decorative alarm at 10:47"),
        ("mirror", "gilded bathroom mirror"),
        ("hall", "breakfast hall, table for forty set for two"),
        ("card", "Visa Platinum locked in a velvet box"),
        ("monday", "office tower forecourt, convertible across two spaces"),
        ("office", "corner office, floor 67, a plant taller than a career"),
        ("coffee", "the coffee point, two espresso cups"),
        ("badge", "a badge printer, waking with bureaucratic enthusiasm"),
        ("descent", "the glass lift descending 67 to 3"),
    ]:
        bg(n, lbl)

    def meter(name, delta):
        v = max(0, min(10, getattr(store, name) + delta))
        setattr(store, name, v)
        sign = "+" if delta > 0 else "−"
        renpy.notify(name.capitalize() + " " + sign + str(abs(delta)))


## ── Chapter registry ─────────────────────────────────────────────────────────
## The main menu builds its chapter list from this. Add entries as episodes are
## written; set available False for ones not yet built (shown locked).
## Chapter list. kicker_line / title_line are the exact strings the menu prints,
## precomputed here so the screen stays simple. Locked chapters get "· LOCKED".
init python:
    def _chapter(kicker, time, title, label, available):
        return {
            "label": label,
            "available": available,
            "kicker_line": kicker.upper() + ("" if available else " · LOCKED"),
            "title_line": "%s: %s." % (time, title),
        }

define CHAPTERS = [
    _chapter("Prologue",                    "10:47 AM", "How the Money Ends", "ch_prologue",    True),
    _chapter("Interlude",                   "2:15 PM",  "The Application",     "ch_application", False),
    _chapter("Module 1 · Episode 1",        "9:00 AM",  "Day One",             "ch_dayone",      False),
    _chapter("Module 1 · Finale (preview)", "7:58 PM",  "The Gala",            "ch_gala",        False),
]

label start:
    jump ch_prologue

label ch_prologue:

    scene bg wake with fade
    "Silk sheets. A canopy bed the size of a branch office. A bedroom with better square footage than most startups."
    "The alarm clock has been set to 'decorative' since 2019."

    scene bg mirror with dissolve
    "The bathroom. Heated marble. Eleven kinds of soap, none ever opened. And the mirror. Gilded, generous, and extremely well paid."

    call screen mirror_select
    "Yes. That one. Obviously."

    nestor "Your father requests your presence at breakfast. He used the word 'requests' loosely."

    scene bg hall with dissolve
    "11:15 AM. The breakfast hall. A table for forty, set for two."
    "At the far end, behind a financial newspaper: Father. The front page shows a yacht, a harbour, and a crane lifting something that used to be expensive."

    father "Do you know what a margin is?"

    menu:
        "\"A type of butter?\"":
            $ meter("composure", -1)
        "\"...something in Excel?\"":
            pass
        "Say nothing. The newspaper says enough.":
            $ meter("composure", +1)

    father "A margin is what your yacht did to the harbour master's boat in Portofino. The fine has six digits. I have paid it. That was the last time."

    scene bg card with dissolve
    "Nestor appears with a small velvet box, held like a coffin at a state funeral. The Visa Platinum is placed inside. The lock clicks with terrible finality."

    father "You start Monday. Vice Head of Special Projects at McQuinsey and Company."
    you "...what happened to the previous Vice Head?"
    father "There has never been one. Kristof owed me a favour. No allowance. No accounts. No calls to my office. You will live on a salary. Look the word up."

    "The newspaper rises again like a drawbridge. The audience is over."
    "The weekend passes through the five stages of grief. By Sunday night, acceptance arrives wearing Nestor's face, laying out a suit like armor for a war somebody else has chosen."

    scene bg monday with dissolve
    "8:58 AM, Monday. The convertible is parked across two spaces. One of them belongs to the CFO."

    scene bg office with dissolve
    "Floor 67. Corner office. Two windows. A plant taller than your career."
    "You open Excel. A full screen of cells stares back. You stare. The cells win. The laptop closes. A dating app opens."

    vergeau "Oh. You are the new one! Come. Coffee. It is not optional here, like breathing."

    scene bg coffee with dissolve
    "10:30 AM. The coffee point. Small talk, it turns out, is the one market where you hold a monopoly."

    vergeau "So. Our client's margin is collapsing in the DACH region. Your read?"

    menu:
        "\"We should leverage synergies to disrupt the paradigm. End-to-end.\"":
            $ meter("reputation", -2)
        "\"Have they tried... marketing?\"":
            $ meter("reputation", -2)
        "\"Margins are down 4.7 percent. I feel this strongly.\" (You invented the number just now.)":
            $ meter("reputation", -2)

    vergeau "How does a person who cannot read a P and L become Vice Head of Special..."
    "Her eyes drop to your badge. P. VAULMONT. A pause the length of a fiscal quarter."
    vergeau "Ah. Now I understand."
    vergeau "Under my leadership, no nepotism. Out of respect for your father, you are not fired. Out of respect for the firm, you are no longer Vice Head of anything."

    scene bg badge with dissolve
    "She takes the badge with two fingers, the way one removes evidence. A badge printer wakes up with bureaucratic enthusiasm."

    $ player_name = renpy.input("\"First name,\" she says, not looking up.", default="", length=16).strip() or "Analyst"

    "The printer produces your new identity with insulting speed:"
    "{b}[player_name] — JUNIOR ANALYST (PROBATIONARY){/b}"

    vergeau "Here, you have no surname. You will earn one back. Or you will not."

    scene bg descent with dissolve
    "The lift descends from 67 to 3 in silence. The smallest desk on the open floor waits beside the printer."
    "And so, at the printer desk, the game begins."

    call screen assignment_card(
        "Mme Vergeau",
        [
            "Survive three conversations without creating a diplomatic incident.",
            "Say nothing quotable. Nothing.",
            "Make exactly one important person remember your name favourably.",
        ],
        "Success is invisible. Failure will be discussed at Monday's partner meeting.",
        "Understood. Invisible. Memorable. Both.",
    )

    call screen verdict_card(
        "Day Zero, Reviewed",
        reputation,
        composure,
        "You lost a surname, a floor and a Visa Platinum. You kept the convertible. Priorities intact.",
        "Course concepts ahead: drivers of globalisation · political risk · economic systems\ncultural dimensions · ethics and CSR · instruments of trade policy",
    )

    return

## Placeholder labels for chapters not yet written. Kept so the menu can link
## them once available; currently they are locked in the chapter list.
label ch_application:
    "The Application — coming soon."
    return

label ch_dayone:
    "Day One — coming soon."
    return

label ch_gala:
    "The Gala — coming soon."
    return
