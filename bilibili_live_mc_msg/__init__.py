# -*- coding: utf-8 -*-

#加载所有API
from mcdreforged.api.all import *
#加载库文件
from bilibili_live_mc_msg import *
#加载依赖
import asyncio
from bilibili_live_mc_msg.libs import *
import blivedm
import random

#当插件被加载时(on_load)
def on_load(server: PluginServerInterface, prev_module):
    global reload_counter
    if prev_module is None:
        server.logger.info(server.tr('main_msg.load_message'))
        server.register_command(
            Literal('!!blhx').
                then( 
                    Literal('room').   
                        then(
                            Literal('list').runs(lambda src, ctx: get_room_list(src))
                        ).
                        then(
                            Literal('remove').
                                then(
                                    #callback4 = lambda src: src.reply('pong')
                                    Integer('room_id').runs(lambda src, ctx: del_live_room(ctx["room_id"],src))
                                )
                        ).
                        then(Literal('add').
                                then(
                                    Integer('room_id').
                                        then(
                                            Text('room_name').runs(lambda src, ctx: add_live_room(ctx["room_id"], ctx["room_name"],src))
                                        )
                                )
                        ).
                        then(
                            Literal('start').runs(room_start_sync())
                        ).
                        then(
                            Literal('stop').runs(room_stop_sync())
                        ).
                        then(
                            Literal('reload').runs(room_reload_sync())
                        )
                )
            )
        server.register_command(
            Literal('!!blhx').
                then( 
                    Literal('help').runs(lambda src: print_help_message(src))
                )
        )
    else:
        server.logger.info(server.tr('main_msg.reload_message'))
        server.say(server.tr('main_msg.reload_message'))
 
#服务器Done的时候
def on_server_startup(server: PluginServerInterface):
    #构建指令
    server.logger.info(server.tr('main_msg.server_start_message'))
    server.say(server.tr('main_msg.server_start_message'))

    #main()

#当服务器有人加入时的欢迎信息
def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    server.say('Welcome to Minectaft server ,{}'.format(player))

#当服务器有人离开时的信息
def on_player_lift(server: PluginServerInterface, player: str, info: Info):
    server.say('Goodbye ,{}'.format(player))

#当服务器停止的时候
def on_server_stop(server: PluginServerInterface, server_return_code: int):
    if server_return_code != 0:
        server.logger.info(server.tr('main_mag.server_error_stop_message'))

    else:
        server.logger.info(server.tr('main_mag.server_stop_message'))
