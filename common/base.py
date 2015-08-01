#!/usr/bin/env python
# encoding: utf-8

import io
import os


# source: https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def super_len(o):
    if hasattr(o, '__len__'):
        return len(o)

    if hasattr(o, 'len'):
        return o.len

    if hasattr(o, 'fileno'):
        try:
            fileno = o.fileno()
        except io.UnsupportedOperation:
            pass
        else:
            return os.fstat(fileno).st_size

    if hasattr(o, 'getvalue'):
        # e.g. BytesIO, cStringIO.StringIO
        return len(o.getvalue())


if __name__ == '__main__':
    print super_len("abcde")
    print super_len([1, 2, 3])
