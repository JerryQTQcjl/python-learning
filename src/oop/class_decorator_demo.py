#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 类装饰器 """
__date__ = "2024/10/2 15:18"

# from src.function.decorator_demo import log

# 自定义装饰器
class MyProperty:

    def __init__(self, get=None, set=None):
        self.__get = get
        # self.__get = lambda x: x._score
        self.__set = set
        print(f'MyProperty.__init__ self:{self}, get: {self.__get}, set: {self.__set}')

    # 添加了@MyProperty的方法，会被调用
    # 当调用s.score时，会调用__get__方法
    def __get__(self, instance, type):
        print(f'__get__ self: {self}, instance: {instance}, type: {type}')
        return self.__get(instance)

    # 当调用s.score = 60时，会调用__set__方法
    def __set__(self, instance, value):
        print(f'__set__ self: {self}, instance: {instance}, value: {value}')
        if self.__set is None:
            raise AttributeError("this attribute is read-only")
        return self.__set(instance, value)

    def setter(self, set):
        self.__set = set
        print(f'setter self: {self}, set: {set}')
        return self

    def getter(self, get):
        self.__get = get
        print(f'getter self: {self}, get: {get}')
        return self

class ClassForClassDecorator:
    def __init__(self, cls):
        print(f'ClassForClassDecorator.__init__ self:{self}, cls:{cls}')
        self.cls = cls

    def __call__(self, *args, **kwargs):
        print(f'ClassForClassDecorator.__call__ {self}, {args}, {kwargs}')
        # return self.cls(*args, **kwargs)
        return self

def funcForClassDecorator(cls):
    print(f'funcForClassDecorator, cls:{cls}')
    cls.teacher = 'MR.Li'
    return cls

"""
如果注解是一个类，那么会调用这个类的__init__方法，相当于实例化这个类，类型变成这个类的实例
如果注解是一个方法，那么会调用这个方法，类型变成方法的返回值
"""
@ClassForClassDecorator
# @funcForClassDecorator
class Student(object):

    @MyProperty
    # @property
    # @log()
    def score(self):
        return self._score

    # @score.setter
    # @score是MyProperty的实例，所以@score.setter相当于调用MyProperty实例的setter方法，注意，这里是实例
    # @log()
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

if __name__ == "__main__":
    # s = Student()
    # print(f'type(Student): {type(Student)}')
    # s.score = 60
    # print(f's.score: {s.score}')
    # print(f's.teacher: {s.teacher}')
    # s.score = 9999
    s = Student()
    print(f'type(Student): {type(s)}')
    # s()
    pass
