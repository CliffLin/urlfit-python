#!/usr/bin/env python


from setuptools import setup

setup(
	name='UrlFit',
	version='1.0.3',
	description='UrlFit - Shorten your url',
	author='Ze-Yan Lin',
	author_email='zylin@url.fit',
	url='https://url.fit',
	install_requires = ['requests[security]','cryptography'],
	packages=['urlfit'],
	entry_points={"console_scripts": ["urlfit=src.urlfit:main"]}
)

