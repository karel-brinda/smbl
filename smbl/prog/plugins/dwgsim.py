import smbl
import snakemake
import os

import __program

DWGSIM      = __program.get_bin_file_path("dwgsim")
DWGSIM_EVAL = __program.get_bin_file_path("dwgsim_eval")


##########################################
##########################################


class DwgSim(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				DWGSIM,
				DWGSIM_EVAL,
			]

	@classmethod
	def install(cls):
		gitdir=cls.git_clone("http://github.com/nh13/dwgsim","dwgsim")
		smbl.prog.correct_samtools_make(os.path.join(gitdir,"samtools","Makefile"))
		cls.run_make("dwgsim")
		cls.install_file("dwgsim/dwgsim",DWGSIM)
		cls.install_file("dwgsim/dwgsim_eval",DWGSIM_EVAL)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
