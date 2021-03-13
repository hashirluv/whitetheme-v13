# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in whitetheme_v13/__init__.py
from whitetheme_v13 import __version__ as version

setup(
	name='whitetheme_v13',
	version=version,
	description='White Theme for v13',
	author='Hashir',
	author_email='hashirabdulla@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
