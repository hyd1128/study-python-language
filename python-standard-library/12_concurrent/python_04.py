#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/6 15:50
# @Author : limber
# @desc :

import concurrent.futures

# def fibonacci(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(n - 1):
#         a, b = b, a + b
#     return b
#
# numbers = [5, 10, 15, 20, 25]
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     future_list = [executor.submit(fibonacci, i) for i in numbers]
#
#     for future in future_list:
#         print(future.result())


# import concurrent.futures
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(n - 1):
#         a, b = b, a + b
#     return b
#
# numbers = [5, 10, 15, 20, 25]
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     results = executor.map(fibonacci, numbers)
#
#     for result in results:
#         print(result)

import concurrent.futures
import time

def task(n):
    time.sleep(n)  # 模拟任务运行时间
    return n

numbers = [3, 1, 2]  # 任务的模拟运行时间

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, num) for num in numbers]

    for future in futures:
        print(future.result())