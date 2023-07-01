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
    poem = input("需要查询的诗名或诗句：")
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
    title = soup_poetry.find('h1')
    if len(title) == 0:
        print("未找到古诗")
        continue
    print("标题："+title.text.strip())
    author = soup_poetry.find("p", class_="source")
    print("作者:"+author.text.strip())
    contents = soup_poetry.find("div", class_="contson")
    print("古诗:"+contents.text.strip())
    trans = soup_poetry.find("div", id=re.compile(r'fanyi+\d')).find('p')
    print("翻译:"+trans.text.strip().lstrip("译文"))
    # # 结果转化为dict
    # author_poems = dict(zip(title, author, contents, trans))
    # for title, author, contents, trans in author_poems.items():
    #     print("标题："+title.text.strip())
    #     print("作者:"+author.text.strip())
    #     print("古诗:"+contents.text.strip())
    #     print("翻译:"+trans.text.strip())

