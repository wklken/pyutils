#!/usr/bin/env python
# encoding: utf-8
# from werkzeug


class TypeConversionDict(dict):
    def get(self, key, default=None, type=None):
        try:
            rv = self[key]
            if type is not None:
                rv = type(rv)
        except (KeyError, ValueError):
            rv = default

        return rv


if __name__ == '__main__':
    d = TypeConversionDict({'a': '1', 'b': 'i'})

    a = d.get('a', type=int)
    print type(a)
    print a

    b = d.get('b', default=0, type=int)
    print type(b)
    print b
