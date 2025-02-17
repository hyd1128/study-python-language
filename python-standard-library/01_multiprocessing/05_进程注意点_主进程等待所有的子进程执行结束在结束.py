#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/16 17:14
# @Author : limber
# @desc :

import multiprocessing
import time


# 定义进程所需要执行的任务
def task():
    for i in range(10):
        print("任务执行中...")
        time.sleep(1)


if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 设置守护主进程，主进程退出子进程直接销毁，子进程的生命周期依赖与主进程
    # sub_process.daemon = True
    sub_process.start()

    time.sleep(0.5)
    # 让子进程销毁
    # sub_process.terminate()
    # sub_process.join()
    print("over")
    exit()

    # 总结： 如果在主进程没有显示的调用sub_process.join(),则主进程不会等待子进程结束,反之会等待子进程结束后再结束
    # 如果想要主进程退出子进程销毁，可以设置守护主进程或者在主进程退出之前让子进程销毁



