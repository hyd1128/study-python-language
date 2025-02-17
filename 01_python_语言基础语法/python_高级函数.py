#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/1/14 11:55
# @Author : limber
# @desc :

# map
list1 = [1, 2, 4, 5, 6]


def func1(i: int):
    return i ** 2


list2 = map(func1, list1)
for i in list2:
    print(i)
