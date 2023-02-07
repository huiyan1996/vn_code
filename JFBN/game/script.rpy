# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define ja = Character('Ja', color="#78b159")
define first = Character('First', color="#f4900c")
define boss = Character('Boss', color="#265ffc")
define noeul = Character('Noeul', color="#e60c86")
# define full = Character(None, kind=nvl, what_text_align=0.5, what_xalign=0.5)
define full = Character(None, kind=nvl, what_xalign=0.5)
define displayDay = Character(None, what_yalign=0.5, kind=nvl)
# 视角
define char = "f"
define final = 0

# 怒气值
define pts = 0

# 游戏在此开始。

# screen Pts:
#     text "Pts [pts]" xpos 0.87 ypos 0.106

label start:

    # 宴会scene
    scene ballroom

    # show screen Pts

    play music "audio/ballroom.mp3"

    # 故事开始
    "夜幕降临，街道霓虹灯的闪烁，照亮着来往的行人，会场内人头攒动，不少人端着酒杯想要拓宽自己的社交圈子，而有的人满场找自己的好友。"

    show ja with Dissolve(0.3)
    ja "First，你确定Noeul真的来了吗？"

    hide ja
    show first with Dissolve(0.3)
    first "当然，你没看到门口他们那个剧的海报吗，而且上午也说了下午见。"

    hide first
    "Ja和First在会场里穿梭着一边和相熟的人打招呼，First一边四处寻找着Noeul。"

    show first with Dissolve(0.3)
    first "诶，Noeul。"

    hide first
    "First看到了不远处一抹熟悉的身影，有些激动的拉住Ja的手臂往那边走。"

    show noeul with Dissolve(0.3)
    noeul "First！"

    hide noeul
    "Noeul正在放空的喝着手里的香槟，突然看到一抹红色入眼，迅速抽掉挎在Boss手臂上的手，张开手臂拥抱走过来的First。"

    show first with Dissolve(0.3)
    first "嗷，好久不见，好想念。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "不是上午才见过？"

    hide noeul
    show first with Dissolve(0.3)
    first "打电话而已，又不是真人。"

    hide first
    "Boss和Ja礼貌性行了合十礼，Boss这应该不是第一次见Ja和First，但之前还没有追到Noeul，也没有聊过天。"

    show first
    first "感觉你好像长肉了，看来某些人给的伙食挺好的。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "First！一定要这么交流吗？那你这日渐红润的......"

    hide noeul
    "Noeul还没说完，就被First捂上了嘴巴，两人不停的眼神乱飞，Boss和Ja看着闹腾的人不由笑出声。"

    show boss with Dissolve(0.3)
    boss "好了好了，既然都是朋友，不如坐下来聊聊天。"

    hide boss
    show first with Dissolve(0.3)
    first "好想法，他咖啡馆就在附近，我前几天吃了几个新出的甜品巨好吃。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "是吗，可我不能再吃了，最近在减肥，现在吃甜品热量会不会太高了。"

    hide noeul
    show first with Dissolve(0.3)
    first "你还要减肥啊，太瘦了之前，不如跟着我锻炼一起增加肌肉。"

    hide first
    "Boss本来都已经伸出了手想要去牵Noeul，谁知道他和First聊得正欢，完全忽视了人的手，拽着First的胳膊就往前走。"

    show ja
    ja "咳，习惯就好了。"

    hide ja
    show boss with Dissolve(0.3)
    boss "嗷，好吧。"

    hide boss
    "Ja和Boss走在两人的身后，气氛有些尴尬，但幸好咖啡馆不远，没走两步就到了。"

    menu:
        "选择聊天的视角"

        "Noeul":
            $char = "n"
            jump afterCharSel
        "First":
            $char = "f"
            jump afterCharSel


    # 此处为游戏结尾。

    return
