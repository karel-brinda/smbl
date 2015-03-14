import smbl
import snakemake
import os

import __program

LASTAL = __program.get_bin_file_path("lastal")
LASTDB = __program.get_bin_file_path("lastdb")


##########################################
##########################################


class Last(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				LASTAL,
				LASTDB,
			]

	@classmethod
	def install(cls):
		last_version="last-548"
		fn=cls.download_file("http://last.cbrc.jp/{}".format(last_version),"last.zip")
		dir=os.path.dirname(fn)
		snakemake.shell("cd {dir} && unzip last.zip")
		snakemake.shell("mv {} {}".format(
				os.path.join(dir,last_version,"*"),
				dir
			))
		cls.run_make(dir)
		cls.install_file("src/lastal",LASTAL)
		cls.install_file("src/lastdb",LASTDB)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","macos","linux"]
