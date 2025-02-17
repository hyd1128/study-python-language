#!/usr/bin/env python
# _*_ coding: utf-8 _*_


from typing import Union


def process_input(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(f"接收数字：{value}")
    else:
        print(f"接收字符串：{value}")
