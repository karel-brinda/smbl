import smbl
import snakemake
import os

from ._program import *

BFAST = get_bin_file_path("bfast")

#todo: mapping commands from http://genome.jouy.inra.fr/ngs/mapping/


##########################################
##########################################


class BFast(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				BFAST,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("git://github.com/nh13/bfast","")
		smbl.utils.shell('(cd "{}" && sh autogen.sh) > /dev/null'.format(cls.src_dir))
		cls.run_configure("")
		cls.run_make("")
		cls.install_file("bfast/bfast",BFAST)

	@classmethod
	def supported_platforms(cls):
		return ["linux"]
