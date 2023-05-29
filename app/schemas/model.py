# -*- coding: utf-8 -*-
# @Time    : 2023/5/28
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : base.py
# @Software: PyCharm
import os
import time
from typing import Union, List
from pydantic import BaseModel, Field, validator
from pathlib import Path

from app.config.setupsetting import sysuuid, sysmodel, hostname


class Clip(BaseModel):
    id: str = sysuuid
    driver: str = sysmodel
    name: str = hostname
    time: float = Field(default_factory=time.time)
    type: int
    value: Union[str, List[Path]]

    @validator('value')
    def passwords_match(cls, value, ):
        return value.rstrip(os.linesep)  # 去除末尾换行符
