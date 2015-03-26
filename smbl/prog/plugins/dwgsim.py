#
# TODO:
#  - fix linking error in CygWin
#

import smbl
import snakemake
import os

import _program

DWGSIM      = _program.get_bin_file_path("dwgsim")
DWGSIM_EVAL = _program.get_bin_file_path("dwgsim_eval")


##########################################
##########################################


class DwgSim(_program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				DWGSIM,
				DWGSIM_EVAL,
			]

	@classmethod
	def install(cls):
		gitdir=cls.git_clone("git://github.com/nh13/dwgsim","dwgsim")
		smbl.prog.correct_samtools_make(os.path.join(gitdir,"samtools","Makefile"))
		cls.run_make("dwgsim")
		cls.install_file("dwgsim/dwgsim",DWGSIM)
		cls.install_file("dwgsim/dwgsim_eval",DWGSIM_EVAL)

	@classmethod
	def supported_platforms(cls):
		return ["osx","linux"]
