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


# 循环调试
for x in range(20):
    poem = input("需要查询的诗名或诗句：")
    url = "https://so.gushiwen.cn/search.aspx?value=" + poem + "&valuej=" + poem[0]
    req = requests.get(url=url)
    req.encoding = "utf-8"
    html = req.text  # 返回的html内容
    # 从html文件中提取数据(作者与古诗)
    soup = bs(html, features="html.parser")  # 返回解析对象
    author = soup.find_all("p", class_="source")
    poems = soup.find_all("div", class_="contson")
    # 将作者与古诗对应，转化为dict
    author_poems = dict(zip(author, poems))
    for author, poem in author_poems.items():
        print("作者:"+author.text.strip())
        print("古诗:"+poem.text.strip())

