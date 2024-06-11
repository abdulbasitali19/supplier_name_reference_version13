from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in supplier_name_reference_version13/__init__.py
from supplier_name_reference_version13 import __version__ as version

setup(
	name="supplier_name_reference_version13",
	version=version,
	description="supplier_reference_version13",
	author="Abdul Basit",
	author_email="basit@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
