# -*- codeing = utf-8 -*-
# @Time : 2023-07-06 10:33
# @Author : Shelly
# @File : __init__.py.py
# @Software : PyCharm
#
from nonebot import get_driver

from .style import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

