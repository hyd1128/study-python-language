#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/16 16:58
# @Author : limber
# @desc :

import multiprocessing
import time


# 跳舞任务
def dance():
    for i in range(5):
        print("跳舞中....")
        time.sleep(0.2)


# 唱歌任务
def sing():
    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)


if __name__ == '__main__':
    dance_process = multiprocessing.Process(target=dance, name="myprocess_one")
    sing_process = multiprocessing.Process(target=sing)
    # 查看各个进程的名称
    print("dance_process_id: " + str(dance_process.name))
    print("sing_process_id: " + str(sing_process.name))
    # 启动子进程执行对应的任务
    dance_process.start()
    sing_process.start()
