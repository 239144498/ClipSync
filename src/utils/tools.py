# -*- coding: utf-8 -*-
# @Time    : 2023/5/28
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : utils.py
# @Software: PyCharm
from os import environ
from sys import platform
from platform import platform as _platform


def _get_platform():
    # 如果设置了环境变量PLATFORM，则使用环境变量的值
    custom = environ.get("PLATFORM")
    if custom:
        return custom
    elif 'iphone' in _platform().lower():
        return 'ios'
    elif 'P4A_BOOTSTRAP' in environ:
        return 'android'
    elif 'ANDROID_ARGUMENT' in environ:
        # We used to use this method to detect android platform,
        # leaving it here to be backwards compatible with `pydroid3`
        # and similar tools outside kivy's ecosystem
        return 'android'
    elif platform in ('win32', 'cygwin'):
        return 'win'
    elif platform == 'darwin':
        return 'macosx'
    elif platform.startswith('linux'):
        return 'linux'
    elif platform.startswith('freebsd'):
        return 'linux'
    return 'unknown'


