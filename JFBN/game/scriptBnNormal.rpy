# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后

label bnNormal:

    # 房间1
    scene room1

    play music "audio/normal.mp3" fadeout 1.0 fadein 1.0

    "回到家，Boss脱掉外套，瘫在沙发上面无表情的玩着手机，Noeul倒了一杯果汁递给人。"

    show noeul with Dissolve(0.3)
    noeul "咖啡喝的嘴巴发酸，来点果汁。"

    hide noeul
    "Boss犹豫了几秒还是接了果汁。"

    show noeul with Dissolve(0.3)
    noeul "还在生气吗？"

    hide noeul
    show boss with Dissolve(0.3)
    boss "没有。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "是吗？"

    hide noeul
    show boss with Dissolve(0.3)
    boss "一点点。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "我跟First一直是很好的朋友，而且很多事情都跟你说过了，至于高中的那些，都是小打小闹。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "我只是觉得，你们聊得很开心，我坐在那里没有任何过去的参与感。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "不要每次都在这种事情上伤神，即使没有过去我也很爱你的。"

    hide noeul
    "Noeul握住Boss的手，他能感受到人安全感的缺乏，所以他一直都很愿意一遍遍告诉Boss爱他。"

    show boss with Dissolve(0.3)
    boss "我知道，我也很爱你。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "所以不要暗自伤神，对了跟你说件事。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "什么？"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "爸妈喊我们去回韩国，他们想见见你。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "嗷，太突然了。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "不要激动，先淡定有我在不用惊慌，咱后天去，这两天带着你准备准备。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "好，但控制不住的紧张。"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "那就控制控制，好了太晚了，要睡觉了。"

    hide noeul
    "Noeul准备起身收拾杯子，却被Boss拦腰抱住。"

    show boss with Dissolve(0.3)
    boss "今天都生气了，有补偿吗？"

    hide boss
    "Noeul看着人期待的眼神，伸手想要掰开人的手。"

    show noeul with Dissolve(0.3)
    noeul "不行，明天还有事。"

    hide noeul
    show boss with Dissolve(0.3)
    boss "一次嘛~"

    hide boss
    show noeul with Dissolve(0.3)
    noeul "不行"

    hide noeul
    show boss with Dissolve(0.3)
    boss "就一次嘛~"

    hide boss
    "Noeul再次尝试从人怀里站起来的时候，被Boss抱的很牢，Noeul尝试了几次放弃了。"

    show noeul with Dissolve(0.3)
    noeul "一次。"

    hide noeul
    "夜很长。"

    jump endLabel

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。


    # 此处为游戏结尾。

    return
