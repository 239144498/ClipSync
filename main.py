# -*- coding: utf-8 -*-
# @Time    : 2023/5/27
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : main.py
# @Software: PyCharm
import uvicorn
from threading import Thread
from src.config.conf import conf
from src.task.task import comparison


def main():
    config = conf.get_config().config
    t = Thread(target=comparison)
    t.daemon = True
    t.start()
    uvicorn.run("src.api.service:app", host=config.get('API_SERVER', 'host'), port=config.getint('API_SERVER', 'port'))


if __name__ == '__main__':
    main()

