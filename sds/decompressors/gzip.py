# -*- coding: utf-8 -*-

import gzip

from . import _base


class Decompressor(_base.Decompressor):
    '''
    GZIP archive decompressor.
    '''
    def _open(self):
        return gzip.GzipFile(fileobj=self.data)
