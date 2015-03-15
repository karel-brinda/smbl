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
		if smbl.is_linux() and smbl.is_os_64bit:
			cls.download_file("http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa",TWOBITTOFA)
			url=""
		elif smbl.is_mac() and smbl.is_os_64bit:
			cls.download_file("http://hgdownload.cse.ucsc.edu/admin/exe/macOSX.x86_64/twoBitToFa",TWOBITTOFA)
			url=""
		elif smbl.is_mac():
			cls.download_file("http://hgdownload.cse.ucsc.edu/admin/exe/macOSX.i386/twoBitToFa",TWOBITTOFA)
		else:
			raise NotImplementedError("For your OS, twoBitToFa is not precompiled")


	@classmethod
	def supported_platforms(cls):
		return ["macos","linux"]
