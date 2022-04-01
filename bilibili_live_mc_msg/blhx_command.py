# -*- coding: utf-8 -*-

#加载所有API
from mcdreforged.api.all import *
#加载库文件
from bilibili_live_mc_msg.libs import add_live_room, del_live_room, get_room_list, print_help_message, room_reload_sync, room_start_sync, room_stop_sync


global live_status
live_status=False 

def add_help_command(server):
    server.register_help_message('!!blhx', 'BiliBili弹幕姬，小满特制版')
    server.register_help_message('!!blhx help', '获得blhx的帮助信息')
    server.register_help_message('!!blhx room list', '获取房间列表')
    server.register_help_message('!!blhx room add <room_id> <room_name>', '添加房间到列表')
    server.register_help_message('!!blhx room remove <copunt>', '移除列表里的房间')
    server.register_help_message('!!blhx room start ', '开始同步')
    server.register_help_message('!!blhx room stop ', '停止同步')
    server.register_help_message('!!blhx room relaod ', '重新运行')
def add_command(server):
    server.register_command(
        Literal('!!blhx').
            then( 
                Literal('room').   
                    then(
                        Literal('list').runs(lambda src: get_room_list(src))
                        ).
                    then(
                        Literal('remove').
                            then(
                                #callback4 = lambda src: src.reply('pong')
                                Integer('room_id').
                                runs(lambda src, ctx: del_live_room(ctx["room_id"],src))
                            )
                        ).
                    then(
                        Literal('add').
                            then(
                                Integer('room_id').
                                     then(
                                        GreedyText('room_name').
                                            runs(lambda src, ctx: add_live_room(ctx["room_id"], ctx["room_name"],src))
                                    )
                            )
                    ).
                    then(
                        Literal('start').runs(lambda src:room_start_sync(src,live_status))
                    ).
                    then(
                        Literal('reload').runs(lambda src:room_reload_sync(src,live_status))
                    ).
                    then(
                        Literal('stop').runs(lambda src:room_stop_sync(src,live_status))
                    )
                ).
            then(
                Literal('help').runs(lambda src: print_help_message(src))))

