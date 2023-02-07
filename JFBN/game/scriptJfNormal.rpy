# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后
label jfNormal:

    # 房间2

    scene room2

    play music "audio/normal.mp3" fadeout 1.0 fadein 1.0

    "Ja随手接过First脱下来的外套，First已经累的瘫在沙发上放空。"

    "Ja接了一杯水递给小一。"

    show ja with Dissolve(0.3)
    ja "吃那么多甜的，喝点水，小心明早胃疼。"

    hide ja
    show first with Dissolve(0.3)
    first "不会啦。"

    hide first
    "First接过水杯，拽着Ja的手让人坐下，然后顺势把腿搭在人腿上一晃一晃的。"

    show first with Dissolve(0.3)
    first "还生气吗？"

    hide first
    show ja with Dissolve(0.3)
    ja "我不是生气。"

    hide ja
    show first with Dissolve(0.3)
    first "我知道，只是心里不舒服。"

    hide first
    show ja with Dissolve(0.3)
    ja "嗯。"

    hide ja
    "First把水杯递给人，然后伸手勾住人的脖子，抵住人的额头。"

    show first with Dissolve(0.3)
    first "那现在呐。"

    hide first
    show ja with Dissolve(0.3)
    ja "我不会把不好的表情对着你。"

    hide ja
    show first with Dissolve(0.3)
    first "我知道，但是我是问，你心里的感觉。"

    hide first
    show ja with Dissolve(0.3)
    ja "慢慢在平复。"

    hide ja
    show first with Dissolve(0.3)
    first "你不是一直跟我说要稳重，怎么今天？"

    hide first
    show ja with Dissolve(0.3)
    ja "这种事情上我也很难稳重。"

    hide ja
    scene normaljf
    "First在人嘴唇上落下一吻。"

    scene room2
    show first with Dissolve(0.3)
    first "OK，我明白了。"

    hide first
    show ja with Dissolve(0.3)
    ja "什么。"

    hide ja
    show first with Dissolve(0.3)
    first "以后我会多照顾你的情绪的。"

    hide first
    show ja with Dissolve(0.3)
    ja "你不用……"

    hide ja
    show first with Dissolve(0.3)
    first "不，很需要，我的男朋友生气，我当然要格外照顾了。"

    hide first
    "First的鼻尖蹭过Ja的鼻尖，Ja慢慢勾起了嘴角，双手掐着人的腰，把人往怀里带。"

    show ja with Dissolve(0.3)
    ja "今天的事情我应该道歉的。"

    hide ja
    show first with Dissolve(0.3)
    first "不，你不需要，各自都有自己的社交，但你在场我就要兼顾你。"

    hide first
    show ja with Dissolve(0.3)
    ja "我也希望你开心。"

    hide ja
    "Ja眼里透露着对First的爱意，他只希望自己的男孩快乐。"

    show first with Dissolve(0.3)
    first "当然我很快乐，在一起的每一天都很快乐。"

    hide first
    show ja with Dissolve(0.3)
    ja "我也很快乐。"

    hide ja
    "First笑着在人嘴唇上又落下一吻，Ja嘴角上扬，手不禁把人圈的更紧，First感应到了什么，推搡了几下。"

    show first with Dissolve(0.3)
    first "Ja，明天还有活动。"

    hide first
    show ja with Dissolve(0.3)
    ja "可是。"

    hide ja
    "Ja盘算了一下时间。"

    show ja with Dissolve(0.3)
    ja "没事我叫你起床"

    hide ja
    "今晚月色很美"

    jump endLabel


    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。


    # 此处为游戏结尾。

    return
