import smbl
import snakemake
import os

import __program

STORM_NUCLEOTIDE = __program.get_bin_file_path("storm-nucleotide")
STORM_COLOR      = __program.get_bin_file_path("storm-color")


##########################################
##########################################


class Storm(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				STORM_NUCLEOTIDE,
				STORM_COLOR,
			]

	@classmethod
	def install(cls):
		cls.svn_checkout("svn://scm.gforge.inria.fr/svnroot/storm/trunk","")
		cls.run_make("")
		cls.install_file("storm-color",STORM_COLOR)
		cls.install_file("storm-nucleotide",STORM_NUCLEOTIDE)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
