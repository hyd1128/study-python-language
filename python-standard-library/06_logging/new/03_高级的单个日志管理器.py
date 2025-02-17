#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import logging
import sys


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='app.log',
        filemode='w',
        encoding='utf-8',
        errors='ignore'
    )


def handle_exception(exc_type, exc_value, exc_traceback):
    """
    全局异常处理函数，用于捕获并处理所有未被捕获的异常。

    Args:
        exc_type: 异常的类型，例如 ZeroDivisionError
        exc_value: 异常实例，包含异常消息等信息。
        exc_traceback: 一个 traceback 对象，包含异常发生时的调用堆栈信息。

    Returns:

    """
    # 使用 logging 记录异常信息
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def my_function():
    # 潜在的异常操作
    result = 10 / 0
    return result


if __name__ == '__main__':
    setup_logging()
    sys.excepthook = handle_exception
    # 运行示例函数
    my_function()


"""
    进一步的，应用程序在运行时候，特别是在复杂的应用程序中，可能无法预见所有可能的错误场景。这个时候，最好的做法是让程序能够优雅地终止或继续运行。
"""
