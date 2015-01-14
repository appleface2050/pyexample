#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A():
    def __init__(self):
        print self.__class__            #__class限制当前类名


class B(A):
    pass

if __name__ == '__main__':
    b = B()
