define me = Character("我",what_prefix="“",what_suffix="”",ctc="ctc-img",ctc_position="fixed")
# add side image later
define by = Character("白一", image="byimg",what_prefix="“",what_suffix="”", ctc="ctc-img",ctc_position="fixed")
define cx = Character("岑宣",what_prefix="“",what_suffix="”")
define fj = Character("繁锦",what_prefix="“",what_suffix="”")
define lwl = Character("林望龙",what_prefix="“",what_suffix="”")
define sw = Character("姒舞",what_prefix="“",what_suffix="”")
define ty = Character("天玉",what_prefix="“",what_suffix="”")
define wf = Character("卫锋",what_prefix="“",what_suffix="”")
define xl = Character("小蓝",what_prefix="“",what_suffix="”")
define xp = Character("西平",what_prefix="“",what_suffix="”")
define xs = Character("西顺",what_prefix="“",what_suffix="”")
define zb = Character("张班",what_prefix="“",what_suffix="”")
define unknown = Character("？？",what_prefix="“",what_suffix="”")

image side byimg = LayeredImageProxy("byimg", Transform(zoom=0.49,xoffset=-250,yoffset=1450))

# 白一
layeredimage byimg:
    group body:
        attribute uniform default:
            "images/char/by/uniform.webp"
        # attribute shirt:
        #     "images/char/mei/shirt.png"

    group eyes:
        attribute eye_def default:
            "images/char/by/eye-def.webp"
        attribute eye_close:
            "images/char/by/eye-close.webp"
        attribute eye_wacky:
            "images/char/by/eye-wacky.webp"
        attribute eye_still:
            "images/char/by/eye-still.webp"
        attribute eye_shock:
            "images/char/by/eye-shock.webp"
        attribute eye_move:
            "images/char/by/eye-move.webp"

    group mouse:
        attribute def default:
            "images/char/by/m-def.webp"
        attribute smile:
            "images/char/by/m-smile.webp"
        attribute e:
            "images/char/by/m-e.webp"
        attribute o:
            "images/char/by/m-o.webp"

# 岑宣
layeredimage cximg:
    group body:
        attribute uniform default:
            "images/char/cx/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/cx/eye-def.webp"
        attribute eye_close:
            "images/char/cx/eye-close.webp"
        attribute eye_angry:
            "images/char/cx/eye-angry.webp"
        attribute eye_sad:
            "images/char/cx/eye-sad.webp"

    group mouse:
        attribute def default:
            "images/char/cx/m-def.webp"
        attribute smile:
            "images/char/cx/m-smile.webp"
        attribute o:
            "images/char/cx/m-o.webp"

# 繁锦
layeredimage fjimg:
    group body:
        attribute coat default:
            "images/char/fj/coat.webp"
        # attribute shirt:
        #     "images/char/mei/shirt.png"

    group eyes:
        attribute eye_def default:
            "images/char/fj/eye-def.webp"
        attribute eye_close:
            "images/char/fj/eye-close.webp"
        attribute eye_squint:
            "images/char/fj/eye-squint.webp"
        attribute eye_sad:
            "images/char/fj/eye-sad.webp"
        attribute eye_shock:
            "images/char/fj/eye-shock.webp"

    group mouse:
        attribute def default:
            "images/char/fj/m-def.webp"
        attribute smile:
            "images/char/fj/m-smile.webp"
        attribute o:
            "images/char/fj/m-o.webp"
        attribute laugh:
            "images/char/fj/m-laugh.webp"


# 林望龙
layeredimage lwlimg:
    group body:
        attribute uniform default:
            "images/char/lwl/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/lwl/eye-def.webp"
        attribute eye_squint:
            "images/char/lwl/eye-squint.webp"

    group mouse:
        attribute def default:
            "images/char/lwl/m-def.webp"
        attribute smile:
            "images/char/lwl/m-smile.webp"
        attribute o:
            "images/char/lwl/m-o.webp"


# 姒舞
layeredimage swimg:
    group body:
        attribute uniform default:
            "images/char/sw/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/sw/eye-def.webp"
        attribute eye_blink:
            "images/char/sw/eye-blink.webp"
        attribute eye_squint:
            "images/char/sw/eye-squint.webp"
        attribute eye_sad:
            "images/char/sw/eye-sad.webp"

    group mouse:
        attribute def default:
            "images/char/sw/m-def.webp"
        attribute smile:
            "images/char/sw/m-smile.webp"
        attribute o:
            "images/char/sw/m-o.webp"
        attribute laugh:
            "images/char/sw/m-laugh.webp"


# 天玉
layeredimage tyimg:
    group body:
        attribute uniform default:
            "images/char/ty/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/ty/eye-def.webp"
        attribute eye_close:
            "images/char/ty/eye-close.webp"
        attribute eye_squint:
            "images/char/ty/eye-squint.webp"
        attribute eye_sad:
            "images/char/ty/eye-sad.webp"

    group mouse:
        attribute def default:
            "images/char/ty/m-def.webp"
        attribute smile:
            "images/char/ty/m-smile.webp"
        attribute o:
            "images/char/ty/m-o.webp"
        attribute laugh:
            "images/char/ty/m-laugh.webp"


# 卫锋
layeredimage wfimg:
    group body:
        attribute uniform default:
            "images/char/wf/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/wf/eye-def.webp"
        attribute eye_close:
            "images/char/wf/eye-close.webp"
        attribute eye_still:
            "images/char/wf/eye-still.webp"
        attribute eye_sad:
            "images/char/wf/eye-sad.webp"

    group mouse:
        attribute def default:
            "images/char/wf/m-def.webp"
        attribute smile:
            "images/char/wf/m-smile.webp"
        attribute o:
            "images/char/wf/m-o.webp"
        attribute purse:
            "images/char/wf/m-purse.webp"


# 小蓝
layeredimage xlimg:
    group body:
        attribute uniform default:
            "images/char/xl/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/xl/eye-def.webp"

    group mouse:
        attribute def default:
            "images/char/xl/m-def.webp"
        attribute o:
            "images/char/xl/m-o.webp"


# 西平
layeredimage xpimg:
    group body:
        attribute uniform default:
            "images/char/xp/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/xp/eye-def.webp"

    group mouse:
        attribute def default:
            "images/char/xp/m-def.webp"
        attribute o:
            "images/char/xp/m-o.webp"


# 西顺
layeredimage xsimg:
    group body:
        attribute uniform default:
            "images/char/xs/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/xs/eye-def.webp"
        attribute eye_close:
            "images/char/xs/eye-close.webp"
        attribute eye_move:
            "images/char/xs/eye-move.webp"
        attribute eye_squint:
            "images/char/xs/eye-squint.webp"
        attribute eye_shock:
            "images/char/xs/eye-shock.webp"

    group mouse:
        attribute def default:
            "images/char/xs/m-def.webp"
        attribute smile:
            "images/char/xs/m-smile.webp"
        attribute o:
            "images/char/xs/m-o.webp"
        attribute purse:
            "images/char/xs/m-laugh.webp"


# 张班
layeredimage xpimg:
    group body:
        attribute uniform default:
            "images/char/xp/uniform.webp"

    group eyes:
        attribute eye_def default:
            "images/char/xp/eye-def.webp"

    group mouse:
        attribute def default:
            "images/char/xp/m-def.webp"
        attribute o:
            "images/char/xp/m-o.webp"
        attribute e:
            "images/char/xp/m-e.webp"