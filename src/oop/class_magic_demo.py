#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        """初始化方法，创建实例时被调用"""
        self.name = name
    
    def __str__(self):
        """
        返回对象的字符串表示，用于print()和str()
        当使用print()打印对象时会调用此方法
        """
        return f'Student object (name: {self.name})'
    
    # __repr__用于调试，返回开发者看到的字符串表示
    # 当没有__str__时会使用__repr__作为替代
    __repr__ = __str__
    
    def __call__(self):
        """
        使实例可以像函数一样被调用
        例如: student()会调用这个方法
        """
        print(f'My name is {self.name}')

class Fibonacci(object):
    def __init__(self):
        """初始化斐波那契数列的前两个数"""
        self.a, self.b = 0, 1
    
    def __iter__(self):
        """
        使类可迭代，返回迭代器对象
        实现了__iter__方法的对象可以用于for循环
        """
        return self
    
    def __next__(self):
        """
        返回数列的下一个值
        当数列中的值大于100时，停止迭代
        """
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
    
    def __getitem__(self, n):
        """
        根据索引获取数列中的值
        支持整数索引和切片
        """
        if isinstance(n, int):
            a, b = 1, 1
            for _ in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice):
            start = n.start if n.start else 0
            stop = n.stop
            L = []
            a, b = 1, 1
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L

class DynamicAttr(object):
    def __init__(self):
        self.name = 'Dynamic'
    
    def __getattr__(self, attr):
        """
        动态返回属性值
        如果请求的属性是'score'，返回99
        如果请求的属性是'age'，返回一个函数，调用该函数返回25
        """
        if attr == 'score':
            return 99
        elif attr == 'age':
            return lambda: 25
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")

def main():
    # 测试 Student
    s = Student('张三')
    print(s)  # 测试 __str__
    s()       # 测试 __call__
    
    # 测试 Fibonacci
    f = Fibonacci()
    print('Fibonacci 迭代:')
    for n in f:
        print(n, end=' ')
    print('\n')
    
    print(f'第5个斐波那契数：{f[4]}')
    print(f'斐波那契切片[0:5]：{f[0:5]}')
    
    # 测试 DynamicAttr
    d = DynamicAttr()
    print(f'score: {d.score}')
    print(f'age: {d.age()}')
    
if __name__ == "__main__":
    main()
