"""
    项目主文件
"""
from LLM.spark_desk import SparkDesk
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

from webSearch.web_search_poem import search_poem

if __name__ == "__main__":
    # 创建大模型
    llm = SparkDesk()

    poem_input = input("请输入诗句：")
    # 检索古诗
    poetry_dict = search_poem(poem_input)


