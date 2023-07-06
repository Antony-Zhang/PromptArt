from pydantic import BaseModel, Extra
from nonebot import on_keyword, on_message
from nonebot import on_notice, Bot
from nonebot.adapters.onebot.v11 import Message, GroupMessageEvent, MessageSegment,Event
from nonebot.rule import to_me

'''
引导语：1、欢迎使用
        2、 /imagine + 诗句 → prompt词
        3、 /style + 风格 →
'''

#enter=on_keyword({"/help"})
enter = on_message(rule=to_me())


@enter.handle()
async def _(bot:Bot,event:Event):
    file_path = r'C:\Users\小白\Desktop\mj\mountain.png'
    image_seg = MessageSegment.image(file=f'file:///{file_path}')

    await bot.send(event, message=image_seg)

    content = "\n 欢迎使用由”想名字“团队开发的PromptArt-Midjourney提示词生成器 \n" \
              "输入 ”/imagine + 诗句“，生成Midjourney提示词 \n" \
              "输入 ”/style”获取风格提示 \n1、"

    message =  content
    # MessageSegment.at(event.user_id) +
    await enter.finish(message)


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""


