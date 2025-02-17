#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/22 17:04
# @Author : limber
# @desc :

from jose import jws
import base64

# 生成token
# signed = jws.sign({'a': 'b'}, 'secret', algorithm='HS256')
# print(signed)

"""
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhIjoiYiJ9.jiMyrsmD8AoHWeQgmxZ5yq8z0lXS67_QGs52AzC8Ru8
"""

token_ = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhIjoiYiJ9.jiMyrsmD8AoHWeQgmxZ5yq8z0lXS67_QGs52AzC8Ru8"

# 使用base64解码token的header和pyload
# token_header = base64.b64decode("eyJhIjoiYiJ9").decode('utf-8')
# print(token_header)

# 验证token
data = jws.verify(token_, 'secret', algorithms=['HS256'])
print(data)