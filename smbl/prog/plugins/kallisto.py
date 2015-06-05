#
# TODO:
#  - fix linking error in CygWin
#

import smbl
import snakemake
import os

from ._program import *

from .cmake import *

KALLISTO  = get_bin_file_path("kallisto")


##########################################
##########################################


class Kallisto(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				KALLISTO,
			]

	@classmethod
	def depends_on(cls):
		return [
			CMake,
		]


	@classmethod
	def install(cls):
		gitdir=cls.git_clone("git://github.com/pachterlab/kallisto","kallisto")
		cls.run_cmake("kallisto")
		cls.run_make("kallisto")
		cls.install_file("kallisto/src/kallisto",KALLISTO)

	@classmethod
	def supported_platforms(cls):
		return []
		#["osx","linux","cygwin"]
