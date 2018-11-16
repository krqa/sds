# -*- coding: utf-8 -*-


class DownloaderGetError(Exception):
    pass


class Downloader(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        try:
            return self._get()
        except Exception as e:
            raise DownloaderGetError() from e

    def _get(self):
        raise NotImplementedError
