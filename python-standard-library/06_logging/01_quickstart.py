#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/17 10:55
# @Author : limber
# @desc :

import logging

logging.warning("watch out")


"""
python logging 四大模块:
1、记录器
2、处理器
3、过滤器
4、格式化器
"""

logger_name1 = "a"
logger_name2 = "a.b"
logger_name3 = "a.b.c"

# 根记录器
logger_root = logging.getLogger("root")
# 一级记录器
logger_1 = logging.getLogger(logger_name1)
# 二级记录器
logger_2 = logging.getLogger(logger_name2)
# 三级记录器
logger_3 = logging.getLogger(logger_name3)




