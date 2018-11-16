# -*- coding: utf-8 -*-

from urllib.request import urlopen

from . import _base


class Downloader(_base.Downloader):
    def _get(self):
        return urlopen(self.url)
