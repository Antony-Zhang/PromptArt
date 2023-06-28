import prompt.desc_expand as desc_expand
import prompt.content_get as content_get
import prompt.pu_trans as pu_trans

import  youdaoTrans

if __name__ == "__main__":
    print("请开始对话吧!!")

    # 有道翻译
    print("本程序调用有道词典的API进行翻译，可达到以下效果：")
    print("外文-->中文")
    print("中文-->英文")
    txt = input('请输入你想要翻译的词或句：')
    list_trans = youdaoTrans.youdaoTrans.translate(txt)
    youdaoTrans.youdaoTrans.get_result(list_trans)

    txt = input("\n(输入-1结束对话)文案:")
    # 输入的txt中不可包含\n换行符!

    while txt != "-1":  # 机械的循环交互,但不知道长连接本身是否可支持
        # # 意象识别(+情感)
        # image_analysis.ImageAnalysis.analyze(txt)
        # # 古诗翻译
        # poem_trans.PoemTrans.trans(txt)

        # 描述扩写
        # desc_expand.DescExpand.expand(txt)

        # # 情绪识别
        # MoodAnalysis.MoodAnalysis.mood_analyze
        # 古诗翻译
        # pu_trans.pu_trans.puTrans(txt)
        # 古诗白话文赏析
        # Pu_Trans.Pu_Trans.puTrans(txt)

        # 意象提取
        # Image_Get.Image_Get.getImage(txt)

        # 提取画作内容
        # content_get.content_get.getContent(txt)

        # txt = input("\n(输入-1结束对话)文案:")

        # 有道翻译
        txt = input('请输入你想要翻译的词或句：')
        list_trans = youdaoTrans.youdaoTrans.translate(txt)
        youdaoTrans.youdaoTrans.get_result(list_trans)

