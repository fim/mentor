#!/usr/bin/env python

from distutils.core import setup

setup(name='mentor',
    version=0.1,
    description='Simple file sharing tool over HTTP/HTTPS',
    author='fim',
    install_requires=[
        'M2Crypto',
        'miniupnpc',
        'gevent'],
#    author_email='',
    scripts=['mentor']
)
