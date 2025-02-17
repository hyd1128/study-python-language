#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/9 15:18
# @Author : limber
# @desc :

from datetime import datetime

# 定义两个时间
time_format = "%H:%M:%S"
time1 = datetime.strptime("12:30:00", time_format)
time2 = datetime.strptime("14:45:30", time_format)

# 计算间隔的描述
interval = (time2 - time1).total_seconds()
print(interval)

