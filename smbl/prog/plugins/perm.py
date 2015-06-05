import smbl
import snakemake
import os

from ._program import *

PERM = get_bin_file_path("perm")


##########################################
##########################################


class PerM(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				PERM,
			]

	@classmethod
	def install(cls):
		if (smbl.utils.is_linux()):
			fn=cls.download_file("https://perm.googlecode.com/files/PerM4_Linux64.gz","perm.gz")
			cls.extract_gz(fn)
			cls.install_file("perm",PERM)
		elif (smbl.utils.is_osx()):
			fn=cls.download_file("https://perm.googlecode.com/files/PerM4_Mac64.tar.gz","perm.tar.gz")
			cls.extract_tar(fn,strip=0)
			cls.install_file("perm",PERM)
		elif (smbl.utils.is_cygwin()):
			fn=cls.download_file("https://perm.googlecode.com/files/PerM4_Win32.zip","perm.zip")
			cls.extract_zip(fn)
			cls.install_file("perm.exe",PERM)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
