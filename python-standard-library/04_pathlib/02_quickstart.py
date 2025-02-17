#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/22 17:34
# @Author : limber
# @desc :

from passlib_test import pwd_context

# 加密一个密码
hash_ = pwd_context.hash("somepass")
print(hash_)

# 验证一个密码
result_1 = pwd_context.verify("somepass", hash_)
result_2 = pwd_context.verify("wrongpass", hash_)

print(result_1)
print(result_2)



