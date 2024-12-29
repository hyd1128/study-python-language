from datetime import date, datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

time_ = datetime(2024, 12, 27, 16, 8, 0)


# time_str = datetime(2009, 11, 6, 16, 30, 5)

def my_job(text):
    print(text)


# job 将在 2009 年 11 月 6 日 16:30:05 运行
sched.add_job(my_job, "date", run_date=time_, args=["text"])
# 另一种写法
# sched.add_job(my_job, "date", run_date=, args=["text"])

sched.start()
