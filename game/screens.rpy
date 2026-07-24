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
## Buttons — one reusable button with a smooth cross-fade hover.
## The idle (paper) and hover (solid-ink) looks are two stacked layers that
## cross-fade over 0.14s, so the fill and the text colour ease together instead
## of snapping — matching the web version's `transition: 0.14s ease`.
################################################################################

## caption may be one or two lines (use {size=..} tags for a two-line card).
screen xbutton(caption, act, width=720, dim=False):
    button:
        action act
        at dimmed(0.5 if dim else 1.0)
        fixed:
            fit_first True
            frame:
                background Frame("gui/btn_idle.png", 22, 22)
                xsize width
                padding (30, 15, 30, 17)
                at hv_hide
                text caption color nepo.ink size 30 xfill True text_align 0.5 line_spacing 2
            frame:
                background Frame("gui/btn_hover.png", 22, 22)
                xsize width
                padding (30, 15, 30, 17)
                at hv_show
                text caption color nepo.paper size 30 xfill True text_align 0.5 line_spacing 2

## Cross-fade pair: idle layer at rest, hover layer on hover. These respond to
## the enclosing button's focus because the transform is its child.
transform hv_hide:
    alpha 1.0
    on hover, selected_hover:
        ease 0.14 alpha 0.0
    on idle, selected_idle:
        ease 0.14 alpha 1.0

transform hv_show:
    alpha 0.0
    on hover, selected_hover:
        ease 0.14 alpha 1.0
    on idle, selected_idle:
        ease 0.14 alpha 0.0

## Portraits are images, so they cannot colour-invert; a gentle zoom instead.
transform portrait_hover:
    on idle, selected_idle:
        ease 0.15 zoom 1.0
    on hover, selected_hover:
        ease 0.15 zoom 1.04

## Locked chapter cards are dimmed to 50%; they still fill (grey) on hover.
transform dimmed(a=1.0):
    alpha a

################################################################################
## Choice — in-scene dialogue options.
################################################################################

screen choice(items):
    style_prefix "choice"
    vbox:
        style "choice_vbox"
        for i in items:
            use xbutton(i.caption, i.action, 860)

style choice_vbox:
    xalign 0.5
    yalign 0.42
    spacing 18

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

    vbox:
        xalign 0.5
        yalign 0.9
        use xbutton(accept, Return(), 600)

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
                        add Solid("#e6e4dc") xysize (460, 24)
                        add Solid(nepo.ink) xysize (int(460 * value / 10.0), 24) yalign 0.5
                    text "[value]/10" size 36 yalign 0.5
            null height 12
            text roast font nepo.serif_italic italic True size 40 xalign 0.5 text_align 0.5
            text concepts size 28 color nepo.ink_soft xalign 0.5 text_align 0.5

    vbox:
        xalign 0.5
        yalign 0.92
        use xbutton("Back to the chapters", Return(), 560)

################################################################################
## Main menu, pause, confirm, notify
################################################################################

screen main_menu():
    tag menu
    ## Scale the art to fill the 16:10 canvas (source may be any size), so there
    ## are never black edges if the uploaded image is not exactly 1920x1200.
    add Transform("images/menu_bg.png", fit="cover", xysize=(1920, 1200))
    ## Soft paper scrim so the title and cards never blend into busy artwork.
    add Transform("images/menu_scrim.png", fit="cover", xysize=(1920, 1200))

    ## Title block, upper area.
    vbox:
        xalign 0.5
        yalign 0.12
        spacing 10
        text "BUSINESS AND MANAGEMENT IN A GLOBAL CONTEXT":
            xalign 0.5 size 21 color nepo.ink_faint kerning 7
        text "Nepo The Game" font nepo.serif_bold size 92 xalign 0.5
        text "You had a surname, a platinum card and a corner office.\nYou have lost all three. Earn them back.":
            xalign 0.5 text_align 0.5 size 29 font nepo.serif_italic italic True color nepo.ink_soft

    ## Chapter select — cards that cross-fade to solid ink on hover, exactly like
    ## the web. Locked cards are dimmed and fill grey; a click explains why.
    vbox:
        xalign 0.5
        yalign 0.56
        spacing 16
        for ch in CHAPTERS:
            if ch["available"]:
                use xbutton(ch["menu_caption"], Start(ch["label"]), 760)
            else:
                use xbutton(ch["menu_caption"], Function(renpy.notify, "Locked — finish the previous chapter first."), 760, True)

    vbox:
        xalign 0.5
        yalign 0.95
        use xbutton("Quit", Quit(confirm=True), 300)

screen pause_menu():
    tag menu
    modal True
    add Transform("images/menu_bg.png", fit="cover", xysize=(1920, 1200))
    add Transform("images/menu_scrim.png", fit="cover", xysize=(1920, 1200))

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 14
        text "Paused" font nepo.serif_bold size 80 xalign 0.5
        null height 20

    vbox:
        xalign 0.5
        yalign 0.62
        spacing 18
        use xbutton("Return to the scene", Return(), 480)
        use xbutton("Main Menu", MainMenu(), 480)
        use xbutton("Quit", Quit(confirm=True), 480)

## Always-available menu button (top-right), shown over every scene.
screen nepo_menu_button():
    zorder 90
    if not main_menu and not renpy.get_screen("pause_menu"):
        textbutton "☰ Menu":
            xalign 0.985
            yalign 0.02
            action ShowMenu("pause_menu")
            text_style "menu_button_text"
            ## Paper chip so the control never blends into the scene art.
            background Frame("gui/btn_idle.png", 22, 22)
            padding (26, 10, 26, 12)

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
                spacing 40
                use xbutton("Yes", yes_action, 240)
                use xbutton("No", no_action, 240)

## Handwritten margin note (meter changes), shown via renpy.notify
screen notify(message):
    zorder 100
    text message style "hand_note" xalign 0.88 yalign 0.10 at notify_appear
    timer 3.0 action Hide("notify")

transform notify_appear:
    alpha 0.0
    rotate -3
    linear 0.25 alpha 1.0
