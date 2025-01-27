screen detail_screen:
    add "#0000001a"
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


    if category == "clue":
        frame:
            add "#fff"
            style_prefix "detail"
            align (0.5,0.5)
            xysize (520,920)
            vpgrid:
                cols 2
                spacing 30
                draggable True
                mousewheel True

                scrollbars "vertical"

                # Since we have scrollbars, we have to position the side, rather
                # than the vpgrid proper.
                side_xalign 0.8

                for i in range(len(clueList)):
                    button:
                        add "evlocked":
                            align (0.5,0.0)
                            yoffset 20
                        background "gui/ev/ev-btn-idle.png"
                        hover_background "gui/ev/ev-btn-hover.png"
                        text "[clueList[i][0]]":
                            yoffset -20
                            align (0.5,1.0)
                            color gui.black
                            font gui.detailtitle_font
                            size 20
                        xysize(215,250)
                        action Return("i")
    

    elif category == "dict":
        frame:
            add "#fff"
            style_prefix "detail"
            align (0.5,0.5)
            xysize (520,920)
            if len(persistent.dictList) == 0:
                vbox:
                    text "目录为空":
                        align (0.5,0.5)
                        font gui.detailtitle_font
                        color gui.black
            else:
                viewport:
                    ysize 920
                    xalign 0.5
                    yalign 0.5
                    style_prefix 'detail'
                    mousewheel True draggable True pagekeys True
                    scrollbars "vertical"
                    yinitial 1.0

                    has vbox
                    spacing 30
                    for i in range(len(persistent.dictList)):
                        vbox:
                            text "[persistent.dictList[i][0]]":
                                font gui.detailtitle_font
                                color gui.black
                            text "[persistent.dictList[i][1]]":
                                font gui.detail_font
                                color gui.black
                                size 23
                
    else:
        frame:
            background "black"
            align (0.5,0.5)
            xysize (460,920)



# screen clue_screen(index):



style detail_vscrollbar:
    xsize 25
    base_bar Frame("gui/scrollbar/ev-vsc-bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/ev-vsc-thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'
    xoffset 150


# images for this screen
image evlocked = "gui/ev/ev-locked.png"