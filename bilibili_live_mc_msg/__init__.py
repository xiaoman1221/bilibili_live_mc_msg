# -*- coding: utf-8 -*-

#加载所有API
from mcdreforged.api.all import *
#加载库文件
from bilibili_live_mc_msg import *
from bilibili_live_mc_msg.blhx_command import register_blhx_command
from bilibili_live_mc_msg.libs import *
#加载依赖
import asyncio
import random


     
#当插件被加载时(on_load)
def on_load(server: PluginServerInterface, prev_module):
    if prev_module is None:
        server.logger.info(server.tr('main_msg.load_message'))
        lambda src: register_blhx_command(src)

    else:
        server.logger.info(server.tr('main_msg.reload_message'))
        server.say(server.tr('main_msg.reload_message'))
        lambda server: register_blhx_command(server)

#服务器Done的时候
def on_server_startup(server: PluginServerInterface):
    #构建指令
    server.logger.info(server.tr('main_msg.server_start_message'))
    server.say(server.tr('main_msg.server_start_message'))
    #main()

#当服务器有人加入时的欢迎信息
def on_player_joined(server: PluginServerInterface, player: str):
    server.say('Welcome to Minectaft server ,{}'.format(player))

#当服务器有人离开时的信息
def on_player_lift(server: CommandSource, player: str):
    server.say('Goodbye ,{}'.format(player))

#当服务器停止的时候
def on_server_stop(server: PluginServerInterface, server_return_code: int):
    if server_return_code != 0:
        server.logger.info(server.tr('main_mag.server_error_stop_message'))

    else:
        server.logger.info(server.tr('main_mag.server_stop_message'))
