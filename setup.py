# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name='sds',
    version='1.0',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'sds = sds.main:main',
        ],
    },
)
