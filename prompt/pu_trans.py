# -*- codeing = utf-8 -*-
# @Time : 2023-06-28 14:43
# @Author : Shelly
# @File : pu_trans.py
# @Software : PyCharm

# -*- codeing = utf-8 -*-
# @Time : 2023-06-24 11:32
# @Author : Shelly
# @File : Pu_Trans.py
# @Software : PyCharm
import WS

class Pu_Trans:
    @classmethod
    def puTrans(cls, txt):
        ws = WS.Ws_Param()
        prompt = f'''
            [知识]
            理解古诗词可以从作者生平经历、诗歌创作的历史背景等入手
            更重要的是传达作者所要表达的情感而非一字一句的翻译
            关注重点意象，如“杨柳”多指送别，“大雁”多表示思乡之情，但存在偏差
            注重作者所要表达的情感
            [任务]
            作为一个古诗研究专家，将文案中的古诗用白话文表达，意思清晰，内容明确。
            [步骤]
            1、先根据句号或感叹号之类的标点，将诗歌划分为多个短句。
            2、对每个短句进行翻译
            3、将翻译结果进行整合，总结概括
            4、用第一人称讲故事的形式得到最终结果
            5、到
            [格式]
            只输出最终整合得到的古诗对应普通话表示，不用输出诗歌相关背景信息
            [文案]
            {txt}
        '''

        WS.main(ws, prompt)