import smbl
import snakemake
import os

import _program

PERM = _program.get_bin_file_path("perm")


##########################################
##########################################


class PerM(_program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				PERM,
			]

	@classmethod
	def install(cls):
		fn=cls.download_file("https://perm.googlecode.com/files/PerM4Source.tar.gz","perm.tar.gz")
		dir=cls.extract_tar(fn,strip=2)
		cls.run_make(dir)
		cls.install_file("perm",PERM)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
