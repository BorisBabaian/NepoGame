# ui/screen_margin_note.rpy — handwritten meter annotation
#
# styles.css .effect-note: hand font, ink-soft, rotated ~2 degrees.
# Shown automatically by shift() in core/meters.rpy — story code never
# calls this screen directly.

transform margin_note_appear:
    alpha 0.0
    xoffset 40
    rotate -2.5
    parallel:
        linear 0.35 alpha 1.0
    parallel:
        easeout 0.45 xoffset 0
    pause 2.4
    linear 0.7 alpha 0.0


screen margin_note(lines):
    zorder 90
    style_prefix "margin_note"

    vbox at margin_note_appear:
        xalign 0.955
        yalign 0.26
        spacing 8

        for line in lines:
            text line

    timer 3.6 action Hide("margin_note")


style margin_note_text:
    font gui.hand
    size 40
    color gui.ink_soft
    outlines [(3, gui.paper, 0, 0)]
