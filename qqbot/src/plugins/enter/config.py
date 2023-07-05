from pydantic import BaseModel, Extra
from nonebot import on_keyword, on_message
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Message, GroupMessageEvent, MessageSegment
from nonebot.rule import to_me

'''
引导语：1、欢迎使用
        2、 /imagine + 诗句 → prompt词
        3、 /style + 风格 →
'''

# word=on_keyword({""},rule=to_me())
word = on_message(rule=to_me())


@word.handle()
async def _(event:GroupMessageEvent):
    content = "\n 欢迎使用由”想名字“团队开发的PromptArt-Midjourney提示词生成器 \n" \
              "输入 ”/imagine + 诗句“，生成Midjourney提示词 \n" \
              "输入 ”/style”获取风格提示"
    message = MessageSegment.at(event.user_id) + content
    await word.finish(message)


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""


