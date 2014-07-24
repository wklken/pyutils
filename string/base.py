#!/usr/bin/env python
# encoding: utf-8


#source: https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def iter_slices(string, slice_length):
    """Iterate over slices of a string."""
    pos = 0
    while pos < len(string):
        yield string[pos:pos + slice_length]
        pos += slice_length

if __name__ == '__main__':

    s = "abcdefg"
    for i in iter_slices(s, 2):
        print i
    #result:
    #ab
    #cd
    #ef
    #g


