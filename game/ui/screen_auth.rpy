# ui/screen_auth.rpy — registration / sign-in STUB.
#
# Future (TECHNICAL_PLAN.md §7): this becomes a blocking `auth_gate` form
# called from `label before_main_menu` (see screens.rpy, main_menu comment).
# It will store persistent.auth_token / persistent.account_id via core/net/.
# For now it only reserves the diegetic entry point.

screen auth_stub():
    modal True
    zorder 150

    add "#14141466"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 50

        vbox:
            xalign 0.5
            spacing 30
            xmaximum 720

            text _("EMPLOYEE VERIFICATION") style "auth_kicker" xalign 0.5

            text _("Sign-in arrives together with the online build. For now, the firm takes you at your word — a decision it will come to regret."):
                style "auth_body"
                xalign 0.5
                text_align 0.5

            textbutton _("VERY WELL") action Hide("auth_stub") xalign 0.5

style auth_kicker is text:
    size 22
    kerning 6
    color gui.ink_faint

style auth_body is text:
    size 28
    italic True
    color gui.ink_soft
