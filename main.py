"""
    项目主文件
"""
from LLM.spark_desk import SparkDesk
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import load_prompt

from webSearch.web_search_poem import search_poem

if __name__ == "__main__":
    # 创建大模型
    llm = SparkDesk()

    poem_input = input("请输入诗句：")
    # 检索古诗
    poetry_dict = search_poem(poem_input)
    # 场景切割(prompt待写入)
    prompt_scene_get = load_prompt("prompts/content_get2.json")     # 从JSON文件读取prompt模版
    chain_scene_get = LLMChain(llm=llm, prompt=prompt_scene_get)
    # 提取画面内容(JSON格式输出)
    prompt_content_get2 = load_prompt("prompts/content_get2.json")
    chain_content_get = LLMChain(llm=llm, prompt=prompt_content_get2)

    # 前端呈现结果
