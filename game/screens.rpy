################################################################################
## screens.rpy — all game screens, "The Jaded Euro" ink style (styles.css)
################################################################################

################################################################################
## Button motion — "The Jaded Euro"
################################################################################
## Ink-on-paper wants restraint: nothing bounces, nothing glows. Buttons lift
## slightly off the page on hover and press back down on click, echoing
## .choice-btn:active { transform: translate(1px,1px); box-shadow: none }
## and .portrait-cell:hover { transform: translateY(-2px) } from styles.css.
##
## Button states send these events to any transform attached with `at`.

transform ink_lift:
    ## Framed buttons: the paper lifts, then sits back down when pressed.
    on idle, insensitive, selected_idle:
        easeout 0.18 yoffset 0 xoffset 0
    on hover, selected_hover:
        easein 0.18 yoffset -4 xoffset -2

transform ink_nudge:
    ## Plain text buttons: a small step to the right, like a pen finding a line.
    on idle, insensitive, selected_idle:
        easeout 0.18 xoffset 0
    on hover, selected_hover:
        easein 0.18 xoffset 7

transform ink_settle:
    ## Menu items appear with a faint settle, so the page never snaps.
    on show:
        alpha 0.0 yoffset 6
        parallel:
            linear 0.22 alpha 1.0
        parallel:
            easeout 0.28 yoffset 0


################################################################################
## Base styles
################################################################################

style default:
    font gui.serif
    size gui.text_size
    color gui.ink

style input:
    color gui.ink
    xalign 0.5

style button:
    background None
    xpadding 30
    ypadding 12

style button_text:
    font gui.serif
    size gui.interface_size
    color gui.ink_soft
    hover_color gui.ink
    selected_color gui.ink
    insensitive_color gui.ink_faint

style label_text:
    font gui.serif
    size gui.label_size
    bold True
    color gui.ink

style frame:
    background gui.panel
    xpadding 30
    ypadding 24

style vscrollbar:
    xsize 20
    base_bar gui.panel_paper
    thumb gui.panel_hover
    unscrollable "hide"


################################################################################
## Say — .narration / .dialogue: centered, serif, speaker in tracked caps
################################################################################

screen say(who, what):

    window:
        id "window"

        vbox:
            xfill True
            yalign 0.5
            spacing 14

            if who is not None:
                text who id "who" style "say_label"

            text what id "what" style "say_dialogue"

## Textbox: white ink-frame panel across the bottom.
## The generous horizontal padding is what keeps the first and last letters
## clear of the drawn ink border — without it the frame eats them.
style window:
    xfill True
    yalign 1.0
    ysize 320
    background gui.panel
    padding (150, 46)

style say_label:
    font gui.serif
    size gui.name_size
    bold True
    kerning 4
    color gui.ink
    xalign 0.5

style say_dialogue:
    font gui.serif
    size gui.text_size
    color gui.ink
    xalign 0.5
    xmaximum 1450
    text_align 0.5
    line_spacing 8


################################################################################
## Input — .ink-input: centered typed text
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xfill True
            yalign 0.5
            spacing 26

            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xalign 0.5
    text_align 0.5
    size 30
    italic True
    color gui.ink_soft


################################################################################
## Choice — .choice-btn: ink border, hover inverts to ink/paper
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption:
                action i.action
                at ink_lift

style choice_vbox is vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 18

style choice_button is button:
    xsize 900
    background gui.panel
    hover_background gui.panel_hover
    xpadding 36
    ypadding 18

style choice_button_text is button_text:
    size 28
    xalign 0.5
    text_align 0.5
    color gui.ink
    hover_color gui.paper


################################################################################
## Quick menu — .continue-hint: small tracked caps, faint ink
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -10
            spacing 44

            textbutton _("BACK") action Rollback() at ink_nudge
            textbutton _("HISTORY") action ShowMenu('history') at ink_nudge
            textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True) at ink_nudge
            textbutton _("AUTO") action Preference("auto-forward", "toggle") at ink_nudge
            textbutton _("SAVE") action ShowMenu('save') at ink_nudge
            textbutton _("Q.SAVE") action QuickSave() at ink_nudge
            textbutton _("Q.LOAD") action QuickLoad() at ink_nudge
            textbutton _("SETTINGS") action ShowMenu('preferences') at ink_nudge
            textbutton _("QUIT") action Show("exit_prompt") at ink_nudge

default quick_menu = True

init python:
    config.overlay_screens.append("quick_menu")

style quick_button is button:
    xpadding 8
    ypadding 4

style quick_button_text is button_text:
    size 19
    kerning 3
    color gui.ink_faint
    hover_color gui.ink


################################################################################
## Main menu — .cover: kicker / big title / italic subtitle / begin button
################################################################################

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add gui.paper

    ## ------------------------------------------------------------------
    ## FUTURE MANDATORY REGISTRATION (TECHNICAL_PLAN.md §7).
    ## When the backend exists, the gate goes into `label before_main_menu`
    ## (Ren'Py runs it before showing this screen):
    ##
    ##   label before_main_menu:
    ##       if persistent.auth_token is None:
    ##           call screen auth_gate    # blocking sign-in / register form
    ##       return
    ##
    ## Until then, a non-blocking stub button reserves the entry point.
    ## ------------------------------------------------------------------

    textbutton _("SIGN IN"):
        style "main_menu_signin"
        xalign 0.97
        ypos 36
        action Show("auth_stub")
        at ink_nudge

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 10

        text _("MCQUINSEY & COMPANY PRESENT") style "main_menu_kicker" xalign 0.5
        text _("BMGC") style "main_menu_title" xalign 0.5
        text _("A season in consulting, for a man\nwho has never once opened Excel."):
            style "main_menu_subtitle"
            xalign 0.5
            text_align 0.5

        null height 46

        textbutton _("BEGIN MONDAY"):
            action Start()
            style "main_menu_primary"
            xalign 0.5
            at ink_lift

        null height 18

        textbutton _("LOAD A SAVED WEEK"):
            action ShowMenu("load")
            style "main_menu_secondary"
            xalign 0.5
            at ink_nudge

        textbutton _("SETTINGS"):
            action ShowMenu("preferences")
            style "main_menu_secondary"
            xalign 0.5
            at ink_nudge

    ## Quit sits apart at the foot of the page, with a confirmation.
    ## Show() is used rather than Quit(confirm=True) because Ren'Py ignores
    ## the automatic quit confirmation while in the main menu — this way the
    ## prompt is ours and always appears, in our own ink-framed card.
    if renpy.variant("pc"):
        textbutton _("QUIT"):
            style "main_menu_secondary"
            xalign 0.5
            yalign 0.88
            at ink_nudge
            action Show("confirm",
                message=_("Leave the firm for today?"),
                yes_action=Quit(confirm=False),
                no_action=Hide("confirm"))

    text _("episode zero — “How the Money Ends”"):
        style "main_menu_footnote"
        xalign 0.5
        yalign 0.97

style main_menu_kicker is text:
    size 24
    kerning 8
    color gui.ink_faint

style main_menu_title is text:
    size 150
    bold True
    color gui.ink

style main_menu_subtitle is text:
    size 32
    italic True
    color gui.ink_soft

style main_menu_primary is button:
    background gui.panel
    hover_background gui.panel_hover
    xminimum 460
    xpadding 44
    ypadding 20

style main_menu_primary_text is button_text:
    size 30
    kerning 4
    xalign 0.5
    color gui.ink
    hover_color gui.paper

style main_menu_secondary is button

style main_menu_secondary_text is button_text:
    size 23
    kerning 4
    color gui.ink_soft
    hover_color gui.ink

style main_menu_signin is button

style main_menu_signin_text is button_text:
    size 20
    kerning 4
    color gui.ink_faint
    hover_color gui.ink

style main_menu_footnote is text:
    font gui.hand
    size 30
    color gui.ink_faint


################################################################################
## Game menu shell — paper page, nav column on the left
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0, nav="game"):
    style_prefix "game_menu"

    if main_menu:
        add gui.paper
    else:
        add "#fcfbf7f2"

    hbox:
        xpos 80
        ypos 140

        frame:
            style "game_menu_navigation_frame"

            ## Settings gets its own column of sections instead of the
            ## global navigation.
            if nav == "preferences":
                use preferences_navigation
            else:
                use navigation

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":
                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    vbox:
                        spacing 24
                        transclude
            else:
                transclude

    text title style "game_menu_label" xpos 90 ypos 48

    ## Settings carries Return inside its own section column, so the shared
    ## one would be a duplicate.
    if nav != "preferences":
        textbutton _("RETURN"):
            style "game_menu_return"
            xpos 90
            yalign 0.96
            action Return()
            at ink_nudge

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_navigation_frame is frame:
    background None
    xsize 380
    ysize 800

style game_menu_content_frame is frame:
    background None
    xsize 1320
    ysize 800

style game_menu_label is text:
    size 46
    bold True
    kerning 6
    color gui.ink

style game_menu_return is button

style game_menu_return_text is button_text:
    size 24
    kerning 4


screen navigation():

    vbox:
        style_prefix "navigation"
        yalign 0.5
        spacing 18

        if main_menu:
            textbutton _("Start") action Start() at ink_nudge
        else:
            textbutton _("History") action ShowMenu("history") at ink_nudge
            textbutton _("Save") action ShowMenu("save") at ink_nudge

        textbutton _("Load") action ShowMenu("load") at ink_nudge
        textbutton _("Settings") action ShowMenu("preferences") at ink_nudge

        if not main_menu:
            ## Leaving the story writes an autosave first, so a player who
            ## walks away mid-episode never loses the walk.
            textbutton _("Main Menu"):
                action [Function(renpy.force_autosave), MainMenu()]
                at ink_nudge

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu) at ink_nudge

style navigation_button is button:
    xpadding 8

style navigation_button_text is button_text:
    size 30
    kerning 2


################################################################################
## Save / Load — ink-framed slots
################################################################################

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

init python:

    def DiscardSave(slot):
        """Always ask before deleting a save.

        FileDelete's own `confirm` is skipped while in the main menu, and the
        load screen is reachable from there — so the prompt is raised
        explicitly instead, using our own ink-framed confirm card.
        """
        return Show("confirm",
                    message=_("Discard this save? It does not come back."),
                    yes_action=[Hide("confirm"), FileDelete(slot, confirm=False)],
                    no_action=Hide("confirm"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid 3 2:
                style_prefix "slot"
                xalign 0.5
                yalign 0.55
                spacing 24

                for i in range(6):
                    $ slot = i + 1

                    ## The slot and its delete affordance are siblings inside
                    ## a fixed, not nested buttons — Ren'Py does not handle a
                    ## button inside a button reliably.
                    fixed:
                        xysize (420, 320)

                        button:
                            style "slot_button"
                            xysize (420, 320)
                            action FileAction(slot)
                            at ink_lift

                            has vbox
                            add FileScreenshot(slot) xalign 0.5
                            text FileTime(slot, format=_("{#file_time}%d %B %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action DiscardSave(slot)

                        ## Only occupied slots can be discarded.
                        if FileLoadable(slot):
                            textbutton "×":
                                style "slot_delete"
                                align (1.0, 0.0)
                                action DiscardSave(slot)
                                at ink_lift

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing 14

                textbutton _("<") action FilePagePrevious() at ink_nudge
                textbutton _("{#auto_page}A") action FilePage("auto") at ink_nudge
                textbutton _("{#quick_page}Q") action FilePage("quick") at ink_nudge

                for page in range(1, 8):
                    textbutton "[page]" action FilePage(page) at ink_nudge

                textbutton _(">") action FilePageNext() at ink_nudge

style page_label is button:
    xpadding 20
    ypadding 6

style page_label_text is text:
    size 30
    bold True
    kerning 2
    color gui.ink
    xalign 0.5

style slot_button is button:
    background gui.panel
    xpadding 14
    ypadding 12

style slot_time_text is text:
    size 21
    xalign 0.5
    color gui.ink_soft

style slot_name_text is text:
    size 19
    xalign 0.5
    color gui.ink_faint

## Discard a save: a small ink cross in the corner of an occupied slot.
style slot_delete is button:
    background gui.panel_paper
    hover_background gui.panel_hover
    xysize (46, 46)

style slot_delete_text is button_text:
    size 26
    xalign 0.5
    yalign 0.5
    color gui.ink_faint
    hover_color gui.paper

style page_button is button:
    xpadding 12
    ypadding 6

style page_button_text is button_text:
    size 24
    kerning 2


################################################################################
## Preferences
################################################################################

## Which settings section is open. A store variable rather than a screen
## variable, so the section column and the content pane can both see it.
default prefs_tab = "gameplay"


screen preferences_navigation():

    vbox:
        style_prefix "navigation"
        yalign 0.5
        spacing 18

        textbutton _("Gameplay"):
            action SetVariable("prefs_tab", "gameplay")
            selected prefs_tab == "gameplay"
            at ink_nudge

        textbutton _("Screen"):
            action SetVariable("prefs_tab", "screen")
            selected prefs_tab == "screen"
            at ink_nudge

        textbutton _("Audio"):
            action SetVariable("prefs_tab", "audio")
            selected prefs_tab == "audio"
            at ink_nudge

        null height 28

        textbutton _("Return") action Return() at ink_nudge


screen preferences():
    tag menu

    use game_menu(_("Settings"), scroll="viewport", nav="preferences"):

        vbox:
            spacing 40

            ## -- Gameplay ------------------------------------------------
            if prefs_tab == "gameplay":

                vbox:
                    style_prefix "slider"
                    spacing 22

                    label _("Text speed")
                    bar value Preference("text speed")

                    label _("Auto-forward time")
                    bar value Preference("auto-forward time")

                null height 10

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen text") action Preference("skip", "toggle")
                    textbutton _("After choices") action Preference("after choices", "toggle")

            ## -- Screen --------------------------------------------------
            elif prefs_tab == "screen":

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                    null height 10

                vbox:
                    style_prefix "check"
                    label _("Presentation")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            ## -- Audio ---------------------------------------------------
            else:

                vbox:
                    style_prefix "slider"
                    spacing 22

                    if config.has_music:
                        label _("Music volume")
                        bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound volume")
                        bar value Preference("sound volume")

                if config.has_music or config.has_sound:
                    null height 14
                    vbox:
                        style_prefix "check"
                        textbutton _("Mute all"):
                            style "mute_all_button"
                            action Preference("all mute", "toggle")

style radio_label is label

style radio_label_text is label_text:
    size 30

style check_label is radio_label
style check_label_text is radio_label_text
style slider_label is radio_label
style slider_label_text is radio_label_text

style radio_button is button:
    xpadding 8
    ypadding 4

style radio_button_text is button_text:
    size 26
    color gui.ink_faint
    hover_color gui.ink_soft
    selected_color gui.ink

style check_button is radio_button
style check_button_text is radio_button_text

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style slider_slider is slider:
    xsize 700
    ysize 34
    base_bar gui.panel_paper
    thumb "gui/ink/thumb.png"


################################################################################
## History
################################################################################

screen history():
    tag menu
    predict False

    use game_menu(_("History"), scroll="viewport", yinitial=1.0):

        style_prefix "history"

        for h in _history_list:
            vbox:
                spacing 4

                if h.who:
                    text h.who style "history_name_text"

                text h.what style "history_text"

        if not _history_list:
            text _("The dialogue history is empty.") style "history_empty_text"

style history_name_text is text:
    size 23
    bold True
    kerning 3
    color gui.ink

style history_text is text:
    size 27
    color gui.ink_soft

style history_empty_text is text:
    size 27
    italic True
    color gui.ink_faint


################################################################################
## Confirm — modal ink card
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add "#14141466"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 50

        vbox:
            xalign 0.5
            spacing 44

            text _(message):
                style "confirm_prompt"
                xalign 0.5
                text_align 0.5

            hbox:
                xalign 0.5
                spacing 120

                textbutton _("Yes") action yes_action at ink_lift
                textbutton _("No") action no_action at ink_lift

    key "game_menu" action no_action

style confirm_prompt is text:
    size 32

style confirm_button is button:
    background gui.panel
    hover_background gui.panel_hover
    xminimum 220
    xpadding 34
    ypadding 14

style confirm_button_text is button_text:
    size 30
    bold True
    kerning 3
    xalign 0.5
    color gui.ink
    hover_color gui.paper


################################################################################
## Notify — .effect-note: handwritten annotation
################################################################################

transform notify_appear:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        style "notify_frame"
        text "[message!tq]"

    timer 3.25 action Hide('notify')

style notify_frame is frame:
    xpos 60
    ypos 40
    background gui.panel_paper
    xpadding 26
    ypadding 10

style notify_text is text:
    font gui.hand
    size 30
    color gui.ink_soft


################################################################################
## Skip indicator
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        style "skip_frame"
        text _("SKIPPING >>>") style "skip_text"

style skip_frame is frame:
    xpos 60
    ypos 40
    background gui.panel_paper
    xpadding 24
    ypadding 10

style skip_text is text:
    size 21
    kerning 4
    color gui.ink_soft
