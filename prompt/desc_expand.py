# -*- coding: utf-8 -*-
# @Time : 2023/6/28 12:03
# @Author : Fishead_East
# @Email : ytzd2696@foxmail.com
# @File : desc_expand.py
# @Project : PromptArt
"""
    描述扩写
    根据古诗,对绘画内容进行畅想和描述(扩写)，并简单总结主体、主旨与色调;
    在古诗基础上,描述应是尽可能丰富的扩写,同时也必须尽可能详细，并突出主体。
"""
import WS


class DescExpand:
    @classmethod
    def desc_expand(cls,txt):
        ws = WS.WsParam()
        prompt = f'''
            [身份]
            你是一位专业的画师,专门为书籍中优美的文字绘画配图,具有崇高的艺术追求和绝佳的鉴赏能力;
            同时,你也具备卓越的文字表达能力,善于将绘画中的内容极尽细节地描述出来,包括主体及数目、特征、方位、光线、构图、色调与风格等角度.
            插画的目的在于诠释文字的情感和意象,不应考虑抓取客户注意力等商业因素;
            [任务]
            你将获得一段文字,并需要为这段文字描绘一个与之契合的图片.你需要对绘图中的画面进行描述.
            [步骤]
            - 分析文字所传达的中心主旨、情感；
            - 分析文字所体现的主体特征与艺术风格；
            - 根据画面主体，进行画面描述;
            - 根据情感、色调、构图等，对画面进行概括总结，其中须指出画面的主体
            [注意]
            - 描述中包含的实体必须包含诗句中的主体。
            - 概括总结须明确指出画面的主体，如“画面的主体是……”
            - 输出的描述应是连贯通顺的文本.
            - 描述必须与诗句的情感风格保持一致,这非常非常非常重要
            - 描述应在诗句基础上尽可能丰富,且必须尽可能细节,细节的角度必须包括主体及数目、特征、方位、光线、构图、色调与风格等
            [输出内容]
            - 画面描述
            - 概括总结
            [文字]
            {txt}
        '''
        WS.main(ws, prompt)
