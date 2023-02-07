# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后

label bnNc:

    # 房间
    scene room1

    "到家后"

    "Boss直接把人抵在了柜子上。"

    show noeul with Dissolve(0.3)
    noeul "干嘛？"

    noeul "还在生气吗？"

    hide noeul
    show boss with Dissolve(0.3)
    boss "不明显吗？"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "我和小一只是朋友，你该不会吃我俩的醋吧。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "一点点。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "那怎么办？别生气了。"

    hide noeul
    "Noeul伸手揉了揉人的脸。"

    show boss with Dissolve(0.3)
    boss "给亲一口就不生气了。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "啊来哇。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "哄人要有诚意吧。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "好，就一口。"
    
    hide noeul
    scene normalbn
    "Noeul在人嘴上印了一下。"
    scene room1

    show boss with Dissolve(0.3)
    boss "没尝出来味道。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "？什么"

    hide noeul
    show boss with Dissolve(0.3)
    boss "再来一下"

    hide boss
    scene ncbn2
    "Noeul还没反应过来，Boss已经按住人的脖颈吻了上去。"

    scene room1
    show noeul with Dissolve(0.3)
    noeul "唔。"

    hide noeul
    scene ncbn1
    "Boss吸吮着人的嘴唇，舌头勾着人的舌头。"
    scene room1

    play sound "audio/breathbn7.mp3"
    "Noeul用手微微抵开亲吻，喘着粗气。"

    show noeul with Dissolve(0.3)
    noeul "去床上。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "好。"
    
    hide boss
    "Boss直接把人抱了起来，径直回到卧室，把人的衣服熟练的脱下。"

    "Noeul勾着人的脖子。"

    show noeul with Dissolve(0.3)
    noeul "还生气吗？"

    hide noeul
    show boss with Dissolve(0.3)
    boss "还是有点。"

    hide boss
    stop sound
    play sound "audio/kissbn.mp3"
    "Noeul抬头吻上了Boss"

    scene ncbn3
    "Boss顺势迎合人的吻，然后向下舔过人的喉结，吻上人的红缨。"
    scene room1

    show noeul with Dissolve(0.3)
    play music "audio/ncbnbgm.mp3" fadeout 1.0 fadein 1.0
    stop sound
    play sound "audio/breathbn2.mp3"
    noeul "呃……"

    hide noeul
    scene ncbn5
    "Boss伸手拿出安全套，熟练的给自己套上，挤出润滑剂，伸手往人的后穴探。"
    scene room1

    show noeul with Dissolve(0.3)
    stop sound
    play sound "audio/breathbn4.mp3"
    noeul "嘶…慢点…"

    hide noeul
    show boss with Dissolve(0.3)
    boss "乖放松点，太紧了"

    hide boss
    scene ncbn4
    "又不是第一次，但每次Noeul脸都会爆红，他捏着人的肩膀顺应着人。"
    scene room1

    show noeul with Dissolve(0.3)
    stop sound
    play sound "audio/breathbn2.mp3"
    noeul "啊…哈。"

    hide noeul
    "Boss一个挺身顶了进去。"

    show noeul with Dissolve(0.3)
    stop sound
    play sound "audio/breathbn5.mp3"
    noeul "唔……啊…哈"

    hide noeul
    show boss with Dissolve(0.3)
    boss "我看到你跟别人走的太近，真的不开心。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "啊……哈…我知道"

    noeul "但是……唔…不是现在…说"

    hide noeul
    show boss with Dissolve(0.3)
    boss "可…嗯…我控不住情绪。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "我……呜…知道…轻点。"

    hide noeul
    "Boss故意的，说某些词的时候就会撞的很深。"

    show noeul with Dissolve(0.3)
    stop sound
    play sound "audio/breathbn5.mp3"
    noeul "唔…啊…哈……啊"

    hide noeul
    show boss with Dissolve(0.3)
    boss "你…答应我…保持距离…"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "唔…不……要……闹脾气。"

    hide noeul
    "Boss发狠的顶了几下。"

    show noeul with Dissolve(0.3)
    stop sound
    play sound "audio/breathbn3.mp3"
    noeul "呜……好……啊。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "Boss满意的加快了速度。"

    hide boss
    show noeul with Dissolve(0.3)
    stop sound
    play sound "audio/breathbn5.mp3"
    noeul "啊……要到了……啊…"

    hide noeul
    show boss with Dissolve(0.3)
    boss "等我一起…"

    hide boss
    stop sound
    play sound "audio/breathbn6.mp3"
    "一股热流顶在人的身体里，Boss泄了气趴在人的身上。"

    stop sound
    show boss with Dissolve(0.3)
    boss "我…要搬来住。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "Krub"
    hide noeul

    jump conversation

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。


    # 此处为游戏结尾。

    return
