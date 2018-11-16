# -*- coding: utf-8 -*-

import json

from . import _base


class Parser(_base.Parser):
    '''
    Parser for JSON formatted data.
    '''
    def _parse(self, data):
        for item in json.load(data):
            yield _base.Datum(**item)
