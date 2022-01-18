# -*- coding: utf-8 -*-

#加载API
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
#监听单个------------------------------------------
async def run_single_client():
    """
    监听一个直播间
    """
    room_id = random.choice(ROOM_IDS)
    # 如果SSL验证失败就把ssl设为False，B站真的有过忘续证书的情况
    client = blivedm.BLiveClient(room_id, ssl=True)
    handler = BLH_Handler()
    client.add_handler(handler)

    client.start()
    try:
        # 演示5秒后停止
        await asyncio.sleep(5)
        client.stop()

        await client.join()
    finally:
        await client.stop_and_close()
#监听多个------------------------------------------
async def run_multi_client():
    """
    同时监听多个直播间
    """
    clients = [blivedm.BLiveClient(room_id) for room_id in ROOM_IDS]
    handler = BLH_Handler()
    for client in clients:
        client.add_handler(handler)
        client.start()

    try:
        await asyncio.gather(*(
            client.join() for client in clients
        ))
    finally:
        await asyncio.gather(*(
            client.stop_and_close() for client in clients
        ))
#类-----------------------------------------
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
#监听MIan主程序
async def main():
    await run_single_client()
    await run_multi_client()

#指令树相关！！------------------------------------------------------------------
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
    del ROOM_IDS[count]     ##使用del删除元素
    return 0
def get_room_list(server: PluginServerInterface):
    for item in ROOM_IDS:
        server.say(item)  #遍历数组
def get_help_info():
    return '获取帮助info'
def reload_room():
    pass
