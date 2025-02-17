#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/16 16:01
# @Author : limber
# @desc :

import time
from fastapi import  FastAPI, Request
import asyncio

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def get_run_time():
    # import time
    # time.sleep(5)
    await asyncio.sleep(5)
