#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 面向对象 """
__date__ = "2024/10/1 18:31"

from bisect import insort
from time import sleep
from types import MethodType

# object类似java的Object对象，是所有类的基类
class Animals(object):

    def __init__(self, name):
        self.name = name

    def run(self):
        print('animal is running')


class Pet(object):
    def __init__(self):
        pass

    def run(self):
        print('pet is running')

    def sleep(self):
        print('pet is sleeping')

# Cat 继承 Animals, Pet；多继承时，优先使用第一个父类的方法（多个父类存在冲突时）
class Cat(Animals, Pet):

    def __init__(self, name, age):
        # 调用父类的构造函数
        super().__init__(name)
        # self.name = name
        self.age = age
        # 私有变量，_owner为约定，__sex为强制，但可以通过_Cat__sex访问
        self._owner = 'jerry'
        self.__sex = 'male'

    # 如果没有定义某个属性，可以通过__getattr__方法动态返回属性值，否则直接获取会报错
    def __getattr__(self, item):
        print(f'{self}.__getattr__({item})')
        if item == 'age':
            return 10
        return item

    def get_owner(self):
        return self._owner

    def get_sex(self):
        return self.__sex

class Mouse(Animals):
    # 类似于java的static
    hobby = 'eat'

    @classmethod
    def modify_hobby(cls):
        print(f'modify_hobby, {cls.hobby}')
        Mouse.hobby = 'play'
        pass

    @staticmethod
    def hello(*info):
        Mouse.hobby = 'sleep'
        print(f'mouse say hello {info}')
        return Mouse(info[0])

    def __call__(self, *args, **kwargs):
        print(f'mouse is running')
        sleep(1)
        print(f'mouse is sleeping')


def run(obj):
    obj.run()

if __name__ == "__main__":
    cat = Cat('Tom', '66')
    mouse = Mouse('Jerry')
    print(
        f'cat:({cat.name}, {cat.age}, {cat._owner}, {cat.get_owner()}, {cat._Cat__sex}, {cat.get_sex()}), mouse:{mouse.name}')
    print(f'isinstance(cat, Animals): {isinstance(cat, Animals)}，isinstance(cat, Pet): {isinstance(cat, Pet)}')
    # 优先使用第一个父类的方法（多个父类存在冲突时）
    cat.run()
    cat.sleep()

    # 动态语言，只需要类重定义了同名方法即可
    run(Animals("Alice"))
    run(Pet())

    print(f"hasattr(mouse, 'age'): {hasattr(mouse, 'age')}")
    # mouse.age = 12
    print(f"getattr(mouse, 'age', 10): {getattr(mouse, 'age', 10)}")
    print(f"setattr(mouse, 'age', 10): {setattr(mouse, 'age', 20)}")
    print(f'mouse.age: {mouse.age}')
    print(f'mouse.hobby: {mouse.hobby}')
    print(f'Mouse.hobby: {Mouse.hobby}')
    mouse.hobby = 'play'
    print(f'mouse.hobby: {mouse.hobby}')
    print(f'Mouse.hobby: {Mouse.hobby}')

    mouse.eat = lambda: print('mouse eat')
    mouse.eat()

    def set_age(self, age):
        self.age = age
    mouse.set_age = MethodType(set_age, mouse)
    mouse.set_age(123)
    print(f'mouse.age: {mouse.age}')

    Mouse.modify_hobby()
    print(Mouse.hobby)

    mouse2 = Mouse.hello("kk")
    print(Mouse.hobby)
    print(mouse2)


