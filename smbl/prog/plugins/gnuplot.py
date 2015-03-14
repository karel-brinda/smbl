#
# TODO:
#  - fix CygWin error
#



import smbl
import snakemake
import os

import __program

GNUPLOT4 = __program.get_bin_file_path("gnuplot4")
GNUPLOT5 = __program.get_bin_file_path("gnuplot5")


##########################################
##########################################


class GnuPlot4(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				GNUPLOT4,
			]

	@classmethod
	def install(cls):
		fn=cls.download_file("http://sourceforge.net/projects/gnuplot/files/gnuplot/4.6.6/gnuplot-4.6.6.tar.gz/download","gnuplot.tar.gz")
		dir=cls.extract_tar(fn,strip=1)
		cls.run_configure(dir)
		cls.run_make(dir)
		cls.install_file("src/gnuplot",GNUPLOT4)

	@classmethod
	def supported_platforms(cls):
		return ["macos","linux"]


class GnuPlot5(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				GNUPLOT5,
			]

	@classmethod
	def install(cls):
		fn=cls.download_file("http://sourceforge.net/projects/gnuplot/files/gnuplot/5.0.0/gnuplot-5.0.0.tar.gz/download","gnuplot.tar.gz")
		dir=cls.extract_tar(fn,strip=1)
		cls.run_configure(dir)
		cls.run_make(dir)
		cls.install_file("src/gnuplot",GNUPLOT5)

	@classmethod
	def supported_platforms(cls):
		return ["macos","linux"]
