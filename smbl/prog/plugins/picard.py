import smbl
import snakemake
import os

from ._program import *

PICARD = get_bin_file_path("picard.jar")


##########################################
##########################################


class Picard(Program):
	@classmethod
	def get_installation_files(cls):
		return [
				PICARD,
			]

	@classmethod
	def install(cls):
		ver="1.133"
		fn=cls.download_file("https://github.com/broadinstitute/picard/releases/download/{ver}/picard-tools-{ver}.zip".format(ver=ver),"picard.zip")
		dir=os.path.dirname(fn)
		smbl.utils.shell('(cd "{dir}" && unzip -j picard.zip) > /dev/null'.format(dir=dir))
		cls.install_file("picard.jar",PICARD)

	@classmethod
	def supported_platforms(cls):
		return ["osx","linux","cygwin"]
