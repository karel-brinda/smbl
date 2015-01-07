import os.path, shutil
	
#
# PROGRAMS
#

EXAMPLE_FASTA   = "example_fasta.fa"

#USE_HOME=1

# use user's home directory (to share the already compiled programs)?

try:
	USE_HOME
except NameError:
	USE_HOME=False

if USE_HOME:
	bin_dir = os.path.join(os.path.expanduser("~"),".snakemake-lib","bin")
else:
	bin_dir = "bin"

print("directory for programs: ",bin_dir)

ART_454         = os.path.join(bin_dir,"art_454")
ART_ILLUMINA    = os.path.join(bin_dir,"art_illumina")
ART_SOLID       = os.path.join(bin_dir,"art_solid")
BCFTOOLS        = os.path.join(bin_dir,"bcftools")
BGZIP           = os.path.join(bin_dir,"bgzip")
BWA             = os.path.join(bin_dir,"bwa")
DWGSIM          = os.path.join(bin_dir,"dwgsim")
SAMTOOLS        = os.path.join(bin_dir,"samtools")
TABIX           = os.path.join(bin_dir,"tabix")


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

rule __test_all__:
	input:
		(
			DWGSIM,
			EXAMPLE_FASTA,
			ART_454,
			ART_ILLUMINA,
			ART_SOLID,
			BCFTOOLS,
			BGZIP,
			BWA,
			SAMTOOLS,
			TABIX
		)

rule example_fasta:
	output:
		EXAMPLE_FASTA
	shell:
		"""
		curl --insecure -o {output[0]} ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Mycobacterium_tuberculosis_H37Rv_uid170532/NC_018143.fna
		"""

rule prog_art:
	message:
		"Compiling ART"
	output:
		ART_ILLUMINA,
		ART_SOLID,
		ART_454
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
		BCFTOOLS
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
		DWGSIM
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
			"""
		)

# BWA
rule prog_bwa:
	message:
		"Compiling BWA "
	output:
		BWA
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
		TABIX,
		BGZIP
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
		SAMTOOLS
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
