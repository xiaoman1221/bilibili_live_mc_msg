# -*- coding: utf-8 -*-

#加载所有API
from mcdreforged.api.all import *
#加载库文件
from bilibili_live_mc_msg import *
from bilibili_live_mc_msg.libs import *
#组建命令
def register_blhx_command(src: PluginServerInterface):
    src.register_command(
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
                        Literal('start').runs(room_start_sync())
                    ).
                    then(
                        Literal('reload').runs(room_reload_sync())
                    )
                ).
            then(
                Literal('help').
                    then(
                        Integer('page')).
                            runs(lambda src: print_help_message(src))))