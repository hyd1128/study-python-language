#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/12 14:09
# @Author : limber
# @desc :
from datetime import datetime, timedelta

def generate_end_execution_time(task_today_start_execution_time: str, task_duration_execution_time: str) -> str:
    """
    根据今日任务开始执行时间和任务持续时间生成今日任务结束时间

    注: 今日任务开始时间+任务持续时间<=24:00:00
    :param task_today_start_execution_time:
    :param task_duration_execution_time:
    :return:
    """
    time_format = "%H:%M:%S"
    start_dt_obj = datetime.strptime(task_today_start_execution_time, time_format)
    duration_dt_obj = datetime.strptime(task_duration_execution_time, time_format)
    duration_td_obj = timedelta(hours=duration_dt_obj.hour, minutes=duration_dt_obj.minute,
                                seconds=duration_dt_obj.second)
    end_dt_obj = start_dt_obj + duration_td_obj
    standard_end_time = end_dt_obj.time().isoformat("seconds")
    return standard_end_time


if __name__ == '__main__':
    start_time = "10:00:00"
    duration_time = "9:00:00"
    result = generate_end_execution_time(start_time, duration_time)
    print(result)
