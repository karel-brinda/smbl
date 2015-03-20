import smbl
import snakemake
import os

import _program

CMAKE = _program.get_bin_file_path("cmake")


##########################################
##########################################


class CMake(_program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				CMAKE,
			]

	@classmethod
	def install(cls):
		fn=cls.download_file("http://www.cmake.org/files/v3.2/cmake-3.2.1.tar.gz","cmake.tar.gz")
		dir=cls.extract_tar(fn,strip=1)
		snakemake.shell('(cd "{dir}" && ./bootstrap --prefix="{install_dir}") > /dev/null'.format(dir=dir,install_dir=smbl.smbl_dir))
		cls.run_make("")
		print("install")
		snakemake.shell('(cd "{dir}" && make install) > /dev/null'.format(dir=dir))
		#cls.install_file("bin/cmake",CMAKE)



	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
