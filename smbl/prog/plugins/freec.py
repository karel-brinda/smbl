import smbl
import snakemake
import os

from ._program import *

FREEC = get_bin_file_path("freec")


##########################################
##########################################


class Freec(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				FREEC,
			]

	@classmethod
	def install(cls):
		fn=cls.download_file("http://bioinfo-out.curie.fr/projects/freec/src/FREEC_Linux64.tar.gz","freec.tar.gz")
		dir=cls.extract_tar(fn)
		cls.run_make(dir,clean=True)
		cls.install_file("freec",FREEC)

	@classmethod
	def supported_platforms(cls):
		return ["linux"]
