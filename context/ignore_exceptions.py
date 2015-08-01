#!/usr/bin/env python
# encoding: utf-8

from contextlib import contextmanager

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

with ignored(ValueError):
    int('string')
