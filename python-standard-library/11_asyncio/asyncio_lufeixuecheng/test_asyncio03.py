#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/8/28 13:03
# @Author : limber
# @desc :

'''
协程：通过一个线程在多个上下文中京女性来回切换执行

对于计算类型操作，使用协程会降低性能，对于IO类型操作，使用协程会提升性能
'''
import time

import aiohttp
import asyncio

async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('_')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
        'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
        'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    end_time = time.time()

    print(f"运行耗时: {end_time - start_time}s")