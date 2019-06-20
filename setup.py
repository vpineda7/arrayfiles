#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup


setup(
    name='easyfile',
    version='0.0.1',
    description='Random Accessible Text file handler',
    long_description=open('./README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yasufumy/textfile',
    author='Yasufumi Taniguchi',
    author_email='yasufumi.taniguchi@gmail.com',
    packages=[
        'easyfile'
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
