#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/9/29 00:06"

import math
from functools import reduce

"""
// java lambda 表达式不支持传入可变参数，所以不会闭包问题
public static void main(String[] args) {
    List<Supplier<Integer>> list = new ArrayList<>();
    for (int i = 1; i < 4; i++) {
        int finalI = i;
        list.add(() -> finalI * finalI);
    }
    list.stream().map(Supplier::get).forEach(System.out::println);
}
"""

def func_with_closure():
    l = list()
    for i in range(1, 4):
        # i 为可变变量，存在闭包问题
        l.append(lambda: i * i)
    return l

def func_solve_closure():
    l = list()
    # def inner_func(i):
    #     return lambda: i * i
    inner_func = lambda x: lambda: f'x*x = {x * x}, id(x) = {id(x)}'
    for i in range(1, 4):
        # 立即执行inner_func，i当前值传入inner_func，因此可以解决闭包问题，类似于java中把变量赋值给一个最终类型
        print(f'id(i) = {id(i)}')
        l.append(inner_func(i))
        # 这种方案不可行，因为执行时获取的仍然是x最后的地址
        # x = i
        # print(x, id(x))
        # l.append(lambda: f'x*x = {x * x}, id(x) = {id(x)}')
    return l

def func_get_outter_vars():
    x = 0
    return lambda: x + 1

def func_set_outter_vars():
    x = 0

    def inner_func():
        # 声明x为非局部变量，这样就可以在inner_func中修改x的值了
        nonlocal x
        x += 1
        return x

    return inner_func

if __name__ == "__main__":
    no_param_lambda = lambda: print('hello world')
    no_param_lambda()
    lambada = lambda x: x * x
    print(f'lambada(10): {lambada(10)}')

    def inner_func(x):
        return x * x
    print(f'inner_func(10): {inner_func(10)}')

    return_func1, return_func2, return_func3 = func_with_closure()
    print(f'return_func1: {return_func1()}, return_func2: {return_func2()}, return_func3: {return_func3()}')

    return_func_list = func_solve_closure()
    return_func_exec_list = [x() for x in return_func_list]
    print(f'return_func_exec_list: {return_func_exec_list}')

    print(func_get_outter_vars()())

    set_outter_vars_func = func_set_outter_vars()
    set_outtre_vars_func2 = func_set_outter_vars()
    print(f'set_outter_vars_func(): {set_outter_vars_func()}')
    print(f'set_outter_vars_func(): {set_outter_vars_func()}')
    print(f'set_outtre_vars_func2(): {set_outtre_vars_func2()}')
    print(f'set_outtre_vars_func2(): {set_outtre_vars_func2()}')

    def map_func(x):
        print(f'x: {x}')
        return math.pow(x, 2)
    map_result = map(map_func, [1, 2, 3])
    # 只有在遍历map_result时，才会执行map_func
    print(f'next(map_result): {next(map_result)}')
    print(f'next(map_result): {next(map_result)}')

    def reduce_func(x, y):
        print(f'x: {x}, y: {y}')
        return x + y
    reduce_result = reduce(reduce_func, list(range(10)))
    print(f'reduce_result: {reduce_result}')

    def filter_func(x):
        print(f'x: {x}')
        return x % 2 == 0
    filter_result = filter(filter_func, list(range(10)))
    print(f'filter_result: {list(filter_result)}')

    # 翻转排序
    print(sorted(list(range(10)), reverse=True))
    # 根据key转换后排序
    print(sorted(list(range(10)), key=lambda x: x if x % 2 == 0 else -x, reverse=True))
