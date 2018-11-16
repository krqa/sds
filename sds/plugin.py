# -*- coding: utf-8 -*-

from importlib import import_module

from sds.decompressors._base import Decompressor
from sds.downloaders._base import Downloader
from sds.parsers._base import Parser

class PluginNameInvalid(Exception):
    pass

class PluginDoesNotExist(Exception):
    pass


def get_plugin(typ, name):
    '''
    Imports and returns plugin of given type with given name.
    '''
    # XXX: Do some more robust plugin "system"?
    # This seems to rely too much on shenanigans.
    import_module('.{}'.format(name), 'sds.{}'.format(typ))
    types = {
        'decompressors': Decompressor,
        'downloaders': Downloader,
        'parsers': Parser,
    }
    plugins = [
        plugin for plugin in types[typ].__subclasses__()
        if name == plugin.__module__.rsplit('.', 1)[1]
    ]
    if len(plugins) > 1:
        raise PluginNameInvalid(name)
    if not plugins:
        raise PluginDoesNotExist(name)
    return plugins[0]
