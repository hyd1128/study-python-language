#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/2 22:45
# @Author : limber
# @desc :

"""
可等待对象有三种：协程、任务、Future
"""
import asyncio


# 可等待对象：任务
async def nested():
    return 42


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
