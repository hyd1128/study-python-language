#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/16 17:05
# @Author : limber
# @desc :


import multiprocessing
import time

# 进程之间不共享全局变量
# 定义全局变量

g_list = list()


# 添加数据的任务
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add: " + str(i))
        time.sleep(0.2)


def read_data():
    print("read_data", g_list)


if __name__ == '__main__':
    # 创建添加数据的子进程
    add_data_process = multiprocessing.Process(target=add_data)
    # 创建读取数据的子进程
    read_data_process = multiprocessing.Process(target=read_data)

    # 启动子进程执行对应的任务
    add_data_process.start()
    # 主进程等待添加数据的子进程执行完成以后程序再继续往下执行，读取数据
    add_data_process.join()
    read_data_process.start()

    print("main:", g_list)

    # 总结: 多进程之间不共享全局变量
