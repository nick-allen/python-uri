#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from uri import __version__, __doc__


def parse_requirements(requirements):
	with open(requirements) as f:
		return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

with open('README.md') as f:
	long_description = f.read().strip()

test_requirements = parse_requirements('test-requirements.txt')

setup(
	name='uri',
	version=__version__,
	packages=find_packages(exclude=('tests.*', 'tests',)),
	url='https://github.com/nick-allen/python-uri',
	license='MIT',
	author='Nick Allen',
	author_email='nick.allen.cse@gmail.com',
	description=__doc__,
	long_description=long_description,
	include_package_data=True,
	zip_safe=False,
	install_requires=parse_requirements('requirements.txt'),
	extras_require={
		'test': test_requirements
	},
	test_suite='nose.collector',
	tests_require=test_requirements
)