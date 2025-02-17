#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/16 11:51
# @Author : limber
# @desc :

from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    # 将Pydantic模型转换为dict，并将datetime转换为str。
    json_compatible_item_data = jsonable_encoder(item)
    print(json_compatible_item_data)
    fake_db[id] = json_compatible_item_data