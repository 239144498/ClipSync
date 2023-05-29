# -*- coding: utf-8 -*-
# @Time    : 2023/5/27
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : main.py
# @Software: PyCharm
import uvicorn
from app.config.conf import conf


def main():
    config = conf.get_config().config
    uvicorn.run("app.service:app", host=config.get('API_SERVER', 'host'), port=config.getint('API_SERVER', 'port'))


if __name__ == '__main__':
    main()

