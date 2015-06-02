import smbl
import snakemake
import os

from ._program import *

PBSIM = get_bin_file_path("pbsim")


##########################################
##########################################


class PbSim(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				PBSIM,
			]

	@classmethod
	def install(cls):
		fn=cls.download_file("https://pbsim.googlecode.com/files/pbsim-1.0.3.tar.gz","pbsim.tar.gz")
		dir=cls.extract_tar(fn,strip=1)
		cls.run_configure(dir)
		cls.run_make(dir)
		cls.install_file("src/pbsim",PBSIM)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
