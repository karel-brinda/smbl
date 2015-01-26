import os

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


####################################################
####################################################

FA_EXAMPLE           = "example_fasta.fa"
FA_HG39              = "hg39.fa"

PROG_ART_454         = os.path.join(bin_dir,"art_454")
PROG_ART_ILLUMINA    = os.path.join(bin_dir,"art_illumina")
PROG_ART_SOLID       = os.path.join(bin_dir,"art_solid")
PROG_BCFTOOLS        = os.path.join(bin_dir,"bcftools")
PROG_BGZIP           = os.path.join(bin_dir,"bgzip")
PROG_BWA             = os.path.join(bin_dir,"bwa")
PROG_DWGSIM          = os.path.join(bin_dir,"dwgsim")
PROG_DWGSIM_EVAL     = os.path.join(bin_dir,"dwgsim_eval")
PROG_SAMTOOLS        = os.path.join(bin_dir,"samtools")
PROG_TABIX           = os.path.join(bin_dir,"tabix")
PROG_WGSIM           = os.path.join(bin_dir,"wgsim")
PROG_WGSIM_EVAL      = os.path.join(bin_dir,"wgsim_eval.pl")

####################################################
####################################################

ALL_FAS = (
		FA_EXAMPLE
	)

ALL_FAIS = ["{}.fai".format(fa) for fa in ALL_FAS]

ALL_PROGS = (
		PROG_DWGSIM,
		PROG_DWGSIM_EVAL,
		PROG_ART_454,
		PROG_ART_ILLUMINA,
		PROG_ART_SOLID,
		PROG_BCFTOOLS,
		PROG_BGZIP,
		PROG_BWA,
		PROG_SAMTOOLS,
		PROG_TABIX,
		PROG_WGSIM,
		PROG_WGSIM_EVAL
	)
