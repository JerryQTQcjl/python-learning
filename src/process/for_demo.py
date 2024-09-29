#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/9/25 21:57"

from typing import Generator, Iterator, Iterable

if __name__ == "__main__":
    # for循环
    # python 没有 for int i =0; i < 10; i++ {} 这样的语法
    print('for循环')
    for i in range(10):
        print(i)

    # while循环
    print('while循环')
    i = 0
    while i < 10:
        print(i)
        i = i+1

    # 遍历列表
    print('遍历列表')
    l1 = [1, 2, 3, 4, 5]
    for i in l1:
        print(i)

    d1 = {'a': 1, 'b': 2, 'c': 3}
    for k, v in d1.items():
        print(k, v)
