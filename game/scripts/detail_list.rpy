define clueList = [ # clue content, index = line number - 2
    ("调查报告1", "与怪异联系后，城安局特调组重新对温心的死亡事件进行了调查。"),
    ("客厅-餐桌","抽屉里有一双木质筷子，一双用过后洗干净的一次性筷子，上面刻有“湘味”的字迹。"),
    ("客厅-床铺","被子已经被掀开，堆在一边。床单很旧，有不少补丁，但很干净。枕头上有两个人躺过的痕迹。"),
    ("灶台-燃气灶","有长时间开过火的痕迹，燃气灶老旧，燃气喷嘴处有异物堵塞。"),
    ("灶台-垃圾桶","空空如也，没有袋子"),
    ("洗手间-窗户","被百叶窗盖住的窗户关闭，上了锁"),
    ("储物柜-药盒","透明药盒里有两瓶一样的感冒药，其中一瓶空了。"),
    ("门口-备忘录","6:30起床，7:00到校，17:00放学，XXXX（涂黑），20:00扔垃圾（周末整理房间），23:30睡觉"),
    ("校医室-床","套着简易被套，盖着薄被的铁架单人床。"),
    ("校医室-房门","通往内侧房间的门，上面贴有几个可爱的贴纸。正中央挂着一张门牌，用圆润的字体画着“love”的字样。"),
    ("校医室-柜子","玻璃柜上了锁，可以看到里面摆放着创可贴，棉球，纱布，感冒冲剂等物品。"),
    ("大堂-箭头","墙面上贴着指向标的图样。好几个箭头，标注了不同方向的信息。左侧是游戏室、茶水间、后花园，右侧是电影房和卫生间。从正中间往里，则是巨大的宴会厅。"),
    ("大堂-日历","墙上挂着日历，停留在这个月的页面。设计灵动，装帧精美，配上美丽的纹样，当作装饰也毫不突兀。1月1日的地方用记号笔圈出一个大大的圆圈，旁边标有手写的笔记“17岁生日”。"),
    ("云玉阁-钥匙","一把钥匙挂着吊牌，上面写有房间数字。"),
    ("201-蜡烛","放在床头柜上，已经烧完了。透过留给灯芯的洞，能够看到容器里剩下的浅浅一层像是碎屑的残留物。"),
    ("201-杯子","在茶几边缘，里面有干涸的水渍和浸透的茶包。"),
    ("201-内门","连接202房间，可以把两间房变成大号套房的两扇门。轻轻掩着，都没有上锁。"),
    ("201-洗手间","地面上有一个长条形的，类似椭圆的痕迹，不太清晰。"),
    ("201-墙面","二楼平面图，标注了各个房间的位置以及消防电梯的位置"),
    ("调查报告2","梁绵绵的调查报告"),
    ("行动表","在询问后，记录下的学生行动轨迹。"),
    ("电影房-牛奶","也许是因为室内的空调开得好，牛奶还保持在常温状态，没有变凉。"),
    ("游戏室-窗户","大概是为了透气，窗户开着。窗外是后花园，传来源源不断的冷风。"),
    ("游戏室-玩具","玩具被随意地堆在窗户底下的地毯上。魔方，积木，卡牌……不同种类的玩具被堆在一起，有个小球甚至被挤出了盒子外面。"),
    ("游戏室-显示屏","放在桌子上的显示屏连接着电脑，上面投影着知名游戏平台的账号内容，最新玩过的游戏是《交织的印记》。"),
    ("茶水间-助眠套装","和房间里收到的一样，是多出来的助眠套装，里面有茶包，香薰蜡烛，蒸汽眼罩。"),
    ("茶水间-饮料","桌上摆满了一排排的饮料，除了瓶装，还有桶装的，可以倒在旁边的一次性杯子里。"),
    ("202-内门","连接201房间，可以把两间房变成大号套房的两扇门。轻轻掩着，都没有上锁。"),
    ("202-盒子","助眠套装，没有拆开过。"),
    ("202-拖鞋","酒店的一次性拖鞋，被胡乱地甩在床边。"),
    ("白一的手机","白一的手机软件，因为长时间不用，有过盗号记录。"),
    ("监控","学校为了家长会新装修增加的监控，在每层楼的楼梯口。"),
    ("墙壁","墙上贴有“心理小贴士”，用圆润可爱的字体列举了一些给中学生的建议。"),
    ("门口","靠近门口的天花板上挂着一个风铃。莹润的珠串连接着些许小巧的可爱吊坠，门被推开的时候，会带起叮叮当当的声音。"),
    ("书桌","书桌很干净，上面的东西摆放得整整齐齐。电脑，水杯，以及放在角落的常用小药箱。"),
    ("抽屉","抽屉里放了几本心理学的书籍，除此以外，最下面是一本笔记本，里面详细记录了每次做辅导的时间和对象。"),
]

default persistent.clue = [0]*36
# images for clues
image evlocked = "gui/ev/ev-locked.png"
image clue0 = "images/clue/clue_0.png"
image clue1 = "images/clue/clue_1.png"
image clue2 = "images/clue/clue_2.png"
image clue3 = "images/clue/clue_3.png"
image clue4 = "images/clue/clue_4.png"
image clue5 = "images/clue/clue_5.png"
image clue6 = "images/clue/clue_6.png"
image clue7 = "images/clue/clue_7.webp"
image clue8 = "images/clue/clue_8.png"
image clue9 = "images/clue/clue_9.png"
image clue10 = "images/clue/clue_10.png"
image clue11 = "images/clue/clue_7.webp"
image clue12 = "images/clue/clue_7.webp"
image clue13 = "images/clue/clue_13.png"
image clue14 = "images/clue/clue_14.png"
image clue15 = "images/clue/clue_15.png"
image clue16 = "images/clue/clue_16.png"
image clue17 = "images/clue/clue_17.png"
image clue18 = "images/clue/clue_18.png"
image clue19 = "images/clue/clue_19.png"
image clue20 = "images/clue/clue_20.png"
image clue21 = "images/clue/clue_21.png"
image clue22 = "images/clue/clue_22.png"
image clue23 = "images/clue/clue_23.png"
image clue24 = "images/clue/clue_24.png"
image clue25 = "images/clue/clue_25.png"
image clue26 = "images/clue/clue_26.png"
image clue27 = "images/clue/clue_27.png"
image clue28 = "images/clue/clue_28.png"
image clue29 = "images/clue/clue_29.png"
image clue30 = "images/clue/clue_30.png"
image clue31 = "images/clue/clue_31.png"
image clue32 = "images/clue/clue_32.png"
image clue33 = "images/clue/clue_33.png"
image clue34 = "images/clue/clue_34.png"
image clue35 = "images/clue/clue_35.png"



# character info
define charList = [
    "白一",
    "岑宣",
    "繁锦",
    "梁绵绵",
    "林望龙",
    "姒舞",
    "天玉",
    "卫锋",
    "温心",
    "西平",
    "西顺",
    "张班",
]
default persistent.char = [0]*len(charList)

# story noun explanation
define persistent.dictList = [
]