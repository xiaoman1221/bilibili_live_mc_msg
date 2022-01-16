from mcdreforged.api.all import *

from bilibili_live_mc_msg import libs


def on_load(server: PluginServerInterface, old):
    server.logger.info(server.tr('bilibili_live_mc_msg.load_message'))
