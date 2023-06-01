from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pos_compu_sys/__init__.py
from pos_compu_sys import __version__ as version

setup(
	name="pos_compu_sys",
	version=version,
	description="Devs",
	author="Digital Box",
	author_email="eng.bakraldubai@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
