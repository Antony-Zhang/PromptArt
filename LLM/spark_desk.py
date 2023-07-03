# # -*- coding: utf-8 -*-
# # @Time : 2023/6/28 16:08
# # @Author : Fishead_East
# # @Email : ytzd2696@foxmail.com
# # @File : spark_desk.py
# # @Project : PromptArt
"""
    使用LangChain自定义LLM
"""
import os
import time
import logging
from typing import Optional, List, Dict, Mapping, Any
import ssl

from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import websocket
from web_interact import Singleton, WsParam, WS
from web_interact import (on_close,
                          on_open,
                          on_error,
                          on_message)

# class SparkDeskEmbedding(LLM):
#     """
#     讯飞星火的Embedding模型
#     """
#     url = r'https://knowledge-retrieval.cn-huabei-1.xf-yun.com/v1/aiui/embedding/query'


@Singleton
class SparkDesk(LLM):
    """
    讯飞星火的语言模型
    """

    url = "wss://spark-api.xf-yun.com/v1.1/chat"
    APPID = os.getenv("APPID")
    APIKey = os.getenv("APIKEY")
    APISecret = os.getenv("APISECRET")

    @property
    def _llm_type(self) -> str:
        return "SparkDesk"

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        _param_dict = {
            "url": self.url,
            "APPID": self.APPID,
            "APIKey": self.APIKey,
            "APISecret": self.APISecret
        }
        return _param_dict

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        ws_param = WsParam(os.getenv("APPID"), os.getenv("APIKEY"), os.getenv("APISECRET"))
        websocket.enableTrace(False)
        wsUrl = ws_param.create_url()
        ws = WS(appid=ws_param.APPID,
                url=wsUrl,
                on_message=on_message,
                on_error=on_error,
                on_close=on_close,
                on_open=on_open)
        ws.question = prompt
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})  # 建立长连接
        return ws.received_message


if __name__ == "__main__":
    llm = SparkDesk()
    print(llm("请说‘你好’"))


# if __name__ == "__main__":
#     llm = SparkDesk()
#     while True:
#         human_input = input("Human: ")
#
#         begin_time = time.time() * 1000
#         # 请求模型
#         response = llm(human_input, stop=["you"])
#         end_time = time.time() * 1000
#         used_time = round(end_time - begin_time, 3)
#         logging.info(f"chatGLM process time: {used_time}ms")
#
#         print(f"ChatGLM: {response}")

# # 创建一个LLM实例并定义相应的提示来生成响应
# prompt = PromptTemplate(input_variables=["question"], template="What is the answer to {question}?")
#
# # 使用链来将LLM与其他计算或知识源组合起来
# chain = LLMChain(llm=llm, prompt=prompt)
#
# # 使用代理来确定如何使用LLM来采取行动
# # 这里省略代理的定义
#
# # 使用内存来在链或调用之间存储状态
# # 这里省略内存的定义
#
# # 测试应用程序
# response = chain.run("the meaning of life")
# print(response)
