import smbl
import snakemake
import os

import __program

MASON_FRAG_SEQUENCING   = __program.get_bin_file_path("mason_frag_sequencing")
MASON_GENOME            = __program.get_bin_file_path("mason_genome")
MASON_MATERIALIZER      = __program.get_bin_file_path("mason_materializer")
MASON_METHYLATION       = __program.get_bin_file_path("mason_methylation")
MASON_SIMULATOR         = __program.get_bin_file_path("mason_simulator")
MASON_SPLICING          = __program.get_bin_file_path("mason_splicing")
MASON_VARIATOR          = __program.get_bin_file_path("mason_variator")


##########################################
##########################################


class Mason2(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				MASON_FRAG_SEQUENCING,
				MASON_GENOME,
				MASON_MATERIALIZER,
				MASON_METHYLATION,
				MASON_SIMULATOR,
				MASON_SPLICING,
				MASON_VARIATOR,
			]

	@classmethod
	def install(cls):
		if smbl.is_linux() and smbl.is_os_64bit():
			fn=cls.download_file("http://packages.seqan.de/mason2/mason2-2.0.0-Linux-x86_64.tar.bz2","mason.tar.bz2")
		elif smbl.is_linux():
			fn=cls.download_file("http://packages.seqan.de/mason2/mason2-2.0.0-Linux-i686.tar.bz2","mason.tar.bz2")
		elif smbl.is_mac() and smbl.is_os_64bit():
			fn=cls.download_file("http://packages.seqan.de/mason2/mason2-2.0.0-Mac-x86_64.tar.bz2","mason.tar.bz2")
		elif smbl.is_mac():
			fn=cls.download_file("http://packages.seqan.de/mason2/mason2-2.0.0-Mac-i686.tar.bz2","mason.tar.bz2")
		else:
			raise NotImplementedError("Unsupported OS")

		dir=cls.extract_tar(fn,strip=2)

		cls.install_file("mason_frag_sequencing",MASON_FRAG_SEQUENCING)
		cls.install_file("mason_genome",MASON_GENOME)
		cls.install_file("mason_materializer",MASON_MATERIALIZER)
		cls.install_file("mason_methylation",MASON_METHYLATION)
		cls.install_file("mason_simulator",MASON_SIMULATOR)
		cls.install_file("mason_splicing",MASON_SPLICING)
		cls.install_file("mason_variator",MASON_VARIATOR)

	@classmethod
	def supported_platforms(cls):
		return ["macos","linux"]
