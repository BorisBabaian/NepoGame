## Nepo The Game — screens. Full-screen visual novel, ink and paper design code.

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
    size 48

################################################################################
## Say (dialogue) — bottom VN bar, dark namebox pill with the speaker's name
################################################################################

screen say(who, what):
    style_prefix "say"

    ## soft paper vignette so text reads over any illustration
    add "images/vignette.png"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## click-anywhere advance, plus a quiet hint
    if not renpy.get_screen("choice"):
        text "click to continue" style "continue_hint"

style window:
    xalign 0.5
    xsize 1500
    yalign 1.0
    ysize gui.textbox_height
    background Frame("gui/textbox.png", 40, 40, tile=False)
    bottom_margin 40

style namebox:
    xpos 0.5
    xanchor 0.5
    ypos gui.name_ypos
    background Frame("gui/namebox.png", 30, 12)
    padding (34, 8, 34, 12)

style say_label:
    font nepo.serif_bold
    color nepo.paper
    size gui.name_text_size
    xalign 0.5
    kerning 2

style say_dialogue:
    font nepo.serif
    color nepo.ink
    xalign 0.5
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    text_align 0.5
    line_spacing 8

style continue_hint:
    font nepo.serif
    italic True
    color nepo.ink_faint
    size 26
    xalign 0.98
    yalign 0.995

################################################################################
## Choice — ink buttons that invert to solid ink with paper text on hover
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

## Portraits are images, so they cannot colour-invert like the text buttons.
## They get a gentle zoom on hover instead.
transform portrait_hover:
    on idle, selected_idle:
        ease 0.15 zoom 1.0
    on hover, selected_hover:
        ease 0.15 zoom 1.04

## Locked chapter cards are dimmed; they still fill (grey) on hover, like the web.
transform faded:
    alpha 0.5

style choice_vbox:
    xalign 0.5
    yalign 0.42
    spacing gui.choice_spacing

style choice_button is default:
    xminimum gui.choice_button_width
    xmaximum gui.choice_button_width
    background Frame("gui/btn_idle.png", 20, 20)
    hover_background Frame("gui/btn_hover.png", 20, 20)
    padding (40, 22, 40, 26)

style choice_button_text is default:
    font nepo.serif
    color nepo.ink
    hover_color nepo.paper
    size gui.choice_button_text_size
    xalign 0.5
    text_align 0.5

################################################################################
## Input — the badge printer line
################################################################################

screen input(prompt):
    style_prefix "input"
    add "images/vignette.png"

    window:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xalign 0.5
    text_align 0.5
    size 42
    xsize 1200

style input:
    xalign 0.5
    size 54
    color nepo.ink

################################################################################
## The Assignment card (task node)
################################################################################

screen assignment_card(fromwho, objectives, stakes, accept="Understood."):
    modal True
    add "images/bg_paper.png"

    frame:
        xalign 0.5
        yalign 0.4
        xsize 1200
        background Frame("gui/frame_double.png", 24, 24)
        padding (70, 56, 70, 50)

        vbox:
            spacing 24
            text "THE ASSIGNMENT" font nepo.serif_bold color nepo.ink size 32 xalign 0.5 kerning 8
            null height 6
            for idx, obj in enumerate(objectives, start=1):
                hbox:
                    spacing 20
                    text "[idx]." font nepo.serif_bold size 40
                    text obj size 40
            if stakes:
                null height 8
                text stakes style "hand_note" xalign 0.5 text_align 0.5
            text "— [fromwho]" style "hand_note" xalign 1.0 at rotate_note

    textbutton accept:
        style "choice_button"
        xalign 0.5
        yalign 0.9
        action Return()

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
        yalign 0.06
        spacing 30
        text "The mirror has been paid to be kind.\nChoose the face it shows you.":
            xalign 0.5
            text_align 0.5
            size 46

    grid 3 2:
        xalign 0.5
        yalign 0.60
        xspacing 40
        yspacing 34
        for i in range(1, 7):
            imagebutton:
                at portrait_hover
                idle Fixed(
                    Frame("gui/frame_ink.png", 16, 16),
                    Transform("images/portraits/p%d.png" % i, xysize=(280, 374), align=(0.5, 0.5)),
                    xysize=(296, 390),
                )
                hover Fixed(
                    Frame("gui/frame_ink.png", 16, 16),
                    Transform("images/portraits/p%d.png" % i, xysize=(280, 374), align=(0.5, 0.5)),
                    xysize=(296, 390),
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
        yalign 0.38
        xsize 1200
        background Frame("gui/frame_ink.png", 24, 24)
        padding (70, 56, 70, 50)

        vbox:
            spacing 22
            text "PERFORMANCE REVIEW · STRICTLY CONFIDENTIAL":
                xalign 0.5 size 26 color nepo.ink_faint kerning 6
            text title font nepo.serif_bold size 60 xalign 0.5
            null height 10
            for label_text, value in [("Reputation", reputation), ("Composure", composure)]:
                hbox:
                    xalign 0.5
                    spacing 26
                    text label_text size 38 min_width 280 text_align 1.0 yalign 0.5
                    fixed:
                        xysize (460, 24)
                        yalign 0.5
                        add Frame("gui/btn_idle.png", 8, 8) xysize (460, 24)
                        add Solid(nepo.ink) xysize (int(460 * value / 10.0), 24) yalign 0.5
                    text "[value]/10" size 36 yalign 0.5
            null height 12
            text roast font nepo.serif_italic italic True size 40 xalign 0.5 text_align 0.5
            text concepts size 28 color nepo.ink_soft xalign 0.5 text_align 0.5

    textbutton "Back to the chapters":
        style "choice_button"
        xalign 0.5
        yalign 0.92
        action Return()

################################################################################
## Main menu, pause, confirm, notify
################################################################################

screen main_menu():
    tag menu
    add "images/menu_bg.png"

    ## Title block, upper area.
    vbox:
        xalign 0.5
        yalign 0.12
        spacing 10
        text "BUSINESS AND MANAGEMENT IN A GLOBAL CONTEXT":
            xalign 0.5 size 24 color nepo.ink_faint kerning 6
        text "Nepo The Game" font nepo.serif_bold size 120 xalign 0.5
        text "You had a surname, a platinum card and a corner office.\nYou have lost all three. Earn them back.":
            xalign 0.5 text_align 0.5 size 34 font nepo.serif_italic italic True color nepo.ink_soft

    ## Chapter select — centered cards that fill on hover, exactly like the web
    ## version. Available cards invert to solid ink with paper text; locked cards
    ## are dimmed and fill grey. A two-line label: kicker over "TIME: Title."
    vbox:
        xalign 0.5
        yalign 0.56
        spacing 14
        for ch in CHAPTERS:
            button:
                style "chapter_button"
                if ch["available"]:
                    action Start(ch["label"])
                else:
                    action Function(renpy.notify, "Locked — finish the previous chapter first.")
                    at faded
                vbox:
                    xfill True
                    spacing 4
                    text ch["kicker_line"] style "chapter_kicker"
                    text ch["title_line"] style "chapter_title"

    textbutton "Quit":
        style "choice_button"
        xalign 0.5
        yalign 0.95
        xminimum 300
        action Quit(confirm=True)

style chapter_button is default:
    xsize 1000
    xalign 0.5
    background Frame("gui/btn_idle.png", 20, 20)
    hover_background Frame("gui/btn_hover.png", 20, 20)
    padding (40, 18, 40, 22)

style chapter_kicker is default:
    font nepo.serif
    size 22
    kerning 4
    color nepo.ink_faint
    hover_color nepo.paper
    xfill True
    text_align 0.5

style chapter_title is default:
    font nepo.serif_bold
    size 40
    color nepo.ink
    hover_color nepo.paper
    xfill True
    text_align 0.5

screen pause_menu():
    tag menu
    modal True
    add "images/menu_bg.png"

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 14
        text "Paused" font nepo.serif_bold size 80 xalign 0.5
        null height 20

    vbox:
        xalign 0.5
        yalign 0.62
        spacing 22
        textbutton "Return to the scene" style "choice_button" xminimum 460 action Return()
        textbutton "Main Menu" style "choice_button" xminimum 460 action MainMenu()
        textbutton "Quit" style "choice_button" xminimum 460 action Quit(confirm=True)

## Always-available menu button (top-right), shown over every scene.
screen nepo_menu_button():
    zorder 90
    if not main_menu and not renpy.get_screen("pause_menu"):
        textbutton "☰ Menu":
            xalign 0.985
            yalign 0.02
            action ShowMenu("pause_menu")
            text_style "menu_button_text"
            background None

style menu_button_text:
    font nepo.serif
    size 32
    color nepo.ink_faint
    hover_color nepo.ink

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add "#141414aa"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        background Frame("gui/frame_ink.png", 24, 24)
        padding (70, 56, 70, 50)
        vbox:
            spacing 40
            text message xalign 0.5 text_align 0.5 size 42
            hbox:
                xalign 0.5
                spacing 60
                textbutton "Yes" style "choice_button" xminimum 260 action yes_action
                textbutton "No" style "choice_button" xminimum 260 action no_action

## Handwritten margin note (meter changes), shown via renpy.notify
screen notify(message):
    zorder 100
    text message style "hand_note" xalign 0.88 yalign 0.10 at notify_appear
    timer 3.0 action Hide("notify")

transform notify_appear:
    alpha 0.0
    rotate -3
    linear 0.25 alpha 1.0
