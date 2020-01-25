#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import Command, find_packages, setup
import os

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, 'README.md')) as infile:
    long_description = infile.read()

_VERSION = '0.2'

_CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
]

setup(
    name='dallasparser',
    version=_VERSION,
    install_requires=[
        r for r in open('requirements.txt', 'r').read().split('\n') if r
    ],
    description='TX Dallas Criminal Case Parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='texas dallas criminal court parser',
    url='https://github.com/jaycatsby/tx_dallas_court_parser',
    author='Jay Choi',
    author_email='nobeedee@gmail.com',
    license='MIT',
    packages=find_packages(include=['dallasparser', 'dallasparser.*']),
    entry_points={
        'console_scripts': ['dallasparser=dallasparser.cli:main'],
    },
    python_requires='>=3.6',
    classifiers=_CLASSIFIERS,
)
