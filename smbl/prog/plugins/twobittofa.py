import smbl
import snakemake
import os

import _program

TWOBITTOFA = _program.get_bin_file_path("twoBitToFa")


##########################################
##########################################


class TwoBitToFa(_program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				TWOBITTOFA
			]

	@classmethod
	def install(cls):
		if smbl.is_linux() and smbl.is_os_64bit():
			url="http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa"
		elif smbl.is_osx() and smbl.is_os_64bit():
			url="http://hgdownload.cse.ucsc.edu/admin/exe/macOSX.x86_64/twoBitToFa"
		elif smbl.is_osx():
			url="http://hgdownload.cse.ucsc.edu/admin/exe/macOSX.i386/twoBitToFa"
		else:
			smbl.messages.error("Operating system '{}' is not supported".format(smbl.get_platform()),program="SMBL")
			raise NotImplementedError("Unsupported OS")

		cls.download_file(url,"twoBitToFa")
		cls.install_file("twoBitToFa",TWOBITTOFA)

	@classmethod
	def supported_platforms(cls):
		return ["osx","linux"]
