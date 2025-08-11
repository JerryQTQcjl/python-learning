#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/11 01:06"


from sys import exception
import traceback


def inner():
    inner_result = yield 2
    print("inner", inner_result)
    yield 5
    yield 6
    print("inner end")
    return 3

def inner2(x):
    print("inner2 start")
    if x == 1:
        yield 11
    print("inner2 end")

def outer():
    yield 1
    val = yield from inner()
    print("outer", val)
    yield 4
    print("outer end")
    yield from inner2(2)


gen = outer()
print(next(gen))  # 输出: 1
# print(gen.throw(RuntimeError("error")))
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: inner None, 5
print(gen.send("abc"))  # 输出: 6
# print(next(gen))  # 输出: outer 3, 4
print(next(gen))  # 输出: inner end, outer 3, 4
try:
    print(next(gen))  # 输出: outer end, StopIteration
except StopIteration as e:
    print(traceback.format_exc())
