label c1_3:
    by "……阿嚏！！"
    "推开门，白一立马狠狠地打了个喷嚏，随后用力拢了拢外套。"
    me "真的很冷……你不能多穿点吗？"
    by eye_move o "我很穷的，你就冷着吧，我也冷啊。"
    me "……"
    by eye_move def "呵呵。哦，对了。"
    "白一轻哼一声，然后又像想起什么一样，转过身拿下了门口柜子上的耳机。"
    by eye_close o "以免我被当成精神病……啧，说不定真的是。"
    me "……你们学校都不管的吗？带手机上学哎？"
    by eye_def o "没事啦，我这种没存在感的坏学生，不打扰其他人就算好的咯。"
    "白一习以为常地摆摆手，完全不在意这件事。"
    me "好吧……"

    $ quick_menu = False
    window hide
    scene bg_classroom with Fade(0.5,0.8,0.5,color="#000")
    window hide
    show screen tpoinfo("12月14日，星期二","丰宁育才中学") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    window show
    $ quick_menu = True
    "白一的座位在后排的窗边，桌上有些乱，书本被胡乱地堆在四周，空出中间一块地方。"
    "中间摆着一张试卷，折了角，皱皱巴巴，问答题下有几处涂黑的字迹，其余都是空白。"
    me "还真的没人管你啊。"
    by eye_close o "对啊，我不是说过了吗。"
    "白一轻哼一声，随意地把卷子也推到一旁。"
    by eye_def o "我自己戴耳机听音乐，或者趴着睡觉，又不弄出动静影响别人。"
    me "……那你现在不是在跟我说话吗。"
    by eye_move def "{size=23}……我不是说得很小声吗，而且现在还没上课。{/size}"
    me "……"
    by eye_close o "啧，别想太多，我在学校消失几天都不会有人在意的好吧。"
    show tophalfblk with dissolve
    "她说完，就啪的一下，脑袋侧着倒在书桌上。"
    "似乎，还真的完全没有要认真上课的想法。"
    "……"

    scene bg_classroom with pix1
    show tophalfblk with dissolve
    by eye_still o "{size=23}喂……{/size}"
    by eye_def o "喂，喂？[user]？"
    hide tophalfblk with dissolve
    me "啊……呃，啊？"
    by eye_def e "你还活着啊。我还以为你终于消失了，或者聋了。哦，你这种灵体也会聋吗？"
    "下课铃后，连续听到白一的声音，我才后知后觉地发现她在跟我说话。"
    "经过一上午，我的脑子有些麻木，一时没能反应，不知是受了白一的影响还是真的听晕了。"
    me "不是……我刚刚只是没反应过来……怎么了？"
    by eye_still o "这个怎么办？"
    "她用手敲了敲桌面，我这才发现那里被放了一张纸条，上面排列着工整的字迹。"
    "“白一同学：中午放学之后，可以到C栋一楼后门外面等我吗？我有话想对你说。“"
    me "去呗？人家都这么说了。"
    me "嗯，我觉得这种说法，一般来说要么是表白，要么是约架。"
    by eye_still e "啧，你可真会推理，用屁股推理的吧。"
    me "……"
    me "说到这个，你之前才说，消失都不会有人在意……现在在意的人来了。"
    "我说不过她，只好提到另一个揭短的话题。"
    by eye_wacky o "草，这绝对是意外……算了，去看了就知道了。"
    "她低低地骂了一声，把纸条塞进兜里往外走。"

    scene bg_buildingoutside with fade
    by eye_still def "嘶……"
    "冰冷的风吹过，在面颊如尖刀般停留，也仿佛渗透进四肢百骸，令外套的作用变得虚无。"
    by eye_wacky e "靠，真服了，谁啊非要找这个地方说话，我真想打爆他的头——"
    by eye_shock o "咳咳咳——还是算了……"
    me "……？你变得也太快了。"
    by "我不知道找我的人是她啊！现在跑还来得及吗？"
    "——来不及了。"
    "白一小声骂骂咧咧，停住脚步，顺着目光能看到不远处的墙边站着一个女生。"
    me "你不是说你很会骂人的吗。"
    by "是……但是，唉……她真的很烦……"
    by eye_def e "那个，班长……是你找我吗？"
    show wfimg o at char_mid with moveinleft
    wf "白一同学你来了。我有个事情想问问你。"
    hide wfimg
    show wfimg eye_sad o at char_mid
    wf "温心今天还没回学校上学，你知道她现在怎么样了吗？"
    by eye_wacky def "什么？你说的是……"
    hide wfimg
    show wfimg o at char_mid
    wf "那天是我打电话报案的，可能影响到你了，我也想给你道个歉。"
    by eye_shock o "啊？！"
    hide wfimg
    show wfimg eye_sad purse at char_mid
    wf "当时我看到你们都没反应，真的很害怕，所以才……但现在看来，应该是我弄错了吧。"
    hide wfimg
    show wfimg eye_sad o at char_mid
    wf "你们的事……我是说，嗯，那天之后你们应该是去过医院，然后没事了吧？"
    by eye_move e "额……"
    "面对卫锋，白一难得的不知道怎么接话，连呛声都没说出口。"
    "看样子，卫锋大概是以为白一和温心是生命垂危，然后被医院救活了。"
    hide wfimg
    show wfimg eye_sad o at char_mid
    wf "所以，那你应该是和温心一起的吧？你来学校了，她还没来，是不是有什么事情？"
    by eye_still o "我……"
    by eye_move e "呃，那个，好像有人给我打电话，我待会再……"
    hide wfimg
    show wfimg smile at char_mid
    wf "噢这样啊，没事的，没事的，你先去吧，我可以等你！谢谢你啊白一同学。"
    by eye_move def "……"
    scene black with dissolve
    scene bg_schoolcorri with moveinleft
    by eye_move e "怎么办？！草，没想到那个报案的同班同学是她。"
    "白一刷地一下开溜到楼的另一边，声音显得有些烦躁和不安。"
    menu:
        "实话实说":
            me "她都知道这件事，要么就实话实说……"
            by eye_wacky e "西顺不是说不能说的吗？你不会忘了吧。"
            me "那你觉得呢？"
            by eye_move def "……"
            by eye_move e "那……就跟她一个人说一下而已……应该没事。"
            "她像是要说服自己一般喃喃道，下意识用手指攥紧了耳机线。"
            scene black with dissolve
            scene bg_buildingoutside with moveinright
            by eye_def o "班长。"
            show wfimg o at char_mid with moveinleft
            wf "啊！你那边聊完了是吗？那温心……"
            hide wfimg
            show wfimg at char_mid
            by eye_def e "其实——"
            "毫无预兆，白一的声音突兀地停住。"
            "右手的食指指尖突然传来剧烈的痛觉，仿佛正在被炙热的烈火烧灼。"
            "很快，疼痛感开始扩散，如野火侵蚀草原般向全身疯长。"
            by eye_shock o "咳，咳啊……咳咳……"
            "白一止不住地咳嗽，无法说出原本想说的话语。"
            "好一会儿，直到她放弃说话的尝试，那种烧灼感才渐渐散去。"
            hide wfimg
            show wfimg eye_sad o at char_mid
            wf "白一同学……你没事吧？"
            by eye_shock def "咳，没……没事……"
            hide wfimg
            show wfimg eye_sad at char_mid
            wf "那……"
        "敷衍过去":
            me "你不想说的话……大不了你就敷衍过去？"
            by eye_close o "唉，我怕她死缠烂打……"
            by eye_still o "不，算了，还是这样比较好……"
            scene black with dissolve
            scene bg_buildingoutside with moveinright
            by eye_def o "班长。"
            show wfimg o at char_mid with moveinleft
            wf "啊！你那边聊完了是吗？那温心……"

    hide wfimg
    show wfimg at char_mid
    by eye_move e "其实我也不知道……"
    hide wfimg
    show wfimg o at char_mid
    wf "啊？"
    by eye_move o "就是，呃……我跟她不是一起的……所以我也不知道她的情况……"
    hide wfimg
    show wfimg eye_sad o at char_mid
    "卫锋难以置信地张大嘴巴，呼出的白气令脸上被吹出的红晕更加明显。"
    wf "什么？那其他人呢，你可以问到情况的吧。"
    hide wfimg
    show wfimg eye_sad at char_mid
    by eye_def o "我没问啊。"
    hide wfimg
    show wfimg o at char_mid
    wf "去过医院，应该有记录，你现在问也来得及呀。"
    hide wfimg
    show wfimg purse at char_mid
    wf "或者，你告诉我办法，我自己去问就可以。"
    by "我真不知道……"
    hide wfimg
    show wfimg eye_still o at char_mid
    wf "是因为觉得太麻烦嘛？这样不好吧，我们不能因为事情难就这么容易放弃啊。"
    wf "很多事情只是看起来难，真正开始做之后就会发现其实也可以接受的。"
    hide wfimg
    show wfimg purse at char_mid
    by eye_still def "……"
    me "要不你找个别的话题糊弄过去？"
    by eye_wacky e "{size=23}你倒是提供一个啊……{/size}"
    "白一咬牙切齿，细微的声音仿佛从喉咙里挤出来一般。"
    me "问她跟温心相关的其他人？"
    by eye_still o "{size=23}噢，啊……{/size}"
    by eye_def o "要不你问问其他人，比如跟温心关系好的人啊，他们说不定会知道。"
    by eye_def def "我跟她又不熟，真的不清楚那天之后的事。"
    hide wfimg
    show wfimg eye_sad o at char_mid
    wf "可跟她关系最好的就是我啊……噢，不对……{size=23}说不定那个霸凌的人又影响她了。{/size}"
    hide wfimg
    show wfimg eye_still o at char_mid
    wf "嗯，我知道了！那白一同学你也去找医院的人问一下吧，之后我再找你！谢谢！"
    hide wfimg
    show wfimg at char_mid
    by eye_wacky def "喂……"
    "白一刚想开口，然而卫锋却没给她更多机会。"
    hide wfimg with moveoutleft
    "她双手合十，有些夸张地作了个揖，而后不等白一再说什么就离开了。"
    "白一长长地吐了口气，放在口袋里的手也松了力，没再紧紧捏着裤子。"
    by eye_wacky o "……谁答应她了？"

    scene bg_canteen with Fade(0.5,0.8,0.5)
    "食堂里人声鼎沸，伴随着萦绕四周的温热空气。"
    "白一绕过人群，端着饭盘走到最角落的位置坐下。"
    "周围三三两两吃饭聊天的人很多，即使发出点声音也不引人注意。"
    "她放下餐盘，便急不可耐地小声抱怨起来。"
    by eye_close o "靠，我真的服了，没想到那天去的人是班长。"
    by eye_wacky e "温心家是菜市场吗？怎么大家都想去。"
    by eye_still e "我不知道为什么去了，有个不知道存不存在的凶手去了，后来班长也去了。"
    by eye_close o "靠，有毛病啊。"
    me "……想开点，说不定卫锋知道你为什么去呢？"
    by eye_still e "那我难道直接问她？就说——"
    by eye_def o "啊你知道我上周为什么去温心家了吗我自己好像不记得了耶。"
    by eye_close e "呵呵，别人怕不是会以为我是精神病。"
    me "……"
    "说得好像很有道理。"
    by eye_def o "而且这么不自然，万一被人注意到了怎么办，不是说要小心的吗。"
    "她恶狠狠地把红烧冬瓜倒在米饭上，用力搅合在一起，一口又一口。"
    me "说起来，你好像面对她的时候，很——克制？"
    "我本来想说“怂”，但……有些过分。"
    "不过，那时候确实是和她现在这一边吃饭一边碎碎念的样子有天壤之别。"
    by eye_shock o "噗——咳咳……"
    "听到我的话，白一立马被饭呛到，咳得厉害，好一会才停下。"
    by eye_move e "你说得倒也没错……我真的不想跟她说话，不对，不止是说话，我不想跟她有任何联系。"
    me "哇哦。好严重的指控啊。"
    by eye_move o "高一的时候我跟她做同桌，有一次说脏话被听到，被她训了三天。"
    by eye_move e "说什么“不要因为一时的刺激去做一些自认为很酷的事”，“要对自己负责”，“年纪小也不能肆意妄为”……"
    by eye_close o "我靠，什么鬼，说得好像她不是十几岁一样？"
    by eye_wacky e "太可怕了，她见到我就要念叨一番，还差点想管我写不写作业，而且她那种好学生让老师都听她的，简直太可怕了好吧。"
    me "噗……"
    me "那你还，挺……识时务的。"
    "我自认中肯地评价，换来白一的两声冷笑。"
    by eye_wacky o "这还用你说？"
    me "好吧，那，你不想跟她说话，怎么办？"
    by eye_def o "什么怎么办？"
    me "不是要查温心的事情吗……她似乎是你现在唯一能问的人。"
    by eye_wacky def "……靠啊。"
    by eye_still e "可是真不能问她……我说不记得肯定会被怀疑的，而且她还那么执着于温心的事，被缠上更麻烦了。"
    by eye_close o "当然，主要是我也不想跟她说话。"
    by eye_def o "真是搞不懂，那么在意就自己去想办法啊，缠着我算什么……"
    me "嗯……"
    by eye_move e "哦，对了。{size=23}她好像提到有人霸凌温心来着。{/size}"
    "说到这，白一的声音放得更低了，吃饭的动作也慢下来。"
    me "噢，对，她刚刚好像有提到……"
    me "不过，霸凌……真有这种事吗？"
    by "呵呵，不然呢？你不会不相信吧？"
    me "只是觉得可能没那么常见。"
    by "这种事常见才是正常的好吧。"
    "你太悲观了……我想这么说，但还是没说出口。"
    me "如果真的是霸凌，那那个人应该很讨厌温心吧。"
    by "也就是说，相当有作案动机咯？"
    me "嗯。"
    by "很好。那么……那个人是谁呢……"
    menu:
        "问老师":
            me "要不你问问老师……"
            by "……你是脑干缺失吗？老师怎么可能会管这种事。"
            me "不会吗？"
            by "要是会的话，我们就不会听说有这件事了。"
            me "……那？"
            by "问老师还不如问别的同学，又不是只有班长一个人。"
            me "噢……比如温心的同桌？"
            by "嗯。"
        "问同学":
            me "不能问卫锋，那找其他同学问一下也可以的吧。"
            by "问谁？"
            me "比如……她同桌？"
            by "哦……可以试试。"
            by "所以又要去找人咯？还是连续找人。"
            me "嗯。"            

    by eye_close o "……哦。"
    by eye_move e "呃啊——真受不了，想不到我的校园生活还能用“繁忙”来形容。"
    me "这也没办法，毕竟……"
    "毕竟她被我缠上，连生命都有三个月为期的危险。"
    "不知为何，我并不想明确地说出这些话，因而话音停留在嘴边，又被收了回去。"
    by eye_close o "你说的我知道，就是烦啊……也不知道能问出个什么鬼。"
    "盘子里的饭剩下最后一口，白一全数塞进嘴里，从座位上站起来。"
    by eye_def o "唉，走了，找人，然后下午还要经历上课的摧残。"


    scene bg_schoolcorri with Fade(0.5,0.8,0.5)
    "白一盯着写着高二七班的牌子，躲开不断走进走出的人，迟迟没有新的动作。"
    "好一会儿，她才把目光从班牌转到后门口，提腿走近。"
    by eye_def def "{size=23}待会记得提醒我说话。{/size}"
    me "……噢。"
    by eye_def o "请问，你们班……姒舞在班上吗？"
    stuA "在在，你是找她吗？我帮你叫她出来？啊，或者你直接进去也可以的。"
    by "那麻烦你帮我叫一下她吧……"
    stuA "好哦，你等一下下哦。"

    scene bg_schoolcorri with fade
    show swimg o at char_mid with moveinleft
    sw "诶？你好……？"
    hide swimg 
    show swimg smile at char_mid 
    sw "是你叫我出来的吗？"
    by eye_def o "啊，对。"
    me "是她，姒舞。"
    "浅色的头发有些散乱地洒在肩膀后侧，显得眼前的少女格外有活力。"
    "她就是问过温心同桌之后知道的，和温心交流比较多的人。"
    hide swimg 
    show swimg o at char_mid 
    sw "噢，好！不过……抱歉我好像没有印象……你是谁？找我有什么事情吗？"
    by eye_def o "嗯，你应该不认识我。不过我找你是想问点事情。"
    hide swimg 
    show swimg eye_squint laugh at char_mid 
    sw "这样啊，难怪！好说好说，你问吧，我尽量回答~"
    hide swimg 
    show swimg eye_squint smile at char_mid 
    "对于白一找上门来，说了一番可以称之为奇怪突兀的话，姒舞的反应非常良好，甚至可以说好得过了头。"
    "以至于白一愣了一瞬间，过了一会才找回自己的声音。"
    by "想问一下……你认识温心吗？"
    hide swimg 
    show swimg at char_mid 
    "瞬间，姒舞的笑容僵住。"
    hide swimg 
    show swimg eye_sad smile at char_mid 
    "她抽了抽嘴角，无奈地扯出一个笑容。"
    hide swimg 
    show swimg eye_blink o at char_mid 
    sw "好吧，原来是这个……那我们换个地方说吧？"

    scene bg_buildingoutside with Fade(0.3,0.5,0.3)
    "一缕凉风卷起，白一伸手提了提衣领，盖住自己的半张脸。"
    by "{size=23}靠……好想骂人……{/size}"
    me "你这不是已经在骂了吗？"
    by "{size=23}烦死了，为什么都喜欢到外面说话啊，不嫌冷吗，有毛病……{/size}"
    show swimg o at char_right with moveinright
    sw "你说什么？"
    "姒舞走到角落停下，转过身，有些奇怪地看着白一自言自语。"
    by eye_move e "噢，没，你听错了。"
    show swimg o at char_mid with moveinright
    sw "好吧，所以你有什么关于温心的问题？直接问吧？"

    
    # 【和温心的关系】
    by "你看起来知道很多温心的情况，你和她很熟悉是吗？"
    sw "嗯……算是吧？我偶尔会让她帮我做点事这样。"
    sw "因为不在一个班，要说特别熟的话也没有，但就还可以吧。"
    by "所以你们相处得挺好的？"
    sw "嗯，对呀，挺好的。"
    by "……总觉得很奇怪。"
    # 【温心上周发生的事】
    by "看起来你认识温心，那你有注意到她上周做了什么吗？"
    sw "啊？这也太宽泛了吧……就算是我同桌，我也不可能知道她做的每件事啊，温心跟我还不是同一个班的呢。"
    by "就是，有没有做什么会让你注意到的，和平时不一样的事？"
    sw "没啊，我都这么说了，当然是没有嘛。和平时一样，很早来学校，下课也很早走。"
    sw "噢，不过最近好像没那么早走了，不过就一点点。"
    "她用夸张地用两根手指比了个手势，随后放下，耸了耸肩膀。"
    by "一点点……好像什么也不能说明。"
    # 【对问问题的想法】
    by "话说……我这么过来问你，你不觉得奇怪吗？"
    sw "不奇怪啊。你自己找我为什么要这么问？"
    sw "噢，所以你不知道我是谁嘛？"
    by "姒舞啊。"
    sw "不不，不是说名字。"
    by "啊？"
    sw "我啊——社交小天才，八卦小能手，育才小神通！"
    by "……"
    "白一罕见地呆住，似是怀疑自己所听到的话。"
    by "你……"
    by "这种情况多久了？"
    by "我好像听说过……青春期的时候，有些人会觉得自己很特别，会做一些，和别人不一样的事。"
    sw "……我才不是中二病！只是想跟你解释一下而已！"
    sw "哼，明明是你找我，现在还说这种话。"
    by "噢……嗯，好。"
    "几个不痛不痒的话题说完，白一陷入短暂的沉默。"
    "而后，她像是决定了什么，重新开口。"
    by "你平时……经常霸凌温心吗？"
    sw "……哈？！"
    "不想试探什么，直接问吧——白一大概是这么想的。"
    "而效果也很明显：姒舞瞪大了眼睛和嘴巴，表情十分夸张，像是完全不敢相信发生了什么。"
    sw "原来如此……难怪你要来找我！"
    sw "拜托，我又要解释一遍……我没有啊！"
    by "又要是什么意思？"
    sw "对啊，你们班班长也来问过一遍，就在不久之前。"
    "姒舞撇了撇嘴，一副十分不爽的表情，最后无奈地叹了口气。"
    by "说明你确实很可疑。"
    sw "什么叫可疑啊！"
    by "你不是说经常让她帮忙吗？就是强迫她做事？"
    sw "才没有！只是字面意思上的帮忙，而且她也愿意的啊。"
    by "呵呵，强行自愿的事情多了去了。"
    by "你认识那么多人，估计有个小团体吧，你们要是合起伙来强迫，难道还能拒绝？"
    sw "我是有，但……干嘛把别人都想得这么坏啊！"
    "姒舞气鼓鼓地瞪着白一，白一没反应，只是冷冷地看回去。"
    sw "她……我……"
    sw "她——"
    "姒舞深吸一口气。"
    sw "她之前在厕所没有卫生巾被我遇见了我就给了她一张后来发现她经济条件不太好所以有时候会借口让她帮我买东西顺便把买的东西送她一点"
    sw "然后……事情就是这样。"
    sw "我才没有霸凌……真要说那明明是隔壁——呸呸……"
    "她不满地嘟了嘟嘴，一边小声嘟囔着什么一边从兜里掏出手机。"
    "手指对着屏幕划了几下，朝着白一的方向展示。"
    "屏幕上是一段聊天软件的记录，看起来是姒舞和她另一个朋友的对话。"
    "“/表情包-喂”"
    "“喂，人呢？不会又去找温心了吧。”"
    "“对，刚好给她送一点东西。”"
    "“真能行吗？这么频繁，不会被她发现吧。”"
    "“不会，她是好人，只要说是帮忙就不会多想。”"
    "“/表情包-无语”"
    sw "喏……就是这样，够解释了嘛？"
    by "……"
    by "你们真的没有霸凌？"
    "明知道是废话，但白一还是脱口而出。"
    sw "对呀！"
    by "所以……你的意思是，其实是同学之间的互帮互助？"
    sw "对呀！"
    sw "这还不够明显嘛？对了，你去问温心呀，问我有没有欺负她嘛。"
    by "……"
    "白一对此保持沉默。"
    "这一次，她沉默了很久，最后也只是用粗劣的话语搪塞话题的结尾。"
    "白一和温心并不熟悉，不如说几乎是陌生人，只是刚好同在一个班上学而已。"
    "自然，也没有多余的心神去考虑她的事。"
    "直到此时此刻，白一才开始“感知”到她的死亡。"
    "一个人的死亡意味着什么？"
    "无法被看到。"
    "无法为自己说话。"
    "无法再做到任何事。"
    "最后……彻底消失在这个世界上。"
    me "话说，你有注意到她当时没说完的话吗？"
    by "啥玩意？"
    me "说到霸凌的时候，说隔壁什么的……"
    by "……"
    by "那都无所谓吧。"
    me "啊……只是稍微有点好奇。"
    by "那你好奇着吧……我对其他人的事不感兴趣。"
    me "温心也算其他人吗？"
    by "……你是白痴吗？"
    by "我现在在这里做这些麻烦事，只是因为我……不，只是因为西顺要我这么做而已。"
    by "至于其他人，当然跟我没有任何关系。"
    return