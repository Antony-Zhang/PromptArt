# -*- codeing = utf-8 -*-
# @Time : 2023-06-24 10:55
# @Author : Shelly
# @File : Poem_Trans.py
# @Software : PyCharm

import WS


class Poem_Trans:
    @classmethod
    def poemTrans(cls, txt):
        ws = WS.Ws_Param()
        prompt = f'''
            [角色]
            你是一个专业的中英翻译家和古诗词研究者
            [知识]
            古诗翻译重点在于用英文传达作者所要表达的情感，而非一字一译。
            以下你过往的作品：
            中文：无边落木萧萧下，不尽长江滚滚来。
            英文：The boundless forest sheds its leaves shower by shower; The endless river rolls its waves hour after hour.
            中文：大漠孤烟直，长河落日圆。
            英文：In boundless desert lonely smokes rise straight;
            Over endless river the sun sinks round.
            中文：生当作人杰，死亦为鬼雄。
            英文：Be man of men while you’re alive,
            And soul of souls if you’re dead.
            [任务]
            基于过往，把下面的中文诗句{txt}翻译为英文。注意用词准确，符合英文表达习惯，可适当填充细节内容；只要输出英文。

        '''

        WS.main(ws, prompt)
