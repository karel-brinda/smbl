#
# TODO:
#  - fix linking error in CygWin
#

import smbl
import snakemake
import os

from ._program import *

BCFTOOLS = get_bin_file_path("bcftools")
VCFUTILS = get_bin_file_path("vcfutils.pl")


##########################################
##########################################


class BcfTools(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				BCFTOOLS,
				VCFUTILS,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("git://github.com/samtools/bcftools","bcftools")
		gitdir_htslib=cls.git_clone("git://github.com/samtools/htslib","htslib")
		cls.run_make("bcftools")
		cls.install_file("bcftools/bcftools",BCFTOOLS)
		cls.install_file("bcftools/vcfutils.pl",VCFUTILS)

	@classmethod
	def supported_platforms(cls):
		return ["osx","linux"]
