import smbl
import snakemake
import os

import __program

WGSIM              = __program.get_bin_file_path("wgsim")
WGSIM_EVAL         = __program.get_bin_file_path("wgsim_eval.pl")


##########################################
##########################################


class WgSim(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				WGSIM,
				WGSIM_EVAL,
			]

	@classmethod
	def install(cls):
		src_dir=os.path.join(smbl.src_dir,"wgsim")
		build_dir=os.path.join(src_dir,"wgsim")

		FROM=[
				os.path.join(build_dir,"wgsim"),
				os.path.join(build_dir,"wgsim_eval.pl"),
			]
		TO = WgSim.get_files()


		smbl.run_commands(
			'''
				rm -fR "{src_dir}"
				mkdir -p "{build_dir}"
				git clone --depth=1 http://github.com/lh3/wgsim "{build_dir}"
				cd "{build_dir}" && gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm
				cp "{FROM[0]}" "{TO[0]}"
				cp "{FROM[1]}" "{TO[1]}"
				rm -fR "{src_dir}"
			'''.format(
					src_dir=src_dir,
					build_dir=build_dir,
					FROM=FROM,
					TO=TO,
				),
			)
