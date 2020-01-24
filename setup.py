from setuptools import Command, find_packages, setup
import os

CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
]

setup(
    name='dallasparser',
    description='TX Dallas Criminal Case Parser',
    keywords='texas dallas criminal court parser',
    url='https://github.com/jaycatsby/tx_dallas_court_parser',
    author='Jay Choi',
    author_email='nobeedee@gmail.com',
    license='MIT',
    packages=find_packages(include=['dallasparser', 'dallasparser.*']),
    python_requires='>=3.6',
    classifiers=CLASSIFIERS,
)
