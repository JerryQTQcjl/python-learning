
"""
数据描述符
描述符必须实现__get__, __set__, __delete__
"""
from types import MethodType

class DataDescriptor:
    def __get__(self, instance, owner):
        print(f'__get__({self}, {instance}, {owner})')
        return self

    def __set__(self, instance, value):
        print(f'__set__({self}, {instance}, {value})')

    def __delete__(self, instance):
        print(f'__delete__({self}, {instance})')


"""
非数据描述符
只有__get__方法的描述符, 没有__set__和__delete__
"""
class NonDataDescriptor:
    def __get__(self, instance, owner):
        print(f'__get__({self}, {instance}, {owner})')
        return self
    
class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        if hasattr(obj, '__get__'):
            print(1)
            return self.f.__get__(cls)
        print(2)
        return MethodType(self.f, cls)


class Test:
    apple = DataDescriptor()
    banana = NonDataDescriptor()

    def __getattr__(self, name):
        print(f'__getattr__({name})')

    def __setattr__(self, name, value):
        print(f'__setattr__({name}, {value})')

    @ClassMethod
    def test(cls):
        print(f'test {cls}')
        pass

def func():
    pass


if __name__ == '__main__':
    t = Test()
    # t.apple = 1
    t.apple
    Test.apple
    """ del t.apple
    print(t.banana)
    t.banana = 1
    print(t.banana)
    del t.banana

    print(Test.__getattr__)
    print(t.__getattr__)
    print(func) """

    Test.test()