#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 闭包的使用
# 外部函数
def config_name(name):
    # 内部函数
    def say_info(info):
        print(name + ": " + info)

    return say_info


tom = config_name("Tom")
tom("你好!")
tom("你好, 在吗?")

jerry = config_name("jerry")
jerry("不在, 不和你玩!")
