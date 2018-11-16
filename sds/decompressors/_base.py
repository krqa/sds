# -*- coding: utf-8 -*-

class DecompressorError(Exception):
    pass


class Decompressor(object):
    '''
    Base class for data decompressors to inherit from.
    '''
    def __init__(self, data):
        self.data = data

    def open(self):
        '''
        Opens a file inside archive, returning decompressed
        file-like object.
        '''
        try:
            return self._open()
        except Exception as e:
            raise DecompressorError() from e

    def _open(self):
        '''
        Performs actual decompression.

        Must be implemented by subclasses.
        '''
        raise NotImplementedError
