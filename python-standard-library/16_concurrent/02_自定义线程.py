#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import queue
from concurrent.futures import ThreadPoolExecutor


class BoundedThreadPoolExecutor(ThreadPoolExecutor):
    def __init__(self, max_workers, max_queue_size):
        super().__init__(max_workers=max_workers)
        self._work_queue = queue.Queue(maxsize=max_queue_size)

# 任务函数
# def worker(task_id)

