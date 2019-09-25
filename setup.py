# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description： websdk
    date: 2019-09-24
"""
from setuptools import setup

setup(
    name='websdk',
    version='0.0.1',
    packages=['sdk'],
    url='https://github.com/KHdvip/websdk',
    license='GPL-3.0',
    install_requires=[
        'fire',
        'shortuuid',
        'pymysql',
        'sqlalchemy',
        'python3-pika',
        'PyJWT',
        'Crypto',
        'requests',
        'redis',
        'tornado',
        'aliyun-python-sdk-core-v3==2.8.6',
        'aliyun-python-sdk-dysmsapi',
        'python-dateutil==2.7.5',
        'ldap3==2.6',
        'pycryptodome',
        'werkzeug',
    ],
    author='阿慕路泽',
    author_email='314901758@qq.com',
    description='python web script'
)