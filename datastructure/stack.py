#!/usr/bin/env python
# encoding: utf-8


# source: webpy
def restack(stack, index=0):
    """Returns the element at index after moving it to the top of stack.

           >>> x = [1, 2, 3, 4]
           >>> restack(x)
           1
           >>> x
           [2, 3, 4, 1]
    """
    x = stack.pop(index)
    stack.append(x)
    return x
