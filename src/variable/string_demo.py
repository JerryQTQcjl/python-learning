#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符串相关使用

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/9/26 23:06"

# 字符串
str1 = "hello python"

# 字符串长度
print(len(str1))

# 字符串拼接
str2 = "hello"
str3 = "python"
print(str2 + str3)

# 字符串格式化
print("hello %s" % str3)

# 字符串格式化
print("hello {} {}".format(str2, str3))

# 字符串格式化
print(f"hello {str2} {str3}")

# 字符串格式化
print("hello {0} {1}".format(str2, str3))

# 字符串格式化
print("hello {1} {0}".format(str2, str3))
