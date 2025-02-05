# The game starts here.

label start:
    # "{font=fonts/BlueSecretText.ttf}test{/font}"
    # testing
    call c1_1
    "test: c1_1 end"
    $ quick_menu = False
    window hide
    scene black with Dissolve(1)
    pause
    $ renpy.notify("通知栏在这里")

    return
