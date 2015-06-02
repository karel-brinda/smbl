import smbl
import snakemake
import os

from ._program import *

SAMTOOLS = get_bin_file_path("samtools")


##########################################
##########################################


class SamTools(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				SAMTOOLS,
			]

	@classmethod
	def install(cls):
		gitdir_samtools=cls.git_clone("git://github.com/samtools/samtools","samtools")
		gitdir_htslib=cls.git_clone("git://github.com/samtools/htslib","htslib")
		smbl.prog.correct_samtools_make(os.path.join(gitdir_samtools,"Makefile"))
		cls.run_make("samtools")
		cls.install_file("samtools/samtools",SAMTOOLS)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
