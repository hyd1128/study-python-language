#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import yaml

# 转存文档
users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]
# print(yaml.dump(users))

# 写入文档
with open('users.yaml', 'w') as f:

    data = yaml.dump(users, f)




