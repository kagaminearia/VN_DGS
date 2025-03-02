label c2_2:
    scene bg_byroom1 with fade
    "天玉办的派对活动在12月31日。"
    "星期五晚上，还正好能赶上跨年，实在是过于适合玩乐的时间。"
    "即使这天通常是要和家人一起过，也有不少人是愿意出来和同学玩的。"

    $ quick_menu = False
    window hide
    scene bg_manor1 with Fade(0.5,0.8,0.5)
    show screen tpoinfo("12月31日，星期五","云玉阁") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    window show
    $ quick_menu = True
    "白一到达目的地时，天色已晚，但这里的路灯很亮，倒也不影响什么。"
    "雕花的铁制大门打开，平整的大道一路向前向上，隐约可见远处山坡上的低矮建筑群。"
    "两侧是精心种植的灌木，种在温和灯光的照耀下，在冬日的夜晚里显得格外鲜艳。"
    by eye_wacky e "靠，她是公主吗？这么大排场。"
    me "毕竟，好像要请将近一个班的人吧？"
    by eye_close o "啧，受不了。太浮夸了。"
    me "……你还要去吃饭呢。"
    "依稀记得有句老话叫“端起碗吃饭，放下碗骂娘”。"
    "白一这吃饭还没吃上，已经开骂了。"
    "这份心态实在是……令人佩服。"

    scene bg_lobby with fade
    "大厅已经到了不少人，但人还没齐，并没有集合在一起。坐着休息的，四处游荡的，做什么的都有。"
    "总而言之，很热闹。"
    "但白一进来的时候，仍然有一瞬的安静。"
    "随即，像是刚刚什么都没发生一样，众人继续玩闹，做自己的事。"
    by eye_still o "啧……好多人啊。天玉到底怎么想的？竟然邀请我来。"
    by eye_move e "我在这，其他人不会觉得很晦气吗？"
    me "……等等，有你这样说自己的吗？"
    by eye_close o "我只是很好心地替他们说出内心的想法而已。"
    "白一发出轻哼的声音，不再看那些人的方向。"
    me "……"
    "对于她毫不留情，连自己也不放过的行为，我无话可说。"
    me "可能，实际问题也没那么大吧？在学校不也都是同学吗。"
    by "嗯……但特意叫出来就没必要了。"
    me "可能他们只是看你穿校服奇怪呢。"
    "这话倒是没错。在场好几个人，只有白一穿着全套校服，的确很显眼。"
    by eye_still e "管天管地还管人穿衣服啊？"
    by eye_close o "唉，为了蹭饭，我付出太多。"
    me "……"
    "白一作出沉痛的语气。"
    me "所以，什么时候吃饭？"
    by eye_move o "之前好像是说七点半吧。"
    by eye_close o "唉，我明明都想刻意踩点的。结果没想到，司机开那——么快。"
    by eye_def e "哇，我感觉晃得脑浆都要出来了。"
    me "……"
    me "那，就先在这看看呗？反正也没事做……"
    by eye_def def "哦，好吧，有道理。"
    # map
    jump lobby
    return



    

label c2_2_extra:
    scene bg_lobby with Fade(0.5,1,0.5)
    "绕一圈的时间过得很快，白一没空再去看这里的其他地方，人就到齐了。"
    "天玉从里面把门推开，一群人欢呼着进去。"
    scene bg_diningroom2 with sunshine
    by eye_move e "这里真够大的……"
    show tophalfblk with vpunchm
    by eye_shock o "啊……！"
    "白一正四周打量着房间，忽然被什么东西撞了一下，身体一歪，撞到墙上。"
    by eye_shock o "我靠，干嘛？"
    hide tophalfblk with dissolve
    "她猛地抬起头，瞪向受到冲击的方向。"
    stu "啊对不起不好意思……"
    "那人显然也很抱歉，不住地说对不起。"
    show tyimg o at char_right with moveinright
    ty "怎么了？"
    "天玉似乎是听到声响，马上过来问道。"
    show tyimg o at char_mid with moveinright
    "看到她来了，那人像是找到了主心骨，立马朝天玉小声解释了几句，就赶紧离开了。"
    hide tyimg
    show tyimg eye_sad at char_mid
    "只剩天玉站在白一面前，微微拧起眉毛。"
    hide tyimg
    show tyimg eye_sad o at char_mid
    ty "发生什么了？你们……没事吧？"
    by eye_def o "哦，没事，只是被撞了一下。"
    by eye_def e "但是手机飞出去了，然后——呃……你踩到了。"
    hide tyimg
    show tyimg o at char_mid
    ty "啊？"
    "白一用手指指了指地面，天玉惊讶地睁大眼，立马把手机捡了起来。"

    "手机被摔碎了屏幕，拿起来的时候能看到电子屏上的内容正在不规则地闪烁。"
    hide tyimg
    show tyimg eye_sad o at char_mid
    ty "真是抱歉……不如就让我来负责修好你的手机吧？也当作替这位同学给你道歉了。"
    hide tyimg
    show tyimg o at char_mid
    ty "我去找人，很快的，不过今天是活动嘛，大概要等几天。"
    hide tyimg
    show tyimg smile at char_mid
    ty "修好之后，我马上就拿去还给你。"
    by "呃……行啊。"
    "白一是真的不太在意这个——她没有什么联系人，平时也不怎么用手机——便无所谓地点了点头。"
    "不过……"
    hide tyimg with dissolve
    by eye_def e "{size=23}我还以为天玉是那种很看不起人的刁蛮大小姐。{/size}"
    "天玉离开后，白一立马开始在背后“诋毁”人家。"
    me "看起来不太像……她也没有对你生气，语气不好之类的。"
    by eye_move o "{size=23}对啊，搞得我都有些不好意思蹭饭了，还能白得一个新手机。{/size}"
    me "……那你如果知道她跟你想的不一样，会不来吗？"
    by eye_close o "不会。"
    me "……"
    "果然……话是要说的，饭也还是要蹭的。"

    scene bg_diningroom2 with fade
    "如白一所说，宴会厅足够大，里面摆满了圆桌和长桌。"
    "圆桌设计成中间是一个大转盘，外侧放置一圈电磁炉的样式。"
    "转盘上是各式新鲜食物。每个座位旁都有一个电磁炉，上面摆放着小锅。"
    by eye_def o "哇，吃火锅。厉害。"
    "白一小声地赞叹，在一众的夸奖喧闹声中并不显眼。"
    "除了圆桌中间的食材，两侧的长桌上还有饮料和各式小吃。"
    "白一找了个角落的圆桌，在最里面的位置坐下。"
    "姒舞如之前所说的那样没有找过来，然而旁边却出现了另一个未曾料想的人。"

    scene bg_diningroom1 with dissolve
    show lmmimg o at char_left with moveinleft
    lmm "我能坐这儿吗？"
    hide lmmimg
    show lmmimg smile at char_left
    "不知为何，梁绵绵忽然靠近没人的角落，冲着白一笑了笑。"
    by eye_def o "啊？哦……好。"
    hide lmmimg with dissolve
    "两人之前的“过节”大家基本都知道，梁绵绵在这坐下倒不显得奇怪，也遏制了其他人看过来的好奇心。"
    "白一虽然不太愿意有人坐得近，但前不久才做了对不起梁绵绵的事，她也只能止住自己蠢蠢欲动的心思。"
    "于是她点点头，从裤兜里掏出耳机挂在耳朵上。"
    "动作十分明显，充分表明了不想对外交流的意思。"
    me "你竟然还把耳机戴上了。"
    by eye_close smile "{size=23}这不是为了跟你“打电话”嘛。{/size}"
    "白一说着，竟然小声地笑出来，颇有些揶揄的意味。"
    me "……"
    "的确，只要带着耳机，加上说话声音小一点，即使一个人说话也不会被觉得奇怪。"
    by eye_def o "火锅的话，你一般喜欢吃什么？"
    me "嗯？都还好，我不怎么挑食。"
    me "不过，一般来说有样东西不怎么吃……"
    by eye_def e "哦——这样啊，了解了。"
    "白一摆出一副恍然大悟的样子，而后伸出手，转动桌上的转盘。"
    "转盘停下，她用筷子夹了满满一盘我不喜欢的菜。"
    me "……"
    me "你的了解了就是这个意思吗？"
    by eye_close smile "嗯呐。"
    "面对我的不敢置信，白一似乎心情很好地笑了笑，把菜放进锅里，很快嘴里就尝到味道。"
    me "……"
    "不等我再说什么，熟悉又陌生的感觉就从口腔传来。"
    "熟悉是因为吃过，陌生是因为不喜欢所以不常吃。"
    "果然一如既往地难吃——"
    by eye_squint def "呕，好难吃，难怪你不喜欢。"
    me "……噗！！"
    "我愣住，而后就是大笑。"
    me "你看吧，我都说了……你还夹这么多。"
    me "不能浪费食物哦。"
    by eye_wacky def "废话，我知道——"
    "白一翻了个重重的白眼。"
    by eye_still o "我吃的时候你不也能感觉到？真不知道你在幸灾乐祸什么。"
    me "……"
    "好像有道理……"
    "但……我好像诡异地理解了，白一之前说的“伤敌八百自损一千”的爽感。"
    by eye_wacky e "咳咳，呕……真受不了……这都什么事啊。"
    me "……我才想说呢。"

    scene bg_diningroom1 with fade
    me "对了，你们之前说的，全名是什么意思？"
    "嘴里难吃的味道太重，我又什么也做不了，只好努力找些话题，试图通过聊天分散注意力。"
    by eye_def o "什么全名？哦，你说天玉啊？"
    me "嗯，对，你们不是说她的全名云天玉吗。"
    by eye_still o "别我们，这是姒舞说的，不是我。"
    me "……这是重点吗？"
    me "不过，其实……我一直看到她是叫云天玉来着。"
    by eye_def o "啊？哦，你能看到……那你竟然能忍到现在才问？"
    me "嗯……我以为是小名之类的，没太在意……"
    by eye_move e "名字要解释的话确实比较麻烦……让我想想。"
    by eye_def o "嗯，以前的话，名字是分姓和名的，名是家长取，姓就是跟着家长嘛。"
    me "是啊，我知道，所以难道现在不是吗？"
    by eye_move o "其实也是……不过四六开吧，多数人的名字是和家里人没关系的。"
    by eye_def o "在信息系统上还是有分姓和名，但姓和名是分开记录，姓的位置可以空着，只要有名字就可以。"
    by eye_def o "成年以后，可以自己给自己取一个姓，在名字前加上，或者就保留原状。"
    by eye_def e "哦还有，已经有姓的人，只能在结婚的时候改。"
    by eye_def o "没有姓的，有些结婚之后，也会和自己伴侣选择同一个姓加在名字前面，大概……算是一种仪式感吧。"
    by eye_def o "比如姒舞成年之后可以叫苏姒舞，或者苏舞，看她的名字是怎么登记的。"
    by eye_def e "天玉结婚后可以从云天玉改成祝天玉之类的。当然，她应该是不会改的啦……"
    me "嗯？为什么这么说？"
    by eye_def o "她家里人让她用了姓，说明这很重要啊，当然不会改了。"
    by eye_def o "之前不是说了嘛，大概有四成人会让孩子跟着家长姓。"
    by eye_def e "这种情况呢要么是家庭环境比较传统，要么是有家族企业需要继承，要么就是个人喜好。"
    by eye_def o "像天玉这种大小姐，当然也是在这类人里的咯。"
    me "听起来很复杂。"
    by eye_close e "对啊，所以我们平时就是，别人说怎么叫称呼，直接叫就完了。"
    by eye_def o "姓啊名啊，都是登记在信息系统上的事。天玉说她叫天玉，那我们就叫她天玉，别的，那就不关我事了嘛。"
    me "原来如此啊……不过既然这么复杂，那为啥还要分得这么仔细呢？直接用一整个名字不就完了，总归新生儿也不可能自己给自己取名。"
    by eye_close o "谁知道？其实我也跟你是一样的想法啊，完全不理解。"
    by eye_move e "然而呢——事实证明，绝大部分人都把姓看得十分重要，所以才有专门的记录方式咯。"
    "白一耸了耸肩，语气轻佻。"
    by eye_close o "真是够无聊的。"
    me "是这样啊……那你呢？白是名还是姓？"
    by eye_still e "……你猜猜？猜对了我就告诉你。"
    me "不想告诉我就直说嘛……"
    "其实，我倒没有真的很想知道，只是聊到这里，难免好奇想要问一嘴罢了。"
    "她既然不想解释，那也没必要揪着不放。"
    "当然，就算我真的想揪着不放，其实也没有任何办法就是了……"

    scene bg_diningroom2 with fade
    by eye_close o "啊——受够了，我要洗洗嘴巴。"
    "白一放下筷子，站起来走到两边的长桌旁。"
    "略过色香味俱全的小菜不提，她直奔摆着的各种饮料。"
    by eye_def o "对了，这些你有什么喜欢喝的吗？"
    me "……"
    "实话说……在经过刚刚的事情之后，我不太想开口。"
    by eye_move e "嗤，别慌啊。"
    me "……很难不慌。"
    by eye_still o "哼，算了。我随便问问而已，你以为我很想参考你的意见啊。"
    "她撇了撇嘴，从中间抽出一杯冰可乐，咕嘟咕嘟倒进嘴里。"
    "冰凉的气泡从口腔沁润至整个喉管，令人感到舒爽。"
    by eye_close o "呼，终于，感觉好多了。"

    scene bg_diningroom1 with fade
    "拿着可乐回到座位，白一忽然发现桌上放了个刚才没出现的东西。"
    by eye_def o "……啥玩意？"
    "一把钥匙挂着吊牌，上面写有数字。"
    show lmmimg o at char_left with moveinleft
    lmm "那个是晚上睡觉的房间的钥匙，天玉刚刚拿过来的。"
    hide lmmimg
    show lmmimg smile at char_left
    lmm "啊，我不是故意打扰你打电话……就是这个是给你的，我帮你放到位置上。"
    hide lmmimg with moveoutleft
    by eye_mvoe e "没事……嗯，谢谢。"
    "因为今天晚上会闹到很晚，再让大家回家就太危险了。"
    "天玉直接提供了这栋楼的一整层房间，足够来的同学一人一间住进去。"
    by eye_still o "条件真好啊，比住自己家还好。"
    by eye_move def "就是真的好吵……"
    "虽然还没有正式开始庆祝，但人多总是闹哄哄的。"
    me "你要求也太多了吧。"
    by eye_close o "我就说说而已啊。"
    by eye_def def "啧，反正是我赚了。"
    "终于解决完刚才那盘令我们都难以忍受的菜，白一的动作悠闲了许多。"
    "她不紧不慢地尝过感兴趣的菜——平时在学校或在家里，很难有机会吃得这么好。"
    "因而，胃部有种格外的满足感。"

    scene bg_lobby2 with fade
    "人一多，吃饭的时间就拉得很长。"
    "但即使这样，吃完后距离零点还有很长时间。"
    ty "大家，一起去看电影如何？两个小时正好可以看一部。"
    ty "如果不想，也可以自己去游戏室玩。"
    ty "宴会厅待会就会关闭，如果还要拿饮料和零食的可以去茶水间。"
    ty "但是不要乱跑到其他地方噢，找不到人就不好了。"
    "白一没有去玩游戏的想法，毕竟自己没怎么玩过，也并不擅长。"
    "而朋友？更是没有。"
    "隔着一段距离，她跟在人群的后面往电影房走去，并不起眼。"

    scene bg_filmroom with fade
    "电影室看起来十分专业。"
    "不仅面积够大，座位足够，各种各样的设备看起来和外面的电影院也毫无区别。"
    "白一一如既往，选了最后一排的角落坐下。"
    show tophalfblk with dissolve
    "电影是关于青春爱情的题材。"
    "两个主角在学校相识，一起度过了高中的三年，成为了非常好的朋友。"
    "但毕业总会到来。而在那时，两人间产生了矛盾，以至于连毕业后的网络联系也断了。"
    "大家与电影主角年龄相仿，故事背景也相似，不少人都看得十分入迷。"
    "在两位主角成年后意外重逢时，前面的座位上传来轻声抽气的声音。"
    "白一捏了捏眉心，在众人都全神贯注的时候悄悄从房间里摸了出去。"

    scene bg_lobby2 with fade
    by eye_close o "哈啊……"
    "从电影厅出来，明亮的灯光刺得白一眯了眯眼睛。"
    "她揉揉眼睛，摸索着坐到墙边的小沙发上，长长舒出一口气。"
    me "……你就直接跑出来了？"
    by eye_still e "啊？嗯……对啊。"
    me "你不喜欢看爱情片吗？"
    by eye_def o "爱情片？我不知道啊……"
    me "……合着你根本没看啊。"
    by eye_move o "嗯……差不多吧。我没办法集中精神，看不进去。吵死了……"
    "白一捏着眉心，看起来有些烦躁。"
    me "好吧……那你还跟着进去。"
    by eye_move e "呃，我本来以为可以看的？"
    "她也懒得再说什么了，只是好好地舒展了一下四肢，靠在软和的靠垫上。"
    show tophalfblk with dissolve
    by eye_close o "哎，好烦……要等到什么时候才搞完啊……"
    unknown "搞完什么？"
    by eye_close o "搞完活动啊……嗯？"
    "白一小声念叨的时候，忽然觉得有些不对劲。"
    hide tophalfblk with dissolve
    "她猛地抬起头，就看到另一个身影。"
    show lmmimg at char_mid with dissolve
    by eye_shock def "……"
    by eye_still o "是，是你啊……"
    hide lmmimg
    show lmmimg o at char_mid
    lmm "对呀，还有其他人？你刚刚不是在跟我说话吗？"
    hide lmmimg
    show lmmimg at char_mid
    "面对白一干巴巴的话，梁绵绵显得十分疑惑。"
    by eye_move e "呃，是，没啥……你怎么在这？"
    hide lmmimg
    show lmmimg o at char_mid
    lmm "我出来拿点饮料，就看到你。我才奇怪你为什么在这呢。"
    by eye_close o "……没啥。"
    hide lmmimg
    show lmmimg at char_mid
    "白一轻轻摇摇头，没有解释的意思，也完全表明了自己不想继续说话的态度。"
    "但梁绵绵却没有马上离开，在白一几乎忍不住要赶她走的时候，忽然再次开口。"
    hide lmmimg
    show lmmimg eye_sad o at char_mid
    lmm "那个……我想好想要你帮我做的事了。"
    by eye_def o "哦，好啊。你说。"
    hide lmmimg
    show lmmimg o at char_mid
    lmm "……那个……你有喜欢的男生吗？"
    by eye_wacky e "……啊？"
    hide lmmimg
    show lmmimg at char_mid
    "本来已经准备洗耳恭听梁绵绵的请求，没想到她说的却是听起来毫不相关的事。"
    me "这不就是女高中生最爱的话题吗，恋爱故事？"
    by eye_wacky def "{size=23}……闭嘴啊。{/size}"
    "白一无语地打断我的话，又正经地冲梁绵绵摇摇头。"
    by eye_def o "没有啊。干嘛？"
    hide lmmimg
    show lmmimg eye_sad o at char_mid
    lmm "噢，噢……我就问问。那……"
    hide lmmimg
    show lmmimg eye_sad at char_mid
    lmm "你有喜欢的女生吗？"
    by eye_shock o "啊？？"
    hide lmmimg
    show lmmimg eye_sad o at char_mid
    lmm "抱歉我随便问的……是不是很奇怪？"
    hide lmmimg
    show lmmimg eye_sad at char_mid
    by eye_still o "是啊……你是说突然问我这些问题吗？确实很奇怪。"
    hide lmmimg
    show lmmimg eye_close at char_mid
    "听到白一承认，梁绵绵的脸上浮现出紧张，但听完一整句话，她似乎又放松下来，让白一有些莫名其妙地看着她。"
    hide lmmimg
    show lmmimg eye_sad o at char_mid
    lmm "不是啦……我是说，女生喜欢女生，是不是很奇怪……"
    hide lmmimg
    show lmmimg eye_sad at char_mid
    by eye_still o "……哦。没有啊，反正我男的女的都不喜欢。"
    by eye_def o "所以，都差不多。没什么区别。"
    "她如此总结道，令梁绵绵一时说不出话来。"
    hide lmmimg
    show lmmimg eye_sad o at char_mid
    lmm "真的吗？我不是质疑你，就是……不是很多人都觉得很奇怪嘛……"
    by eye_def o "你问的是我，反正我无所谓。"
    hide lmmimg
    show lmmimg eye_sad smile at char_mid
    lmm "好吧好吧……谢谢你这么说。"
    hide lmmimg
    show lmmimg eye_squint smile at char_mid
    lmm "那……你可以祝我接下来做的事情都一切顺利吗？"
    by eye_def o "啊？"
    hide lmmimg
    show lmmimg o at char_mid
    lmm "就是，我想让你帮我做的一件事啊……"
    hide lmmimg
    show lmmimg smile at char_mid
    lmm "你不是想补偿我吗？真心祝福我，就是最好的补偿啦。"
    by eye_still o "……就这个？"
    hide lmmimg
    show lmmimg eye_squint smile at char_mid
    lmm "嗯嗯，真心祝福，要真心的哦。"
    hide lmmimg
    show lmmimg smile at char_mid
    by eye_wacky def "……"
    by eye_move e "……无法理解……"
    "白一小声嘀咕着，但还是轻叹口气，点了点头。"
    by eye_move o "好吧……我尽量。"
    by eye_close o "那就——咳咳……"
    by eye_def o "祝你顺利……祝你要做的事情，都顺利。"
    hide lmmimg
    show lmmimg eye_squint laugh at char_mid
    lmm "谢谢你呀。"
    "梁绵绵再次笑了，看上去是真的很开心。"
    "这样就好……白一这才缓缓吐了口气，把悬着的心放下。"

    scene bg_lobby2 with fade
    "说完话之后，梁绵绵走了，白一终于松了口气。"
    me "刚刚她那么问，我还以为她要跟你表白呢。"
    by eye_wacky o "哈？？这一点都不好笑。"
    me "就是说说嘛……很像啊。"
    by eye_wacky e "滚啊，像个鬼。"
    me "好吧……那你不回去吗？"
    by eye_def o "回哪？电影厅？回去干嘛？"
    me "就坐在这……不觉得无聊吗。"
    by eye_def e "还好吧。"
    by eye_move o "哦其实……上个学期有个老师特别严格。"
    me "……所以？"
    "我实在没懂她突然提到这个话题的意思，听上去毫无关联。"
    by eye_def o "她不让学生上课睡觉，所以我就练就了一个技能。"
    by eye_close o "看起来像在认真听课，实际上脑袋是放空的。"
    by eye_move e "所以，我很擅长……什么都不做？"
    me "……"
    by eye_def e "所以，就算回去看电影，也差不多，还不如就坐这呢。"
    me "……你把看电影当上课？？"
    by eye_close o "因为，都差不多啊……反正也集中不了精力……都很无聊。"
    me "好吧……这么严重吗？"
    me "我还以为……看起来跟你们的日常差不多，应该不会觉得无聊才对。"
    by eye_still e "哪里差不多了……我又没有朋友，离爱情更是十万八千里远。"
    me "……"
    "这么说好像有道理……我顿时觉得提出这个话题不太明智。"
    me "呃，好吧，我只是觉得，看看也挺有意思的嘛。"
    me "而且，说不定呢？那句话怎么说来着，一切皆有可能……"
    "我给自己刚才的话找借口，而白一则是毫不掩饰地翻了个白眼。"
    by eye_wacky o "拜托，你有没有发现，跟我关系最好，聊天最多，距离最近的人其实是你？"
    by eye_wacky def "而且——"
    "白一的话倏地停住。"
    me "……"
    "她没有继续刚才的话，但我大概猜到她想要说什么。"
    "只是我们都不会再次提起来而已。"
    "关系最好，聊天最多，距离最近。"
    "但……"
    "——我们之间的时间只有三个月。"

    scene bg_garden with Fade(0.5,0.8,0.5)
    "“还有两分钟！”"
    show tophalfblk with dissolve
    "夜幕下，众人兴高采烈地聚在一起，等待着零点的到来。"
    "四周的灯控制在最暗的亮度，只是堪堪能让人看清脚下，不要踩到他人。"
    "深沉的天幕如暗黑的水流，缓缓流淌，漂浮有点点繁星，落入人们的眼睛。"
    "清凉的风吹过，却已撼动不了高涨的情绪。"
    by eye_still def "……"
    "白一站在不远处的角落，看着身旁的热闹，却完全融入不了，也无法理解。"
    "她只是静静看着，那些兴奋和欢喜的脸庞。"
    hide tophalfblk with dissolve
    "{size=45}“十！”{/size}"
    "更大的叫喊声响起，如水潮般，一下又一下。"
    "{size=45}“九！”{/size}"
    "{size=45}“八！”{/size}"
    "{size=45}“七！”{/size}"
    "{size=45}“六！”{/size}"
    "{size=45}“五！”{/size}"
    "{size=45}“四！”{/size}"
    "{size=45}“三！”{/size}"
    "{size=45}“二！”{/size}"
    "{size=45}“一！”{/size}"
    "“零！！！”"
    scene bg_firework0 with dissolve
    "{size=50}砰——{/size}"
    show bg_firework1 with sunshine
    show bg_firework2 with sunshine
    show bg_firework3 with sunshine
    "盛大的烟花于不远处冲天而起，在高空肆意生长。"
    "绚烂而华丽的颜色由中央绽放，铺洒至整片天空。"
    "流光如瀑布般倾泻，随即消散，像是梦境的碎片。"
    "漫天的礼花点亮夜空，也将情绪烘托至顶峰。"
    "“天玉生日快乐！”"
    "不知是谁忽然开口，在礼花爆炸的间隙插入自己的声音。"
    "于是，有其他声音也加入这份激动中，几乎将礼花声音盖过。"
    "“天玉生日快乐！”"
    "“大家新年快乐！！”"
    "“新年快乐！！”"
    scene bg_firework0 with dissolve
    "青少年们欢笑着，叫喊着，交换热烈炽盛的祝福。"
    return