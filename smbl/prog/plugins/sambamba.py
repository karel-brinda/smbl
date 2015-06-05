import smbl
import snakemake
import os

from ._program import *

SAMBAMBA = get_bin_file_path("sambamba")


##########################################
##########################################


class SamBamBa(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				SAMBAMBA,
			]

	@classmethod
	def install(cls):
		version="v0.5.4"

		if smbl.utils.is_linux():
			fn=cls.download_file("http://github.com/lomereiter/sambamba/releases/download/{ver}/sambamba_{ver}_linux.tar.bz2".format(ver=version),"sambamba.tar.bz2")
		elif smbl.utils.is_osx():
			fn=cls.download_file("http://github.com/lomereiter/sambamba/releases/download/{ver}/sambamba_{ver}_osx.tar.bz2".format(ver=version),"sambamba.tar.bz2")
		else:
			smbl.messages.error("Operating system '{}' is not supported".format(smbl.utils.get_platform()),program="SMBL")
			raise NotImplementedError("Unsupported OS")
		dir=cls.extract_tar(fn)

		cls.install_file("sambamba_{ver}".format(ver=version),SAMBAMBA)

	@classmethod
	def supported_platforms(cls):
		return ["osx","linux"]
