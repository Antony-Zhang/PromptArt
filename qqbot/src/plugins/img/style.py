# -*- codeing = utf-8 -*-
# @Time : 2023-07-06 10:33
# @Author : Shelly
# @File : style.py
# @Software : PyCharm

import re

from pydantic import BaseModel, Extra
from nonebot import on_keyword, on_message, on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Message, Bot, Event, MessageSegment
from nonebot.rule import to_me


'''
提供image prompt参考和选项选择
'''

def valid(text):
    """
    是否只选了一个类型
    :param text:
    :return: 是否有多个数字
    """
    pattern = r"\d+"  # 匹配连续的数字
    matches = re.findall(pattern,text)
    return len(matches) == 1


# 图片地址和对应消息段
file_path1 = r'C:\Users\小白\Desktop\mj\mountain.png'
image_seg1 = MessageSegment.image(file=f'file:///{file_path1}')

# 输入关键字'/style'触发
style = on_keyword({'choose'})


@style.got('/choose', prompt='回复”参考“获取图片样例参考'
                             '回复\'取消\'以停止 \n')
async def _(bot: Bot, state: T_State, event: Event):
    # await style.send("1、" + Message('[CQ:image,file='https://cdn.discordapp.com/attachments/1120201914768969870/1123449797534306346/mountain.png']'))
    # a = state['/st']
    a = str(event.get_message().extract_plain_text())

    if a == "取消":
        await style.finish("已取消")
    if a == "参考":
        await style.send("1."+image_seg1 + "\n回复序号进行选择，或回复\'取消\'以停止，请注意只能选择一张图片")
    else:
        await style.finish("输入参数有误，已退出")
    a = str(event.get_message().extract_plain_text())
    has_choose = False
    while(not has_choose):
        a = str(event.get_message().extract_plain_text())
        if not valid(a):
            await style.send("请输入数字序号进行选择")
        if int(a)<0 or int(a)>10:
            await style.send("请输入正确序号")
        else:
            await style.finish("选择成功")
            has_choose = True


# img = on_command('img',priority=20)
#
#
# @img.handle()
# async def _(bot:Bot, event:Event, state:dict):
#     await img.send("lalala")
#     image_message = MessageSegment.image('https://cdn.discordapp.com/attachments/1120201914768969870/1123449797534306346/mountain.png')
#     await img.send(image_message)
#
#     a = str(event.get_message().extract_plain_text())
#     # await style.finish(a)
#     if a == "取消":
#         await style.finish("已取消")
#     if not valid(a):
#         await style.finish("请只选择一个图片")
#     if int(a) < 0 or int(a) > 10:
#         await style.finish("输入错误，已停止")
#     else:
#         await style.finish("选择成功")


# 传递风格
class StyleHolder:
    def __init__(self):
        self.string = ""

    def add_style(self,new_style):
        self.string += new_style

    def get_style(self):
        return self.string


class Config(BaseModel, extra=Extra.ignore):

    """
    Plugin Config Here
    """