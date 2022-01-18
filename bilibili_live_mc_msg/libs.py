# -*- coding: utf-8 -*-

#加载API
from pickle import TRUE
from time import sleep
from mcdreforged.api.all import *
#加载依赖
import asyncio
import blivedm
import random


# 直播间ID的取值,看直播间URL
# 例子：https://live.bilibili.com/13007212,其中13007212就是直播间ID
# 支持多个直播间轮询
ROOM_IDS = [
    23367128,#DurexAir
    13007212 #xiaoman1221
]
def run_single_client():
    """
    监听直播间
    """
    room_id = random.choice(ROOM_IDS)
    # 如果SSL验证失败就把ssl设为False，B站真的有过忘续证书的情况
    # 睿叔叔我啊，最爱圈钱了（bushi
    client = blivedm.BLiveClient(room_id, ssl=True)

    handler = BLH_Handler()
    client.add_handler(handler)

    client.start()
    try:
        # 5秒后停止
        sleep(5)
        client.stop()

        client.join()
    finally:
        client.stop_and_close()
class BLH_Handler(blivedm.BaseHandler):
     def _on_heartbeat(self, client: blivedm.BLiveClient, message: blivedm.HeartbeatMessage,server: PluginServerInterface):
        server.say(f'[{client.room_id}] 当前人气值：{message.popularity}')
    
     def _on_danmaku(self, client: blivedm.BLiveClient, message: blivedm.DanmakuMessage,server: PluginServerInterface):
    
        server.say(f'[{client.room_id}] {message.uname}：{message.msg}')
     def _on_gift(self, client: blivedm.BLiveClient, message: blivedm.GiftMessage,server: PluginServerInterface):
        server.say(f'[{client.room_id}] {message.uname} 赠送{message.gift_name}x{message.num}'
              f' （{message.coin_type}瓜子x{message.total_coin}）')
    
     def _on_buy_guard(self, client: blivedm.BLiveClient, message: blivedm.GuardBuyMessage,server: PluginServerInterface):
        server.say(f'[{client.room_id}] {message.username} 购买{message.gift_name}')
    
     def _on_super_chat(self, client: blivedm.BLiveClient, message: blivedm.SuperChatMessage,server: PluginServerInterface):
        server.say(f'[{client.room_id}] 醒目留言 ¥{message.price} {message.uname}：{message.message}')

def main():
    while TRUE:
        run_single_client()
        sleep(5)
def print_help_message():
    return '帮助信息'
def print_unknown_argument_message():
    return '未知信息帮助信息'
def get_help_msg():
    return '获取帮助信息'
def get_page_count():
    #获取页数？？
    return 1
def add_live_room(roomid):
    ROOM_IDS.append(roomid)   ## 使用 append() 添加元素
    return 0
def add_live_room(count):
    del ROOM_IDS[count]
    return 0
def get_room_list(server: PluginServerInterface):
    for item in ROOM_IDS:
        server.say(item)
def get_help_info():
    return '获取帮助info'
def reload_room():
    pass