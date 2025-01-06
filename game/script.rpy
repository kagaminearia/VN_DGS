# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bai = Character("白一")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show byimg

    # These display lines of dialogue.

    bai "【站酷仓耳渔阳体】是仓耳字库在2020新冠疫情期间为造福社会奉上的一份礼物，也是站酷冠名的首款拥有家族字体的公益字库。字形结合宋、黑二体的结构特点，将部分笔画转折处做圆角处理，方圆结合，厚重又不失灵动。"
    bai "{size=20}【站酷仓耳渔阳体】是仓耳字库在2020新冠疫情期间为造福社会奉上的一份礼物，也是站酷冠名的首款拥有家族字体的公益字库。{/size}"

    $ renpy.notify("通知栏在这里")

    menu:
        "选择"
        "这是第一个选项":
            pass
        "这是第二个选项":
            pass
    # This ends the game.

    return
