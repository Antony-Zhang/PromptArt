# -*- codeing = utf-8 -*-
# @Time : 2023-06-28 14:48
# @Author : Shelly
# @File : content_get.py
# @Software : PyCharm

from LLM import web_interact


class content_get:
    @classmethod
    def getContent(cls, txt):
        ws = websocket.WsParam()
        prompt = f'''
            [知识]
            对于给定文本，画师需要首先概括出画作所要重点描绘的主体以及灯光氛围、环境、构图等多个要素、理解作者所想要表达的情感，为真正绘图做准备。其中，主体出现在画面关键之处，通常有特定的修饰词，起突出强调画家情感的作用；是单一的一个对象或一组对象。环境指的是画面的主体周围的人物、景物和空间。
            [角色]
            你是一位专业的插画画家，擅长为用户提供的文字绘制相对应的插画。你有崇高的艺术追求，不仅要让画作贴合文本，更要通过画作表达文本的情感。
            [任务]
            你需要对输入的文本整体分析，总结提取画作的主体、环境、灯光、色调、情绪、构图等。
            [输出格式]
            用清单分别输出所提取出的主体、环境、灯光、色调、情绪、构图。
            [文案]
            {txt}
                '''
        websocket.main(ws, prompt)
