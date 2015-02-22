import sys
from setuptools import setup , find_packages

if sys.version_info < (3,2):
	print("At least Python 3.2 is required.\n", file=sys.stderr)
	exit(1)

setup(
	name = 'smbl',
	packages = ['smbl'], # this must be the same as the name above
	package_dir = {"smbl" : "smbl"},
	package_data = {"smbl" : ["*.snake"] },
	version = '0.0.11',
	description = 'SnakeMake Bioinformatics Library',
	long_description = """\
SnakeMake Bioinformatics Library
--------------------------------

A library for SnakeMake pipelines which makes possible to install various bioinformatics
tools and download data (e.g., in FASTA format). See http://github.com/karel-brinda/smbl
for details.

Copyright (c) 2015 Karel Břinda <karel.brinda@gmail.com> (see LICENSE)
""",
	install_requires=[
		'snakemake',
	],
	zip_safe=False,
	author = 'Karel Břinda',
	author_email = 'karel.brinda@gmail.com',
	url = 'http://github.com/karel-brinda/smbl',
	license = "MIT",
	#download_url = 'https://github.com/karel-brinda/smbl/tarball/0.0.1',
	keywords = ['Snakemake', 'bioinformatics'],
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
