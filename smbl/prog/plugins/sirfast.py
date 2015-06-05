import smbl
import snakemake
import os

from ._program import *

SIRFAST = get_bin_file_path("sirfast")


##########################################
##########################################


class SirFast(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				SIRFAST,
			]

	@classmethod
	def install(cls):
		cls.git_clone("git://github.com/BilkentCompGen/sirfast","")
		cls.run_make("")
		cls.install_file("sirfast",SIRFAST)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
