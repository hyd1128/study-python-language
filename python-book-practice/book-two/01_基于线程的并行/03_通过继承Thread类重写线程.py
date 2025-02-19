#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f"starting {self.name}")
        print_time(self.name, self.counter, 5)
        print(f"exit {self.name}")


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            import _thread
            _thread.exit()
        time.sleep(delay)
        print(f"{thread_name}, {time.ctime(time.time())}")
        counter -= 1


# 创建新线程
thread_one = MyThread(1, 'thread_one', 1)
thread_two = MyThread(2, 'thread_two', 2)

# 启动新线程
thread_one.start()
thread_two.start()
print('exiting main thread')
