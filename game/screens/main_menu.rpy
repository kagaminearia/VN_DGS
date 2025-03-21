
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    add "images/main/main.png"
    add "images/main/main-title.png"
    vbox:
        style_prefix "main_navigation"
        xpos 175
        yalign 0.85
        spacing 10
        
        textbutton _("开始游戏") action Start()
        textbutton _("读取进度") action ShowMenu("load")
        textbutton _("游戏设置") action ShowMenu("preferences")
        textbutton _("关于游戏") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("游戏帮助"):
                action ShowMenu("help")

        if renpy.variant("pc"):
            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出游戏") action Quit(confirm=not main_menu)
        
        textbutton _("测试") action ShowMenu("testchapter")

style main_navigation_button_text:
    color gui.white
    hover_color gui.white
    size 50
    hover_underline True
    selected_underline True
    selected_hover_underline True
    
screen testchapter():
    tag menu
    key "mouseup_3" action Return()
    add "#000000ff"
    hbox:
        xalign 0.3
        yalign 0.5
        spacing 110
        vbox:
            # xalign 0.25
            # yalign 0.25
            spacing 10
            textbutton ("c0") action Start("c0")
            textbutton ("c1-1") action Start("c1_1")
            textbutton ("c1-2") action Start("c1_2")
            textbutton ("c1-3") action Start("c1_3")
            textbutton ("c1-4") action Start("c1_4")
            textbutton ("c1-5") action Start("c1_5")
            textbutton ("c2-1") action Start("c2_1")
            textbutton ("c2-2") action Start("c2_2")
            textbutton ("c2-3") action Start("c2_3")
            textbutton ("c2-4") action Start("c2_4")
            textbutton ("c2-5") action Start("c2_5")
        vbox:
            textbutton ("temp") action Start("c2_4_choice1")