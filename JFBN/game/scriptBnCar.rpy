# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后
label bnCar:

    # 车上
    "Noeul看着依然有些不高兴的Boss，低声询问。"

    show noeul with Dissolve(0.3)
    noeul "怎么了，你看起来脸色不好。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "我想回家，就是现在。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "可是......"

    hide noeul
    show boss with Dissolve(0.3)
    boss "P'Ja我们回头再聊"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "First我们先走了，拜拜。"

    hide noeul
    "Noeul回头跟First匆忙的道别后，就跟着Boss快步走出了餐厅"

    scene car1

    show noeul with Dissolve(0.3)
    noeul "你看起来不开心？"

    hide noeul
    show boss with Dissolve(0.3)
    boss "所以你看出来了？"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "有一点。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "我知道我生气并不对，但是……"
    hide boss

    menu:
        "夜晚的车内非常昏暗，Boss欲言又止的话把气氛降到了一个极点。"
        "Noeul伸手拍了拍人的肩膀，大拇指摩挲着人的肩膀。":
            pass
        "我们只是多年好友聚餐，不要多想。":
            $pts+=1

    "Boss点了点头，并没有过多的语言和动作。"

    "快到公寓门口的时候，Boss才发话。"

    # 门前
    scene outroom

    show boss with Dissolve(0.3)
    boss "리노엔，我今天要睡你的公寓。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "可以啊。"

    hide noeul
    "Noeul听到人喊自己的韩文名字不由得倒吸一口冷气。"

    show noeul with Dissolve(0.3)
    noeul "特别生气吗？"

    hide noeul
    show boss with Dissolve(0.3)
    boss "没有。"
    hide boss

    if pts >= 3:
        $final = 2
        jump bnNc
    else:
        $final = 1
        jump bnNormal

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。


    # 此处为游戏结尾。

    return
