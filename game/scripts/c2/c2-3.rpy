label c2_3:
    $ quick_menu = False
    scene black with Dissolve(3)
    $ quick_menu = True
    "……"
    scene bg_hotelroom with dissolve
    show tophalfblk
    by eye_close def "……"
    by eye_still e "……呃，什么鬼？"
    hide tophalfblk with dissolve
    "白一摇摇晃晃地从床上坐起来，眼睛半睁不睁，一时间还没有分清现在是什么情况。"
    me "你昨晚回到房间之后，收拾了一下就直接睡着了。"
    by eye_still o "啊？哦，对……我很少这么晚睡，好累……"
    "昨晚的活动弄到十二点多一些，白一大概是十二点半睡的。"
    "现在醒来，还有些晕晕乎乎的感觉。"
    by eye_still e "呃啊，好难受……"
    me "……十二点半睡也还好吧？"
    by eye_move o "估计是昨晚太吵了……感觉现在头还在痛……"
    "白一发出有些烦躁的呻吟，不太痛快地下床。"

    by eye_def o "说起来昨天都还没来得及看房间，还说要好好享受一下。"
    by eye_close o "可惜，待会吃完早餐就要走了。"
    "白一说着，很快收拾好自己，准备推门——"
    by eye_def def "嗯？"
    "推门出去，但门后却不是走廊，而是另一扇上锁的门。"
    by eye_still o "啥？……哦，我走错了。"
    "她有些无语，这才发现房间里除了房门还有另外一扇内门，看起来一模一样。"
    me "这是干嘛的？"
    by eye_def o "大概就是，连号的两个房间是个套房，两边都打开门的话就可以变成大房间。"
    by eye_def o "都锁上就是分开的两个房间，可以分别住。"
    me "噢——"
    by eye_move o "啧，真的好高级。"

    $ quick_menu = False
    window hide
    scene bg_diningroom1 with Fade(0.5,1,0.5)
    show screen tpoinfo("1月1日，星期六","云玉阁") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    window show
    $ quick_menu = True
    "尽管昨天的活动结束是零点之后，有些人也许闹到更晚，但年轻人大多是精力充沛的——{p}当然，白一除外。"
    "等到白一下楼的时候，已经能看到大多数人起床了，在走廊和大厅三三两两。"
    "部分人在餐厅吃饭，还有些更有精力的，拿着早饭就和别人开下一把游戏。"
    by eye_move e "唔，最后一次免费的饭，可惜啊。"
    "白一拿着包子塞进嘴里，一边含含糊糊地说着话。"
    me "嗯……说起来，明明是来参加天玉的生日会的，结果都没怎么看到她。"
    by eye_close o "没必要啊。"
    by eye_def o "她是大小姐，我是路人甲，待在角落凑合就好咯。"
    "她说着，又拿起另一个包子。"
    "包子的面皮柔软，内馅是香菇猪肉，味道香浓，鲜嫩多汁。"
    "配上冒着热气的豆浆，咸甜具备，鲜美的味道在口腔弥漫。"
    me "嗯……的确很好吃。"
    by "是吧，咱们专心吃饭就好——"
    show tophalfblk with vpunchm
    unknown "{size=45}啊！！！{/size}"
    "话音刚落，隐约有尖叫声从不远处的大厅传来。"
    "能传到这里让人听见，说明声音不小。"
    "白一的动作顿了顿，迅速把最后一口吃的咽下去。"
    hide tophalfblk with dissolve
    by eye_still o "难道我有乌鸦嘴？"
    me "嗯……不要迷信，要相信科学。"
    by eye_still e "……你这种东西都出现了，你让我相信科学？"
    me "……"
    "她毫不留情地吐槽我，但也没停下脚下的动作，跟着其他人往外走。"

    scene bg_lobby with fade
    "大厅，不少人聚在靠墙的沙发旁边。"
    "不少人都在小声说话，聚在一起却也显得声音嘈杂。"
    "能听到声音，却听不清在说什么，令人感到更加烦躁。"
    by eye_still e "什么情况啊……"
    "白一皱了皱眉，刚想靠近一点，就感觉右边的手臂被拉住了。"
    show swimg coat o at char_right with moveinright
    sw "等等呀，别过去。"
    by "姒舞？你怎么在这……"
    show swimg coat o at char_mid with moveinright
    sw "大家都是听到声音过来的，有人突然晕倒了，正在打电话叫救护车。"
    hide swimg
    show swimg coat eye_sad o at char_mid
    sw "你就别凑过去了，好挤的。"
    by eye_def e "呃，是吗……"
    by eye_def o "所以怎么会晕倒？"
    hide swimg
    show swimg coat eye_sad at char_mid
    sw "唉，不知道啊，听说看起来像吃错东西了，但是不确定。"
    by eye_def o "啊？怎么可能？"
    hide swimg
    show swimg coat eye_sad o at char_mid
    sw "对啊，所以大家都很担心的呢。"
    hide swimg
    show swimg coat eye_sad at char_mid
    sw "感觉心情好复杂哦……"
    by eye_still def "？"
    by eye_def o "你和晕倒的人很熟吗？"
    hide swimg
    show swimg coat o at char_mid
    sw "不熟呀。"
    by eye_def e "那你有什么好复杂的。"
    hide swimg
    show swimg coat eye_blink at char_mid
    sw "唔，在这里出事，肯定会影响天玉。看到她吃亏我应该高兴。"
    hide swimg
    show swimg coat eye_sad o at char_mid
    sw "但是因为别人的身体健康问题弄成这样……我又不高兴了。"
    hide swimg
    show swimg coat eye_sad at char_mid
    by eye_still def "……"
    by eye_move o "别想太多。"
    "白一无法理解她这复杂的心情，最后只是干巴巴地这么说。"

    scene bg_lobby1 with fade
    show tyimg coat eye_still o at char_mid with dissolve
    ty "大家——我有件事情想说。"
    hide tyimg
    show tyimg coat eye_still at char_mid
    "天玉的声音响起，其他人不约而同停下了说话。"
    "她的表情有些严肃，没了平时那副和气温柔的样子。"
    hide tyimg
    show tyimg coat eye_still o at char_mid
    ty "今天发生这样的事情……我非常抱歉。"
    ty "救护车马上就到了。同时，我们会在送梁绵绵同学去医院之后，马上安排大家进行体检。"
    ty "我们从昨天晚上到今天都是一起在这里吃住，其他人没有事，也许梁绵绵同学也会很快好起来的。"
    hide tyimg
    show tyimg coat eye_close o at char_mid
    ty "我也不希望看到这样的情况，也希望大家保持冷静。"
    hide tyimg
    show tyimg coat eye_still o at char_mid
    ty "希望大家相信我，也要相信梁绵绵同学。"
    hide tyimg
    show tyimg coat eye_still at char_mid
    "大厅安静下来后，天玉的声音也能清晰地传入每个人的耳朵里。"
    "她的声音不大，也没有激动的吼叫声，只是有节奏地，沉静地把情况娓娓道来。"
    "清晰的话语柔和但不失力量，仿佛有一种魔力，使得其他人也不那么惶恐慌张。"
    "她说完话，许久都没有人再开口，但那种如绷紧的弦一般的气氛不知不觉间慢慢消散了。"

    scene bg_lobby with fade
    show swimg coat eye_sad o at char_mid with moveinleft
    sw "白一……"
    "人群散开后，姒舞不知道从哪又摸了过来。"
    hide swimg
    show swimg coat eye_sad at char_mid
    by eye_def o "啊。"
    hide swimg
    show swimg coat eye_sad o at char_mid
    sw "怎么办，白一，我突然感觉天玉还挺厉害的……"
    sw "可是，我真的好不喜欢她啊……"
    hide swimg
    show swimg coat eye_sad at char_mid
    sw "可是，我又觉得我不好不喜欢她……"
    "姒舞自顾自地说了一通，让白一都没来得及说话，还差点被她绕来绕去的说法弄晕了。"
    by eye_still e "……那你就不喜欢啊。"
    hide swimg
    show swimg coat o at char_mid
    sw "但她很厉害呀。"
    by eye_still o "她厉害跟你不喜欢有什么关系？又不冲突。"
    hide swimg
    show swimg coat eye_sad o at char_mid
    sw "就是……觉得不太好。"
    by eye_def o "那你试着喜欢？"
    hide swimg
    show swimg coat eye_squint at char_mid
    sw "我不想喜欢……"
    by eye_wacky def "……"
    by eye_wacky def "{size=23}到底要怎样啊……{/size}"
    hide swimg
    show swimg coat at char_mid
    "白一有些无语，拧了拧眉，索性转移了话题。"
    by eye_def o "车应该要到了，收拾好东西走吧。"
    hide swimg
    show swimg coat smile at char_mid
    sw "诶？好~"

    scene bg_medical1 with Fade(0.5,1,0.5)
    "医院是个很神奇的地方。"
    "人很多，声音也嘈杂，乱糟糟的。"
    "却并没有让人感觉到任何鲜活感。"
    "白一拿着自己的资料，跟在队伍后一个个做完检查，终于回归自由。"
    by eye_close o "好累啊……总觉得有点喘不过气。"
    me "嗯……出去透透气吧。"
    "白一的声音很轻，甚至可以说是有些虚弱。"
    "也许是因为排队太久，走路的时候腿脚也有些乏力。"

    scene bg_medical3 with dissolve
    by eye_move e "啊，真烦……"
    by eye_close o "没想到最后会是这个走向……啊！"
    show tophalfblk with vpunchm
    "下楼梯的时候，白一突然感觉腿一软，整个人向下倒去。"
    by eye_squint def "呃……！"
    show black with dissolve
    "想象中的剧痛并没有来临。"
    "有人及时拉住了她。"
    unknown "你没事吧？"
    me "对啊好险……你没事吧？"
    by eye_still o "嗯，没……嗯？"
    show cg_cx01 at cg0 with dissolve
    hide black
    "白一重新睁开眼，看到面前的人抓住自己的手臂，又很快松开。"
    show cg_cx00 at cg0 with dissolve
    "她脸上带着的担忧变为惊讶，而后是像在忍受什么的，深深的凝视。"
    scene bg_medical3 with Fade(0.5,1,0.5)
    show cximg coat eye_sad at char_mid with dissolve
    cx "怎么会是你……"
    by eye_still o "呃……你是？"
    "她和看起来和白一差不多大，表情变幻得像调色盘一样丰富，令白一感到困惑。"
    me "她叫岑宣，你认识吗？"
    by eye_def e "{size=23}不认识……{/size}啊，我是说，我不认识你。"
    hide cximg
    show cximg coat eye_angry at char_mid
    cx "……"
    hide cximg
    show cximg coat eye_angry o at char_mid
    cx "我是，跟你一个学校的，就在你楼上的班级的，你的同学，梁绵绵的朋友。"
    "岑宣一字一顿地说完这句话，每一次断句都加重了一次语气。"
    hide cximg
    show cximg coat eye_angry at char_mid
    by eye_still o "……噢。"
    "这时候听到梁绵绵这个名字，不太算得上是让人高兴的话题。"
    "因而白一只是干巴巴地应了一声，却令岑宣的眉毛皱得更紧了。"
    by eye_def o "你找我有事？"
    hide cximg
    show cximg coat eye_angry o at char_mid
    cx "你怎么能……都是因为你她才会这样！"
    hide cximg
    show cximg coat eye_angry at char_mid
    by eye_still o "……啊？"
    "白一不理解她的突然发难，只觉得莫名其妙。"
    by eye_def e "你是说昨天吗？那一桌上又不止我和她吃饭。"
    hide cximg
    show cximg coat eye_angry o at char_mid
    cx "不，你根本不知道。"
    hide cximg
    show cximg coat eye_sad at char_mid
    cx "绵绵她……她不是食物中毒，是别的方式中毒的……"
    hide cximg
    show cximg coat eye_sad o at char_mid
    cx "但是，医生说，她原本不会这么严重。是因为她腿上有大面积的伤口，所以才这么严重的。"
    hide cximg
    show cximg coat eye_angry o at char_mid
    cx "我说的有错吗？这都是，都是因为你啊……"
    hide cximg
    show cximg coat eye_angry at char_mid
    cx "而且她年纪比较小，这样子……对身体的影响更大了……"
    by eye_still def "……"
    by eye_def o "她是怎么中毒的？"
    hide cximg
    show cximg coat eye_sad o at char_mid
    cx "什么？这……"
    by eye_move e "应该不是意外中毒吧。"
    by eye_def o "是谁让她中毒的呢？"
    hide cximg
    show cximg coat eye_sad at char_mid
    cx "……"
    by eye_still e "之前的事，我是很抱歉。"
    by eye_def o "但是……因为我做错了一件事，所有的事都要我承担吗？"
    by eye_move o "我要把你们所有的情绪都放在自己身上承担吗，不太好吧。"
    "白一垂下眼睛，只是淡淡地，缓慢地说完话，就陷入沉默。"
    "她的平静让我感到惊讶，但，我似乎也能感觉到，她的内心并不像语气表现出来的那样。"
    "或许……这只是她的一种习惯。"
    "习惯于让自己在别人面前变得毫无破绽。"
    hide cximg
    show cximg coat eye_close at char_mid
    cx "……"
    hide cximg
    show cximg coat eye_sad o at char_mid
    cx "对，你说得没错……发生这样的事，不能都怪在你头上。"
    hide cximg
    show cximg coat eye_angry at char_mid
    cx "……你觉得，我应该这么说吗？"
    hide cximg
    show cximg coat eye_sad at char_mid
    cx "我很抱歉，抱歉……但是……我不知道……"
    hide cximg
    show cximg coat eye_sad o at char_mid
    cx "也许我该夸你很聪明？很冷静？被人质问还能想到这么多？"
    hide cximg
    show cximg coat eye_angry o at char_mid
    cx "但是，只是……因为你觉得与你无关，你置身事外，你不在乎，你才能做到这样……"
    hide cximg
    show cximg coat eye_angry at char_mid
    cx "是吗？是这样吗？"
    hide cximg
    show cximg coat eye_sad at char_mid
    cx "啊，不，对不起……对不起……"
    hide cximg with dissolve
    by eye_still def "……"
    "岑宣看起来像是很痛苦，她完全没有看着白一，只是低声自语，也不期望得到白一的回答。"
    "而白一只是静静地看着她。"

    scene bg_medical1 with fade
    show cximg coat eye_angry o at char_mid with dissolve
    cx "你要去看看绵绵吗？不，你跟我去看一下绵绵吧。"
    by eye_still o "……为什么？"
    hide cximg
    show cximg coat eye_sad o at char_mid
    cx "因为，因为……我希望你去看一下她……"
    hide cximg
    show cximg coat o at char_mid
    cx "对了，你知道吗？小玉已经报警了，很快就会有人让我们回去等候的。"
    by eye_def o "小玉？"
    hide cximg
    show cximg coat eye_close o at char_mid
    cx "就是天玉。她很厉害，一定会好好负责的，所以……"
    hide cximg
    show cximg coat o at char_mid
    cx "所以，现在你就算走了，之后也要回来。"
    hide cximg
    show cximg coat at char_mid
    cx "所以，就跟我过去看一下她吧。"
    "白一没回应，但也没有拒绝。"
    "她任由岑宣粗暴地拽住手腕，被拉着往楼上走去。"

    scene bg_medical2 with Fade(0.5,1,0.5)
    "病房里很安静，梁绵绵盖着被子，靠坐在病床上。"
    "听到开门的声音，病床上的人影轻微晃动了一下。"
    "好一会儿，她才抬起头，看向白一她们的方向。"
    show cg_lmm12 at cg0 with dissolve
    "梁绵绵的神情空洞，脑袋转过来后，也只是呆呆地看着正前方。"
    "做完转头的动作后，她就没有别的反应了。"
    cx "……绵绵，我来看看你。"
    "岑宣小心翼翼地靠近，在距离病床一米远的地方停住，尝试轻声对她说话。"
    lmm "……"
    show cg_lmm10 at cg0 with dissolve
    hide cg_lmm12
    lmm "啊……"
    cx "那个……我，我是岑宣。"
    lmm "……啊……哦……"
    show cg_lmm11 at cg0 with dissolve
    hide cg_lmm10
    lmm "嘿嘿……"
    "梁绵绵的嘴微微开合，而后，咧开嘴笑了笑。"
    show cg_lmm12 at cg0 with dissolve
    hide cg_lmm11
    "她自顾自地笑了一会，又突然止住。"
    "像是想到什么，她皱起眉毛，用力抿住嘴巴又张开，又抿住，又张开。"
    show cg_lmm10 at cg0 with dissolve
    hide cg_lmm12
    lmm "……不，不……呃……啊……"
    "声音有些僵硬，带着颤抖。"

    scene bg_medical2 with fade
    cx "好，好好休息，绵绵……就这样，靠着就好，对……"
    cx "那，那我先走了……"
    "岑宣弓起身体，让自己的视线和梁绵绵齐平。"
    "她缓缓地用手上的动作安抚梁绵绵，而后，再次谨慎地远离病床，拉着白一走出了房间。"

    scene bg_medical1 with pix1
    show cximg coat eye_sad at char_mid with dissolve
    cx "……"
    hide cximg
    show cximg coat o at char_mid
    cx "你有什么想说的吗？"
    by eye_still def "……"
    "白一没回答，但要表达的意思已经很明显了。"
    hide cximg
    show cximg coat eye_sad o at char_mid
    cx "……我就知道。"
    hide cximg
    show cximg coat eye_sad at char_mid
    cx "我怎么会想着指望你？"
    hide cximg
    show cximg coat eye_angry o at char_mid
    cx "呵呵，你当然不会理解……不可能理解……"
    hide cximg
    show cximg coat eye_sad at char_mid
    cx "对不起……我有点……我现在不想看到你……我先走了……"
    hide cximg with dissolve
    "岑宣说完，低着头飞快离开了。"
    "那之后，白一看了看她的背影，又收回目光。"
    by eye_still o "……她在发什么神经？"
    by eye_move o "明明是她先找上我的，自顾自跑过来，又自顾自走了。"
    by eye_move e "我还什么都没说呢。"
    me "……也不能这么说吧……毕竟……"
    "毕竟是自己的朋友遭遇不好的事，情绪激动也是正常的……"
    "我没能说完这句话，因为白一忽然重重地往墙上一靠，发出沉闷的撞击声。"
    "好像绷紧的弦忽然松开了，白一靠着，长长地叹了口气。"
    

    by eye_def e "[user]？"
    me "……啊？嗯。"
    "她很少这样，可以说是有些刻意地叫我，让我一时间没反应过来。"
    by eye_still o "没什么，就是叫一下，烦一下你。"
    me "……"
    by eye_move e "突然感觉好烦啊。"
    by eye_close o "为什么我又要遇到这种事？"
    me "嗯……是啊。"
    by eye_still o "我真是搞不懂她们，为什么都要这样。"
    me "嗯……嗯？什么意思，谁？"
    by eye_close o "温心，梁绵绵啊……还有班长，岑宣。"
    by eye_still e "{size=23}都会这样吗？发神经……好吧，也不是。{/size}"
    by tye_move def "{size=23}出事之后……会有人因为她的事受影响，为她奔走，甚至迁怒别人。{/size}"
    by eye_close o "啊，算了，当我没说。"
    "白一似乎也不知道自己是在说什么，只是有些烦躁地摇摇头，将刚才的话全部撇去。"
    "也许……是在感叹吗？感叹什么？"
    "是感叹为何自己再次成为迁怒对象，还是感叹于那种竟然真实存在的情谊？"
    menu:
        "“……”":
            "这样的气氛令人感到不安。"
            "因而，我只是保持沉默"
        "“我也会”":
            "这样的气氛令人感到不安。"
            "但，不知为何，在这样的气氛下，我还是想要说些什么。"
            me "……我也会？"
            by eye_wacky o "……你在说啥？会什么？"
            me "啊，就是……我应该也会，因为你的事受影响，吧……"
            me "被她反问，我竟然有些不确定。"
            by eye_still def "……"
            by eye_still e "你是忘了西顺说的话吗。"
            me "……没。"
            "我当然没忘。"
            "她的意思无非就是，我和她现在的一切都只是共感带来的移情，都是被困在一起的吊桥效应。"
            "是一份仅仅存在三个月的，虚假的关系。"
            menu:
                "认同":
                    me "好吧……你说得也对。"
                    "我叹了口气，没法反驳，也不再继续这个话题。"
                "反驳":
                    me "是这样……但是……你是结果论吗？"
                    by eye_still o "啥？什么？"
                    me "只要结果是错，所有都是错的？"
                    by eye_still e "那不是废话吗？走错路，走一段死路有什么意义？"
                    me "呃……也许你觉得走在路上也挺开心的？"
                    by eye_wacky def "难道我是白痴吗？"
                    me "……"
                    "不对……好像又被她带偏了。"
                    me "我只是觉得，只是想说……走那条路是一种经历。"
                    "我慢吞吞地解释，尽量不让自己词不达意。"
                    me "就算没有结果，并不会让经历过的事情当作没发生过……"
                    me "就像所有事情都会留下痕迹……"
                    by eye_def def "……"
                    by eye_close o "随便吧。"
                    "白一没有反驳我，只是这么说。"



    scene bg_lobby1 with Fade(0.5,1,0.5)
    "如岑宣所说，很快白一和其他人就被叫回了云玉阁，每个人会被隔离在单独的房间里。"
    "不过，为了防止影响现场的判断，并不是待在之前的房间，而是在三楼。"
    "出乎白一预料的是，她看到一个熟悉的身影。"

    scene bg_lobby2 with Dissolve(2)
    show xsimg at char_mid with dissolve
    by eye_def o "……怎么又是你？你来干嘛？"
    hide xsimg
    show xsimg eye_move smile at char_mid 
    xs "来加班啊。"
    hide xsimg
    show xsimg smile at char_mid 
    "西顺懒懒地挑起一个笑容，在白一看来，实在很像不怀好意。"
    by eye_still o "这种也算特别案件？"
    hide xsimg
    show xsimg o at char_mid 
    xs "从影响上看，勉强算吧。"
    xs "概率是随机伤人，伤害未成年，还是在这种大型集团的产业里发生的事。"
    hide xsimg
    show xsimg eye_close o at char_mid 
    xs "唔，很难搞啊。"
    hide xsimg
    show xsimg eye_close at char_mid 
    "她耸了耸肩，一副无奈的样子。"
    hide xsimg
    show xsimg o at char_mid 
    xs "所以，你要不要来帮我？"
    by eye_shock o "哈？？"
    by eye_wacky o "跟我有什么关系？"
    xs "我听说了啊，你和受害人的爱恨情仇。"
    hide xsimg
    show xsimg smile at char_mid 
    xs "不如说，我是因为听说你在这，才过来的。"
    by eye_wacky e "……你知道谣言是怎么产生的吗？"
    hide xsimg
    show xsimg eye_close o  at char_mid 
    xs "好吧，我开玩笑的。但你确实很好用，可以帮我提高效率。"
    by eye_still o "别把人说得像工具啊。"
    "尽管这么说，但白一并没有拒绝西顺的话。"
    "从各种意义上说，她都没办法拒绝。"


    scene bg_hotelroom with Fade(0.5,1,0.5)
    me "所以，这里应该就是案发现场吧。"
    by eye_def o "嗯，对啊。"
    by eye_still def "啧……我感觉我就是个工具人。"
    "因为事情发生在早上，房间还没有来得及收拾。在事情发生之后，也被保持在梁绵绵离开时候的样子。"
    # map
    jump hotelroom
    return



label c2_3_extra1:
    scene bg_hotelroom with fade
    $ quick_menu = True
    show xsimg o at char_mid with dissolve
    xs "你看出什么了吗？"
    hide xsimg
    show xsimg at char_mid 
    xs "哦，对了，你先看这个。"
    "西顺递过来一份资料，是关于梁绵绵的报告。上面有些地方被划掉了，大约是一些内部信息。"
    by eye_still def "原来是这样。"
    by eye_def o "我觉得……让她中毒的直接原因……"
    jump c2_3_menu1
    
    return


# for 【中毒原因】
label c2_3_menu1:
    window hide
    $ quick_menu = False
    # 【选择蜡烛】
    show screen clue_choice([14],"c2_3_menu1_wrong","c2_3_menu1_correct")
    pause
    jump c2_3_menu1
    return

label c2_3_menu1_wrong:
    $ quick_menu = True
    hide xsimg
    show xsimg o at char_mid 
    xs "嗯，这个和中毒有关系吗？"
    hide xsimg
    show xsimg at char_mid 
    by eye_move o "呃，不，等等，不是这个……"
    jump c2_3_menu1
    return
    
# 【选择蜡烛】
label c2_3_menu1_correct:
    $ quick_menu = True
    by eye_def o "是蜡烛吧，说是呼吸道吸入中毒的话……"
    me "啊——对，蜡烛可能有问题。"
    me "容器里还有燃烧后的残留物，如果检查的话应该能查出来。"
    hide xsimg
    show xsimg eye_still o at char_mid 
    xs "嗯，有道理。这样说就行得通。"
    hide xsimg
    show xsimg o at char_mid 
    xs "除了这个，还有别的吗？"
    hide xsimg
    show xsimg at char_mid 
    jump c2_3_menu2
    return

# for 【补充内容】
label c2_3_menu2:
    window hide
    $ quick_menu = False
    # 【选择地面痕迹】
    show screen clue_choice([17],"c2_3_menu2_wrong","c2_3_menu2_correct")
    pause
    jump c2_3_menu2
    return


label c2_3_menu2_wrong:
    $ quick_menu = True
    hide xsimg
    show xsimg o at char_mid 
    xs "嗯？这个部分似乎没有更多细节了。"
    hide xsimg
    show xsimg at char_mid 
    by eye_still o "哦……是吗。那，就不是这个……"
    jump c2_3_menu2
    return

# 【选择地面痕迹】
label c2_3_menu2_correct:
    $ quick_menu = True
    by eye_def o "哦，对了，洗手间里。"
    by eye_still e "有一个……呃，看起来像鞋印的东西。"
    hide xsimg
    show xsimg o at char_mid 
    xs "等等，我去看看。你没把痕迹弄掉吧？"
    by eye_still e "……你觉得我看起来像白痴吗？"
    hide xsimg with dissolve
    "西顺已经习惯白一的阴阳怪气，对此视若无睹。"
    "她推开洗手间的门，有些小心，不让自己影响里面的痕迹。"
    scene bg_hotelroom with fade
    show xsimg o at char_mid with dissolve
    xs "嗯，没错，是鞋印。那好，等会我去把所有人的鞋底都记录一下。"
    jump c2_3_extra2
    return


label c2_3_extra2:
    $ quick_menu = True
    hide xsimg
    show xsimg at char_mid 
    xs "那现在先这样。"
    hide xsimg
    show xsimg o at char_mid 
    xs "因为推测中毒时间是零点到一点半之间，所以我去问了在这之前所有人的单独行动情况，然后选了一部分。"
    hide xsimg
    show xsimg at char_mid 
    xs "你看一下这些，有没有可以补充的。"
    hide xsimg with dissolve
    by "啊？哦……"
    
    $ persistent.clue[20] = 1
    show clue_20 at clue with dissolve
    xs "就是这些，当然这个具体时间点是有偏差的，不过不多，也不影响。"
    hide clue_20 with dissolve
    by eye_wacky e "我靠，这也太多了吧，这要一个个问过去吗？"
    "那张表格的确问得很详细，基本上有三分之一的同学名字都在上面。"

    me "嗯……也许？"
    me "要不从你熟悉的人开始看。"
    by eye_def o "我没有熟悉的人。"
    me "……喂……"
    me "你这话要是让人家姒舞知道了，她会很难过吧。"
    by eye_close o "她装的吧。"
    me "……"
    by eye_still o "就算熟悉也不知道啊，拜托，我昨天全程只关注过吃饭好吗？"
    me "这倒也是……"
    by eye_stil le "如果有看到别的，难道你会不知道吗？"
    me "这，这倒也是……"
    by eye_still o "或者，你有注意到别的？"
    me "……我没有。"
    "说完，我不免有些心虚。好像是没有问她的必要……"
    by eye_wacky smile "呵呵，那你还能知道点什么？你怎么好意思问我的？"
    "白一果然冷笑起来，明晃晃地翻了个白眼。"
    by eye_close o "这太扯了，关我什么事。"
    by eye_close def "等西顺回来，让她自己筛选去吧。"
    me "……"

    scene bg_hotelroom with fade
    show xsimg eye_close o at char_mid with dissolve
    xs "啊……"
    "西顺在墙边的沙发上坐下，轻轻叹出一口气。"
    hide xsimg
    show xsimg o at char_mid 
    xs "你看得怎么样了？"
    by "……就那样？"
    hide xsimg
    show xsimg eye_close at char_mid 
    xs "好吧。那么……"
    hide xsimg
    show xsimg eye_still o at char_mid 
    xs "蜡烛的确是直接原因，不过不是它本身有问题，而是被人为加入了有毒物质。"
    hide xsimg
    show xsimg o at char_mid 
    xs "具体还不知道是什么东西，不过，总之是被掺杂在一起，在蜡烛使用时一起燃烧。"
    xs "问过云玉阁那边，提供给学生的那个助眠礼盒是七点左右才拆开分装到每个小盒子里的。"
    xs "在此之前，那些蜡烛和茶包都是在密封的快递箱里。"
    by eye_def o "就是说，所以在分完之后才有机会放东西进去咯？"
    hide xsimg
    show xsimg at char_mid 
    xs "嗯，没错。"
    hide xsimg
    show xsimg o at char_mid 
    xs "小盒子是谁都可以打开的，所以要往里面放东西很容易。"
    xs "那些盒子放在茶水间，天玉说她在21:30的时候还一个个检查过。但是她只看了有没有缺东西，没仔细看过里面。"
    by eye_still e "哦……那个蜡烛的容器不是透明的，不是刻意的话，很难看到里面吧。"
    hide xsimg
    show xsimg at char_mid 
    xs "是啊。"
    hide xsimg
    show xsimg o at char_mid 
    xs "一楼走廊上有监控，我们确认过，和询问的记录能够对应。"
    hide xsimg
    show xsimg eye_close o at char_mid 
    xs "不过那个监控角度不行，游戏室和茶水间在一侧，看不清具体是哪个门进出的。"
    hide xsimg
    show xsimg o at char_mid 
    xs "当然，两个房间互相进出走动是看得出来的。"
    by eye_def o "那还能看清人的吗？"
    xs "看得清，门是角度问题嘛。也能够看到没人拿过那些助眠包裹到走廊上。"
    by eye_def o "所以要下手的话肯定是在茶水间里咯。"
    hide xsimg
    show xsimg at char_mid 
    xs "没错。而且从逻辑上来说，特地把它拿走再放回去没什么必要。"
    by eye_def o "也就是说，要查去过茶水间那个方向的人啊……"
    by eye_wacky e "也太多了吧喂。"
    hide xsimg
    show xsimg eye_move o at char_mid 
    xs "没办法，谁让你们来了这么多人呢。"
    by eye_still def "……"
    hide xsimg
    show xsimg o at char_mid 
    xs "对了，刚才检验那边查出来，梁绵绵房间的那个助眠礼盒上，只有她和服务员的指纹。"
    by eye_still e "哦……所以呢？她是凶手？"
    hide xsimg
    show xsimg eye_close def at char_mid 
    xs "这不能确定，一般凶手不会让自己的指纹留在现场，但，也不排除有疏忽的可能性。"
    hide xsimg
    show xsimg o at char_mid 
    xs "不过，大家都知道是她把礼盒送到每个人的房间，没有留下指纹反而才奇怪。"
    by eye_still o "……那你说这个有什么意义？"
    xs "嗯，从目前的线索看，她就算不是凶手，也至少算是嫌疑人之一。"
    hide xsimg
    show xsimg at char_mid 
    xs "就像你说的，我们不可能漫无目的地枚举。"
    by eye_move def "哦……"
    hide xsimg with dissolve
    me "等等，礼盒有这两个人的指纹的话有点奇怪？"
    by eye_def o "嗯？什么奇怪？"
    me "因为……如果是这样的话……那张行动表上，有嫌疑的只有一部分人……"
    by eye_def o "啊？是吗。"
    "白一下意识皱眉，又重新看了看那张纸。"
    by eye_def e "哦……那，有嫌疑的是谁，要问多少人啊？"
    return

label c2_3_choice:
    me "嗯……要问的人数应该是……"
    menu:
        "3":
            jump c2_3_choice_wrong
        "4":
            jump c2_3_choice_wrong
        "5":
            jump c2_3_extra3
        "6":
            jump c2_3_choice_wrong
    return


label c2_3_choice_wrong:
    # 【选错】
    by eye_still o "嗯……好像不对吧？你是不是不识数？不是这些……"
    jump c2_3_choice
    return

label c2_3_extra3:
    by eye_def o "哦，对，应该是这样。"
    "白一点点头，用旁边的笔在纸上潦草地画了几笔，递给西顺。"
    show xsimg o at char_mid with dissolve
    xs "嗯？这是……"
    hide xsimg
    show xsimg eye_still o at char_mid 
    xs "我明白了，你的意思是说，礼盒上没有天玉的指纹。"
    by eye_def def "对……"
    hide xsimg
    show xsimg o at char_mid 
    xs "她在21:30的时候还检查过，却没有留下指纹。"
    xs "那么，如果是凶手擦掉的，凶手只能是在她之后进入房间的，或者，就是她本人。"
    hide xsimg
    show xsimg at char_mid 
    by eye_still def "嗯……"
    by eye_def o "所以，至少现在只用看这些人对吧？"
    hide xsimg
    show xsimg o at char_mid 
    xs "嗯，行，应该没问题。"
    "西顺拿着手机，又看看那张资料，似乎是在比对什么。"
    xs "那么，几个需要现在调查的人，天玉，服务员小蓝，姒舞，卫锋，岑宣。"
    xs "那工作量就少很多了，你可以先休息会，吃点东西。"
    xs "我之后再来跟你说。"
    by eye_def o "哦，好。"

    scene bg_hotelroom with fade
    "云玉阁分给同学们住的房间窗户很大，拉开窗帘，能够看见摆放成特定形状的花朵。"
    show bg_garden with dissolve
    "窗外更远处，能看到是一片空地，昨天，众人就是在那里完成庆祝活动。"
    hide bg_garde with dissolve
    by eye_still o "然后，就在这些人里面……一个同学要害了另一个吗？"
    by eye_move def "啧啧……"
    "白一用手撑着头，坐在窗边，百无聊赖地戳弄着窗帘上的绳子。"
    me "你觉得会是谁？"
    by eye_still o "我怎么知道……"
    by eye_close o "我唯一知道的就是，这几个人我都认识。"
    me "……那你知道的可真多。"
    by eye_move o "还行还行。"
    "我跟她互相呛声，但也只是说了一些废话般的言论，说不出个所以然来。"
    by eye_def e "不过硬要说的话，就因为认识，反而更难猜测了。"
    me "……近乡情怯？"
    by eye_still o "这词是这么用的吗？"
    by eye_move o "我只是觉得，虽然我是没什么感觉……但真的会发生什么事，要到给人下毒的地步吗？"
    by eye_move def "梁绵绵啊……"
    "白一不由自主地轻声念着梁绵绵的名字。"
    "也许即使是她，虽然说着没感觉，但也会因为这样的事情感到惋惜。"
    "那个笑得开朗，甚至有些傻傻的女生……"
    "为什么，非得遇到这种事情不可呢？"


    by eye_close o"啊，真是的……这里又不是电视剧，大家都是普通女高中生没错吧……"
    by eye_still def "竟然给我搞这种事……"
    me "……应该是吧？"
    me "但要这么讲，现在你好像是最不普通的那个，女高中生。"
    by eye_wacky def "……靠！"
    "白一的手指顿住，而后忽然用力扯了扯绳子，像在发泄情绪。"
    by eye_still o "你还好意思说？那不都是因为你？"
    me "……不不，在这一点上，我们都是被坑了好嘛？"
    by eye_move def "……切。"
    return