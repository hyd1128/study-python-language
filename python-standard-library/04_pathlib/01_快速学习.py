#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/15 9:30
# @Author : limber
# @desc :


from pathlib import Path

p = Path('.')
result = [x for x in p.iterdir() if x.is_dir()]
print(result)

result2 = list(p.glob('**/*.py'))
print(result2)