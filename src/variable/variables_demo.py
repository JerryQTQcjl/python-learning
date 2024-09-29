#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jerry chan'

CONSTANTS_NUM = 123444

if __name__ == '__main__':
    print(CONSTANTS_NUM)
    # 数字
    var = 1
    print(var)
    # 浮点数
    var = 1.23
    print(var)
    # 字符串
    var = "123"
    print(var)
    # 多行字符串
    var = """hello python"""
    print(var)
    # 布尔
    var = True
    print(var)
    # 空
    var = None
    print(var)
    # 赋值地址
    var1 = var
    print(id(var1))
    print(id(var))
    # 重置赋值，引用指向新地址
    var = 213123
    print(var1, var)
    print(id(var))
