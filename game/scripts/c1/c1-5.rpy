label c1_5:
    $ quick_menu = False
    window hide
    scene bg_buildingoutside with Fade(0.5,0.8,0.5)
    show screen tpoinfo("12月20日，星期一","丰宁二中") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    show tophalfblk with dissolve
    window show
    $ quick_menu = True
    by eye_squint o "哈……啾！"
    "白一胡乱地抹了鼻子几下，有些不爽。"
    by eye_still e "靠，都好几天了，感冒怎么还没好，鼻子都要被擦烂了。"
    me "的确……有点痛。要不你再多穿点？"
    "我跟着吸了吸鼻子。"
    by eye_close o "已经很多了啊，再叠就穿不上校服外套了。"
    by eye_def o "而且室内有些地方温差大容易出汗，到时候更冷了。"
    me "好吧……"
    by eye_def e "要我说最好的解决方式就是不上学。"
    by eye_def o "在家待着就什么事都没了，是吧？"
    me "呃……嗯。"
    by eye_close o "所以说啊——"
    scene black
    show bg_buildingoutside with vpunchm
    sw "白一！"
    "肩膀突然从后面被人拍了一下，白一整个人都打了个激灵，差点就要原地跳起来。"
    show cg_sw01 at cg0 with dissolve
    "回过头，果不其然是一脸笑意的姒舞。"
    show cg_sw00 at cg0
    hide cg_sw01
    sw "早啊~白一~"
    by eye_def o "……早。"

    show bg_buildingoutside with fade
    hide swimg
    show swimg o at char_mid with dissolve
    sw "对了，刚刚好像听见你在跟谁说话？你刚刚在说什么呢？"
    hide swimg
    show swimg at char_mid
    by eye_move e "……呃，刚刚有个电话。"
    "没想到会在上学路上偶遇，白一顿住，用手指了指耳朵上挂着的耳机。"
    me "噗……没想到耳机还真的派上用场了。"
    "我忍不住笑了出来，被白一在兜里掐住了手指。"
    by "{size=23}……滚啊。{/size}"
    hide swimg
    show swimg o at char_mid
    sw "啊？这样啊，不好意思不好意思……"
    by eye_move o "不……没事，打完了。"
    by eye_def o "所以你又有什么事？"
    hide swimg
    show swimg smile at char_mid
    sw "没有啊，这不是看到你，来打个招呼嘛。"
    hide swimg
    show swimg eye_blink smile at char_mid
    sw "对了对了，你看我们这么有缘，干脆就交换个号码呗~"
    by eye_still e "嗯……好啊。"
    me "等等，你不会真的想查她的手机号吧。"
    "白一从喉咙里发出极其轻微的哼声，我知道我大概猜对了。"
    hide swimg
    show swimg o at char_mid
    sw "就算不——咦？你同意啦？"
    hide swimg
    show swimg smile at char_mid
    "姒舞惊喜的表情不似作伪，以至于白一都有些迟疑。"
    "白一自认自己是个毫无优点，也十分无趣的人，对于太过主动热情的姒舞，不得不觉得奇怪。"
    by "所以你为什么非要找我？"
    hide swimg
    show swimg eye_squint smile at char_mid
    sw "因为你没朋友啊。"
    by eye_shock def "？？？"
    me "……这是可以直接说的吗？"
    hide swimg
    show swimg o at char_mid
    sw "啊……不好意思，我不是那个意思啦。"
    hide swimg
    show swimg eye_squint o at char_mid
    sw "好吧，其实也有点那个意思……"
    by eye_wacky def "？"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "就是……我有点讨厌你们班的一个人，但你和班上的人好像关系都不好。"
    hide swimg
    show swimg eye_squint laugh at char_mid
    sw "所以……敌人的敌人就是朋友！你懂的！对吧？！"
    by eye_wacky def "……"
    "关于姒舞异常的热情，在这之前，白一其实私下阴谋论了好几回。"
    "但她完全没想过，最后姒舞给出的是这样一个有些……令人无语的回答。"

    scene bg_canteen with Fade(0.5,0.8,0.5)
    by eye_def o "我感觉，好像可以不用让西顺查姒舞的手机号了。"
    "食堂，咽下一口饭后，白一突然开口。"
    me "嗯？为什么突然说这个。"
    by eye_still e "我感觉她好像没有脑子。"
    by eye_close o "不，不对……怎么说，应该说脑子里都是八卦？"
    by eye_def e "看起来不像是会做出杀人这种事还能隐瞒过去的人。"
    me "噗……"
    "虽然刚刚认为姒舞说话很直接，但现在看来，骂人的话似乎还是白一更擅长。"
    by eye_close o "算了，拿都拿到了，给西顺发一份好了。"
    by eye_close e "反正工作的不是我。"
    "白一理直气壮地说着，快速敲打手机键盘，把姒舞的电话号码发了过去。"
    scene bg_canteen with fade
    me "话说，姒舞说的，讨厌你们班的人，是谁呀？"
    by eye_def o "嗯？就是天玉啊。"
    me "我知道……她说过名字了。"
    by eye_still o "那你还问我？"
    me "……我的意思是，她具体是什么样的人，之类的……不是问名字啊。"
    by eye_still def "哦……那你说清楚点啊。"
    "白一毫不犹豫地把问题推在我身上。"
    by eye_def o "天玉啊，她在班上挺活跃的，人缘也好。"
    by eye_move e "嗯……班长是老古板好学生的话，她像是那种，呃，活泼可爱的好学生。"
    by eye_def o "不过你怎么突然问这个？其实我跟她也不熟，只知道这些。"
    me "啊，就是有点好奇……是怎样的人，让姒舞讨厌到甚至跟你交朋友。"
    by eye_still e "……什么叫“甚至跟我交朋友”？"
    me "就是很难得的意思。"
    by eye_still def "嘁……"
    by eye_def o "不过，这么说姒舞找我确实没问题，我应该是班上少数跟天玉毫无关系的人……"
    me "所以她为什么讨厌天玉？"
    by eye_close o "我怎么知道？谁管她啊。"
    "白一摇摇头，满不在乎。"
    "而后，她又像想到什么似的，提起另一个话题。"
    by eye_def e "说起来……天玉她好像也算长头发。"
    me "……你特意说一句这个，该不会是在怀疑她吧。"
    by eye_def o "嗯，不可以吗？"
    by eye_close o "随便问问呗，理论上，我还可以怀疑学校里所有长头发的人。"
    me "你怎么不干脆把这个市里的人都怀疑一遍……"
    by eye_still def "……"
    by eye_def o "那倒不至于，凶手总不至于是校外的……温心平时就每天在家和学校两处跑而已。"
    me "……我在学你吐槽。"
    "结果白一竟然一本正经地跟我解释。"
    by eye_close o "废话，我当然知道。难道我要等着被你吐槽吗？"
    me "……"
    "好吧，我想我大概是说不过她。"
    "白一吃完饭， 端着盘子从座位上站起来。"
    "顿时，周边几桌的人都投来了似有似无的打量视线。"
    "吃过饭的好心情消失了，白一用力捏紧了餐盘，快步收好，赶紧离开了食堂。"
    
    scene bg_buildingoutside with Dissolve(1.5)
    by eye_wacky e "靠，我感觉我像是动物园的猴子。"
    me "嗯……可能还是因为那个谣言吧，还没过去多久。"
    me "不过西顺不是说会找人帮你的吗。"
    by eye_move o "我才不相信她的话，劝你也别相信。"
    me "这……"
    by eye_def e "不过，就算她真的去做，有用就有鬼了。"
    me "……啊？"
    by eye_move e "谣言要是能被轻易解决，就不会传成现在这样……"
    by eye_def def "而且被传的人还是我。"
    by eye_close o "好吧……我瞎说的。不过，反正……大部分人都已经相信了吧，毕竟我本来就不受欢迎。"
    by eye_def o "就算之后说要澄清，大概率也是被无视或者不被相信之类的。"
    by eye_move def "嗯，大概吧。"
    "白一用最有自信的语气说出最丧气的话。"
    me "不至于吧……"
    by eye_close o "都说了我随便说的啊。"
    me "不，但是……那你看起来很了解，还说得这么头头是道的……"
    "难道是因为之前也经历过吗？"
    "我想问的问题差点就顺势脱口而出，但也只说出了第一个字就停住了。"
    "这实在不是适合我问的问题。"
    by eye_close smile "可能是因为我比较聪明吧。"
    me "……"
    "但她怎么还自夸起来了……"
    me "噢，这样啊……呃，那，就好……"
    by eye_still o "切，你那是什么语气。"
    by eye_squint def "但是被当猴子真的很烦啊，啊——"
    "白一有些抓狂地挠了挠头，又忍不住翻了个白眼。"
    by eye_wacky def "靠，算了，滚吧，都无所谓。反正我也没办法……"

    scene bg_classroom with Fade(0.5,0.8,0.5)
    "正如白一所想的那样，下午最后一节课下课后，班主任走了进来。"
    show zbimg o at char_mid with dissolve
    zb "最近，同学们的心有些涣散啊。"
    zb "学生的天职就是学习，你们要做的就是听老师的话，好好完成功课。"
    zb "父母把你们送来学校，不是让你们说八卦、搞小动作的。"
    hide zbimg
    show zbimg at char_mid
    zb "好了，放学。白一你跟我出来一下。"
    by eye_still def "……"

    scene bg_schoolcorri with Fade(0.5,0.8,0.5)
    show zbimg o at char_mid with dissolve
    zb "白一，老师不是不相信你……"
    "班主任以这句话开头的瞬间，白一就忍不住嗤笑了出来，只是没发出声音。"
    zb "但是呢，你要知道，咱们这个班是一个集体，你不能只想着自己，要为集体着想。"
    zb "他们接受过教育了，那么你也没必要继续激化矛盾。"
    zb "就像我说的，学校是学习的地方，不要做那些影响学习氛围的事。"
    by eye_still def "……哦。"
    zb "听懂了吗？别不说话，我们要交流。"
    by eye_move o "哦，知道了。"
    hide zbimg
    show zbimg at char_mid
    zb "你这样——唉，算了。"
    hide zbimg
    show zbimg o at char_mid
    zb "你啊……别影响别人学习就好。"
    "班主任看着白一，欲言又止，似乎是很失望似的叹了口气。"
    hide zbimg with dissolve
    "而白一仍然是没有什么反应，只是冷冷地看着班主任，直到她说完离开。"
    by eye_close e "啊……受够了。"
    me "你们班主任……为什么要找你说话？"
    by eye_move o "来教育我的吧。"
    by eye_still o "虽然其他人造谣我，但我可不能骂回去，不然影响不好。"
    by eye_close o "拜托，我还没开始骂好不好？"
    me "……不是应该处理你的谣言吗？"
    by eye_move e "呵呵，处理了啊，她刚刚不是说了。"
    "白一耸了耸肩，一副毫不意外也毫不在意的样子。"
    by eye_still o "反正就是警告大家要好好学习咯。"
    me "总感觉……是不是处理得有些敷衍？"
    by eye_close o "对啊，恭喜你领悟了真谛哦。真棒棒呢。"
    me "……好像没有什么可值得恭喜的。"


    $ quick_menu = False
    window hide
    scene bg_byroom1 with Fade(0.5,0.8,0.5)
    show screen tpoinfo("12月21日，星期二","白一的家") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    show tophalfblk with dissolve
    window show
    $ quick_menu = True
    show xsimg o at char_mid with moveinright
    xs "姒舞跟你说的那些解释大体上是没有问题的。"
    by eye_def o "啊。"
    xs "她的性子挺直，做事不太会瞻前顾后，所以也不会搞那种小动作。"
    hide xsimg
    show xsimg at char_mid
    xs "有时候跳脱一点，在学校让老师头疼，但没犯什么原则性问题。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "和温心的事也是真的，这孩子不知道从哪听的话，说直接给人打钱是在羞辱对方，所以想出这么个办法拐着弯的帮同学。"
    by eye_still def "……哦。"
    by eye_def o "所以你还是去查她咯？知法犯法？"
    hide xsimg
    show xsimg o at char_mid
    xs "你啊……这是重点吗？"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "我是有自己的方法，不是你想的那样。"
    by eye_def e "哪样？用权压人呗？"
    hide xsimg
    show xsimg at char_mid
    xs "你——"
    "滴滴滴，滴滴滴——"
    "手机的铃声打断了西顺即将说的话。"
    hide xsimg with moveoutright
    xs "抱歉，先接个电话。"
    by eye_def def "噢。"

    scene bg_byroom1 with fade
    xs "什么？为什么会出现这样的意外？"
    xs "嗯，是还在看之前的那件事。"
    xs "所以呢，局里没有其他人了吗？"
    xs "你说西平？不，她只能跟在我身边。"
    xs "之前说好的吧。"
    xs "……我知道。"
    xs "我会跟上进度去查，但是这边我也要查。"
    xs "好，我知道。"
    xs "嗯，会的。"
    xs "挂了，拜。"
    show xsimg o at char_mid with moveinright
    xs "抱歉让你等了啊。"
    by eye_def e "没……"
    hide xsimg
    show xsimg at char_mid
    xs "嗯，我们快点讲完吧。刚刚是说到……"
    by eye_def o "说到姒舞。"
    hide xsimg
    show xsimg o at char_mid
    xs "噢，对。不过，我想先跟你把刚才的话题讲清楚。"
    by eye_still def "……"
    hide xsimg
    show xsimg at char_mid
    xs "嗯……我并不否认，权力的确有很多好处。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "远的不说，就说现在。如果没有权力，我早就被开除了，你说是吧？"
    hide xsimg
    show xsimg o at char_mid
    xs "那样的话，我现在也没办法继续寻找真相，你的事情也会无疾而终。"
    xs "而——"
    by eye_wacky def "……哈？等等。"
    by eye_wacky o "所以你的意思是我是多么荣幸，能够承你的情咯？"
    by eye_wacky e "是不是还要对你感激万分才行？"
    "这样的话似曾相识，白一之前也说过，现在仍然是同样的毫不留情。"
    "被打断话语，西顺也有些无奈，但也如之前一般否定了白一的想法。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "我并不是那个意思。"
    hide xsimg
    show xsimg o at char_mid
    xs "只是想说，我没有能够通天的权力改变一切，只能尽力在自己的范围内做好。"
    xs "我不知道你为什么对我有意见……也许就是因为这个。"
    xs "我没办法改变你的想法，但是，在你的事情上，我和你的目的是相同的，我也至少不会因为权力害你。"
    xs "所以，至少，我不希望每次跟你交流，都要浪费一段时间在针锋相对上。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "这样，我解释得够清楚么？"
    hide xsimg
    show xsimg o at char_mid
    xs "最多三个月，我们保持心平气和地说话，可以么？"
    by eye_move def "……"
    "白一移开视线，不去看西顺。"
    "好一会，她才闷闷地应声。"
    by eye_move o "哦……知道了。"

    scene bg_byroom1 with fade
    show xsimg o at char_mid with dissolve
    xs "嗯，好，那我们回到刚刚的话题。"
    hide xsimg
    show xsimg o at char_mid
    xs "就目前的情况，姒舞基本可以排除嫌疑，这一点上没有问题吧？"
    by eye_def o "我知道，其实我是大概相信她的话的。"
    by eye_move e "她……就是那样。"
    "双手无声地绞紧了手指，白一轻叹了口气，说不清自己是什么心情。"
    hide xsimg
    show xsimg smile at char_mid
    xs "嗯，你可以跟人家多学学啊，或者打好关系也不错。"
    xs "人家在学校社交圈可广了，指不定就能帮上什么忙是不是？"
    hide xsimg
    show xsimg at char_mid
    by eye_still def "……"
    by eye_close o "跟她谈不来。"
    hide xsimg
    show xsimg o at char_mid
    xs "好吧好吧，只是建议。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "那，既然现在是这样……就先不继续查姒舞的事了，把时间放在别的地方。"
    xs "不过你平时也可以顺便关注一下，她说的温心的事情让我有些在意。"
    by eye_def o "啥？"
    xs "记录显示，姒舞的确经常用帮忙的方法给温心送日用品，但是，她似乎并不知道温心前段时间生病的事。"
    by eye_def e "所以？"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "嗯，如果是这样，那温心家里的药跟她没关系。"
    hide xsimg
    show xsimg at char_mid
    by eye_def o "不是说了温心的事跟姒舞没关系吗，没关系不是很正常？"
    by eye_still o "哦……你的意思是。"
    jump c1_5_choice1
    return

label c1_5_choice1:
    hide xsimg
    show xsimg at char_mid
    menu:
        "姒舞在说谎":
            by eye_def o "你是说，姒舞其实知道她生病，只是在骗你？"
            hide xsimg
            show xsimg eye_close o at char_mid
            xs "不……这件事我找其他人证实过，姒舞应该没有说谎。"
            hide xsimg
            show xsimg o at char_mid
            xs "她确实不知道温心生病。"
            by eye_def o "那……"
            jump c1_5_choice1
        "温心的药的来源有问题":
            by eye_def o "你是觉得，如果温心的药不是姒舞送的，就很奇怪？"
            jump c1_5_extra
    return


label c1_5_extra:
    hide xsimg
    show xsimg eye_close at char_mid
    xs "嗯……"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "温心这个人……我不确定，也没有证据，所以只是猜测。"
    hide xsimg
    show xsimg o at char_mid
    xs "你觉得，她平时感冒生病，会去自己买药吃吗？"
    by eye_def o "我不知道啊……学校不是有校医室吗？"
    hide xsimg
    show xsimg at char_mid
    xs "你去过校医室吗？"
    by eye_def o "没有啊。"
    hide xsimg
    show xsimg o at char_mid
    xs "据我所知，你们学校的校医室基本上只处理一些简单的外伤，还有做检查开请假证明。"
    xs "具体的药是不会开给学生的，因为容易惹出麻烦。"
    hide xsimg
    show xsimg at char_mid
    by eye_still def "啧……"
    by eye_close o "那谁知道啊。"
    by eye_def o "是不是别人给的药很重要吗？又不是到她家里给的。"
    hide xsimg
    show xsimg o at char_mid
    xs "现在没有别的线索，只能用最原始的办法，一个个找温心的社会联系。"
    xs "找到这些跟她有过联系的人，再去细查，一个个排除。"
    by eye_still o "好麻烦……"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "是啊，而且效率还很低……但没办法。"
    by eye_still def "……"
    hide xsimg
    show xsimg eye_close at char_mid
    "西顺捏了捏鼻梁，难得的露出明显的疲惫之情。"
    "城安局的事情当然很多，电视节目上甚至经常以此为案例歌颂人性光辉，但落在真实的人身上的或许只有累。"
    "白一没有任何立场和资格评价什么，但，只是……"
    "只是……也好像被这份疲惫影响了一样。"
    by eye_move o "那就……慢慢来吧……慢慢找。"
    hide xsimg
    show xsimg o at char_mid
    xs "嗯？你不着急？"
    by eye_move o "……反正……我和温心不熟。"
    by eye_close o "我没良心，不在乎呗。"
    hide xsimg
    show xsimg eye_still o at char_mid
    xs "我是说你自己。"
    by eye_close e "……那，不是还有三个月吗。"

    
    $ quick_menu = False
    window hide
    scene bg_classroom with Fade(0.5,0.8,0.5)
    show screen tpoinfo("12月24日，星期五","丰宁育才中学") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    show tophalfblk with dissolve
    window show
    $ quick_menu = True
    by "嘶……"
    by "感觉，我现在什么别的都不想考虑了。"
    "看着发下来的资料，白一倒吸一口凉气。"
    me "怎么了。"
    by eye_still e "这才是现在最大的困难，其他的都滚一边去。"
    "她用手指了指白纸上的黑字，大标题“丰宁育才中学年度体质测试”。"
    "手指又向下划，到中间的某一行。"
    "跑步：1000米。"
    by eye_still o "去年还是800米的，今年又加了……"
    by eye_wacky e "这种大冷天，别说1000，800我都不想跑……"
    "她的声音幽幽传来，带着快要断气的感觉。"
    by eye_still o "你能不能帮我跑啊？"
    me "……你又开始异想天开了。"
    by eye_close o "呵呵呵……要不是你太没用，我就不会只是想想了。"
    me "……"
    me "你要这么想，虽然我不能帮你跑，但我也会陪你受苦的。"
    "毕竟她的感知就是我的感知，这么说，可不是陪着嘛……"
    by eye_wacky o "那还真是谢谢你啊。"
    "白一翻了个白眼，把通知用力揉成团，塞进背包。"

    scene bg_playground1 with Fade(0.5,1,0.5)
    "无论怎么咒骂，该来的事情还是躲不掉。"
    "上午的天空依然阴沉，厚厚的灰云堆积在操场的上空，让人有种憋闷的感觉。"
    by eye_move e "{size=23}快点下雨……快点下暴雨……{/size}"
    "白一站在班级队伍的最后，嘴里不断地小声碎碎念。"
    me "你这是在祈祷吗，人形求雨娃娃？"
    by eye_wacky e "{size=23}滚啊……不能帮我就别在这说话。{/size}"
    "不知为何，她的神经过分紧绷，就像被拉到再也不能伸长的弦，再稍微用力就会爆掉的那种。"
    me "呃……嗯……"
    me "可我跟你说话，你就可以骂我，不会让你更爽吗？"
    by eye_wacky def "……"
    by eye_wacky o "我看起来像那种变态吗？"
    "……难道不是吗？"
    "我实在很想这么说，但还是没说出口。"
    me "呃……大概？"
    by eye_wacky e "你……呵呵，好吧。"
    "白一深深吐了口气，然后无语地笑了。"
    by eye_wacky e "我觉得，你愚蠢的发言确实把我逗笑了……"
    by eye_close o "呼……我要，放松……"
    "看到她平静下来，我也松了口气。"
    "实不相瞒，刚才我差点就要被那高度紧张的精神压垮了。"
    "只是，或许是因为身体跟着用力，放松下来后，有种四肢发麻的感觉。"
    "直到白一慢悠悠跟着做完跑步前的伸展运动，也没能让手脚多一些力气。"
    teacher "……下一组……白一……"
    scene bg_playground2 with dissolve
    "听到自己的名字，白一打了一个激灵，赶忙上前，站到操场的跑道上。"
    "{size=45}砰——{/size}"
    "发令枪响，脚步声也跟着迅速响起。"
    scene black with dissolve
    "白一缀在一行人的最后，很快就拉开了差距。"
    show bg_playground1 with shaking
    "第一圈——"
    by eye_still def "嗯……"
    "第二圈——"
    by eye_close o "哈……啊……哈……"
    "第三圈——"
    by eye_close e "呼……呼……"
    "第四圈——"
    by eye_squint def "嘶……"
    "学校的操场是二百米一圈的长度，一千米也就是要跑五圈。"
    "到第四圈的时候，白一已经连喘息的声音都快要发不出。"
    "频繁的换气动作后，只有少得可怜的气流从齿缝间泄露。"
    "喉咙像被粗糙的砂纸划过，充满铁锈味的腥气源源不断涌上，令人想要呕吐。"
    "四肢格外沉重，手臂几乎要抬不起来，只能靠手指攥住上衣的布料保持不成型的动作。"
    "落地格外艰难，每一次脚落地时都几乎快要撑不住，软倒在地。"
    show bg_black with dissolve
    pause 0.2
    hide bg_black with dissolve
    "刷——"
    "白一再次被人从后面超过。"
    "但，这个身影是……"
    "虽然她就在不远的前方，但已经是在第五圈了。"
    "意识到这一点之后，白一有些着急。"
    "再这么慢的话，也许就要超时不合格了……"
    "想到这里，白一咬紧了牙关。"
    "全身紧绷，从头顶的发丝到脚尖都开始拼命用力。"
    "跑，再用力一点，跑……"
    "左脚落地，右脚再落——"
    scene black with vpunchm
    "——咚！"
    show bg_playground2 with vpunchm
    "砰！！"
    by eye_squint def "呃……！"
    unknown "啊！！"
    unknown "诶——？！！"
    "只是一瞬间发生的事。"
    show bg_black with dissolve
    hide bg_playground2 
    pause 0.2
    show bg_playground2 
    "眼前的景象开始变得模糊不清。"
    "疼痛与酸胀从身体各处升起。"
    "下一秒，白一失去了意识。"
    return