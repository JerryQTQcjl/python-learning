#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/9/27 00:05"

if __name__ == "__main__":
    # 初始化
    d1 = dict()
    d2 = {'a': 1, 'b': 2, 'c': 3}
    print(f'd1: {d1}, d2: {d2}')

    # 添加元素
    d1['a'] = 1
    print(f'd1: {d1}')

    # 删除元素
    d1.pop('a')

    # 查找元素
    print(f'd2["a"]: {d2["a"]}')
    try:
        # 不存在的元素会报错
        print(d1['a'])
    except Exception as e:
        print(f'error: {e}')
    # 需要通过get方法获取，避免报错
    print(d1.get('a'))
    print(d1.get('a', 123))

