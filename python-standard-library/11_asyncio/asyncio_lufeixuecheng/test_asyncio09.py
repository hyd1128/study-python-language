#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/8/28 14:52
# @Author : limber
# @desc :

import asyncio


async def func1():
    print("1")
    await asyncio.sleep(2)
    print("2")


async def func2():
    print("3")
    await asyncio.sleep(3)
    print("4")


coroutine_list = [func1(), func2()]

asyncio.run(asyncio.wait(coroutine_list))

