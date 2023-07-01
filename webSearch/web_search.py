# -*- coding: utf-8 -*-
# @Time : 2023/6/30 15:27
# @Author : Fishead_East
# @Email : ytzd2696@foxmail.com
# @File : web_search.py
# @Project : PromptArt
"""
    web检索古诗的全文与释义
"""
from bs4 import BeautifulSoup as bs
import requests
import re   # 正则表达式


url = "https://so.gushiwen.cn"
# 循环调试
for x in range(20):
    poem = input("###需要查询的诗名或诗句：")
    # 进入搜索界面
    url_search = url + "/search.aspx?value=" + poem + "&valuej=" + poem[0]
    req_search = requests.get(url=url_search)
    req_search.encoding = "utf-8"
    html = req_search.text  # 返回的html内容
    soup_search = bs(html, features="html.parser")  # 返回解析对象

    # 定位第一首古诗，并跳转至详情页
    new_url = soup_search.find("div", {"class": "sons"}).find('a').attrs['href']  # 获取古诗跳转链接
    url_poetry = url + new_url
    req_poetry = requests.get(url=url_poetry)
    req_poetry.encoding = "utf-8"
    soup_poetry = bs(req_poetry.text, features="html.parser")

    # 提取数据
    title = soup_poetry.find('h1').text.strip()
    if len(title) == 0:
        print("未找到古诗")
        continue
    author = soup_poetry.find("p", class_="source").text.strip()
    contents = soup_poetry.find("div", class_="contson").text.strip()
    trans = soup_poetry.find("div", id=re.compile(r'fanyi+\d')).find('p').text.strip().lstrip("译文")

    # 结果转化为dict
    keys = ["标题", "作者", "古诗", "翻译"]
    values = [title, author, contents, trans]
    poetry_dict = dict(zip(keys, values))

    # 打印
    for key, value in poetry_dict.items():
        print(key+": "+value)

