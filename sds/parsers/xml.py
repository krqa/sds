# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

from . import _base


class Parser(_base.Parser):
    '''
    Parser for XML formatted data.
    '''
    def _parse(self, data):
        root = ET.parse(data).getroot()
        for item in root:
            values = {}
            for val in item:
                if val.tag == 'latest_price':
                    val.tag = 'price'
                elif val.tag == 'available':
                    val.tag = 'in_stock'

                values[val.tag] = val.text

            yield _base.Datum(**values)
