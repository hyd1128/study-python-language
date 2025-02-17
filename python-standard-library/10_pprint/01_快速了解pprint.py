#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/9 14:11
# @Author : limber
# @desc :

from pprint import pprint

data = [
    {
        "name": "John",
        "age": 45,
        "children": [
            "Alice",
            "Bob"
        ]
    },
    {
        "name": "Mike",
        "age": 30,
        "children": [
            "Thomas",
            "Ann"
        ]
    }
]

print(data)
pprint(data)
pprint(data, width=30, indent=2)
