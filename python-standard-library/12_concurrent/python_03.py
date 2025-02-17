#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/6 14:52
# @Author : limber
# @desc :

from concurrent.futures import ThreadPoolExecutor, as_completed
import math
import time

# 计算阶乘的函数，cpu计算密集型
def fibonacci(n):
    time.sleep(2)
    return math.factorial(n)

# 定义要计算的数字列表
numbers = [10, 20, 30, 40, 50]

# # 使用线程池的map方法
# with ThreadPoolExecutor(max_workers=3) as executor:
#     # 使用线程池并行计算阶乘
#     results = executor.map(Fibonacci, numbers)
#
#     # fs = [self.submit(fn, *args) for args in zip(*iterables)]
#     # 使用列表推导式，同时使用了函数解包
#
#
# for number, result in zip(numbers, results):
#     print(f"{result}--{result}")

# 使用as_computed来完成
executor = ThreadPoolExecutor(max_workers=5)
future_list = [executor.submit(fibonacci, i) for i in numbers]
for future in future_list:
    print(future.result())

# for future in as_completed(future_list):
#     # 状态？
#     # print(future.result())
#     print(future.result())

for future in future_list:
    print(future.result())

