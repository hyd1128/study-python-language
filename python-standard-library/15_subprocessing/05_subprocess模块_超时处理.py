#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import subprocess

try:
    result = subprocess.run("ping -n 3 www.baidu.com", timeout=5, stdout=subprocess.PIPE, text=True, shell=True,
                            universal_newlines=True)
    print(result.stdout)
    print(result.returncode)
except subprocess.TimeoutExpired:
    print("命令执行超时。")
