 #!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/1/14 11:36
# @Author : limber
# @desc :


# def now():
#     print('2024-6-1')


# print(now.__name__)
# f = now
# print(f.__name__)

"""
不带参数装饰器定义方式:
    - 内层的wrapper可以任意定义 只需要返回时的函数名称是一样的就行
"""
import functools


def log(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        print(f'call {func.__name__}')
        return func(*args, **kwargs)

    return wrapper


@log
def now(a, b, c=1):
    print(a)
    print(b)
    print(c)
    print('2024-6-1')


def now1():
    print('2024-7-1')


"""
允许传参的装饰器
    - 
"""


def log_plus(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{text}--{func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_plus("我是允许传参的装饰器")
def now2(a, b, c=1):
    print(a)
    print(b)
    print(c)
    print('2024-8-1')


if __name__ == '__main__':
    now(1, 2, c=3)
    print(now.__name__)
    # now1 = log(now1)
    # now1()

    now2(10, 20, c=30)
    print(now2.__name__)
