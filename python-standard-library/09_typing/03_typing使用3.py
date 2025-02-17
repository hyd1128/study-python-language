#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/11/10 16:47
# @Author : limber
# @desc :


# 特殊类型原语

# 特殊类型
# typing.Any
# 特殊类型，表示没有约束的类型。
# 所有类型都与 Any 兼容。
# Any 与所有类型都兼容。


# typing.NoReturn
# 标记没有返回值的函数的特殊类型。例如：
from typing import NoReturn, Union


def stop() -> NoReturn:
    raise RuntimeError('no way')


# typing.TypeAlias
# 用于显式声明 类型别名 的特殊标注。 例如:
from typing import TypeAlias
Factors: TypeAlias = list[int]


# 特殊形式
# typing.Tuple
# 元组类型； Tuple[X, Y] 是二项元组类型，第一个元素的类型是 X，第二个元素的类型是 Y。
# 空元组的类型可写为 Tuple[()]。

# typing.Union
# 联合类型； Union[X, Y] 等价于 X | Y ，意味着满足 X 或 Y 之一。
# 联合类型会被展平
Union[Union[int, str], float] == Union[int, str, float]




