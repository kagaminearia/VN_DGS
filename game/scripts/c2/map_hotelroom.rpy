label hotelroom:
    window hide
    $ quick_menu = False
    if persistent.clue[14] and persistent.clue[15] and persistent.clue[16] and persistent.clue[17] and persistent.clue[18]:
        jump c2_3_extra1
    else:
        show screen hotelroom_screen
        pause
        jump hotelroom1
    return

define loc_hotelroom = [
    {
        "name": "客房-蜡烛",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "room_candle",
        "xpos": 1127,
        "ypos": 655
    },
    {
        "name": "客房-杯子",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "room_cup",
        "xpos": 1355,
        "ypos": 567
    },
    {
        "name": "客房-内门",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "room_door",
        "xpos": 1525,
        "ypos": 266
    },
    {
        "name": "客房-地面",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "room_ground",
        "xpos": 17,
        "ypos": 673
    },
    {
        "name": "客房-平面图",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "room_wall",
        "xpos": 314,
        "ypos": 230
    },
]

screen hotelroom_screen:
    modal True
    add "images/map/hotelroom.webp"

    # buttons for each location
    for location in loc_hotelroom:
        imagebutton:
            idle location["idle_image"]
            hover location["hover_image"]
            xpos location["xpos"]
            ypos location["ypos"]
            action [Hide("hotelroom_screen"), Jump(location["label"])]


label room_candle:
    $ quick_menu = True
    $ persistent.clue[14] = 1
    show clue_14 at clue with dissolve
    "香薰蜡烛被放在床头柜上，已经烧完了。"
    "透过留给灯芯的洞，能够看到容器里剩下的浅浅一层像是碎屑的残留物。"
    hide clue_14
    jump hotelroom
    return

label room_cup:
    $ quick_menu = True
    $ persistent.clue[15] = 1
    show clue_15 at clue with dissolve
    "在茶几边缘，里面有干涸的水渍和浸透的茶包。"
    hide clue_15
    jump hotelroom
    return

label room_door:
    $ quick_menu = True
    $ persistent.clue[16] = 1
    show clue_16 at clue with dissolve
    "连接202房间，可以把两间房变成大号套房的两扇门。轻轻掩着，都没有上锁。"
    hide clue_16
    jump hotelroom
    return

label room_ground:
    $ quick_menu = True
    $ persistent.clue[17] = 1
    show clue_17 at clue with dissolve
    "洗手间地面有一个长条形的，类似椭圆的痕迹，不太清晰。"
    hide clue_17
    jump hotelroom
    return

label room_wall:
    $ quick_menu = True
    $ persistent.clue[18] = 1
    show clue_18 at clue with dissolve
    "楼平面图，标注了各个房间的位置以及消防电梯的位置"
    hide clue_18
    jump hotelroom
    return