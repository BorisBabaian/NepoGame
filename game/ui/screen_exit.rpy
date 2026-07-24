# ui/screen_exit.rpy — leaving the game from inside the story.
#
# Raised by the QUIT button in the quick menu. Offers the two ways out —
# back to the main menu, or all the way to the desktop — plus a way to
# change one's mind. Both exits write an autosave first, so walking away
# mid-episode never costs the player the episode.

screen exit_prompt():

    modal True
    zorder 200
    style_prefix "exit"

    add "#14141466"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 70
        ypadding 56

        vbox:
            xalign 0.5
            spacing 32

            text _("LEAVING THE OFFICE"):
                style "exit_kicker"
                xalign 0.5

            text _("Your progress is saved either way.\nThe firm, regrettably, will still be here."):
                style "exit_body"
                xalign 0.5
                text_align 0.5

            null height 4

            hbox:
                xalign 0.5
                spacing 28

                textbutton _("MAIN MENU"):
                    action [Function(renpy.force_autosave), MainMenu(confirm=False)]
                    at ink_lift

                if renpy.variant("pc"):
                    textbutton _("DESKTOP"):
                        action [Function(renpy.force_autosave), Quit(confirm=False)]
                        at ink_lift

            textbutton _("stay a little longer"):
                style "exit_cancel"
                xalign 0.5
                action Hide("exit_prompt")
                at ink_nudge

    ## Escape backs out of the prompt rather than stacking another menu.
    key "game_menu" action Hide("exit_prompt")


style exit_frame is frame:
    background gui.panel

style exit_kicker is text:
    size 22
    kerning 6
    color gui.ink_faint

style exit_body is text:
    size 28
    italic True
    color gui.ink_soft

style exit_button is button:
    background gui.panel_paper
    hover_background gui.panel_hover
    xminimum 320
    xpadding 36
    ypadding 18

style exit_button_text is button_text:
    size 28
    bold True
    kerning 3
    xalign 0.5
    color gui.ink
    hover_color gui.paper

style exit_cancel is button

style exit_cancel_text is button_text:
    font gui.hand
    size 32
    color gui.ink_faint
    hover_color gui.ink_soft
