#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup
from pisces import __version__


def read(fname):
    """Loads the contents of a file, returning it as a string"""
    filepath = os.path.join(os.path.dirname(__file__), fname)
    return open(filepath, 'r').read()


setup(
    name="pisces",
    version=__version__,
    description='Use keywords to search for and download images.',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author='wolfhong',
    author_email='hongxucai1991@gmail.com',
    url='https://github.com/wolfhong/pisces',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
    ],
    keywords=[
        'download-images', 'search-images', 'algorithm-training', 'image-dataset',
        'google', 'baidu',
    ],
    license="MIT",
    packages=['pisces'],
    platforms='any',
    install_requires=[
        'selenium>=2.53.6',
        'requests',
    ],
    python_requires='>=2.7, <4',
    entry_points={
        'console_scripts': [
            'pisces=pisces.command:main',
        ],
    },
)
