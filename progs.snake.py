include: "constants.py"

import os.path, shutil


# SamTools cannot be compiled on OpenSuse because it normally requires 
# the curses library instead of ncurses
def correct_samtools_make(makefile_fn):
	makefile_backup_fn = makefile_fn+".backup"
	if not os.path.isfile(makefile_backup_fn):
		with open(makefile_fn, 'r') as makefile:
			content = makefile.read()
			content = content.replace("-lcurses","-lncurses")
		with open(makefile_fn, 'w') as makefile:
			makefile.write(content)

rule __test_all_progs__:
	input:
		ALL_PROGS

rule prog_art:
	message:
		"Compiling ART"
	output:
		PROG_ART_ILLUMINA,
		PROG_ART_SOLID,
		PROG_ART_454
	params:
		url="http://www.niehs.nih.gov/research/resources/assets/docs/artsrcvanillaicecream031114linuxtgz.tgz",
		dir="art_src_VanillaIceCream_Linux"
	shell:
		"""
			mkdir -p src_ext
			cd src_ext
			curl -o art.tgz {params.url}
			tar xvf art.tgz
			cd {params.dir}
			./configure
			make
			cd ..
			cd ..
			cp src_ext/{params.dir}/art_illumina {output[0]}
			cp src_ext/{params.dir}/art_SOLiD {output[1]}
			cp src_ext/{params.dir}/art_454 {output[2]}
		"""

rule prog_bcftools:
	message:
		"Compiling BcfTools"
	output:
		PROG_BCFTOOLS
	shell:
		"""
			rm -fR src_ext/bcftools
			mkdir -p src_ext/bcftools
			cd src_ext/bcftools
			git clone --depth=1 http://github.com/samtools/bcftools
			git clone --depth=1 http://github.com/samtools/htslib
			cd bcftools
			make
			cd ../../..
			cp src_ext/bcftools/bcftools/bcftools {output[0]}
		"""

rule prog_dwgsim:
	message:
		"Compiling DwgSim"
	output:
		PROG_DWGSIM, PROG_DWGSIM_EVAL
	run:
		shell(
			"""
				mkdir -p src_ext
				cd src_ext
				rm -fR dwgsim
				git clone --depth=1 http://github.com/nh13/DWGSIM dwgsim
				cd dwgsim
				git submodule init
				git submodule update
				""")
		correct_samtools_make(os.path.join("src_ext","dwgsim","samtools","Makefile"))
		shell(
			"""
				cd src_ext/dwgsim
				make
				cd ../..
				cp src_ext/dwgsim/dwgsim {output[0]}
				cp src_ext/dwgsim/dwgsim_eval {output[1]}
			"""
		)

rule prog_wgsim:
	message:
		"Compiling WgSim"
	output:
		PROG_WGSIM, PROG_WGSIM_EVAL
	run:
		shell(
			"""
				mkdir -p src_ext
				cd src_ext
				rm -fR wgsim
				git clone --depth=1 http://github.com/lh3/wgsim
				cd wgsim
				gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm
				cd ../..
				cp src_ext/wgsim/wgsim {output[0]}
				cp src_ext/wgsim/wgsim_eval.pl {output[1]}
			"""
		)
# BWA
rule prog_bwa:
	message:
		"Compiling BWA "
	output:
		PROG_BWA
	shell:
		"""
			mkdir -p src_ext
			cd src_ext
			rm -fR bwa
			git clone --depth=1 http://github.com/lh3/bwa
			cd bwa
			make
			cd ../..
			cp src_ext/bwa/bwa {output[0]}
		"""

rule prog_htslib:
	message:
		"Compiling HtsLib"
	output:
		PROG_TABIX,
		PROG_BGZIP
	shell:
		"""
			rm -fR src_ext/htslib
			mkdir -p src_ext/htslib
			cd src_ext/htslib
			git clone --depth=1 --branch=develop http://github.com/samtools/bcftools
			git clone --depth=1 http://github.com/samtools/htslib
			cd htslib
			make
			cd ../../..
			cp src_ext/htslib/htslib/tabix {output[0]}
			cp src_ext/htslib/htslib/bgzip {output[1]}
		"""

rule prog_samtools:
	message:
		"Compiling SamTools"
	output:
		PROG_SAMTOOLS
	run:
		shell(
			"""
				rm -fR src_ext/samtools
				mkdir -p src_ext/samtools
				cd src_ext/samtools
				git clone --depth=1 http://github.com/samtools/samtools
				git clone --depth=1 http://github.com/samtools/htslib
			"""
		)
		correct_samtools_make("src_ext/samtools/samtools/Makefile")
		shell(
			"""
				cd src_ext/samtools/samtools
				make
				cd ../../..
				cp src_ext/samtools/samtools/samtools {output[0]}
			"""
		)
