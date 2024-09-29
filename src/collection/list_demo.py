#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 列表 """
__date__ = "2024/9/26 23:10"

if __name__ == "__main__":
    # 初始化
    l1 = list()
    l2 = [1, 2, 3, 4, 5]
    print(f'l1: {l1}, l2: {l2}')

    # 添加元素
    l1.append(1)
    l1.append(2)
    l1.append(6)
    l2.insert(4, 6)
    print(f'l1: {l1}')
    print(f'l2: {l2}')

    # 删除元素
    # 删除最后一个元素
    l2.pop()
    # 删除指定位置的元素
    l2.pop(2)
    print('l2: ', l2)
    # 删除指定元素
    l2.remove(4)
    print('l2: %s' % l2)

    # 获取元素, 第一个元素，第二元素，最后一个元素, 倒数第二个元素
    print(f'l1[0]: {l1[0]}, l1[1]: {l1[1]}, l1[-1]: {l1[-1]}, l1[-2]: {l1[-2]}')
    print(f'l1 == l2: {l1 == l2}')

    # 更新
    l1[0] = 100
    print(f'l1: {l1}')

    print(len(l1))

    # 并集
    l3 = l1 + l2
    print(f'l1+l2: {l3}')

    # 生成式列表
    gl1 = [x * x for x in range(1, 11)]
    # for 之后的是过滤条件，不能带上 else
    gl2 = [x * x for x in range(1, 11) if x % 2 == 0]
    gl3 = [x * y for x in range(1, 10) for y in range(10, 20)]
    # for 之前的是表达式，必须有值
    gl4 = [x if x % 2 == 0 else -x for x in range(10)]

    print(f"""[x * x for x in range(1, 11)]: {gl1}
[x * x for x in range(1, 11) if x % 2 == 0]: {gl2}
[x * y for x in range(1, 10) for y in range(10, 20)]: {gl3}
[x if x % 2 == 0 else -x for x in range(10)]: {gl4}
""")
