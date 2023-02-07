# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后
label jfCar:

    # 车上

    "Boss和Noeul在聊些什么，First还没反应过来，俩人已经离开了店铺。"

    show first with Dissolve(0.3)
    first "诶，怎么走的这么急。"

    hide first
    show ja with Dissolve(0.3)
    ja "好了，我们该回家了，Udon和Sancho要喂食了。"

    hide ja
    show first with Dissolve(0.3)
    first "可是出来的时候不已经喂过了吗？你脸色怎么这么不好，诶诶诶走慢点。"

    hide first
    "First快走几步跟了上去，Ja的脸色不好让自己有些忌惮，心里盘算着原因，却也摸不着头脑。"

    scene car2

    show ja with Dissolve(0.3)
    ja "你今天好像很开心。"

    hide ja
    show first with Dissolve(0.3)
    first "其实也没有。"

    hide first
    show ja with Dissolve(0.3)
    ja "为什么。"

    hide ja
    show first with Dissolve(0.3)
    first "蛋糕没吃完就扔了。"

    hide first
    show ja with Dissolve(0.3)
    ja "太晚了，我们应该回家了。"

    hide ja
    show first with Dissolve(0.3)
    first "你今天很反常。"

    hide first
    show ja with Dissolve(0.3)
    ja "有吗？"

    hide ja
    show first with Dissolve(0.3)
    first "有!"

    first "所以你是生气了？"

    hide first
    show ja with Dissolve(0.3)
    ja "嗯。"

    hide ja
    show first with Dissolve(0.3)
    first "吃醋了？"

    hide first
    show ja with Dissolve(0.3)
    ja "嗯。"
    hide ja

    menu:
        "Ja也不多说话只是开车。"
        "都说了是闺蜜":
            $pts+=1
            
            show first with Dissolve(0.3)
            first "诶呀见Noeul十次八次你都吃醋，都说了是闺蜜"
            hide first
        "给人嘴里塞颗糖":
            pass

    show first
    first "不生气了好不好。"

    hide first
    show ja with Dissolve(0.3)
    ja "回家再说。"
    hide ja

    scene outroom

    "到家后"

    if pts >= 3:
        $final = 4
        jump jfNc
    else:
        $final = 3
        jump jfNormal


    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。


    # 此处为游戏结尾。

    return
