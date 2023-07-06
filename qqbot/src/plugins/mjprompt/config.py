from pydantic import BaseModel, Extra
from nonebot import on_keyword, on_command
from nonebot.adapters.onebot.v11 import MessageSegment,GroupMessageEvent,Bot,Event
from nonebot.typing import T_State
from nonebot.params import CommandArg

from LLM.spark_desk import SparkDesk
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import load_prompt

# from qqbot.src.plugins.style.config import StyleHolder as StyleHolder

import re


# 判断输出是否合法
def check(result):
    # 判断文本是否包含中文
    if re.search('[\u4e00-\u9fff]', result):
        return False

    # 关键词判断格式是否正确
    keywords = ["Type","Subject","Environment"]
    for keyword in keywords:
        if keyword in result:
            continue
        else: return False

    return True


class Config(BaseModel, extra=Extra.ignore):

    """
    Plugin Config Here
    """


prompt = on_keyword("imagine")


@prompt.handle()
async def prompt_gen(event: Event):
    content = str(event.get_message())
    # 去掉前面的关键字，只要诗句
    poem = content[9:]
    result = prompt_get(poem)
    while not check(result):
        # await word.send(result)
        result = prompt_get(poem)
    message = MessageSegment.at(event.get_user_id()) + "\n" + result + ":: "
    # + StyleHolder.get_style()

    await prompt.finish(message)


# 调用星火
def prompt_get(poem):
    llm = SparkDesk()

    # chain1：诗句白话文翻译
    prompt_pu_get = load_prompt("../prompts/poem2pu.json")
    chain_pu_get = LLMChain(llm=llm, prompt=prompt_pu_get)
    # chain2: 提取画面内容
    prompt_content_get2 = load_prompt("../prompts/content_get2.json")
    chain_content_get = LLMChain(llm=llm, prompt=prompt_content_get2)
    # 连接chain
    overall_chain = SimpleSequentialChain(chains=[chain_pu_get, chain_content_get], verbose=True)

    result = overall_chain.run(poem)
    return result
