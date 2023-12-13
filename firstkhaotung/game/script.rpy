# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define f = Character('First', color="#ffb13c")
define kt = Character('Khaotung', color="#fd8700")
define frank = Character('Frank', color="#000000")
define podd = Character('Podd', color="#000000")
# define full = Character(None, kind=nvl, what_text_align=0.5, what_xalign=0.5)
define full = Character(None, kind=nvl, what_xalign=0.5)
define displayDay = Character(None, what_yalign=0.5, kind=nvl)
# 视角
define fkt = 0 #一糖点
define link = 0 #羁绊
define lf1 = 0 #梦境1
define lf2 = 0 #梦境2
define isCat = 0 #有没有馒头

screen Pts:
    text "{color=#ff7700}一糖 [fkt] 羁绊 [link]" xpos 0.87 ypos 0.106

# 游戏在此开始。

label start:

    scene ktroom

    show screen Pts

    # 此处显示各行对话。

    f "我们是不是在哪见过？"

    "First接过人递来的剧本，无厘头的抛出一句话。"

    kt "什么，你睡迷糊了？"

    "Khaotung看着神色涣散的First发笑，递给人一管鼻通，示意人清醒清醒。"

    "First接过人递来的鼻通，不由得笑出了声，他深吸一口气，看着Khaotung。"

    f "我说的话，你信吗？"

    kt "我为什么不会信？"

    "然后First似乎做了很大的决定，开始喋喋不休的解释自己做了很奇怪的梦，是关于他们的但不是发生在现在。"

    "Khaotung耐心的听完人的冗长的解释，然后似懂非懂的点了点头，露出了一个心底了然的微笑。"

    kt "所以你是太想我了嘛，会梦到我。"

    f "诶，tung。"

    "看着人得意的笑，First忍不住把剧本卷成筒上手揍人，但Khaotung快速的缩脖子躲开了，First看人嬉笑的躲开了，也没有再说下去。"

    kt "好了好了，读本吧读本吧，今天先看看本，明天要进组了。"

    "Khaotung伸手怕了拍人的肩膀，大拇指摩挲这人的肩膀，当做安抚炸毛的First，First很吃这一套，迅速的安静下来，铺展成卷的剧本。"

    "Khaotung很喜欢炸毛后乖顺的First，忍不住盯着人多望了几秒，First转头对上人的眼神，不由得起了一层鸡皮疙瘩。"

    f "tung ! 看剧本。"

    "Khaotung思绪被人的声音拉回到剧本上，有些心虚的舔了舔嘴唇，埋头泛起了剧本。"

    jump life1

    # 此处为游戏结尾。

    return
