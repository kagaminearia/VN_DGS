init:
    define persistent.c2_4_ty = 0
    define persistent.c2_4_xl = 0
    define persistent.c2_4_wf = 0
    define persistent.c2_4_sw = 0
    define persistent.c2_4_cx = 0

label c2_4:
    scene bg_hotelroom with Fade(0.5,1,0.5)
    "根据之前得到的信息，除去其他人后，西顺选择先仔细询问在可能作案时间里去过茶水间方向的几人。"
    "这几个人是目前嫌疑最高的，仔细调查必不可少。"
    "再次询问，一是为了得到可能的更多细节，二是通过重复问话来观察他们有没有说谎。"
    jump c2_4_menu1
    return

label c2_4_menu1:
    hide rec
    if persistent.c2_4_ty == 1 and persistent.c2_4_xl == 1 and persistent.c2_4_wf == 1 and persistent.c2_4_sw == 1 and persistent.c2_4_cx == 1:
        jump c2_4_extra1
    show black with dissolve
    pause 0.4
    hide black with dissolve
    menu:
        "天玉":
            show rec with dissolve
            show tyimg coat smile at char_mid with dissolve
            ty "姐姐你好，嗯嗯，是还要问什么吗？"
            hide tyimg
            show tyimg coat o at char_mid
            ty "去茶水间的时候吗？这个我之前其实说过了呀。当时是人已经来齐了，所以我就打算在吃饭之前最后去检查一遍那些盒子。"
            hide tyimg
            show tyimg coat smile at char_mid
            ty "因为是要发给大家的嘛，如果弄错就不好了。"
            hide tyimg
            show tyimg coat o at char_mid
            ty "对，那些盒子是谁都可以打开的。"
            hide tyimg
            show tyimg coat eye_sad o at char_mid
            ty "是我疏忽了，没有想到……我只是在旁边写了纸条，说不要碰。"
            hide tyimg
            show tyimg coat eye_sad at char_mid
            ty "但要是有人还是动了的话，我也不知道……"
            hide tyimg
            show tyimg coat o at char_mid
            ty "蜡烛吗？是可以单独拿出来。"
            hide tyimg
            show tyimg coat eye_still o at char_mid
            ty "但是为了固定，那个盒子里是加了卡扣的，拿出来就会被破坏。"
            ty "我当时检查的时候，并没有看到有坏掉的。"
            hide tyimg
            show tyimg coat at char_mid
            ty "唔，别的我没注意，抱歉……"
            hide tyimg
            show tyimg coat o at char_mid
            ty "我只能记得，那时检查的时候，就是为了确认里面的东西嘛。"
            ty "所以能确定东西都在，至少数量都是对的，没有缺少内容，也没有坏掉的情况。"
            hide tyimg
            show tyimg coat eye_sad smile at char_mid
            ty "嗯，对，好，如果能帮到忙就太好了……"
            hide tyimg
            show tyimg coat eye_close o at char_mid
            ty "我也很希望能快点找出结果，辛苦你们了……谢谢。"
            hide tyimg with dissolve
            jump c2_4_menu1
        "小蓝":
            show rec with dissolve
            show xlimg o at char_mid with dissolve
            xl "啊……！您，您好……"
            xl "我，我真的没有对东西动过手脚！"
            hide xlimg
            show xlimg at char_mid
            xl "我怎么会动要送人的东西呢……这个，这个是不可能做的。"
            hide xlimg
            show xlimg o at char_mid
            xl "是的，昨天一天都是我在负责这里的杂事……"
            xl "巡逻就是检查一遍一楼整体的情况……主要是看有没有人跑到不该去的地方，或者走错了之类的。"
            hide xlimg
            show xlimg at char_mid
            xl "没，没有要求的时候，我就会在大厅等候。"
            hide xlimg
            show xlimg o at char_mid
            xl "对，对不起……！我不知道……"
            xl "因为来的同学很多……我实在没法对上每个人的长相。"
            hide xlimg
            show xlimg at char_mid
            xl "不过，不过我能确定的是……在第二天凌晨回房之前，所有人都是在一楼没错……"
            hide xlimg
            show xlimg o at char_mid
            xl "是的，那些助眠礼盒都是我送到每个房间的……但我真的没有打开过！"
            hide xlimg
            show xlimg at char_mid
            xl "就，就是，去每个房间敲门，把东西给他们……"
            hide xlimg
            show xlimg o at char_mid
            xl "那应该，应该是在十二点二十左右……就是他们刚回房没多久。"
            xl "因因因为是……再晚的话就可能有人睡了，就太打扰了……所以十二点半之前肯定送完了。"
            hide xlimg
            show xlimg at char_mid
            xl "是的，我做的就只有这些……真的没有擅自主张什么的……"
            hide xlimg with dissolve
            jump c2_4_menu1
        "卫锋":
            show rec with dissolve
            show wfimg coat eye_sad purse at char_mid with dissolve
            wf "您好……我是卫锋。"
            hide wfimg
            show wfimg coat eye_sad o at char_mid
            wf "好的，我……明白。"
            hide wfimg
            show wfimg coat o at char_mid
            wf "嗯，昨天的事，我记得的。"
            hide wfimg
            show wfimg coat eye_still o at char_mid
            wf "一开始……我是提前到的，因为这样比较好……啊，对，提前了一点，然后等待过程中去了一下洗手间。"
            hide wfimg
            show wfimg coat o at char_mid
            wf "之后就是，看电影的时候。嗯，大概就是十点多吧……"
            hide wfimg
            show wfimg coat purse at char_mid
            wf "中途去了一次茶水间，因为想给可乐加一点冰……就去拿了。"
            hide wfimg
            show wfimg coat eye_sad o at char_mid
            wf "嗯……就是，因为我不习惯晚睡，所以当时有点困，就想喝点冰的。"
            hide wfimg
            show wfimg coat o at char_mid
            wf "啊？不知道有没有被看到……"
            hide wfimg
            show wfimg coat at char_mid
            wf "我是自己去的。"
            hide wfimg
            show wfimg coat eye_sad purse at char_mid
            wf "因为大家都在看电影，当然不好麻烦其他人，这样。"
            hide wfimg
            show wfimg coat eye_still o at char_mid
            wf "其他的，我也没有注意……我加完冰之后就回去了。"
            hide wfimg
            show wfimg coat o at char_mid
            wf "晚上？我住219，没有出去过。"
            hide wfimg
            show wfimg coat eye_close at char_mid
            wf "嗯，很快，就是这些了。"
            hide wfimg with dissolve
            jump c2_4_menu1
        "姒舞":
            show rec with dissolve
            show swimg coat at char_mid with dissolve
            sw "欸——那个……你好你好。"
            hide swimg
            show swimg coat eye_blink o at char_mid
            sw "啥？我昨晚的行动？不是说过了嘛？"
            hide swimg
            show swimg coat o at char_mid
            sw "噢，具体的两个时候……去游戏室和茶水间的时候？"
            hide swimg
            show swimg coat eye_squint o at char_mid
            sw "我那一晚上好像就去了这两个地方啊！唔，对不起，我太激动了……"
            hide swimg
            show swimg coat at char_mid
            sw "七点多的时候我刚到，就想着到处逛逛嘛……"
            hide swimg
            show swimg coat o at char_mid
            sw "然后就看到游戏室了，当然会想着看一下里面啊——这样子。"
            sw "我到的比较早，所以没找到熟悉的人跟我一起去。"
            hide swimg
            show swimg coat at char_mid
            sw "就是到那里看了一下下，没别的了。"
            hide swimg
            show swimg coat o at char_mid
            sw "去茶水间就是晚上嘛，当时是去拿点零食，想着打游戏的时候可以一边吃一边打。"
            hide swimg
            show swimg coat eye_blink o at char_mid
            sw "这个当时游戏室有好几个人呀，大家都知道的。"
            hide swimg
            show swimg coat at char_mids
            sw "嗯嗯，就是这样……"
            hide swimg
            show swimg coat o at char_mid
            sw "我的房间是217，我是一直在打游戏嘛，是最晚一批回去的，回去之后就睡了，其他不知道。"
            hide swimg
            show swimg coat eye_sad o at char_mid
            sw "其他人？我没注意过哎……感觉没什么特别的呀……"
            hide swimg
            jump c2_4_menu1
        "岑宣":
            show rec with dissolve
            show cximg coat eye_sad at char_mid with dissolve
            cx "嗯，好……昨天吗？嗯……"
            hide cximg
            show cximg coat eye_sad o at char_mid
            cx "之前好像说过一次了……我没怎么动过……就是去了一次洗手间。"
            hide cximg
            show cximg coat eye_close at char_mid
            cx "嗯，那时候是在看电影……我自己出去的。"
            hide cximg
            show cximg coat o at char_mid
            cx "好像，就是十一点之后吧……大概几分十几分的时候？"
            hide cximg
            show cximg coat at char_mid
            cx "不，没人看见我……应该。"
            hide cximg
            show cximg coat o at char_mid
            cx "那个放电影的地方很大，入口也拐了好几次，所以……中途自己出去，不会被影响别人看电影……也不会被注意到……"
            cx "晚上房间……？是，202……"
            hide cximg
            show cximg coat eye_sad o at char_mid
            cx "没有，抱歉……我真的不知道……"
            hide cximg
            show cximg coat eye_angry o at char_mid
            cx "我也不知道梁绵绵为什么会这样！"
            hide cximg
            show cximg coat eye_shock o at char_mid
            cx "不，没有，我……抱歉……对不起……"
            hide cximg
            show cximg coat eye_shock at char_mid
            "岑宣陷入无法控制的情绪中，对话中断。"
            hide cximg with dissolve
            jump c2_4_menu1s
        
    return
    
label c2_4_extra1:
    scene bg_hotelroom with Fade(0.5,1,0.5)
    "嘟。"
    "录像带播完，记录的询问对话也看完了，西顺把它拿起来，收回兜里。"
    show xsimg o at char_mid with dissolve
    xs "有什么想法吗？你们。"
    by eye_still o "有个毛线啊……什么都听不出来。"
    me "嗯……只有这些也不太好推测什么吧。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "的确，现在暂时没有物证，还得继续看。"
    by eye_def o  "你问房间号干嘛啊？"
    hide xsimg
    show xsimg o at char_mid
    xs "看晚上她们有没有出去找过人啊，如果是在服务员离开之后去找梁绵绵也是有可能的吧。"
    hide xsimg
    show xsimg at char_mid
    xs "别忘了那个鞋印。"
    by eye_still o "是有可能……但谁会告诉你啊？"
    by eye_def o "二楼没监控的吗？"
    hide xsimg
    show xsimg o at char_mid
    xs "没有，这种地方都比较注意隐私。"
    by eye_still o "啧……那你问了有什么用。"
    xs "嗯，还是得问一下，当做参考。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "之后如果和询问的情况对不上，从说谎动机也可以继续分析。"
    hide xsimg
    show xsimg o at char_mid
    xs "不过，现场的痕迹已经查出来了，有一些进展。"
    by eye_def o "什么？"
    hide xsimg
    show xsimg eye_still smile at char_mid
    xs "这个啊……这个就要你帮忙了。"
    "看到西顺浅浅的笑容，白一顿觉不妙。"
    by eye_wacky o "哈？?"
    hide xsimg
    show xsimg o at char_mid
    xs "等会我把收集好的鞋印给你，你来跟房间里的那个比对一下。"
    by eye_still o "哈？为什么又是我，那你呢？"
    hide xsimg
    show xsimg at char_mid
    xs "我去查颜料啊。"
    by eye_still def "颜料？"
    hide xsimg
    show xsimg o at char_mid
    xs "对。哦，我是不是没有说，有毒物质也查出来了。"
    hide xsimg
    show xsimg eye_still o at char_mid
    xs "是一种含铅量很高的颜料，被扔进蜡烛的容器里面。等蜡烛烧到底下，就跟着一起燃烧。"
    hide xsimg
    show xsimg o at char_mid
    xs "烧的时候，出来的气体全是含铅颗粒的，被受害人从呼吸道吸入，也从暴露的伤口感染了。"
    hide xsimg
    show xsimg at char_mid
    by eye_still o "颜料……？竟然会是这种东西。"
    by eye_def e "听起来并不是那种很难搞到的东西啊。"
    me "但是，颜料的毒性有这么重，还能拿出来卖吗？"
    by eye_def o "也许是一般人不会想着把它烧了？"
    me "嗯……"
    hide xsimg
    show xsimg o at char_mid
    xs "这种颜料会有残留一定毒性，但一般来说效果不会这么严重……"
    hide xsimg
    show xsimg eye_still o at char_mid
    xs "虽然也有受害人本身的体质原因，但我们还是认为颜料问题很大。"
    hide xsimg
    show xsimg eye_still at char_mid
    xs "所以，现在要查它的来源。"
    hide xsimg
    show xsimg o at char_mid
    xs "那么，检查鞋印的事情，就拜托你了。"
    by eye_still o "哦，难怪……{size=35}等等？？？{/size}"
    "西顺三言两语间就给白一增加了工作。"
    hide xsimg with dissolve
    "以至于白一都还没反应过来，她就已经把东西留下，人出去了。"
    by eye_wacky o "不是，她——我靠？？"
    me "噗……人都已经走了，你叫也没用。"
    by eye_wacky o "你在笑个毛线啊？难道你就不用看了？"
    me "……好吧。"
    "房间里留下的痕迹并不多，只能收集部分鞋印图案，所以不容易直接比对。"
    "白一认命地把资料摊开，对着那些相似的形状，试图找出和房间里相同的那个。"
    jump c2_4_choice1
    return

label c2_4_choice1:
    scene black with dissolve
    $ quick_menu = False
    show footprint with dissolve
    $ persistent.inputstyle = 1
    python:
        foot = renpy.input("能对应上的编号是？", length=4)
        foot = foot.strip()
        if not foot:
            user = "0"
    $ quick_menu = True
    if foot == "10":
        jump c2_4_extra2
    else:
        scene bg_hotelroom with Dissolve(1)
        by eye_def def "哦，是这个吗？我看看……"
        by eye_still def "……"
        by eye_still o "你眼睛是不是有问题？这看起来哪像了？"
        me "啊？哦，嗯……这是个意外。"
        jump c2_4_choice1
    return

label c2_4_extra2:
    scene bg_hotelroom with Dissolve(1)
    by eye_def def "哦，是这个吗？我看看……"
    by eye_still o "嗯——好像……真的是？"
    "看到走势几乎一模一样的曲线，白一反而有些不敢相信，来回比对了好几次。"
    by eye_def def "嗯，好像真的是。"
    me "对啊，就是这个没错。"
    me "所以这是谁的？"
    by eye_def o "嗯我看看啊，是——"
    "白一的声音忽然停了一会，才说完后半句。"
    by eye_still e "……呃，是岑宣的。"
    me "……啊？"
    me "岑宣？"
    "一瞬间，我怀疑自己的耳朵出了问题。"
    by eye_close o "是啊，就是那个在医院恨不得把我吃了的岑宣。"
    me "……"
    me "可是……她……应该……不会是她做的吧？"
    "说这话的时候，我的声音放得很轻。"
    "毕竟，我自己也知道没什么说服力，只是自己不希望是这样而已。"
    by "啧……这也不能说明就是她啊。只能说明，她曾经去过梁绵绵的房间，并且在这件事上说谎了而已。"
    me "……听起来好像也没有好到哪里去……感觉更可疑了呢。"
    by "那又怎样？不过，她现在的确就是最有嫌疑的那个吧。"
    me "嗯……"

    by "你忘了吗，之前我们看到的那个应该就跟她有关。"
    me "什么？"
    # 【选错】
    by "……不是这个。"
    by "你真的忘了啊？"
    # 【选择内门】
    by "对，那个门不是开着吗，应该就是从那里进去找她的吧。"
    me "的确……她跟梁绵绵的房间是靠着的，进房间找人很方便……"
    by "不过如果是她，那她之前是搞毛线啊……最强演员？"
    me "应该不至于吧……"
    "虽然这的确没有证据，但不知道为什么，我似乎就是觉得她那种情绪并不是假装的……"
    by "啧，谁知道。"
    by "说起来，她不是我们班的，但也来生日会了。"
    me "欸，她不是你们班的吗？"
    by "你没发现吗？眼睛不好使？"
    me "……你每天就坐在自己座位上，我能看到什么啊。"
    by "算了，别在意，这不是重点。"
    "总感觉她是因为说不过就果断转移话题……"
    me "那，姒舞也不是你们班的，没什么奇怪的啊。"
    by "姒舞是我叫来的啊，不知道她是为什么来。"
    me "……被你说得更有嫌疑了。"
    by "还好吧，本来嫌疑就是最大的了。"
    by "不过其实……我私心希望她是凶手。"
    me "啊？为什么？"
    by "这样就不用继续查了。"
    me "……"
    "该说她是太直白呢，还是毫不在乎呢……如此随意地，把堪称恶劣的想法直接说出口。"
    "我实在无言以对。"
    me "还是觉得难以想象，如果是岑宣……她的动机是什么呢？"
    me "而且，那样的话，同学就是凶手什么的……"
    by "……恕我直言，除了服务员小姐，剩下的好像都是同学，是谁有什么区别？"
    by "而且服务员小姐才是最没动机的那个吧，人家只是在工作。"
    me "你说得也……"
    xs "你们在说什么？什么动机？"
    "突然的声音插入了我们的对话，是西顺回来了。"
    by "就是凶手的动机啊。"
    by "哦，对了，那个鞋印是岑宣的。"
    xs "岑宣啊？倒是没有想到……她自己完全没提过这一点。"
    by "谁会把这种一看就很可疑的事说出来啊？"
    xs "这个嘛……如果她不是凶手，这么做反而是害了自己。"
    by "说不定就是呢？"
    xs "嗯，也有这种可能。"
    xs "不过，不管是不是，光靠这个也没法确定。"
    by "还没找到决定性的证据啊？"
    xs "嗯。"
    xs "但先从这个鞋印的问题继续问吧。"
    by "啧……颜料呢？"
    xs "查出来是一个很小众的品牌，之前还因为生产不合规上过新闻。但后来整改了，大概就是上个月的事。"
    xs "从燃烧后剩下的成分分析出来，是跟整改之前的那批颜料一样。"
    xs "但那些颜料现在已经不售卖了，不知道是从哪里来的。"
    me "可能是很早之前就买的吧。"
    by "肯定是。不过，那怎么会现在突然想起来要用？"
    me "这……谁知道呢。"
    xs "这倒是没那么重要，找到现在用过颜料的证据才是最直接的。"
    by "那你倒是找到重要的啊。"
    "白一从喉咙里挤出不爽的声音，不悦地看向西顺。"
    xs "你要去楼下看看吗？"
    by "啊？"
    xs "检查一下案发现场以外的，其他相关的地点。"
    by "……这是可以的吗？"
    xs "可以啊，在你身上放一个定位器就行。"
    by "……"
    by "哦，随你吧。"
    "大概是因为记得西顺之前说的话，现在白一除了嘴上仍然不饶人以外，对西顺的态度并没有之前那么激烈的抗拒。"
    "当然……白一也知道自己并没有什么反抗的资格。"
    "一楼还是跟之前一样，但没有那么多同学在，这里显得更大了。"
    by "啊，真烦，有胆子伤人怎么没胆子承认？"
    me "这个……世界上百分之九十九的凶手都不会承认的吧……"
    me "话说其他人呢？"
    by "应该都还在楼上房间里吧。"
    by "不用跟别人说话倒是感觉舒服了一些。"
    by "从哪开始看？"
    # 【电影房】
    "电影房在一般状态下都保持着黑暗，只有地板上的小灯，勉强照亮走过的路。"
    "- 牛奶"
    "也许是因为室内的空调开得好，牛奶还保持在常温状态，没有变凉。"
    by "谁这么没素质，不把东西带走……"
    # 【游戏室】
    "游戏室亮着灯，东西很多，似乎还保持在昨天很多人玩的状态，显得有点乱糟糟的。"
    "- 窗户"
    "大概是为了透气，窗户开着。窗外是后花园，传来源源不断的冷风。"
    by "阿嚏……！！"
    me "不用离得这么近吧，小心感冒。"
    "白一靠得很近，以至于额头头快靠上窗框了，实在过于冰凉。"
    by "哦，知道了知道了。"
    "- 玩具"
    "玩具被随意地堆在窗户底下的地毯上。"
    "魔方，积木，卡牌……不同种类的玩具被堆在一起，有个小球甚至被挤出了盒子外面。"
    by "东西好多……好乱。"
    me "应该是没来得及收拾，毕竟发生了那种事……"
    by "看着好不爽。能不能把它们收好啊？"
    me "等等，冷静啊——保护现场——"
    "白一收回了蠢蠢欲动的手。"
    "- 显示屏"
    "放在桌子上的显示屏连接着电脑，上面投影着知名游戏平台的账号内容，最新玩过的游戏是《交织的印记》。"
    by "什么鬼……这是什么游戏啊？看名字就觉得很奇怪。"
    by "少女们的情感……纠缠……呃，什么意思？"
    me "啊，这就是文字类游戏吧，有角色扮演，恋爱模拟，悬疑冒险啦之类的。这一部应该就是女主和不同的女生谈恋爱吧。"
    by "哦，懂了。我好像听说过。"
    by "就是说喜欢这种游戏的都是死宅。对吧。"
    me "……请不要用这么不礼貌的称呼。"
    # 【茶水间】
    "- 助眠套装"
    "和房间里收到的一样，是多出来的助眠套装，里面有茶包，香薰蜡烛，蒸汽眼罩。"
    by "从这个角度看……好像确实看不到蜡烛里面啊。"
    me "嗯，就算塞了东西进去也看不出来吧。"
    "- 饮料"
    "桌上摆满了一排排的饮料，除了瓶装，还有桶装的，可以倒在旁边的一次性杯子里。"
    me "要喝点吗？"
    by "可以啊，你喜欢喝什么？"
    me "……"
    "熟悉的问题又开始攻击我，我选择沉默。"
    # 【后花园】
    by "……阿嚏！阿嚏！"
    "刚从后门出去，白一就狠狠地打了两个喷嚏。"
    "空荡荡的花园里，植物被种在道路和中央广场的两侧。平坦的路面上什么也没有。"
    by "靠……别看了，冷得要死。"
    by "一楼，也不包括一楼外面，是吧？"
    me "……你要这么说的话，也行。"
    "说实话，就算我想和白一唱反调，也不能做什么。"
    xs "你——"
    by "什么都没发现，别问了。"
    "西顺拉着白一回到茶水间休息。她还没开口说完，白一就先发制人。"
    xs "……"
    xs "好吧。"
    xs "那么，说回岑宣的事。"
    by "她说了什么了吗？杀人，不，伤人原因之类的？"
    xs "啊？不，她并没有这么说。"
    cx "什么？！不可能吧？……那，那个是……"
    cx "呃……嗯，我不知道……"
    cx "不是！！不是我害了绵绵！我怎么可能会做那种事！！"
    cx "我和绵绵关系很好的！怎么可能会……"
    cx "……"
    cx "我，我是……我……"
    cx "……晚上，是绵绵来找我的。"
    cx "她……敲了里面的门，我才知道是她在隔壁。"
    cx "然后她让我去她房间……说话……"
    cx "……说了什么重要吗？反正，我现在说的，也没什么用对不对……"
    cx "只要我没证据，你们还是会觉得是我害了她……"
    cx "颜料？什么颜料……我不知道啊。"
    cx "我没什么好说的了……"
    "岑宣的状态不太好，声音也断断续续的。"
    by "……她这么说，你就信了？"
    xs "当然没有，所以我也问了别的。"
    xs "不过，这些都只是各自的说法，先听听就好。"
    # 【同】岑宣？她和梁绵绵很熟啊，以前她经常来我们班找梁绵绵。
    # 【同】对……因为最近没来过。听说好像是之前吵架了吧，还挺严重的。
    # 【同】不是我们班的，但岑宣和天玉是好朋友，会来也正常啊。
    # 【同】呃？不至于吧？她们关系挺好的，一次吵架也不会怎么样……
    by "所以是说岑宣和梁绵绵之前关系好，但最近吵过一次架咯？"
    by "这么看来，她从动机和时间上都很可疑啊。"
    xs "的确，不过我倒不觉得她的情绪是装的。"
    by "这也能看出来？"
    xs "只是感觉。"
    by "切。"
    me "有没有可能……是她原本也不想这样……但是误伤了？"
    by "这玩意要怎么误伤啊？"
    me "呃……谁知道呢……只是说不定？因为她看起来也确实很难过……"
    by "可能真的是装的啊。"
    xs "不管是不是，她有一点说得没错，就是没有证据。"
    xs "不管是证明她没害人，还是证明她是无辜的，都没证据。"
    by "也就是说，问了这么多也没用咯。"
    xs "去她房间里看一下吧。试着找出有用的证据。"
    by "哦……"
    "——地图"
    # 【内门】连接201房间，可以把两间房变成大号套房的两扇门。轻轻掩着，都没有上锁。
    by "果然这边也是一样，对称的。"
    # 【盒子】助眠套装，没有拆开过。
    by "她根本没打开过？"
    me "那……会不会她根本就不知道里面有什么？"
    by "不至于吧，天玉肯定说过。"
    by "她都在班上说了，岑宣还是朋友，肯定也会说。"
    me "嗯……也有道理。"
    # 【拖鞋】酒店的一次性拖鞋，被胡乱地甩在床边。
    by "这么说她真的是被梁绵绵叫出去的？"
    me "为什么？啊，因为没换鞋吗？"
    by "对啊，要是她是故意的……肯定会穿酒店拖鞋吧。"
    me "噢，留下鞋印的确很直接。太容易找到了。"
    by "这里也没剩下什么东西啊。"
    me "这也正常……如果有什么明显的估计早就被发现了吧。"
    by "呃啊——"
    "白一发出长长的抱怨声，丧气地倒在西顺拎过来的椅子上。"
    xs "休息会，慢慢来。"
    xs "你好，抱歉，能帮我们拿点喝的吗？"
    xl "您需要什么呢？"
    xs "嗯……矿泉水，加一杯冰咖啡吧，多加点冰。"
    xl "啊那个……不好意思，我们这的制冰机坏了，因为天冷，一直没来得及修……"
    xs "常温也行。没事。"
    "西顺点了点头，重新拿出手机比对着什么。"
    by "等等。"
    "白一原本仰着头，放空脑袋，忽然像意识到什么似的开口。"
    by "你不觉得有点奇怪吗？"
    me "什么？"
    by "她刚刚说的话啊？"
    me "啊？你是说……"
    # 【服务员】
    me "你是说，服务员小姐现在很冷静？"
    by "……我看是你需要冷静冷静。"
    # 【矿泉水】
    me "你是说，你现在不想喝矿泉水？"
    by "……你讨厌喝什么？快点说，我马上去喝。"
    # 【冰咖啡】
    me "你是说，西顺要冰咖啡，多加冰，然后……啊！"
    by "嗯嗯。"
    me "然后服务员小姐说制冰机坏了，一直没修。"
    by "听起来像是坏了有一段时间，至少不是今天才坏的。"
    me "对，没错——那这么说，有个人的话就很奇怪了……"
    # 【选错】
    by "你的前后逻辑呢？有没有点默契啊？"
    me "……原来我们之间是有默契的吗？"
    by "呵呵。"
    # 【选对】
    by "是啊，班长她之前说……"
    me "去茶水间给可乐加冰。"
    by "但制冰机根本没用，所以她肯定是瞎说的。"
    me "所以她肯定是做了别的什么事，还要说谎。"
    by "肯定是去搞蜡烛了啊。"
    me "这么肯定嘛……又没证据。"
    by "难道她也有苦衷，还是不可言说的故事？拜托，都这样了还能是做什么。"
    me "嗯……"
    xs "之前在一楼查过一圈，有什么相关信息吗？"
    by "啊？我想想……不确定，应该有，吧？"
    me "如果是说到卫锋的话……有个地方好像有点奇怪。"
    by "什么？"
    # 【其他】
    by "这地方有什么奇怪的啊？"
    me "呃……哦，错了，不是这。"
    by "靠，你能不能靠谱一点？"
    # 【游戏室】
    by "这里吗？有什么奇怪的地方？啊，你是说——"
    # 【玩具】
    me "我只是觉得不太对劲，但——"
    by "噢，这个地方之前太乱了，没太注意，现在看来……"
    by "那个东西是有点怪怪的。"
    # 【选择图片】
    by "啊对，就是这个？总觉得很眼熟，不像玩具，是啥玩意呢……"
    me "不觉得很像卫锋身上的东西吗？"
    by "啊？有吗，是哪里？"
    # 【头发】
    me "她头发上有个发夹，上面有一串珠子。然后，好像少了一个。"
    by "……这你都能看出来？"
    me "啊……可能是我跟你的视角不太一样。"
    by "啧，那直接拿这个去问她吧。"
    by "不对，这也不能说明什么……不行不行。"
    by "班长的东西掉在窗户旁边，那她肯定在这里做了什么……"
    by "可这个房间里没有别的东西了。"
    me "会不会……在别的地方？"
    by "什么？"
    "如果是窗户旁边的话……也许应该去那里。"
    # 【后花园】
    by "靠，结果还是要来这里啊……阿嚏！"
    me "至少你现在知道要去哪里找了。"
    by "嗯……阿嚏！游戏室那扇窗户是吧？"
    "白一贴着灌木往床边走，到那扇开着窗的地方停下脚步。"
    by "看起来……有区别吗？这里到处都长得差不多，真的是分不清。"
    by "看不出有什么痕迹……直接弄开怎么样？"
    me "会不会被骂啊……"
    by "那就是西顺要管的事了，是她放我出来的嘛。"
    me "……欸等等！"
    "白一无视我的声音，直接把手伸进枝叶交叉的灌木。"
    "粗糙的枝丫划过手臂，因为她粗暴的动作，刮得人生疼，但她似乎毫无感觉。"
    "- 图片点击"
    by "啊，找到了……"
    "一个塑料袋从剥开的杂草和树枝中显露出来。"
    "塑料袋很小，皱皱巴巴的，里面似乎有一片介于固体和液体之间的物质。"
    me "等等等——这个真的不能碰了吧。"
    by "这我还是知道的。"
    "白一不屑地嗤了一声，用定位器的紧急报警功能联系上了西顺。"
    xs "厉害啊。"
    xs "这个很好，拿去分析痕迹和成分，如果查出什么就好办了。"
    by "嗯……应该可以确定了吧。"
    xs "希望如此。"
    "白一垂下眼睛，看着西顺细致地把东西放进证物袋里，轻声叹出一口气。"
    "是放松下来的心情，或许也有些难以言喻的无奈。"
    xs "你昨天晚上去了一次茶水间，是去给饮料加冰了，是吗？"
    wf "是的，那个……怎么了，不是问过了吗？"
    xs "嗯，只是再次确认一下而已。"
    "西顺深深地看了卫锋一眼。"
    xs "所以，是这样没错吧？"
    wf "嗯，对……是的。"
    xs "好吧。那么——你见过这个东西吗？"
    wf "……啊……！"
    "西顺把那个塑料袋拿出来的时候，卫锋肉眼可见地产生了变化。"
    "她下意识地轻呼一声，又硬生生地止住，而后咬紧了嘴唇。"
    wf "……"
    xs "你——关于这个，有什么要说的吗？"
    wf "……"
    "卫锋低下头，不说话。"
    "而西顺只是直直地看着她，毫不遮掩的视线仿佛有千斤重，落在她的身上。"
    wf "……是我之前带来的。"
    xs "容我确认一下，你的意思是，里面的颜料，让梁绵绵中毒的物质，是你带来的吗？"
    wf "嗯。"
    xs "你带着之后，在昨天晚上把它放进装蜡烛的容器里了吗？"
    wf "对。"
    xs "你怎么知道会有这个，嗯，这个机会可以下毒的？"
    wf "……啊……？天玉，在班上说过，会送香薰的事。"
    xs "颜料是哪里来的？"
    wf "……以前，家里剩下的。"
    xs "为什么会想这么做？"
    wf "……"
    xs "据我了解，你和梁绵绵之间似乎并没有超过同班同学的交流，是有什么矛盾吗？"
    wf "……"
    xs "为什么要对梁绵绵下手？"
    wf "……"
    wf "对不起……我做了错事。"
    wf "希望能得到应有的惩罚。"
    "卫锋对于自己是下毒者的事供认不讳，有问必答。"
    "然而，提到“动机”这一点时，无论怎么问，她都没有给出任何回应。"
    "只是重复着认错的模样，诚恳道歉，渴望受罚。"
    "最后，被几个人带上车，融入在黑色的阴影里。"
    return