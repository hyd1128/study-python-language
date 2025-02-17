#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import yaml

with open('data.yaml') as f:
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:
        for k, v in doc.items():
            print(k, "->", v)
