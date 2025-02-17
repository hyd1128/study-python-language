#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/11/17 1:50
# @Author : limber
# @desc :

"""
fastapi 处理错误

"""
import time
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# items = {"foo": "the foo wwrestlers"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         # 因为该httpexception是python异常 所以以rais返回错误 不能够以return 返回错误
#         raise HTTPException(status_code=404,
#                             detail="Item not found",
#                             # 添加一个请求头
#                             headers={"X-Error": "---There goes my error"})
#     return {"item": items[item_id]}

# 覆盖 HTTPException 错误处理器
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# 覆盖默认异常处理器
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


#
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}
