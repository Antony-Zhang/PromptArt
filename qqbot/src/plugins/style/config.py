from pydantic import BaseModel, Extra
from nonebot import on_keyword, on_message, on_command
from nonebot.typing import T_State
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Message, Bot, Event, MessageSegment
from nonebot.rule import to_me

'''
提供image prompt参考和选项选择
'''


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""


# 输入关键字'ch'触发
style = on_keyword({'/style'})


@style.got('/style', prompt='请回复你的出生日期\n如:2003 9 27\n可回复\'取消\'停止')
async def get_live_time(bot: Bot, state: T_State, event: Event):
    global monthList
    a = state['/style']
    await style.finish(a)
    await style.finish(str[a])
    if str(a) == "取消":
        await style.finish("已取消")
    if int(str[a])<0 or int(str[a])>10:
        await style.finish("输入错误，已停止")
    await style.finish(str[a])




# 传递风格
class StyleHolder:
    def __init__(self):
        self.string = ""

    def add_style(self,new_style):
        self.string += new_style

    def get_style(self):
        return self.string