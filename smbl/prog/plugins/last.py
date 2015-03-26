import smbl
import snakemake
import os

import _program

LASTAL = _program.get_bin_file_path("lastal")
LASTDB = _program.get_bin_file_path("lastdb")


##########################################
##########################################


class Last(_program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				LASTAL,
				LASTDB,
			]

	@classmethod
	def install(cls):
		last_version="last-548"
		fn=cls.download_file("http://last.cbrc.jp/{}.zip".format(last_version),"last.zip")
		dir1=os.path.dirname(fn)
		snakemake.shell('(cd "{dir1}" && unzip last.zip)')
		dir2=os.path.join(dir1,last_version)
		cls.run_make(dir2)
		cls.install_file("{}/src/lastal".format(dir2),LASTAL)
		cls.install_file("{}/src/lastdb".format(dir2),LASTDB)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]
