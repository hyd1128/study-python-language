#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/22 17:34
# @Author : limber
# @desc :

from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.hash("toomanysecrets")
print(hash)

is_same = pbkdf2_sha256.verify("toomanysecrets", hash)
print(is_same)

is_same = pbkdf2_sha256.verify("joshua", hash)
print(is_same)

