#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ type动态创建class """
__date__ = "2024/10/4 14:31"

if __name__ == "__main__":
    Hello = type('Hello', (object,), dict(hello=lambda self: 'hello world'))
    h = Hello()
    print(f'type(Hello): {type(Hello)}')
    print(f'type(h): {type(h)}')
    print(f'h.hello(): {h.hello()}')
    pass
