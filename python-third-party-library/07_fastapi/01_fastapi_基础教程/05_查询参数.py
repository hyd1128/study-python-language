#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/15 14:34
# @Author : limber
# @desc :

from fastapi import FastAPI
from typing import Union

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# 查询参数
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# 包含路径参数和可选查询参数
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item