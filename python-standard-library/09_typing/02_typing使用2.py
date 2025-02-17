#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/11/10 16:04
# @Author : limber
# @desc :


#  NewType
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)


def get_user_name(user_id: UserId) -> str:
    ...


# 静态类型检查器把新类型当作原始类型的子类，这种方式适用于捕捉逻辑错误
# passes type checking
user_a = get_user_name(UserId(42351))

# fails type checking; an int is not a UserId
# user_b = get_user_name(-1)


# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)
print(output)

from typing import NewType

UserId = NewType('UserId', int)

# 通过Newtype创建的类型是不能被类继承的 如果想要派生NewType的新类型 可以通过下面的这种方式
from typing import NewType

UserId = NewType('UserId', int)

ProUserId = NewType('ProUserId', UserId)

# 可调用对象 Callable
# Callable[[Arg1Type, Arg2Type], ReturnType]
from collections.abc import Callable


def feeder(get_next_item: Callable[[], str]) -> None:
    # Body
    ...


def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    # Body
    ...


# async def on_update(value: str) -> None:
#     # Body
# callback: Callable[[str], Awaitable[None]] = on_update


# 定义泛型
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')  # 声明一个泛型变量


def first(l: Sequence[T]) -> T:  # 泛型函数
    return l[0]

# 一个泛型可以有任何数量的类型变量。所有种类的 TypeVar 都可以作为泛型的参数
from typing import TypeVar, Generic, Sequence

T = TypeVar('T', contravariant=True)
B = TypeVar('B', bound=Sequence[bytes], covariant=True)
S = TypeVar('S', int, str)

class WeirdTrio(Generic[T, B, S]):
    ...

# Generic 类型变量的参数应各不相同。下列代码就是无效的
from typing import TypeVar, Generic
T = TypeVar('T')
# class Pair(Generic[T, T]):   # INVALID
#     ...


# 定义一个泛型函数
T = TypeVar("T")
# 通过下面的例子可以看出 如果要定义一个泛型函数 只需要定义一个泛型变量 就可以直接使用这个泛型变量
# 如果要定义一个泛型类 就需要使用Genertic类
def func(a: T) -> T:
    return type(a)

print(func(1))
print(func("a"))
print(func(True))


# Any类型
# Any 是一种特殊的类型。静态类型检查器认为所有类型均与 Any 兼容，同样，Any 也与所有类型兼容。
# 也就是说，可对 Any 类型的值执行任何操作或方法调用，并赋值给任意变量
from typing import Any

a: Any = None
a = []          # OK
a = 2           # OK

s: str = ''
s = a           # OK

def foo(item: Any) -> int:
    # Passes type checking; 'item' could be any type,
    # and that type might have a 'bar' method
    item.bar()
    ...
