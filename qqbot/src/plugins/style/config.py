# -*- codeing = utf-8 -*-
# @Time : 2023-07-06 10:33
# @Author : Shelly
# @File : style.py
# @Software : PyCharm

import re

from nonebot import on_keyword, on_message, on_command,get_bot
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
    matches = re.findall(pattern, text)
    return len(matches) == 1


# 图片地址和对应消息段
file_path1 = r'D:\AIGC\PromptArt\resource\img\1.png'
file_path2 = r'D:\AIGC\PromptArt\resource\img\2.png'
file_path3 = r'D:\AIGC\PromptArt\resource\img\3.png'
file_path4 = r'D:\AIGC\PromptArt\resource\img\4.png'
file_path5 = r'D:\AIGC\PromptArt\resource\img\5.png'
file_path6 = r'D:\AIGC\PromptArt\resource\img\6.png'
file_path7 = r'D:\AIGC\PromptArt\resource\img\7.png'
file_path8 = r'D:\AIGC\PromptArt\resource\img\8.png'
image_seg1 = MessageSegment.image(file=f'file:///{file_path1}')
image_seg2 = MessageSegment.image(file=f'file:///{file_path2}')
image_seg3 = MessageSegment.image(file=f'file:///{file_path3}')
image_seg4 = MessageSegment.image(file=f'file:///{file_path4}')
image_seg5 = MessageSegment.image(file=f'file:///{file_path5}')
image_seg6 = MessageSegment.image(file=f'file:///{file_path6}')
image_seg7 = MessageSegment.image(file=f'file:///{file_path7}')
image_seg8 = MessageSegment.image(file=f'file:///{file_path8}')

# 输入关键字'#style'触发
style = on_keyword({'#stl'})


@style.handle()
async def _():
    await style.finish("下为图片提示样例，你可以在\"#imagine\”中使用\n"
                       "1." + image_seg1 + "\n2." + image_seg2 + "\n3." + image_seg3 +
                       "\n4." + image_seg4 + "\n5." + image_seg5 + "\n6." + image_seg6 +
                       "\n7." + image_seg7 + "\n8." + image_seg8)


choose = on_keyword({'#选择'})


@choose.got('num', prompt='回复序号进行选择，或回复\'取消\'以停止，请注意只能选择一张图片')
async def _(bot: Bot, state: T_State, event: Event):
    a = str(event.get_message().extract_plain_text())

    if a == "取消":
        await style.finish("已取消")

    has_choose = False
    while not has_choose:
        # event = await bot.wait_event(Event,timeout=60)
        if not valid(a):
            await style.reject("请输入数字序号进行选择")
        if int(a) <= 0 or int(a) > 10:
            await style.reject("请输入有效序号")
        else:
            await style.finish("选择成功，你选择了第" + a + "张图")
            has_choose = True


class StyleHolder:
    def __init__(self):
        self.string = ""

    def add_style(self, new_style):
        self.string += new_style

    def get_style(self):
        return self.string



