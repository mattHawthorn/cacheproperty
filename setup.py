#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [

]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    name='cacheproperty',
    version='0.1.1',
    description="A subclass of python's builtin property class that removes boilerplate by implementing the h_hidden_attribute pattern with a single decorator call. Also afacilitates invalidation of the cached hidden attribute with a @cacheproperty.invalidate decorator on any other methods or properties in a class.",
    long_description=readme + '\n\n' + history,
    author="Matthew Hawthorn",
    author_email='hawthorn.matthew@gmail.com',
    url='https://github.com/mattHawthorn/cacheproperty',
    packages=find_packages(include=['cacheproperty']),
    entry_points={
        'console_scripts': [
            'cacheproperty=cacheproperty.cli:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='cacheproperty',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
