#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/6 13:35
# @Author : limber
# @desc :

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

lock = threading.Lock()


# 任务函数，计算平方数
def calculate_square(n):
    # with lock:
    #     print(f"Calculating square of {n}")
    print(f"Calculating square of {n}")
    time.sleep(2)
    return n * n


# 任务列表
numbers = [1, 2, 3, 4, 5]

# 创建一个线程池
executor = ThreadPoolExecutor(max_workers=3)

# 提交任务到线程池
futures_to_number = {executor.submit(calculate_square, number): number for number in numbers}

# 获取结果
for future in as_completed(futures_to_number):
    number = futures_to_number[future]
    try:
        result = future.result()
        # with lock:
        #     print(f"Square of {number} is {result}
        print(f"Square of {number} is {result}")
    except Exception as e:
        print(f"{number}---{e}")

