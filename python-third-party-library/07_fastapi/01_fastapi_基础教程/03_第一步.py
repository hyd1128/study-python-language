#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/15 13:40
# @Author : limber
# @desc :

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    # 自动将dict对象转换成json
    return {"message": "hello world"}
