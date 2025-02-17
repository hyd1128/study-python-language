#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/8/28 13:59
# @Author : limber
# @desc :

import asyncio
async def others():
    print("start")
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response1 = await others()
    print("IO请求结束，结果为：", response1)
    response2 = await others()
    print("IO请求结束，结果为：", response2)

asyncio.run(func())

'''
协程编写：
1、首先编写一个 async修饰的协程函数
     
2、创建一个事件循环 
    loop = asyncio.get_event_loop()

3、将协程当作一个任务提交到事件循环的列表当中，协程执行完之后结束
    loop.run_until_complete(result)
   
补充：在py3.7之后，2，3步骤可以使用asyncio.run()异步搞定
 asyncio.run(result)

'''


