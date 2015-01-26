import sys
from setuptools import setup , find_packages

#DISTUTILS_DEBUG="yesss"

if sys.version_info < (3,2):
    print("At least Python 3.2 is required.\n", file=sys.stderr)
    exit(1)

setup(
  name = 'SMBL',
  packages = ['SMBL'], # this must be the same as the name above
  package_dir = {"SMBL" : "SMBL"},
  package_data = {"SMBL" : ["*.snake"] },
  #include_package_data=True,
  #packages=setuptools.find_packages(),
  #include_package_data=True,  # use MANIFEST.in during install
  version = '0.0.1',
  description = 'SnakeMake Bioinformatics Library',
  author = 'Karel Brinda',
  install_requires=[
  	'snakemake',
  ],
  author_email = 'karel.brinda@gmail.com',
  url = 'https://github.com/karel-brinda/smbl', # use the URL to the github repo
  #download_url = 'https://github.com/karel-brinda/smbl/tarball/0.0.1', # I'll explain this in a second
  keywords = ['Snakemake', 'bioinformatics'], # arbitrary keywords
  classifiers = [],
)
