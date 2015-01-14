#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fun_var_args(farg, *args):
    print "arg:", farg
    for value in args:
        print "another arg:", value
#fun_var_args(1, "two", 3) # *args可以当作可容纳多个变量组成的list
fun_var_args(2, ("two",3))

def fun_var_kwargs(farg, **kwargs):
    print "arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])
#fun_var_kwargs(farg=1, myarg2="two", myarg3=3) # myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary
