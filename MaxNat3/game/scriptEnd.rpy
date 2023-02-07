# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define new = Character('New', color="#ffff00")
define max = Character('Max', color="#f06ca9")
define nat = Character('Nat', color="#4fa6e8")
define pb = Character(None, kind=nvl, what_text_align=0.5, what_xalign=0.5)
define displayDay = Character(None, what_yalign=0.5, kind=nvl)
# define narrator = nvl_narrator


# 游戏在此开始。

label afterSel:
    pb "Max从口袋里掏出了一个小巧的盒子"
    pb "里面是一枚精致的戒指"

    nvl clear

    hide nat happy
    show max stand with dissolve
    max "这本来是昨天拿到打算等你20岁生日时表白成功再给你戴上的，结果没想到这么快就用上了"
    "Max一边结结巴巴解释"
    "一边用他激动的微微颤抖的手试图给Nat套上"
    "结果半天都对不准，惹得Nat都不自觉的脸颊红红的说"

    hide max stand
    show nat happy with dissolve
    nat "快点，快点戴上啦，我都害羞了！"
    hide nat happy

    pb "一分钟过去了"
    pb "Max终于把戒指给Nat戴上了"
    pb "Nat也很开心把另一枚戒指给Max套上"
    pb "开开心心的牵着男朋友一起去吃早餐了。"

    nvl clear
    pb "至于集团总裁Max之后天天春风得意的戴着戒指上班引得员工们议论纷纷"
    pb "还有可怜的Tutor是怎么换着法儿地哄了好几天他的秘密交往男友Yim的事"
    pb "那都是后话啦！"
    pb "END"

    # 此处为游戏结尾。

    return
