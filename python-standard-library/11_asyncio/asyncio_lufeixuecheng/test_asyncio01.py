#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/8/28 13:03
# @Author : limber
# @desc :

'''
协程：通过一个线程在多个上下文中京女性来回切换执行

对于计算类型操作，使用协程会降低性能，对于IO类型操作，使用协程会提升性能

协程函数：定义形式为 async def
协程对象： 调用协程函数所返回的对象


'''

import asyncio

async def func():
    print("执行协程函数的内部代码")
    response = await asyncio.sleep(2)
    print("IO请求结束，结果为：" + str(response))

result = func()

asyncio.run(result)


