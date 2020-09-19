#!/usr/bin/env python

from setuptools import setup, find_packages
import wtknowledgebase

setup(
    name='wagtail-knowledgebase',
    version=wtknowledgebase.__version__,
    description='Knowledgebase pages with bootstrap compatible StreamFields configured',
    long_description=open('README.rst').read(),
    author='Shaun Kruger',
    author_email='shaun.kruger@gmail.com',
    url='https://github.com/skruger/wagtail-knowledgebase',
    packages=find_packages(exclude=('tests*', 'testapp', 'search')),
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php',
    platforms='all',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        "wagtail>=2.9.1",
    ],
    include_package_data=True,
    zip_safe=False,
)
