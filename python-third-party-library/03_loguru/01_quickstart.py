#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/17 10:15
# @Author : limber
# @desc :

"""
desc loguru:
    Loguru 是一个用于 Python 中的日志记录库，它以简洁、易用和功能丰富而著称。
    相较于 Python 标准库中的 logging 模块，Loguru 提供了更为简单直观的接口，
    并且在常见的日志记录需求上做了许多优化，使得开发者可以更轻松地处理日志。

"""
import sys

from loguru import logger

# 没有 Handler，没有 Formatter，没有 Filter：一个函数来统治它们
# logger.debug("That's it, beautiful and simple logging!")


# 通过旋转/保留/压缩更轻松地记录文件
# logger.add("file_{time}.log")
# logger.add("file_1.log", rotation="500 MB")    # 自动旋转太大的文件
# logger.add("file_2.log", rotation="12:00")     # 每天中午创建新文件
# logger.add("file_3.log", rotation="1 week")    # 文件太旧后，将对其进行轮换
# logger.add("file_X.log", retention="10 days")  # 一段时间后的清理
# logger.add("file_Y.log", compression="zip")    # 节省一些心爱的空间


# 使用大括号样式的现代字符串格式
# feature = "f-strings"
# num1 = 3.6
# logger.info(f"If you're using Python {num1}, prefer {feature} of course!")


# 在 threads 或 main 中捕获异常
# @logger.catch
# def my_function(x, y, z):
#     # An error? It's caught anyway!
#     return 1 / (x + y + z)
#
# my_function(0, 0, 0)


# 带有漂亮颜色的日志记录
# logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
# logger.debug("jianghcnehngyaunchengyua")

# 异步、线程安全、多进程安全
# logger.add("somefile.log", enqueue=True)

# 完全描述性的异常
# 注意，“diagnose=True” 是默认值，可能会泄露 prod 中的敏感数据
logger.add("out.log", backtrace=True, diagnose=True)

# def func(a, b):
#     return a / b
#
# def nested(c):
#     try:
#         func(5, c)
#     except ZeroDivisionError:
#         logger.exception("What?!")
#
# nested(0)


# 根据需要惊醒结构化日志记录
# logger.add(custom_sink_function, serialize=True)
# logger.add("file.log", format="{extra[ip]} {extra[user]} {message}")
# context_logger = logger.bind(ip="192.168.0.1", user="someone")
# context_logger.info("Contextualize your logger easily")
# context_logger.bind(user="someone_else").info("Inline binding of extra attribute")
# context_logger.info("Use kwargs to add context during formatting: {user}", user="anybody")


# 昂贵函数的惰性评估
# logger.opt(lazy=True).debug("If sink level <= DEBUG: {x}", x=lambda: expensive_function(2**64))

# By the way, "opt()" serves many usages
# logger.opt(exception=True).info("Error stacktrace added to the log message (tuple accepted too)")
# logger.opt(colors=True).info("Per message <blue>colors</blue>")
# logger.opt(record=True).info("Display values from the record (eg. {record[thread]})")
# logger.opt(raw=True).info("Bypass sink formatting\n")
# logger.opt(depth=1).info("Use parent stack context (useful within wrapped functions)")
# logger.opt(capture=False).info("Keyword arguments not added to {dest} dict", dest="extra")


# 可自定义的级别
# new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")
# logger.log("SNAKY", "Here we go!")


# 更好的日期时间处理
# logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
# logger.debug("jianghcnejgiancheng1")


# 适用于脚本
# For scripts
# config = {
#     "handlers": [
#         {"sink": sys.stdout, "format": "{time} - {message}"},
#         {"sink": "file.log", "serialize": True},
#     ],
#     "extra": {"user": "someone"}
# }
# logger.configure(**config)
#
# # For libraries, should be your library's `__name__`
# logger.disable("my_library")
# logger.info("No matter added sinks, this message is not displayed")
#
# # In your application, enable the logger in the library
# logger.enable("my_library")
# logger.info("This message however is propagated to the sinks")









