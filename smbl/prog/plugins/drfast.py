import smbl
import snakemake
import os

import __program

DRFAST = __program.get_bin_file_path("drfast")


##########################################
##########################################


class DrFast(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				DRFAST,
			]

	@classmethod
	def install(cls):
		cls.git_clone("http://github.com/BilkentCompGen/drfast","")
		cls.run_make("")
		cls.install_file("drfast",DRFAST)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
