label detail_label:
    show screen detail_screen
    pause
    jump detail_label
    return


screen detail_screen:
    default category = "dict"
    add "gui/ev/ev-bg.png":
        xalign 0.5
        yalign 0.5

    button:
        background "gui/ev/category-btn.png"
        hover_background "gui/ev/category-btn-hover.png"
        selected_background "gui/ev/category-btn-hover.png"
        xysize(150,90)
        pos(490,86)
        text _("词典"):
            align (0.5,0.5)
            color gui.black
            font gui.interface_text_font
            size 35
        action SetScreenVariable("category","dict")

    button:
        background "gui/ev/category-btn.png"
        hover_background "gui/ev/category-btn-hover.png"
        selected_background "gui/ev/category-btn-hover.png"
        xysize(150,90)
        pos(490,204)
        text _("线索"):
            align (0.5,0.5)
            color gui.black
            font gui.interface_text_font
            size 35
        action SetScreenVariable("category","clue")

    button:
        background "gui/ev/category-btn.png"
        hover_background "gui/ev/category-btn-hover.png"
        selected_background "gui/ev/category-btn-hover.png"
        text _("人物"):
            align (0.5,0.5)
            color gui.black
            font gui.interface_text_font
            size 35
        xysize(150,90)
        pos(490,322)
        action SetScreenVariable("category","char")


    imagebutton:
        idle "gui/ev/close-btn.png"
        hover "gui/ev/close-btn-hover.png"
        pos(505,884)
        action Return()


    if category == "dict":
        frame:
            background "black"
            align (0.5,0.5)
            xysize (460,920)
    elif category == "clue":
        frame:
            background "black"
            align (0.5,0.5)
            xysize (460,920)
    else:
        frame:
            background "black"
            align (0.5,0.5)
            xysize (460,920)