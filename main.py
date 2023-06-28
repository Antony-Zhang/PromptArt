import prompt.desc_expand as desc_expand

if __name__ == "__main__":
    print("请开始对话吧!!")

    txt = input("\n(输入-1结束对话)文案:")
    # 输入的txt中不可包含\n换行符!

    while txt != "-1":  # 机械的循环交互,但不知道长连接本身是否可支持
        # # 意象识别(+情感)
        # image_analysis.ImageAnalysis.analyze(txt)
        # # 古诗翻译
        # poem_trans.PoemTrans.trans(txt)

        # 描述扩写
        desc_expand.DescExpand.expand(txt)
        # # 情绪识别
        # MoodAnalysis.MoodAnalysis.mood_analyze
        # 古诗翻译
        # Poem_Trans.Poem_Trans.poemTrans(txt)
        # 古诗白话文赏析
        # Pu_Trans.Pu_Trans.puTrans(txt)

        # 意象提取
        # Image_Get.Image_Get.getImage(txt)
        txt = input("\n(输入-1结束对话)文案:")
