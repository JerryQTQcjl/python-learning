#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/9/28 23:05"


# 啥也不做
def none_func():
    pass


# 定义无默认值参数
def func_with_param(param, param2):
    print(f'exec func_with_param({param}, {param2})')


# 定义带默认值参数
def func_with_default_param(param, param2=10, param3=20):
    print(f'exec func_with_default_param({param}, {param2}, {param3})')


# 定义默认值是可变变量的参数
def func_with_list_default_param(param=[]):
    param.append(1)
    print(f'exec func_with_list_default_param({param})')
    return param


# 定义可变参数
def func_with_variable_param(*param):
    print(f'exec func_with_variable_param({param}), type(param): {type(param)}')


# 定义关键字参数
def func_with_keyword_param(**param):
    print(f'exec func_with_keyword_param({param}), type(param): {type(param)}')


# 定义固定名称的关键字参数，中间的*用于指明后面参数是关键字参数
def func_with_fix_keyword_param(param1, *, param2, param3):
    print(f'exec func_with_keyword_param2({param1}, {param2}, {param3})')


# 定义带可变参数和固定名称的关键字参数，带可变参数可省略*
def func_with_variable_param_and_fix_keyword_param(param1, *param2, param3=10, param4):
    print(f'exec func_with_variable_param_and_fix_keyword_param({param1}, {param2}, {param3}, {param4})')


# 定义带可变参数和关键字参数
def func_with_variable_param_and_keyword_param(param1, *param2, param3, **param4):
    print(f'exec func_with_variable_param_and_keyword_param({param1}, {param2}, {param3}, {param4})')


# 显式指明参数类型和返回值类型（不强制限制，但可以明显知道参数类型，便于增加可读性）
def func_with_obvious_type(param1: int, param2: str, *param3: str, param4: list, **param5: str) -> int:
    print(f'exec func_with_obvious_type({param1}, {param2}, {param3}, {param4}, {param5})')
    return 1


# 多返回值
def func_with_multi_return() -> tuple[int, str, list[str]]:
    return 1, '1', ['1', '2']


if __name__ == "__main__":
    # 啥也不做
    none_func()
    # 定义无默认值参数
    func_with_param(1, 2)
    func_with_param(param2=5, param=1)
    # 定义带默认值参数
    func_with_default_param(1, param3=30)
    func_with_default_param(1)
    # 定义默认值是可变变量的参数(默认只是可变类型，数据会一直存在，不建议使用可变类型作为默认值)
    func_with_list_default_param()
    func_with_list_default_param()
    func_with_list_default_param()
    # 定义可变参数（实际上是tuple类型）
    func_with_variable_param(1, 2, 3)
    func_with_variable_param(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    # 定义关键字参数
    func_with_keyword_param(param1=1, param2=2, param3=3)
    # 定义固定名称的关键字参数
    func_with_fix_keyword_param(1, param2=2, param3=3)
    # 定义带可变参数和固定名称的关键字参数
    func_with_variable_param_and_fix_keyword_param(1, 2, 3, 4, 5, param4=7)
    # 定义带可变参数和关键字参数
    func_with_variable_param_and_keyword_param(1, 2, 3, 4, 5, param3=7, param4=8, param5=9, param6=10)
    # 显式指明参数类型和返回值类型
    print(func_with_obvious_type(1, '2', '1', '2', '3', param4=[1, 2, 3], param5='', param6='a'))
    # 多返回值
    print(func_with_multi_return())
