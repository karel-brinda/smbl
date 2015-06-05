#
# TODO:
#  - fix linking error in CygWin
#

import smbl
import snakemake
import os

from ._program import *

DWGSIM      = get_bin_file_path("dwgsim")
DWGSIM_EVAL = get_bin_file_path("dwgsim_eval")


##########################################
##########################################


class DwgSim(Program):
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
