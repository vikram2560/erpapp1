# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpapp1/__init__.py
from erpapp1 import __version__ as version

setup(
	name='erpapp1',
	version=version,
	description='testing app',
	author='vikram',
	author_email='vikramsahani256@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
