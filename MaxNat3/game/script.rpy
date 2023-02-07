# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define new = Character('New', color="#ffff00")
define max = Character('Max', color="#f06ca9")
define nat = Character('Nat', color="#4fa6e8")
define pb = Character(None, kind=nvl, what_text_align=0.5, what_xalign=0.5)
define displayDay = Character(None, what_yalign=0.5, kind=nvl)
define pts = 0
# define narrator = nvl_narrator

screen Pts:
    text "Pts [pts]" xpos 0.87 ypos 0.106

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    show screen Pts

    play music "audio/happy_morning.mp3"

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show nunew worry with dissolve

    # 此处显示各行对话。

    new "Nat，你确定要这样吗？Max会生气的吧"

    hide nunew worry
    show nat happy with dissolve

    nat "没事的啦！我有分寸的"
    nat "我实在是等不下去了！"

    nvl clear
    pb "回想起那个习惯性当骑士，喜欢他这么多年却闭口不言只想等他成年的青梅竹马大哥哥Max，Nat情不自禁的笑了出来。"
    pb "这个傻子只会在一旁守护着他，一边暗地里偷偷吃醋一边假装理直气壮的赶走他身边出现的各个“危险人物”"
    pb "无辜躺枪的足球队大哥哥，班级里偷偷给他递情书的男生，酒吧里坐他旁边的帅哥……最后甚至连New的醋也开始吃了！"

    nvl clear
    pb "虽然之前也这样双方都心知肚明但不点破的等了好多年了，但最近就算只剩一个多月就到20岁了Nat也等不及了"
    pb "谁要Max那个前凸后翘的女秘书已经假装有公事实际上是到家门口来挑事宣战了呢！"

    nvl clear
    pb "于是接下来的几天，Max感觉他的骑士地位受到了前所未有的挑战。"

    hide nat happy

    play music "audio/fun_day.mp3" fadeout 1.0 fadein 1.0

    nvl clear
    displayDay "Day 1"

    $pts += 1

    show max stand with dissolve

    max "喂，New，可以告诉我Nat现在在哪里吗？我打不通他电话。"

    hide max stand
    show nunew worry with dissolve

    new "可能是快要期末考了，Nat和他的同学Tutor一起在图书馆复习吧？"

    nvl clear
    pb "刚说完New就听见汽车发动的声音和Max的谢谢再见一起响起，随后电话立马就被挂断了。"
    pb "而另外一边，在图书馆里一直看着手机反复亮起又暗下的Nat心里暗爽，嘴角忍不住勾起一抹坏笑。"

    nvl clear
    displayDay "Day 2"

    $pts += 1

    hide nunew worry
    show nat happy with dissolve

    nat "p’Max怎么啦？刚刚在和朋友打电话没接到你电话，不好意思呀。"
    "Nat趴在床上，悠闲地晃着小脚丫回复Max的消息"

    hide nat happy
    show max stand with dissolve

    max "刚刚n’Nat是在和谁打电话？"
    "Max立马警觉的问道"

    hide max stand
    show nat happy with dissolve

    nat "只是同班的同学啦？问了几个考试有关的问题再闲聊一下天啦，我困啦，p’Max晚安"
    "说完便立马关上手机，不再理会那头Max接下来的提问，翻了个身沉沉的睡去。"

    hide nat happy

    nvl clear
    displayDay "Day 3"

    $pts += 1

    "正好是周五，Nat和一群同学刚参加完音乐节目"
    "突然拍了拍身边的Tutor，趁着对方抬脸，迅速的拍了一张合照"

    show twitter ss at topleft with dissolve
    "传到twi上并配文 “真是一个美好的夜晚” 还顺带@了Tutor"

    "至于Max在下面留言的一堆问号..."
    "那当然是放置play啦！{fast}"

    hide twitter ss
    nvl clear
    pb "哦对了，还要和家里的阿姨们打好招呼说p’Max来问的话就说要半夜才回家"
    pb "嘻嘻。"

    nvl clear
    displayDay "周六"

    "Nat刚起床准备到餐厅去吃早餐时一眼就看到了在自家客厅的Max。"

    show nat happy with dissolve
    nat "p’Max，你怎么来啦！"
    "Nat笑盈盈的看着眼眶底下青黑一看就是没睡好的Max问道。"

    hide nat happy
    show max stand with dissolve
    max "你还好意思问！你昨晚去哪了？怎么可以这么晚都不回家？{fast}"
    "max气冲冲的质问道"
    max "你知不知道我有多担心你！{fast}"

    hide max stand
    show nat happy with dissolve
    nat "我昨晚和朋友去玩了呀？我已经是大人了，哥哥不用担心我的安全的。还是说哥哥怕我被其他人拐跑了呀，嗯？"

    hide nat happy
    show max stand with dissolve
    max "我…我…我就是怕你的朋友是坏人"

    hide max stand
    show nat happy with dissolve
    nat "可是Nat的爸爸妈妈都没有担心耶"
    nat "p’Max又是以什么身份来担心我呢？如果是邻家哥哥的话，好像管不了这么多呢？除非是我男朋友才管得到呢"

    hide nat happy
    show max stand with dissolve
    max "你…"
    max "我…"
    max "那…"
    "Max憋了半天都说不出一句完整的话"
    "最后沉沉的深呼吸一口气, 大声的喊道"
    max "那就请你做我的男朋友好吗？让我来管你！你不要再和别人那么亲近了！"
    "说完只敢紧紧的闭着眼睛，害怕在看到Nat可爱的脸上看到任何拒绝的神情。"
    menu:
        "答应他":
            $pts += 1
            jump accept
        "拒绝他":
            jump reject

label accept:
    hide max stand
    show nat happy with dissolve
    "然而什么拒绝都没有"
    "Nat在Max的嘴上轻轻的啄吻了一下"
    nat "好吧，我答应你了"
    "Max一听，立刻高兴的睁开眼睛，紧紧的抱住了Nat"
    "然后捧着Nat的脸颊来了个并不熟练的深吻"

    nvl clear
    pb "等两人都吻得晕晕乎乎时"
    jump afterSel

label reject:
    hide max stand
    show nat happy with dissolve
    "我才不要"

    hide nat happy
    show max stand with dissolve
    "Max慌张的睁开眼睛"
    max "为…为什么呢？是对我有什么不满意吗"

    hide max stand
    show nat happy with dissolve
    "Nat看着眼前慌张的大总裁，忍不住笑了起来"
    "笑完后抬手戳戳Max的脑袋"
    nat "因为你这傻子让我等太久啦！"

    hide nat happy
    nvl clear
    pb "Max听完愣在了原地"
    pb "日理万机的脑袋此刻竟然理解不了一句短短的话。"

    "看着眼前这个不知所措的Max，Nat心想还是自己主动吧"
    "这样想着....Nat在Max的嘴上轻轻的啄吻了一下"

    nvl clear
    pb "这时Max终于回过神来"
    jump afterSel


    # 此处为游戏结尾。

    return
