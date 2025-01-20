
## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xalign 0.0
    yalign 0.5
    color gui.white

style input:
    xalign 0.5
    xmaximum 1116
    color gui.white


style input:
    adjust_spacing False
