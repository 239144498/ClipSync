# -*- coding: utf-8 -*-
# @Time    : 2023/5/28
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : base.py
# @Software: PyCharm
from enum import Enum


class Platform(Enum):
    WINDOWS = 1
    LINUX = 2
    MACOS = 3
    IOS = 4
    ANDROID = 5
    OTHER = 6


class DataType(Enum):
    TEXT = 1
    IMAGE = 2
    FILE = 3




