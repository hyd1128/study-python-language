#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/15 14:11
# @Author : limber
# @desc :

from enum import Enum


# class Weekday(str, Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Web = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6


class Gender(str, Enum):
    Male = "male"
    Female = "female"

if __name__ == '__main__':
    # day1 = Weekday.Mon
    # print(day1)
    # print(day1.value)

    print(Gender.Male)
    print(type(Gender.Male))
    print(Gender.Male == "male")