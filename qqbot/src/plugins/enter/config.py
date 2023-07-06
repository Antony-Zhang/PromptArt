from pydantic import BaseModel, Extra
from nonebot import on_keyword
from nonebot import on_notice, Bot
from nonebot.adapters.onebot.v11 import Message, MessageSegment,Event
from nonebot.rule import to_me

'''
引导语：1、欢迎使用
        2、 /imagine + 诗句 → prompt词
        3、 /style + 风格 →
'''

enter = on_keyword({"#help"})
# enter = on_message(rule=to_me())


@enter.handle()
async def _(bot:Bot,event:Event):
    content = """
    欢迎使用由”想名字“团队开发的Midjourney提示词生成器——PromptArt！
    您可从历史示例直接选取满意的提示词，也可直接生成提示词
    
    #### 查看历史示例 ####
    1.输入"#history"查看示例
        
    #### 查看参考图片 ####
    输入"#style",输出参考风格图片，您可选择心仪的图片作为重要风格参考！
        
    #### 生成提示词 ####
    1.输入"#imagine + <诗句>" ，输出生图提示词
    如"#imagine 落霞与孤鹜齐飞，秋水共长天一色"
    2.输入"/imagine-<图片序号> + <诗句>" ，输出生图提示词，且指定生图风格
    如"#imagine-1 落霞与孤鹜齐飞，秋水共长天一色"
    """
    await enter.finish(content)


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""


