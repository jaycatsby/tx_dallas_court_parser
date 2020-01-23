from setuptools import Command, find_packages, setup
import os

setup(
    name='dallasparser',
    description='TX Dallas Criminal Case Parser',
    keywords='texas dallas criminal court parser',
    url='https://github.com/jaycatsby/tx_dallas_court_parser',
    author='Jay Choi',
    author_email='nobeedee@gmail.com',
    license='MIT',
    packages=find_packages(include=['dallasparser', 'dallasparser.*'])
)
