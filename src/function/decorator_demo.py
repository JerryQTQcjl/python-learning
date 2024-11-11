#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 装饰器，装饰器模式，类似于java切面的思想 """
__date__ = "2024/9/29 11:48"

import functools

def log(*arg):
    print(f'log: {arg}')

    def log_wrapper(func):
        print(f'log2: {arg}')

        @functools.wraps(func)
        def wrapper(*args, **kws):
            print(f'{func.__name__} start params: {args}, {kws}')
            result = func(*args, **kws)
            print(f'{func.__name__} end result: {result}')
            print(f'log3: {arg}')
            return result

        return wrapper

    return log_wrapper

# def log(func):
#     # 加上这个注解，wrapper.__name__ = func.__name__
#     @functools.wraps(func)
#     def wrapper(*args, **kws):
#         print(f'{func.__name__} start params: {args}, {kws}')
#         result = func(*args, **kws)
#         print(f'{func.__name__} end result: {result}')
#     return wrapper

class ClassForFuncDecorator:

    def __init__(self, func):
        self.func = func

    # @functools.wraps() 原生的无法支持，需要参考源码自定义
    def __call__(self, *args, **kwargs):
        print(f'ClassForFuncDecorator call {args} {kwargs}', args, kwargs)
        return self.func(*args, **kwargs)

# @log
@log('log1221')
# @ClassForFuncDecorator
def helloworld(name: str) -> str:
    print(f'hello {name}')
    return f'hello {name}'

if __name__ == '__main__':
    print(f"helloworld('world'): {helloworld('world')}")

    h2 = helloworld
    h2('kitty')

    print(f'helloworld.__name__: {helloworld.__name__}')
