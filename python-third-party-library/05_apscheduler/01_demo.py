#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/24 14:04
# @Author : limber
# @desc :


# 使用apischedule的几个步骤
# 1、创建调度器
# 2、创建任务
# 3、添加任务到调度器
# 4、启动调度器

from apscheduler.schedulers.blocking import BlockingScheduler

# 创建调度器
scheduler = BlockingScheduler()


# 创建任务
def job():
    print("I'm working...")


# 添加任务到调度器
# 每隔5秒钟执行一次任务
scheduler.add_job(job, 'interval', seconds=5)

"""
触发器  trigger date interval cron
作业储存器
执行器
调度器
"""

scheduler.start()