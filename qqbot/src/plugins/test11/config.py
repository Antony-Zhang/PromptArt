from pydantic import BaseModel, Extra
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""


word=on_keyword({"雷猴"})

@word.handle()
async def _():
    await word.finish(Message("我是崽种!"))