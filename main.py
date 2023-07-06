"""
    项目主文件
"""
from LLM.spark_desk import SparkDesk
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import load_prompt

import json
import codecs

from webSearch.web_search_poem import search_poem


if __name__ == "__main__":
    # 创建大模型
    llm = SparkDesk()

    poem_input = input("请输入诗句：")

    # 检索古诗
    # poetry_dict = search_poem(poem_input)
    # 从字典中分割译文
    # poem_trans = poetry_dict["trans"]

    # chain：诗句白话文翻译
    prompt_pu_get = load_prompt("prompts/poem2pu.json")
    chain_pu_get = LLMChain(llm=llm,prompt=prompt_pu_get)
    # # chain：场景切割
    # prompt_scene_get = load_prompt("prompts/scene_get.json")     # 从JSON文件读取prompt模版
    # chain_scene_get = LLMChain(llm=llm, prompt=prompt_scene_get)
    # chain: 提取画面内容
    prompt_content_get2 = load_prompt("prompts/content_get2.json")
    chain_content_get = LLMChain(llm=llm, prompt=prompt_content_get2)
    # 连接chain
    overall_chain = SimpleSequentialChain(chains=[chain_pu_get, chain_content_get], verbose=True)

    result = overall_chain.run(poem_input)

    # 结果合法与否判断

    # 前端呈现结果
