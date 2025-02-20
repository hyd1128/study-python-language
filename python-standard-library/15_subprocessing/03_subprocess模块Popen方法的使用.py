#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import subprocess

# # 执行命令
# process = subprocess.Popen(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
# # 读取标准输出和错误
# out, err = process.communicate()
#
# print("标准输出:")
# print(out)
#
# print("标准错误:")
# print(err)

import subprocess
import time

# 方法1: 流式读取
# p = subprocess.Popen(["ping", "www.baidu.com"], stdout=subprocess.PIPE, text=True)
#
# # 逐行读取并实时输出
# for line in p.stdout:
#     print(line.strip())  # 处理并打印每一行

# 方式2: 手动readline() 逐行读取
# p = subprocess.Popen(["ping", "www.baidu.com"], stdout=subprocess.PIPE, text=True)
#
# while True:
#     line = p.stdout.readline()  # 读取一行
#     if not line:
#         break
#     print(line.strip())  # 处理并打印

# 方式3: 一次性读取
import subprocess

p = subprocess.Popen(["ping", "-n", "4", "www.baidu.com"], stdout=subprocess.PIPE, text=True)
output, _ = p.communicate()  # 一次性获取全部输出
print(output)
