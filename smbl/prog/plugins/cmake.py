import smbl
import snakemake
import os

from ._program import *

CMAKE = get_bin_file_path("cmake")


##########################################
##########################################


class CMake(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				CMAKE,
			]

	@classmethod
	def install(cls):
		fn=cls.download_file("http://www.cmake.org/files/v3.2/cmake-3.2.3.tar.gz","cmake.tar.gz")
		dir=cls.extract_tar(fn,strip=1)
		cls.shell('cd "{dir}" && ./bootstrap --prefix="{install_dir}"'.format(dir=dir,install_dir=smbl.smbl_dir))
		cls.run_make("")
		print("install")
		cls.shell('cd "{dir}" && make install'.format(dir=dir))

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
