#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/2 22:16
# @Author : limber
# @desc :


import asyncio


async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")


asyncio.run(main())
# 协程函数要么只能在asyncio中运行，也可以在异步上下文中用 await main() 来运行它。
# main()
