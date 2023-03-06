# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后
label extraStory:

    # 结束
    "触发番外"

    scene school

    "不知不觉，Neo和Louis交往一个多月了"

    show neo with Dissolve(0.3)
    neo "Louis~ 过几天我们的纪念日你有想要什么吗？"

    hide neo
    show louis with Dissolve(0.3)
    louis "？"

    louis "什么纪念日？"

    louis "我们交往不是这几天啊...你告白也不是啊..."

    hide louis
    show neo with Dissolve(0.3)
    neo "过几天是我们认识100天纪念日！"

    hide neo
    show louis with Dissolve(0.3)
    louis "蛤？"

    louis "这个也可以算纪念日吗"

    hide louis
    show neo with Dissolve(0.3)
    neo "反正就是纪念日，你要什么礼物嘛"

    hide neo
    show louis with Dissolve(0.3)
    louis "那我想好了再给你发"

    hide louis
    scene louisroom
    "晚上..."

    "Louis想到了要什么就给Neo发消息"

    show neo with Dissolve(0.3)
    neo "不是说不算吗还给我列这么多"

    hide neo
    show louis with Dissolve(0.3)
    louis "啊？太多了吗？那我不要了"

    hide louis
    show neo with Dissolve(0.3)
    neo "不行你必须要，你都列出来了"

    neo "但给你这么多礼物你是不是应该要亲我一下"

    hide neo
    show louis with Dissolve(0.3)
    louis "你都还没给我礼物就开始得寸进尺了啊？"

    hide louis
    show neo with Dissolve(0.3)
    neo "那你先答应给我一个吻"

    hide neo
    show louis with Dissolve(0.3)
    louis "我不"

    hide louis
    scene restaurant
    "纪念日当天..."

    show neo with Dissolve(0.3)
    neo "Louis纪念日快乐"

    neo "虽然我们认识的过程不是很愉快，一开始相处也不是很合拍"

    neo "从我们认识到现在也有100天了"

    neo "希望我们可以从庆祝认识100天纪念日到1000天纪念日甚至10000天纪念日"

    neo "这个是你给我列的清单，每一样我都买了哦！"

    neo "甚至手作的礼物我都做了哦！"

    hide neo
    show louis with Dissolve(0.3)
    louis "Neo好棒"

    louis "但是"

    louis "还差一个礼物没有呢"

    hide louis
    show neo with Dissolve(0.3)
    neo "蛤？有吗？"

    hide neo
    "说着Neo就把清单对了一遍"

    show neo with Dissolve(0.3)
    neo "没有啊，这个有了，那个也有了啊"

    neo "还差什么啊？"

    hide neo
    show louis with Dissolve(0.3)
    louis "你再想想还差什么"

    hide louis
    show neo with Dissolve(0.3)
    neo "没了啊...难道我记少了？"

    hide neo
    "Louis把脸凑到Neo的旁边"

    show louis with Dissolve(0.3)
    louis "还差一个吻。"

    "最近NeoLouis太甜了给大家写个小番外，谢谢大家玩到这边 Jub Jub"

    nvl clear
    full "文本：静苒{vspace=10}故事：小九 @nini小九123{vspace=10}主线：小九 @nini小九123{vspace=10}制作：静苒{vspace=10}"
    full "{vspace=40}BGM: https://www.ashamaluevmusic.com/"
    
    # 此处为游戏结尾。

    return
