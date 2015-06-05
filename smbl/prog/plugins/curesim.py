import smbl
import snakemake
import os

from ._program import *

CURESIM = get_bin_file_path("CuReSim.jar")
CURESIM_EVAL = get_bin_file_path("CuReSimEval.jar")


##########################################
##########################################


class CuReSim(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				CURESIM,
				CURESIM_EVAL,
			]

	@classmethod
	def install(cls):
		fn1=cls.download_file("http://www.pegase-biosciences.com/wp-content/uploads/2013/04/CuReSim1.2.zip","curesim.zip")
		fn2=cls.download_file("http://www.pegase-biosciences.com/wp-content/uploads/2013/04/CuReSimEval1.1.zip","curesim_eval.zip")
		dir=os.path.dirname(fn1)
		smbl.utils.shell('(cd "{dir}" && unzip -j -o curesim.zip && unzip -j -o curesim_eval.zip) > /dev/null'.format(dir=dir))
		cls.install_file("CuReSim.jar",CURESIM)
		cls.install_file("CuReSimEval.jar",CURESIM_EVAL)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
