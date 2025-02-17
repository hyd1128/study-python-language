# #!/usr/bin/env python
# # _*_ coding: utf-8 _*_
# # @Time : 2024/11/13 11:45
# # @Author : limber
# # @desc :
#
# from datetime import datetime, timedelta
# # format_time = datetime.strptime(datetime.now().strftime(time_style), time_style)
# # print(format_time)
#
# time_style = "%Y-%m-%d %H:%M:%S"  # 使用标准格式
#
# datetime_one = datetime.strptime("2024-11-14 00:00:00", time_style)
# datetime_two = datetime.strptime("2024-11-13 11:00:00", time_style)
#
# time_ = datetime_one - datetime_two
# print(abs(time_.total_seconds()))
#
#
# print([]== [])

list1 = [
    "home",
    "./app/prism/adv4_1/prismlogo.png",
    "swipe",
    "./app/prism/adv4_1/step1.png",
    "./app/prism/adv4_1/step2.png",
    "./app/prism/adv4_1/step3.png",
    "./app/prism/adv4_1/step4.png",
    "./app/prism/adv4_1/step5.png",
    "waiting",
    "adv",
    "home",
    "home",
    "kill"
]

n1 = 2
n2 = -3

list3 = list1[:2] + list1[-3:]
print(list3)
