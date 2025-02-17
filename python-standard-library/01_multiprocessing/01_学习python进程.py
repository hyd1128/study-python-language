#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/16 11:17
# @Author : limber
# @desc :

# Process 类
# 在 multiprocessing 中，通过创建一个 Process 对象然后调用它的 start() 方法来生成进程。
# Process 和 threading.Thread PI 相同。 一个简单的多进程程序示例是:

# from multiprocessing import Process
#
#
# def f(name):
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()


####################################
from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())  # 返回父进程ID
    print('process id:', os.getpid())   # 获取当前进程ID


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
