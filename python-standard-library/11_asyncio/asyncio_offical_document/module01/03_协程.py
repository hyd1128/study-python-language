#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/2 22:37
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


async def main():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    print(type(task1))
    print(type(task2))

    # 等待两个任务都要完成需要2秒
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
