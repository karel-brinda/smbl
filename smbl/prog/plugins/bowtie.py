import smbl
import snakemake
import os

import __program

BOWTIE2            = __program.get_bin_file_path("bowtie2")
BOWTIE2_ALIGN_L    = __program.get_bin_file_path("bowtie2-align-l")
BOWTIE2_ALIGN_S    = __program.get_bin_file_path("bowtie2-align-s")
BOWTIE2_BUILD      = __program.get_bin_file_path("bowtie2-build")
BOWTIE2_BUILD_L    = __program.get_bin_file_path("bowtie2-build-l")
BOWTIE2_BUILD_S    = __program.get_bin_file_path("bowtie2-build-s")
BOWTIE2_INSPECT    = __program.get_bin_file_path("bowtie2-inspect")
BOWTIE2_INSPECT_L  = __program.get_bin_file_path("bowtie2-inspect-l")
BOWTIE2_INSPECT_S  = __program.get_bin_file_path("bowtie2-inspect-s")


##########################################
##########################################


class Bowtie2(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				BOWTIE2,
				BOWTIE2_ALIGN_L,
				BOWTIE2_ALIGN_S,
				BOWTIE2_BUILD,
				BOWTIE2_BUILD_L,
				BOWTIE2_BUILD_S,
				BOWTIE2_INSPECT,
				BOWTIE2_INSPECT_L,
				BOWTIE2_INSPECT_S,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("http://github.com/BenLangmead/bowtie2","")
		cls.run_make("")
		cls.install_file("bowtie2",BOWTIE2)
		cls.install_file("bowtie2-align-l",BOWTIE2_ALIGN_L)
		cls.install_file("bowtie2-align-s",BOWTIE2_ALIGN_S)
		cls.install_file("bowtie2-build",BOWTIE2_BUILD)
		cls.install_file("bowtie2-build-l",BOWTIE2_BUILD_L)
		cls.install_file("bowtie2-build-s",BOWTIE2_BUILD_S)
		cls.install_file("bowtie2-inspect",BOWTIE2_INSPECT)
		cls.install_file("bowtie2-inspect-l",BOWTIE2_INSPECT_L)
		cls.install_file("bowtie2-inspect-s",BOWTIE2_INSPECT_S)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
