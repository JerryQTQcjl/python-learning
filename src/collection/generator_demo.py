#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 生成器 """
__date__ = "2024/9/27 00:04"

from collections.abc import Iterable, Iterator
from threading import Thread
from time import sleep


# 生成器
def gen():
    count = 0
    while True:
        count += 1
        print(f'gen: {count}')
        yield count

if __name__ == "__main__":
    # 把生成式列表的[]改为()，就创建了一个generator
    # 生成器的优势是不会一次全部计算出来，而是在需要的时候才计算（懒加载的思想，节省cpu和内存资源）
    g1 = (x for x in range(10))
    print(f'g1: {g1}, type(g1): {type(g1)}')

    print(f'next(g1): {next(g1)}')
    print(f'next(g1): {next(g1)}')
    # 可以看到是从第3个元素开始遍历的
    for i in g1:
        print(f'traverse g1: {i}')

    # 对于复杂的生成器，我们可以定义一个函数，然后用 yield 来返回值
    g2 = gen()
    print(f'next(g2): {next(g2)}')
    print(f'next(g2): {next(g2)}')
    # 生成器函数中的代码只有遇到next()的时候才会执行，遇到yield就会返回值，然后暂停执行
    # 这里的暂定不是阻塞线程，可以理解为是定义了一串字符串，遇到next()时才会执行一次，然后遇到yield就结束
    for i in range(20):
        print(f'traverse g2: {next(g2)}')

    print(f'isinstance(g1, Iterable): {isinstance(g1, Iterable)}, isinstance(g2, Iterator): {isinstance(g2, Iterator)}')
    sleep(10)
