# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = [
		line
		for line in f.read().strip().split('\n')
		if line and not line.startswith('#')
	]

# Keep version inline so editable installs work in uv's isolated build env
# (importing the package pulls in runtime deps like frappe).
version = '0.0.1'

setup(
	name='whitelabel',
	version=version,
	description='ERPNext Whitelabel',
	author='Bhavesh Maheshwari',
	author_email='maheshwaribhavesh95863@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
