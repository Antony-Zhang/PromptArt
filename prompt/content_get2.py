# -*- codeing = utf-8 -*-
# @Time : 2023-06-29 15:04
# @Author : Shelly
# @File : content_get2.py
# @Software : PyCharm

'''
重构后的内容提取
注重提取内容的阐述和定义
'''
from LLM import web_interact


class content_get2:
    @classmethod
    def getContent(cls, txt):
        ws = websocket.WsParam()
        prompt = f'''
            你是一个图像prompt生成器，可以为输入文本生成对应描述图像的英文prompt。
            prompt的框架是:类型+主体+环境+情感+灯光+构图+风格+参数。其中类型指的是图象类型，比如logo图、水彩画、插画等。主体是人或物及其描述或者动作，可以有多个。环境指的是主体所在的环境，包括自然和社会环境。情感指的是文本作者所要表达的情感或感受、如愉悦痛苦等、只要输出情绪词、不要解释；画作中应体现相同的情感。灯光指的是画作的色调、光线效果等，必须和作者所要表达的情感一致。构图指的是画作焦点，或是主体的朝向等等。风格包含几个方面的元素，比如年代、艺术家、或者具体的艺术类型，比如pop at。参数主要包含清晰度。用名词或主谓宾短语进行描述。
            一定要按照这个框架来生成prompt，尽可能简短，多用短语进行阐述，符合中文原文意义和英文表达习惯，不要用大段文字，不要在参数面前加上说明性质的词汇。
            文案背景应该是中国古代，因此注意中国元素的提取和整合、必要时进行细节补充。文案中可能暗含作者自身，应注意补充。
            只用英文来输出，介词短语定要替换为形容词加名词的形式，或者替换为主谓宾结构的短语。多用短语描述，短语间用逗号隔开。框架中的每个内容属性都要分点输出，保证简短且符合英文表达习惯，不要总结，不用输出文本翻译或总结，务必只输出英文.
            {txt}
                '''
        WS.main(ws, prompt)
