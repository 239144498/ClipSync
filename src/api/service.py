# -*- coding: utf-8 -*-
# @Time    : 2023/5/26
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : api.py
# @Software: PyCharm
from fastapi import FastAPI
from fastapi.params import Form

from src.config.conf import conf
from src.core.sync import client
from src.enums.model import DataType
from src.models.response import Response200, Response400
from src.schemas.model import Clip

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print("ClipSync is starting up...")


@app.get("/")
async def root():
    return {
        "status": "running",
        "message": [
            "欢迎使用ClipSync服务",
        ]
    }


@app.post("/copy")
async def pbcopy(data:str = Form(...)):
    try:
        config = conf.get_config()
        print(data)
        client.publish(config.config.get("MQTT_CLIENT", "publish"), Clip(type=DataType.TEXT.value, value=data).dict())
        return Response200(msg="复制成功")
    except Exception as error:
        return Response400(msg="复制失败")


@app.get("/paste")
async def pbpaste():
    try:
        return Response200(data=client.clip.paste())
    except Exception as error:
        return Response400(msg="粘贴失败")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
