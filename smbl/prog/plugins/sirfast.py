import smbl
import snakemake
import os

import __program

SIRFAST = __program.get_bin_file_path("sirfast")


##########################################
##########################################


class SirFast(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				SIRFAST,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("http://github.com/BilkentCompGen/sirfast","")
		cls.run_make("")
		cls.install_file("sirfast",SIRFAST)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]