"""
    情感识别+意象识别
"""
import WS


class ImageAnalysis:
    @classmethod
    def analyze(cls, txt):
        ws = WS.WsParam()
        prompt = f'''
                    你将获得一段文案,需要识别以下内容:
                    - 核心情感
                    - 核心意象

                    请注意,核心意象的数目必须不超过5个,若超过则请再次筛选、直到数目满足要求;

                    [文案]
                    {txt}

                    [输出形式]
                    核心情感:
                    核心意象:

                    [结果]

                '''
        WS.main(ws, prompt)
