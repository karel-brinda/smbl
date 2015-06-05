import smbl
import snakemake
import os

from ._program import *

ART_454      = get_bin_file_path("art_454")
ART_ILLUMINA = get_bin_file_path("art_illumina")
ART_SOLID    = get_bin_file_path("art_solid")


##########################################
##########################################


class Art(Program):
	@classmethod
	def get_installation_files(cls):
		return [
			ART_454,
			ART_ILLUMINA,
			ART_SOLID,
		]

	@classmethod
	def install(cls):
		if smbl.utils.is_linux()  and smbl.utils.is_os_64bit():
			fn=cls.download_file("http://www.niehs.nih.gov/research/resources/assets/docs/artbinchocolatecherrycake031915linux64tgz.tgz","art.tgz")
		elif smbl.utils.is_linux():
			fn=cls.download_file("http://www.niehs.nih.gov/research/resources/assets/docs/artbinchocolatecherrycake031915linux32tgz.tgz","art.tgz")
		elif smbl.utils.is_osx() and smbl.utils.is_os_64bit():
			fn=cls.download_file("http://www.niehs.nih.gov/research/resources/assets/docs/artbinchocolatecherrycake031915macos64tgz.tgz","art.tgz")
		elif smbl.utils.is_osx():
			fn=cls.download_file("http://www.niehs.nih.gov/research/resources/assets/docs/artbinchocolatecherrycake031915macos32tgz.tgz","art.tgz")
		else:
			smbl.messages.error("Operating system '{}' is not supported".format(smbl.utils.get_platform()),program="SMBL")
			raise NotImplementedError("Unsupported OS")

		dir=cls.extract_tar(fn,strip=2)

		cls.install_file("art_454",ART_454)
		cls.install_file("art_illumina",ART_ILLUMINA)
		cls.install_file("art_SOLiD",ART_SOLID)

	@classmethod
	def supported_platforms(cls):
		return ["osx","linux"]
