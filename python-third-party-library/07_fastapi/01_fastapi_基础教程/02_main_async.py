#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/15 10:04
# @Author : limber
# @desc :


from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}