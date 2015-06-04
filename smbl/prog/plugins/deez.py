import smbl
import snakemake
import os

from ._program import *

DEEZ = os.path.join(smbl.bin_dir,"deez")


##########################################
##########################################


class Deez(Program):

	@classmethod
	def get_installation_files(cls):
		return [DEEZ]

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]

	@classmethod
	def install(cls):
		cls.git_clone("git://github.com/sfu-compbio/deez","deez")
		cls.run_make("deez")
		cls.install_file("deez/deez",DEEZ)
