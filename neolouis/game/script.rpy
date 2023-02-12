# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define neo = Character('Neo', color="#5cb3ee")
define louis = Character('Louis', color="#ffffff")
define pond = Character('Pond', color="#265ffc")
define phuwin = Character('Phuwin', color="#bde7ff")
define dunk = Character('Dunk', color="#faea57")
# define full = Character(None, kind=nvl, what_text_align=0.5, what_xalign=0.5)
define full = Character(None, kind=nvl, what_xalign=0.5)
define displayDay = Character(None, what_yalign=0.5, kind=nvl)
# 视角
define pts = 0

# 游戏在此开始。

label start:

    scene hoteldoor
    play music "audio/hotel.mp3"

    # show eileen happy

    # 此处显示各行对话。

    "Neo二十岁生日那天，朋友们请他去酒吧庆祝，酒过三巡，大家说要送他一个成人礼物，于是给了他一张房卡，送他进入电梯。"

    show neo with Dissolve(0.3)
    neo "611，611在哪"

    neo "到了"

    hide neo
    "说着用房卡去开门，但是总打不开，于是开始用力敲门"

    show neo with Dissolve(0.3)
    neo "开门，不是说要给我礼物吗！"

    hide neo
    "半分钟之后..."

    scene dooropen

    "房门被打开了"

    scene hotelroom

    "还没等房门里的人问话，他就一把抱住了眼前的男孩子，整个身体都压在他的身上，头枕在对方的肩膀上，用鼻尖嗅着对方的脖颈"

    show neo with Dissolve(0.3)
    neo "你真好闻。这个礼物，我喜欢。"

    hide neo
    "说着就把人往房间里推，男孩子挣扎起来，可是双方力气悬殊太大，Neo直接把对方带到床上"

    show louis with Dissolve(0.3)
    louis "放开我，我不是……"

    hide louis
    "Neo酒劲上来，只看见软嘟嘟的嘴唇，像是水果糖，于是亲了上去，他心里想，这下安静了，之后不顾对方挣扎把人锁进自己的怀里，抱着睡着了。"
    
    "这一觉睡得极好"

    "Neo梦见了自己好像被云层裹挟着，又软又香很是舒服，直到自己被外力拉扯醒来"

    "他睁开眼睛看见床边站着俩个人，一下子全醒了坐了起来"

    show neo with Dissolve(0.3)
    neo "你们是谁？"
    
    hide neo
    show louis with Dissolve(0.3)
    louis "嗯～ 好吵"

    louis "哥，Dunk，你们来了，家里怎么说？同意我不去国外了吗？"

    hide louis
    show pond with Dissolve(0.3)
    pond "Louis，说说看，怎么回事，他是谁？"

    hide pond
    show louis with Dissolve(0.3)
    louis "我不认识他，我昨天乖乖在房间里等你来接我，然后有人敲房门，我去开了，他就把我抱住了，我想挣脱，但是没成功，然后就是你们看见的样子了。"

    hide louis
    show pond with Dissolve(0.3)
    pond "你的嘴巴怎么回事？别告诉我说睡了一觉肿了。"

    hide pond
    "Louis脸刷的就红了，舌尖抵上了唇内的一个破口，Neo也瞟向了他的嘴唇"

    show dunk with Dissolve(0.3)
    dunk "你们昨天还有发生什么事吗？"

    hide dunk
    show neo with Dissolve(0.3)
    neo "什么都没有，我昨天喝醉了，我还想问呢？为什么在我的房间？你们想干什么？仙人跳？"

    hide neo
    show louis with Dissolve(0.3)
    louis "什么你的房间？这明明是我定的！"

    hide louis
    show neo with Dissolve(0.3)
    neo "这是601，我有房卡，怎么会是你定的？"

    hide neo
    show louis with Dissolve(0.3)
    louis "607，这间房是607！"
    hide louis

    menu: 
        "这时，Neo发现自己进错房间了，他说"

        "是我错了":
            $pts+=1
            
            show neo with Dissolve(0.3)
            neo "对不起 我进错房间了"

            hide neo
            show louis with Dissolve(0.3)
            louis "没关系，你喝醉了可能看错了房间号"
            hide louis

        "我喝醉了":

            show neo with Dissolve(0.3)
            neo "我昨晚喝醉了看错了房号"

            neo "又不是我想的"

            neo "我朋友要给我的礼物都还没拿到呢"
            hide neo

    show pond
    pond "你是谁？"

    pond "你对我弟干嘛了？"

    pond "把你的证件拿出来"
    hide pond

    "Pond说着去翻了Neo外套的口袋，从那里找到了身份证和学生证，拍了照"

    show pond
    pond "把电话号码给我"

    hide pond
    show neo with Dissolve(0.3)
    neo "为什么"

    hide neo
    show pond with Dissolve(0.3)
    pond "给我！"

    hide pond
    show neo with Dissolve(0.3)
    neo "哦...."
    hide neo

    "拿了电话号码之后， Pond把Louis从床下拉了下来"

    show pond with Dissolve(0.3)
    pond "不要再接近我弟"
    hide pond

    "Pond说完就带着Louis和Dunk一起离开了"

    scene car
    play music "audio/pondcar.mp3" fadeout 1.0 fadein 1.0

    show pond
    pond "你和他是不是在学校就认识了？"

    hide pond
    show louis with Dissolve(0.3)
    louis "他和我是一个学校的吗？我没看过他。医学院里没有这号人物。"

    hide louis
    "说完Louis向Pond撒娇"

    show louis with Dissolve(0.3)
    louis "哥哥，我不想出国，我长这么大都没有离开过你，你就帮我和爸妈再说说吧！"

    louis "不然，等以后你出国工作。把我也带上，总之我现在不出去，要是你们执意如此，我下次再跑就不和你说了！"

    louis "哥哥，你会答应我的吧！"

    hide louis
    show dunk with Dissolve(0.3)
    dunk "你是Pond的小尾巴吗？这么大还对着哥哥撒娇。"

    hide dunk
    show pond with Dissolve(0.3)
    pond "我已经和爸妈谈妥了，但是你答应我在学校里不许和Neo接触，不然我会亲自送你出国。"
    hide pond

    menu: 
        "Louis想了想说"

        "为什么":
            $pts += 1
            
            show louis with Dissolve(0.3)
            louis "为什么呀？"

            louis "我感觉他也没怎么啊"

            hide louis
            show pond with Dissolve(0.3)
            pond "反正你不许和他接触"

            hide pond
            show louis with Dissolve(0.3)
            louis "好吧"
            hide louis

        "好的": 
            show louis with Dissolve(0.3)
            louis "知道了哥"

            louis "我不会和他接触的"

            louis "我和他又不在一个学院"

            hide louis
            show pond with Dissolve(0.3)
            pond "你自己答应的啊"
            hide pond

    "Louis乖巧的点了点头，心里却默默记住了Neo的名字"

    "原来他叫Neo阿"

    scene neohome
    play music "audio/bothhome.mp3" fadeout 1.0 fadein 1.0

    show neo with Dissolve(0.3)
    neo "我回来啦~我亲爱的弟弟"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "哟，舍得回家啦？"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "怎么对你哥说话的"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "你去酒店就去酒店你穿我衣服去干嘛"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "我衣服还在晾，借你衣服一下不行吗？又不是不会还"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "呵，现在轮到我衣服晾不干了我明天还要穿呢！"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "你穿我的呗"

    neo "对了你学校那个叫Louis的你认识吗"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "哦你说P Pond的弟弟吗？"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "别给我提那个Pond，对是那个Louis"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "怎么了？Louis算是我朋友吧，但不太熟"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "没有，他...额挺可爱的"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "?"

    phuwin "看上人家了？"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "我没有喜欢他，只是好奇罢了"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "你突然问我Louis我以为你想追他呢"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "我真的没有喜欢他好吧，他怎么看都不是我的菜好吧"

    neo "不和你说了，回房了。"
    hide neo

    scene school
    play music "audio/school.mp3" fadeout 1.0 fadein 1.0

    "周末很快结束了"

    "Louis从解剖课上出来，远远的就看见Neo站在学院楼的进出口"

    "Louis想着对哥哥的承诺，无视Neo的存在和同学一起走了"

    menu:
        "Neo看到Louis无视自己觉得有点不高兴，所以他"

        "扯住Louis的手腕":
            "Neo一时心急扯住了Louis的手腕"

            show louis with Dissolve(0.3)
            louis "嘶——"

            louis "疼！"
            hide louis

        "跑到Louis前面挡住他的路":
            $pts+=1

            "Neo跑到Louis前面不让他继续无视自己"

    show neo with Dissolve(0.3)
    neo "为什么看到我，不和我打招呼？"

    hide neo
    show louis with Dissolve(0.3)
    louis "你是谁？"

    louis "我不认识你。"
    hide louis

    "Louis的同学用疑惑的眼神看了一眼Louis，想知道怎么了"

    show louis with Dissolve(0.3)
    louis "没什么，他可能认错人了，走吧。"

    hide louis
    show neo with Dissolve(0.3)
    neo "不认识，那谁在上周五晚上……"
    hide neo

    "话还没说完，路易就用另一只手捂住了Neo的嘴巴，在同学的惊诧中和Neo离开了。"

    scene car2
    play music "audio/neocar.mp3" fadeout 1.0 fadein 1.0

    "Neo带着Louis到车上"

    show neo with Dissolve(0.3)
    neo "现在认识了？"

    hide neo
    show louis with Dissolve(0.3)
    louis "你找我干什么？你怎么知道我在医学院的？"

    hide louis
    show neo with Dissolve(0.3)
    neo "我认识你哥，想找到你不是很简单吗？"

    hide neo
    show louis with Dissolve(0.3)
    louis "你找我干什么？"
    hide louis

    menu:
        "这个时候Neo回答"

        "我来找我弟":
            show neo with Dissolve(0.3)
            neo "谁说我找你了？"
            
            neo "我是来找我弟的，是你把我拉过来的"
            hide neo

            "Louis听完只觉得无语，就想打开车门离开"

            show neo with Dissolve(0.3)
            neo "你在学校不要来找我，我们什么关系都没有"

            neo "还有，我不喜欢你这种类型的人"

            neo "懂了吗？别想借机缠上我"
            hide neo

            "Louis甩开Neo还拉着他的手，头也没回就开门下车走了"

        "没事":
            $pts+=1

            show neo with Dissolve(0.3)
            neo "没事啊，我本来是来找我弟的"

            neo "刚刚在路上看到你，你居然当作不认识我直接走过去了"

            neo "我就是觉得不太高兴才把你拦下来的"

            neo "我先说我没有喜欢你，我只是不喜欢被无视"

            hide neo
            show louis with Dissolve(0.3)
            louis "你放心我也没有喜欢你"

            louis "可以放手了我要走了"
            hide louis

            "Louis扒开Neo的手就下车走了"

    scene neohome
    play music "audio/bothhome.mp3" fadeout 1.0 fadein 1.0

    "晚上..."

    show phuwin
    phuwin "哥，你今天来医学院了？怎么没找我就走了？"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "你怎么知道我去医学院的？"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "你和Louis在学院门口拉拉扯扯，被人拍下来上传到网上了。你俩交朋友了？"

    phuwin "不是说不喜欢他那类型的？"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "没有的事，我只是有些事要问他"

    neo "对啊，我一直喜欢的都是明艳动人的，不是早就说了他这种小兔子不是我的菜吗？"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "那..."

    hide phuwin
    show neo with Dissolve(0.3)
    neo "不聊了，有事"

    hide neo
    "Neo没给Phuwin继续发问的机会，就回自己房间了。"

    scene louishome

    "另一边..."

    show pond with Dissolve(0.3)
    pond "说吧，昨天不是和我保证不和他联系，今天就被拍到照片，你之前到底认不认识他？"

    hide pond
    show louis with Dissolve(0.3)
    louis "不认识，他今天来找我，和我说所有场合都别和他讲话。照片什么的可能是被人拍照了，我不知情的"

    louis "你看我都没有他的联系方式"
    hide louis

    "说着Louis把手机拿出来给Pond看"

    "Neo请求添加您为好友"

    show pond with Dissolve(0.3)
    pond "那这是什么？"

    pond "拒绝了"

    hide pond
    "说着Pond替Louis拒绝了好友申请然后拿起自己手机打给了Neo"

    show pond with Dissolve(0.3)
    pond "你想对我弟干嘛？"

    pond "劝你别对我弟动什么心思"

    hide pond
    show neo with Dissolve(0.3)
    neo "我先说我绝对不会对Louis有好感，只是看见了网上的照片，想让他别乱想。"

    hide neo
    show pond with Dissolve(0.3)
    pond "最好是这样。你以后别再学校去找他，我自己的弟弟我自己可以照顾好。别再联系他。"
    hide pond

    "说完这句Pond就把电话挂了"

    show pond with Dissolve(0.3)
    pond "你要交友哥哥没意见，但是他不行，你从小就很乖，Neo心思太浮，不适合做你的朋友。"

    hide pond
    show louis with Dissolve(0.3)
    louis "哥哥，我从没想过和他做朋友，你别担心我。"
    hide louis

    "之后Louis又收到了Neo的交友请求"

    show louis with Dissolve(0.3)
    louis "还是拒绝吧"
    hide louis

    "Louis想着哥哥对自己说的还是拒绝了好友申请"

    scene library
    play music "audio/library.mp3" fadeout 1.0 fadein 1.0

    "第二天..."

    "Louis正在找外科的参考书籍"

    show neo with Dissolve(0.3)
    neo "为什么拒绝我的好友请求？"

    hide neo
    show louis with Dissolve(0.3)
    louis "没必要加好友"

    louis "上次你说的话我明白了"

    louis "我不会缠着你的"
    hide louis

    "Louis想走开却发现Neo的动作把他离开的路堵死了"

    show louis with Dissolve(0.3)
    louis "我还有课，可以走了吗？"

    hide louis
    show neo with Dissolve(0.3)
    neo "距离你的课还有两个小时呐"
    hide neo

    "Neo一边说一边看着Louis"

    show louis with Dissolve(0.3)
    louis "蛤？"

    hide louis
    show neo with Dissolve(0.3)
    neo "把手机给我，我就让你过去。"
    hide neo

    menu:
        "Louis经过无数次的内心挣扎，决定"

        "给":
            $pts+=1

            "Louis不想在这里拉拉扯扯的了决定还是把手机拿出来"

            show louis with Dissolve(0.3)
            louis "呐"
            hide louis

        "不给":

            show louis with Dissolve(0.3)
            louis "不给"
            hide louis

            "Louis不想和Neo有过多的牵扯，想把Neo推开"

            "Louis用尽了吃奶的力气，Neo还是纹丝不动"

            show neo with Dissolve(0.3)
            neo "你加我好友，我就让你过去，还是说你想让我一直来找你？"
            hide neo

            "Louis无奈，把手机交给了Neo"

    show neo with Dissolve(0.3)
    neo "你不许像刚才那样看别人，也不许对别人撅嘴，听见没有，我不喜欢，一点都不好看。"
    hide neo

    "Neo一边用Louis的社交账号添加自己一边说"

    show louis with Dissolve(0.3)
    louis "现在可以放我走了吗？"
    
    hide louis
    show neo with Dissolve(0.3)
    neo "等等我先把我手机号存上"
    hide neo

    menu:
        "Neo吧自己手机号存成"

        "A Neo Nimtawat":

            "Neo把自己手机号存成了A Neo Nimtawat"

            show neo with Dissolve(0.3)
            neo "这样的话，以后打开通讯录看到的第一个人就是我了"
            hide neo

        "Nemo":

            $pts+=1
            
            "Neo把自己手机号存成了Nemo"

            "想了想给名字后面还加了个可爱的小鱼"

            "接下来Neo用Louis的手机给自己打电话"
            
            show neo with Dissolve(0.3)
            neo "Louis吗，存个什么名字好呢"
            hide neo

            "Neo想了一下，把名字存成了L，后面还有个小爱心"

    show neo with Dissolve(0.3)
    neo "呐，还你"

    neo "去上课吧，你上课时间快到了"

    hide neo
    show louis with Dissolve(0.3)
    louis "不对"

    louis "你怎么知道我的课表？"

    hide louis
    show neo with Dissolve(0.3)
    neo "Phuwin是我弟弟。"

    neo "对了，我找你的时候你必须接电话，不然我还会来"

    neo "你不想让Pond担心吧。"

    hide neo
    show louis with Dissolve(0.3)
    louis "你为什么要找我"

    louis "你不是说了没有喜欢我吗"

    louis "那我们应该当陌生人就好"

    hide louis
    "Neo听着这句话觉得有点刺耳，怎样才能让他闭嘴呢"

    "Neo把Louis压在书架上，亲了上去"

    "味道是草莓味的果冻，又香又甜，这样想着还吸了一下"

    show neo with Dissolve(0.3)
    neo "你要是不听话，下次被我逮住，可就不只如此了。"
    hide neo

    "说完捏了捏Louis肉肉的脸颊"

    show neo with Dissolve(0.3)
    neo "走了，记得回我消息还有接我电话"
    hide neo

    "说着Neo就走了"

    scene neoroom
    play music "audio/bothhome.mp3" fadeout 1.0 fadein 1.0

    "Neo有了联系方式后，就开始不断的发消息给Louis"

    show chat1 at topleft
    neo "在吗？"

    hide chat1
    show chat2 at topleft
    neo "Louis？"

    hide chat2
    show chat3 at topleft
    neo "不是让你一定要回我消息吗"

    hide chat3
    show chat4 at topleft
    neo "再不回我的话..."

    hide chat4
    show chat5 at topleft
    neo "我就告诉你哥了"

    hide chat5
    show chat6 at topleft
    neo "还不回吗"

    hide chat6
    show chat7 at topleft
    neo "那我给你哥打电话"

    hide chat7
    show chat8 at topleft
    neo "就说我们除了睡了还..."
    hide chat8

    "Neo还在编辑消息，Louis电话就打了进来"

    show louis with Dissolve(0.3)
    louis "你到底想干嘛？我们明明什么关系都没有"
    hide louis

    "Neo听着电话里传来软糯的声音，想象对方奶凶奶凶的样子"

    show neo with Dissolve(0.3)
    neo "谁说我们没关系？我们亲过也睡过了。"
    hide neo

    "啪的一声，Louis把电话挂掉了"

    show neo with Dissolve(0.3)
    neo "所有我的信息你都要回，记住向我报告每天和谁在一起干了什么，还有不许你和同学过于亲密，特别是男生"

    neo "快回复我！"

    hide neo
    show louis with Dissolve(0.3)
    louis "你好无聊。没事别联系我。"
    hide louis

    scene school
    play music "audio/school.mp3" fadeout 1.0 fadein 1.0

    "俩人不在一个学院本来很难遇到，可是Neo在那之后总是以各种理由出现在医学院的教学楼"

    "比如..."

    show neo with Dissolve(0.3)
    neo "嗨我们又见面了"
    
    hide neo
    show louis with Dissolve(0.3)
    louis "额... 嗨"

    hide louis
    "比如..."
    
    show neo with Dissolve(0.3)
    neo "哈喽~ 你是不是逃课了，这个时间你应该在上课才对"

    neo "我先说我是来找我弟的，只是看到你才来打个招呼的"

    hide neo
    show louis with Dissolve(0.3)
    louis "为什么上个厕所还能遇到你..."
    hide louis

    "比如..."

    show neo with Dissolve(0.3)
    neo "在吃饭吗？一起啊"

    neo "你喜欢吃这个吗？"

    hide neo
    show louis with Dissolve(0.3)
    louis "我吃完了，你自己吃吧我走了"
    hide louis

    "比如..."

    show neo with Dissolve(0.3)
    neo "等巴士回家吗？上车我载你回家"

    neo "绝对不收你一分钱"

    hide neo
    show louis with Dissolve(0.3)
    louis "不用了，我在等我哥。"
    hide louis

    "比如..."

    show neo with Dissolve(0.3)
    neo "你接下来没课了吧？"

    neo "本来约了我弟去看电影的，但他临时有事，要不你陪我去看吧"

    neo "要是你不去的话这个票就浪费了"
    hide neo

    "Louis想想其实最近Neo除了有点烦，也没对他做什么，人也挺好的"

    show louis with Dissolve(0.3)
    louis "今天下课后好像也没事，行吧"
    hide louis

    scene shoppingmall
    play music "audio/shoppingmall.mp3" fadeout 1.0 fadein 1.0

    "看完电影之后"
    
    show neo with Dissolve(0.3)
    neo "你要先吃饭还是逛逛街再吃"
    hide neo

    menu:
        "Louis想了想决定"

        "吃饭":
            show louis with Dissolve(0.3)
            louis "吃饭吧，吃完就得回家了"

            louis "不然我哥会担心的"
            hide louis

            "吃饱后Neo就把Louis送回家了"

        "逛街":
            $pts+=1

            show louis with Dissolve(0.3)
            louis "先逛一下吧我还不饿"
            hide louis

            "Neo陪着Louis逛了街，也在逛街的时候知道了Louis喜欢什么东西"

            "之后Neo陪着Louis一起去吃饭，然后Neo才把Louis送回家"

    show louis with Dissolve(0.3)
    louis "辛苦啦，回家小心呐"
    hide louis

    scene neohome
    play music "audio/bothhome.mp3" fadeout 1.0 fadein 1.0

    "晚上"

    show neo with Dissolve(0.3)
    neo "我明天可能还要去你学院一趟，要我载你回家吗？"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "呵，做了二十年的兄弟，第一次感受到我哥这么爱我，爱我爱到寸步难离了吗。"

    phuwin "不用了，我约了隔壁栋的医学生去看电影"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "你们学院每天的课那么多，大家应该都很忙吧？"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "还行，怎么了？"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "Louis和谁关系好？我看他总是点赞Tony。你就不能和他在一起多玩玩吗？"

    hide neo
    show phuwin with Dissolve(0.3)
    phuwin "我和他的专业方向又不一样，再说，他有自己的朋友，我也有"

    phuwin "哥，你实在不行转到我们专业吧，二十四小时看着他，你这么喜欢他，和他告白啊。让他知道，这样你就能光明正大的去找他了"

    hide phuwin
    show neo with Dissolve(0.3)
    neo "转专业是不可能的别想了我都快毕业了"

    neo "至于告白我还得琢磨琢磨"
    hide neo

    scene school
    play music "audio/school.mp3" fadeout 1.0 fadein 1.0

    nvl clear

    full "接下来的好几个月，Neo一直做着一样的事情：上课，下课，找Louis"

    full "Louis也从一开始对Neo特别抗拒直到习惯了天天看到他"

    full "习惯了一下课就有人在课室外等着"

    full "习惯了和Neo一起吃饭，听着他在旁边叭叭叭"

    full "直到..."

    scene neoroom
    play music "audio/sea.mp3" fadeout 1.0 fadein 1.0

    "某个周末"

    show neo with Dissolve(0.3)
    neo "Louis"

    neo "有空吗？"

    neo "等下到海边和我见面吧"

    neo "有重要的事情要说"

    hide neo
    show louis with Dissolve(0.3)
    louis "重要的事吗？"

    louis "好吧"
    hide louis

    scene sea

    show louis
    louis "你想和我说什么？"
    
    hide louis
    show neo with Dissolve(0.3)
    neo "我喜欢你"

    neo "虽然我之前说了一些话，但都不是我的真心，我也不知道，为什么那么在意你"

    neo "一想到你不理我，我就难过"

    neo "你和别人多说话，我就生气"

    neo "你对别人点赞的多，我就嫉妒"

    neo "我想这就是喜欢，我只想让你在第一时间注意我"

    neo "我可以请求你成为我的男朋友吗？"
    hide neo

    "Louis没有说话，就这么看着Neo的眼睛"

    "几分钟后..."

    if pts >= 5:
        show louis with Dissolve(0.3)
        louis "其实...我也喜欢你"
        
        louis "虽然你的性格不是很好"

        louis "虽然我们相遇的过程不是很愉快"

        louis "但是经过这段时间，我发现你在我心中的份量越来越重"

        louis "所以"

        louis "我接受你的告白了"

        louis "男朋友"
        hide louis

    else:
        show louis with Dissolve(0.3)
        louis "好，我们试一试。"

        louis "虽然我们可能性格不太合"

        louis "但是你说的很真诚，我愿意和你试一试"
        hide louis

    "Neo愣了一下，反应过来后飞快的抱住了Louis"

    if pts >= 5:
        show neo with Dissolve(0.3)
        neo "你现在是我的男朋友了"
        hide neo

        scene nlkiss
        "Neo说完飞快地在Louis嘴上啄了一下"

    scene sea
    show neo with Dissolve(0.3)
    neo "我一定不会让你有机会反悔的。我喜欢你。"
    hide neo

    "我遇见了一个少年，我也说不出他哪里好，但是我一见他就会笑，一想到他便觉得春光明媚。我想这应该就是喜欢了。"

    jump endLabel

    # 此处为游戏结尾。

    return
