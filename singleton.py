#coding=utf-8

class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class MyClass(object):
    __metaclass__ = Singleton

one = MyClass()
two = MyClass()

two.a = 3
print one.a
#3
print id(one)
#31495472
print id(two)
#31495472
print one == two
#True
print one is two
#True
