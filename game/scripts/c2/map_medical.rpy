label medical:
    window hide
    $ quick_menu = False
    if persistent.clue[8] and persistent.clue[9] and persistent.clue[10]:
        jump c2_1_extra
    else:
        show screen medical_screen
        pause
        jump medical
    return


define loc_medical = [
    {
        "name": "校医室-床",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "medical_bed",
        "xpos": 1635,
        "ypos": 540
    },
    {
        "name": "校医室-内门",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "medical_door",
        "xpos": 434,
        "ypos": 460
    },
    {
        "name": "校医室-柜子",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "medical_shelf",
        "xpos": 920,
        "ypos": 258
    },
]

screen medical_screen:
    modal True
    add "images/map/medical.webp"

    # buttons for each location
    for location in loc_medical:
        imagebutton:
            idle location["idle_image"]
            hover location["hover_image"]
            xpos location["xpos"]
            ypos location["ypos"]
            action [Hide("medical_screen"), Jump(location["label"])]


label medical_bed:
    $ persistent.clue[8] = 1
    "套着简易被套，盖着薄被的铁架单人床。"
    by "别说，睡起来还挺舒服的。"
    by "以后能不能翘课来这里睡觉啊。"
    me "你的想法很危险……"
    jump medical
    return

label medical_door:
    $ persistent.clue[9] = 1
    "通往内侧房间的门，上面贴有几个可爱的贴纸。正中央挂着一张门牌，用圆润的字体画着“love”的字样。"
    by "什么鬼？好恶心。"
    me "这是啥啊？"
    by "心理辅导室的门。"
    by "去年开始搞的，说什么要关注学生心理健康。"
    by "就是说你难过的时候可以来找老师聊聊天啊巴拉巴拉的。"
    me "嗯……这不好吗？"
    by "拜托，都是做做样子的好吧？"
    by "这房间都是临时装的，本来是校医室的杂物间来着。"
    by "就为了说出去面子上好看，还搞什么每个月的心灵讲座。"
    by "根本没人在听的好吗，听了也没什么用。"
    me "……"
    "总感觉这人怨气好重……我识相地闭嘴了。"
    jump medical
    return

label medical_shelf:
    $ persistent.clue[10] = 1
    "玻璃柜上了锁，可以看到里面摆放着创可贴，棉球，纱布，感冒冲剂等物品。"
    me "好像没有温心吃的那种药，那个是药片我记得。"
    by "嗯，这边没有。"
    by "那个冲剂其实都没什么用，但学校里大概只能有这种东西。"
    me "说起来你喝过？"
    by "是啊，超级苦，关键是又苦又没用。"
    by "简直像不下雪的冬天一样耍流氓。"
    me "……"
    jump medical
    return