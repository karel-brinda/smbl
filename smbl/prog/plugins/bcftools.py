import smbl
import snakemake
import os

import __program

BCFTOOLS = __program.get_bin_file_path("bcftools")


##########################################
##########################################


class BcfTools(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				BCFTOOLS,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("http://github.com/samtools/bcftools","bcftools")
		gitdir_htslib=cls.git_clone("http://github.com/samtools/htslib","htslib")
		cls.run_make("bcftools")
		cls.install_file("bcftools/bcftools",BCFTOOLS)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
