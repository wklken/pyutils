#!/usr/bin/env python
# encoding: utf-8
# from werkzeug


class UpdateDictMixin(object):
    """Makes dicts call `self.on_update` on modifications.

    .. versionadded:: 0.5

    :private:
    """

    on_update = None

    def calls_update(name):
        def oncall(self, *args, **kw):
            rv = getattr(super(UpdateDictMixin, self), name)(*args, **kw)
            if self.on_update is not None:
                self.on_update(self)
            return rv

        oncall.__name__ = name
        return oncall

    def setdefault(self, key, default=None):
        modified = key not in self
        rv = super(UpdateDictMixin, self).setdefault(key, default)
        if modified and self.on_update is not None:
            self.on_update(self)
        return rv

    def pop(self, key, default=None):
        modified = key in self
        if default is None:
            rv = super(UpdateDictMixin, self).pop(key)
        else:
            rv = super(UpdateDictMixin, self).pop(key, default)
        if modified and self.on_update is not None:
            self.on_update(self)
        return rv

    __setitem__ = calls_update('__setitem__')
    __delitem__ = calls_update('__delitem__')
    clear = calls_update('clear')
    popitem = calls_update('popitem')
    update = calls_update('update')
    del calls_update


class CallbackDict(UpdateDictMixin, dict):
    """A dict that calls a function passed every time something is changed.
    The function is passed the dict instance.
    """

    def __init__(self, initial=None, on_update=None):
        dict.__init__(self, initial or ())
        self.on_update = on_update

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, dict.__repr__(self))

if __name__ == '__main__':

    def callback(the_dict):
        print the_dict.items()

    a = CallbackDict(initial={1: 'a'}, on_update=callback)
    print a

    a[2] = 'b'
    a[1] = 'c'
