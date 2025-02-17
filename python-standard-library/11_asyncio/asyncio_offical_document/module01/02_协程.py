#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/2 22:29
# @Author : limber
# @desc :

import asyncio
import time


async def say_after(delay, what):
    print(1)
    await asyncio.sleep(delay)
    # time.sleep(delay)
    print(2)
    print(what)


# 任然是串行
async def main():
    print(f"started at {time.strftime('%X')}")

    # await say_after(2, "hello")
    # await say_after(2, "world")

    # 通过结果可知，协程函数返回的是协程对象，通过事件循环执行完后才获得值
    a = say_after(2, "hello")
    b = say_after(2, "hello")

    # 查看类型
    print(type(a))
    print(type(b))

    await a
    await b

    print(f"started at {time.strftime('%X')}")


# 创建事件循环列表 创建异步上下文
asyncio.run(main())
