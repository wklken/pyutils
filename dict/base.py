#!/usr/bin/env python
# encoding: utf-8


# source: webpy
def dictreverse(mapping):
    """
    Returns a new dictionary with keys and values swapped.

        >>> dictreverse({1: 2, 3: 4})
        {2: 1, 4: 3}
    """
    return dict([(value, key) for (key, value) in mapping.iteritems()])


# source: webpy
def dictfind(dictionary, element):
    """
    Returns a key whose value in `dictionary` is `element`
    or, if none exists, None.

        >>> d = {1:2, 3:4}
        >>> dictfind(d, 4)
        3
        >>> dictfind(d, 5)
    """
    for (key, value) in dictionary.iteritems():
        if element is value:
            return key


# source: webpy
def dictfindall(dictionary, element):
    """
    Returns the keys whose values in `dictionary` are `element`
    or, if none exists, [].

        >>> d = {1:4, 3:4}
        >>> dictfindall(d, 4)
        [1, 3]
        >>> dictfindall(d, 5)
        []
    """
    res = []
    for (key, value) in dictionary.iteritems():
        if element is value:
            res.append(key)
    return res
