#!/usr/bin/env python
# encoding: utf-8

from configparser import ConfigParser

# source: https://github.com/defnull/bottle/blob/master/bottle.py
class ConfigDict(dict):
    """ A dict-like configuration storage with additional support for
        namespaces, validators, meta-data, on_change listeners and more.
    """

    __slots__ = ('_meta', '_on_change')

    def __init__(self):
        self._meta = {}
        self._on_change = lambda name, value: None

    def load_config(self, filename):
        """ Load values from an ``*.ini`` style config file.

            If the config file contains sections, their names are used as
            namespaces for the values within. The two special sections
            ``DEFAULT`` and ``bottle`` refer to the root namespace (no prefix).
        """
        conf = ConfigParser()
        conf.read(filename)
        for section in conf.sections():
            for key, value in conf.items(section):
                if section not in ('DEFAULT', 'bottle'):
                    key = section + '.' + key
                self[key] = value
        return self

    def load_dict(self, source, namespace=''):
        """ Load values from a dictionary structure. Nesting can be used to
            represent namespaces.

            >>> c = ConfigDict()
            >>> c.load_dict({'some': {'namespace': {'key': 'value'} } })
            {'some.namespace.key': 'value'}
        """
        for key, value in source.items():
            if isinstance(key, str):
                nskey = (namespace + '.' + key).strip('.')
                if isinstance(value, dict):
                    self.load_dict(value, namespace=nskey)
                else:
                    self[nskey] = value
            else:
                raise TypeError('Key has type %r (not a string)' % type(key))
        return self

    def update(self, *a, **ka):
        """ If the first parameter is a string, all keys are prefixed with this
            namespace. Apart from that it works just as the usual dict.update().
            Example: ``update('some.namespace', key='value')`` """
        prefix = ''
        if a and isinstance(a[0], str):
            prefix = a[0].strip('.') + '.'
            a = a[1:]
        for key, value in dict(*a, **ka).items():
            self[prefix+key] = value

    def setdefault(self, key, value):
        if key not in self:
            self[key] = value

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('Key has type %r (not a string)' % type(key))
        value = self.meta_get(key, 'filter', lambda x: x)(value)
        if key in self and self[key] is value:
            return
        self._on_change(key, value)
        dict.__setitem__(self, key, value)

    def __delitem__(self, key):
        self._on_change(key, None)
        dict.__delitem__(self, key)

    def meta_get(self, key, metafield, default=None):
        """ Return the value of a meta field for a key. """
        return self._meta.get(key, {}).get(metafield, default)

    def meta_set(self, key, metafield, value):
        """ Set the meta field for a key to a new value. This triggers the
            on-change handler for existing keys. """
        self._meta.setdefault(key, {})[metafield] = value
        if key in self:
            self[key] = self[key]

    def meta_list(self, key):
        """ Return an iterable of meta field names defined for a key. """
        return self._meta.get(key, {}).keys()

#useage:
#self.config = ConfigDict().load_dict(config)
#self.config = ConfigDict()
#self.config._on_change = functools.partial(self.trigger_hook, 'config')
#self.config.meta_set('autojson', 'validate', bool)
#self.config.meta_set('catchall', 'validate', bool)
#self.config['catchall'] = catchall
#self.config['autojson'] = autojson
