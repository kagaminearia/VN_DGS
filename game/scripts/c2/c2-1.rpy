label c2_1:
    $ quick_menu = False
    scene black with fade
    show white with w19
    pause 0.1
    hide white with dissolve
    $ quick_menu = True
    "一缕光线穿过黑暗。"
    scene bg_schoolmedical with sunshine
    "而后，视野闪了闪，逐渐变得明亮起来。"
    by eye_still o "……嗯？什么情况……"
    "白一晕晕乎乎的，摸索着直起身子。"
    by eye_still e "等等，总觉得这个场景好像似曾相识……靠。"
    "又是晕过去，又是在别的房间醒来。"
    me "嗯……你之前又晕倒了，现在还好吗？"
    by eye_close e "还行，就是感觉全身都好酸痛啊……怀疑有人在我睡觉的时候偷偷揍我。"
    unknown "白一你醒了？"
    me "……还有其他人在？"
    "白一说话的声音立马止住，她眨了眨眼睛，装作什么都没发生，刚醒过来的样子。"
    "很快，刚才发出声音的对象就走到了白一身旁。"
    show tyimg o at char_mid with moveinleft
    ty "白一，你还好吧？现在都下午了，我还以为你要睡一天呢，吓死我们了……"
    "来人是前不久才讨论过的主角，天玉。"
    "是她出现在眼前，这让白一愣了一下才反应过来。"
    by eye_def o "啊，嗯……所以是怎么回事？"
    by eye_def o "我怎么晕了，睡了多久？"
    hide tyimg
    show tyimg o at char_mid
    ty "你在一千米测试的时候好像脚滑，跟前面的梁绵绵撞一起了。"
    hide tyimg
    show tyimg at char_mid
    ty "然后你们都摔倒在地上，你就晕过去了。"
    by eye_shock o "……撞，撞到人了？"
    hide tyimg
    show tyimg o at char_mid
    ty "嗯，不过她没晕过去，就是腿擦伤了。"
    hide tyimg
    show tyimg smile at char_mid
    ty "你要是觉得不好，再买点药送给她就行。"
    by eye_still def "噢……"
    hide tyimg
    show tyimg eye_sad o at char_mid
    ty "所以你呢，有没有哪里不舒服？还能动吗？"
    by "好像……还行。"
    "白一试着坐起来，动腿下床。"
    "脚触地的一瞬间，似乎还有些提不起劲，好在她抓紧了单人床的床柱，免于再次摔倒。"
    hide tyimg
    show tyimg eye_squint o at char_mid with vpunchs
    ty "唉等等……小心！"
    hide tyimg
    show tyimg eye_squint at char_mid
    "天玉赶紧扶住白一的肩膀。她满脸着急，看起来像被吓到了。"
    hide tyimg
    show tyimg eye_sad o at char_mid
    ty "你真的没关系吗？要不，我抱着你吧？"
    by eye_shock o "抱——{size=45}抱我？？！！{/sisze}"
    "白一声音提高，瞪大眼睛，表情比刚才的天玉还要惊恐。"
    hide tyimg
    show tyimg o at char_mid
    ty "对呀，怎么了？"
    hide tyimg
    show tyimg smile at char_mid
    ty "之前也是我抱你到校医室的呀。"
    by eye_squint o "噗——！咳咳咳……"
    me "哇，她原来这么厉害的吗。"
    "天玉个子不算矮，比白一高一个头左右。"
    "但她的身形看起来是修长纤细的类型，难以想象是怎么把一个将近成年的女性抱起来的。"
    "果然……该说不愧是人不可貌相吗……"
    by eye_shock def "不，不用了——我可以的。"
    "白一被吓得差点一个踉跄，话都差点说不利索了，但还是凭借惊人的求生欲稳稳站好。"

    scene bg_schoolmedical with fade
    by eye_move o "那个，之前谢了。"
    show tyimg smile at char_mid with dissolve
    ty "没事啊，我们是同学嘛，要互帮互助的。"
    by eye_still e "……我没事了，你回去吧。"
    hide tyimg
    show tyimg eye_sad o at char_mid
    ty "啊……真的可以么？"
    by eye_move o "当然。你现在应该回去上课吧。"
    hide tyimg
    show tyimg smile at char_mid
    ty "啊，这个呀，不用担心，我跟老师说过了。"
    hide tyimg
    show tyimg eye_squint smile at char_mid
    ty "我自己的话，空缺一两节课也没关系的。"
    "天玉温柔地笑着，脸上是一种类似“好学生的余裕”的自信。"
    by eye_still o "……真没事。"
    hide tyimg
    show tyimg smile at char_mid
    ty "好吧，听你的。那你要注意休息哦，腿的位置容易再伤到。"
    hide tyimg
    show tyimg o at char_mid
    ty "啊，对了——"

    scene bg_schoolmedical with Fade(0.5,1,0.5)
    by eye_close o "……哈啊！"
    "好不容易打发走天玉后，白一一屁股坐回了床上，带着床垫重重地弹跳了一下。"
    by eye_squint def "草，痛死我了。"
    me "我还以为你的痛觉神经被撞失灵了呢……"
    "明明腿那么痛，却还能面不改色地站着说话，我都有点佩服了。"
    "如果不是我也会跟着痛的话就更好了……"
    by eye_still e "那不然怎么办，难道真的让她来抱我走？"
    by eye_wacky o "不行，光是说出来就感觉要吐了。呕。"
    me "……"
    "我想象了一下那个画面，确实有些……难以形容。"
    me "腿现在怎么样了？"
    "白一撩起裤腿，露出红肿的膝盖和擦伤的小腿。"
    by eye_def o "还好，其实外面不是很严重。"
    by eye_still e "但……好像是因为我撞到那个人之后，她替我挡了一下。"
    by eye_still def "那她应该比我严重很多……"
    by eye_wacky def "草，完蛋了，我会不会被她的家长骂死。"
    me "有可能……但，那也……没办法……"
    "这事不管怎么说，白一都不占理。"
    by eye_move e "……还好还好，至少我家不会有家长骂我，最多只会被骂一次。"
    me "……你还挺会安慰自己的。"
    by eye_close def "嗯呢。"
    "虽然已经是下午，但还没到下课时间。"
    "校医室没有别人在，十分安静，白一干脆换了个舒适的姿势，靠坐在床上观察房间。"
    show black with dissolve
    pause 0.2
    hide black
    # 地图
    jump medical
    return
    
    

label c2_1_extra:
    scene bg_schoolmedical with Fade(0.5,1,0.5)
    $ quick_menu = True
    me "话说，老师去哪了？"
    by eye_def o "可能提前下班了吧，或者有事走了？或者吃饭了？"
    by eye_close o "随便啦，总归校医室也不实用的。"
    me "那……待会就这样走了？没关系吗？"
    by "没事，我只是看看，又没弄乱东西，走的时候记得关门就好了。"
    scene bg_schoolmedical with fade
    "铃——铃——"
    "下课铃声响起，结束了我跟白一在校医室内进行一圈的指指点点。"
    by eye_def def "啊，下课了，回家。"
    me "你的腿还好吗，不用再缓一会？"
    by eye_def o "没事啊，回家再休息一样的。"
    by eye_close smile "回家不积极，脑袋有问题~"
    me "……"
    "还是第一次听到白一用这种语气说话……甚至让我觉得，有些惊悚。"
    "看得出来她是真的很想马上回家……"
    show swimg o at char_mid with vpunchm
    sw "白一！"
    "正说着回家，不速之客——对于现在的白一来说——闯入了校医室。"
    hide swimg
    show swimg laugh at char_mid
    sw "啊太好了，你真的在这！"
    by eye_still o "……你又是要干嘛？"
    hide swimg
    show swimg o at char_mid
    sw "哎呀，我就是听说你受伤了，还很严重，都进校医室了，就想来看望你呀。"
    by eye_def e "你的消息还真够灵通的。"
    hide swimg
    show swimg eye_squint laugh at char_mid
    sw "那当然！我可是——"
    by eye_def o "停——打住。"
    "白一举起手臂，做了个中止的手势，把姒舞没说完的话都堵在了嘴里。"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "欸~~"
    hide swimg
    show swimg eye_blink at char_mid
    by eye_def o "所以，来看我干嘛？"
    hide swimg
    show swimg o at char_mid
    sw "我们不是朋友了吗？当然要来关怀一下啊！"
    by eye_still e "我们……难道是朋友吗？"
    hide swimg
    show swimg smile at char_mid
    sw "都交换过手机号码了，当然是啦。"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "啊！你该不会要赖账吧？要把我用完就扔掉了！"
    hide swimg
    show swimg eye_blink at char_mid
    by eye_wacky def "……"
    me "哈哈哈哈，她真有意思。"
    hide swimg
    show swimg at char_mid
    "难得看见白一吃瘪，我乐不可支地笑出了声。"
    by "{size=23}闭嘴啊。{/size}"
    "白一不太想继续搭理这个话题。"
    "她揉了揉太阳穴，只觉得现在的脑袋比腿还疼。"
    by eye_still e "嗯……那你看完了。"
    by eye_def o "哦对，有件事。"
    hide swimg
    show swimg o at char_mid
    sw "嗯？怎么啦？"
    by eye_def o "刚刚，天玉来找过我。"
    hide swimg
    show swimg eye_squint at char_mid
    sw "噫——"
    "姒舞顿时拧起了眉毛，做出夸张的嫌恶表情。"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "我知道，她抱着你过来的！干嘛呀要说她。"
    hide swimg
    show swimg eye_blink at char_mid
    by eye_shock e "噗——我不是说这件事……你怎么知道的？"
    "白一万万没想到还有自己被抱着的这码事。"
    hide swimg
    show swimg o at char_mid
    sw "啊？大家都看到了啊。"
    "姒舞眨了眨眼睛，似乎在疑惑白一的反应过度。"
    hide swimg
    show swimg at char_mid
    by eye_wacky def "……"
    by eye_close e "{size=23}算了，算了……{/size}"
    "白一长长地呼出一口气，努力把这件事情赶出自己的脑袋。"
    hide swimg
    show swimg eye_sad o at char_mid
    sw "啊啊——完了，你是不是也觉得她人很好，很不错？"
    by eye_def def "嗯？就……还行。"
    "白一没有犹豫，也没考虑姒舞的想法，只是实话实说。"
    "对她来说，不论是天玉还是姒舞，其实都没什么区别。"
    hide swimg
    show swimg eye_sad at char_mid
    "姒舞好像受了很大打击，嘴巴一瘪，发出哭唧唧的声音。"
    hide swimg
    show swimg eye_sad o at char_mid
    sw "呜呜，我就知道……我就知道！"
    hide swimg
    show swimg eye_sad at char_mid
    sw "为什么呀，为什么她总是比我还受欢迎呀……"
    by eye_still e "……合着你不喜欢她只是单纯的嫉妒啊。"
    hide swimg
    show swimg eye_squint o at char_mid
    sw "才不是！！不喜欢就是不喜欢！第一眼看到就不喜欢！"
    by eye_move o "好好好……随便你。"
    hide swimg
    show swimg eye_squint at char_mid
    "白一无意了解她和天玉的爱恨情仇，敷衍地摆了摆手。"
    by eye_def o "我是想说，天玉跟我说下周她生日，请班上的同学一起去玩。"
    by eye_def o "她问我要不要去，然后也可以带熟悉的人去。"
    hide swimg
    show swimg o at char_mid
    sw "啊？"
    sw "我好像前几天有听人说过，她要请好多人。"
    sw "但你怎么也跟我说这个？"
    hide swimg
    show swimg eye_blink o at char_mid
    sw "难道你的意思是你也想去，还问我想不想跟着一起？"
    by eye_def e "差不多吧。"
    hide swimg
    show swimg eye_sad o at char_mid
    sw "我刚刚才跟你骂完她欸！你竟然让我去捧她的场，呜呜——"
    by eye_still def "……"
    by eye_def o "免费蹭饭有什么不好的。"
    hide swimg
    show swimg eye_sad at char_mid
    sw "呜呜——嗯？你是说，你只是为了蹭饭啊……"
    by eye_def e "对啊，不然呢。"
    hide swimg
    show swimg at char_mid
    "姒舞的装哭声戛然而止，她瞪着白一看了一会，突然恍然大悟般大叫一声。"
    hide swimg
    show swimg o at char_mid
    sw "哦！！"
    sw "对啊，我懂了，我要去，让她看到我比她更受欢迎！"
    hide swimg
    show swimg eye_squint laugh at char_mid
    sw "真不错，你太棒了，好聪明呀，简直是天才！"
    hide swimg
    show swimg eye_squint smile at char_mid
    sw "白一~~~"
    by eye_move def "……"
    "面对姒舞的热情夸赞和沾沾自喜，白一表示拒绝。"
    by eye_still o "我要回家休息了，你也早点走吧。"

    scene bg_classroom with Fade(0.5,0.8,0.5)
    "放学后，教室里比以往还要吵闹。"
    "好些人聚在一起，似乎在热烈讨论着什么。"
    "连白一这个前段时间位于话题中心的人，在进门时也没有再收到频频投来的目光。"
    by eye_wacky def "……搞毛啊？"
    "她往吵闹声来源的方向一瞥，就看见天玉被人群围在中间，笑得很高兴。"
    by eye_move o "哦……我知道了，还是她搞生日活动的事。"
    "学生们总是爱玩的，天玉请人吃饭玩乐，自然是点燃了大家的热情。"
    "就像春游一样，明明离日子还有好几天，也不能阻挡大家讨论怎么玩得开心。"
    "笑声一阵又一阵，话题从天南聊到海北。"
    show tophalfblk with dissolve
    stuA "欸~还有这种事啊~"
    stuB "哈哈哈，开玩笑的啦。"
    stuA "不过，真的好难呐，离期末考太近了，最近睡觉都睡不好。"
    stuB "我也是，你看我的黑眼圈，呜呜~"
    ty "我也有点……"
    stuA "对呀对呀，所以能去天玉那玩一天太好了，放松一下！"
    ty "唔，到时候我也送大家一点帮助睡眠的东西吧。"
    stuB "还有这种东西呀？"
    ty "嗯，助眠的，蒸汽眼罩，香薰，还有花茶包之类的。"
    ty "因为我平时也有这种情况嘛，所以在这方面还算比较有心得。"
    ty "毕竟失眠真的很不舒服呢。"
    stuA "哇，好啊好啊，可以试试！"
    hide tophalfblk with dissolve
    by eye_wacky def "……啧。"
    "跟教室中央的热闹相比，白一所在的位置显得格外安静。"
    "就仿佛彩色的校园里格格不入的一块白色一样。"
    "在闹哄哄的欢笑声里，她终于不动声色地收好书桌的东西，挎上书包，忙不迭地离开教室。"
    by eye_squint e "{size=23}到时候——{/size}我去，好痛！"
    me "好痛！"
    by eye_shock o "我靠！你叫什么？吓我一跳。"
    "白一整个人惊得抖了一下，差点再次踩空，为本就疼痛的伤口再添一笔。"
    me "……我也会感觉到痛啊。"
    by eye_def o "哦，差点忘了这码事。"
    by eye_move o "突然感觉好爽，不止我一个人疼。"
    by eye_close smile "哇塞，赞。"
    me "……"
    me "你这就是所谓的……伤敌八百，自损一千？"
    by eye_move def "切，我乐意。"
    "白一撇了撇嘴，拖着腿一瘸一拐地慢慢走。"

    scene bg_byroom1 with fade
    xs "听说你今天摔着了？"
    by "……是啊。"
    by "怎么你也来问一遍这个。"
    xs "关照一下你的身体健康啊。"
    by "我只是伤了，又不是残了，或者死了。"
    "白一翻了个白眼。"
    "尽管隔着屏幕，西顺看不见，但她大概是想象到白一的反应了吧，叹气声从手机里传出。"
    xs "是这样没错……但是。"
    xs "事实上，你有没有想过为什么。"
    by "你在说啥？"
    xs "同样是摔了一跤，你的那个同学擦过药之后就去继续上课了。"
    xs "但你直接晕倒了，之后睡了一下午。"
    xs "而且她比你伤得严重。"
    by "……什么意思。"
    xs "从比较科学的角度说，这是一种类似于免疫系统的疾病。"
    xs "你的身体受到影响，会导致身体各处虚弱无力，呼吸困难。"
    xs "从不那么科学的角度说……就是你身上的诅咒在消耗你的生命力。"
    "第一次说到白一身上的事情时，西顺就提到过诅咒的效果和三个月的期限。"
    "但资料的概念太过遥远，这是白一第一次切身体会到。"
    "体会到“自己也许就要死了”的事实。"
    by eye_def e "哦……"
    by eye_close o "好像是有这码事。"
    xs "当然我不是要让你有压力，只是想你对自己的情况有个具体的认知，也有个心理准备。"
    xs "其实，就像我一开始说的那样，不要有压力，但也最好注意一下身体。"
    by eye_close o "好好，我明白。"
    "白一懒洋洋地开口。"
    by eye_def e "就是说，万一你最后也没查出来，我也不会怪你的。"
    by eye_def o "哦不不不，如果我真的死了好像也不能投诉你。"
    by eye_close o "总之，真的没关系啊。哪怕你现在说你不想查了，也无所谓，我懂的。"
    xs "……我说你……"
    "西顺顿了顿，欲言又止，最后还是没有说完这句话。"
    xs "好吧，没事，你能保持这样的心态，也不错。"
    xs "不过，离那种山穷水尽的地步还远吧，不要说得那么悲观嘛。"
    by eye_move e "……拜托，我是开玩笑的。"
    by eye_close e "这么明显，你都看不出来吗？"
    xs "是吗？"
    "西顺重重地拉长了声音，似乎是在透过电话里的语气了解白一的内心所想。"
    "隔着电话，白一放松了些，只是懒懒地靠在原地，并没有再多解释什么。"
    "但好在西顺也没再在这个话题上多说。"
    xs "那就好。"
    by eye_close e "行了行了知道了。"
    by eye_def o "对了我今天不是受伤去校医室了吗，刚好看了一下，是像你说的那样，没有温心吃的那个药。"
    xs "这么说来，也算是又有一个可切入的点。"
    xs "明面上看和温心交流比较多的人也就卫锋和姒舞，具体倒也不清楚了。"
    xs "可能还是你在学校多观察一下比较容易。"
    by eye_def o "哦……尽量。"
    by eye_close o "过几天我们班有个同学开生日会，我让姒舞跟我过去。算是按你说的，尝试打好关系吧。"
    "白一顿了顿，想到姒舞的热情，有些头疼。"
    xs "挺好。我还以为你不愿意呢。"
    by eye_move o "……因为，感觉她好像很好骗。"
    "西顺没忍住轻笑出声。"
    xs "有你这么说同学的吗？"
    xs "就算没问到什么，你在学校，能多个朋友也是好的。"
    by eye_def def "……哦。"
    "对此，白一显得有些兴致缺缺。"

    scene bg_byroom2 with circlewipe
    by eye_def o "你刚刚怎么不说话？"
    "挂完电话，白一躺倒在床上，用手指敲了敲墙壁。"
    me "说什么话？"
    by eye_def o "就跟平常一样啊，点评，感慨，骂我？"
    me "等等，别加戏啊，我什么时候骂你了……"
    by eye_still e "喂，这是重点吗？重点是你怎么不说话。"
    me "……就是……感觉不太习惯？"
    by eye_def o "哈？"
    me "西顺不是能听到嘛，就感觉，有点怪怪的。"
    me "类似于做坏事被发现的心情。"
    by eye_still e "你也知道你骂我是坏事啊。"
    me "都说了我没有骂你啊——"
    by eye_close o "好吧，我知道了知道了，就是能被她听到所以害怕呗？"
    me "嗯……差不多吧。"
    by eye_move e "真是搞不懂，明明我也能听到你说话啊？"
    me "你当然是不一样的啊。"
    "这话听上去怪怪的……我刚说完就立马意识到不对，于是开始找补。"
    me "嗯我的意思是……毕竟我“借用”了你的身体。"
    me "西顺她，就是，更像“外人”吧。"
    by eye_still o "啧，你这么说，好像有道理。"
    by eye_still def "明明被用的是我的身体，她竟然也能听见——"
    by eye_move o "这样说的话好像是有些不爽。"
    me "不爽倒没有，不过……所以我不想那时候说话嘛。"
    by eye_close o "好吧，准了。"
    "……这人突然就摆起了谱。"
    "我有些无语，但竟然又觉得理所应当。"
    "就好像……习惯了她就是会做这样的事。"
    "习惯了她会说这样的话。"
    "也习惯了她的存在。"
    return