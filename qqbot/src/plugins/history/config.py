import json

from pydantic import BaseModel, Extra
from nonebot import on_keyword, on_command
from nonebot.params import CommandArg, ArgStr
from nonebot.adapters.onebot.v11 import Message, GroupMessageEvent, MessageSegment,Event
'''
查看历史
'''
# 发送历史诗句+根据输入返回
history_show = on_keyword({'#history'})


@history_show.got("num", prompt=f"请输入要查看的古诗序号，输入\"取消”退出\n"
                                f"1.古道西风瘦马。夕阳西下，断肠人在天涯 \n"
                                f"2.两岸猿声啼不住，轻舟已过万重山 \n"
                                f"3.落霞与孤鹜齐飞，秋水共长天一色 \n"
                                f"4.年年越溪女，相忆采芙蓉")
async def show_history(arg: str = ArgStr("num")):
    if arg == "取消":
        await history_show.finish("已退出")
    if int(arg) <= 0 or int(arg) > 4:
        await history_show.reject("请重新输入合法的序号")
    else:
        url = "../resource/"+arg+".json"
        with open(url,"r") as j:
            data = json.load(j)
        # await history_show.finish(data["prompt"]+"\n"+data["url"])
        text = data["prompt"]
        image_seg = MessageSegment.image(file=f'file:///{data["url"]}')
        await history_show.finish(text + "\n" + image_seg)


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""
