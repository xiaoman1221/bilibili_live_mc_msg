# -*- coding: utf-8 -*-

#加载所有API
from mcdreforged.api.all import *
#加载库文件
from bilibili_live_mc_msg import libs
#加载依赖
import asyncio
import random
import blivedm

#当插件被加载时(on_load)
def on_load(server: PluginServerInterface, old):
    server.logger.info(server.tr('bilibili_live_mc_msg.load_message'))
#强缩进，主要空格！