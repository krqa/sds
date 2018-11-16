# -*- coding: utf-8 -*-

import argparse
import mimetypes

from sds.output import Output
from sds.plugin import get_plugin


def detect_type(url):
    '''
    Detects file/url type. based on extension.
    '''
    typ, compression = mimetypes.guess_type(url)
    if typ == 'application/zip':
        typ = mimetypes.guess_type(url[:-4])[0]
        compression = 'zip'
    return (typ.split('/')[1], compression)


def do_work(urls, output_fn):
    '''
    Performs the work.
    [aka. ties everything together.]
    '''
    output = Output(output_fn)

    for url in urls:
        data = get_plugin('downloaders', 'http')(url).get()

        typ, compression = detect_type(url)

        if compression is not None:
            data = get_plugin('decompressors', compression)(data).open()

        output.store(typ, get_plugin('parsers', typ)().parse(data))

    output.close()


def main():
    ap = argparse.ArgumentParser(description="Simple Data Standardizer")
    ap.add_argument(
        '-o', '--output', default='output.csv',
        help='Output Filename (default: `output.csv`)',
    )
    ap.add_argument('url', nargs='+')
    args = ap.parse_args()

    do_work(args.url, args.output)
