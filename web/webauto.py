# -*- coding: utf-8 -*-
# @Time : 2023/6/27 11:54
# @Author : Fishead_East
# @Email : ytzd2696@foxmail.com
# @File : webauto.py
# @Project : PromptArt
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebAuto:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = "https://xinghuo.xfyun.cn/botcenter"  # 星火大模型入口网页

    def get_cookies(self):
        """
            用于获取cookies：在打开网页后60s内完成登录操作，即可将登录状态cookie保存在cookies.txt文件中
        """
        self.browser.get(self.url)

        # 程序打开网页后60秒内手动登陆账户
        time.sleep(60)

        with open('cookies.txt', 'w') as cookie_f:
            # 将cookies保存为json格式
            cookie_f.write(json.dumps(self.browser.get_cookies()))

        self.browser.close()

    def login_cookies(self):
        """
            使用cookie登录网页
        """
        self.browser.get(self.url)
        # 首先清除由于浏览器打开已有的cookies
        self.browser.delete_all_cookies()

        with open('cookies.txt', 'r') as cookie_f:
            # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
            cookies_list = json.load(cookie_f)
            for cookie in cookies_list:
                if "domain" in cookie:
                    del cookie["domain"]
                self.browser.add_cookie(cookie)

        # 刷新界面
        self.browser.refresh()

        # self.enter_bot_center()

    def enter_bot_center(self):
        self.browser.find_element(By.XPATH, "//*[@id='root']/main/section[1]/div[3]/div").click()


# if __name__ == "__main__":
#     web = WebAuto()
#     web.login_cookies()