# -*- coding: utf-8 -*-
"""Installer for the hph.widgets package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = read('README.rst')

setup(
    name='mhb.site',
    version='1.0.0',
    description="Meetshaus Site",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone, Python',
    author='Christoph Böhner-Figas',
    author_email='cb@ade25.de',
    url='http://pypi.python.org/pypi/adk.site',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['mhb'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
