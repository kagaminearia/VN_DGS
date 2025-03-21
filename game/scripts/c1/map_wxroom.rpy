label wxroom:
    window hide
    $ quick_menu = False
    show screen wxroom_screen
    pause
    jump wxroom
    return


define loc_wxroom = [
    {
        "name": "客厅-餐桌",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_table",
        "xpos": 1231,
        "ypos": 696
    },
    {
        "name": "客厅-床铺",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_bed",
        "xpos": 1820,
        "ypos": 602
    },
    {
        "name": "灶台-燃气灶",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_stove",
        "xpos": 32,
        "ypos": 715
    },
    {
        "name": "灶台-垃圾桶",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_garbage",
        "xpos": 286,
        "ypos": 836
    },
    {
        "name": "洗手间-窗户",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_window",
        "xpos": 657,
        "ypos": 500
    },
    {
        "name": "储物柜-药盒",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_medicine",
        "xpos": 1368,
        "ypos": 566
    },
    {
        "name": "门口-备忘录",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_note",
        "xpos": 336,
        "ypos": 289
    },
    {
        "name": "白一",
        "idle_image": "images/map/qby_idle.webp",
        "hover_image": "images/map/qby_hover.webp",
        "label": "wxroom_by",
        "xpos": 1275,
        "ypos": 20
    },
]


screen wxroom_screen:
    modal True
    add "images/map/wxroom.webp"

    # buttons for each location
    for location in loc_wxroom:
        imagebutton:
            idle location["idle_image"]
            hover location["hover_image"]
            xpos location["xpos"]
            ypos location["ypos"]
            action [Hide("wxroom_screen"), Jump(location["label"])]


label wxroom_table:
    $ quick_menu = True
    $ persistent.clue[1] = 1
    show clue_1 at clue with dissolve
    "抽屉里有一双木质筷子，一双用过后洗干净的一次性筷子，上面刻有“湘味”的字迹。"
    hide clue_1 with dissolve
    me "一次性筷子用第二次的话还能叫一次性筷子吗？"
    by eye_wacky e "哈？你要用谁会管你？等等，你在说这双吗？"
    me "嗯，这是用过之后洗干净的，被收起来了。"
    by eye_def o "不是吧，这你都能看出来？"
    me "是啊……"
    by eye_def o "没想到你还有点用嘛。啊，竟然是这家店。"
    me "什么？"
    by eye_def o "是一家我吃不起的餐厅。你看，他们连一次性筷子都要定制。"
    by eye_move e "啧，有钱真好。"
    me "好沉重的话题……"
    jump wxroom
    return

label wxroom_bed:
    $ quick_menu = True
    $ persistent.clue[2] = 1
    show clue_2 at clue with dissolve
    "被子已经被掀开，堆在一边。床单很旧，有不少补丁，但很干净。枕头上有两个人躺过的痕迹。"
    hide clue_2 with dissolve
    by eye_wacky e "我之前就跟她躺在这吗……"
    me "看起来是的。"
    by eye_wacky e "难以置信……我竟然会跟不熟的人睡一起……要死啊，到底发生了什么……"
    me "噗嗤……谁知道呢。"
    by eye_wacky def "啧……你别忘了你现在用的是我的身体。"
    "白一轻嗤一声，意有所指，撩起左手的衣袖，佯装要在小臂上用力。"
    me "……"
    "我不想再继续说话了，总觉得她真的能做出这种伤敌八百自损一千的事情。"
    jump wxroom
    return

label wxroom_stove:
    $ quick_menu = True
    $ persistent.clue[3] = 1
    show clue_3 at clue with dissolve
    "有长时间开过火的痕迹，燃气灶老旧，燃气喷嘴处有异物堵塞。"
    hide clue_3 with dissolve
    me "这个灶台，之前好像开了很久……旁边都烧到变形了。"
    me "喷嘴好像有点塞住了，这样会燃烧不完全，产生一氧化碳的吧。"
    by eye_def o "啊？这样的话，这应该是，嗯……她死亡的直接原因。"
    by eye_def o "不过，怎么会堵塞的？"
    me "看起来像太久没用，积了很多灰，没清理过，团结成块了。"
    by eye_def def "真奇怪……"
    jump wxroom
    return

label wxroom_garbage:
    $ quick_menu = True
    $ persistent.clue[4] = 1
    show clue_4 at clue with dissolve
    "空空如也，没有袋子"
    hide clue_4 with dissolve
    by eye_def o "收拾得好干净啊。"
    me "嗯。"
    by eye_def o "那这里好像没什么好看的。"
    me "对。"
    by eye_still e "……你还能再敷衍一点吗？"
    jump wxroom
    return

label wxroom_window:
    $ quick_menu = True
    $ persistent.clue[5] = 1
    show clue_5 at clue with dissolve
    "被百叶窗盖住的窗户关闭，上了锁"
    hide clue_5 with dissolve
    me "嗯？百叶窗后面是锁死的。"
    by eye_def o "难怪感觉这里好闷，完全不透气啊。"
    me "那快点出去吧。"
    jump wxroom
    return

label wxroom_medicine:
    $ quick_menu = True
    $ persistent.clue[6] = 1
    show clue_6 at clue with dissolve
    "透明药盒里有两瓶一样的感冒药，其中一瓶空了。"
    hide clue_6 with dissolve
    by eye_def o "啊，这个我知道，味道超级苦的感冒药。"
    me "是吗？她吃了很多，有一瓶空了。"
    by eye_def o "哇，了不起。都怪这鬼天气，实在是太冷了。"
    jump wxroom
    return

label wxroom_note:
    $ quick_menu = True
    $ persistent.clue[7] = 1
    show clue_7 at clue with dissolve
    "6:30起床，7:00到校，17:00放学，XXXX（涂黑），20:00扔垃圾（周末整理房间），23:30睡觉"
    hide clue_7 with dissolve
    by eye_def o "我去，好吓人的日程表。"
    me "你不是吗？同个学校的学生应该都差不多吧。"
    by eye_def o "我可没这么认真学习，受不了。"
    me "……"
    jump wxroom
    return

label wxroom_by:
    $ quick_menu = True
    if persistent.clue[1] and persistent.clue[2] and persistent.clue[3] and persistent.clue[4] and persistent.clue[5] and persistent.clue[6] and persistent.clue[7]:
        scene bg_wxroom with fade
        $ quick_menu = True
        by eye_def o "好像看完了，你觉得是什么情况？"
        me "嗯……"
        jump c1_1_extra
    else:
        by eye_still e "怎么了，继续看啊？"
        me "啊，没，就是觉得你看得还挺认真……"
        by eye_wacky o "呵呵，我都要变成杀人凶手了，能不认真吗？"
        me "……"
        jump wxroom
    return