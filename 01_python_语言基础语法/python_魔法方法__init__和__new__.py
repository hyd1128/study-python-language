#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/1/14 16:43
# @Author : limber
# @desc :

class Solution(object):
    def __init__(self, name=None, data=None):
        self.name = name
        self.data = data
        # 初始化加载数据
        self.xml_load(self.data)

    def xml_load(self, data):
        print("初始化init", data)

    def Parser(self):
        print("解析完成finish", self.name)


a = Solution(name="A111", data=10)
a.Parser()
b = Solution(name="A112", data=20)
b.Parser()
# print(a)与 print(b)返回了类的名称和对象的地址
print(a)
print(b)
# 可以使用内置函数id()查看python对象的内存地址
print(id(a))
print(id(b))
