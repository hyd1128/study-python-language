#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import yaml

with open('items.yaml') as f:
    data = yaml.scan(f, Loader=yaml.FullLoader)

    for token in data:
        print(token)
