# -*- coding: utf-8 -*-

import io
import zipfile

from . import _base


class Decompressor(_base.Decompressor):
    '''
    ZIP archive decompressor.
    '''
    def _open(self):
        # ZipFile does not like HTTPResponse objects...
        fi = zipfile.ZipFile(io.BytesIO(self.data.read()))
        # TODO: Handle multiple files?
        filename = fi.namelist()[0]
        return fi.open(filename)
