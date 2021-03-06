# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import dirname, join

setup(
    name='django-clientsignal',
    version='0.3.1',
    author='Will Barton',
    author_email='g@gulielmus.com',
    description='Django Client Signals is a SockJS-Tornado-based mechanism for sending and receiving Django signals as client-side events.',
    long_description=open('README.md').read(),
    url='http://github.com/gulielmus/django-clientsignal',
    install_requires=["sockjs-tornado", "redis", "tornado-redis", "django"],
    include_package_data=True,
    package_data={'clientsignal':['static/clientsignal/js/*',],},
    packages=find_packages(),
    license='BSD'
)

