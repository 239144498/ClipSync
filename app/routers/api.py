# -*- coding: utf-8 -*-
# @Time    : 2023/5/29
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : api.py
# @Software: PyCharm
from fastapi import APIRouter
from fastapi.params import Body
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse

from app.config.conf import conf
from app.core.sync import client
from app.enums.model import DataType
from app.models.response import Response200, Response400
from app.schemas.model import Clip


router = APIRouter(tags=['剪贴板服务'])


@router.get('/', summary='首页', response_class=HTMLResponse)
async def home(request: Request):
    context = {'request': request}
    return request.app.state.jinja.TemplateResponse("index.html", context=context)


@router.post("/copy", summary='复制剪贴板', response_class=JSONResponse)
async def pbcopy(data: Clip = Body()):
    try:
        config = conf.get_config()
        client.publish(config.config.get("MQTT_CLIENT", "publish"), payload=data.dict())
        return Response200(msg="复制成功")
    except Exception as error:
        return Response400(msg="复制失败")


@router.get("/paste", summary='粘贴剪贴板', response_class=JSONResponse)
async def pbpaste():
    try:
        return Response200(data=Clip(type=DataType.TEXT.value, value=client.clip.paste()).dict())
    except Exception as error:
        return Response400(msg="粘贴失败")


@router.get("/history", summary='历史剪贴板', response_class=JSONResponse)
async def history():
    try:
        return Response200(data=list(client.clip_history()))
    except Exception as error:
        return Response400(msg="获取历史剪贴板失败")


@router.get('/favicon.ico', include_in_schema=False)
async def home():
    return RedirectResponse('/static/img/logo.png')
