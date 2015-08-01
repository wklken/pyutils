#!/usr/bin/env python
# encoding: utf-8

from itertools import chain, islice


def chunks(iterable, size, format=iter):
    it = iter(iterable)
    while True:
        yield format(chain((it.next(), ), islice(it, size - 1)))


# source: webpy
def group(seq, size):
    """
    Returns an iterator over a series of lists of length size from iterable.

        >>> list(group([1,2,3,4], 2))
        [[1, 2], [3, 4]]
        >>> list(group([1,2,3,4,5], 2))
        [[1, 2], [3, 4], [5]]
    """

    def take(seq, n):
        for i in xrange(n):
            yield seq.next()

    if not hasattr(seq, 'next'):
        seq = iter(seq)
    while True:
        x = list(take(seq, size))
        if x:
            yield x
        else:
            break


if __name__ == '__main__':
    a = range(10)

    for i in chunks(a, 3, format=iter):
        print i
        print tuple(i)

    print list(group([1, 2, 3, 4, 5], 2))
