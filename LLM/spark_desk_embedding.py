# -*- coding: utf-8 -*-
# @Time : 2023/7/3 15:41
# @Author : Fishead_East
# @Email : ytzd2696@foxmail.com
# @File : spark_desk_embedding.py
# @Project : PromptArt
import os
import json
import requests
from typing import Optional, List, Mapping, Any

from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.embeddings.base import Embeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

from LLM.webInteract.web_param import WsParamEmb


class SparkDeskEmbeddings(HuggingFaceEmbeddings):
    """重写HuggingFaceEmbeddings加载类"""
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Compute doc embeddings using a HuggingFace transformer model.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        texts = list(map(lambda x: x.replace("\n", " "), texts))
        embeddings = self.client.encode(texts, normalize_embeddings=True)
        return embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        """Compute query embeddings using a HuggingFace transformer model.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        text = text.replace("\n", " ")
        embedding = self.client.encode(text, normalize_embeddings=True)
        return embedding.tolist()


# class SparkDeskEmbedding(LLM):
#     """
#     讯飞星火的Embedding模型
#     """
#     url = r'https://knowledge-retrieval.cn-huabei-1.xf-yun.com/v1/aiui/embedding/query'
#     APPID: str = os.getenv("APPID")
#     APIKey: str = os.getenv("APIKEY")
#     APISecret: str = os.getenv("APISECRET")
#
#     @property
#     def _llm_type(self) -> str:
#         return "SparkDeskEmbedding"
#
#     @property
#     def _identifying_params(self) -> Mapping[str, Any]:
#         _param_dict = {
#             "url": self.url,
#             "APPID": self.APPID,
#             "APIKey": self.APIKey,
#             "APISecret": self.APISecret
#         }
#         return _param_dict
#
#     def _get_param(self, text) -> Mapping[str, Any]:
#         """
#         组织请求消息
#         :param text: 待向量化的文本
#         :return:
#         """
#         param_dict = {
#             'header': {
#                 'app_id': self.APPID
#             },
#             'payload': {
#                 'text': text
#             }
#         }
#         return param_dict
#
#     def _call(
#             self,
#             prompt: str,
#             stop: Optional[List[str]] = None,
#             run_manager: Optional[CallbackManagerForLLMRun] = None,
#     ) -> str:
#         ws_param = WsParamEmb(self.url, self.APPID, self.APIKey, self.APISecret)
#         wsUrl = ws_param.create_url()
#         param_dict = self._get_param(prompt)
#         response = requests.post(url=wsUrl, json=param_dict)
#         result = json.loads(response.content.decode('utf-8'))
#         print(result)
#         return result


if __name__ == '__main__':
    # llm_emb = SparkDeskEmbedding()
    # print(llm_emb("OK"))
