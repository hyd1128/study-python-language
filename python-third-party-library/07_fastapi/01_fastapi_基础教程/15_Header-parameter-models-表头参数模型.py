#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/16 10:45
# @Author : limber
# @desc :


from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    # 添加这一行就会禁止额外的参数
    # model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    print(headers)
    return headers