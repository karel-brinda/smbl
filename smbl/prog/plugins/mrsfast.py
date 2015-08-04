#
# TODO:
#  - fix sysctl error in CygWin
#


import smbl
import snakemake
import os

from ._program import *

MRSFAST = get_bin_file_path("mrsfast")


##########################################
##########################################


class MrsFast(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				MRSFAST,
			]

	@classmethod
	def install(cls):
		cls.git_clone("git://github.com/sfu-compbio/mrsfast/","")
		cls.run_make("")
		cls.install_file("mrsfast",MRSFAST)

	@classmethod
	def supported_platforms(cls):
		return ["osx","linux"]
