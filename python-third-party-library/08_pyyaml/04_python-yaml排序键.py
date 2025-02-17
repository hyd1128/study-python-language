#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import yaml

with open('items.yaml') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    sorted = yaml.dump(data, sort_keys=True)
    print(sorted)






