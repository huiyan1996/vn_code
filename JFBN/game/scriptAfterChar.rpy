# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后
label afterCharSel:

    # 咖啡厅scene
    scene coffeeshop

    play music "audio/coffeeshop.mp3" fadeout 1.0 fadein 1.0

    show first with Dissolve(0.3)
    first "诶，我们找一个靠里的位置吧，Ja，我还要上次的甜点，如果你不吃的话，就……各来三份。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "嗷，不用，P'Ja，各来两份就可以，我和Boss一起吃一份。"

    hide noeul
    "夜晚进食太多甜食确实对身体并不太好，Noeul拦下了还要点东西的First。"

    show noeul with Dissolve(0.3)
    noeul "First够多了，我们是来聊天了，不是要吃饭。"

    hide noeul
    show first with Dissolve(0.3)
    first "嗷，可是真的都很不错，确定不都来点。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "是聊天，不是甜品品鉴大会。"
    
    hide noeul
    show first with Dissolve(0.3)
    first "好吧，那我们去那边坐。"
    hide first

    if char == "f":
        "Ja熟练的拿起托盘给人去拿甜点，并嘱托店员做三杯咖啡。"

        show ja with Dissolve(0.3)
        ja "三杯就可以，First那杯我来。"
        hide ja

    "Boss跟着Noeul一起落座，First坐在Noeul对面看着人有些明显的黑眼圈有些担忧。"

    show first with Dissolve(0.3)
    first "最近真的好忙，我看你都憔悴了。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "还好了，最近可能事情太多没休息好。"

    hide noeul
    show first with Dissolve(0.3)
    first "对了，讲讲细节，怎么在一起的。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "唔咦，什么时候这么八卦了。"

    hide noeul
    show first with Dissolve(0.3)
    first "不是八卦，只是想了解一下事情的发展到了那一步。"

    hide first
    "First的手不老实的在人胳膊上乱点，Noeul急忙挡开。"

    show noeul with Dissolve(0.3)
    noeul "嗷，那你发展到那一步了，别动手动脚的啊。"

    hide noeul
    show first with Dissolve(0.3)
    first "我俩都谈两年了，啥没跟你说，你不得给我分享分享你的，担心你的幸福啊。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "别，还不如担心你自己，就你那个脑子，不知道谁当年去试了个戏回来就说我恋爱了。"

    hide noeul
    show first with Dissolve(0.3)
    first "唔咦哪有，不要乱说。"

    hide first
    "Boss看着两个鬼马精聊天，然后礼貌的接过Ja递过来的咖啡和甜点。"

    show ja with Dissolve(0.3)
    ja "在聊什么这么开心。"
    hide ja

    if char == 'f':
        "Ja熟练的给人咖啡插上吸管推到人面前，First气鼓鼓的吸了一大口。"

    show noeul with Dissolve(0.3)
    noeul "聊你俩怎么相恋的。"

    hide noeul
    show first with Dissolve(0.3)
    first "那有明明是八卦你俩怎么走到一起的。"

    if char == 'n':
        first "诶，Boss你不知道吧，之前Noeul可多人追了，上学的时候，那课桌里表白信，玫瑰花，小礼物都不断。"

        hide first
        show noeul with Dissolve(0.3)
        noeul "说的跟你不是一样，不知道谁喜欢吃甜的，有人就天天送。"

        hide noeul
        show first with Dissolve(0.3)
        first "那甜点咱俩是不是对半分的，说的跟你没收过一样。"
    elif char == 'f':
        hide first
        show noeul with Dissolve(0.3)
        noeul "Ja可能不知道，First喜欢吃甜的，有人就天天送。"
        
        hide noeul
        show first with Dissolve(0.3)
        first "那甜点咱俩是不是对半分的，说的跟你没收过一样，某些人收的花还少吗。"

    hide first
    "Noeul和First两个互相挖苦着，丝毫没有察觉到身边两人神色已经从笑容转变的有些阴沉。"

    if char == 'n':
        show boss with Dissolve(0.3)
        boss "怎么没听你讲过？"

        hide boss
        show noeul with Dissolve(0.3)
        noeul "这些事也不重要，先吃甜品。"
        menu:
            "Noeul只看出来Boss有些不开心，所以他"

            "把甜品推到人面前。":
                $pts+=1
            "喂人一大勺自己盘子里的甜品":
                pass
        hide noeul

    elif char == 'f':
        show ja with Dissolve(0.3)
        ja "你们高中的那些人还有联系吗？"

        hide ja
        show first with Dissolve(0.3)
        first "没有了，多少年不联系了。"
        
        hide first
        show noeul with Dissolve(0.3)
        noeul "不过送甜品那小女孩不是也进圈子了？"

        hide noeul
        show ja with Dissolve(0.3)
        ja "是吗？"
        menu:
            "Ja脸更黑了，喝了一口咖啡。"
            "那说不一定能遇到。":
                $pts+=1
            "我没见过她。":
                pass
        hide ja
        "First吃了一大口蛋糕继续跟Noeul聊着天"

    show first with Dissolve(0.3)
    first "诶对了，你记得那棵树吗？"

    hide first
    show noeul with Dissolve(0.3)
    noeul "那颗？学校操场那颗吗？"

    hide noeul
    show first with Dissolve(0.3)
    first "听说还在，咱之前不都说它快倒了，没想到能撑这么久，我最近还看有人发给我看。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "想起那个小树林，那小树林真的太恐怖了。"

    hide noeul
    show first with Dissolve(0.3)
    first "到现在没有一届敢去的都是害怕，那故事传的越来越离谱了。"

    first "不过也是那个学校没点传说啊，都是吓唬小孩的。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "那可不，当年被吓的，我回家都得绕路走。"

    hide noeul
    show first with Dissolve(0.3)
    first "诶，你们工作安排的怎么样了，谈恋爱要谈，工作也得安排上。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "不要以经纪人的口吻来训我，我觉得我的工作够多了，最近忙着拍摄和活动都快累死了。"

    hide noeul
    "Noeul挖了一大口蛋糕入嘴，香甜感让他很满意。"

    show noeul with Dissolve(0.3)
    noeul "哦豁，怪不得First每次都要夸一夸你店里的甜品，真的不错。"

    hide noeul
    show first with Dissolve(0.3)
    first "是吧，特别好吃，我总是没事让他从店里打包回家，放冰箱里屯起来慢慢吃，当然我俩一生气，我就去疯狂吃甜品。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "小心你的牙齿啊。"
    hide noeul

    if char == 'n':
        menu:
            "Noeul伸手戳了戳人鼓起的脸颊，这个举动两人并没有在意，只是身边没说话的那位更加不自在了。"

            "回头看Boss":
                pass
            "继续聊天":
                $pts += 1

        show boss with Dissolve(0.3)
        boss "Noeul，咱们要不先回家吧，时间不早了，明天还有活动。"

        hide boss
        show noeul with Dissolve(0.3)
        noeul "你记错了吧，明天活动不是延期了吗？你忘了。"

        hide noeul
        show boss with Dissolve(0.3)
        boss "是吗？可是……"

        hide boss
        "Boss话还没说完，Noeul已经回头继续跟First聊天了，Boss看了一眼对面的Ja，似乎也不太开心，他有些同病相怜的感觉，所以他想做些什么。"

        show boss with Dissolve(0.3)
        boss "我之前关注了P’Ja的Twitter，不如我们加个联系方式吧。"

        hide boss
        show ja with Dissolve(0.3)
        ja "可以"

        hide ja
        "Ja递出了手机，刚通过就听见叮的一声。"

        show bossja at topleft with Dissolve(0.3)
        boss "多多交流。"

        hide bossja
        show bossja2 at topleft
        # \U0001F44C
        ja "OK"
        hide bossja2

    elif char == 'f':
        show ja with Dissolve(0.3)
        ja "First，店铺一会儿要打烊了，要不下次再聊。"

        hide ja
        show first with Dissolve(0.3)
        first "不要，再聊一会儿，一会儿，你可以先让员工下班啊，一会儿我帮你一起收拾剩下的。"

        hide first
        "Ja舔了舔嘴唇，把话压了下去，喝了一口咖啡看着人继续聊天，但是脸色很不好，坐在对面的Boss突然说要加联系方式。"

        show ja with Dissolve(0.3)
        ja "可以。"

        hide ja
        "Ja承认在之前听到Noeul有男友后还暗爽了一段时间，现在看来是得意早了，手机叮的一声。"

        show jaboss at topleft
        boss "多多交流"

        hide jaboss
        show jaboss2 at topleft
        "Ja心领神会发了一个OK。"
        hide jaboss2

    show noeul with Dissolve(0.3)
    noeul "我想起来一个事，你还欠我顿饭，什么时候请回来。"

    hide noeul
    show first with Dissolve(0.3)
    first "啊来哇？我啥时候欠你饭，我怎么不记得。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "？"

    noeul "我给你转的视频你是不是没看？"

    hide noeul
    show first with Dissolve(0.3)
    first "什么视频，你天天给我转那么多我哪知道是哪个？"

    hide first
    show noeul with Dissolve(0.3)
    noeul "! 你有认真看嘛？"

    hide noeul
    show first with Dissolve(0.3)
    first "当然!大概？应该……可能我认真看了。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "哼，你一定是没看，我给你找出来。"

    hide noeul
    "Noeul那着手机一顿操作，点开了那个很久之前的视频，根据猜自己头顶的词牌上的名字。"

    show first with Dissolve(0.3)
    first "唔咦，很胸有成竹啊，猜的很快啊。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "那是，我对你是真爱好吗。"
    hide noeul

    if char == 'n':
        menu:
            "Noeul收起手机，就觉得Boss有些异常，人的手捏着自己的膝盖摩擦，西装裤上都揉出一些褶皱。 "
            "并不理会":
                $pts+=1
                "Noeul并没有过多理会，也没有多想，只是静悄悄的握住人的手，把人的手从自己膝盖上拿开。"
            "握住人的手":
                pass

    show first with Dissolve(0.3)
    first "那今天这顿就算了，算我们请你们的。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "拜托，不要逃脱，分明是P'Ja请我们的。"

    hide noeul
    show first with Dissolve(0.3)
    first "Ja的就是我的啊，一样的，不要计较这些细节。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "不行，不要企图蒙混过关啊。"

    hide noeul
    show first with Dissolve(0.3)
    first "ok，ok，那等咱俩有空了，出去逛街的时候，我请你，还得是我爱你。"
    hide first

    if char == 'f':
        menu:
            "Ja的咖啡杯与桌面发出清脆的碰撞声，First惊了一下，目光扫过人，总觉得人生气了，但又不知道为什么。 "
            "握住人的手当作安抚":
                pass
            "有些疑惑的看着":
                $pts+=1

        show first with Dissolve(0.3)
        first "怎么了，咖啡不好喝吗？"

        hide first
        show ja with Dissolve(0.3)
        ja "没事，手滑了。"
    else:
        show ja with Dissolve(0.3)

    ja "如果要出去吃饭，可以给你们推荐几个餐厅，非常不错。"

    hide ja
    show noeul with Dissolve(0.3)
    noeul "可以可以，列入我们的备选清单，那天出去逛街就把这顿饭吃了。"

    hide noeul
    show first with Dissolve(0.3)
    first "对了我上次去韩国还去拜访了叔叔阿姨，还说好久没见过了，咱也确实也好久没逛街了。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "你最近有啥工作吗？"

    hide noeul
    show first with Dissolve(0.3)
    first "好像没有，怎么了？"

    hide first
    show noeul with Dissolve(0.3)
    noeul "我最近也没工作诶，你要不要来我公寓住。"

    hide noeul
    show first with Dissolve(0.3)
    first "可是不好吧，Boss也在。"

    hide first
    show noeul with Dissolve(0.3)
    noeul "没有，他住自己家，不在我公寓住，你可以来我公寓住一段时……。"
    hide noeul

    if char == 'n':
        menu:
            "Noeul话还没说完，就感觉腰被抓了一把，他转头就对上Boss有些委屈带着哀怨的眼睛。"
            "揽住人的脖子":
                pass
            "拿走人放在腰间的手":
                $pts+=1
        "First似乎并没有感受到不对。"
        "Ja默默把咖啡收了起来，招手示意服务员可以收拾了。"

        show first with Dissolve(0.3)
        first "嗷，我还没吃完诶，等等，Ja你怎么这么着急，我和Noeul还没聊完。"
        hide first
    elif char == 'f':
        "Noeul的话语被打断，First想要答应下来但总觉得气氛不对，只好先低头吃着甜品。"
        menu:
            "Ja已经不想继续呆着了，默默把咖啡收了起来，招手示意服务员可以收拾了，自己揽住人的腰。"
            "等等别急":
                $pts+=1

                show first with Dissolve(0.3)
                first "嗷，我还没吃完诶，等等，Ja你怎么这么着急，我和Noeul还没聊完。"
                hide first
            "握住人的手":
                "First虽然不情愿还是同意了，握住了人的手。"

    if char == 'n':
        jump bnCar
    if char == 'f':
        jump jfCar

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。


    # 此处为游戏结尾。

    return
