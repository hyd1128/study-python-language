#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/6 13:52
# @Author : limber
# @desc :


# map()函数
# def func1(n):
#     return n*n
#
# list1 = [1, 2, 3, 4, 5]
#
# print(list(map(func1, list1)))


class IterClass:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


if __name__ == '__main__':
    # iter1 = IterClass()
    # myiter = iter(iter1)
    # for x in myiter:
    #     print(x)

    # for i in iter1:
    #     print(i)

    # zip
    # map()

    # print(type(range(10)))
    # a = sum(i * i for i in range(10))
    # print(a)
    # b = [i * i for i in range(10)]
    # print(b)
    # sum
    # pass
    # def reverse(data):
    #     for index in range(len(data) - 1, -1, -1):
    #         yield data[index]
    # # 返回一个生成器
    # a = reverse([1, 2, 3])
    #
    # # 遍历一个生成器
    # for i in a:
    #     print(i)

    a = (i * i for i in range(10))
    # print(type(a))
    # print(sum(a))

    # for i in a:
        # print(i)

    b = (i for i in range(1000))
    print(b)
    print(type(b))