#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 元组 """
__date__ = "2024/9/27 00:03"

if __name__ == "__main__":
    # 初始化
    t1 = tuple(range(5))
    t2 = (1, 2, 3, 4, 5)
    print(f't1: {t1}, t2: {t2}')

    # 获取元素, 第一个元素，第二元素，最后一个元素, 倒数第二个元素
    print(f't2[0]: {t2[0]}, t2[1]: {t2[1]}, t2[-1]: {t2[-1]}, t2[-2]: {t2[-2]}')

    # 不支持变更
    try:
        t1[0] = -1
        print(f't1: {t1}')
    except Exception as e:
        print(f'error: {e}')
        # pass


