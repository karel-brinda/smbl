import smbl
import snakemake
import os

from ._program import *

TABIX = get_bin_file_path("tabix")
BGZIP = get_bin_file_path("bgzip")


##########################################
##########################################


class HtsLib(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				TABIX,
				BGZIP,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("git://github.com/samtools/bcftools","bcftools")
		gitdir_htslib=cls.git_clone("git://github.com/samtools/htslib","htslib")
		cls.run_make("htslib")
		cls.install_file("htslib/tabix",TABIX)
		cls.install_file("htslib/bgzip",BGZIP)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
