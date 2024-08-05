# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  mixiu-app-helper
# FileName:     setup.py
# Description:  TODO
# Author:       zhouhanlin
# CreateDate:   2024/07/17
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from setuptools import setup, find_packages

setup(
    name='mixiu-app-helper',
    version='0.1.4',
    description='This is my mixiu app helper package',
    long_description='This is my mixiu app helper package',
    author='ckf10000',
    author_email='ckf10000@sina.com',
    url='https://github.com/ckf10000/mixiu-app-helper',
    packages=find_packages(),
    install_requires=[
        'airtest-helper>=0.1.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
