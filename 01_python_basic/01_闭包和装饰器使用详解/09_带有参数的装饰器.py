#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 添加输出日志的功能
def logging(flag):  # 装饰器传参
    def decorator(fn):  # 传递的函数对象
        def inner(num1, num2):  # 被装饰的函数的传参
            if flag == "+":
                print("--正在努力加法计算--")
            elif flag == "-":
                print("--正在努力减法计算--")
            result = fn(num1, num2)
            return result

        return inner

    # 返回装饰器
    return decorator


# 使用装饰器装饰函数
@logging("+")
def add(a, b):
    result = a + b
    return result


@logging("-")
def sub(a, b):
    result = a - b
    return result


result = add(1, 2)
print(result)

result = sub(1, 2)
print(result)
