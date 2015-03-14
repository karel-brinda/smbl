import smbl
import snakemake
import os

import __program

BFAST = __program.get_bin_file_path("bfast")


##########################################
##########################################


class BFast(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				BFAST,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("http://github.com/nh13/bfast","")
		snakemake.shell('(cd "{}" && sh autogen.sh) > /dev/null'.format(cls.src_dir))
		cls.run_configure("")
		cls.run_make("")
		cls.install_file("bfast/bfast",BFAST)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
