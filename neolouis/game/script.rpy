﻿# 游戏的脚本可置于此文件中。

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
define char = "f"
define final = 0


# 游戏在此开始。

label start:

    scene hoteldoor

    # show eileen happy

    # 此处显示各行对话。

    "Neo二十岁生日那天，朋友们请他去酒吧庆祝，酒过三巡，大家说要送他一个成人礼物，于是给了他一张房卡，送他进入电梯。"

    neo "611，611在哪"

    neo "到了"

    "说着用房卡去开门，但是总打不开，于是开始用力敲门"

    neo "开门，不是说要给我礼物吗！"

    "半分钟之后..."

    scene dooropen

    "房门被打开了"

    scene hotelroom

    "还没等房门里的人问话，他就一把抱住了眼前的男孩子，整个身体都压在他的身上，头枕在对方的肩膀上，用鼻尖嗅着对方的脖颈"

    neo "你真好闻。这个礼物，我喜欢。"

    "说着就把人往房间里推，男孩子挣扎起来，可是双方力气悬殊太大，Neo直接把对方带到床上"

    louis "放开我，我不是……"

    "Neo酒劲上来，只看见软嘟嘟的嘴唇，像是水果糖，于是亲了上去，他心里想，这下安静了，之后不顾对方挣扎把人锁进自己的怀里，抱着睡着了。"
    
    "这一觉睡到极好"

    "Neo梦见了自己好像被云层裹挟着，又软又香很是舒服，直到自己被外力拉扯醒来"

    "他睁开眼睛看见床边站着俩个人，一下子全醒了坐了起来"

    neo "你们是谁？"

    louis "嗯～，好吵"

    louis "哥，Dunk，你们来了，家里怎么说？同意我不去国外了吗？"

    pond "Louis，说说看，怎么回事，他是谁？"

    louis "我不认识他，我昨天乖乖在房间里等你来接我，然后有人敲房门，我去开了，他就把我抱住了，我想挣脱，但是没成功，然后就是你们看见的样子了。"

    pond "你的嘴巴怎么回事？别告诉我说睡了一觉肿了。"

    "Louis脸刷的就红了，舌尖抵上了唇内的一个破口，Neo也瞟向了他的嘴唇，被Louis瞪了回去。"

    dunk "你们昨天还有发生什么事吗？"

    neo "什么都没有，我昨天喝醉了，我还想问呢？为什么在我的房间？你们想干什么？仙人跳？"

    louis "什么你的房间？这明明是我定的！"

    neo "这是601，我有房卡，怎么会是你定的？"

    louis "607，这间房是607！"

    pond "你是谁？把你的证件拿出来"

    pond "要是我弟弟有什么事，我不会放过你！"

    "Pond说着去翻了Neo外套的口袋，从那里找到了身份证和学生证，拍了照"

    pond "把电话号码给我"

    neo "为什么"

    pond "给我！"

    neo "哦...."

    "拿了电话号码之后， Pond把Louis从床下拉了下来"

    pond "不要再接近我弟"

    "Pond说完就带着Louis和Dunk一起离开了"

    scene car

    pond "你和他是不是在学校就认识了？"

    louis "他和我是一个学校的吗？我没看过他。医学院里没有这号人物。"

    "说完Louis向Pond撒娇"

    louis "哥哥，我不想出国，我长这么大都没有离开过你，你就帮我和爸妈再说说吧！"

    louis "不然，等以后你出国工作。把我也带上，总之我现在不出去，要是你们执意如此，我下次再跑就不和你说了！"

    louis "哥哥，你会答应我的吧！"

    dunk "你是Pond的小尾巴吗？这么大还对着哥哥撒娇。"

    pond "我已经和爸妈谈妥了，但是你答应我在学校里不许和Neo接触，不然我会亲自送你出国。"

    louis "知道了哥"

    "Louis乖巧的点了点头，心里却默默记住了Neo的名字"

    "原来他叫Neo阿"

    scene school

    "周末很快结束了"

    "Louis从解剖课上出来，远远的就看见Neo站在学院楼的进出口"

    "Louis想着对哥哥的承诺，无视Neo的存在和同学一起走了"

    neo "为什么看到我，不和我打招呼？"

    "看着Louis无视自己，Neo有点不爽，扯住了Louis的手腕"

    louis "你是谁？"

    louis "我不认识你。"

    "怎么了，Louis？"

    "同学问道"

    louis "没什么，他可能认错人了，走吧。"

    neo "不认识，那谁在上周五晚上……"

    "话还没说完，路易就用另一只手捂住了Neo的嘴巴，在同学的惊诧中和Neo离开了。"

    scene car2

    "Neo带着Louis到车上"

    neo "现在认识了？"

    louis "你找我干什么？你怎么知道我在医学院的？"

    neo "我认识你哥，想找到你不是很简单吗？"

    louis "你找我干什么？"

    neo "谁说我找你了？我找我弟弟，是你拉我过来的。"

    "Louis听完后只觉得无语，想打开车门离开"

    neo "你在学校不要来找我，我们什么关系都没有，还有我不喜欢你这种类型的人，懂吗？别想借机缠上我。"

    "Louis甩开Neo还拉着他的手，头也没回就开门下车走了。"

    scene neohome

    "晚上..."

    phuwin "哥，你今天来医学院了？怎么没找我就走了？你是怎么认识Louis的？"

    neo "你怎么知道去医学院的？还认识Louis？"

    phuwin "你俩在学院门口拉拉扯扯，被人拍下来上传到网上了。你俩交朋友了？"

    neo "没有的事，我有些事要问他，再说我喜欢的是明艳动人的，他这种小兔子不是我的菜。"

    phuwin "那..."

    neo "不聊了，有事"

    "Neo没给Phuwin继续发问的机会，就回自己房间了。"

    scene louishome

    "另一边..."

    pond "说吧，昨天不是和我保证不和他联系，今天就被拍到照片，你之前到底认不认识他？"

    louis "不认识，他今天来找我，和我说所有场合都别和他讲话。照片什么的可能是被人拍照了，我不知情的"

    louis "你看我都没有他的联系方式"

    "说着Louis把手机拿出来给Pond看"

    "Neo请求添加您为好友"

    pond "那这是什么？"

    pond "拒绝了"

    "说着Pond替Louis拒绝了好友申请然后拿起自己手机打给了Neo"

    pond "你想对我弟干嘛？"

    pond "劝你别对我弟动什么心思"

    neo "我先说我绝对不会对Louis有好感，只是看见了网上的照片，想让他别乱想。"

    pond "最好是这样。你以后别再学校去找他，我自己的弟弟我自己可以照顾好。别再联系他。"

    "说完这句Pond就把电话挂了"

    pond "你要交友哥哥没意见，但是他不行，你从小就很乖，Neo心思太浮，不适合做你的朋友。"

    louis "哥哥，我从没想过和他做朋友，你别担心我。"

    "之后Louis又收到了Neo的交友请求"

    louis "还是拒绝吧"

    "Louis想着哥哥对自己说的还是拒绝了好友申请"

    scene library

    "第二天..."

    "Louis正在找外科的参考书籍"

    neo "你在做什么？为什么拒绝我的好友请求？"

    "Louis回头瞪了Neo一眼"

    louis "你想做什么？上次你说的话我明白了。"

    "Louis想走开却发现Neo的动作把他离开的路堵死了"

    louis "我还有课，可以走了吗？"

    neo "你等会不是没课吗？"

    "Neo一边说一边看着Louis"

    "此时Neo只觉Louis望向他的眼睛含着一汪春水，好想把他揉进怀里，弄哭他"

    louis "蛤？"

    neo "把手机给我，我就让你过去。"

    "Louis不想和Neo有过多的牵扯，想把Neo推开"

    "Louis用尽了吃奶的力气，Neo还是纹丝不动"

    neo "你加我好友，我就让你过去，还是说你想让我一直来找你？"

    "Louis无奈，把手机拿了出来"

    neo "你不许像刚才那样看别人，也不许对别人撅嘴，听见没有，我不喜欢，一点都不好看。"

    "Neo一边用Louis的社交账号添加自己一边说"

    louis "现在可以放我走了吗？"

    louis "不对！你怎么知道我的课表？"

    neo "Phuwin是我弟弟。"

    neo "还有我找你的时候你必须接电话，不然我还会来"

    neo "你不想让Pond担心吧。"

    louis "你来找我干什么？我们都不熟，我不想和你扯上关系。"

    "Neo把Louis压在书架上，亲了上去"

    "味道是草莓味的果冻，又香又甜，这样想着还吸了一下"

    neo "你要是不听话，下次被我逮住，可就不只如此了。"

    "说完捏了捏Louis肉肉的脸颊"

    neo "走了，记得回我消息还有接我电话"

    "说着Neo就走了"

    scene neohome

    "Neo有了联系方式后，就开始不断的发消息给路易"

    neo "在吗？"

    neo "Louis？"

    neo "不是让你一定要回我消息吗"

    neo "再不回我的话..."

    neo "我告诉你哥了"

    neo "还不回吗"

    neo "那我给你哥打电话"

    neo "就说我们除了睡了还..."

    "Neo还在编辑消息，Louis电话就打了进来"

    louis "你到底想做什么？我们什么关系都没有！别打电话给我哥哥，不然我可不会放过你！"

    "Neo听着电话里传来软糯的声音，想象对方奶凶奶凶的样子"

    neo "谁说我们没关系？我们亲过也睡过了。"

    "啪的一声，Louis把电话挂掉了"

    neo "所有我的信息你都要回，记住向我报告每天和谁在一起干了什么，还有不许你和同学过于亲密，特别是男生"

    neo "回复我！"

    louis "你好无聊。没事别联系我。"

    "俩人不在一个学院本来很难遇到，可是Neo在那之后总是以各种理由出现在医学院的教学楼"

    phuwin "呵，做了二十年的兄弟，第一次感受到哥哥如此爱我，以至于寸步难离的程度。"

    neo "你们学院每天的课那么多，大家应该都很忙吧？"

    phuwin "还行，怎么了？"

    neo "Louis和谁关系好？我看他总是点赞Tony。你就不能和他在一起多玩玩吗？"

    phuwin "我和他的专业方向又不一样，再说，他有自己的朋友，我也有"

    phuwin "哥，你实在不行转到我们专业吧，二十四小时看着他，你这么喜欢他，和他告白啊。让他知道，这样你就能光明正大的去找他了！"

    "周末"

    neo "Louis"

    neo "有空吗？"

    neo "等下到海边和我见面吧"

    neo "有重要的事情要说"

    louis "重要的事吗？"

    louis "好吧"

    scene sea

    louis "你想和我说什么？"

    neo "我喜欢你"

    neo "虽然我之前说了一些话，但都不是我的真心，我也不知道，为什么那么在意你"

    neo "一想到你不理我，我就难过"

    neo "你和别人多说话，我就生气"

    neo "你对别人点赞的多，我就嫉妒"

    neo "我想这就是喜欢，我只想让你在第一时间注意我"

    "Louis没有说话，就这么看着Neo的眼睛"

    "几分钟后..."

    louis "好，我们试一试。"

    "Neo愣了一下，反应过来后飞快的抱住了Louis"

    neo "我一定不会让你有机会反悔的。我喜欢你。"

    "我遇见了一个少年，我也说不出他哪里好，但是我一见他就会笑，一想到他便觉得春光明媚。我想这应该就是喜欢了。"

    # 此处为游戏结尾。

    return