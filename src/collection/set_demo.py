#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ set 集合 """
__date__ = "2024/9/27 00:05"

if __name__ == "__main__":
    # 初始化
    s1 = set(range(5))
    s2 = {1, 2, 3, 4, 5}
    print(f's1: {s1}, s2: {s2}')

    # 不支持索引
    try:
        print(f's1[0]: {s1[0]}')
    except Exception as e:
        print(f'error: {e}')
        # pass

    # 添加元素
    s1.add(6)
    s1.add(7)
    s1.add(5)
    print(f's1: {s1}')

    # 删除元素
    s1.remove(6)
    print(f's1: {s1}')

    # 运算
    # 并集
    print(f's1 | s2: {s1 | s2}')
    # 交集
    print(f's1 & s2: {s1 & s2}')
    # 差集
    print(f's1 - s2: {s1 - s2}')
    # 差集
    print(f's2 - s1: {s2 - s1}')
