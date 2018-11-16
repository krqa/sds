# -*- coding: utf-8 -*-

from collections import namedtuple
from distutils.util import strtobool

class ParserError(Exception):
    pass


# TODO: Move this to some more reasonable place? Perhaps to some config?
fields = ('id', 'name', 'brand', 'retailer', 'price', 'in_stock')


class Datum(namedtuple('Datum', fields)):
    '''
    Represents a single data element.

    Also performs some standarization on creation,
    for things like prices and boolean values.
    '''
    __slots__ = ()

    def __new__(cls, id, name=None, brand=None, retailer=None, price=None, in_stock=None):
        price = "{:.2f}".format(float(price)) if price else ""
        try:
            in_stock = strtobool(in_stock)
        except AttributeError:
            in_stock = 1 if in_stock else 0
        return super().__new__(cls, id, name, brand, retailer, price, in_stock)


class Parser(object):
    '''
    Base class for data parsers to inherit from.
    '''
    def parse(self, data):
        '''
        Parses data (which is some kind of iterable) into
        another iterable of Datum instances.
        '''
        try:
            return self._parse(data)
        except Exception as e:
            raise ParserError() from e

    def _parse(self, data):
        '''
        Performs actual parsing part.

        Must be implemented by subclasses.
        '''
        raise NotImplementedError
