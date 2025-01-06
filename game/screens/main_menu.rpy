
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background = HBox(
    Solid("#292835", xsize=350),
    Solid("#21212d")
)

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main"
    add "main-title"
    vbox:
        style_prefix "main_navigation"
        xpos 125
        yalign 0.5
        yoffset 150
        spacing 10

        textbutton _("开始游戏") action Start()

        textbutton _("读取进度") action ShowMenu("load")

        textbutton _("游戏设置") action ShowMenu("preferences")

        textbutton _("关于游戏") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("游戏帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出游戏") action Quit(confirm=not main_menu)


style main_navigation_button_text:
    color "#fff"
    hover_color "#ad973f"
    size 48
    # xalign 0
    