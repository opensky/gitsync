#!/usr/bin/env python

from setuptools import setup, find_packages

files = ["gitsync/*"]

setup(
    name = 'GitSync',
    version = "1.0",
    description = "A small app to keep servers files in sync with git",
    author = "Mike Zupan",
    author_email = "mzupan@shopopensky.com",
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            'gitsync = gitsync.main:main',
        ]
    },
)