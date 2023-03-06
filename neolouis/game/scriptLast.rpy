# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 游戏在此开始。

# 选视角过后
label endLabel:

    # 结束
    "END"

    if pts >= 5:
        "触发结局《男朋友》"

        jump extraStory
    else:
        "触发结局《试用期》"

    nvl clear
    full "文本：静苒{vspace=10}故事：小九 @nini小九123{vspace=10}主线：小九 @nini小九123{vspace=10}制作：静苒{vspace=10}"
    full "{vspace=40}BGM: https://www.ashamaluevmusic.com/"
    
    # 此处为游戏结尾。

    return
