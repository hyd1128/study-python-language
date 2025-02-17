"""
    datetrigger:
"""

from datetime import date, datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


def my_job(text):
    print(text)


# job 将在 2009 年 11 月 6 日 16:30:05 运行
# sched.add_job(my_job, "date", run_date=datetime(2024, 10, 24, 15, 1, 0), args=["text"])
# 另一种写法
sched.add_job(func=my_job, trigger="date", run_date="2024-10-24 15:03:00", args=["text"])

sched.start()
