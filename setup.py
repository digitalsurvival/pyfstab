#!/usr/bin/env python3

import os
from pyfstab.version import __author__,__email__,__description__,__source__,__version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    author=__author__,
    author_email=__email__,
    name='pyfstab',
    version=__version__,
    description=__description__,
    url=__source__,
    license='MIT',
    keywords='linux fstab library filesystem editor',
    packages=['pyfstab'],
    install_requires=[''],
    long_description=read('README.md'),
    py_modules=['pyfstab'],
)
