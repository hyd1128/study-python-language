#!/usr/bin/env python
# _*_ coding: utf-8 _*_

class Check(object):
    def __init__(self, fn):
        # 初始化操作在此完成
        self.__fn = fn

    # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用。
    def __call__(self, *args, **kwargs):
        # 添加装饰功能
        print("请先登陆...")
        self.__fn()


@Check
def comment():
    print("发表评论")


comment()

"""
想要让类的实例对象能够像函数一样进行调用，需要在类里面使用call方法，把类的实例变成可调用对象(callable)
类装饰器装饰函数功能在call方法里面进行添加
"""
