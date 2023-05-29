# -*- coding: utf-8 -*-
# @Time    : 2023/5/28
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : setupsetting.py
# @Software: PyCharm
import uuid
import socket
from pathlib import Path
from app.enums.model import Platform
from app.utils.tools import _get_platform


ROOT_DIR = Path(__file__).parent.parent.parent
SRC = ROOT_DIR / "app"
CONFIG = SRC / "config"
static_url_prefix: str = '/static'
static_dir = ROOT_DIR / 'static'
jinja2_templates_dir = ROOT_DIR / 'templates'

print("根目录：", ROOT_DIR)
hostname = socket.gethostname()
print("主机名称：", hostname)

sysmodel = _get_platform()
print("系统型号：", sysmodel)

if sysmodel == "win":
    sysname = Platform.WINDOWS
    print("您正在使用 Windows 操作系统")
elif sysmodel == "linux":
    sysname = Platform.LINUX
    print("您正在使用 Linux 操作系统")
elif sysmodel == "macosx":
    sysname = Platform.MACOS
    print("您正在使用 macOS 操作系统")
elif sysmodel == "android":
    sysname = Platform.ANDROID
    print("您正在使用 Android 操作系统")
elif sysmodel == "ios":
    sysname = Platform.IOS
    print("您正在使用 iOS 操作系统")
else:
    sysname = Platform.OTHER
    print("当前系统不能被识别")

sysuuid = ''.join(("%012x" % uuid.getnode())[i:i + 2] for i in range(0, 12, 2))

