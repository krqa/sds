# -*- coding: utf-8 -*-

import csv

from sds.parsers._base import fields


class Output(object):
    '''
    Stores data (Datum instances) in a CSV file.
    '''
    def __init__(self, filename):
        self.file = open(filename, 'w', newline='')
        self.csv = csv.writer(self.file)
        self.csv.writerow(fields + ('source',))

    def close(self):
        self.file.close()

    def store(self, source, data):
        '''
        Stores data from given source, along with the source name.
        '''
        for datum in data:
            self.csv.writerow(datum + (source,))
