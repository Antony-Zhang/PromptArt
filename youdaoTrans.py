# -*- codeing = utf-8 -*-
# @Time : 2023-06-28 15:33
# @Author : Shelly
# @File : youdaoTrans.py
# @Software : PyCharm

import json

import requests

class youdaoTrans:
    # 翻译函数，word 需要翻译的内容
    def translate(word):
        # 有道词典 api
        url = 'http://fanyi.youdao.com/translate'
        # 传输的参数，其中 i 为需要翻译的内容
        key = {
            "i": word,  # 待翻译的字符串
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": "16081239145423",
            "sign": "94f8a159b53a1086a938801ddbda275a",
            "doctype": "json",
            "version": "3.0",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        # key 这个字典为发送给有道词典服务器的内容
        response = requests.post(url, data=key)
        # 判断服务器是否相应成功
        if response.status_code == 200:
            # 然后相应的结果
            return response.text
        else:
            print("有道词典调用失败")
            # 相应失败就返回空
            return None

    def get_result(repsonse):
        # 通过 json.loads 把返回的结果加载成 json 格式
        result = json.loads(repsonse)
        # print("输入的词为：%s" % result['translateResult'][0][0]['src'])
        # print("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])
        print(result['translateResult'][0][0]['tgt'])
