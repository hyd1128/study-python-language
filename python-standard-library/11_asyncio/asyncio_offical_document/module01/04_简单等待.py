#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/2 22:45
# @Author : limber
# @desc :

import asyncio

async def foo():
    return 42

async def main():
    # coro = asyncio.create_task(foo())
    coro = foo()
    # wait会自动将协程对象转化为task

    done, pending = await asyncio.wait({coro})
    print(done)
    print(pending)
    print(coro)
    print(coro in done)

asyncio.run(main())