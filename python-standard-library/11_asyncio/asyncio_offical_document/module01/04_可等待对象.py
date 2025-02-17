#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/2 22:45
# @Author : limber
# @desc :

"""
可等待对象有三种：协程、任务、Future
"""
import asyncio


# 可等待对象：协程
async def nested():
    return 42


async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # nested()

    # Let's do it differently now and await it:
    print(await nested())

asyncio.run(main())


