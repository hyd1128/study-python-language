#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import concurrent.futures
import time


def task(n):
    time.sleep(n)
    return n


# 创建一个线程池
with concurrent.futures.ThreadPoolExecutor() as executor:
    # 提交任务
    futures = [executor.submit(task, i) for i in [2, 4, 1, 3]]

    # 等待任务完成
    # concurrent.futures.FIRST_COMPLETED：第一个完成的任务完成时返回。
    # concurrent.futures.FIRST_EXCEPTION：第一个抛出异常的任务完成时返回。
    # concurrent.futures.ALL_COMPLETED：所有任务完成时返回（这是默认值）。
    done, not_done = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_EXCEPTION)

    # 输出已完成的任务结果s
    for future in done:
        print(f"Task result: {future.result()}")