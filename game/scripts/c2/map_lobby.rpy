label lobby:
    window hide
    $ quick_menu = False
    if persistent.clue[11] and persistent.clue[12] and persistent.lobby_sw_flag and persistent.lobby_wf_flag and persistent.lobby_lmm_flag:
        jump c2_2_extra
    else:
        show screen lobby_screen
        pause
        jump lobby
    return


define loc_lobby = [
    {
        "name": "大厅-箭头",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "lobby_sign",
        "xpos": 1492,
        "ypos": 116
    },
    {
        "name": "大厅-日历",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "lobby_calender",
        "xpos": 1375,
        "ypos": 295
    },
    {
        "name": "姒舞",
        "idle_image": "images/map/qsw_idle.webp",
        "hover_image": "images/map/qsw_hover.webp",
        "label": "lobby_sw",
        "xpos": 503,
        "ypos": 652
    },
    {
        "name": "梁绵绵",
        "idle_image": "images/map/qlmm_idle.webp",
        "hover_image": "images/map/qlmm_hover.webp",
        "label": "lobby_lmm",
        "xpos": 1452,
        "ypos": 601
    },
    {
        "name": "卫锋",
        "idle_image": "images/map/qwf_idle.webp",
        "hover_image": "images/map/qwf_hover.webp",
        "label": "lobby_wf",
        "xpos": 28,
        "ypos": 499
    },
]

screen lobby_screen:
    modal True
    add "images/map/lobby.webp"

    # buttons for each location
    for location in loc_lobby:
        imagebutton:
            idle location["idle_image"]
            hover location["hover_image"]
            xpos location["xpos"]
            ypos location["ypos"]
            action [Hide("lobby_screen"), Jump(location["label"])]

init:
    define persistent.lobby_sw_flag = 0
    define persistent.lobby_lmm_flag = 0
    define persistent.lobby_wf_flag = 0


label lobby_sign:
    $ quick_menu = True
    $ persistent.clue[11] = 1
    show clue_11 at clue with dissolve
    "墙面上贴着指向标的图样。好几个箭头，标注了不同方向的信息。"
    "左侧是游戏室、茶水间、后花园，右侧是电影房和卫生间。从正中间往里，则是巨大的宴会厅。"
    hide clue_11 with dissolve
    by eye_def o "这里看起来好大啊，竟然有这么多房间。"
    me "从外面能看出来，这里的建筑占地面积就不小。"
    by eye_still e "啧……住在这里肯定很舒服。"
    me "这不是现在可以体验一次嘛。"
    by eye_def e "……虽然你说得有道理。"
    by eye_move o "但不知道为什么，总感觉好像更不爽了。"
    by eye_still o "都怪你。"
    me "……关我什么事啊？"
    "总感觉这人跟我说话越来越放飞自我了……"
    jump lobby
    return

label lobby_calender:
    $ quick_menu = True
    $ persistent.clue[12] = 1
    show clue_12 at clue with dissolve
    "墙上挂着日历，停留在这个月的页面。设计简约，装帧精美，配上美丽的纹样，当作装饰也毫不突兀。"
    "1月1日的地方用记号笔圈出一个大大的圆圈，旁边标有手写的笔记“生日”。"
    hide clue_12 with dissolve
    by eye_def o "哦，这个标出来的就是天玉生日是吧。"
    by eye_def o "这么隆重。"
    me "都叫了这么多人来，直接搞派对了。"
    by eye_def e "哦……也是。"
    by eye_def o "还挺新奇的。应该会吃得很好吧？"
    "白一说着，甚至吸溜了一下口水。"
    me "喂……"
    "感受到那份饥饿感，我甚至也想跟着吸溜一下。"
    me "话说你生日是什么时候？"
    "为了不让饥饿感充斥大脑，我赶紧转移注意力。"
    by eye_def o "啊？好像是……这个月吧。"
    by eye_close o "16号？还是18号？不，好像是23号……"
    by eye_move e "呃，嗯，差不多啦。"
    me "？"
    me "你自己的生日，你都记不清的吗？"
    me "等等，是这个月？？那不是已经过了吗？"
    "我大为震撼。"
    by eye_def o "对啊，所以呢？"
    me "那……你当时都没说过啊？"
    by eye_close o "我都不记得，怎么说啊。"
    me "……"
    "她说得好有道理，我竟然无法反驳……"
    me "但……呃……就是……生日不是都很重要的嘛？"
    by eye_def o "是吗？"
    "我有些弱弱地开口，但白一只是不咸不淡地回应。"
    by eye_def o "我好像没什么感觉。"
    by eye_move o "不过我知道我今年过的17岁生日。"
    me "那……你好棒棒？"
    by eye_close smile "那是。"
    "白一轻哼一声，得意地笑了。"
    "这有什么好得意的啊……"
    "虽然这么想，但莫名的，我也不自觉跟她一起笑了出来。"
    jump lobby
    return

label lobby_sw:
    $ quick_menu = True
    $ persistent.lobby_sw_flag = 1
    scene bg_lobby1
    show cg_sw10 at cg0 with dissolve
    "姒舞坐在一张小圆桌旁边的沙发上，和旁边的人有说有笑。"
    show cg_sw11 at cg0 with dissolve
    "不知为何，她身上像是装了雷达似的，白一的眼神扫过去时，她正好转过了头。"
    "四目相对。"
    show cg_sw12 at cg0 with vpunchm
    by eye_shock def "……靠！"

    scene bg_lobby1 with fade
    "只看一眼，白一立马收回目光，假装刚刚什么都没看到，什么都没发生。"
    "身体转开，脚下已经开始动作，保持着平稳的步伐往另一个方向走。"
    "只是——"
    show swimg eye_squint laugh at char_mid with moveinleft
    sw "白一~"
    "姒舞一如往常的热情，很快就朝着白一的方向走来。"
    show tophalfblk with dissolve
    by eye_move o "{size=23}我没听见我没听见……{/size}"
    "听到声音，白一也没回头，而是开始自欺欺人。"
    hide tophalfblk
    hide swimg
    show swimg eye_squint o at char_mid with vpunchm
    sw "白一！你明明就看到我了。"
    by eye_still def "……嘶。"
    "姒舞从白一的正前方冒出来，令白一不得不停住了脚步。"
    hide swimg
    show swimg o at char_mid
    sw "我还以为你不来了，人家好失望的呢。"
    by eye_still def "……"
    hide swimg
    show swimg laugh at char_mid
    sw "怎么样？我是不是很厉害，在天玉搞的活动里一样很受欢迎哦。"
    by eye_still def "……"
    "白一用余光瞥了瞥沙发那侧的人群，极其无奈地叹了口气。"
    by eye_move o "那你更不应该来找我。"
    hide swimg
    show swimg o at char_mid
    sw "欸——为什么啊？"
    hide swimg
    show swimg at char_mid
    by eye_def o "难道，你没发现其他人都很讨厌我吗？"
    by eye_def o "跟我一起，影响你社交小天才的路啊。"
    "白一耸了耸肩，把姒舞自己说的称号还给她。"
    hide swimg
    show swimg o at char_mid
    sw "啊？不是……"
    hide swimg
    show swimg at char_mid
    "姒舞看了看周围，许多隐晦打量的眼神飘过来，又因为她的转头飘走。"
    "她瘪了瘪嘴，似乎意识到不同寻常的气氛，也看出白一的不情愿。"
    by eye_def o "这样你的人气绝对比不过天玉。"
    "白一用她讨厌的人当理由，却没想到姒舞只是哼了一声。"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "我是讨厌她，但也没想着要靠你跟别人打好关系啊……那跟霸凌有什么区别？"
    by eye_def o "……也没那么严重吧。"
    by eye_close o "无所谓啊，又不是你主动害我。"
    hide swimg
    show swimg o at char_mid with vpunchs
    sw "……才不是咧！"
    by "而且其他人也没做什么，他们不喜欢我，我也不喜欢他们，都很正常的。"
    hide swimg
    show swimg eye_sad at char_mid
    sw "可是……那种眼神就很奇怪啊……"
    hide swimg
    show swimg eye_sad o at char_mid
    sw "要是只是普通的不喜欢，为什么要一起弄出那种氛围呢……这样一点也不好。"
    by eye_def def "……"
    hide swimg
    show swimg eye_sad at char_mid
    sw "{size=27}但……如果你真的不想的话……{/size}"
    "面对沉默的白一，姒舞的声音也逐渐变低。"
    by eye_still def "……"
    by eye_def o "所以你啊，干嘛非要找我？"
    hide swimg
    show swimg o at char_mid
    sw "就是想跟你说说话啊。"
    by eye_shock o "……你有那么多朋友还不够说啊？"
    "白一是真的很震惊，平淡如水的语气都有了些起伏。"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "不是，这怎么能一样呢？"
    "姒舞举起手，认真地跟白一解释。"
    hide swimg
    show swimg o at char_mid
    sw "她们又不是你的替代品，你也不是她们的替代品啊。"
    sw "每个人都不一样的。"
    hide swimg
    show swimg smile at char_mid
    sw "找你，也是因为喜欢跟你聊天的感觉啊。"
    by eye_still def "……"
    by eye_def o "你说话真的有点中二。"
    me "噗——"
    hide swimg
    show swimg eye_squint o at char_mid
    sw "哇，我那么认真，你竟然这样说？"
    by eye_move e "……只是实话实说？"
    hide swimg
    show swimg eye_blink at char_mid
    sw "哼。"
    hide swimg
    show swimg o at char_mid
    sw "反正我都在这里了，你就跟我聊聊嘛。"
    sw "我保证之后就不在这主动找你了。"
    hide swimg
    show swimg at char_mid
    by eye_def def "……哦。"
    "白一最终还是没再说拒绝的话。"
    "不过……毕竟她也没办法直接把人赶走就是了。"
    hide swimg
    show swimg o at char_mid
    sw "我跟你说哦，那边竟然有个游戏室，有超多游戏的。好羡慕~有钱真好~"
    hide swimg
    show swimg at char_mid
    by "确实……有钱真好。"
    by "租这么大的场地肯定很贵。"
    hide swimg
    show swimg o at char_mid
    sw "欸，我不是这个意思。"
    by "啊？"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "你不知道吗？天玉她全名叫云天玉哦。"
    hide swimg
    show swimg eye_blink at char_mid
    by eye_still o "呃……云天玉？"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "那你记得这地方叫什么名字嘛？"
    me "……好像叫云玉阁。"
    by eye_wacky def "……靠。"
    by eye_wacky o "有钱真好。"
    hide swimg
    show swimg eye_blink at char_mid
    "见白一似乎已经懂了自己的意思，姒舞点了点头。"
    hide swimg
    show swimg eye_squint at char_mid
    sw "对吧？竟然是真的大小姐欸，真讨厌~"
    hide swimg
    show swimg at char_mid
    "白一扶了扶额头，只觉得自己好像也有点讨厌天玉了。"
    "不过……纯粹是因为仇富之类的……倒没有姒舞那好像很复杂的爱恨情仇。"
    by eye_def o "你那么讨厌天玉，竟然不叫她全名。"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "一码归一码咯。她说她的称呼是这个，那当然要尊重。"
    hide swimg
    show swimg o at char_mid
    sw "毕竟名字很重要的啊。"
    by eye_def o "……是哦。"    
    jump lobby
    return

label lobby_lmm:
    $ quick_menu = True
    $ persistent.lobby_lmm_flag = 1
    scene bg_lobby3
    show cg_lmm00 at cg0 with dissolve
    "梁绵绵独自坐在角落，一条腿伸得很直，是个不太自然的姿势。"
    "她的眼神止不住东张西望，似乎在寻找什么。"
    scene bg_lobby with fade
    by eye_move o "说起来，之前都还没去跟她道歉……主要是总找不到机会。"
    by eye_def o "不过我竟然没有被家长找上门，也没被骂个狗血淋头。"
    by eye_def e "真神奇。"
    me "那说明她应该挺好人的吧，没跟你较真。"
    by eye_still o "所以我就是很坏人咯。啊……虽然感觉也没说错……"
    me "我可没有那个意思啊……"
    by eye_close o "行，行。你说啥是啥。"
    me "不过，现在不是正好吗，去跟她说呗？"
    by eye_def o "现在？合适吗，她好像在找人？"
    me "等她找到了更不方便吧，至少现在她还一个人坐着。"
    by eye_move e "呃……好吧，有道理。"
    "白一略微思索一下，还是朝着她走了过去。"

    scene bg_lobby3 with Dissolve(2)
    show lmmimg o at char_mid with dissolve
    lmm "……白一？"
    "听到动静，梁绵绵转过头来，眼神里是明显的惊讶。"
    hide lmmimg 
    show lmmimg at char_mid
    by eye_def o "啊，对，是我。"
    by eye_move e "就是……嗯，之前体育测试的事，对不起了。"
    "白一不太自然地卡了卡壳，才慢慢地把话说完。"
    "她很少有这么结实平和的语气，也更少会有说对不起这句话的场合。"
    "尽管听起来很干巴巴，但大概已经是很认真的状态。"
    hide lmmimg 
    show lmmimg smile at char_mid
    lmm "噢，你说那个啊，没事的。"
    by eye_def o "但我记得，你受伤很严重啊，哪里没事了。"
    by eye_def o "我应该要赔偿吧？让我赔偿。"
    me "哇，你是怎么把赔偿说得像讨债的？"
    "她的语气实在过于生硬，配上冷淡的表情和居高临下看着梁绵绵的角度，让我幻视某些不和谐的画面。"
    by eye_move def "……啧。"
    "白一轻轻磨了磨牙，左手狠狠地在腿上捏了一把。"
    me "噫！"
    hide lmmimg 
    show lmmimg o at char_mid
    lmm "你说严重……可是已经看过医生，涂过药了。"
    hide lmmimg 
    show lmmimg smile at char_mid
    lmm "而且，我是体育生啊，虽然最近比赛不多……但之前经常受伤的。"
    hide lmmimg 
    show lmmimg laugh at char_mid
    lmm "真的没事啦。"
    "白一微微拧起眉毛，似乎是不理解梁绵绵的行为。"
    by eye_def o "赔偿是我应该做的啊。"
    by eye_move e "哦，如果你是不想跟我这种人多牵扯的话，找个中间人也可以。"
    "她的语气开始变得不耐烦，但梁绵绵仍然只是笑笑，弯起了眼睛。"
    hide lmmimg 
    show lmmimg smile at char_mid
    lmm "不是在说你……腿的问题只是需要时间恢复，过段时间就好了。"
    hide lmmimg 
    show lmmimg o at char_mid
    lmm "那要不这样吧，你帮我做一件别的事情。"
    by eye_def o "做什么事？"
    hide lmmimg 
    show lmmimg smile at char_mid
    lmm "我还没想好呢。"
    by eye_still e "……那你说什么。"
    "白一有些无语地看着她，梁绵绵则是不在意地笑了笑。"
    hide lmmimg 
    show lmmimg eye_squint smile at char_mid
    lmm "没关系，还有一晚上时间呢，等我想好告诉你。"
    by eye_still def "哦……好。"

    scene bg_lobby3 with fade
    by eye_def e "人不可貌相啊。"
    me "嗯？"
    "这似乎是我也想说过的话，只是没想到会先一步从她嘴里说出来。"
    by eye_move o "没想到梁绵绵说话是那种风格？"
    by eye_def o "她那么结实，看起来就很能打，不是还说是体育生吗……"
    by eye_move o "我之前还弄伤她，结果她竟然一点都不凶。"
    by eye_close o "甚至还挺温柔……真离谱。"
    "白一叹了口气，小声地唠唠叨叨，我忍不住八卦起来。"
    me "哦，原来你喜欢温柔的呀？"
    by eye_shock o "我靠，你在说什么鬼话？"
    me "难道不是嘛，温柔的大姐姐，不好吗？"
    me "你都没骂过人家诶。"
    by eye_still o "……拜托，你是白痴吗？"
    by eye_def o "首先，她看起来好像比我小吧，哪来的姐姐。"
    by eye_still o "其次，我虽然没素质，没心没肺，冷血自私，孤僻阴暗……"
    "白一一连说了好几个形容词，才堪堪停下来。"
    by eye_still e "但不至于到人渣的程度好吗？恩将仇报？"
    me "噗……我开玩笑的……"
    "不过，虽然她这么说，但我能从白一的情绪感觉到，她比之前放松了许多。"
    by eye_def o "而且，你不要说得好像我经常骂人一样。"
    me "……难道没有吗？"
    by eye_def o "难道有吗？"
    me "……"
    "她毫不迟疑地反问我，如此自信，反倒让我怀疑起自己来……"
    jump lobby
    return

label lobby_wf:
    $ quick_menu = True
    $ persistent.lobby_wf_flag = 1
    show cg_wf00 at cg0 with dissolve
    "白一的目光扫过去的时候，正好看到班长从左侧的方向走出来。"
    "她手里拿着一个魔方，看到白一时，迅速低下头，一边摆弄着手里的魔方一边走开了。"
    scene bg_lobby with dissolve
    by eye_still def "……"
    by eye_still o "靠。"
    by eye_def o "虽然她不来烦我我很高兴，但还是有种莫名的不爽。"
    by eye_still e "总感觉她在用一种很讨厌的眼神看我。"
    me "嗯？啊……也很正常啦。"
    me "不是你先讨厌她的吗……"
    "毕竟不管再怎么说，被人直白地讨厌当然不会令人高兴。"
    by eye_still o "不是你想的那样。"
    by eye_close o "我才不在意她讨厌我，毕竟我也不喜欢她。"
    by eye_def o "但很明显她讨厌我是因为温心，这就很烦了。"
    by eye_move e "有一种替人背了黑锅的感觉。"
    me "……那也没有什么办法。你又没跟她解释。"
    by eye_close e "哼。"
    by eye_move o "好学生班长，竟然也会露出这种表情。"
    "白一不知道该用什么心情。"
    "该说是感慨呢？还是佩服呢？"
    "在温心死后，还有一个人念着她，为她的死亡生气，希望找到凶手。"
    "不是像白一这样有利可图，而是……发自真心？"
    jump lobby
    return