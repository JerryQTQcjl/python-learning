#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 迭代器
1. 可迭代对象：实现了 __iter__ 方法的对象
2. 迭代器：实现了 __iter__ 和 __next__ 方法的对象
3. 迭代器是可迭代对象的一种，迭代器是一种特殊的对象，它可以记住遍历的位置
"""
__date__ = "2024/9/27 00:04"

from collections.abc import Iterable, Iterator


class MyIterable:

    def __iter__(self):
        return self


class MyIterator:
    def __iter__(self):
        return self

    def __next__(self):
        pass


"""
判断是否可迭代
"""


def iterable_judge():
    print('=================iterable_judge=================')
    # 判断是否可迭代
    l1 = [1, 2, 3]
    print(f'l1: {l1}, isinstance(l1, Iterable): {isinstance(l1, Iterable)}')

    t1 = (1, 2, 3)
    print(f't1: {t1}, isinstance(t1, Iterable): {isinstance(t1, Iterable)}')

    s1 = '123'
    print(f's1: {s1}, isinstance(s1, Iterable): {isinstance(s1, Iterable)}')

    d1 = {'a': 1, 'b': 2, 'c': 3}
    print(f'd1: {d1}, isinstance(d1, Iterable): {isinstance(d1, Iterable)}')

    r1 = range(10)
    print(f'r1: {r1}, isinstance(r1, Iterable): {isinstance(r1, Iterable)}')

    e1 = enumerate(l1)
    print(
        f'e1: {e1}, isinstance(e1, Iterable): {isinstance(e1, Iterable)}, isinstance(e1, tuple): {isinstance(e1, tuple)})')
    for e in e1:
        print(f'e: {e} in e1')
    e1 = enumerate(l1)
    for i, e in e1:
        print(f'i:{i}, e: {e} in e1')

    # 定义了 __iter__ 的对象，就是可迭代的
    i1 = MyIterable()
    print(f'i1: {i1}, isinstance(i1, Iterable): {isinstance(i1, Iterable)}')


def judge_iterator():
    print("=================judge_iterator=================")
    l1 = [1, 2, 3]
    print(f'l1: {l1}, isinstance(l1, Iterator): {isinstance(l1, Iterator)}, '
          f'iter(l1): {iter(l1)}, isinstance(iter(l1), Iterator): {isinstance(iter(l1), Iterator)}')

    d1 = {'a': 1, 'b': 2, 'c': 3}
    print(f'd1: {d1}, isinstance(d1, Iterator): {isinstance(d1, Iterator)},'
          f' iter(d1): {iter(d1)}, isinstance(iter(d1), Iterator): {isinstance(iter(d1), Iterator)}')

    # 定义了 __iter__ 和 __next__ 的对象，就是迭代器
    i1 = MyIterator()
    print(f'i1: {i1}, isinstance(i1, Iterator): {isinstance(i1, Iterator)}')

    r1 = range(10)
    print(f'r1: {r1}, isinstance(r1, Iterator): {isinstance(r1, Iterator)}')

    # 生成器
    g1 = (i for i in r1 if i % 2 == 0)
    print(f'g1: {g1}, isinstance(g1, Iterator): {isinstance(g1, Iterator)}')


if __name__ == "__main__":
    iterable_judge()
    judge_iterator()
