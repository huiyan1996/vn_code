# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后
label endLabel:

    # 结束
    "END"

    if final == 1:
        "触发 BossNoeul 普通结局"
    elif final == 2:
        "触发 BossNoeul NC结局"
    elif final == 3:
        "触发 JaFirst 普通结局"
    elif final == 4:
        "触发 JaFirst NC结局"

    nvl clear
    full "文本：虫二{vspace=10}故事：虫二{vspace=10}制作：静苒{vspace=10}"
    full "BGM: https://www.ashamaluevmusic.com/{vspace=10}JF BGM: De Amor Nadie Se Muere{vspace=10}BN BGM: 巴赫G大调第一无伴奏大提琴曲{vspace=10}"
    full "音效：剧里截的{vspace=10}"
    
    # 此处为游戏结尾。

    return
