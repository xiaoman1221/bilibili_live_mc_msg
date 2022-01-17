# -*- coding: utf-8 -*-

#加载所有API
from mcdreforged.api.all import *
#加载库文件
from bilibili_live_mc_msg import libs
#加载依赖
import asyncio
import blivedm
import random

#当插件被加载时(on_load)
def on_load(server: PluginServerInterface, prev_module):
    global reload_counter
    if prev_module is None:
        server.logger.info(server.tr('main_msg.load_message'))
        #server.register_command(command_list)
        #server.register_help_message(...)
    else:
        server.logger.info(server.tr('main_msg.reload_message'))
        server.say(server.tr('main_msg.reload_message'))
 
#服务器Done的时候
def on_server_startup(server: PluginServerInterface):
    server.logger.info(server.tr('main_msg.server_start_message'))
    server.say(server.tr('main_msg.server_start_message'))
    
    libs.main()

#当服务器有人加入时的欢迎信息
def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    server.say('Welcome {}'.format(player))

#当服务器有人离开时的信息
def on_player_left(server: PluginServerInterface, player: str, info: Info):
    server.say('Goodbye {}'.format(player))

#当服务器停止的时候
def on_server_stop(server: PluginServerInterface, server_return_code: int):
    if server_return_code != 0:
        server.logger.info(server.tr('main_mag.server_error_stop_message'))

    else:
        server.logger.info(server.tr('main_mag.server_stop_message'))
#尝试构建一些指令
class command_list():
    pass
