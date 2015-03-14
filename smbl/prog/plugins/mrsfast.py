import smbl
import snakemake
import os

import __program

MRSFAST = __program.get_bin_file_path("mrsfast")


##########################################
##########################################


class MrsFast(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				MRSFAST,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("git://git.code.sf.net/p/mrsfast/code","")
		cls.run_make("",parallel=False)
		cls.install_file("mrsfast",MRSFAST)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
