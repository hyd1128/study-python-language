#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/12 11:26
# @Author : limber
# @desc :
import datetime as datetime_
from datetime import datetime, timedelta, time
# 常量
print(datetime_.MINYEAR)
print(datetime_.MAXYEAR)


# from datetime import timedelta, datetime, time
# duration_time = timedelta(hours=10, minutes=20, seconds=20)
# now = datetime.strptime("11:36:20", "%H:%M:%S")
# time_ = now + duration_time
# print(time_)
# print(type(time_))
#
# time1 = time(hour=10, minute=0, second=0)
# print(time1)
#
# time2 = time1 + duration_time
# print(time2)
# print(type(time2))

start_time = "08:00:00"
time_format = "%H:%M:%S"
duration_time = "10:00:00"
# 1、将获得的任务开始执行时间转化为datetime对象
start_dt = datetime.strptime(start_time, time_format)
duration_time_dt = datetime.strptime(duration_time, time_format)
duration_timedelta = timedelta(hours=duration_time_dt.hour, minutes=duration_time_dt.minute, seconds=duration_time_dt.second)
end_time = start_dt + duration_timedelta
standard_end_time = end_time.time().isoformat("seconds")
print(type(standard_end_time))

time1 = datetime.strptime(datetime.now().strftime(time_format), time_format)
time2 = datetime.strptime(standard_end_time, time_format)
print(time1)
print(time2)
print(time1 < time2)







