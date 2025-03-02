#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import schedule


# 使用装饰员安排工作
# from schedule import every, repeat, run_pending
# import time
#
#
# @repeat(every(10).seconds)
# def job():
#     print("I am a scheduled job")
#
#
# while True:
#     run_pending()
#     time.sleep(1)


# 将争论传递给工作
# import schedule
#
#
# def greet(name):
#     print('Hello', name)
#
#
# schedule.every(2).seconds.do(greet, name='Alice')
# schedule.every(4).seconds.do(greet, name='Bob')

# from schedule import every, repeat
#
#
# @repeat(every().second, "World")
# @repeat(every().day, "Mars")
# def hello(planet):
#     print("Hello", planet)


# cancle 取消工作
# import schedule
#
# def some_task():
#     print('Hello world')
#
# job = schedule.every().day.at('22:30').do(some_task)
# schedule.cancel_job(job)


# 运行一次
# import schedule
# import time
#
# def job_that_executes_once():
#     # Do some work that only needs to happen once...
#     return schedule.CancelJob
#
# schedule.every().day.at('22:30').do(job_that_executes_once)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)


# 找到所有工作
# import schedule
#
# def hello():
#     print('Hello world')
#
# schedule.every().second.do(hello)
#
# all_jobs = schedule.get_jobs()
# print(all_jobs)


# 取消所有的工作
# import schedule
#
# def greet(name):
#     print('Hello {}'.format(name))
#
# schedule.every().second.do(greet)
#
# schedule.clear()


# 得到几个工作, 被标签过滤
# import schedule
#
#
# def greet(name):
#     print('Hello {}'.format(name))
#
#
# schedule.every().day.do(greet, 'Andrea').tag('daily-tasks', 'friend')
# schedule.every().hour.do(greet, 'John').tag('hourly-tasks', 'friend')
# schedule.every().hour.do(greet, 'Monica').tag('hourly-tasks', 'customer')
# schedule.every().day.do(greet, 'Derek').tag('daily-tasks', 'guest')
#
# friends = schedule.get_jobs('friend')
# print(friends)


# 取消几个作业, 被标签过滤
# import schedule
#
# def greet(name):
#     print('Hello {}'.format(name))
#
# schedule.every().day.do(greet, 'Andrea').tag('daily-tasks', 'friend')
# schedule.every().hour.do(greet, 'John').tag('hourly-tasks', 'friend')
# schedule.every().hour.do(greet, 'Monica').tag('hourly-tasks', 'customer')
# schedule.every().day.do(greet, 'Derek').tag('daily-tasks', 'guest')
#
# schedule.clear('daily-tasks')


# 随机运行
# def my_job():
#     print('Foo')
#
# # Run every 5 to 10 seconds.
# schedule.every(1).to(3).seconds.do(my_job)
#
# while True:
#     schedule.run_pending()


# 运行工作直到指定的时间
# import schedule
# from datetime import datetime, timedelta, time
#
# def job():
#     print('Boo')
#
# # run job until a 18:30 today
# schedule.every(1).hours.until("18:30").do(job)
#
# # run job until a 2030-01-01 18:33 today
# schedule.every(1).hours.until("2030-01-01 18:33").do(job)
#
# # Schedule a job to run for the next 8 hours
# schedule.every(1).hours.until(timedelta(hours=8)).do(job)
#
# # Run my_job until today 11:33:42
# schedule.every(1).hours.until(time(11, 33, 42)).do(job)
#
# # run job until a specific datetime
# schedule.every(1).hours.until(datetime(2020, 5, 17, 11, 36, 20)).do(job)
# # 直到方法设置了作业截止日期。在截止日期之后，这项工作将不会运行。


# 直到下一次执行的时间
# import schedule
# import time
#
# def job():
#     print('Hello')
#
# schedule.every(5).seconds.do(job)
#
# while 1:
#     n = schedule.idle_seconds()
#     print(n)
#     if n is None:
#         # no more jobs
#         break
#     elif n > 0:
#         # sleep exactly the right amount of time
#         time.sleep(n)
#     schedule.run_pending()


# 现在要运行所有的工作, 无论他们的安排如何
import schedule

def job_1():
    print('Foo')

def job_2():
    print('Bar')

schedule.every().monday.at("12:40").do(job_1)
schedule.every().tuesday.at("16:40").do(job_2)

schedule.run_all()

# Add the delay_seconds argument to run the jobs with a number
# of seconds delay in between.
schedule.run_all(delay_seconds=10)



