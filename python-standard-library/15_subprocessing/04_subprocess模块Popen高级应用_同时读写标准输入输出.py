#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import subprocess

# 创建命令进程
process = subprocess.Popen(["python", "-u"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True)

# 写入数据到标准输入
process.stdin.write("print('Hello from child process')\n")
process.stdin.flush()

# 读取并打印标准输出
output, errors = process.communicate()
print("标准输出:")
print(output)

# 打印标准错误
print("标准错误:")
print(errors)