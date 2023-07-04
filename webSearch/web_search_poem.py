# -*- coding: utf-8 -*-
# @Time : 2023/6/30 15:27
# @Author : Fishead_East
# @Email : ytzd2696@foxmail.com
# @File : web_search_poem.py
# @Project : PromptArt

from typing import Optional, Any
from bs4 import BeautifulSoup as BS
import requests
import re  # 正则表达式

url = "https://so.gushiwen.cn"


def search_poem(poem) -> Optional[dict[Any, Any]]:
    """
    实时Web检索古诗(第一首)
    :param poem: 诗句
    :return: 古诗信息的字典["title", "author", "contents", "trans"]
    """
    # 进入搜索界面
    url_search = url + "/search.aspx?value=" + poem + "&valuej=" + poem[0]
    req_search = requests.get(url=url_search)
    req_search.encoding = "utf-8"
    html = req_search.text  # 返回的html内容
    soup_search = BS(html, features="html.parser")  # 返回解析对象

    # 定位第一首古诗，并跳转至详情页
    new_url = soup_search.find("div", {"class": "sons"}).find('a').attrs['href']  # 获取古诗跳转链接
    url_poetry = url + new_url
    req_poetry = requests.get(url=url_poetry)
    req_poetry.encoding = "utf-8"
    soup_poetry = BS(req_poetry.text, features="html.parser")

    # 提取数据
    title = soup_poetry.find('h1').text.strip()
    if len(title) == 0:
        print("未找到古诗")
        return None

    author = soup_poetry.find("p", class_="source").text.strip()
    contents = soup_poetry.find("div", class_="contson").text.strip()
    trans = soup_poetry.find("div", id=re.compile(r'fanyi+\d')).find('p').text.strip().lstrip("译文")

    # 结果转化为dict
    keys = ["title", "author", "contents", "trans"]
    values = [title, author, contents, trans]
    poetry_dict = dict(zip(keys, values))

    return poetry_dict
    # # 打印
    # for key, value in poetry_dict.items():
    #     print(key+": "+value)