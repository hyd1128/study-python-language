#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/11/17 1:50
# @Author : limber
# @desc :
import time

from fastapi import FastAPI, Request

app = FastAPI()


# 创建一个中间件
# 固定格式
@app.middleware("http")
async def add_process_time_header_one(request: Request, call_next):
    # start_time = time.perf_counter()
    print("中间件1执行")
    response = await call_next(request)
    print("中间件1结束")
    # process_time = time.perf_counter() - start_time
    # response.headers["X-time"] = str(process_time)
    return response


@app.middleware("http")
async def add_process_time_header_two(request: Request, call_next):
    print("中间件2执行")
    response = await call_next(request)
    print("中间件2结束")
    return response


@app.middleware("http")
async def add_process_time_header_three(request: Request, call_next):
    print("中间件3执行")
    response = await call_next(request)
    print("中间件3结束")
    return response



@app.get("/")
def read_root():
    return {"hello": "world"}
