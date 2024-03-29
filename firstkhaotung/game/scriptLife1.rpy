﻿# 游戏在此开始。

label life1:

    scene ktroom

    # 此处显示各行对话。

    "First已经不知道多少次梦见Khaotung了，他还记得第一次进公司的时候，他在人群里看到Khaotung，只是一个侧脸，First就觉得似有似无的藤蔓开始缠绕在心尖。"

    "后来他们认识了，是在一次公司为了增进新人感情所举办的聚会上，First看着坐在角落的Khaotung，耀眼的霓虹灯照在他的脸上，First第一次看清Khaotung的全脸。"

    "青涩，精致，可爱。"

    "First的脑子里蹦出这三个词的时候，自己都吓了一跳，看着手里的酒，不由得嘲笑自己一定是酒精上头了，竟然想夸一个男孩子可爱。"

    menu:
        "要不要上前打招呼"

        "要":
            $fkt += 1
            f "能交个朋友吗？"

            "First心尖的那根藤蔓又再长了，所以他拎着酒杯跨过重重人群坐到了Khaotung身边。"

            "Khaotung有些吃惊，First竟然会主动来找他，他其实有注意到First，即使是昏暗的酒吧，也掩盖不了First清澈的大眼闪着光芒，那个感觉，很是熟悉。"

            kt "当然可以。"

        "不要":
            "Khaotung盯着不远处的First陷入沉思，那双大眼睛如此熟悉，看到人躲避了几次交汇的眼神，端起身前的酒杯朝First方向走去。"

            kt "能交个朋友吗？"

            "First有些吃惊，出于礼貌的点了点头，对人报以微笑，昏暗的灯光看不到他泛红的耳廓。"

    "两人碰了手里的杯子，开始有一句没一句的聊着。"
            
    f "诶，竟然是同岁啊，但我比你大，你应该叫我哥。"

    kt "是的，但也只大几十天。"

    f "那也是比你大。"

    "这时不远处有一个醉醺醺的中年男人端着酒杯直奔Khaotung。"

    "中年男人" "来一起喝一杯。"
    
    "Khaotung盯着酒杯轻微皱眉。"

    menu: 
        "其他人来对烤糖劝酒 First"

        "替他挡酒":
            $fkt += 1
            "First看到后直接伸手接过人的酒杯。"

            f "抱歉我朋友今天身体不太舒服，我替他喝。"

            "First不等人说什么，就举起自己的酒杯一饮而尽，Khaotung微微挑眉。"

            "男人似乎不能说什么，举着酒杯悻悻的离开了。"

        "问候他":
            "还没趁First反应过来，Khaotung直接举起酒杯一饮而尽，男人很开心的喝光自己手里的酒，继续向Khaotung靠近，却被Khaotung咳嗽声阻挡。"

            kt "抱歉先生，我可能需要离开这里"

            "Khaotung转身就走，First连忙撂下酒杯追了出去。"

            f "你怎么样？"

            kt "没事，我只是不太喜欢酒局"

    "First看着人并没有受影响，依旧笑的眉眼弯弯，心头的藤曼似乎在发疯了长，First不由得捂上心口，神情恍惚，他搞不明白最近怎么了，是不是要做一个全身的体检了。"

    "Khaotung有些担心的看着面前的人捂着胸口，上前扶住人，低声在人耳边询问。"

    kt "你还好吗？需要我送你回家吗？"

    "First微微歪头对上Khaotung的眼神，犹豫了一下。"

    menu: 
        "要不要让Khaotung送回家"

        "接受": 
            $link += 1
            "鬼斧神差的点了点头"

            "直到出了酒吧，曼谷夜晚的风扑在First脸上，First才清醒过来。"

            "看着身边架着他的Khaotung，连忙抽走了手，然后道歉。"

            f "对不起，不麻烦你了，我可以自己回去的。"

            kt "你确定吗，你可是喝了不少酒，我送你吧。"

            "First依旧没有拒绝，他今晚的拒绝似乎说不出口。"

            "曼谷夜晚的风带来了一些清凉，吹醒了First，可吹不散心头的那株藤蔓。"

        "拒绝":
            "First摇了摇头"

            f "对不起，不麻烦你了，我可以自己回去的。"

            kt "你确定吗，你可是喝了不少酒，我送你吧。"

            "Khaotung架着人的胳膊，把人送上自己的车。"

    f "谢谢你送我回来。"

    "First站在公寓门口对眼前人表示感谢。"

    "清澈如水的眼睛在黑夜里更加灵动，眼睫毛扑闪扑闪的引得Khaotung心痒痒，不由得笑出了声。"

    kt "没事，举手之劳。"

    

    menu:
        "First给人倒了杯水，看着人眉眼弯弯，内心在思考是否要问人加个联系方式"

        "问": 
            $link += 1

            "First决定遵从内心，拿出自己的手机"

            f "能留个联系方式吗"

            "Khaotung愣了一下，但很快点头说好，拿出自己的手机。"

        "不问":

            "First终究没有开口，他觉得太冒犯了。"

            kt "如果方便的话可以留一个联系方式。"

            "Khaotung的声音响起，First愣了一下，点了点头，然后慌乱的拿出手机。"

            f "当然方便。"

    "那一夜的晚风都是甜的，First在那一晚迎来了他生命中重要的人。"

    kt "fir。"

    "First抬头对上Khaotung的眼睛，今天是他们一起在公司开会的日子，结束后两人商量着一起去吃饭，坐上副驾就听见人似乎在喊自己的名字。"

    kt "我可以这样叫你吗？"

    menu:

        "可以这样叫吗？"

        "可以": 
            
            "First对上人的眼神，微微皱眉装作一副有些嫌弃的样子点了点头。"

            f "爱怎么叫怎么叫，反正也不叫我哥。"

        "叫哥":

            $fkt += 1

            f "你得叫我哥。"

    kt "你只比我大四十天。"

    "First微微撇嘴不再接话，扣好了安全带找了一个舒适的姿势开始玩手机，过了一会儿，突然抬头看着正在开车的Khaotung。"

    f "tung"

    kt "嗯，怎么了？"

    f "没事，这样叫比较亲切。"

    "Khaotung转头对上人带些小机灵的眼神，不由得也跟着笑出了声，他这个朋友可是一点都不简单。"

    "First很粘人很闹腾，是Khaotung想不到的粘人很闹腾，准确来说Khaotung之前总喜欢一个人静静地待着，但是First的出现后，Khaotung生活有些不一样了。"

    f "tung，今天公司活动，结束后要不要逛街。"

    f "tung，有一家好吃的烤肉店，要不要一起。"

    f "tung，有粉丝给我做应援诶，要去打卡吗？"

    f "tung，我看到一个款游戏，感兴趣吗？"

    menu:
        
        "今天有个粉丝应援，要不要叫上烤糖一起去打卡"

        "要":
            
            $link += 1

            "First兴致勃勃的把消息发送给Khaotung，得到了回应后，First已经在思考那一天要穿什么了。那是他们第一次一起去打卡应援，而往后会有很多次。"

        "还是算了":

            "First半夜刷到的时候在想自己是不是太闹腾了，Khaotung似乎每次都很疲惫，First犹豫再三没有把消息发出去。"


    "之后First甚至已经成功的在khaotung的公寓，获得一点自己的位置，他窝在沙发上刷推时，看大别人再买衣服，动了做品牌的心思，抬头看了一眼Khaotung。"

    menu:

        "想做一个自己的品牌"

        "问烤糖是否要一起做":

            $link += 1

            f "tung，我们要不要做个自己的品牌啊，卖卖衣服什么的。"

            "First看着发呆的人，知道人又没有再听，气鼓鼓的丢出去一个抱枕。"

            "Khaotung思绪被拉回来，看着一脸怨气的First，宠溺的叹了口气，捡起身边的抱枕。"

            kt "我有在听，可以啊，刚好公司也同意提供支持，不如就试试。"

            f "好诶。"

        "告诉烤糖自己的想法":

            f "我想做一个自己的品牌。"

            kt "可以啊，刚好我也有相同的想法。"

            f "真的吗！刚好可以一起啊。"

    "Khaotung看着又咧开了嘴角First，忍不住跟着勾起嘴角。"

    "两人事务更加繁忙，日子过得很快，Khaotung的生日要来了，公司提出举办生日会，有很多粉丝也会来。"

    "First作为好友也当然也会去，只是看着经纪人发来的场地布置邀请和手中挑选礼物的界面陷入了思考。"

    menu:

        "烤糖的生日快到了"

        "去帮忙布置现场":

            $link += 1

            "First看着快要挑好的礼物，回复经济人自己马上到，自己当然要在现场留下自己布置的小惊喜。"

        "询问烤糖想要什么礼物":

            "First看了看炎热的天气还是会绝了经纪人的邀请，选好礼物下单，期待着人收到礼物是的表情。"

    "First工作完一天，劳累的躺在床上。"

    f "呼，太累了，终于到家了。"

    "First瘫在床上，看着Khaotung发来的消息，笑着回了几句，眼皮就有些发沉，翻了个身伸手按灭了灯，浑浑噩噩的睡了过去。"

    "叮当，叮当，叮当。"

    "First觉得自己脑子要炸掉了，伸手按掉闹钟。"

    "明亮的阳光透过窗户扑在他脸上，他皱着眉用被子蒙着头，迷迷糊糊之间似乎还在思考什么。"

    "逐渐清醒时，有些懵的坐起身，抬手揉了揉自己的头发，觉得自己似乎忘了什么，但又想不起来。"

    f "好像做了一个奇怪但又想不起来的梦。"

    "First看了一眼枕头，果然熟悉的泪痕出现在上边，他叹了口气，起身去洗漱，一会儿还要赶着去Khaotung的生日会。"

    "First到的时候Khaotung已经在准备了，他穿着自己品牌的衣服，接受着经济人的拍照，First一眼看到了Frank，凑了过去坐在了人身边，跟人聊着生日会作为布置。"

    "突然抬头看到了放在桌子上的蛋糕。"

    menu:

        "First看到了蛋糕 询问Frank"

        "待会儿谁端蛋糕？":

            f "一会儿谁给他端蛋糕。"

            "First薅了一把有些凌乱的头发，然后轻轻晃脑袋让头发更加顺滑。"

            frank "咱一起啊。"

        "等下一起端蛋糕吗？":

            $link += 1

            "First不知道谁要给Khaotung端蛋糕，通常都会选择最亲密的人，First环视了一周也没有看到Khaotung的家人，直接扭头问Frank。"

            f "一会儿我们一起端蛋糕吧。"

            frank "本来就是我们啊，你睡迷糊了。"

            "可是First有些疑惑，不知道什么时候他已经跟Frank沟通过要端蛋糕的事。"

    "Frank往嘴里塞了一块橘子，剩下的递给First，示意人尝一块，被First拒绝推开了。"

    f "行。"

    "First刚想离开座位去找Khaotung，工作人员举着手机拍了过来，First从容的打了声招呼。"

    "工作人员" "为什么来的这么晚？"

    f "因为要陪到他最后一刻。"

    "工作人员" "那为什么不一开始就在，要晚一点出现"

    "工作人员和First打趣着，First笑了笑，脑子里突然蹦出来一句话。"

    f "因为留到最后的人，才是对的人。"

    "工作人员开始起哄，First的脑中也嗡了一声，他不知道为什么会说这句话，他依旧很得意的看着镜头，心理盘算这句话从何而来。"

    "镜头转走，Frank手搭了上来，似笑非笑的调侃人。"

    frank "兄弟，敢说啊，这话听着真肉麻。"

    f "去去去，别调侃我。"

    "Frank阴阳怪气的学了两句躲开人的追打去找其他同事聊天去了，First看着Frank和摄像的离去，耳尖更加的红。"

    menu:

        "饭卡走开了"

        "去找烤糖诉苦":

            $link += 1

            "起身越过人群，找到了最前边正在吃东西的Khaotung，坐在了人的身边。"

            f "我给你说，不知道为什么今天睡醒很累，差点迟到。"
            
            kt "那你还好吗？"

            "Khaotung咽下最后一口米饭，看着坐在身边有些苦闷的First有些担心。"

            "First摇了摇头，示意自己没事，刚想继续说下去，经纪人就提示生日会要开始了，First拍了拍Khaotung的肩膀当做鼓励，就起身离开了。"

        "自己待着":

            "First看了一眼最前排在吃饭的Khaotung思考再三决定先不去打扰人，自己刷这手机掩盖着内心的燥热。"

    "Khaotung拿着话筒和在场的粉丝的互动，坐在不远处的First拉着Frank看着时机差不多了，悄悄离开了人群，去端蛋糕。"

    f "Happy birthday to you"

    "生日歌响起，First和Frank端着蛋糕穿过层层粉丝慢慢的走向Khaotung。"

    "Khaotung有些惊喜的看着两人手里的蛋糕，因为这是一个小惊喜，他对上First喜悦的眼神，听着周围的生日歌，眼底泛着泪花。"

    f "快许愿啊。"

    "First看着愣在原地的Khaotung，连忙提醒人，Khaotung回过神，闭上眼睛，许了愿望，然后吹灭蜡烛，人群沸腾欢呼。"

    "Khaotung看着一起欢呼的First，在心底说了一句谢谢。"

    "等一切都结束了，两人坐在车上，他们还有工作要赶回公司，First还在回味刚才生日会上的情节，看着专注开车的Khaotung，在思考刚才的愿望。"

    menu:

        "要不要问烤糖许了什么愿望"

        "问":

            $fkt += 1

            f "你许的什么愿望？"

            "生日会结束，在回去的路上First刷着推特，无聊的抛出了这个问题，Khaotung摇了摇头。"

            kt "说出来就不灵了。"

        "不问":

            "First觉得有些唐突，还是没问出口。"

            "Khaotuang瞄了一眼副驾的First，内心要想逗人一句。"

            kt "你不想知道我许了什么愿望吗。"

            f "什么愿望。"

            kt "不告诉你，说出来就不灵了。"

    "First看了一眼在带着些许嘚瑟的Khaotung笑出了声。"

    "生活又回归了平淡，First经常会找Khaotung聊各种事，两人很契合在各个方面都让对方很舒服。"

    "像往常一样下班后，First拎上自己的包直接去找Khaotung，看到在捣鼓手机的Khaotung直接手臂搭了上去。"

    f "Tung，今晚我家，新游戏怎么样。"

    kt "可以啊。"

    "Khaotung并没有防备，直接答应了，手上继续编辑着自己的推文。"

    menu:

        "烤糖正在编辑推特"

        "帮烤糖收拾好东西":

            $fkt += 1

            "First伸手收拾好人的东西，听到Khaotung嗯了一声，就拉着Khaotung直奔停车场，等编辑完了，抬头已经在gmm大楼外了。"

        "在旁边等着烤糖":

            "First看到Khaotung在忙，也没有好好回应，就在原地等了一会儿，等到Khaotung再次抬头，First对上人的眼神。"

            f "搞完了吗？走吧。"

    kt "嗷，要干嘛？"

    f "打游戏啊，你刚才同意了。"

    "Khaotung来不及反应，First已经连推带拉的把人塞进车里了。"

    "Khaotung不得再次感叹First每天真的精力充沛。"

    f "我觉得，我们可以先吃个饭，然后直接开始打游戏，今晚可以通宵。"

    "Khaotung一边听人说话，一边系好安全带，然后调整了一个舒服的姿势，开始闭目养神。"

    "这应该是他俩认识的第二年，First在公司里每天都像开心小猫一样，喜欢在各个工位之间乱窜，跟每一个人都能搭得上话，最成功的便是可以跟自己的偶像tay玩闹。"

    "Khaotung属于很安静的人，他也喜欢和人玩闹，但更多的时候，喜欢一个人呆着看着人玩闹。"

    "虽然First每次看到他都喜欢把他从座位上薅起来，但他依旧大部分情况下喜欢一个人呆着。"

    "Khaotung睡得并不安稳，睁开眼舒展一下身体发现车子正在等红绿灯，而First正在刷着推特。"

    kt "在看什么？"

    f "想出去旅游。"

    "天色有些黑了，车内昏暗使得First的眼睛更加灵动，看的Khaotung内心痒痒。"

    kt "你想去哪旅游。"

    menu:
        "要去哪里旅游"

        "爬山":

            f "爬山？也可以如果你喜欢的话。"

            "Khaotung不是很喜欢太剧烈的运动，相比爬山他有些想去海边，但如果First喜欢他也会尝试着去做。"

        "海边":

            $link += 1

            f "海边吧"

            "绿灯亮起，心意不谋而合，Khaotung点了点头。"

            kt "我认同，可以去海边看日出。"

    "First默默地把旅游加入计划清单。"

    "而现在First要拉着Khaotung玩游戏，炎热的日子里只要没了工作，就喜欢拉着Khaotung去自己家玩游戏。"

    kt "朋友要先吃个饭吗？"

    f "我觉得可以，楼下有一家不错的餐馆就去哪。"

    "First和Khaotung来到餐厅，随意点了点东西，等待上菜的间隙，First看到一旁坐着的老板满脸喜悦。"

    menu:

        "饭店老板看起来很开心，好像有什么喜事"

        "询问老板":

            $link += 1

            f "叔叔，今天怎么这么高兴。"

            "老板" "我儿子新给我发来的结婚请帖，他跟对象在国外领证。"

            f "国外领证？"

            "老板" "因为那个孩子也是个男孩。"

            f "哦，那恭喜叔叔"

            "老板" "哈哈哈，谢谢，今天给你们打折。"

            f "谢谢叔叔。"

            "Khaotung和First向老板道谢，First有些惊讶的跟Khaotung讨论。"

            f "很勇敢啊。"

            kt "是啊。"


        "不询问":

            "First认为没礼貌也没有询问，两人吃完饭就回家了。"

    "饭很快就端上来了，两人吃完就回家开始打游戏了。"

    f "诶诶诶，朋友，用点心，诶诶诶，要死了。"

    "First重重的叹了口气，看了一眼身边在打哈欠的Khaotung，忍不住也打了个哈欠，眼泛泪花的First抬头看了一眼表，已经是凌晨六点。"

    "身边的Khaotung拍了拍First的肩膀，艰难的站了起来，舒展了一下身体。"

    kt "睡觉吧，太晚了。"

    menu:

        "有点困了"

        "现在就去睡":

            $link += 1

            "First也起身，随意的倒向身后的床，把自己的头埋进枕头里，Khaotung艰难的抬了抬眼皮，看了一眼躺在床上的First，摸索着站起身，然后躺在人身边。"

            "本来想着喊人换个衣服再睡，但是实在没有力气，喊了几声fir后，自己也意识模糊了。"

        "再打一盘":

            "First摇了摇头说要再打一盘，Khaotung实在承受不住，直接起身去睡觉，First只好也起身躺回床上很快的进入了梦乡。"

    jump endLabel

    # 此处为游戏结尾。

    return
