#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor

class BoundedThreadPoolExecutor(ThreadPoolExecutor):
    def __init__(self, max_workers, max_queue_size):
        super().__init__(max_workers=max_workers)
        self._work_queue = queue.Queue(maxsize=max_queue_size)

task_queue = queue.Queue()

for i in range(100):
    task_queue.put(i)

print("初始化时队列中的元素个数:" + str(task_queue.qsize()))


def task(num: int):
    print("消费的队列对象为:" + str(num))
    time.sleep(20)


def see_task_queue():
    while True:
        time.sleep(1)
        print("当前队列中剩余元素:" + str(task_queue.qsize()))


t = threading.Thread(target=see_task_queue)
t.start()

with BoundedThreadPoolExecutor(max_workers=10, max_queue_size=1) as executor:
    while not task_queue.empty():
        executor.submit(task, task_queue.get())

"""
    当任务数大于线程池的线程数，当线程池中线程用完的时候，任务还会继续被线程池领取，此时存放任务的地方为线程池原生的线程任务队列，
    直至内存耗尽
"""


