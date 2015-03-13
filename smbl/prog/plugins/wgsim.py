import smbl
import snakemake
import os

import __program

WGSIM      = __program.get_bin_file_path("wgsim")
WGSIM_EVAL = __program.get_bin_file_path("wgsim_eval.pl")


##########################################
##########################################


class WgSim(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				WGSIM,
				WGSIM_EVAL,
			]

	@classmethod
	def install(cls):
		gitdir=cls.git_clone("http://github.com/lh3/wgsim","wgsim")
		snakemake.shell('cd "{dir}" && gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm'.format(dir=gitdir))
		cls.install_file("wgsim/wgsim",WGSIM)
		cls.install_file("wgsim/wgsim_eval.pl",WGSIM_EVAL)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
