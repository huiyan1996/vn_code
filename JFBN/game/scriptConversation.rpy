# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后
label conversation:

    # 闺蜜对话

    scene room3

    play music "audio/conversation.mp3" fadeout 1.0 fadein 1.0

    "第二天"

    show noeul2 at left with Dissolve(0.3)
    noeul "喂，First在干嘛？"

    hide noeul2
    show first2 at right with Dissolve(0.3)
    first "嗯…我还没起床，你好早啊。"

    hide first2
    show noeul2 at left with Dissolve(0.3)
    noeul "你今天不是有活动吗？怎么还不起？"

    hide noeul2
    show first2 at right with Dissolve(0.3)
    first "我有Ja，不用担心。"

    hide first2
    "First迷迷糊糊中带着沙哑声音，Noeul立马就察觉到不一样。"

    show noeul2 at left with Dissolve(0.3)
    noeul "怎么昨晚在干嘛，这么累？"

    hide noeul2
    show first2 at right with Dissolve(0.3)
    first "唔……没啥事就挂了。"

    hide first2
    "First忍不住翻了一个白眼。"

    show noeul2 at left with Dissolve(0.3)
    noeul "别别别，这不是关心你嘛？"

    hide noeul2
    show first2 at right with Dissolve(0.3)
    first "关心我？那你昨晚睡得咋样啊。"

    hide first2
    show noeul2 at left with Dissolve(0.3)
    noeul "我自然是…是睡的很好。"

    noeul "不过有个正事要跟你说。"

    hide noeul2
    show first2 at right with Dissolve(0.3)
    first "什么？"

    hide first2
    show noeul2 at left with Dissolve(0.3)
    noeul "Boss要来我公寓住了，所以昨天的提议作废了。"

    hide noeul2
    "First又忍不住翻了个白眼。"

    show first2 at right with Dissolve(0.3)
    first "知道了知道了，祝你的腰好运!"

    hide first2
    show noeul2 at left with Dissolve(0.3)
    noeul "什么意思？"

    hide noeul2
    show first2 at right with Dissolve(0.3)
    first "字面意思。"

    hide first2
    "Noeul还没来及反应，First就挂断了电话，大概是太困了，又睡了过去。"

    "Noeul看了一眼在收拾房间的Boss起身去帮忙。"

    "愿他们在每一个平行世界都好好相爱"

    jump endLabel


    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。


    # 此处为游戏结尾。

    return
