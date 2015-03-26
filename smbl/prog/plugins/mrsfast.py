#
# TODO:
#  - fix sysctl error in CygWin
#


import smbl
import snakemake
import os

import _program

MRSFAST = _program.get_bin_file_path("mrsfast")


##########################################
##########################################


class MrsFast(_program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				MRSFAST,
			]

	@classmethod
	def install(cls):
		cls.git_clone("git://git.code.sf.net/p/mrsfast/code","")
		cls.run_make("")
		cls.install_file("mrsfast",MRSFAST)

	@classmethod
	def supported_platforms(cls):
		return ["osx","linux"]
