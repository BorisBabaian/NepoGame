# ui/screen_mirror.rpy — diegetic character creation: the flattering mirror.
#
# Called with `call screen mirror_portraits` from the prologue.
# Returns a portrait id ("p1".."p4") via _return.
# Ink style: paper overlay, white ink-framed cells, hover inverts and lifts
# (.portrait-grid / .portrait-cell from styles.css).
#
# When real ink portraits exist, replace the text cells with imagebuttons;
# the Return values stay the same.

screen mirror_portraits():

    modal True

    add "#fcfbf7f2"

    vbox:
        align (0.5, 0.5)
        spacing 44

        text _("The mirror has been paid to be kind.\nChoose the face it shows you."):
            style "mirror_prompt"
            xalign 0.5
            text_align 0.5

        hbox:
            spacing 28
            xalign 0.5

            for i in range(1, 5):
                button:
                    style "mirror_cell"
                    xysize (280, 370)
                    action Return("p{}".format(i))
                    at ink_lift

                    text _("ink portrait\n№ [i]"):
                        style "mirror_cell_text"
                        align (0.5, 0.5)
                        text_align 0.5

style mirror_prompt is text:
    size 36
    italic True
    color gui.ink

style mirror_cell is button:
    background gui.panel
    hover_background gui.panel_hover

style mirror_cell_text is text:
    size 26
    color gui.ink_faint
    hover_color gui.paper
