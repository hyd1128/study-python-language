#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/16 10:30
# @Author : limber
# @desc :

from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None, ads_id1: Annotated[str | None, Cookie()] = None):
    print(Cookie())
    print(ads_id1)
    print(ads_id)
    return {"ads_id": ads_id}