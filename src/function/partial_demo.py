#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 偏函数 """
__date__ = "2024/9/30 17:52"

import functools as f

if __name__ == "__main__":
    def pow2(x):
        return x * x

    # 偏函数，固定函数的某些参数，返回一个新的函数
    pow3 = f.partial(pow2, 3)
    print(f'pow3(): {pow3()}')

    def helloworld(name: str) -> str:
        print(f'hello {name}')
        return f'hello {name}'

    h2 = f.partial(helloworld, 'jerry')
    print(f'h2(): {h2()}')

    def xxx(x, y, z):
        print(f'x: {x}, y: {y}, z: {z}')
        return x + y + z
    x = f.partial(xxx, 1)
    print(f'x(2, 3): {x(y=3, z=4)}')

    try:
        x(1, 2, 3)
    except Exception as e:
        e.with_traceback()
