#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/29 22:32
# @Author : limber
# @desc :

"""
以下是一个综合示例，展示了如何结合触发器、作业存储、执行器和调度器：
"""

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.triggers.cron import CronTrigger

# 配置作业存储和执行器
jobstores = {'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')}
executors = {'default': ThreadPoolExecutor(10)}

# 创建调度器
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors)


# 定义任务
def my_task():
    print("任务运行中...")


# 添加任务
trigger = CronTrigger(hour=22, minute=38)  # 每天9:30运行
scheduler.add_job(my_task, trigger=trigger, id='daily_task')

# 启动调度器
scheduler.start()
