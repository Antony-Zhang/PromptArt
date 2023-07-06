from pydantic import BaseModel, Extra
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import MessageSegment,Bot,Event

from LLM.spark_desk import SparkDesk
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import load_prompt
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
        else:
            return False

    return True


# 定义图片及其地址的字典
imgdict = {'1':  'https://cdn.discordapp.com/attachments/1120201914768969870/1126412313369530488/1.png',
           '2': 'https://cdn.discordapp.com/attachments/1120201914768969870/1126412342045966376/',
           '3': 'https://cdn.discordapp.com/attachments/1120201914768969870/1126412357896245299/3.png',
           '4': 'https://cdn.discordapp.com/attachments/1120201914768969870/1126412394235691008/4.png',
           '5': 'https://cdn.discordapp.com/attachments/1120201914768969870/1126412399700869190/5.png',
           '6': 'https://cdn.discordapp.com/attachments/1120201914768969870/1126412417530863656/6.png',
           '7': 'https://cdn.discordapp.com/attachments/1120201914768969870/1126412443799793715/7.png',
           '8': 'https://cdn.discordapp.com/attachments/1120201914768969870/1126412471217967114/8.png',}

prompt = on_keyword({"#imagine"})


@prompt.handle()
async def prompt_gen(event: Event):
    content = event.get_message().extract_plain_text()
    has_img = False
    # 第一种情况，有img prompt
    pattern1 = r'#imagine-(\d+)\s+(.*)'

    match = re.match(pattern1,content)

    if match:
        has_img = True
        number = match.group(1)
        if int(number) <= 0 or int(number) > 8:
            await prompt.reject("请输入合法的数字序号")
        poem = match.group(2)
    else:
        # 第二种情况，没有
        pattern2 = r'#imagine\s+(.*)'
        match = re.match(pattern2,content)
        if match:
            poem = match.group(1)
        else:
            await prompt.finish("请按正确格式输入")
    await prompt.send("稍等，正在为您生成...")
    result = prompt_get(poem)
    while not check(result):
        result = prompt_get(poem)
    if has_img:
        result = imgdict[number] + "\n" + result

    await prompt.finish(result)


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


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""
