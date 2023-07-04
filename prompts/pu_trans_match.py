# -*- coding: utf-8 -*-
# @Time : 2023/7/1 15:54
# @Author : Fishead_East
# @Email : ytzd2696@foxmail.com
# @File : pu_trans_match.py
# @Project : PromptArt
"""
    诗句与翻译的对应
"""


class PuTransMatch:
    @classmethod
    def trans_match(cls, poem, trans):
        ws = WS.WsParamGPT()
        prompt = f'''
        你是一个诗句和现代汉语的匹配器，可根据语义找出与诗句匹配的现代汉语。
        你将分别获得一段诗句和现代汉语，而现代汉语中存在一个片段的语义与诗句匹配。请输出这个现代汉语片段。其中语义匹配指将古诗中的词语与现代汉语中的词语进行比较，若含义相同则匹配成功，但若古诗或现代汉语片段中存在某词语或事物在另一方中找不到对应的表达，则匹配失败。
        只输出现代汉语片段，不要输出诗句。
        [现代汉语]
        {trans}
        [诗句]
        {poem}
        '''
        WS.main(ws, prompt)

if __name__ == "__main__":
    print("请开始对话吧!!")
    poem = input("古诗:")
    trans = input("全诗翻译:")
    PuTransMatch.trans_match(poem, trans)
