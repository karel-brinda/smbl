import sys
from setuptools import setup , find_packages

#DISTUTILS_DEBUG="yesss"

if sys.version_info < (3,2):
	print("At least Python 3.2 is required.\n", file=sys.stderr)
	exit(1)

setup(
	name = 'smbl',
	packages = ['smbl'], # this must be the same as the name above
	package_dir = {"smbl" : "smbl"},
	package_data = {"smbl" : ["*.snake"] },
	#include_package_data=True,
	#packages=setuptools.find_packages(),
	#include_package_data=True,  # use MANIFEST.in during install
	version = '0.0.1',
	description = 'SnakeMake Bioinformatics Library',
	long_description = """\
SnakeMake Bioinformatics Library
--------------------------------

A library for SnakeMake pipelines which makes possible to install various bioinformatics
tools and download data (e.g., in FASTA format).
""",
	install_requires=[
		'snakemake',
	],
	zip_safe=False,
	author = 'Karel Břinda',
	author_email = 'karel.brinda@gmail.com',
	url = 'https://github.com/karel-brinda/smbl',
	license = "MIT",
	#download_url = 'https://github.com/karel-brinda/smbl/tarball/0.0.1', # I'll explain this in a second
	keywords = ['Snakemake', 'bioinformatics'], # arbitrary keywords
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Environment :: Console",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 3",
		"Topic :: Scientific/Engineering :: Bio-Informatics"
	],
)
