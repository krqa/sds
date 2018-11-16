# -*- coding: utf-8 -*-

import csv

from . import _base


class Parser(_base.Parser):
    '''
    Parser for CSV formatted data.
    '''
    def _parse(self, data):
        data = (line.decode('utf-8') for line in data)
        for item in csv.DictReader(data, skipinitialspace=True):
            item = {k.lower(): v for k, v in item.items()}
            item['in_stock'] = item['instock']
            del item['instock']
            yield _base.Datum(**item)
