#!/usr/bin/env python

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='wordbridge',
    version='0.1.0',
    description='Convert semantic Word documents into clean HTML',
    long_description=read("README"),
    author='Michael Williamson',
    url='http://github.com/mwilliamson/wordbridge',
    packages=['wordbridge'],
    install_requires=["lxml==3.0.1"],
)
