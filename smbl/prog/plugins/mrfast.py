import smbl
import snakemake
import os

from ._program import *

MRFAST = get_bin_file_path("mrfast")


##########################################
##########################################


class MrFast(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				MRFAST,
			]

	@classmethod
	def install(cls):
		cls.git_clone("git://github.com/BilkentCompGen/mrfast","")
		cls.run_make("")
		cls.install_file("mrfast",MRFAST)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
