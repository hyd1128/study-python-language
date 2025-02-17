#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/12 14:20
# @Author : limber
# @desc :

from datetime import datetime


def compare_times(start_time: str, end_time: str) -> bool:
    """
    传入两个24小时制，格式HH:MM:SS的时间，并判断当前时间是否位于传入时间的区间内

    :param start_time:
    :param end_time:
    :return:
    """
    time_format = "%H:%M:%S"
    start_time = datetime.strptime(start_time, time_format)
    end_time = datetime.strptime(end_time, time_format)
    # now_time = datetime.strptime(datetime.now().strftime(time_format), time_format)
    now_time = datetime.strptime("20:00:00", time_format)

    condition_one = now_time >= start_time
    condition_two = now_time <= end_time
    return condition_one and condition_two


if __name__ == '__main__':
    start_time = "10:00:00"
    end_time = "20:00:00"
    result = compare_times(start_time, end_time)
    print(result)
