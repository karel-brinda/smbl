import smbl
import snakemake
import os

import __program

WGSIM              = os.path.join(smbl.bin_dir,"wgsim")
WGSIM_EVAL         = os.path.join(smbl.bin_dir,"wgsim_eval.pl")


##########################################
##########################################


class WgSim(__program.Program):
	@staticmethod
	def get_files():
		return [
				WGSIM,
				WGSIM_EVAL,
			]

	@staticmethod
	def install():
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
				cd "{build_dir}" && make --jobs
				cp "{FROM[0]}" "{TO[0]}"
				cp "{FROM[1]}" "{TO[1]}"
				rm -fR "{src_dir}"
			'''.format(
					src_dir=src_dir,
					build_dir=build_dir,
					FROM=FROM,
					TO=TO,
				)
			)
