## Nepo The Game — screens. Compact set, styled to the ink and paper design code.

################################################################################
## Core styles
################################################################################

style default:
    font nepo.serif
    color nepo.ink
    size gui.text_size

style button_text:
    font nepo.serif
    color nepo.ink_faint
    hover_color nepo.ink
    size gui.interface_text_size

style hand_note:
    font nepo.hand
    color nepo.ink_soft
    size 44

################################################################################
## Say (dialogue) — white ink framed box, centered speaker name above the line
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

style window:
    xalign 0.5
    xsize 1400
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Frame("gui/textbox.png", 24, 24, tile=False)
    bottom_margin 40

style namebox:
    xpos 0.5
    xanchor 0.5
    ypos gui.name_ypos
    background Frame("gui/btn_hover.png", 12, 12)
    padding (28, 6, 28, 8)

style say_label:
    font nepo.serif_bold
    color nepo.paper
    size gui.name_text_size
    xalign 0.5

style say_dialogue:
    xalign 0.5
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    text_align 0.5
    line_spacing 6

################################################################################
## Choice — ink bordered buttons that invert on hover
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox:
    xalign 0.5
    ypos 340
    spacing 22

style choice_button:
    xminimum gui.choice_button_width
    xmaximum gui.choice_button_width
    background Frame("gui/btn_idle.png", 12, 12)
    hover_background Frame("gui/btn_hover.png", 12, 12)
    padding (36, 20, 36, 22)

style choice_button_text:
    font nepo.serif
    color nepo.ink
    hover_color nepo.paper
    size 36
    xalign 0.5
    text_align 0.5

################################################################################
## Input — the badge printer line
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xalign 0.5
            ypos gui.dialogue_ypos
            spacing 24
            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xalign 0.5
    text_align 0.5
    size 38

style input:
    xalign 0.5
    size 46
    color nepo.ink
    caret_blink True

################################################################################
## Ink panel — the comic frame with offset shadow (InkFrame from the web mock)
################################################################################

transform panel_pos:
    xalign 0.5
    yalign 0.28

screen panel(path="images/panels/placeholder.png"):
    zorder 5
    add At(
        Fixed(
            Transform(Frame("gui/btn_hover.png", 12, 12), xoffset=10, yoffset=12),
            Frame("gui/frame_ink.png", 12, 12),
            Transform(path, xysize=(1132, 850), align=(0.5, 0.5)),
            xysize=(1160, 870),
        ),
        panel_pos,
    )

################################################################################
## The Assignment card (task node)
################################################################################

screen assignment_card(fromwho, objectives, stakes, accept="Understood."):
    modal True
    add "images/bg_paper.png"

    frame:
        xalign 0.5
        yalign 0.42
        xsize 1100
        background Frame("gui/frame_double.png", 20, 20)
        padding (60, 50, 60, 44)

        vbox:
            spacing 22
            text "THE ASSIGNMENT" font nepo.serif_bold color nepo.ink size 30 xalign 0.5 kerning 6
            null height 4
            for idx, obj in enumerate(objectives, start=1):
                hbox:
                    spacing 18
                    text "[idx]." font nepo.serif_bold size 36
                    text obj size 36
            if stakes:
                null height 6
                text stakes style "hand_note" xalign 0.5 text_align 0.5
            text "— [fromwho]" style "hand_note" xalign 1.0 at rotate_note

    textbutton accept:
        style "choice_button"
        xalign 0.5
        yalign 0.92
        action Return()
        text_style "choice_button_text"

transform rotate_note:
    rotate -2

################################################################################
## The Mirror — portrait selection (character creation)
################################################################################

screen mirror_select():
    modal True
    add "images/bg_paper.png"

    vbox:
        xalign 0.5
        yalign 0.08
        spacing 30
        text "The mirror has been paid to be kind.\nChoose the face it shows you.":
            xalign 0.5
            text_align 0.5
            size 44

    grid 3 2:
        xalign 0.5
        yalign 0.62
        spacing 34
        for i in range(1, 7):
            imagebutton:
                idle Fixed(
                    Frame("gui/frame_ink.png", 12, 12),
                    Transform("images/portraits/p%d.png" % i, xysize=(268, 358), align=(0.5, 0.5)),
                    xysize=(280, 370),
                )
                hover Fixed(
                    Transform(Frame("gui/btn_hover.png", 12, 12), xoffset=6, yoffset=8),
                    Frame("gui/frame_ink.png", 12, 12),
                    Transform("images/portraits/p%d.png" % i, xysize=(268, 358), align=(0.5, 0.5)),
                    xysize=(280, 370),
                )
                action [SetVariable("portrait_id", i), Return(i)]

################################################################################
## Verdict — the performance review card
################################################################################

screen verdict_card(title, reputation, composure, roast, concepts):
    modal True
    add "images/bg_paper.png"

    frame:
        xalign 0.5
        yalign 0.4
        xsize 1100
        background Frame("gui/frame_ink.png", 20, 20)
        padding (60, 50, 60, 44)

        vbox:
            spacing 20
            text "PERFORMANCE REVIEW · STRICTLY CONFIDENTIAL":
                xalign 0.5 size 24 color nepo.ink_faint kerning 5
            text title font nepo.serif_bold size 52 xalign 0.5
            null height 8
            for label_text, value in [("Reputation", reputation), ("Composure", composure)]:
                hbox:
                    xalign 0.5
                    spacing 24
                    text label_text size 34 min_width 260 text_align 1.0
                    fixed:
                        xysize (420, 22)
                        yalign 0.5
                        add Frame("gui/btn_idle.png", 8, 8) xysize (420, 22)
                        add Solid(nepo.ink) xysize (int(420 * value / 10.0), 22)
                    text "[value]/10" size 32
            null height 10
            text roast italic True size 36 xalign 0.5 text_align 0.5
            text concepts size 26 color nepo.ink_soft xalign 0.5 text_align 0.5

    textbutton "Back to the chapters":
        style "choice_button"
        xalign 0.5
        yalign 0.93
        action Return()
        text_style "choice_button_text"

################################################################################
## Main menu, pause, confirm, notify
################################################################################

screen main_menu():
    tag menu
    add "images/bg_paper.png"

    vbox:
        xalign 0.5
        yalign 0.4
        spacing 16
        text "BUSINESS & MANAGEMENT · IN A GLOBAL CONTEXT":
            xalign 0.5 size 24 color nepo.ink_faint kerning 6
        text "Nepo The Game" font nepo.serif_bold size 120 xalign 0.5
        text "You had a surname, a platinum card and a corner office.\nYou have lost all three. Earn them back.":
            xalign 0.5 text_align 0.5 size 34 italic True color nepo.ink_soft

    vbox:
        xalign 0.5
        yalign 0.82
        spacing 20
        textbutton "Begin the Prologue" style "choice_button" text_style "choice_button_text" action Start()
        textbutton "Quit" style "choice_button" text_style "choice_button_text" action Quit(confirm=True)

screen pause_menu():
    tag menu
    modal True
    add "#fcfbf7ee"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 22
        textbutton "Return" style "choice_button" text_style "choice_button_text" action Return()
        textbutton "Main Menu" style "choice_button" text_style "choice_button_text" action MainMenu()
        textbutton "Quit" style "choice_button" text_style "choice_button_text" action Quit(confirm=True)

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add "#141414aa"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        background Frame("gui/frame_ink.png", 20, 20)
        padding (60, 50, 60, 44)
        vbox:
            spacing 34
            text message xalign 0.5 text_align 0.5 size 38
            hbox:
                xalign 0.5
                spacing 60
                textbutton "Yes" style "choice_button" xminimum 240 text_style "choice_button_text" action yes_action
                textbutton "No" style "choice_button" xminimum 240 text_style "choice_button_text" action no_action

## Handwritten margin note (meter changes) — shown via renpy.notify
screen notify(message):
    zorder 100
    text message style "hand_note" xalign 0.86 yalign 0.12 at notify_appear

    timer 3.0 action Hide("notify")

transform notify_appear:
    alpha 0
    rotate -2
    linear 0.25 alpha 1.0
