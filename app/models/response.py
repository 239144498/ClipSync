# -*- coding: utf-8 -*-
# @Time    : 2023/5/28
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : response.py
# @Software: PyCharm
from typing import Union
from fastapi.responses import JSONResponse, Response


def Response200(*, data: Union[list, dict, str] = None, msg="请求成功", code=200) -> Response:
    return JSONResponse(
        status_code=code,
        content={
            "code": code,
            "msg": msg,
            "data": data,
        }
    )


def Response400(*, data: Union[list, dict, str] = None, msg="请求失败", code=400) -> Response:
    return JSONResponse(
        status_code=code,
        content={
            "code": code,
            "msg": msg,
            "data": data,
        }
    )