#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import subprocess

result = subprocess.run(['adb', 'devices'])
print(type(result))
print(result)

"""
class subprocess.CompletedProcess
run() 的返回值, 代表一个进程已经结束.
"""

