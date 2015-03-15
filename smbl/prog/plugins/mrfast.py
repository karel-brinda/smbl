import smbl
import snakemake
import os

import __program

MRFAST = __program.get_bin_file_path("mrfast")


##########################################
##########################################


class MrFast(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				MRFAST,
			]

	@classmethod
	def install(cls):
		cls.git_clone("http://github.com/BilkentCompGen/mrfast","")
		cls.run_make("")
		cls.install_file("mrfast",MRFAST)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
