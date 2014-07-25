#!/usr/bin/env python
# encoding: utf-8

# source:  https://github.com/defnull/bottle/blob/master/bottle.py
class cached_property(object):
    """ A property that is only computed once per instance and then replaces
        itself with an ordinary attribute. Deleting the attribute resets the
        property. """

    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None: return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value


class A(object):

    @cached_property
    def key(self):
        print "call key()"
        return "hello"

if __name__ == '__main__':
    a = A()


    print a.key
    print a.key


