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
    show clue_8 at clue with dissolve
    "校医室的铁架单人床，套着简易被套，一条薄被放在床头，用来临时安置身体不舒服或是受伤的学生。"
    hide clue_8 with dissolve
    by eye_def o "别说，睡起来还挺舒服的。"
    by eye_close o "以后能不能翘课来这里睡觉啊。"
    me "你的想法很危险……"
    jump medical
    return

label medical_door:
    $ persistent.clue[9] = 1
    show clue_9 at clue with dissolve
    "校医室通往内侧房间的门，上面贴有几个可爱的贴纸。正中央挂着一张门牌，用圆润的字体画着“love”的字样。"
    hide clue_9 with dissolve
    by eye_wacky e "这什么鬼？好恶心。"
    me "这是啥啊？"
    by eye_def o "心理辅导室的门。"
    by eye_def e "去年开始搞的，说什么要关注学生心理健康。"
    by eye_still e "就是说你觉得状态不对的时候可以来找老师聊聊天啊巴拉巴拉的。"
    me "嗯……这不好吗？"
    by eye_close o "拜托，都是做做样子的好吧？"
    by eye_def o "你没看出这房间都是临时装的吗，本来这里是校医室的杂物间来着。"
    by eye_still o "就为了说出去面子上好看，还搞什么每个月的心灵讲座。"
    by eye_still e "根本没人在听的好吗，听了也没什么用。"
    me "……"
    "总感觉这人怨气好重……我识相地闭嘴了。"
    jump medical
    return

label medical_shelf:
    $ persistent.clue[10] = 1
    show clue_10 at clue with dissolve
    "玻璃柜上了锁，可以看到里面摆放着创可贴，棉球，纱布，感冒冲剂等物品。"
    hide clue_10
    me "好像没有温心吃的那种药，那个是药片我记得。"
    by eye_def o "嗯，这边没有。"
    by eye_def o "那个冲剂其实都没什么用，但学校里大概只能有这种东西。"
    me "说起来你喝过？"
    by eye_close e "是啊，超级苦，关键是又苦又没用。"
    by eye_still o "简直像不下雪的冬天一样耍流氓。"
    me "……"
    jump medical
    return