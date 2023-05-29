# -*- coding: utf-8 -*-
# @Time    : 2023/5/27
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : backtask.py
# @Software: PyCharm
import datetime
import time

from threading import Thread
from loguru import logger
from app.config.conf import conf
from app.core.sync import client
from app.enums.model import DataType
from app.schemas.model import Clip


def log_startup():
    logger.info(f"ClipSync startup at {datetime.datetime.now()}")


def comparison():
    config = conf.get_config().config
    while True:
        if client.clip.change_state():
            recent_txt = client.clip.paste()
            client.publish(config.get("MQTT_CLIENT", "publish"),
                           Clip(type=DataType.TEXT.value, value=recent_txt).dict())
        time.sleep(0.2)


Thread(target=comparison, daemon=True).start()
